#!/usr/bin/env python3
"""Frozen ITER178 aggregate and independent implementation adjudicator."""

from __future__ import annotations
import argparse, json, math, statistics
from pathlib import Path
import numpy as np

EXPECTED_N = [384, 512, 768, 1024]
EXPECTED_SEEDS = [211, 223, 227, 229]
AGREEMENT_TOL = 1e-9


def load_dir(path: Path) -> dict[tuple[int, int], dict]:
    out = {}
    for p in sorted(path.glob("*.json")):
        d = json.loads(p.read_text())
        key = (int(d["n"]), int(d["seed"]))
        if key in out:
            raise RuntimeError(f"duplicate {key} in {path}")
        out[key] = d
    return out


def finite_list(xs) -> bool:
    return all(math.isfinite(float(x)) for x in xs)


def fit_power(rows: list[dict]) -> dict | None:
    by_n = {}
    for n in EXPECTED_N:
        g = [float(r["selected_cutoff"]) for r in rows if int(r["n"]) == n and r["selected_cutoff"] is not None]
        if not g:
            return None
        by_n[n] = statistics.median(g)
    x = np.log(np.asarray(EXPECTED_N, dtype=float))
    y = np.log(np.asarray([by_n[n] for n in EXPECTED_N], dtype=float))
    alpha, log_a = np.polyfit(x, y, 1)
    pred = alpha * x + log_a
    den = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - float(np.sum((y - pred) ** 2)) / den if den > 0 else 0.0
    return {
        "median_selected_cutoff_by_n": {str(n): by_n[n] for n in EXPECTED_N},
        "alpha": float(alpha),
        "A": float(math.exp(log_a)),
        "r2": float(r2),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--researcher-dir", type=Path, required=True)
    p.add_argument("--critic-dir", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()

    rr = load_dir(a.researcher_dir)
    cc = load_dir(a.critic_dir)
    expected = {(n, s) for n in EXPECTED_N for s in EXPECTED_SEEDS}
    missing_researcher = sorted(expected - set(rr))
    missing_critic = sorted(expected - set(cc))
    extra_researcher = sorted(set(rr) - expected)
    extra_critic = sorted(set(cc) - expected)

    implementation_errors = []
    pair_summaries = []
    if not missing_researcher and not missing_critic and not extra_researcher and not extra_critic:
        for key in sorted(expected):
            r, c = rr[key], cc[key]
            if r["fractions"] != c["fractions"] or r["ranks"] != c["ranks"]:
                implementation_errors.append({"key": key, "reason": "grid_or_rank_mismatch"})
                continue
            ri = r["mass_deformation_instability"]
            ci = c["mass_deformation_instability"]
            if not finite_list(ri) or not finite_list(ci):
                implementation_errors.append({"key": key, "reason": "nonfinite_instability"})
                continue
            md = max(abs(float(x) - float(y)) for x, y in zip(ri, ci))
            rb = r["selection"]["break_interval_index"]
            cb = c["selection"]["break_interval_index"]
            rs = bool(r["selection"]["resolved"])
            cs = bool(c["selection"]["resolved"])
            if md > AGREEMENT_TOL or rb != cb or rs != cs:
                implementation_errors.append({
                    "key": key, "reason": "researcher_critic_disagreement",
                    "max_instability_abs_diff": md,
                    "researcher_break": rb, "critic_break": cb,
                    "researcher_resolved": rs, "critic_resolved": cs,
                })
            pair_summaries.append({
                "n": key[0], "seed": key[1],
                "max_instability_abs_diff": md,
                "break_interval_index": rb,
                "resolved": rs,
                "selected_cutoff": r["selected_cutoff"],
                "selected_fraction": r["selected_fraction"],
                "selected_to_source_ratio": r["post_selection_selected_to_source_ratio"],
            })

    provenance_valid = not (missing_researcher or missing_critic or extra_researcher or extra_critic)
    implementation_valid = provenance_valid and not implementation_errors

    resolved = [x for x in pair_summaries if x["resolved"]]
    resolved_count = len(resolved)
    interval_counts = {}
    for x in resolved:
        i = int(x["break_interval_index"])
        interval_counts[i] = interval_counts.get(i, 0) + 1

    best_center = None
    best_adjacent_cluster_count = 0
    for center in range(1, 8):
        count = sum(interval_counts.get(i, 0) for i in (center - 1, center, center + 1))
        if count > best_adjacent_cluster_count:
            best_adjacent_cluster_count = count
            best_center = center

    selector_stable = bool(
        implementation_valid
        and resolved_count >= 12
        and best_adjacent_cluster_count >= 12
    )

    power_fit = fit_power(resolved) if selector_stable else None
    source_ratios = [
        float(x["selected_to_source_ratio"])
        for x in resolved
        if x["selected_to_source_ratio"] is not None
    ]
    median_source_ratio = statistics.median(source_ratios) if source_ratios else None

    compatibility = {
        "alpha_pass": bool(power_fit and 0.35 <= power_fit["alpha"] <= 0.65),
        "r2_pass": bool(power_fit and power_fit["r2"] >= 0.85),
        "median_ratio_pass": bool(median_source_ratio is not None and 0.5 <= median_source_ratio <= 2.0),
    }
    source_compatible = selector_stable and all(compatibility.values())

    if not implementation_valid:
        classification = "INVALID_IMPLEMENTATION_ITER178"
    elif not selector_stable:
        classification = "BLOCKED_SCOPED_ITER178_DYNAMIC_BREAK_NOT_STABLY_IDENTIFIED"
    elif source_compatible:
        classification = "PASS_SCOPED_ITER178_MASS_DEFORMATION_DYNAMIC_BREAK_SOURCE_COMPATIBLE"
    else:
        classification = "SCIENTIFIC_FAIL_SCOPED_ITER178_MASS_DEFORMATION_DYNAMIC_BREAK_SOURCE_INCOMPATIBLE"

    out = {
        "iteration": "ITER178",
        "classification": classification,
        "expected_jobs_per_lane": 16,
        "researcher_job_count": len(rr),
        "critic_job_count": len(cc),
        "missing_researcher": missing_researcher,
        "missing_critic": missing_critic,
        "extra_researcher": extra_researcher,
        "extra_critic": extra_critic,
        "implementation_agreement_tolerance": AGREEMENT_TOL,
        "implementation_valid": implementation_valid,
        "implementation_errors": implementation_errors,
        "pair_summaries": pair_summaries,
        "resolved_break_count": resolved_count,
        "break_interval_counts": {str(k): v for k, v in sorted(interval_counts.items())},
        "best_adjacent_cluster_center": best_center,
        "best_adjacent_cluster_count": best_adjacent_cluster_count,
        "selector_stable": selector_stable,
        "post_selection_power_fit": power_fit,
        "post_selection_median_selected_to_source_ratio": median_source_ratio,
        "source_compatibility_predicates": compatibility,
        "source_compatible": source_compatible,
        "claim_locks": {
            "bridge_credit": 0,
            "BRIDGE_DERIVED": False,
            "NEW_PHYSICS_FOUND": False,
            "NEW_QG_THEORY_REQUIRED": False,
            "ALL_KNOWN_SCHOOLS_FAIL": False,
            "ITER118_MATCHING_AUTHORIZED": False,
            "B1_total": "UNAUTHORIZED",
            "candidate_theory": "UNFORMED / 0%",
        },
    }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True, allow_nan=False))
    return 0 if implementation_valid else 2


if __name__ == "__main__":
    raise SystemExit(main())
