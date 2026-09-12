#!/usr/bin/env python3
"""Shared-unitary orientation-null test for a pinned Lorentzian EPRL vertex pair.

The train projector is frozen from the Dl=0 all-zero partial slice exactly as in
the exhaustive cross-shell diagnostic. For each Dl=1 -> Dl=0 holdout pair, the
same Haar unitary U is applied by similarity to both 2x2 holdout operators,

    A1 -> U^† A1 U,  A2 -> U^† A2 U,

while the train-defined projector P is kept fixed. This preserves the spectrum
of each holdout operator and their joint similarity relation while scrambling
only their orientation relative to P.

The test therefore asks whether orientation relative to the source-derived
retained sector is independent composition-closure data in this one-vertex
Lorentzian EPRL realization. It is not a full spinfoam gluing/refinement test.
"""
from __future__ import annotations

import argparse, itertools, json
from pathlib import Path
import numpy as np

from eprl_crossshell_exhaustive import load_sl2t, top_basis, metrics, partial


def haar_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    phase = np.ones_like(d, dtype=np.complex128)
    nz = np.abs(d) > 0
    phase[nz] = d[nz] / np.abs(d[nz])
    return q @ np.diag(np.conj(phase))


def run(t0: np.ndarray, t1: np.ndarray, nnull: int, seed: int, gamma: float) -> dict:
    rng = np.random.default_rng(seed)
    bitrows = list(itertools.product((0, 1), repeat=3))
    rows = []

    for open_axes in itertools.combinations(range(5), 2):
        train = partial(t0, open_axes, (0, 0, 0))
        p = top_basis(train, 1)

        for b1 in bitrows:
            a1 = np.asarray(partial(t1, open_axes, b1), np.complex128)
            for b2 in bitrows:
                a2 = np.asarray(partial(t0, open_axes, b2), np.complex128)
                _, source_return = metrics(a1, a2, p)
                null_returns = np.empty(nnull, dtype=float)
                for k in range(nnull):
                    u = haar_unitary(a1.shape[0], rng)
                    b1u = u.conj().T @ a1 @ u
                    b2u = u.conj().T @ a2 @ u
                    _, null_returns[k] = metrics(b1u, b2u, p)

                eps = np.finfo(float).eps
                mean_null = float(np.mean(null_returns))
                median_null = float(np.median(null_returns))
                rows.append({
                    "open_axes": list(open_axes),
                    "dl1_bits": "".join(map(str, b1)),
                    "dl0_bits": "".join(map(str, b2)),
                    "source_return_defect": float(source_return),
                    "null_mean_return_defect": mean_null,
                    "null_median_return_defect": median_null,
                    "mean_return_improvement": float(mean_null / max(source_return, eps)),
                    "median_return_improvement": float(median_null / max(source_return, eps)),
                    "fraction_null_worse_return": float(np.mean(null_returns > source_return)),
                })

    mean_imp = np.asarray([r["mean_return_improvement"] for r in rows])
    med_imp = np.asarray([r["median_return_improvement"] for r in rows])
    frac = np.asarray([r["fraction_null_worse_return"] for r in rows])
    prior = next(
        r for r in rows
        if r["open_axes"] == [0, 1] and r["dl1_bits"] == "001" and r["dl0_bits"] == "111"
    )

    natural_support = bool(np.median(med_imp) > 1.0 and np.mean(frac > 0.5) > 0.5)
    strong_support = bool(np.median(med_imp) > 1.0 and np.mean(frac > 0.5) > 0.6)

    return {
        "test": "LORENTZIAN_EPRL_SHARED_UNITARY_ORIENTATION_NULL",
        "status": "PASS_EXECUTION",
        "gamma": gamma,
        "n_cases": len(rows),
        "n_null_per_case": nnull,
        "decision_rule_preregistered": {
            "natural_support": "median(case median-null/source return improvement) > 1 and fraction(cases with majority null worse) > 0.5",
            "strong_support": "same median condition and fraction(cases with majority null worse) > 0.6",
            "gravity_side_refutation": "median improvement <= 1 and fraction majority-null-worse <= 0.5"
        },
        "summary": {
            "median_case_mean_return_improvement": float(np.median(mean_imp)),
            "median_case_median_return_improvement": float(np.median(med_imp)),
            "fraction_cases_mean_improvement_gt_1": float(np.mean(mean_imp > 1.0)),
            "fraction_cases_median_improvement_gt_1": float(np.mean(med_imp > 1.0)),
            "fraction_cases_majority_null_worse": float(np.mean(frac > 0.5)),
            "mean_fraction_null_worse": float(np.mean(frac)),
            "natural_support": natural_support,
            "strong_support": strong_support,
        },
        "prior_slice_no_postselection": prior,
        "cases": rows,
        "claim_lock": (
            "Shared-unitary similarity preserves each 2x2 holdout spectrum and their joint similarity relation while "
            "scrambling orientation relative to the frozen train-derived rank-1 projector. This is a one-vertex "
            "Lorentzian EPRL structural diagnostic, not full spinfoam gluing, refinement, GR recovery, or a QG theory claim."
        ),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--dl0", type=Path, required=True)
    p.add_argument("--dl1", type=Path, required=True)
    p.add_argument("--gamma", type=float, required=True)
    p.add_argument("--n-null", type=int, default=256)
    p.add_argument("--seed", type=int, default=20260919)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()

    out = run(load_sl2t(a.dl0), load_sl2t(a.dl1), a.n_null, a.seed, a.gamma)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out["summary"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
