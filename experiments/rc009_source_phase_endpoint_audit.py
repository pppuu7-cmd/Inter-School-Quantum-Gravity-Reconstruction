#!/usr/bin/env python3
"""RC-009 source-phase endpoint audit.

Tests the remaining *source-defined* oscillatory escape route after the
algebraic endpoint-power audit.  The relevant RC-009 branch is

    cos(S_R/G + arg D) + cos(gamma S_R/G - Lambda V4/G).

If its phase arguments approach finite limits and the combined branch stays
nonzero with stable sign as the endpoint is approached, then this branch does
not generate ever-faster oscillations capable of conditionally regularising an
algebraic t^p singularity.  This statement is deliberately scoped to the
reduced isotemporal RC-009 realization and its frozen source branch.
"""
from __future__ import annotations
import argparse, cmath, json, math
from pathlib import Path
import rc009_dense_grid_reliability as r

TWOPI = 2.0 * math.pi


def wrap(x: float) -> float:
    return (x + math.pi) % TWOPI - math.pi


def source_block(j0: float, j1: float, H: float):
    g = r.geom(j0, j1, H)
    if g is None:
        return None
    k, K, Q, SR, V4, phi = g
    x = 1 + K*K - 2*Q
    # D phase only; omit strictly positive real prefactors to avoid underflow.
    z = ((K - 1j*K*K + 1j*Q)**3 * complex(x, 0.0)**3 *
         (K + 1j)**6 * (K - 3j)**2 *
         (1 + 3*K*K - 2*Q - 2j*K*(Q-1))**3)
    varphi = cmath.phase(z)
    p1 = SR / r.G + varphi
    p2 = r.GAMMA * SR / r.G - r.LAMBDA * V4 / r.G
    branch = math.cos(p1) + math.cos(p2)
    return {'p1': p1, 'p2': p2, 'branch': branch, 'SR': SR, 'V4': V4,
            'varphi': varphi}


def unwrap(vals):
    if not vals:
        return []
    out = [vals[0]]
    for v in vals[1:]:
        out.append(out[-1] + wrap(v - out[-1]))
    return out


def blocks_for(mode: str, t: float, anchor: float):
    if mode == 'coarse':
        a, H, mult = 1/9, r.HTOTAL/2, 27
        pairs = [(a, t), (t, a)]
    elif mode == 'fine_diag':
        a, H, mult = 1/16, r.HTOTAL/3, 64
        pairs = [(a, t), (t, t), (t, a)]
    else:
        a, H, mult = 1/16, r.HTOTAL/3, 64
        pairs = [(a, t), (t, anchor), (anchor, a)]
    return H, mult, pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', choices=['coarse','fine_diag','fine_edge'], required=True)
    ap.add_argument('--anchor', type=float, default=0.2)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()

    # Descending t makes the sequence run toward the endpoint.
    ts = [10.0**(-x/2) for x in range(2, 25)]  # 1e-1 ... 1e-12
    rows = []
    per_block = None
    for t in ts:
        H, mult, pairs = blocks_for(args.mode, t, args.anchor)
        bb = [source_block(j0, j1, H) for j0, j1 in pairs]
        if any(x is None for x in bb):
            continue
        combined = 1.0
        log_abs = 0.0
        zero = False
        for b in bb:
            q = b['branch']
            if q == 0:
                zero = True
                break
            combined *= math.copysign(1.0, q) ** mult
            log_abs += mult * math.log(abs(q))
        rows.append({'t': t, 'blocks': bb, 'combined_sign': 0 if zero else int(combined),
                     'combined_log_abs_branch': -math.inf if zero else log_abs})

    nblock = len(rows[0]['blocks'])
    audits = []
    for bi in range(nblock):
        p1 = unwrap([x['blocks'][bi]['p1'] for x in rows])
        p2 = unwrap([x['blocks'][bi]['p2'] for x in rows])
        b = [x['blocks'][bi]['branch'] for x in rows]
        # Last six samples span 10^-9.5 ... 10^-12.
        tail_n = 6
        old_n = 6
        def variation(v, lo, hi):
            q = v[lo:hi]
            return sum(abs(q[i]-q[i-1]) for i in range(1, len(q)))
        tv1 = variation(p1, -tail_n, None)
        tv2 = variation(p2, -tail_n, None)
        ov1 = variation(p1, -(tail_n+old_n), -tail_n+1)
        ov2 = variation(p2, -(tail_n+old_n), -tail_n+1)
        minb = min(abs(x) for x in b[-tail_n:])
        maxdb = max(abs(b[i]-b[i-1]) for i in range(len(b)-tail_n+1, len(b)))
        phase_freezes = (tv1 < 0.1 and tv2 < 0.1 and tv1 <= ov1 + 1e-12 and tv2 <= ov2 + 1e-12)
        branch_nonzero = minb > 1e-6
        audits.append({'block_index': bi, 'tail_phase1_total_variation_rad': tv1,
                       'tail_phase2_total_variation_rad': tv2,
                       'preceding_phase1_total_variation_rad': ov1,
                       'preceding_phase2_total_variation_rad': ov2,
                       'tail_min_abs_branch': minb, 'tail_max_step_branch_change': maxdb,
                       'phase_freezes_toward_endpoint': phase_freezes,
                       'branch_bounded_away_from_zero': branch_nonzero,
                       'source_oscillation_cannot_regularize_this_block': phase_freezes and branch_nonzero})

    signs = [x['combined_sign'] for x in rows[-6:]]
    sign_stable = len(set(signs)) == 1 and signs[0] != 0
    all_blocks = all(x['source_oscillation_cannot_regularize_this_block'] for x in audits)
    out = {
        'test': 'RC009_SOURCE_PHASE_ENDPOINT_AUDIT',
        'mode': args.mode,
        'anchor': args.anchor if args.mode == 'fine_edge' else None,
        'sample_count': len(rows), 't_min': rows[-1]['t'], 't_max': rows[0]['t'],
        'block_audits': audits,
        'combined_tail_sign_stable': sign_stable,
        'source_branch_oscillatory_escape_excluded_scoped': all_blocks and sign_stable,
        'tail_rows': rows[-6:],
        'interpretation_lock': ('Scoped to the frozen RC-009 reduced isotemporal source branch. A positive exclusion means the source phases freeze and the branch remains nonzero/sign-stable at the tested endpoint, so that specific finite-phase oscillation cannot conditionally cure the previously measured algebraic divergence. It is not a no-go for Lorentzian EPRL, other contours, other source-defined measures, or full spin-foam refinement.')
    }
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
