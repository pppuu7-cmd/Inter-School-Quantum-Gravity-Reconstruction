#!/usr/bin/env python3
"""BH-003 entropy-blind scale-flow test from causal-set thinning.

No entropy observable and no source cutoff formula enters the inference.

For one sprinkled causal set:
1. diagonalize iDelta and define several nested UV spectral sectors by fixed
   retained fractions (these are probes, not a fitted physical cutoff);
2. Bernoulli-thin the causal set and form the induced causal matrix exactly;
3. restrict each full-set spectral projector to the retained elements;
4. among nested spectral projectors of the thinned iDelta, find the projector
   that best approximates that restricted operator in Frobenius norm;
5. infer the scale-flow exponent alpha from
      lambda_thin / lambda_full = (N_thin / N_full)^alpha.

If alpha is stable across density, thinning probability and probe rank, a native
spectral scale flow exists.  Only after inference is alpha compared with the
source SSEE exponent 1/2.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy import linalg

from causal_set_ssee_2d_reproduction import sprinkle_diamond, causal_matrix

PROBE_FRACTIONS = (0.08, 0.12, 0.18, 0.26, 0.36)


def spectral_decomposition(c: np.ndarray):
    j = 0.5j * (c - c.T)
    evals, u = linalg.eigh(j, check_finite=False)
    order = np.argsort(np.abs(evals))[::-1]
    return evals[order], u[:, order]


def midpoint_cutoff(abs_evals: np.ndarray, r: int) -> float:
    hi = max(float(abs_evals[r - 1]), 1e-300)
    lo = max(float(abs_evals[r]), 1e-300)
    return math.sqrt(hi * lo)


def best_thinned_projector(a: np.ndarray, v: np.ndarray) -> dict:
    """Approximate R=A A^* by nested thinned spectral projectors V_k V_k^*."""
    m = v.shape[0]
    gram = a.conj().T @ a
    r_norm2 = float(np.sum(np.abs(gram) ** 2))
    r_norm = math.sqrt(max(r_norm2, 1e-300))

    b = v.conj().T @ a
    row_energy = np.sum(np.abs(b) ** 2, axis=1)
    cum_overlap = np.cumsum(row_energy)

    best = None
    kmax = max(4, min(m - 2, int(math.floor(0.70 * m))))
    for k in range(2, kmax + 1, 2):
        # ||R-P_k||_F^2 = ||R||_F^2 + ||P_k||_F^2 - 2 Tr(P_k R)
        err2 = max(0.0, r_norm2 + k - 2.0 * float(cum_overlap[k - 1]))
        err = math.sqrt(err2) / r_norm
        if best is None or err < best[0]:
            best = (err, k, float(cum_overlap[k - 1]))
    if best is None:
        raise RuntimeError("no admissible thinned projector rank")
    return {
        "normalized_transfer_error": best[0],
        "thinned_rank": best[1],
        "projector_overlap_trace": best[2],
        "restricted_projector_frobenius": r_norm,
    }


def run(n: int, thinning: float, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    uv = sprinkle_diamond(n, rng)
    c = causal_matrix(uv)
    evals, u = spectral_decomposition(c)
    abs_e = np.abs(evals)

    keep = rng.random(n) < thinning
    idx = np.flatnonzero(keep)
    m = int(len(idx))
    if m < 64:
        raise RuntimeError("thinned causal set too small")
    c2 = c[np.ix_(idx, idx)]
    evals2, v = spectral_decomposition(c2)
    abs_e2 = np.abs(evals2)

    rows = []
    density_ratio = m / n
    for f in PROBE_FRACTIONS:
        r = int(round(f * n))
        r = max(4, min(n - 4, r))
        if r % 2:
            r += 1
        r = min(n - 4, r)

        # Restricted full-set retained subspace A.  We never use entropy here.
        a = u[idx, :r]
        match = best_thinned_projector(a, v)
        k = int(match["thinned_rank"])
        if k >= m:
            continue

        cf = midpoint_cutoff(abs_e, r)
        ct = midpoint_cutoff(abs_e2, k)
        alpha = math.log(ct / cf) / math.log(density_ratio)
        beta_rank = math.log(k / r) / math.log(density_ratio)
        rows.append({
            "probe_fraction_full": f,
            "full_rank": r,
            "thinned_rank": k,
            "full_cutoff": cf,
            "thinned_cutoff": ct,
            "alpha_cutoff_flow": alpha,
            "beta_rank_flow": beta_rank,
            **match,
        })

    alphas = np.array([x["alpha_cutoff_flow"] for x in rows], dtype=float)
    betas = np.array([x["beta_rank_flow"] for x in rows], dtype=float)
    errors = np.array([x["normalized_transfer_error"] for x in rows], dtype=float)
    return {
        "test": "BH003_THINNING_PROJECTOR_TRANSFER",
        "n_full": n,
        "n_thinned": m,
        "realized_density_ratio": density_ratio,
        "requested_thinning": thinning,
        "seed": seed,
        "probes": rows,
        "summary": {
            "median_alpha_cutoff_flow": float(np.median(alphas)),
            "mean_alpha_cutoff_flow": float(np.mean(alphas)),
            "std_alpha_across_probe_ranks": float(np.std(alphas)),
            "median_beta_rank_flow": float(np.median(betas)),
            "mean_transfer_error": float(np.mean(errors)),
            "max_transfer_error": float(np.max(errors)),
        },
        "posthoc_reference_only": {
            "source_ssee_cutoff_exponent": 0.5,
            "absolute_median_alpha_minus_half": float(abs(np.median(alphas) - 0.5)),
        },
        "claim_lock": (
            "Scale flow inferred only from restricted-projector transfer under causal-set thinning. "
            "The 1/2 source exponent is post-hoc and does not enter rank matching or cutoff inference."
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
