#!/usr/bin/env python3
"""ITER028 Stage S: conservative source graph compiler.

Scientific contract is frozen in prereg/ITER028_RC006_EQ27_TOPOLOGY_FAITHFUL_CONTRACTION_2026-09-14.md.
This stage may PASS only when the byte-pinned source itself mechanically determines the complete
Eq.(27) graph-to-component map. Ambiguity yields the preregistered BLOCKED class; it is never
filled from memory or numerical agreement.
"""
from __future__ import annotations
import gzip, hashlib, io, json, re, tarfile, time, urllib.request
from pathlib import Path, PurePosixPath

ARXIV_ID = "1609.02429v2"
EXPECTED_ARCHIVE_SHA = "3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee"
EXPECTED_EQ27_SHA = "88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d"
OUT = Path("out_iter028_stage_s")
OUT.mkdir(exist_ok=True)
UA = "ISQGR-ITER028-StageS/1.0"


def fetch(url: str, attempts: int = 6) -> bytes:
    err = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=75) as r:
                return r.read()
        except Exception as e:
            err = repr(e)
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"source fetch failed: {err}")


def unpack(data: bytes):
    files = {}
    try:
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:*") as tf:
            for m in tf.getmembers():
                p = PurePosixPath(m.name)
                if p.is_absolute() or ".." in p.parts or not m.isfile() or m.size > 12_000_000:
                    continue
                if p.suffix.lower() not in {".tex", ".sty", ".bib"}:
                    continue
                f = tf.extractfile(m)
                if f:
                    files[str(p)] = f.read().decode("utf-8", "replace")
        if files:
            return files
    except tarfile.TarError:
        pass
    try:
        return {"source.tex": gzip.decompress(data).decode("utf-8", "replace")}
    except Exception:
        return {"source.tex": data.decode("utf-8", "replace")}


def containing_display(text: str, pos: int):
    patterns = [
        (r"\\begin\{align\*?\}", r"\\end\{align\*?\}"),
        (r"\\begin\{equation\*?\}", r"\\end\{equation\*?\}"),
        (r"\\begin\{gather\*?\}", r"\\end\{gather\*?\}"),
        (r"\\ba\b", r"\\ea\b"), (r"\\be\b", r"\\ee\b"), (r"\\bea\b", r"\\eea\b"),
    ]
    starts = []
    for bp, ep in patterns:
        starts.extend((m.start(), ep) for m in re.finditer(bp, text[:pos+1]))
    for start, ep in sorted(starts, reverse=True):
        endm = re.search(ep, text[start:])
        if endm:
            end = start + endm.end()
            if start <= pos <= end:
                return text[start:end], start, end
    return None


def tikz_blocks(display: str):
    return re.findall(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", display, flags=re.S)


def source_commands(block: str):
    # Mechanical inventory only. No semantic graph assumptions are introduced here.
    nodes = []
    for i, m in enumerate(re.finditer(r"\\node(?:\[[^\]]*\])?\s*\(([^)]+)\)(?:\s*at\s*\(([^)]*)\))?\s*\{([^}]*)\}\s*;", block, re.S)):
        nodes.append({"id": f"node_{i}", "source_name": m.group(1).strip(), "at": (m.group(2) or "").strip(),
                      "label_tex": m.group(3).strip(), "source_offset": m.start()})
    draws = []
    for i, m in enumerate(re.finditer(r"\\draw(?:\[[^\]]*\])?\s*(.*?);", block, re.S)):
        raw = m.group(0)
        refs = re.findall(r"\(([^)]+)\)", raw)
        draws.append({"id": f"draw_{i}", "raw": raw, "refs": refs, "source_offset": m.start()})
    return nodes, draws


def label_tokens(s: str):
    toks = sorted(set(re.findall(r"(?<![A-Za-z])(?:j|l|J)(?:_\{?[^\s,;)}]+\}?|\^\{?[+\-]\}?|['+\-])*", s)))
    return toks


def main():
    result = {
        "iteration": 28, "stage": "S", "scientific_contract_changed": False,
        "classification": None, "scientific_pass": False, "numerical_lanes_authorized": False,
        "expected_archive_sha256": EXPECTED_ARCHIVE_SHA, "expected_eq27_sha256": EXPECTED_EQ27_SHA,
    }
    try:
        raw = fetch(f"https://export.arxiv.org/e-print/{ARXIV_ID}")
        archive_sha = hashlib.sha256(raw).hexdigest()
        result["fresh_archive_sha256"] = archive_sha
        if archive_sha != EXPECTED_ARCHIVE_SHA:
            result.update(classification="INFRASTRUCTURE_OR_PROVENANCE_BLOCKED", reason="archive_sha_mismatch")
            (OUT/"stage_s_evidence.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
            print(json.dumps(result, indent=2)); return

        files = unpack(raw)
        hits = []
        for name, text in files.items():
            for m in re.finditer(r"\\label\{eq:eprl-3-valent\}", text):
                d = containing_display(text, m.start())
                if d: hits.append((name, text, d[0], d[1], d[2]))
        result["eq27_display_hits"] = len(hits)
        if len(hits) != 1:
            result.update(classification="RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED", reason="eq27_not_unique")
            (OUT/"stage_s_evidence.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
            print(json.dumps(result, indent=2)); return

        fname, fulltext, display, dstart, dend = hits[0]
        eqsha = hashlib.sha256(display.encode()).hexdigest()
        result["fresh_eq27_sha256"] = eqsha
        result["eq27_source_file"] = fname
        (OUT/"eq27_exact.tex").write_text(display)
        if eqsha != EXPECTED_EQ27_SHA:
            result.update(classification="INFRASTRUCTURE_OR_PROVENANCE_BLOCKED", reason="eq27_snippet_sha_mismatch")
            (OUT/"stage_s_evidence.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
            print(json.dumps(result, indent=2)); return

        blocks = tikz_blocks(display)
        sums = list(re.finditer(r"\\sum\b|\\sum_", display))
        graph = {"source": ARXIV_ID, "source_file": fname, "display_sha256": eqsha, "blocks": [], "scalar_tex": display}
        all_labels = label_tokens(display)
        unresolved = []
        for bi, block in enumerate(blocks):
            nodes, draws = source_commands(block)
            entry = {"id": f"graph_block_{bi+1}", "source_locator": f"{fname}:eq:eprl-3-valent:tikz:{bi+1}",
                     "nodes": nodes, "draw_commands": draws, "labels": label_tokens(block)}
            # A topology-faithful component map requires every draw endpoint to resolve either to a named
            # source node or an explicit coordinate plus an independently source-labelled leg/index.
            named = {n["source_name"] for n in nodes}
            for d in draws:
                symbolic = [r for r in d["refs"] if re.match(r"^[A-Za-z@][A-Za-z0-9_:@.-]*$", r)]
                missing = [r for r in symbolic if r not in named]
                if missing:
                    unresolved.append({"block": bi+1, "draw": d["id"], "kind": "unresolved_named_endpoint", "refs": missing})
                if not label_tokens(d["raw"]) and len(symbolic) < 2:
                    unresolved.append({"block": bi+1, "draw": d["id"], "kind": "edge_without_mechanical_index_or_two_named_endpoints"})
            graph["blocks"].append(entry)

        # Frozen inventory predicates. These do not infer meaning; they only check exact-source structure.
        inventory = {
            "tikz_blocks": len(blocks), "sum_occurrences": len(sums), "label_tokens": all_labels,
            "has_primed_J_plus": bool(re.search(r"J\s*\^\s*\{?\+\}?\s*'|\(J\^\+\)'", display)),
            "has_primed_J_minus": bool(re.search(r"J\s*\^\s*\{?-\}?\s*'|\(J\^-\)'", display)),
            "has_unprimed_J_plus": "J^+" in display or "J^{+}" in display,
            "has_unprimed_J_minus": "J^-" in display or "J^{-}" in display,
        }
        result["inventory"] = inventory
        graph["unresolved"] = unresolved
        (OUT/"eq27_graph_dictionary.json").write_text(json.dumps(graph, indent=2, sort_keys=True)+"\n")

        expected_structural = (len(blocks) == 4 and len(sums) >= 2 and inventory["has_primed_J_plus"] and inventory["has_primed_J_minus"])
        if not expected_structural:
            result.update(classification="RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED",
                          reason="frozen_source_inventory_not_mechanically_reproduced")
        elif unresolved:
            result.update(classification="RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED",
                          reason="exact_graph_to_index_relations_unresolved", unresolved_count=len(unresolved))
        else:
            # Even when syntax endpoints resolve, require explicit source index/order locators for every graph edge.
            # TikZ geometry alone is not an index-order authority under the frozen preregistration.
            lacking_index_authority = []
            for b in graph["blocks"]:
                for d in b["draw_commands"]:
                    if not label_tokens(d["raw"]):
                        lacking_index_authority.append({"block": b["id"], "draw": d["id"]})
            if lacking_index_authority:
                result.update(classification="RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED",
                              reason="tikz_geometry_does_not_mechanically_fix_all_tensor_index_orders",
                              lacking_index_authority_count=len(lacking_index_authority))
                graph["lacking_index_authority"] = lacking_index_authority
                (OUT/"eq27_graph_dictionary.json").write_text(json.dumps(graph, indent=2, sort_keys=True)+"\n")
            else:
                result.update(classification="RC006_EQ27_STAGE_S_SOURCE_GRAPH_MAP_PASS", scientific_pass=True,
                              numerical_lanes_authorized=True, reason="complete_mechanical_map")

        result["graph_dictionary_sha256"] = hashlib.sha256((OUT/"eq27_graph_dictionary.json").read_bytes()).hexdigest()
        result["source_file_count"] = len(files)
        (OUT/"stage_s_evidence.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
        print(json.dumps(result, indent=2, sort_keys=True))
    except Exception as e:
        result.update(classification="NUMERICAL_OR_INFRASTRUCTURE_FAIL_PRE_SCIENCE", reason=repr(e))
        (OUT/"stage_s_evidence.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
        print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
