#!/usr/bin/env python3
"""Joint BH-003 test: sector stability versus heterogeneous closure.

For one 1+1D causal-set sprinkling, define the frozen massless source sector P0
from the SSEE spectral rule |lambda(iDelta_0)| >= sqrt(N)/(4 pi).  For each
mass deformation mu=m^2/rho, independently apply the same source rule to the
deformed commutator iDelta_mu and compare that sector P_mu with P0.  On the
same realization, evaluate heterogeneous composition closure using the frozen
P0 for both orders G_0->G_mu and G_mu->G_0, against rank-matched Haar controls.

This asks whether preservation of source-sector identity is associated with
suppression of discarded-sector return.  It does not derive the source rule and
is not a quantum-gravity dynamics claim.
"""
from __future__ import annotations

import argparse, json, math
from pathlib import Path
import numpy as np
from scipy import linalg

from causal_set_heterogeneous_mass_composition import (
    sprinkle_diamond, causal_matrix, massive_retarded, random_basis, metrics
)


def source_basis_from_retarded(g: np.ndarray, cutoff: float) -> tuple[np.ndarray, np.ndarray]:
    idelta = 1j * (g - g.T)
    evals, evecs = linalg.eigh(idelta, check_finite=False)
    keep = np.abs(evals) >= cutoff
    return evecs[:, keep], evals


def compare_subspaces(a: np.ndarray, b: np.ndarray) -> dict:
    ra, rb = a.shape[1], b.shape[1]
    if min(ra, rb) < 1:
        raise RuntimeError("empty source sector")
    s = linalg.svdvals(a.conj().T @ b, check_finite=False)
    s = np.clip(s, 0.0, 1.0)
    trpq = float(np.sum(s * s))
    dist2 = max(0.0, ra + rb - 2.0 * trpq)
    return {
        "rank_massless": int(ra),
        "rank_deformed": int(rb),
        "rank_delta": int(rb - ra),
        "overlap_fraction_min_rank": float(trpq / min(ra, rb)),
        "mean_principal_cosine": float(np.mean(s)),
        "min_principal_cosine": float(np.min(s)),
        "normalized_projector_distance": float(math.sqrt(dist2 / max(ra + rb, 1))),
    }


def closure_with_controls(g1, g2, p0, rng, nrandom):
    pleak, pret = metrics(g1, g2, p0)
    rl, rr = [], []
    for _ in range(nrandom):
        vr = random_basis(g1.shape[0], p0.shape[1], rng)
        x, y = metrics(g1, g2, vr)
        rl.append(x); rr.append(y)
    rl = np.asarray(rl); rr = np.asarray(rr)
    return {
        "source_leakage": pleak,
        "source_return_defect": pret,
        "mean_random_leakage": float(rl.mean()),
        "mean_random_return_defect": float(rr.mean()),
        "leakage_improvement": float(rl.mean()/pleak) if pleak > 0 else None,
        "return_improvement": float(rr.mean()/pret) if pret > 0 else None,
        "fraction_random_worse_leakage": float(np.mean(rl > pleak)),
        "fraction_random_worse_return": float(np.mean(rr > pret)),
    }


def run(n: int, seed: int, mus: list[float], nrandom: int) -> dict:
    rng = np.random.default_rng(seed)
    uv = sprinkle_diamond(n, rng)
    c = causal_matrix(uv)
    cutoff = math.sqrt(n)/(4.0*math.pi)
    g0 = massive_retarded(c, 0.0)
    p0, _ = source_basis_from_retarded(g0, cutoff)
    if p0.shape[1] < 2 or p0.shape[1] >= n:
        raise RuntimeError("invalid massless source-sector rank")

    rows = []
    for mu in mus:
        gm = massive_retarded(c, mu)
        pm, _ = source_basis_from_retarded(gm, cutoff)
        stability = compare_subspaces(p0, pm)
        # deterministic independent control streams per mu/order while keeping geometry fixed
        rng01 = np.random.default_rng(seed * 1000003 + int(round(mu*1e6)) + 17)
        rng10 = np.random.default_rng(seed * 1000003 + int(round(mu*1e6)) + 31)
        c01 = closure_with_controls(g0, gm, p0, rng01, nrandom)
        c10 = closure_with_controls(gm, g0, p0, rng10, nrandom)
        rows.append({
            "mu": float(mu),
            "operator_relative_difference": float(linalg.norm(gm-g0,'fro')/max(linalg.norm(g0,'fro'),1e-30)),
            "stability": stability,
            "closure_0_to_mu": c01,
            "closure_mu_to_0": c10,
            "mean_return_improvement_both_orders": float(np.mean([c01['return_improvement'], c10['return_improvement']])),
            "mean_fraction_random_worse_return_both_orders": float(np.mean([c01['fraction_random_worse_return'], c10['fraction_random_worse_return']])),
        })
    return {
        "test": "CAUSAL_SET_SECTOR_STABILITY_CLOSURE_JOINT",
        "n": n, "seed": seed, "cutoff": cutoff,
        "massless_rank": int(p0.shape[1]), "n_random_per_order": nrandom,
        "rows": rows,
        "claim_lock": (
            "Joint structural diagnostic on the same 1+1D causal-set realization. "
            "P0 is frozen by the massless source SSEE spectral rule; P_mu is used only to diagnose "
            "sector identity, never to tune the closure test. Association is descriptive, not a derivation."
        )
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--n', type=int, required=True)
    p.add_argument('--seed', type=int, required=True)
    p.add_argument('--mus', type=str, default='0.01,0.03,0.06,0.10,0.15')
    p.add_argument('--n-random', type=int, default=32)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    mus = [float(x) for x in a.mus.split(',') if x.strip()]
    out = run(a.n, a.seed, mus, a.n_random)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
