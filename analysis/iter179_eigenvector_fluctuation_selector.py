#!/usr/bin/env python3
"""ITER179 Researcher: source-derived shared-core eigenvector persistence selector."""

from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy import linalg

M = 12
CORE_FRAC = 0.90
TOP_K = 10
ANCHOR_TOL = 1e-12
POS_TOL = 1e-12


def causal_matrix(uv: np.ndarray) -> np.ndarray:
    u = uv[:, 0]
    v = uv[:, 1]
    return ((u[:, None] < u[None, :]) & (v[:, None] < v[None, :])).astype(float)


def completion_seed(n: int, core_seed: int, q: int) -> int:
    return 10_000_000 + n * 10_000 + core_seed * 20 + q


def eigensystem(uv: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    c = causal_matrix(uv)
    h = 0.5j * (c - c.T)
    w, u = linalg.eigh(h, check_finite=False)
    pos = np.where(w > POS_TOL)[0]
    w = w[pos][::-1]
    u = u[:, pos][:, ::-1]
    return w, u


def top_mean_abs(v: np.ndarray) -> float:
    a = np.abs(v)
    k = min(TOP_K, len(a))
    if k == 0:
        return 0.0
    idx = np.argpartition(a, len(a) - k)[-k:]
    return float(np.mean(a[idx]))


def fit_line(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    a = np.column_stack([x, np.ones_like(x)])
    coef, *_ = np.linalg.lstsq(a, y, rcond=None)
    pred = a @ coef
    rss = float(np.sum((y - pred) ** 2))
    return float(coef[0]), float(coef[1]), rss


def bic(rss: float, n: int, p: int) -> float:
    r = max(float(rss), 1e-300)
    return float(n * math.log(r / n) + p * math.log(n))


def candidate_break(js: np.ndarray, rs: np.ndarray) -> dict:
    n = len(js)
    if n < 40:
        return {"candidate": None, "reason": "fewer_than_40_usable_modes"}
    b0, a0, rss0 = fit_line(js, rs)
    best = None
    for split in range(20, n - 19):
        xp, yp = js[:split], rs[:split]
        xs, ys = js[split:], rs[split:]
        bp, ap, rssp = fit_line(xp, yp)
        c = float(np.mean(ys))
        rsss = float(np.sum((ys - c) ** 2))
        total = rssp + rsss
        if best is None or total < best["rss"]:
            bs, ass, rss_tail_line = fit_line(xs, ys)
            k = int(js[split - 1])
            best = {
                "candidate": k,
                "split_position": split,
                "rss": total,
                "prefix_slope": bp,
                "prefix_intercept": ap,
                "suffix_constant": c,
                "suffix_line_slope": bs,
                "suffix_line_intercept": ass,
                "suffix_line_rss": rss_tail_line,
            }
    assert best is not None
    bic_single = bic(rss0, n, 2)
    bic_lc = bic(best["rss"], n, 4)
    delta_bic = bic_single - bic_lc
    basic = bool(
        delta_bic >= 10.0
        and best["prefix_slope"] < 0.0
        and abs(best["suffix_line_slope"]) <= 0.25 * abs(best["prefix_slope"])
    )
    best.update({
        "single_line_slope": b0,
        "single_line_intercept": a0,
        "single_line_rss": rss0,
        "bic_single": bic_single,
        "bic_line_constant": bic_lc,
        "delta_bic": delta_bic,
        "basic_resolved": basic,
    })
    return best


def persistence_curve(
    eigvecs: list[np.ndarray],
    nc: int,
    anchor: int,
    m_positive: int,
    omit: int | None = None,
) -> tuple[np.ndarray, np.ndarray, list[int]]:
    members = [q for q in range(len(eigvecs)) if q != omit]
    j_max = int(math.floor(0.80 * m_positive))
    js = []
    ratios = []
    unusable = []
    for j in range(5, j_max + 1):
        core_vectors = []
        individual = []
        okay = True
        for q in members:
            v = eigvecs[q][:, j - 1][:nc]
            z = v[anchor]
            if abs(z) < ANCHOR_TOL:
                okay = False
                break
            individual.append(top_mean_abs(v))
            aligned = v * np.exp(-1j * np.angle(z))
            core_vectors.append(aligned)
        if not okay:
            unusable.append(j)
            continue
        a_j = float(np.mean(individual))
        if not math.isfinite(a_j) or a_j <= 0:
            unusable.append(j)
            continue
        avg = np.mean(np.stack(core_vectors, axis=0), axis=0)
        b_j = top_mean_abs(avg)
        r = b_j / a_j
        if not math.isfinite(r):
            unusable.append(j)
            continue
        js.append(j)
        ratios.append(float(r))
    return np.asarray(js, float), np.asarray(ratios, float), unusable


def run(n: int, core_seed: int) -> dict:
    nc = int(round(CORE_FRAC * n))
    core_rng = np.random.default_rng(core_seed)
    core = core_rng.random((nc, 2))
    d2 = np.sum((core - np.array([0.5, 0.5])) ** 2, axis=1)
    anchor = int(np.argmin(d2))

    evals = []
    evecs = []
    seeds = []
    for q in range(M):
        s = completion_seed(n, core_seed, q)
        seeds.append(s)
        extra = np.random.default_rng(s).random((n - nc, 2))
        uv = np.vstack([core, extra])
        w, u = eigensystem(uv)
        evals.append(w)
        evecs.append(u)

    m_positive = min(len(w) for w in evals)
    js, ratios, unusable = persistence_curve(evecs, nc, anchor, m_positive)
    sel = candidate_break(js, ratios)

    loo_breaks = []
    if sel.get("candidate") is not None:
        for omit in range(M):
            j2, r2, _ = persistence_curve(evecs, nc, anchor, m_positive, omit=omit)
            s2 = candidate_break(j2, r2)
            loo_breaks.append(s2.get("candidate"))

    full_break = sel.get("candidate")
    loo_valid = [int(x) for x in loo_breaks if x is not None]
    loo_median = float(np.median(loo_valid)) if loo_valid else None
    within20 = 0
    median_within10 = False
    if full_break is not None and loo_median is not None and full_break > 0:
        median_within10 = abs(loo_median - full_break) / full_break <= 0.10
        within20 = sum(abs(x - full_break) / full_break <= 0.20 for x in loo_valid)
    loo_stable = bool(len(loo_valid) == M and median_within10 and within20 >= 9)

    resolved = bool(sel.get("basic_resolved", False) and loo_stable)
    j_star = int(full_break) if full_break is not None else None
    lambda_star = None
    source = None
    if j_star is not None:
        vals = [float(w[j_star - 1]) for w in evals if len(w) >= j_star]
        if vals and all(v > 0 and math.isfinite(v) for v in vals):
            lambda_star = float(math.exp(np.mean(np.log(vals))))
    if resolved and lambda_star is not None:
        lam_src = math.sqrt(n) / (4.0 * math.pi)
        j_src = [int(np.sum(w >= lam_src)) for w in evals]
        med_jsrc = float(np.median(j_src))
        source = {
            "lambda_source": lam_src,
            "positive_source_ranks": j_src,
            "median_positive_source_rank": med_jsrc,
            "j_star_over_median_source_rank": j_star / med_jsrc if med_jsrc > 0 else None,
            "lambda_star_over_source": lambda_star / lam_src,
        }

    sel["loo_breaks"] = loo_breaks
    sel["loo_median_break"] = loo_median
    sel["loo_within_20pct_count"] = within20
    sel["loo_median_within_10pct"] = median_within10
    sel["loo_stable"] = loo_stable
    sel["resolved"] = resolved

    return {
        "iteration": "ITER179",
        "lane": "researcher",
        "n": n,
        "nc": nc,
        "core_seed": core_seed,
        "completion_seeds": seeds,
        "ensemble_size": M,
        "core_fraction": CORE_FRAC,
        "phase_anchor_core_index": anchor,
        "phase_anchor_uv": core[anchor].tolist(),
        "positive_modes_min_across_ensemble": m_positive,
        "usable_mode_indices": [int(x) for x in js],
        "unusable_mode_indices": unusable,
        "persistence_ratio": [float(x) for x in ratios],
        "selection": sel,
        "selected_positive_rank": j_star,
        "selected_eigenvalue_geomean": lambda_star,
        "post_selection_source_comparison": source,
        "claim_lock": "No entropy or source SSEE cutoff enters the persistence curve or transition selection.",
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, required=True)
    p.add_argument("--core-seed", type=int, required=True)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    out = run(a.n, a.core_seed)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({
        "iteration": out["iteration"], "lane": out["lane"], "n": out["n"],
        "core_seed": out["core_seed"], "resolved": out["selection"]["resolved"],
        "selected_positive_rank": out["selected_positive_rank"],
        "delta_bic": out["selection"].get("delta_bic"),
        "loo_stable": out["selection"]["loo_stable"],
        "source_comparison": out["post_selection_source_comparison"],
    }, indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
