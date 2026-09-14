#!/usr/bin/env python3
"""ITER061 RC008 companion refinement-complex/gluing authority audit.

Preregistered source-authority test only.  No amplitude or RG computation is
performed here.  Each scientific lane fetches and normalizes the same frozen
Frontiers companion endpoint independently.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

URL = "https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2020.00295/full"
DOI = "10.3389/fphy.2020.00295"
TARGET_TITLE = "Hypercuboidal renormalization in spin foam quantum gravity"
LANES = (
    "source-identity",
    "cuboid-complex",
    "embedding-relation",
    "amplitude-blocking",
    "observable-comparator",
    "null-controls",
)


def fetch_source() -> Tuple[str, Dict[str, Any]]:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "Chrome/150.0 Safari/537.36 ISQGR-source-audit/ITER061"
        ),
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.8",
    }
    last: Exception | None = None
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(URL, headers=headers)
            with urllib.request.urlopen(req, timeout=45) as resp:
                raw = resp.read()
                status = getattr(resp, "status", 200)
                final_url = resp.geturl()
                ctype = resp.headers.get("Content-Type", "")
            text = raw.decode("utf-8", errors="replace")
            return text, {
                "requested_url": URL,
                "final_url": final_url,
                "http_status": status,
                "content_type": ctype,
                "raw_sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
                "attempt": attempt,
            }
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
            last = exc
            if attempt < 3:
                time.sleep(2 ** (attempt - 1))
    raise RuntimeError(f"frozen endpoint retrieval failed after 3 attempts: {last!r}")


def normalize_source(raw_html: str) -> str:
    text = re.sub(r"(?is)<script\b[^>]*>.*?</script>", " ", raw_html)
    text = re.sub(r"(?is)<style\b[^>]*>.*?</style>", " ", text)
    text = re.sub(r"(?is)<noscript\b[^>]*>.*?</noscript>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u00a0", " ")
    return re.sub(r"\s+", " ", text).strip()


def search(text: str, pattern: str, flags: int = re.IGNORECASE) -> re.Match[str] | None:
    return re.search(pattern, text, flags)


def all_terms(text: str, terms: Iterable[str]) -> bool:
    low = text.casefold()
    return all(term.casefold() in low for term in terms)


def context(text: str, pattern: str, radius: int = 260) -> Dict[str, Any]:
    m = search(text, pattern)
    if not m:
        return {"found": False, "pattern": pattern, "offset": None, "context": ""}
    lo = max(0, m.start() - radius)
    hi = min(len(text), m.end() + radius)
    return {
        "found": True,
        "pattern": pattern,
        "offset": m.start(),
        "context": text[lo:hi],
    }


def window(text: str, anchor: str, before: int = 500, after: int = 2200) -> str:
    m = search(text, anchor)
    if not m:
        return ""
    return text[max(0, m.start() - before): min(len(text), m.start() + after)]


def predicate_source_identity(text: str) -> Tuple[Dict[str, bool], Dict[str, Any]]:
    title_pat = r"Coarse Graining Spin Foam Quantum Gravity\s*[—–-]\s*A Review"
    author_pat = r"Sebastian\s+Steinhaus"
    target_pat = r"Hypercuboidal renormalization in spin foam quantum gravity"
    target_meta_pat = r"Phys\s*Rev\s*D\s*\.?\s*\(\s*2017\s*\)\s*95\s*:\s*126006"
    cuboid = window(text, r"setup for coarse graining in the quantum cuboid model", 300, 1100)
    checks = {
        "companion_title": bool(search(text, title_pat)),
        "companion_author": bool(search(text, author_pat)),
        "companion_doi": DOI in text,
        "target_reference_title": bool(search(text, target_pat)),
        "target_reference_metadata": bool(search(text, target_meta_pat)),
        "cuboid_attributed_to_bahr_steinhaus_source_work": bool(
            cuboid
            and "quantum cuboid model" in cuboid.casefold()
            and "steinhaus" in cuboid.casefold()
            and ("[112" in cuboid or "112" in cuboid)
        ),
    }
    ev = {
        "title": context(text, title_pat),
        "doi": context(text, re.escape(DOI)),
        "target_reference": context(text, target_pat),
        "cuboid_attribution": context(text, r"setup for coarse graining in the quantum cuboid model"),
    }
    return checks, ev


def predicate_cuboid_complex(text: str) -> Tuple[Dict[str, bool], Dict[str, Any]]:
    cuboid = window(text, r"setup for coarse graining in the quantum cuboid model", 500, 2500)
    checks = {
        "two_hypercuboids_common_3d_cuboid": bool(search(cuboid, r"two hypercuboids glued together along a common 3D cuboid")),
        "fixed_coarse_boundary_geometry": bool(
            search(cuboid, r"total geometry of both hypercuboids is fixed in the coarse boundary state")
            and search(cuboid, r"total area of each coarse face is fixed")
        ),
        "coarse_and_fine_same_observable": bool(
            search(cuboid, r"variance.*?coarse.*?coarse and.*?fine case", re.IGNORECASE | re.DOTALL)
            or search(cuboid, r"variance of the 4-volume is computed in both the coarse and fine case")
        ),
        "each_hypercuboid_subdivided_16": bool(search(cuboid, r"each of the hypercuboids is subdivided into 16")),
    }
    ev = {
        "common_gluing": context(cuboid, r"two hypercuboids glued together along a common 3D cuboid"),
        "fixed_boundary": context(cuboid, r"total geometry of both hypercuboids is fixed in the coarse boundary state"),
        "subdivision": context(cuboid, r"each of the hypercuboids is subdivided into 16"),
        "coarse_fine_observable": context(cuboid, r"variance of the 4-volume is computed in both the coarse and fine case"),
    }
    return checks, ev


def predicate_embedding_relation(text: str) -> Tuple[Dict[str, bool], Dict[str, Any]]:
    setup = window(text, r"Coarse Graining Setup and Results", 100, 4400)
    checks = {
        "geometric_embedding_prescribed": bool(search(setup, r"geometric embedding map is prescribed")),
        "fine_areas_sum_to_coarse_area": bool(search(setup, r"fine areas sum up to the coarse area")),
        "fine_to_coarse_alpha_flow": bool(
            search(setup, r"defines the flow.*?from fine.*?to coarse", re.IGNORECASE | re.DOTALL)
            and ("α" in setup or "alpha" in setup.casefold())
        ),
    }
    ev = {
        "embedding": context(setup, r"geometric embedding map is prescribed"),
        "area_relation": context(setup, r"fine areas sum up to the coarse area"),
        "flow_direction": context(setup, r"defines the flow.*?from fine.*?to coarse"),
    }
    return checks, ev


def predicate_amplitude_blocking(text: str) -> Tuple[Dict[str, bool], Dict[str, Any]]:
    block = window(text, r"blocking of amplitudes", 650, 2600)
    checks = {
        "hypercubic_16_vertex_blocking": bool(search(block, r"blocking of amplitudes.*?16 vertex amplitudes.*?hypercubic combinatorics", re.IGNORECASE | re.DOTALL)),
        "boundary_bulk_split": bool(
            search(block, r"split into two groups")
            and search(block, r"boundary degrees of freedom")
            and search(block, r"block [\"“”']?bulk[\"“”']? degrees of freedom")
        ),
        "bulk_labels_summed": bool(search(block, r"bulk[\"“”']? degrees of freedom.*?summed over", re.IGNORECASE | re.DOTALL)),
        "fine_amplitude_defined": bool(search(block, r"summarized as the fine amplitude")),
        "embedding_defines_effective_amplitude": bool(
            search(block, r"embedding maps.*?derive the effective amplitude", re.IGNORECASE | re.DOTALL)
            or search(block, r"embedding maps.*?define an effective amplitude", re.IGNORECASE | re.DOTALL)
        ),
    }
    ev = {
        "blocking": context(block, r"blocking of amplitudes.*?16 vertex amplitudes.*?hypercubic combinatorics"),
        "boundary_bulk": context(block, r"split into two groups"),
        "bulk_sum": context(block, r"bulk[\"“”']? degrees of freedom.*?summed over"),
        "effective_amplitude": context(block, r"embedding maps.*?derive the effective amplitude"),
    }
    return checks, ev


def predicate_observable(text: str) -> Tuple[Dict[str, bool], Dict[str, Any]]:
    setup = window(text, r"setup for coarse graining in the quantum cuboid model", 900, 3200)
    checks = {
        "fixed_coarse_boundary_state": bool(search(setup, r"fixed coarse boundary state")),
        "four_volume_variance_coarse_and_fine": bool(search(setup, r"variance of the 4-volume is computed in both the coarse and fine case")),
        "observable_defines_flow_fixed_point": bool(
            search(setup, r"fixed point of the renormalization group flow")
            and search(setup, r"flow.*?from fine.*?to coarse", re.IGNORECASE | re.DOTALL)
        ),
    }
    ev = {
        "fixed_boundary": context(setup, r"fixed coarse boundary state"),
        "four_volume": context(setup, r"variance of the 4-volume is computed in both the coarse and fine case"),
        "fixed_point": context(setup, r"fixed point of the renormalization group flow"),
    }
    return checks, ev


def mutate_once(text: str, pattern: str, replacement: str = "[NULL_REMOVED]") -> Tuple[str, bool]:
    out, n = re.subn(pattern, replacement, text, count=1, flags=re.IGNORECASE)
    return out, n == 1


def predicate_null_controls(text: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    controls: List[Dict[str, Any]] = []

    t1, applied1 = mutate_once(text, r"each of the hypercuboids is subdivided into 16")
    c1, _ = predicate_cuboid_complex(t1)
    controls.append({"name": "remove_subdivision_16", "mutation_applied": applied1, "detected": applied1 and not c1["each_hypercuboid_subdivided_16"]})

    t2, applied2 = mutate_once(text, r"fine areas sum up to the coarse area")
    c2, _ = predicate_embedding_relation(t2)
    controls.append({"name": "corrupt_area_sum", "mutation_applied": applied2, "detected": applied2 and not c2["fine_areas_sum_to_coarse_area"]})

    t3, applied3 = mutate_once(text, r"two hypercuboids glued together along a common 3D cuboid")
    c3, _ = predicate_cuboid_complex(t3)
    controls.append({"name": "remove_common_cuboid_gluing", "mutation_applied": applied3, "detected": applied3 and not c3["two_hypercuboids_common_3d_cuboid"]})

    t4, applied4 = mutate_once(text, r"block [\"“”']?bulk[\"“”']? degrees of freedom[^.]{0,180}?summed over")
    c4, _ = predicate_amplitude_blocking(t4)
    controls.append({"name": "remove_bulk_internal_summation", "mutation_applied": applied4, "detected": applied4 and not c4["bulk_labels_summed"]})

    t5, applied5 = mutate_once(text, re.escape(TARGET_TITLE))
    c5, _ = predicate_source_identity(t5)
    controls.append({"name": "replace_target_reference", "mutation_applied": applied5, "detected": applied5 and not c5["target_reference_title"]})

    detected = sum(1 for c in controls if c["detected"])
    applied = sum(1 for c in controls if c["mutation_applied"])
    checks: Dict[str, Any] = {
        "controls_applied": applied,
        "controls_detected": detected,
        "minimum_detected": 4,
        "pass": applied == 5 and detected >= 4,
        "controls": controls,
    }
    return checks, {"controls": controls}


def lane_eval(lane: str, text: str) -> Tuple[Dict[str, Any], Dict[str, Any], bool]:
    if lane == "source-identity":
        checks, ev = predicate_source_identity(text)
        return checks, ev, all(checks.values())
    if lane == "cuboid-complex":
        checks, ev = predicate_cuboid_complex(text)
        return checks, ev, all(checks.values())
    if lane == "embedding-relation":
        checks, ev = predicate_embedding_relation(text)
        return checks, ev, all(checks.values())
    if lane == "amplitude-blocking":
        checks, ev = predicate_amplitude_blocking(text)
        return checks, ev, all(checks.values())
    if lane == "observable-comparator":
        checks, ev = predicate_observable(text)
        return checks, ev, all(checks.values())
    if lane == "null-controls":
        checks, ev = predicate_null_controls(text)
        return checks, ev, bool(checks["pass"])
    raise ValueError(lane)


def run_lane(lane: str, out: Path) -> int:
    payload: Dict[str, Any] = {
        "iteration": "ITER061",
        "lane": lane,
        "frozen_source_url": URL,
        "classification_scope": "source-authority-only",
    }
    try:
        raw, provenance = fetch_source()
        text = normalize_source(raw)
        payload["retrieval"] = provenance
        payload["normalized_sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
        payload["normalized_chars"] = len(text)
        checks, evidence, lane_pass = lane_eval(lane, text)
        payload["checks"] = checks
        payload["evidence"] = evidence
        payload["lane_pass"] = lane_pass
        payload["lane_status"] = "PASS" if lane_pass else "BLOCKED_SOURCE_AUTHORITY"
    except Exception as exc:
        payload["lane_pass"] = False
        payload["lane_status"] = "INFRASTRUCTURE_FAIL"
        payload["error"] = repr(exc)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    # Keep artifact production reliable even for scientific BLOCKED/INFRA lanes.
    return 0


def find_lane_file(root: Path, lane: str) -> Path | None:
    candidates = sorted(root.rglob("evidence.json")) + sorted(root.rglob(f"{lane}.json"))
    for p in candidates:
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if obj.get("lane") == lane:
            return p
    return None


def aggregate(root: Path, out: Path) -> int:
    lanes: Dict[str, Dict[str, Any]] = {}
    missing: List[str] = []
    for lane in LANES:
        p = find_lane_file(root, lane)
        if p is None:
            missing.append(lane)
            continue
        lanes[lane] = json.loads(p.read_text(encoding="utf-8"))

    statuses = {k: v.get("lane_status") for k, v in lanes.items()}
    hashes = {v.get("normalized_sha256") for v in lanes.values() if v.get("normalized_sha256")}
    infra = [k for k, v in lanes.items() if v.get("lane_status") == "INFRASTRUCTURE_FAIL"]
    failed = [k for k, v in lanes.items() if not v.get("lane_pass") and k not in infra]
    source_hash_consistent = len(hashes) == 1 and len(lanes) == len(LANES)

    if missing or infra:
        classification = "INFRASTRUCTURE_FAIL"
    elif not source_hash_consistent:
        classification = "INVALID_IMPLEMENTATION_SOURCE_HASH_MISMATCH"
    elif failed:
        classification = "BLOCKED_SOURCE_AUTHORITY"
    else:
        classification = "PRELIMINARY_PASS_PENDING_MANUAL_AUDIT"

    payload = {
        "iteration": "ITER061",
        "classification": classification,
        "scientific_terminal_verdict": False,
        "manual_audit_required": True,
        "lanes_expected": list(LANES),
        "lanes_present": sorted(lanes),
        "missing": missing,
        "infra": infra,
        "failed": failed,
        "statuses": statuses,
        "normalized_hashes": sorted(hashes),
        "source_hash_consistent": source_hash_consistent,
        "refinement_complex_gluing_authority_complete": False,
        "restricted_amplitude_authorized": False,
        "bridge_credit": False,
        "candidate_theory": "UNFORMED",
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=LANES)
    ap.add_argument("--out", required=True)
    ap.add_argument("--aggregate-dir")
    ns = ap.parse_args()
    out = Path(ns.out)
    if ns.aggregate_dir:
        return aggregate(Path(ns.aggregate_dir), out)
    if not ns.lane:
        ap.error("--lane is required unless --aggregate-dir is supplied")
    return run_lane(ns.lane, out)


if __name__ == "__main__":
    sys.exit(main())