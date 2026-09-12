#!/usr/bin/env python3
"""BH-004 three-level held-out projector/measure transport test.

One parent 1+1D causal set is assigned fixed uniform thinning marks.  This creates
nested induced causal sets at p0=1, p1 and p2 (p2<p1), so the p2 set is a true
subset of p1 and there is a canonical restriction map.

TRAINING uses only levels p0 and p1:
  * construct the source-defined Pauli-Jordan retained sector independently at
    each level with the frozen BH-003 rule sqrt(N)/(4*pi);
  * infer a two-point power-law retained-rank flow r ~ N^alpha.

PREDICTION at held-out p2:
  * predict r2 from the frozen alpha;
  * restrict the p1 retained basis to p2;
  * take the top left singular directions of that restriction, truncated to the
    predicted rank.  No p2 closure or p2 source projector is used to choose the
    predicted orientation or rank.

EVALUATION may then inspect the held-out source projector and native retarded
closure metrics.  Rank-matched Haar projectors provide an orientation-free
control.  An oracle-rank restricted transport is reported only as a diagnostic
separating rank-flow error from orientation-transport error.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy import linalg

from causal_set_ssee_2d_reproduction import sprinkle_diamond, causal_matrix
from bh001_bh003_spectral_closure_bridge import closure_metrics, random_basis
from bh003_source_sector_thinning_diagnostic import spectral_basis, compare_subspaces


def source_sector(c: np.ndarray) -> tuple[np.ndarray, float]:
    n = c.shape[0]
    cutoff = math.sqrt(n) / (4.0 * math.pi)
    _, v = spectral_basis(c, cutoff)
    if v.shape[1] < 2 or v.shape[1] >= n:
        raise RuntimeError(f"invalid source rank {v.shape[1]} for n={n}")
    return v, cutoff


def restricted_svd_basis(v_parent: np.ndarray, child_mask_in_parent: np.ndarray, rank: int) -> np.ndarray:
    a = np.asarray(v_parent[child_mask_in_parent, :], np.complex128)
    if a.size == 0:
        raise RuntimeError("empty restricted basis")
    u, s, _ = linalg.svd(a, full_matrices=False, check_finite=False)
    tol = max(a.shape) * np.finfo(float).eps * max(float(s[0]), 1.0)
    numerical_rank = int(np.sum(s > tol))
    k = min(max(2, int(rank)), numerical_rank, a.shape[0] - 1)
    if k < 2:
        raise RuntimeError("transported basis lost rank")
    return u[:, :k]


def rank_flow_alpha(n0: int, r0: int, n1: int, r1: int) -> float:
    if n0 == n1 or r0 <= 0 or r1 <= 0:
        raise RuntimeError("invalid rank-flow training pair")
    return math.log(r1 / r0) / math.log(n1 / n0)


def predicted_rank(n1: int, r1: int, n2: int, alpha: float) -> int:
    raw = r1 * (n2 / n1) ** alpha
    return int(np.clip(int(round(raw)), 2, n2 - 2))


def random_control_summary(g: np.ndarray, rank: int, n_random: int, rng: np.random.Generator) -> dict:
    rows = [closure_metrics(g, random_basis(g.shape[0], rank, rng)) for _ in range(n_random)]
    leak = np.asarray([x["leakage"] for x in rows], float)
    seq = np.asarray([x["sequential_defect"] for x in rows], float)
    return {
        "n": int(n_random),
        "mean_leakage": float(leak.mean()),
        "median_leakage": float(np.median(leak)),
        "mean_sequential_defect": float(seq.mean()),
        "median_sequential_defect": float(np.median(seq)),
        "leakage_samples": leak,
        "seq_samples": seq,
    }


def run(n_full: int, p1: float, p2: float, seed: int, n_random: int) -> dict:
    if not (1.0 > p1 > p2 > 0.0):
        raise ValueError("require 1 > p1 > p2 > 0")

    rng = np.random.default_rng(seed)
    uv = sprinkle_diamond(n_full, rng)
    c0 = causal_matrix(uv)
    marks = rng.random(n_full)
    idx1 = np.flatnonzero(marks < p1)
    idx2 = np.flatnonzero(marks < p2)
    if len(idx2) < 96:
        raise RuntimeError("held-out causal set too small")

    c1 = c0[np.ix_(idx1, idx1)]
    c2 = c0[np.ix_(idx2, idx2)]
    v0, cut0 = source_sector(c0)
    v1, cut1 = source_sector(c1)
    v2, cut2 = source_sector(c2)  # held-out evaluation only

    n0, n1, n2 = n_full, len(idx1), len(idx2)
    r0, r1, r2 = v0.shape[1], v1.shape[1], v2.shape[1]

    alpha = rank_flow_alpha(n0, r0, n1, r1)
    r2_pred = predicted_rank(n1, r1, n2, alpha)

    # Because idx2 is nested inside idx1, this mask is the canonical restriction.
    child_mask_in_1 = marks[idx1] < p2
    if int(np.sum(child_mask_in_1)) != n2:
        raise RuntimeError("nested thinning map inconsistent")

    vpred = restricted_svd_basis(v1, child_mask_in_1, r2_pred)
    voracle_rank = restricted_svd_basis(v1, child_mask_in_1, r2)

    alignment = compare_subspaces(vpred, v2)
    oracle_alignment = compare_subspaces(voracle_rank, v2)

    g2 = 0.5 * c2
    pred_closure = closure_metrics(g2, vpred)
    source_closure = closure_metrics(g2, v2)
    oracle_rank_closure = closure_metrics(g2, voracle_rank)

    controls = random_control_summary(g2, vpred.shape[1], n_random, rng)
    eps = np.finfo(float).eps
    leak_improvement = controls["median_leakage"] / max(pred_closure["leakage"], eps)
    seq_improvement = controls["median_sequential_defect"] / max(pred_closure["sequential_defect"], eps)
    frac_random_worse_leak = float(np.mean(controls["leakage_samples"] > pred_closure["leakage"]))
    frac_random_worse_seq = float(np.mean(controls["seq_samples"] > pred_closure["sequential_defect"]))

    rank_rel_error = abs(vpred.shape[1] - r2) / max(r2, 1)
    return {
        "test": "BH004_NESTED_THINNING_HELDOUT_PROJECTOR_MEASURE_TRANSPORT",
        "status": "PASS_EXECUTION",
        "seed": seed,
        "levels": {
            "p0": 1.0, "p1": p1, "p2_heldout": p2,
            "n0": n0, "n1": n1, "n2": n2,
            "r0": r0, "r1": r1, "r2_heldout_source": r2,
            "cutoff0": cut0, "cutoff1": cut1, "cutoff2_heldout_source": cut2,
        },
        "training": {
            "rank_flow_alpha_from_p0_p1": float(alpha),
            "predicted_r2_raw_rule": "r1*(n2/n1)^alpha, rounded and bounded",
        },
        "heldout_prediction": {
            "predicted_rank": int(vpred.shape[1]),
            "source_rank": int(r2),
            "rank_relative_error": float(rank_rel_error),
            "alignment_to_source": alignment,
            "closure": pred_closure,
            "random_median_over_predicted_leakage": float(leak_improvement),
            "random_median_over_predicted_seq_defect": float(seq_improvement),
            "fraction_random_worse_leakage": frac_random_worse_leak,
            "fraction_random_worse_seq_defect": frac_random_worse_seq,
        },
        "heldout_source_oracle_evaluation": {
            "closure": source_closure,
            "predicted_over_source_leakage": float(pred_closure["leakage"] / max(source_closure["leakage"], eps)),
            "predicted_over_source_seq_defect": float(pred_closure["sequential_defect"] / max(source_closure["sequential_defect"], eps)),
        },
        "oracle_rank_orientation_diagnostic": {
            "note": "Uses held-out source rank only to separate rank-flow error from orientation-transfer error; not part of prediction.",
            "alignment_to_source": oracle_alignment,
            "closure": oracle_rank_closure,
        },
        "rank_matched_random_control": {
            "n": controls["n"],
            "median_leakage": controls["median_leakage"],
            "median_sequential_defect": controls["median_sequential_defect"],
        },
        "claim_lock": (
            "Three-level nested-thinning held-out test of projector-aware transport in one 1+1D causal-set free-field realization. "
            "The held-out source projector is used only for evaluation, never to construct the predicted projector. "
            "A positive result would support BH-004 transport structure, not derive a fundamental QG RG law."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--n-full", type=int, required=True)
    p.add_argument("--p1", type=float, default=0.75)
    p.add_argument("--p2", type=float, default=0.50)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--n-random", type=int, default=16)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    out = run(a.n_full, a.p1, a.p2, a.seed, a.n_random)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
