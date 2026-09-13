#!/usr/bin/env python3
import argparse
import cmath
import json
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'code' / 'iter019'))
sys.path.insert(0, str(ROOT / 'code' / 'iter023'))
sys.path.insert(0, str(ROOT / 'code' / 'iter025'))

import qcg_solver_validation as base  # noqa: E402
import dual_braid_primitives as db  # noqa: E402
import qbar_sign_normalization as legacy  # noqa: E402

OUT = ROOT / 'out' / 'iter026'
OUT.mkdir(parents=True, exist_ok=True)

PRIMARY_LEVELS = (6, 10, 12)
HELDOUT_LEVELS = (7, 9, 11)
ALL_LEVELS = (6, 7, 9, 10, 11, 12)
SOURCE_RECORD = ROOT / 'sources' / 'ITER025_RC006_QBAR_R_AUTHORITY.md'
EXPECTED_HASHES = {
    '1609.02429v2': '3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee',
    '1312.0905v2': '69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0',
    '1311.1798v1': 'd6804794d3f4589f77a2e11d2a143c1125a900160e0c632ed3b3e471598af3f7',
}
KNOWN_COUNTEREXAMPLES = [(6, 6), (7, 7), (9, 9), (10, 8), (10, 9), (11, 9), (12, 9), (12, 10)]
PRIMARY_PAIRS = ((1, 1), (2, 1), (4, 2), (6, 4), (8, 4), (6, 6), (8, 8))
HELDOUT_PAIRS = ((3, 1), (3, 2), (5, 1), (5, 3))
PRIMARY_FOUR = {
    6: ((1, 1, 1, 1), (2, 2, 2, 2), (4, 2, 4, 2)),
    10: ((1, 1, 1, 1), (2, 2, 2, 2), (4, 2, 4, 2)),
    12: ((1, 1, 1, 1), (2, 2, 2, 2), (4, 2, 4, 2), (6, 6, 6, 6), (8, 4, 8, 4)),
}
# Prospectively selected in implementation source before any production result.
HELDOUT_FOUR = {
    7: ((3, 1, 3, 1),),
    9: ((5, 3, 5, 3),),
    11: ((5, 3, 5, 3),),
}


def reversal(t):
    return np.fliplr(np.eye(t + 1, dtype=complex))


def source_sign(a, b, c):
    exponent = (a + b - c) // 2
    if 2 * exponent != a + b - c:
        raise ValueError(f'nonintegral source-sign exponent {(a,b,c)}')
    return (-1) ** exponent


def singlet_source_gauge(t, k, C):
    target = base.b2_singlet(t, k)
    nz = np.flatnonzero(np.abs(target[:, 0]) > 1e-12)
    if len(nz) == 0:
        raise RuntimeError(f'B2 has no nonzero component {(t,k)}')
    idx = int(nz[0])
    if abs(C[idx, 0]) < 1e-12:
        raise RuntimeError(f'qCG first B2 anchor is zero {(t,k,idx)}')
    sigma = target[idx, 0] / C[idx, 0]
    calibrated = sigma * C
    return calibrated, {
        'k': k,
        'twice_j': t,
        'anchor_flat_index': idx,
        'sigma': [float(sigma.real), float(sigma.imag)],
        'sigma_squared_error': float(abs(sigma * sigma - 1)),
        'sigma_imag_abs': float(abs(sigma.imag)),
        'full_B2_residual': float(np.max(np.abs(calibrated - target))),
    }


def source_qC(a, b, c, k):
    C = base.solve_channel(a, b, c, k)['C']
    meta = None
    if a == b and c == 0:
        C, meta = singlet_source_gauge(a, k, C)
    return C, meta


def cbar_source(a, b, c, k):
    Cq, gauge = source_qC(a, b, c, k)
    Jab = np.kron(reversal(a), reversal(b))
    Cbar = source_sign(a, b, c) * (Jab @ Cq @ reversal(c))
    return Cbar, gauge


def cbar_component_loop(a, b, c, k):
    Cq, _ = source_qC(a, b, c, k)
    Cbar = np.zeros_like(Cq)
    ma = base.magnetic_values(a)
    mb = base.magnetic_values(b)
    mc = base.magnetic_values(c)
    ia = {round(float(m), 12): i for i, m in enumerate(ma)}
    ib = {round(float(m), 12): i for i, m in enumerate(mb)}
    ic = {round(float(m), 12): i for i, m in enumerate(mc)}
    s = source_sign(a, b, c)
    for i, m1 in enumerate(ma):
        for j, m2 in enumerate(mb):
            row = i * (b + 1) + j
            src_row = ia[round(float(-m1), 12)] * (b + 1) + ib[round(float(-m2), 12)]
            for h, m3 in enumerate(mc):
                src_col = ic[round(float(-m3), 12)]
                Cbar[row, h] = s * Cq[src_row, src_col]
    return Cbar


def d_source(a, b, c, k):
    Cbar_ba, _ = cbar_source(b, a, c, k)
    return db.swap_ba_to_ab(a, b) @ Cbar_ba / cmath.sqrt(db.qdim(c, k))


def qbar_intertwiner_residual(a, b, c, k, Cbar):
    _, Z, P, M = db.tensor_bar(a, b, k)
    _, zc, pc, mc = db.rep_bar(c, k)
    return max(
        float(np.max(np.abs(Z @ Cbar - Cbar @ zc))),
        float(np.max(np.abs(P @ Cbar - Cbar @ pc))),
        float(np.max(np.abs(M @ Cbar - Cbar @ mc))),
    )


def admiss_outputs(a, b, k):
    return [c for c in range(k + 1) if base.admissible(a, b, c, k) and abs(db.qdim(c, k)) >= 1e-12]


def planned_pairs(k, heldout=False):
    pool = HELDOUT_PAIRS if heldout else PRIMARY_PAIRS
    return [(a, b) for a, b in pool if a <= k and b <= k and admiss_outputs(a, b, k)]


def common_channels(a, b, c, d, k):
    left = set(admiss_outputs(a, b, k))
    right = set(admiss_outputs(c, d, k))
    return sorted(left & right)


def q_embedding(a, b, c, k):
    C, _ = source_qC(a, b, c, k)
    return C / cmath.sqrt(db.qdim(c, k))


def four_basis(a, b, c, d, t, k):
    return d_source(a, b, t, k) @ q_embedding(c, d, t, k).T


def four_dual(a, b, c, d, t, k):
    D = d_source(a, b, t, k)
    Q = q_embedding(c, d, t, k)
    diag = np.diag([((-1) ** t) * db.qp(m, k) for m in db.ms(t)])
    return D @ diag @ Q.T


def four_residual(quad, k):
    a, b, c, d = quad
    channels = common_channels(a, b, c, d, k)
    if not channels:
        raise RuntimeError(f'no common 4-valent channels {(quad,k)}')
    B = {t: four_basis(a, b, c, d, t, k) for t in channels}
    U = {t: four_dual(a, b, c, d, t, k) for t in channels}
    mat = np.array([[np.sum(U[t] * B[s]) for s in channels] for t in channels], dtype=complex)
    ext_sign = (-1) ** int(round((a + b + c + d) / 2))
    target = np.diag([ext_sign / db.qdim(t, k) for t in channels])
    return float(np.max(np.abs(mat - target))), channels


def lane_domain():
    if not SOURCE_RECORD.exists():
        return {'lane': 'domain', 'blocked_source_authority': True, 'pass': False, 'reason': 'missing source authority record'}
    text = SOURCE_RECORD.read_text(encoding='utf-8')
    hash_presence = {name: digest in text for name, digest in EXPECTED_HASHES.items()}
    locator_presence = {
        'qbar_identity': 'qg_spinnet_20140616.tex:1101' in text,
        'target_qbar_graph': '1432-1464' in text,
        'target_R': '956-987' in text,
        'cited_R': '1668-1682' in text and '1707-1718' in text,
    }
    cup_rows = []
    domain_ok = True
    for k in ALL_LEVELS:
        for t in range(1, k + 1):
            qd = db.qdim(t, k)
            ok = 0 <= t <= k and abs(qd) >= 1e-12 and base.admissible(t, t, 0, k)
            cup_rows.append({'k': k, 'twice_j': t, 'qdim_abs': float(abs(qd)), 'admissible_singlet': bool(ok)})
            domain_ok = domain_ok and ok
    counterexample_coverage = {f'{k}:{t}': any(r['k'] == k and r['twice_j'] == t for r in cup_rows) for k, t in KNOWN_COUNTEREXAMPLES}
    four_rows = []
    for k, quads in {**PRIMARY_FOUR, **HELDOUT_FOUR}.items():
        for quad in quads:
            chans = common_channels(*quad, k)
            ok = bool(chans) and max(quad) <= k
            four_rows.append({'k': k, 'twice_external': list(quad), 'twice_internal': chans, 'domain_ok': ok})
            domain_ok = domain_ok and ok
    pair_rows = []
    for k in PRIMARY_LEVELS:
        for a, b in planned_pairs(k, False):
            pair_rows.append({'k': k, 'twice_pair': [a, b], 'outputs': admiss_outputs(a, b, k)})
    for k in HELDOUT_LEVELS:
        for a, b in planned_pairs(k, True):
            pair_rows.append({'k': k, 'twice_pair': [a, b], 'outputs': admiss_outputs(a, b, k)})
    authority_ok = all(hash_presence.values()) and all(locator_presence.values())
    coverage_ok = all(counterexample_coverage.values()) and len(cup_rows) == sum(ALL_LEVELS)
    return {
        'lane': 'domain',
        'source_hash_presence': hash_presence,
        'source_locator_presence': locator_presence,
        'cup_rows': cup_rows,
        'pair_rows': pair_rows,
        'four_rows': four_rows,
        'known_counterexample_coverage': counterexample_coverage,
        'planned_cup_case_count': len(cup_rows),
        'expected_cup_case_count': sum(ALL_LEVELS),
        'source_domain_ok': bool(domain_ok),
        'authority_ok': bool(authority_ok),
        'coverage_ok': bool(coverage_ok),
        'pass': bool(domain_ok and authority_ok and coverage_ok),
    }


def lane_algebra():
    rows = []
    gauges = {}
    panels = [(k, a, b) for k in PRIMARY_LEVELS for a, b in planned_pairs(k, False)]
    panels += [(k, a, b) for k in HELDOUT_LEVELS for a, b in planned_pairs(k, True)]
    for k, a, b in panels:
        for c in admiss_outputs(a, b, k):
            Cbar, gauge = cbar_source(a, b, c, k)
            loop = cbar_component_loop(a, b, c, k)
            identity = float(np.max(np.abs(Cbar - loop)))
            inter = qbar_intertwiner_residual(a, b, c, k, Cbar)
            rows.append({'k': k, 'twice': [a, b, c], 'source_identity_residual': identity, 'qbar_intertwiner_residual': inter})
            if gauge is not None:
                gauges[f'{k}:{a}'] = gauge
    # Freeze and check every singlet source gauge independently, including full cup-domain labels.
    for k in ALL_LEVELS:
        for t in range(1, k + 1):
            C = base.solve_channel(t, t, 0, k)['C']
            _, meta = singlet_source_gauge(t, k, C)
            gauges[f'{k}:{t}'] = meta
    max_identity = max(r['source_identity_residual'] for r in rows) if rows else float('inf')
    max_inter = max(r['qbar_intertwiner_residual'] for r in rows) if rows else float('inf')
    max_sigma2 = max(x['sigma_squared_error'] for x in gauges.values())
    max_sigma_im = max(x['sigma_imag_abs'] for x in gauges.values())
    max_b2 = max(x['full_B2_residual'] for x in gauges.values())
    return {
        'lane': 'algebra',
        'rows': rows,
        'singlet_source_gauges': list(gauges.values()),
        'max_source_identity_residual': max_identity,
        'max_qbar_intertwiner_residual': max_inter,
        'max_sigma_squared_error': max_sigma2,
        'max_sigma_imag_abs': max_sigma_im,
        'max_B2_residual': max_b2,
        'thresholds': {'identity': 2e-12, 'qbar_intertwiner': 5e-9, 'sigma2': 2e-9, 'sigma_imag': 2e-9, 'B2': 2e-9},
        'inverse_parameter_qbar_solver_used_for_construction': False,
        'per_channel_posthoc_repair': False,
        'pass': bool(max_identity < 2e-12 and max_inter < 5e-9 and max_sigma2 < 2e-9 and max_sigma_im < 2e-9 and max_b2 < 2e-9),
    }


def lane_cup():
    rows = []
    for k in ALL_LEVELS:
        for t in range(1, k + 1):
            D = d_source(t, t, 0, k)
            target = db.cup(t, k).reshape(-1, 1) / cmath.sqrt(db.qdim(t, k))
            residual = float(np.max(np.abs(D - target)))
            rows.append({'k': k, 'twice_j': t, 'residual': residual, 'known_iter025A_counterexample': (k, t) in KNOWN_COUNTEREXAMPLES})
    max_res = max(r['residual'] for r in rows)
    known = [r for r in rows if r['known_iter025A_counterexample']]
    return {
        'lane': 'cup',
        'rows': rows,
        'case_count': len(rows),
        'known_counterexamples': known,
        'max_residual': max_res,
        'threshold': 2e-9,
        'pass': bool(len(rows) == sum(ALL_LEVELS) and len(known) == len(KNOWN_COUNTEREXAMPLES) and max_res < 2e-9),
    }


def lane_four():
    rows = []
    for k, quads in PRIMARY_FOUR.items():
        for quad in quads:
            residual, chans = four_residual(quad, k)
            rows.append({'panel': 'primary', 'k': k, 'twice_external': list(quad), 'twice_internal': chans, 'residual': residual})
    for k, quads in HELDOUT_FOUR.items():
        for quad in quads:
            residual, chans = four_residual(quad, k)
            rows.append({'panel': 'heldout', 'k': k, 'twice_external': list(quad), 'twice_internal': chans, 'residual': residual})
    max_res = max(r['residual'] for r in rows)
    held_levels = sorted({r['k'] for r in rows if r['panel'] == 'heldout'})
    return {
        'lane': 'four',
        'rows': rows,
        'heldout_levels': held_levels,
        'max_residual': max_res,
        'threshold': 5e-8,
        'pass': bool(held_levels == list(HELDOUT_LEVELS) and max_res < 5e-8),
    }


def lane_null():
    controls = []
    # 1. Omit output magnetic reversal J_c on a non-singlet channel.
    k, a, b, c = 12, 2, 1, 1
    correct, _ = cbar_source(a, b, c, k)
    Cq, _ = source_qC(a, b, c, k)
    wrong = source_sign(a, b, c) * (np.kron(reversal(a), reversal(b)) @ Cq)
    controls.append({'name': 'omit_Jc', 'residual': float(np.max(np.abs(wrong - correct)))})
    # 2. Force source sign +1 where the frozen identity requires -1.
    k, a, b, c = 12, 1, 1, 0
    correct, _ = cbar_source(a, b, c, k)
    Cq, _ = source_qC(a, b, c, k)
    wrong = np.kron(reversal(a), reversal(b)) @ Cq @ reversal(c)
    controls.append({'name': 'force_source_sign_plus', 'residual': float(np.max(np.abs(wrong - correct))), 'required_source_sign': source_sign(a, b, c)})
    # 3. Omit the graph tensor-order permutation on an asymmetric pair.
    k, a, b, c = 12, 2, 1, 1
    correct_D = d_source(a, b, c, k)
    wrong_D, _ = cbar_source(b, a, c, k)
    wrong_D = wrong_D / cmath.sqrt(db.qdim(c, k))
    controls.append({'name': 'omit_ba_to_ab_permutation', 'residual': float(np.max(np.abs(wrong_D - correct_D)))})
    # Frozen legacy comparator only; never construction authority or PASS criterion.
    legacy_rows = []
    for kk, tt in KNOWN_COUNTEREXAMPLES:
        legacy_rows.append({'k': kk, 'twice_j': tt, 'legacy_cup_residual': legacy.cup_residual(tt, kk)})
    detected = sum(x['residual'] > 1e-6 for x in controls)
    return {
        'lane': 'null',
        'structural_wrong_controls': controls,
        'detected': detected,
        'required': 3,
        'legacy_ITER025A_negative_comparator': legacy_rows,
        'legacy_comparator_used_for_construction': False,
        'pass': bool(detected >= 3),
    }


def emit(ev):
    (OUT / 'evidence.json').write_text(json.dumps(ev, indent=2, sort_keys=True) + '\n')
    print(json.dumps(ev, indent=2, sort_keys=True))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', required=True, choices=['domain', 'algebra', 'cup', 'four', 'null'])
    args = ap.parse_args()
    try:
        fn = {
            'domain': lane_domain,
            'algebra': lane_algebra,
            'cup': lane_cup,
            'four': lane_four,
            'null': lane_null,
        }[args.lane]
        ev = fn()
    except Exception as exc:
        ev = {'lane': args.lane, 'infrastructure_failure': True, 'scientific_negative': False, 'pass': False, 'error': repr(exc)}
    emit(ev)


if __name__ == '__main__':
    main()
