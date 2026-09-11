#!/usr/bin/env python3
"""Entropy-blind spectral-break test for BH-003.

The cutoff is inferred only from the positive spectrum of iDelta by a frozen
piecewise-linear knee rule in log(rank)-log(lambda) space.  No entropy value,
continuum entropy coefficient, or source cutoff formula is used to choose the
break.  The source rule sqrt(N)/(4*pi) is computed only after the blind choice
for diagnostic comparison.

The test applies the blind rule twice: first on the parent causal diamond and
then on the restricted post-parent-truncation operator in the subdiamond.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy import linalg

from causal_set_ssee_2d_reproduction import (
    sprinkle_diamond,
    sj_matrices,
    nested_indices,
    spectral_project,
    ssee,
)


def _line_sse(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    a = np.column_stack([x, np.ones_like(x)])
    coef, *_ = np.linalg.lstsq(a, y, rcond=None)
    pred = a @ coef
    sse = float(np.sum((y - pred) ** 2))
    return sse, float(coef[0]), float(coef[1])


def blind_spectral_break(i_delta: np.ndarray) -> dict:
    """Frozen entropy-blind two-line knee detector on positive iDelta modes."""
    evals = linalg.eigvalsh(i_delta, check_finite=False)
    vals = np.sort(evals[evals > 1e-11])[::-1]
    m = len(vals)
    if m < 16:
        raise RuntimeError("too few positive spectral modes for blind break")

    # Remove only the extreme endpoints where finite-size/numerical effects are
    # largest.  This trimming rule is fixed before looking at entropy.
    lo = max(2, int(math.floor(0.04 * m)))
    hi = min(m - 2, int(math.ceil(0.96 * m)))
    vals_t = vals[lo:hi]
    ranks_t = np.arange(lo + 1, hi + 1, dtype=float)
    x = np.log(ranks_t)
    y = np.log(vals_t)
    mt = len(vals_t)
    min_seg = max(5, int(math.ceil(0.15 * mt)))

    single_sse, single_slope, _ = _line_sse(x, y)
    best = None
    for k in range(min_seg, mt - min_seg + 1):
        sse1, slope1, _ = _line_sse(x[:k], y[:k])
        sse2, slope2, _ = _line_sse(x[k:], y[k:])
        total = sse1 + sse2
        # Tiny complexity penalty prevents unstable endpoint splits.
        score = total * (1.0 + 2.0 / mt)
        if best is None or score < best[0]:
            best = (score, total, k, slope1, slope2)

    assert best is not None
    _, piece_sse, k, slope1, slope2 = best
    idx_left = lo + k - 1
    idx_right = lo + k
    cutoff = float(math.sqrt(vals[idx_left] * vals[idx_right]))
    improvement = 0.0 if single_sse <= 0 else 1.0 - piece_sse / single_sse
    return {
        "cutoff": cutoff,
        "positive_modes": int(m),
        "break_rank_positive": int(idx_right + 1),
        "single_slope": single_slope,
        "pre_break_slope": slope1,
        "post_break_slope": slope2,
        "piecewise_sse_improvement": float(improvement),
        "trim_lo": int(lo),
        "trim_hi": int(hi),
    }


def run(n: int, seed: int, side_ratio: float) -> dict:
    rng = np.random.default_rng(seed)
    uv = sprinkle_diamond(n, rng)
    i_delta, w, _, _ = sj_matrices(uv)
    idx = nested_indices(uv, side_ratio)
    n_sub = int(len(idx))
    if n_sub < 16:
        raise RuntimeError("subdiamond too small")

    # Raw entropy for diagnostics only; it is not used by the cutoff detector.
    jr = i_delta[np.ix_(idx, idx)]
    wr = w[np.ix_(idx, idx)]
    s_raw, _ = ssee(wr, jr)

    parent_break = blind_spectral_break(i_delta)
    jpt, wpt, kept_parent = spectral_project(i_delta, w, parent_break["cutoff"])
    jr1 = jpt[np.ix_(idx, idx)]
    wr1 = wpt[np.ix_(idx, idx)]

    sub_break = blind_spectral_break(jr1)
    jst, wst, kept_sub = spectral_project(jr1, wr1, sub_break["cutoff"])
    s_blind, blind_modes = ssee(wst, jst, support_rtol=1e-9)

    source_parent = math.sqrt(n) / (4.0 * math.pi)
    source_sub = math.sqrt(n_sub) / (4.0 * math.pi)
    return {
        "test": "BH003_ENTROPY_BLIND_SPECTRAL_BREAK",
        "n_parent": n,
        "n_sub": n_sub,
        "seed": seed,
        "side_ratio": side_ratio,
        "raw_entropy": float(s_raw),
        "blind_truncated_entropy": float(s_blind),
        "blind_parent": parent_break,
        "blind_sub": sub_break,
        "retained_parent_modes_both_signs": int(kept_parent),
        "retained_sub_modes_both_signs": int(kept_sub),
        "blind_generalized_modes": int(blind_modes),
        "diagnostic_source_parent_cutoff": source_parent,
        "diagnostic_source_sub_cutoff": source_sub,
        "blind_to_source_parent_cutoff_ratio": parent_break["cutoff"] / source_parent,
        "blind_to_source_sub_cutoff_ratio": sub_break["cutoff"] / source_sub,
        "log_size_proxy": math.log(math.sqrt(n_sub) / (4.0 * math.pi)),
        "claim_lock": (
            "Entropy-blind spectral-knee test in the same 1+1D free scalar causal-set "
            "realization.  Source cutoff is diagnostic only and never selects the break."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--side-ratio", type=float, default=0.5)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    out = run(a.n, a.seed, a.side_ratio)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
