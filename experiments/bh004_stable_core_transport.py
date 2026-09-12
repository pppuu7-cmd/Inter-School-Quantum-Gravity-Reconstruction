#!/usr/bin/env python3
"""BH-004 stable-core transport with disjoint training/test seeds.

Four geometrically nested Bernoulli levels are generated from one parent causal
set using fixed marks:
    p0=1, p1=0.75, p2=0.5625, p3=0.421875.

TRAIN mode uses source-defined sectors at p0,p1,p2 and scores a preregistered
grid of singular-value retention thresholds tau on the two training transitions
p0->p1 and p1->p2.  No closure metric is used to fit tau.

TEST mode receives one globally frozen tau learned from separate training seeds.
It restricts the p2 source sector to unseen p3 and retains only left-singular
directions with s/s_max >= tau.  The p3 source sector is constructed only after
this prediction for evaluation.  Closure is then compared with rank-matched Haar
controls and with an unpruned restriction baseline.
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

LEVELS = (1.0, 0.75, 0.5625, 0.421875)
TAU_GRID = tuple(round(x, 3) for x in np.arange(0.50, 0.991, 0.025))


def source_sector(c: np.ndarray) -> np.ndarray:
    n = c.shape[0]
    _, v = spectral_basis(c, math.sqrt(n) / (4.0 * math.pi))
    if v.shape[1] < 2 or v.shape[1] >= n:
        raise RuntimeError(f"invalid source rank {v.shape[1]} at n={n}")
    return v


def build_levels(n_full: int, seed: int):
    rng = np.random.default_rng(seed)
    uv = sprinkle_diamond(n_full, rng)
    c0 = causal_matrix(uv)
    marks = rng.random(n_full)
    idx = [np.arange(n_full)] + [np.flatnonzero(marks < p) for p in LEVELS[1:]]
    if len(idx[-1]) < 96:
        raise RuntimeError("final held-out level too small")
    cs = [c0] + [c0[np.ix_(ii, ii)] for ii in idx[1:]]
    vs = [source_sector(c) for c in cs]
    return rng, marks, idx, cs, vs


def restriction_svd(v_parent: np.ndarray, parent_idx: np.ndarray, marks: np.ndarray, p_child: float):
    mask = marks[parent_idx] < p_child
    a = np.asarray(v_parent[mask, :], np.complex128)
    u, s, _ = linalg.svd(a, full_matrices=False, check_finite=False)
    tol = max(a.shape) * np.finfo(float).eps * max(float(s[0]), 1.0)
    nr = int(np.sum(s > tol))
    if nr < 2:
        raise RuntimeError("restricted parent sector lost rank")
    return u[:, :nr], s[:nr]


def basis_for_tau(u: np.ndarray, s: np.ndarray, tau: float) -> np.ndarray | None:
    rel = s / max(float(s[0]), np.finfo(float).eps)
    k = int(np.sum(rel >= tau))
    if k < 2:
        return None
    return u[:, :k]


def train(n_full: int, seed: int) -> dict:
    _, marks, idx, _, vs = build_levels(n_full, seed)
    transitions = []
    for j in (0, 1):
        u, s = restriction_svd(vs[j], idx[j], marks, LEVELS[j + 1])
        transitions.append((u, s, vs[j + 1]))

    score_by_tau = {}
    for tau in TAU_GRID:
        dists = []
        cosines = []
        rank_ratios = []
        valid = True
        for u, s, vchild in transitions:
            pred = basis_for_tau(u, s, tau)
            if pred is None:
                valid = False
                break
            comp = compare_subspaces(pred, vchild)
            dists.append(comp["normalized_projector_distance"])
            cosines.append(comp["mean_principal_cosine"])
            rank_ratios.append(pred.shape[1] / vchild.shape[1])
        if valid:
            score_by_tau[f"{tau:.3f}"] = {
                "mean_projector_distance": float(np.mean(dists)),
                "mean_principal_cosine": float(np.mean(cosines)),
                "mean_rank_ratio_to_source": float(np.mean(rank_ratios)),
            }

    if not score_by_tau:
        raise RuntimeError("no valid tau values")
    local_best = min(score_by_tau, key=lambda k: score_by_tau[k]["mean_projector_distance"])
    return {
        "test": "BH004_STABLE_CORE_TRAIN",
        "status": "PASS_EXECUTION",
        "n_full": n_full,
        "seed": seed,
        "levels": list(LEVELS),
        "source_ranks": [int(v.shape[1]) for v in vs],
        "tau_grid": list(TAU_GRID),
        "score_by_tau": score_by_tau,
        "local_best_tau_descriptive_only": float(local_best),
        "claim_lock": "Training uses source-subspace geometry only on p0->p1 and p1->p2; no closure target and no p3 metric are used. Global tau must be frozen across separate training jobs before test seeds are evaluated."
    }


def test(n_full: int, seed: int, tau: float, n_random: int) -> dict:
    rng, marks, idx, cs, vs = build_levels(n_full, seed)
    u, s = restriction_svd(vs[2], idx[2], marks, LEVELS[3])
    pred = basis_for_tau(u, s, tau)
    if pred is None:
        raise RuntimeError("frozen tau retained fewer than two directions")
    unpruned = u
    vtrue = vs[3]

    pred_align = compare_subspaces(pred, vtrue)
    unpruned_align = compare_subspaces(unpruned, vtrue)
    g3 = 0.5 * cs[3]
    pred_closure = closure_metrics(g3, pred)
    unpruned_closure = closure_metrics(g3, unpruned)
    source_closure = closure_metrics(g3, vtrue)

    random_rows = [closure_metrics(g3, random_basis(g3.shape[0], pred.shape[1], rng)) for _ in range(n_random)]
    rleak = np.asarray([x["leakage"] for x in random_rows], float)
    rseq = np.asarray([x["sequential_defect"] for x in random_rows], float)
    eps = np.finfo(float).eps

    return {
        "test": "BH004_STABLE_CORE_HELDOUT_TEST",
        "status": "PASS_EXECUTION",
        "n_full": n_full,
        "seed": seed,
        "levels": list(LEVELS),
        "frozen_tau": tau,
        "heldout": {
            "n3": int(cs[3].shape[0]),
            "source_rank": int(vtrue.shape[1]),
            "predicted_core_rank": int(pred.shape[1]),
            "rank_fraction_of_source": float(pred.shape[1] / vtrue.shape[1]),
            "alignment_to_source": pred_align,
            "closure": pred_closure,
            "random_median_over_predicted_leakage": float(np.median(rleak) / max(pred_closure["leakage"], eps)),
            "random_median_over_predicted_seq_defect": float(np.median(rseq) / max(pred_closure["sequential_defect"], eps)),
            "fraction_random_worse_leakage": float(np.mean(rleak > pred_closure["leakage"])),
            "fraction_random_worse_seq_defect": float(np.mean(rseq > pred_closure["sequential_defect"])),
        },
        "unpruned_parent_restriction_baseline": {
            "rank": int(unpruned.shape[1]),
            "alignment_to_source": unpruned_align,
            "closure": unpruned_closure,
        },
        "heldout_source_oracle_evaluation": {"closure": source_closure},
        "claim_lock": "Frozen stable-core threshold learned only on disjoint training seeds/source-subspace geometry. Held-out p3 source sector and closure are evaluation-only."
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=("train", "test"), required=True)
    p.add_argument("--n-full", type=int, required=True)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--tau", type=float)
    p.add_argument("--n-random", type=int, default=16)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    if a.mode == "train":
        out = train(a.n_full, a.seed)
    else:
        if a.tau is None:
            raise SystemExit("--tau required in test mode")
        out = test(a.n_full, a.seed, a.tau, a.n_random)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
