#!/usr/bin/env python3
"""ITER178 researcher: entropy-blind mass-deformation spectral-stability selector.

Frozen by prereg/ITER178_RC007_MASS_DEFORMATION_SPECTRAL_STABILITY_SELECTOR_2026-09-19.md.
The source SSEE cutoff is evaluated only after the dynamical break is selected.
"""

from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy import linalg

FRACTIONS = [0.04, 0.06, 0.09, 0.13, 0.18, 0.25, 0.35, 0.48, 0.65, 0.82]
MASSES = [0.0, 2.0, 5.0]


def sprinkle(n: int, seed: int) -> np.ndarray:
    return np.random.default_rng(seed).random((n, 2))


def causal_matrix(uv: np.ndarray) -> np.ndarray:
    u, v = uv[:, 0], uv[:, 1]
    return ((u[:, None] < u[None, :]) & (v[:, None] < v[None, :])).astype(float)


def massive_retarded(c: np.ndarray, mass: float, rho: float) -> np.ndarray:
    k0 = 0.5 * c
    a = np.eye(c.shape[0]) + (mass * mass / rho) * k0
    return linalg.solve(a.T, k0.T, assume_a="gen", check_finite=False).T


def spectral_data(c: np.ndarray, mass: float, rho: float) -> tuple[np.ndarray, np.ndarray]:
    gr = massive_retarded(c, mass, rho)
    i_delta = 1j * (gr - gr.T)
    vals, vecs = linalg.eigh(i_delta, check_finite=False)
    order = np.argsort(np.abs(vals))[::-1]
    return vals[order], vecs[:, order]


def even_rank(n: int, f: float) -> int:
    r = int(round((f * n) / 2.0)) * 2
    return max(4, min(n - 4 if n % 2 == 0 else n - 3, r))


def select_break(instabilities: list[float]) -> dict:
    slopes = []
    for i in range(len(FRACTIONS) - 1):
        den = math.log(FRACTIONS[i + 1]) - math.log(FRACTIONS[i])
        slopes.append((instabilities[i + 1] - instabilities[i]) / den)

    positive = [(s, i) for i, s in enumerate(slopes) if s > 0 and math.isfinite(s)]
    if not positive:
        return {
            "resolved": False, "break_interval_index": None, "break_interval": None,
            "peak_slope": None, "second_positive_slope": None, "peak_ratio": None,
            "slopes": slopes,
        }

    positive.sort(reverse=True)
    peak, idx = positive[0]
    second = positive[1][0] if len(positive) > 1 else 0.0
    ratio = float("inf") if second <= 0 else peak / second
    resolved = bool(idx not in (0, len(slopes) - 1) and peak > 0 and ratio >= 1.25)
    return {
        "resolved": resolved,
        "break_interval_index": idx,
        "break_interval": [FRACTIONS[idx], FRACTIONS[idx + 1]],
        "peak_slope": peak,
        "second_positive_slope": second,
        "peak_ratio": ratio,
        "slopes": slopes,
    }


def run(n: int, seed: int) -> dict:
    uv = sprinkle(n, seed)
    c = causal_matrix(uv)
    rho = float(n)
    spec = {m: spectral_data(c, m, rho) for m in MASSES}

    ranks, cutoffs, instabilities, null_instabilities = [], [], [], []
    perm = np.roll(np.arange(n), 1)

    for f in FRACTIONS:
        r = even_rank(n, f)
        ranks.append(r)
        v0, u0 = spec[0.0]
        cutoff = float(abs(v0[r - 1]))
        cutoffs.append(cutoff)
        u0r = u0[:, :r]

        ds = []
        for m in (2.0, 5.0):
            um = spec[m][1][:, :r]
            overlap2 = float(np.sum(np.abs(u0r.conj().T @ um) ** 2).real)
            ds.append(max(0.0, min(1.0, 1.0 - overlap2 / r)))
        instabilities.append(float(sum(ds) / len(ds)))

        u5_perm = spec[5.0][1][perm, :r]
        null_overlap2 = float(np.sum(np.abs(u0r.conj().T @ u5_perm) ** 2).real)
        null_instabilities.append(max(0.0, min(1.0, 1.0 - null_overlap2 / r)))

    sel = select_break(instabilities)
    selected_fraction = None
    selected_cutoff = None
    source_cutoff = math.sqrt(n) / (4.0 * math.pi)
    source_ratio = None
    if sel["break_interval_index"] is not None:
        i = int(sel["break_interval_index"])
        selected_fraction = math.sqrt(FRACTIONS[i] * FRACTIONS[i + 1])
        selected_cutoff = math.sqrt(cutoffs[i] * cutoffs[i + 1])
        source_ratio = selected_cutoff / source_cutoff

    out = {
        "iteration": "ITER178",
        "lane": "researcher",
        "n": n,
        "seed": seed,
        "rho": rho,
        "masses": MASSES,
        "fractions": FRACTIONS,
        "ranks": ranks,
        "mass_deformation_instability": instabilities,
        "adversarial_permuted_m5_instability": null_instabilities,
        "massless_abs_eigenvalue_cutoffs": cutoffs,
        "selection": sel,
        "selected_fraction": selected_fraction,
        "selected_cutoff": selected_cutoff,
        "post_selection_source_cutoff": source_cutoff,
        "post_selection_selected_to_source_ratio": source_ratio,
        "claim_lock": (
            "Entropy and the source cutoff do not enter selection. Source cutoff is computed "
            "only after the frozen mass-deformation break has been selected."
        ),
    }
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    out = run(a.n, a.seed)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
