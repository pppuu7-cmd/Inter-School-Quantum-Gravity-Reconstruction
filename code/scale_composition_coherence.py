#!/usr/bin/env python3
"""Monte Carlo stress test for BH-001 scale/composition coherence.

For encoding E and decoding D define the coarse channel
    R(Phi) = D o Phi o E.
Sequential functoriality would require
    R(Phi2 o Phi1) = R(Phi2) o R(Phi1).
The exact defect is
    D o Phi2 o (I - E o D) o Phi1 o E.

The experiment compares random fine unitaries that leak out of the retained
subspace with block-preserving unitaries. This is a generic mathematical proxy,
not a quantum-gravity simulation.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def random_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2.0)
    q, r = np.linalg.qr(z)
    diag = np.diag(r)
    phases = np.where(np.abs(diag) > 0.0, diag / np.abs(diag), 1.0)
    return q * phases.conj()


def block_preserving_unitary(dc: int, df: int, rng: np.random.Generator) -> np.ndarray:
    if not 0 < dc < df:
        raise ValueError("require 0 < dc < df")
    u = np.zeros((df, df), dtype=complex)
    u[:dc, :dc] = random_unitary(dc, rng)
    u[dc:, dc:] = random_unitary(df - dc, rng)
    return u


def effective_superoperator(unitary: np.ndarray, encoding: np.ndarray) -> np.ndarray:
    df, dc = encoding.shape
    p = encoding @ encoding.conj().T
    q = np.eye(df, dtype=complex) - p
    tau = np.eye(dc, dtype=complex) / dc

    def apply(rho: np.ndarray) -> np.ndarray:
        fine = encoding @ rho @ encoding.conj().T
        out = unitary @ fine @ unitary.conj().T
        # CPTP decoder: retained block plus erased leakage replaced by tau.
        return encoding.conj().T @ out @ encoding + np.trace(q @ out) * tau

    sop = np.zeros((dc * dc, dc * dc), dtype=complex)
    for a in range(dc):
        for b in range(dc):
            rho = np.zeros((dc, dc), dtype=complex)
            rho[a, b] = 1.0
            out = apply(rho)
            sop[:, a + b * dc] = out.reshape(-1, order="F")
    return sop


def leakage_probability(unitary: np.ndarray, encoding: np.ndarray) -> float:
    df, dc = encoding.shape
    p = encoding @ encoding.conj().T
    q = np.eye(df, dtype=complex) - p
    return float(np.trace(q @ unitary @ p @ unitary.conj().T).real / dc)


def normalized_defect(a: np.ndarray, b: np.ndarray) -> float:
    denom = np.linalg.norm(a, ord="fro")
    if denom == 0.0:
        return float("inf")
    return float(np.linalg.norm(a - b, ord="fro") / denom)


def run(seed: int, trials: int, fine_dim: int = 4, coarse_dim: int = 2) -> dict:
    rng = np.random.default_rng(seed)
    if not 0 < coarse_dim < fine_dim:
        raise ValueError("require 0 < coarse_dim < fine_dim")
    encoding = np.eye(fine_dim, dtype=complex)[:, :coarse_dim]

    random_defects = []
    random_leakage = []
    preserving_defects = []
    preserving_leakage = []

    for _ in range(trials):
        u1 = random_unitary(fine_dim, rng)
        u2 = random_unitary(fine_dim, rng)
        r12 = effective_superoperator(u2 @ u1, encoding)
        r2 = effective_superoperator(u2, encoding)
        r1 = effective_superoperator(u1, encoding)
        random_defects.append(normalized_defect(r12, r2 @ r1))
        random_leakage.append(leakage_probability(u1, encoding))

        v1 = block_preserving_unitary(coarse_dim, fine_dim, rng)
        v2 = block_preserving_unitary(coarse_dim, fine_dim, rng)
        rv12 = effective_superoperator(v2 @ v1, encoding)
        rv2 = effective_superoperator(v2, encoding)
        rv1 = effective_superoperator(v1, encoding)
        preserving_defects.append(normalized_defect(rv12, rv2 @ rv1))
        preserving_leakage.append(leakage_probability(v1, encoding))

    random_defects = np.asarray(random_defects)
    random_leakage = np.asarray(random_leakage)
    preserving_defects = np.asarray(preserving_defects)
    preserving_leakage = np.asarray(preserving_leakage)

    correlation = float(np.corrcoef(random_defects, random_leakage)[0, 1])

    return {
        "test": "BH001_SCALE_COMPOSITION_COHERENCE_MONTE_CARLO",
        "seed": seed,
        "trials": trials,
        "fine_dim": fine_dim,
        "coarse_dim": coarse_dim,
        "random_mixing": {
            "mean_defect": float(random_defects.mean()),
            "median_defect": float(np.median(random_defects)),
            "p95_defect": float(np.quantile(random_defects, 0.95)),
            "mean_leakage": float(random_leakage.mean()),
            "defect_leakage_correlation": correlation,
        },
        "subspace_preserving": {
            "mean_defect": float(preserving_defects.mean()),
            "max_defect": float(preserving_defects.max()),
            "mean_leakage": float(preserving_leakage.mean()),
        },
        "derived_identity": "R(Phi2 o Phi1)-R(Phi2)oR(Phi1)=D o Phi2 o (I-E o D) o Phi1 o E",
        "interpretation": (
            "Sequential scale/composition coherence is non-generic. It becomes exact in "
            "this proxy when fine dynamics preserves the retained physical subspace."
        ),
        "claim_lock": (
            "Generic channel compression is only a methodological proxy. Application to "
            "a QG realization requires its native physical quotient and scale map."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--trials", type=int, default=500)
    parser.add_argument("--fine-dim", type=int, default=4)
    parser.add_argument("--coarse-dim", type=int, default=2)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    result = run(args.seed, args.trials, args.fine_dim, args.coarse_dim)
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
