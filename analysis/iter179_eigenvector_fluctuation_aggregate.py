#!/usr/bin/env python3
"""ITER179 frozen aggregate adjudicator."""

from __future__ import annotations
import argparse, json, math, statistics
from pathlib import Path
import numpy as np

NS = [384, 512, 768, 1024]
SEEDS = [311, 337]
TOL = 1e-7


def load(path: Path) -> dict[tuple[int, int], dict]:
    out = {}
    for p in sorted(path.glob("*.json")):
        d = json.loads(p.read_text())
        key = (int(d["n"]), int(d["core_seed"]))
        if key in out:
            raise RuntimeError(f"duplicate result {key} in {path}")
        out[key] = d
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--researcher-dir", type=Path, required=True)
    ap.add_argument("--critic-dir", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()

    r = load(a.researcher_dir)
    c = load(a.critic_dir)
    expected = {(n, s) for n in NS for s in SEEDS}

    missing_r = sorted(expected - set(r))
    missing_c = sorted(expected - set(c))
    extra_r = sorted(set(r) - expected)
    extra_c = sorted(set(c) - expected)
    errors = []
    pairs = []

    if not (missing_r or missing_c or extra_r or extra_c):
        for key in sorted(expected):
            x, y = r[key], c[key]
            for field in ("nc", "completion_seeds", "ensemble_size", "phase_anchor_core_index",
                          "positive_modes_min_across_ensemble", "usable_mode_indices",
                          "unusable_mode_indices"):
                if x[field] != y[field]:
                    errors.append({"key": list(key), "reason": f"{field}_mismatch"})
            if len(x["phase_anchor_uv"]) == len(y["phase_anchor_uv"]):
                if max(abs(float(u)-float(v)) for u,v in zip(x["phase_anchor_uv"],y["phase_anchor_uv"])) > 1e-14:
                    errors.append({"key": list(key), "reason": "anchor_uv_mismatch"})
            xr = np.asarray(x["persistence_ratio"], float)
            yr = np.asarray(y["persistence_ratio"], float)
            if xr.shape != yr.shape:
                md = None
                errors.append({"key": list(key), "reason": "curve_shape_mismatch"})
            else:
                md = float(np.max(np.abs(xr-yr))) if xr.size else 0.0
                if (not math.isfinite(md)) or md > TOL:
                    errors.append({"key": list(key), "reason": "curve_disagreement", "max_abs_diff": md})
            xres = bool(x["selection"]["resolved"])
            yres = bool(y["selection"]["resolved"])
            xj = x["selected_positive_rank"]
            yj = y["selected_positive_rank"]
            if xres != yres or xj != yj:
                errors.append({
                    "key": list(key), "reason": "classification_or_break_mismatch",
                    "researcher_resolved": xres, "critic_resolved": yres,
                    "researcher_break": xj, "critic_break": yj,
                })
            pairs.append({
                "n": key[0],
                "core_seed": key[1],
                "max_curve_abs_diff": md,
                "resolved": xres,
                "j_star": xj,
                "delta_bic": x["selection"].get("delta_bic"),
                "loo_stable": x["selection"].get("loo_stable"),
                "source_comparison": x["post_selection_source_comparison"],
            })

    provenance_valid = not (missing_r or missing_c or extra_r or extra_c)
    implementation_valid = provenance_valid and not errors
    resolved = [p for p in pairs if p["resolved"]]

    by_n = {n: sum(1 for p in resolved if p["n"] == n) for n in NS}
    qvals = [float(p["j_star"]) / math.sqrt(p["n"]) for p in resolved if p["j_star"]]
    cv = None
    if qvals:
        mean = statistics.fmean(qvals)
        cv = statistics.pstdev(qvals) / mean if mean else None

    transition_gate = bool(
        implementation_valid
        and len(resolved) >= 6
        and all(by_n[n] >= 1 for n in NS)
        and cv is not None
        and cv <= 0.35
    )

    rank_ratios = []
    lambda_ratios = []
    if transition_gate:
        for p in resolved:
            s = p["source_comparison"]
            if s is None:
                errors.append({"key": [p["n"], p["core_seed"]], "reason": "missing_post_selection_source_comparison"})
                continue
            rank_ratios.append(float(s["j_star_over_median_source_rank"]))
            lambda_ratios.append(float(s["lambda_star_over_source"]))

    if errors and implementation_valid:
        implementation_valid = False
        transition_gate = False

    med_rank = statistics.median(rank_ratios) if rank_ratios else None
    med_lambda = statistics.median(lambda_ratios) if lambda_ratios else None
    source_compatible = bool(
        transition_gate
        and med_rank is not None and 0.5 <= med_rank <= 2.0
        and med_lambda is not None and 0.5 <= med_lambda <= 2.0
    )

    if not implementation_valid:
        classification = "INVALID_IMPLEMENTATION_ITER179"
    elif not transition_gate:
        classification = "BLOCKED_SCOPED_ITER179_FLUCTUATION_TRANSITION_NOT_STABLY_IDENTIFIED"
    elif source_compatible:
        classification = "PASS_SCOPED_ITER179_EIGENVECTOR_FLUCTUATION_TRANSITION_SOURCE_COMPATIBLE"
    else:
        classification = "SCIENTIFIC_FAIL_SCOPED_ITER179_STABLE_FLUCTUATION_TRANSITION_SOURCE_INCOMPATIBLE"

    out = {
        "iteration": "ITER179",
        "classification": classification,
        "expected_jobs_per_lane": 8,
        "researcher_jobs": len(r),
        "critic_jobs": len(c),
        "missing_researcher": missing_r,
        "missing_critic": missing_c,
        "extra_researcher": extra_r,
        "extra_critic": extra_c,
        "curve_agreement_tolerance": TOL,
        "implementation_valid": implementation_valid,
        "implementation_errors": errors,
        "pair_summaries": pairs,
        "resolved_count": len(resolved),
        "resolved_by_n": {str(k): v for k,v in by_n.items()},
        "j_star_over_sqrtN_values": qvals,
        "j_star_over_sqrtN_cv": cv,
        "transition_gate": transition_gate,
        "post_selection_rank_ratios": rank_ratios,
        "post_selection_lambda_ratios": lambda_ratios,
        "median_j_star_over_source_rank": med_rank,
        "median_lambda_star_over_source": med_lambda,
        "source_compatible": source_compatible,
        "claim_locks": {
            "bridge_credit": 0,
            "B1_total": "UNAUTHORIZED",
            "ITER118_MATCHING_AUTHORIZED": False,
            "BRIDGE_DERIVED": False,
            "NEW_PHYSICS_FOUND": False,
            "NEW_QG_THEORY_REQUIRED": False,
            "ALL_KNOWN_SCHOOLS_FAIL": False,
            "candidate_theory": "UNFORMED / 0%",
        },
    }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
