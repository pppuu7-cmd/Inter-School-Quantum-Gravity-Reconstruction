#!/usr/bin/env python3
"""2D causal-set spacetime entanglement entropy reproduction experiment.

Scope
-----
Free massless scalar field on a Poisson-sprinkled 1+1D causal diamond, using:
  * causal matrix C;
  * retarded Green matrix G_R = C/2;
  * Pauli-Jordan operator Delta = G_R - G_R^T;
  * Sorkin-Johnston Wightman function = positive spectral part of i Delta;
  * SSEE generalized eigenvalue formula on a nested causal diamond;
  * source-motivated double spectral cutoff |lambda(iDelta)| >= sqrt(N)/(4 pi).

The experiment is intended to reproduce the qualitative source result:
raw causal-set SSEE shows spacetime-volume scaling, whereas the pre-declared
spectral cutoff restores continuum-like logarithmic/area-law scaling in 1+1D.

This is not a quantum-gravity dynamics calculation and does not decide whether
the raw volume law or truncated continuum-like law is fundamentally physical.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy import linalg


def sprinkle_diamond(n: int, rng: np.random.Generator) -> np.ndarray:
    # In null coordinates (u,v), a 1+1D causal diamond is a rectangle.
    # Uniform (u,v) sampling is uniform with respect to the flat volume form.
    return rng.random((n, 2))


def causal_matrix(uv: np.ndarray) -> np.ndarray:
    u = uv[:, 0]
    v = uv[:, 1]
    return ((u[:, None] < u[None, :]) & (v[:, None] < v[None, :])).astype(float)


def sj_matrices(uv: np.ndarray):
    c = causal_matrix(uv)
    delta = 0.5 * (c - c.T)
    i_delta = 1j * delta
    evals, evecs = linalg.eigh(i_delta, check_finite=False)
    positive = evals > 1e-12
    w = (evecs[:, positive] * evals[positive]) @ evecs[:, positive].conj().T
    return i_delta, w, evals, evecs


def spectral_project(i_delta: np.ndarray, w: np.ndarray, cutoff: float):
    evals, evecs = linalg.eigh(i_delta, check_finite=False)
    keep = np.abs(evals) >= cutoff
    vk = evecs[:, keep]
    jk = evals[keep]
    # Orthogonal projection of both operators to the retained spectral subspace.
    i_delta_t = (vk * jk) @ vk.conj().T
    w_t = vk @ (vk.conj().T @ w @ vk) @ vk.conj().T
    return i_delta_t, w_t, int(np.sum(keep))


def ssee(w: np.ndarray, i_delta: np.ndarray, support_rtol: float = 1e-10):
    # Solve W v = lambda (i Delta) v on the non-null support of iDelta.
    # Working in the spectral support is more stable than a singular generalized
    # QZ solve and implements the exclusion of ker(iDelta).
    je, ju = linalg.eigh(i_delta, check_finite=False)
    scale = max(float(np.max(np.abs(je))), 1.0)
    keep = np.abs(je) > support_rtol * scale
    if np.sum(keep) == 0:
        return 0.0, 0
    uk = ju[:, keep]
    jk = je[keep]
    wk = uk.conj().T @ w @ uk
    m = (1.0 / jk)[:, None] * wk
    lam = linalg.eigvals(m, check_finite=False)
    finite = np.isfinite(lam)
    lam = lam[finite]
    lam = lam[np.abs(lam.imag) < 1e-6].real
    lam = lam[np.abs(lam) > 1e-12]
    entropy = float(np.sum(lam * np.log(np.abs(lam))).real)
    return entropy, int(len(lam))


def nested_indices(uv: np.ndarray, side_ratio: float) -> np.ndarray:
    if not 0.0 < side_ratio < 1.0:
        raise ValueError("side_ratio must lie in (0,1)")
    lo = 0.5 * (1.0 - side_ratio)
    hi = 0.5 * (1.0 + side_ratio)
    return np.where(
        (uv[:, 0] >= lo)
        & (uv[:, 0] <= hi)
        & (uv[:, 1] >= lo)
        & (uv[:, 1] <= hi)
    )[0]


def run(n: int, seed: int, side_ratio: float = 0.5) -> dict:
    if n < 32:
        raise ValueError("n must be >= 32")
    rng = np.random.default_rng(seed)
    uv = sprinkle_diamond(n, rng)
    i_delta, w, evals, _ = sj_matrices(uv)
    idx = nested_indices(uv, side_ratio)
    n_sub = int(len(idx))
    if n_sub < 8:
        raise RuntimeError("nested diamond contains too few sprinkled elements")

    # Raw SSEE in the nested region.
    jr = i_delta[np.ix_(idx, idx)]
    wr = w[np.ix_(idx, idx)]
    s_raw, raw_modes = ssee(wr, jr)

    # First source-motivated spectral truncation in the parent diamond.
    cutoff_parent = math.sqrt(n) / (4.0 * math.pi)
    j_parent_t, w_parent_t, kept_parent = spectral_project(
        i_delta, w, cutoff_parent
    )

    # Restrict after the parent truncation, then apply the second truncation in
    # the nested diamond, matching the two-stage prescription.
    jr_t = j_parent_t[np.ix_(idx, idx)]
    wr_t = w_parent_t[np.ix_(idx, idx)]
    cutoff_sub = math.sqrt(n_sub) / (4.0 * math.pi)
    j_sub_t, w_sub_t, kept_sub = spectral_project(jr_t, wr_t, cutoff_sub)
    s_trunc, trunc_modes = ssee(w_sub_t, j_sub_t, support_rtol=1e-9)

    positive_spectrum = np.sort(evals[evals > 1e-12])[::-1]
    n_positive_above_rule = int(np.sum(positive_spectrum >= cutoff_parent))

    return {
        "test": "CAUSAL_SET_SSEE_2D_REPRODUCTION",
        "n_parent": n,
        "n_sub": n_sub,
        "seed": seed,
        "side_ratio": side_ratio,
        "raw_entropy": s_raw,
        "truncated_entropy": s_trunc,
        "cutoff_parent": cutoff_parent,
        "cutoff_sub": cutoff_sub,
        "retained_parent_modes_both_signs": kept_parent,
        "retained_sub_modes_both_signs": kept_sub,
        "raw_generalized_modes": raw_modes,
        "truncated_generalized_modes": trunc_modes,
        "positive_parent_modes_above_rule": n_positive_above_rule,
        "log_cutoff_proxy": math.log(math.sqrt(n_sub) / (4.0 * math.pi)),
        "claim_lock": (
            "Source-inspired 1+1D free-field causal-set reproduction only. "
            "It does not establish a fundamental entropy law or quantum-gravity dynamics."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=256)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--side-ratio", type=float, default=0.5)
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    out = run(a.n, a.seed, a.side_ratio)
    text = json.dumps(out, indent=2, sort_keys=True)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
