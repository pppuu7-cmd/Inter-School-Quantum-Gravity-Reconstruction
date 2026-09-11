#!/usr/bin/env python3
"""Diagnostic: does the known BH-003 source spectral sector itself transfer under thinning?

This does not infer a regulator.  It freezes the source prescription
    lambda_min = sqrt(N)/(4*pi)
on the full causal set and independently on the induced thinned causal set,
then compares the corresponding spectral subspaces after restricting the full
sector to the surviving elements.

The test answers whether Bernoulli thinning is semantically compatible with the
already-known source sector before it is used as an RG map for regulator
inference.  No entropy observable is evaluated.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy import linalg

from causal_set_ssee_2d_reproduction import sprinkle_diamond, causal_matrix


def spectral_basis(c: np.ndarray, cutoff: float) -> tuple[np.ndarray, np.ndarray]:
    j = 0.5j * (c - c.T)
    evals, u = linalg.eigh(j, check_finite=False)
    keep = np.abs(evals) >= cutoff
    return evals, u[:, keep]


def orthonormal_restricted_span(a: np.ndarray) -> np.ndarray:
    q, r = np.linalg.qr(a, mode="reduced")
    diag = np.abs(np.diag(r))
    if len(diag) == 0:
        raise RuntimeError("empty restricted source sector")
    tol = max(a.shape) * np.finfo(float).eps * max(float(diag.max()), 1.0)
    rank = int(np.sum(diag > tol))
    if rank < 2:
        raise RuntimeError("restricted source sector lost rank")
    return q[:, :rank]


def compare_subspaces(q: np.ndarray, v: np.ndarray) -> dict:
    rq, rv = q.shape[1], v.shape[1]
    overlap = q.conj().T @ v
    tr_pq = float(np.sum(np.abs(overlap) ** 2))
    dist2 = max(0.0, rq + rv - 2.0 * tr_pq)
    normalized = math.sqrt(dist2 / max(rq + rv, 1))
    s = linalg.svdvals(overlap, check_finite=False)
    s = np.clip(s, 0.0, 1.0)
    return {
        "rank_restricted_full": int(rq),
        "rank_thinned": int(rv),
        "rank_ratio_thinned_over_restricted": float(rv / rq),
        "overlap_trace": tr_pq,
        "overlap_fraction_min_rank": float(tr_pq / min(rq, rv)),
        "normalized_projector_distance": normalized,
        "mean_principal_cosine": float(np.mean(s)) if len(s) else 0.0,
        "min_principal_cosine": float(np.min(s)) if len(s) else 0.0,
    }


def best_rank_match(q: np.ndarray, evals: np.ndarray, u: np.ndarray) -> dict:
    order = np.argsort(np.abs(evals))[::-1]
    u = u[:, order]
    m = u.shape[0]
    target = q.shape[1]
    # Search broadly around the target rank, without using entropy or source cutoff.
    kmin = max(2, int(math.floor(0.45 * target)))
    kmax = min(m - 2, int(math.ceil(1.75 * target)))
    rows = []
    for k in range(kmin, kmax + 1):
        comp = compare_subspaces(q, u[:, :k])
        rows.append((comp["normalized_projector_distance"], k, comp))
    err, k, comp = min(rows, key=lambda x: x[0])
    return {
        "best_rank": int(k),
        "best_normalized_projector_distance": float(err),
        "best_overlap_fraction_min_rank": comp["overlap_fraction_min_rank"],
        "best_mean_principal_cosine": comp["mean_principal_cosine"],
    }


def run(n: int, thinning: float, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    uv = sprinkle_diamond(n, rng)
    c = causal_matrix(uv)
    source_cutoff_full = math.sqrt(n) / (4.0 * math.pi)
    evals_full, vfull = spectral_basis(c, source_cutoff_full)

    mask = rng.random(n) < thinning
    idx = np.flatnonzero(mask)
    m = int(len(idx))
    if m < 64:
        raise RuntimeError("thinned causal set too small")
    c2 = c[np.ix_(idx, idx)]
    j2 = 0.5j * (c2 - c2.T)
    evals2, u2 = linalg.eigh(j2, check_finite=False)
    source_cutoff_thin = math.sqrt(m) / (4.0 * math.pi)
    keep2 = np.abs(evals2) >= source_cutoff_thin
    vthin_source = u2[:, keep2]

    qrestricted = orthonormal_restricted_span(vfull[idx, :])
    source_comparison = compare_subspaces(qrestricted, vthin_source)
    best = best_rank_match(qrestricted, evals2, u2)

    return {
        "test": "BH003_SOURCE_SECTOR_THINNING_DIAGNOSTIC",
        "n_full": n,
        "n_thinned": m,
        "requested_thinning": thinning,
        "realized_density_ratio": m / n,
        "seed": seed,
        "source_cutoff_full": source_cutoff_full,
        "source_cutoff_thinned": source_cutoff_thin,
        "source_sector": source_comparison,
        "best_spectral_rank_control": best,
        "source_distance_over_best_distance": (
            source_comparison["normalized_projector_distance"] /
            max(best["best_normalized_projector_distance"], 1e-15)
        ),
        "claim_lock": (
            "Diagnostic of the already-known source-defined BH-003 sector under Bernoulli thinning. "
            "No entropy and no regulator fitting are performed."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--thinning", type=float, required=True)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    out = run(a.n, a.thinning, a.seed)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
