#!/usr/bin/env python3
"""ITER178 independent critic.

Recomputes the frozen mass-deformation selector from the same deterministic
sprinkling, but evaluates subspace distance through principal singular values,
i.e. the low-rank orthoprojector identity
||P0-Pm||_F^2/(2r) = 1 - sum(sigma(U0^* Um)^2)/r.
"""

from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy import linalg

FRACTIONS = [0.04, 0.06, 0.09, 0.13, 0.18, 0.25, 0.35, 0.48, 0.65, 0.82]
MASSES = [0.0, 2.0, 5.0]


def points(n: int, seed: int) -> np.ndarray:
    rng = np.random.Generator(np.random.PCG64(seed))
    return rng.uniform(0.0, 1.0, size=(n, 2))


def order_matrix(x: np.ndarray) -> np.ndarray:
    return np.logical_and(
        x[:, 0, None] < x[:, 0][None, :],
        x[:, 1, None] < x[:, 1][None, :],
    ).astype(np.float64)


def retarded(c: np.ndarray, m: float, n: int) -> np.ndarray:
    k = c * 0.5
    b = np.eye(n, dtype=float) + (m * m / float(n)) * k
    # Right solve K B^{-1}, expressed as transposed left solve.
    return np.linalg.solve(b.T, k.T).T


def ordered_eigensystem(c: np.ndarray, m: float) -> tuple[np.ndarray, np.ndarray]:
    k = retarded(c, m, c.shape[0])
    h = 1j * (k - k.T)
    w, u = np.linalg.eigh(h)
    idx = np.argsort(-np.abs(w), kind="stable")
    return w[idx], u[:, idx]


def rank_for_fraction(n: int, f: float) -> int:
    r = 2 * int(np.rint(f * n / 2.0))
    cap = n - 4 if n % 2 == 0 else n - 3
    return int(np.clip(r, 4, cap))


def projector_distance_from_principal_values(u: np.ndarray, v: np.ndarray) -> float:
    r = u.shape[1]
    s = linalg.svdvals(u.conj().T @ v, check_finite=False)
    value = (2.0 * r - 2.0 * float(np.sum(s * s))) / (2.0 * r)
    return float(np.clip(value, 0.0, 1.0))


def frozen_break(curve: list[float]) -> dict:
    slopes = [
        (curve[i + 1] - curve[i]) /
        (math.log(FRACTIONS[i + 1]) - math.log(FRACTIONS[i]))
        for i in range(len(FRACTIONS) - 1)
    ]
    candidates = sorted(
        [(float(s), i) for i, s in enumerate(slopes) if math.isfinite(s) and s > 0],
        reverse=True,
    )
    if not candidates:
        return {
            "resolved": False,
            "break_interval_index": None,
            "break_interval": None,
            "peak_slope": None,
            "second_positive_slope": None,
            "peak_ratio": None,
            "slopes": slopes,
        }
    peak, i = candidates[0]
    second = candidates[1][0] if len(candidates) > 1 else 0.0
    ratio = None if second <= 0 else peak / second
    dominance = True if second <= 0 else ratio >= 1.25
    resolved = bool(i not in (0, len(slopes) - 1) and peak > 0 and dominance)
    return {
        "resolved": resolved,
        "break_interval_index": i,
        "break_interval": [FRACTIONS[i], FRACTIONS[i + 1]],
        "peak_slope": peak,
        "second_positive_slope": second,
        "peak_ratio": ratio,
        "slopes": slopes,
    }


def run(n: int, seed: int) -> dict:
    x = points(n, seed)
    c = order_matrix(x)
    eig = {m: ordered_eigensystem(c, m) for m in MASSES}

    ranks, instability, cutoffs = [], [], []
    for f in FRACTIONS:
        r = rank_for_fraction(n, f)
        ranks.append(r)
        cutoffs.append(float(abs(eig[0.0][0][r - 1])))
        u0 = eig[0.0][1][:, :r]
        vals = [
            projector_distance_from_principal_values(u0, eig[m][1][:, :r])
            for m in (2.0, 5.0)
        ]
        instability.append(float(np.mean(vals)))

    choice = frozen_break(instability)
    selected_fraction = None
    selected_cutoff = None
    source_cutoff = math.sqrt(n) / (4.0 * math.pi)
    source_ratio = None
    if choice["break_interval_index"] is not None:
        i = int(choice["break_interval_index"])
        selected_fraction = math.sqrt(FRACTIONS[i] * FRACTIONS[i + 1])
        selected_cutoff = math.sqrt(cutoffs[i] * cutoffs[i + 1])
        source_ratio = selected_cutoff / source_cutoff

    return {
        "iteration": "ITER178",
        "lane": "critic",
        "n": n,
        "seed": seed,
        "masses": MASSES,
        "fractions": FRACTIONS,
        "ranks": ranks,
        "mass_deformation_instability": instability,
        "massless_abs_eigenvalue_cutoffs": cutoffs,
        "selection": choice,
        "selected_fraction": selected_fraction,
        "selected_cutoff": selected_cutoff,
        "post_selection_source_cutoff": source_cutoff,
        "post_selection_selected_to_source_ratio": source_ratio,
        "claim_lock": (
            "Independent principal-angle/projector-distance critic; entropy and source "
            "cutoff are excluded from selector construction."
        ),
    }


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
