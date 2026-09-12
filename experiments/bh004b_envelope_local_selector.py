#!/usr/bin/env python3
"""BH-004B transport-envelope + local source-native selector test.

A parent source sector is canonically restricted to a nested child causal set and
kept at full numerical rank, defining an orientation envelope E.  The child
Pauli-Jordan operator is then projected into E and the frozen BH-003 source
cutoff sqrt(N_child)/(4*pi) is applied to that projected operator.  The full
child source projector is constructed only afterward for evaluation.

No closure target, child source rank, or child source projector enters the
prediction.
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


def orthonormal_envelope(a: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    a = np.asarray(a, np.complex128)
    u, s, _ = linalg.svd(a, full_matrices=False, check_finite=False)
    if not len(s):
        raise RuntimeError("empty restricted parent sector")
    tol = max(a.shape) * np.finfo(float).eps * max(float(s[0]), 1.0)
    r = int(np.sum(s > tol))
    if r < 2:
        raise RuntimeError("transport envelope rank < 2")
    return u[:, :r], s[:r]


def local_selector(c_child: np.ndarray, envelope: np.ndarray, cutoff: float) -> tuple[np.ndarray, np.ndarray]:
    j = 0.5j * (c_child - c_child.T)
    je = envelope.conj().T @ j @ envelope
    je = 0.5 * (je + je.conj().T)
    evals, u = linalg.eigh(je, check_finite=False)
    keep = np.abs(evals) >= cutoff
    if int(np.sum(keep)) < 2:
        raise RuntimeError("projected local selector retained fewer than two modes")
    pred = envelope @ u[:, keep]
    # Numerical re-orthonormalization only; no target information.
    q, _ = np.linalg.qr(pred, mode="reduced")
    return q, evals


def random_controls(g: np.ndarray, rank: int, n_random: int, rng: np.random.Generator) -> dict:
    rows = [closure_metrics(g, random_basis(g.shape[0], rank, rng)) for _ in range(n_random)]
    leak = np.asarray([r["leakage"] for r in rows], float)
    seq = np.asarray([r["sequential_defect"] for r in rows], float)
    return {
        "median_leakage": float(np.median(leak)),
        "median_seq": float(np.median(seq)),
        "fraction_worse_leakage": leak,
        "fraction_worse_seq": seq,
    }


def run(n_full: int, p_parent: float, p_child: float, seed: int, n_random: int) -> dict:
    if not (1.0 > p_parent > p_child > 0.0):
        raise ValueError("require 1 > p_parent > p_child > 0")

    rng = np.random.default_rng(seed)
    uv = sprinkle_diamond(n_full, rng)
    c0 = causal_matrix(uv)
    marks = rng.random(n_full)
    idxp = np.flatnonzero(marks < p_parent)
    idxc = np.flatnonzero(marks < p_child)
    if len(idxc) < 96:
        raise RuntimeError("child causal set too small")

    cp = c0[np.ix_(idxp, idxp)]
    cc = c0[np.ix_(idxc, idxc)]
    np_, nc = len(idxp), len(idxc)

    cutoff_parent = math.sqrt(np_) / (4.0 * math.pi)
    cutoff_child = math.sqrt(nc) / (4.0 * math.pi)
    _, vp = spectral_basis(cp, cutoff_parent)

    child_mask_in_parent = marks[idxp] < p_child
    if int(np.sum(child_mask_in_parent)) != nc:
        raise RuntimeError("nested index mismatch")
    envelope, restriction_s = orthonormal_envelope(vp[child_mask_in_parent, :])

    # Prediction uses child native operator + frozen scalar rule only inside E.
    pred, projected_evals = local_selector(cc, envelope, cutoff_child)

    # Held-out oracle, constructed only after prediction.
    _, vsource = spectral_basis(cc, cutoff_child)

    pred_comp = compare_subspaces(pred, vsource)
    env_comp = compare_subspaces(envelope, vsource)
    rank_error = abs(pred.shape[1] - vsource.shape[1]) / max(vsource.shape[1], 1)
    distance_ratio = pred_comp["normalized_projector_distance"] / max(env_comp["normalized_projector_distance"], 1e-15)

    # Fraction of source norm captured by the envelope; evaluation only.
    overlap = envelope.conj().T @ vsource
    source_capture = float(np.sum(np.abs(overlap) ** 2) / max(vsource.shape[1], 1))

    g = 0.5 * cc
    pred_closure = closure_metrics(g, pred)
    env_closure = closure_metrics(g, envelope)
    source_closure = closure_metrics(g, vsource)
    ctr = random_controls(g, pred.shape[1], n_random, rng)
    eps = np.finfo(float).eps

    return {
        "test": "BH004B_TRANSPORT_ENVELOPE_LOCAL_SELECTOR",
        "status": "PASS_EXECUTION",
        "seed": seed,
        "n_full": n_full,
        "levels": {
            "p_parent": p_parent,
            "p_child": p_child,
            "n_parent": np_,
            "n_child": nc,
            "cutoff_parent": cutoff_parent,
            "cutoff_child": cutoff_child,
        },
        "prediction": {
            "parent_source_rank": int(vp.shape[1]),
            "envelope_rank": int(envelope.shape[1]),
            "predicted_rank": int(pred.shape[1]),
            "projected_operator_eigenvalue_count": int(len(projected_evals)),
            "source_rank_evaluation_only": int(vsource.shape[1]),
            "rank_relative_error": float(rank_error),
            "alignment_to_source": pred_comp,
            "envelope_alignment_to_source": env_comp,
            "predicted_over_envelope_projector_distance": float(distance_ratio),
            "source_norm_capture_by_envelope": source_capture,
        },
        "closure": {
            "predicted": pred_closure,
            "envelope": env_closure,
            "source_oracle": source_closure,
            "random_median_over_predicted_leakage": float(ctr["median_leakage"] / max(pred_closure["leakage"], eps)),
            "random_median_over_predicted_seq_defect": float(ctr["median_seq"] / max(pred_closure["sequential_defect"], eps)),
            "fraction_random_worse_leakage": float(np.mean(ctr["fraction_worse_leakage"] > pred_closure["leakage"])),
            "fraction_random_worse_seq_defect": float(np.mean(ctr["fraction_worse_seq"] > pred_closure["sequential_defect"])),
            "predicted_over_source_leakage": float(pred_closure["leakage"] / max(source_closure["leakage"], eps)),
            "predicted_over_source_seq_defect": float(pred_closure["sequential_defect"] / max(source_closure["sequential_defect"], eps)),
        },
        "claim_lock": (
            "Parent-derived transport envelope plus child-source-native projected Pauli-Jordan selector. "
            "The full child source projector/rank and closure target are evaluation-only. Success would support a bridge factorization, not a new QG theory."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--n-full", type=int, required=True)
    p.add_argument("--p-parent", type=float, default=0.5625)
    p.add_argument("--p-child", type=float, default=0.421875)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--n-random", type=int, default=24)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    out = run(a.n_full, a.p_parent, a.p_child, a.seed, a.n_random)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
