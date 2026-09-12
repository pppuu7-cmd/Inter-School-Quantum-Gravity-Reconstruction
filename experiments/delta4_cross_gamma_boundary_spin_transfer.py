#!/usr/bin/env python3
"""Preregistered cross-gamma transfer audit for Lorentzian EPRL Delta4.

Motivation
----------
The preceding 24-regime boundary-spin scaling-class audit failed its aggregate
preregistered gate even though a two-slope-by-boundary-spin model substantially
improved median chronological holdout error.  This follow-up does NOT relax that
gate.  It asks a different, independently frozen question: do boundary-spin
specific convergence exponents learned from two Immirzi sectors transfer to a
third, unseen Immirzi sector better than (a) one global exponent and (b) a
spin-label-swapped null?

For every tail/holdout regime and every held-out gamma:
  1. fit global and j-specific slopes only on the other two gammas;
  2. on the held-out gamma, use its early training segment ONLY to calibrate
     dataset-specific intercepts with those slopes frozen;
  3. predict its later chronological holdout;
  4. compare correct j-transfer to global-transfer and to a swapped-j null.

There are 6 tail fractions x 4 holdout fractions x 3 held-out gammas = 72 tasks.
No threshold is changed after inspection.

Natural transfer support requires, in aggregate:
  * all 72 tasks identifiable;
  * median correct-j vs global holdout improvement >= 0.10;
  * correct-j beats global in >= 48/72 tasks;
  * median correct-j vs swapped-j improvement >= 0.10;
  * correct-j beats swapped-j in >= 48/72 tasks;
  * median correct-j vs global improvement > 0 for each held-out gamma.

Scope lock: a positive result is finite-cutoff cross-gamma transfer structure
inside pinned Delta4 data, NOT an RG universality class, continuum limit,
refinement map, or new physics.  A negative result is retained as evidence
against stable boundary-spin classification and does not invalidate EPRL.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

SOURCE_COMMIT = "4fa7e31ffc6553e56da94a443a53a4059a5d2035"
TAIL_FRACTIONS = (0.0, 0.10, 0.20, 0.30, 0.40, 0.50)
HOLDOUT_FRACTIONS = (0.20, 0.25, 0.30, 0.35)


def l2(v):
    return math.sqrt(sum(x*x for x in v))


def unit(v):
    n = l2(v)
    return None if n == 0 else [x/n for x in v]


def cosine(a, b):
    return max(-1.0, min(1.0, sum(x*y for x, y in zip(a, b))))


def parse_matrix(path):
    rows = []
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        rows.append([float(x) for x in re.split(r'[\s,]+', line.strip()) if x])
    if not rows or any(len(r) != len(rows[0]) for r in rows):
        raise ValueError(f"invalid matrix {path}")
    return rows


def select_datasets(root):
    files = list(root.glob('Delta_4_ampls/Immirzi_*/j_*/CSV_format/Delta_4_ampls_Dl_max_*.csv'))
    pat = re.compile(r'Immirzi_([^/]+)/j_([^/]+)/CSV_format/Delta_4_ampls_Dl_max_(\d+)\.csv$')
    chosen = {}
    for f in files:
        m = pat.search(f.as_posix())
        if not m:
            continue
        g, j, d = float(m.group(1)), float(m.group(2)), int(m.group(3))
        if (g, j) not in chosen or d > chosen[(g, j)][0]:
            chosen[(g, j)] = (d, f)
    return [(g, j, d, f) for (g, j), (d, f) in sorted(chosen.items())]


def build_dataset(g, j, dmax, path, root, tail, holdout):
    rows = parse_matrix(path)
    uu = [unit(r) for r in rows]
    if any(u is None for u in uu):
        return None
    raw = []
    for k in range(len(uu)-1):
        e = max(0.0, 1.0 - cosine(uu[k], uu[k+1]))
        if e > 0.0:
            raw.append((k, math.log(k+1.0), math.log(e)))
    cut = int(math.floor(tail*len(raw)))
    pts = raw[cut:]
    nh = max(2, int(math.ceil(holdout*len(pts))))
    nt = len(pts) - nh
    if nt < 4 or nh < 2:
        return None
    return {
        'gamma': g, 'j': j, 'dmax': dmax, 'key': f'g={g},j={j}',
        'train': pts[:nt], 'holdout': pts[nt:],
        'source_file': path.relative_to(root).as_posix(),
    }


def fit_slopes(datasets, group_fn):
    groups = {}
    for d in datasets:
        gr = group_fn(d)
        xs = [p[1] for p in d['train']]
        ys = [p[2] for p in d['train']]
        mx, my = sum(xs)/len(xs), sum(ys)/len(ys)
        q = groups.setdefault(gr, {'num': 0.0, 'den': 0.0})
        q['num'] += sum((x-mx)*(y-my) for x, y in zip(xs, ys))
        q['den'] += sum((x-mx)**2 for x in xs)
    out = {}
    for gr, q in groups.items():
        if q['den'] <= 0:
            return None
        out[gr] = -q['num']/q['den']
    return out


def heldout_rmse(targets, slope_fn):
    sq = []
    per = {}
    for d in targets:
        a = slope_fn(d)
        if a is None or not math.isfinite(a):
            return None
        # Held-out gamma may calibrate ONLY its intercept on its early segment;
        # the slope is transferred frozen from the other gammas.
        b = sum(y + a*x for _, x, y in d['train'])/len(d['train'])
        errs = [(y - (b-a*x))**2 for _, x, y in d['holdout']]
        sq.extend(errs)
        per[d['key']] = math.sqrt(sum(errs)/len(errs))
    if not sq:
        return None
    return {'rmse': math.sqrt(sum(sq)/len(sq)), 'per_dataset_rmse': per, 'n_holdout': len(sq)}


def run_task(ds, root, tail, holdout, heldout_gamma):
    built = []
    for x in ds:
        d = build_dataset(*x, root, tail, holdout)
        if d is None:
            return {'tail_fraction': tail, 'holdout_fraction': holdout,
                    'heldout_gamma': heldout_gamma, 'identifiable': False}
        built.append(d)
    source = [d for d in built if d['gamma'] != heldout_gamma]
    target = [d for d in built if d['gamma'] == heldout_gamma]
    if len(source) != 4 or len(target) != 2:
        return {'tail_fraction': tail, 'holdout_fraction': holdout,
                'heldout_gamma': heldout_gamma, 'identifiable': False}
    ag = fit_slopes(source, lambda d: 'global')
    aj = fit_slopes(source, lambda d: d['j'])
    if ag is None or aj is None or set(aj) != {0.5, 1.0}:
        return {'tail_fraction': tail, 'holdout_fraction': holdout,
                'heldout_gamma': heldout_gamma, 'identifiable': False}
    rg = heldout_rmse(target, lambda d: ag['global'])
    rj = heldout_rmse(target, lambda d: aj[d['j']])
    rs = heldout_rmse(target, lambda d: aj[1.0 if d['j'] == 0.5 else 0.5])
    if not all((rg, rj, rs)):
        return {'tail_fraction': tail, 'holdout_fraction': holdout,
                'heldout_gamma': heldout_gamma, 'identifiable': False}
    imp_global = (rg['rmse'] - rj['rmse'])/max(rg['rmse'], 1e-15)
    imp_swapped = (rs['rmse'] - rj['rmse'])/max(rs['rmse'], 1e-15)
    return {
        'tail_fraction': tail, 'holdout_fraction': holdout,
        'heldout_gamma': heldout_gamma, 'identifiable': True,
        'source_gammas': sorted({d['gamma'] for d in source}),
        'global_alpha': ag['global'],
        'boundary_j_alpha': {str(k): v for k, v in aj.items()},
        'global_transfer': rg, 'correct_j_transfer': rj, 'swapped_j_null': rs,
        'correct_j_vs_global_improvement': imp_global,
        'correct_j_vs_swapped_improvement': imp_swapped,
        'correct_j_beats_global': rj['rmse'] < rg['rmse'],
        'correct_j_beats_swapped': rj['rmse'] < rs['rmse'],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-root', required=True)
    ap.add_argument('--lane', type=int, required=True)
    ap.add_argument('--lanes', type=int, default=24)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    root = Path(args.source_root)
    ds = select_datasets(root)
    if len(ds) != 6:
        raise RuntimeError(f'expected 6 datasets, found {len(ds)}')
    gammas = sorted({g for g, _, _, _ in ds})
    if len(gammas) != 3:
        raise RuntimeError(f'expected 3 gamma sectors, found {gammas}')
    tasks = [(t, h, g) for t in TAIL_FRACTIONS for h in HOLDOUT_FRACTIONS for g in gammas]
    assigned = [x for i, x in enumerate(tasks) if i % args.lanes == args.lane]
    results = [run_task(ds, root, *x) for x in assigned]
    out = {
        'test': 'LORENTZIAN_EPRL_DELTA4_CROSS_GAMMA_BOUNDARY_SPIN_TRANSFER',
        'source_repository': 'PietropaoloFrisoni/HowToSpinFoamAmplitude',
        'source_commit': SOURCE_COMMIT,
        'lane': args.lane, 'lanes': args.lanes,
        'task_count_total': len(tasks), 'results': results,
        'frozen_aggregate_gate': {
            'all_tasks_identifiable': True,
            'minimum_median_correct_j_vs_global_improvement': 0.10,
            'minimum_correct_j_beats_global_count': 48,
            'minimum_median_correct_j_vs_swapped_improvement': 0.10,
            'minimum_correct_j_beats_swapped_count': 48,
            'per_heldout_gamma_median_correct_j_vs_global_improvement_strictly_positive': True,
        },
        'claim_lock': 'Finite-cutoff held-out transfer only; not an RG universality class, continuum/refinement result, bridge derivation, or new physics.'
    }
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
