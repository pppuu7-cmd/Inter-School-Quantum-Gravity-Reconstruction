#!/usr/bin/env python3
"""ITER179 independent Critic implementation."""

from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np

M = 12
CORE_FRAC = 0.90
TOP_K = 10
ANCHOR_TOL = 1e-12
POS_TOL = 1e-12


def order_matrix(points: np.ndarray) -> np.ndarray:
    a = points[:, 0]
    b = points[:, 1]
    return (np.logical_and(a[:, None] < a[None, :], b[:, None] < b[None, :])).astype(np.float64)


def cseed(n: int, core_seed: int, q: int) -> int:
    return int(10_000_000 + 10_000 * n + 20 * core_seed + q)


def positive_modes(points: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    c = order_matrix(points)
    h = (0.5j) * (c - c.T)
    val, vec = np.linalg.eigh(h)
    mask = val > POS_TOL
    val = val[mask]
    vec = vec[:, mask]
    idx = np.argsort(val)[::-1]
    return val[idx], vec[:, idx]


def top10(v: np.ndarray) -> float:
    vals = np.sort(np.abs(v))
    k = min(TOP_K, len(vals))
    return float(np.mean(vals[-k:])) if k else 0.0


def ols(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    xm = float(np.mean(x)); ym = float(np.mean(y))
    den = float(np.sum((x - xm) ** 2))
    slope = 0.0 if den == 0.0 else float(np.sum((x - xm) * (y - ym)) / den)
    intercept = ym - slope * xm
    resid = y - (slope * x + intercept)
    return slope, intercept, float(resid @ resid)


def BIC(rss: float, n: int, p: int) -> float:
    rss = max(float(rss), 1e-300)
    return float(n * np.log(rss / n) + p * np.log(n))


def select(js: np.ndarray, rr: np.ndarray) -> dict:
    n = int(len(js))
    if n < 40:
        return {"candidate": None, "reason": "fewer_than_40_usable_modes"}
    s0, i0, r0 = ols(js, rr)
    winner = None
    for split in range(20, n - 19):
        sp, ip, rp = ols(js[:split], rr[:split])
        tail = rr[split:]
        const = float(np.mean(tail))
        rt = float(np.sum((tail - const) ** 2))
        total = rp + rt
        if winner is None or total < winner["rss"]:
            st, it, rtl = ols(js[split:], tail)
            winner = {
                "candidate": int(js[split - 1]),
                "split_position": split,
                "rss": total,
                "prefix_slope": sp,
                "prefix_intercept": ip,
                "suffix_constant": const,
                "suffix_line_slope": st,
                "suffix_line_intercept": it,
                "suffix_line_rss": rtl,
            }
    assert winner is not None
    b0 = BIC(r0, n, 2)
    b1 = BIC(winner["rss"], n, 4)
    db = b0 - b1
    basic = bool(
        db >= 10.0
        and winner["prefix_slope"] < 0.0
        and abs(winner["suffix_line_slope"]) <= 0.25 * abs(winner["prefix_slope"])
    )
    winner.update({
        "single_line_slope": s0,
        "single_line_intercept": i0,
        "single_line_rss": r0,
        "bic_single": b0,
        "bic_line_constant": b1,
        "delta_bic": db,
        "basic_resolved": basic,
    })
    return winner


def curve(
    vectors: list[np.ndarray],
    nc: int,
    anchor: int,
    mpos: int,
    omit: int | None = None,
) -> tuple[np.ndarray, np.ndarray, list[int]]:
    members = tuple(q for q in range(len(vectors)) if q != omit)
    stop = int(math.floor(0.80 * mpos))
    js: list[int] = []
    rr: list[float] = []
    bad: list[int] = []
    for j in range(5, stop + 1):
        mags = []
        aligned = []
        for q in members:
            v = np.array(vectors[q][:nc, j - 1], copy=True)
            z = v[anchor]
            if abs(z) < ANCHOR_TOL:
                mags = []
                break
            mags.append(top10(v))
            phase = np.conj(z) / abs(z)
            aligned.append(v * phase)
        if not mags:
            bad.append(j)
            continue
        aa = float(np.mean(mags))
        if not (aa > 0.0 and np.isfinite(aa)):
            bad.append(j)
            continue
        vv = np.mean(np.asarray(aligned), axis=0)
        bb = top10(vv)
        val = bb / aa
        if not np.isfinite(val):
            bad.append(j)
            continue
        js.append(j); rr.append(float(val))
    return np.asarray(js, float), np.asarray(rr, float), bad


def run(n: int, core_seed: int) -> dict:
    nc = int(round(CORE_FRAC * n))
    core = np.random.Generator(np.random.PCG64(core_seed)).random((nc, 2))
    anchor = int(np.argmin((core[:, 0] - 0.5) ** 2 + (core[:, 1] - 0.5) ** 2))

    values = []
    vectors = []
    seeds = []
    for q in range(M):
        sd = cseed(n, core_seed, q)
        seeds.append(sd)
        rng = np.random.Generator(np.random.PCG64(sd))
        extra = rng.random((n - nc, 2))
        pts = np.concatenate((core, extra), axis=0)
        ev, U = positive_modes(pts)
        values.append(ev); vectors.append(U)

    mpos = min(len(x) for x in values)
    js, rr, bad = curve(vectors, nc, anchor, mpos)
    ans = select(js, rr)
    full = ans.get("candidate")

    loo = []
    if full is not None:
        for q in range(M):
            x, y, _ = curve(vectors, nc, anchor, mpos, omit=q)
            loo.append(select(x, y).get("candidate"))

    good = [int(x) for x in loo if x is not None]
    med = float(np.median(good)) if good else None
    within = 0
    med10 = False
    if full is not None and med is not None and full > 0:
        med10 = abs(med - full) / full <= 0.10
        within = sum(abs(x - full) / full <= 0.20 for x in good)
    loo_stable = bool(len(good) == M and med10 and within >= 9)
    resolved = bool(ans.get("basic_resolved", False) and loo_stable)

    jstar = int(full) if full is not None else None
    lstar = None
    source = None
    if jstar is not None:
        ls = [float(x[jstar - 1]) for x in values if len(x) >= jstar]
        if ls and all(x > 0.0 and np.isfinite(x) for x in ls):
            lstar = float(np.exp(np.mean(np.log(np.asarray(ls)))))
    if resolved and lstar is not None:
        lsrc = math.sqrt(n) / (4.0 * math.pi)
        jr = [int(np.count_nonzero(x >= lsrc)) for x in values]
        medr = float(np.median(jr))
        source = {
            "lambda_source": lsrc,
            "positive_source_ranks": jr,
            "median_positive_source_rank": medr,
            "j_star_over_median_source_rank": jstar / medr if medr > 0 else None,
            "lambda_star_over_source": lstar / lsrc,
        }

    ans.update({
        "loo_breaks": loo,
        "loo_median_break": med,
        "loo_within_20pct_count": within,
        "loo_median_within_10pct": med10,
        "loo_stable": loo_stable,
        "resolved": resolved,
    })

    return {
        "iteration": "ITER179",
        "lane": "critic",
        "n": n,
        "nc": nc,
        "core_seed": core_seed,
        "completion_seeds": seeds,
        "ensemble_size": M,
        "core_fraction": CORE_FRAC,
        "phase_anchor_core_index": anchor,
        "phase_anchor_uv": core[anchor].tolist(),
        "positive_modes_min_across_ensemble": mpos,
        "usable_mode_indices": [int(x) for x in js],
        "unusable_mode_indices": bad,
        "persistence_ratio": [float(x) for x in rr],
        "selection": ans,
        "selected_positive_rank": jstar,
        "selected_eigenvalue_geomean": lstar,
        "post_selection_source_comparison": source,
        "claim_lock": "Independent implementation; no entropy or source cutoff enters selection.",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--core-seed", type=int, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
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
