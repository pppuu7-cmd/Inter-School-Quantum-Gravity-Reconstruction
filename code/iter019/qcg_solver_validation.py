#!/usr/bin/env python3
import argparse
import cmath
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

OUT = Path('out')
OUT.mkdir(exist_ok=True)
K_TARGET = 12


def qpow(exponent, k):
    if k is None:
        return 1.0 + 0.0j
    return cmath.exp(2j * math.pi * float(exponent) / (k + 2))


def qnum(x, k):
    if k is None:
        return complex(float(x))
    # Exact branch-equivalent sine form of the frozen target definition.
    return complex(math.sin(math.pi * float(x) / (k + 2)) / math.sin(math.pi / (k + 2)))


def magnetic_values(tj):
    return np.array([(-tj + 2 * i) / 2 for i in range(tj + 1)], dtype=float)


def rep(tj, k):
    j = tj / 2
    ms = magnetic_values(tj)
    n = tj + 1
    Jz = np.diag(ms.astype(complex))
    Jp = np.zeros((n, n), dtype=complex)
    Jm = np.zeros((n, n), dtype=complex)
    for col, m in enumerate(ms):
        if m < j:
            Jp[col + 1, col] = cmath.sqrt(qnum(j - m, k) * qnum(j + m + 1, k))
        if m > -j:
            Jm[col - 1, col] = cmath.sqrt(qnum(j + m, k) * qnum(j - m + 1, k))
    return ms, Jz, Jp, Jm


def tensor_ops(tj1, tj2, k):
    ms1, z1, p1, m1 = rep(tj1, k)
    ms2, z2, p2, m2 = rep(tj2, k)
    I1 = np.eye(tj1 + 1, dtype=complex)
    I2 = np.eye(tj2 + 1, dtype=complex)
    if k is None:
        km1 = kp1 = I1
        km2 = kp2 = I2
    else:
        km1 = np.diag([qpow(-x / 2, k) for x in ms1])
        kp1 = np.diag([qpow(x / 2, k) for x in ms1])
        km2 = np.diag([qpow(-x / 2, k) for x in ms2])
        kp2 = np.diag([qpow(x / 2, k) for x in ms2])
    Jp = np.kron(km1, p2) + np.kron(p1, kp2)
    Jm = np.kron(km1, m2) + np.kron(m1, kp2)
    Jz = np.kron(I1, z2) + np.kron(z1, I2)
    weights = np.array([a + b for a in ms1 for b in ms2], dtype=float)
    return ms1, ms2, weights, Jz, Jp, Jm


def admissible(t1, t2, t3, k):
    if abs(t1 - t2) > t3 or t3 > t1 + t2:
        return False
    if (t1 + t2 + t3) % 2:
        return False
    if k is not None:
        if any(t > k for t in (t1, t2, t3)):
            return False
        if t1 + t2 + t3 > 2 * k:
            return False
    return True


def solve_channel(t1, t2, t3, k):
    if not admissible(t1, t2, t3, k):
        raise ValueError(f'inadmissible channel {(t1,t2,t3,k)}')
    _, _, weights, Jz, Jp, Jm = tensor_ops(t1, t2, k)
    j = t3 / 2
    idx = np.where(np.isclose(weights, j))[0]
    idx_out = np.where(np.isclose(weights, j + 1))[0]
    A = Jp[np.ix_(idx_out, idx)] if len(idx_out) else np.zeros((0, len(idx)), dtype=complex)

    if A.shape[0]:
        _, singular, vh = np.linalg.svd(A, full_matrices=True)
        rank = int(np.sum(singular > 1e-10))
        null_dim = A.shape[1] - rank
        if null_dim != 1:
            raise RuntimeError(f'highest-weight nullspace dimension={null_dim} for {(t1,t2,t3)}')
        v_sub = vh.conj().T[:, rank]
    else:
        singular = np.array([], dtype=float)
        null_dim = len(idx)
        if null_dim != 1:
            raise RuntimeError(f'highest-weight nullspace dimension={null_dim} for {(t1,t2,t3)}')
        v_sub = np.ones(1, dtype=complex)

    bilinear_norm = v_sub.T @ v_sub
    if abs(bilinear_norm) < 1e-13:
        raise RuntimeError(f'isotropic highest-weight vector for {(t1,t2,t3)}')
    v_sub = v_sub / cmath.sqrt(bilinear_norm)

    D = len(weights)
    vec = np.zeros(D, dtype=complex)
    vec[idx] = v_sub
    states = {round(j, 12): vec}
    m = j
    while m > -j + 1e-12:
        ladder = cmath.sqrt(qnum(j + m, k) * qnum(j - m + 1, k))
        if abs(ladder) < 1e-13:
            raise RuntimeError(f'zero target lowering coefficient at {(t1,t2,t3,m,k)}')
        vec = (Jm @ vec) / ladder
        m -= 1
        states[round(m, 12)] = vec

    ms3, z3, p3, m3 = rep(t3, k)
    C = np.column_stack([states[round(float(m), 12)] for m in ms3])
    residuals = {
        'Jz': float(np.max(np.abs(Jz @ C - C @ z3))),
        'Jplus': float(np.max(np.abs(Jp @ C - C @ p3))),
        'Jminus': float(np.max(np.abs(Jm @ C - C @ m3))),
    }
    gram = C.T @ C
    a9_self = float(np.max(np.abs(gram - np.eye(t3 + 1))))
    return {
        'C': C,
        'null_dim': null_dim,
        'singular_values': singular,
        'residuals': residuals,
        'max_intertwiner_residual': max(residuals.values()),
        'a9_self_residual': a9_self,
    }


def b2_singlet(tj, k):
    j = tj / 2
    ms = magnetic_values(tj)
    dj = qnum(2 * j + 1, k)
    out = np.zeros(((tj + 1) ** 2, 1), dtype=complex)
    for i, m in enumerate(ms):
        for ii, mpv in enumerate(ms):
            if abs(mpv + m) < 1e-12:
                exponent = int(round(j - m))
                out[i * (tj + 1) + ii, 0] = ((-1) ** exponent) * qpow(m / 2, k) / cmath.sqrt(dj)
    return out


def panel_channels():
    return {
        (1, 1): [0, 2],
        (1, 2): [1, 3],
        (2, 2): [0, 2, 4],
        (6, 6): list(range(0, 13, 2)),
        (8, 8): list(range(0, 9, 2)),
    }


def all_solver_results(k=K_TARGET):
    result = {}
    for pair, targets in panel_channels().items():
        for t3 in targets:
            result[(pair[0], pair[1], t3)] = solve_channel(pair[0], pair[1], t3, k)
    return result


def lane_algebra():
    results = all_solver_results(K_TARGET)
    rows = []
    for key, r in sorted(results.items()):
        rows.append({
            'twice_spins': list(key),
            'null_dim': r['null_dim'],
            'max_intertwiner_residual': r['max_intertwiner_residual'],
            'Jz_residual': r['residuals']['Jz'],
            'Jplus_residual': r['residuals']['Jplus'],
            'Jminus_residual': r['residuals']['Jminus'],
            'a9_self_diagnostic': r['a9_self_residual'],
        })
    max_res = max(x['max_intertwiner_residual'] for x in rows)
    all_null_one = all(x['null_dim'] == 1 for x in rows)
    passed = bool(max_res < 5e-10 and all_null_one)
    return {
        'lane': 'algebra',
        'k': K_TARGET,
        'channels': rows,
        'channel_count': len(rows),
        'max_intertwiner_residual': max_res,
        'all_highest_weight_nullspaces_dim_one': all_null_one,
        'threshold': 5e-10,
        'pass': passed,
    }


# High-precision implementation used only where the non-normal bilinear A8
# projector creates large cancelling matrix entries at k=12.
def mp_qpow(exponent, k):
    if k is None:
        return mp.mpc(1)
    return mp.e ** (2 * mp.pi * 1j * mp.mpf(exponent) / (k + 2))


def mp_qnum(x, k):
    if k is None:
        return mp.mpf(x)
    return mp.sin(mp.pi * mp.mpf(x) / (k + 2)) / mp.sin(mp.pi / (k + 2))


def mp_ms(tj):
    return [mp.mpf(-tj + 2 * i) / 2 for i in range(tj + 1)]


def mp_plus_coeff(tj, m, k):
    j = mp.mpf(tj) / 2
    if m >= j:
        return mp.mpc(0)
    return mp.sqrt(mp_qnum(j - m, k) * mp_qnum(j + m + 1, k))


def mp_minus_coeff(tj, m, k):
    j = mp.mpf(tj) / 2
    if m <= -j:
        return mp.mpc(0)
    return mp.sqrt(mp_qnum(j + m, k) * mp_qnum(j - m + 1, k))


def mp_apply_plus(t1, t2, k, vec):
    m1s, m2s = mp_ms(t1), mp_ms(t2)
    d2 = t2 + 1
    out = [mp.mpc(0) for _ in vec]
    for i1, m1 in enumerate(m1s):
        for i2, m2 in enumerate(m2s):
            c = vec[i1 * d2 + i2]
            if c == 0:
                continue
            if i2 < t2:
                out[i1 * d2 + i2 + 1] += mp_qpow(-m1 / 2, k) * mp_plus_coeff(t2, m2, k) * c
            if i1 < t1:
                out[(i1 + 1) * d2 + i2] += mp_plus_coeff(t1, m1, k) * mp_qpow(m2 / 2, k) * c
    return out


def mp_apply_minus(t1, t2, k, vec):
    m1s, m2s = mp_ms(t1), mp_ms(t2)
    d2 = t2 + 1
    out = [mp.mpc(0) for _ in vec]
    for i1, m1 in enumerate(m1s):
        for i2, m2 in enumerate(m2s):
            c = vec[i1 * d2 + i2]
            if c == 0:
                continue
            if i2 > 0:
                out[i1 * d2 + i2 - 1] += mp_qpow(-m1 / 2, k) * mp_minus_coeff(t2, m2, k) * c
            if i1 > 0:
                out[(i1 - 1) * d2 + i2] += mp_minus_coeff(t1, m1, k) * mp_qpow(m2 / 2, k) * c
    return out


def mp_solve_channel(t1, t2, t3, k):
    m1s, m2s = mp_ms(t1), mp_ms(t2)
    d2 = t2 + 1
    D = (t1 + 1) * (t2 + 1)
    j = mp.mpf(t3) / 2
    idx = [i1 * d2 + i2 for i1, m1 in enumerate(m1s) for i2, m2 in enumerate(m2s) if m1 + m2 == j]
    idx_out = [i1 * d2 + i2 for i1, m1 in enumerate(m1s) for i2, m2 in enumerate(m2s) if m1 + m2 == j + 1]
    out_pos = {ix: r for r, ix in enumerate(idx_out)}
    A = [[mp.mpc(0) for _ in idx] for _ in idx_out]
    for col, ix in enumerate(idx):
        basis = [mp.mpc(0) for _ in range(D)]
        basis[ix] = 1
        y = mp_apply_plus(t1, t2, k, basis)
        for out_ix, row in out_pos.items():
            A[row][col] = y[out_ix]

    coeff = [mp.mpc(0) for _ in idx]
    coeff[0] = 1
    for row_index, row in enumerate(A):
        nz = [c for c, x in enumerate(row) if abs(x) > mp.mpf('1e-60')]
        if nz != [row_index, row_index + 1]:
            raise RuntimeError(f'unexpected highest-weight band structure {nz}')
        coeff[row_index + 1] = -row[row_index] * coeff[row_index] / row[row_index + 1]
    norm = mp.sqrt(sum(x * x for x in coeff))
    coeff = [x / norm for x in coeff]
    vec = [mp.mpc(0) for _ in range(D)]
    for ix, c in zip(idx, coeff):
        vec[ix] = c

    states = {str(j): vec}
    m = j
    while m > -j:
        ladder = mp.sqrt(mp_qnum(j + m, k) * mp_qnum(j - m + 1, k))
        vec = [x / ladder for x in mp_apply_minus(t1, t2, k, vec)]
        m -= 1
        states[str(m)] = vec
    m3s = mp_ms(t3)
    return [[states[str(m)][row] for m in m3s] for row in range(D)]


def mp_add_projector(P, C):
    D = len(C)
    d = len(C[0])
    for i in range(D):
        for j in range(D):
            P[i][j] += sum(C[i][a] * C[j][a] for a in range(d))


def mp_matmul(A, B):
    n, p, m = len(A), len(A[0]), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(p)) for j in range(m)] for i in range(n)]


def lane_projector_cap():
    results = all_solver_results(K_TARGET)
    group_rows = []
    max_a9 = 0.0
    for pair, targets in panel_channels().items():
        C_all = np.column_stack([results[(pair[0], pair[1], t)]['C'] for t in targets])
        gram = C_all.T @ C_all
        residual = float(np.max(np.abs(gram - np.eye(gram.shape[0]))))
        max_a9 = max(max_a9, residual)
        group_rows.append({'twice_input_spins': list(pair), 'twice_output_spins': targets, 'a9_cross_channel_residual': residual})

    C33 = [results[(6, 6, t)]['C'] for t in range(0, 13, 2)]
    P33 = sum((C @ C.T for C in C33), np.zeros((49, 49), dtype=complex))
    full33 = float(np.max(np.abs(P33 - np.eye(49))))

    # High precision is required here because the bilinear projector is strongly
    # non-normal: entries are O(10^3) and cancel to make an idempotent rank-25 map.
    mp.mp.dps = 80
    D44 = 81
    P44_mp = [[mp.mpc(0) for _ in range(D44)] for _ in range(D44)]
    for t in range(0, 9, 2):
        mp_add_projector(P44_mp, mp_solve_channel(8, 8, t, K_TARGET))
    P44_sq = mp_matmul(P44_mp, P44_mp)
    idem44_mp = max(abs(P44_sq[i][j] - P44_mp[i][j]) for i in range(D44) for j in range(D44))
    P44_np = np.array([[complex(x) for x in row] for row in P44_mp], dtype=complex)
    svals44 = np.linalg.svd(P44_np, compute_uv=False)
    rank44 = int(np.sum(svals44 > 1e-8))
    trace44 = sum(P44_mp[i][i] for i in range(D44))

    cap_rows = []
    max_cap = 0.0
    for tj in [1, 2, 4, 6, 8]:
        solver = solve_channel(tj, tj, 0, K_TARGET)['C']
        target = b2_singlet(tj, K_TARGET)
        plus = float(np.max(np.abs(solver - target)))
        minus = float(np.max(np.abs(solver + target)))
        residual = min(plus, minus)
        max_cap = max(max_cap, residual)
        cap_rows.append({'twice_j': tj, 'residual_up_to_sign': residual, 'selected_sign': 1 if plus <= minus else -1})

    idem44 = float(idem44_mp)
    trace44_err = float(abs(trace44 - 25))
    passed = bool(
        max_a9 < 5e-10 and
        full33 < 2e-9 and
        idem44 < 2e-9 and
        rank44 == 25 and
        max_cap < 2e-9
    )
    return {
        'lane': 'projector-cap',
        'k': K_TARGET,
        'a9_groups': group_rows,
        'max_a9_residual': max_a9,
        'full_3x3_completeness_residual': full33,
        'projector_4x4_idempotence_residual_high_precision': idem44,
        'projector_4x4_rank_svd_tol_1e-8': rank44,
        'projector_4x4_trace_minus_25_abs': trace44_err,
        'projector_4x4_high_precision_digits': 80,
        'cap_rows': cap_rows,
        'max_B2_singlet_residual_up_to_sign': max_cap,
        'thresholds': {'A9': 5e-10, 'full_3x3': 2e-9, 'projector_4x4': 2e-9, 'rank_tol': 1e-8, 'B2': 2e-9},
        'pass': passed,
    }


def compose_left(t1, t2, t3, t12, tJ, k):
    C12 = solve_channel(t1, t2, t12, k)['C']
    Cx = solve_channel(t12, t3, tJ, k)['C']
    d1, d2, d3, d12, dJ = t1 + 1, t2 + 1, t3 + 1, t12 + 1, tJ + 1
    A = np.zeros((d1 * d2 * d3, dJ), dtype=complex)
    for i1 in range(d1):
        for i2 in range(d2):
            r12 = i1 * d2 + i2
            for i3 in range(d3):
                r = (i1 * d2 + i2) * d3 + i3
                for im in range(d12):
                    A[r, :] += C12[r12, im] * Cx[im * d3 + i3, :]
    return A


def compose_right(t1, t2, t3, t23, tJ, k):
    C23 = solve_channel(t2, t3, t23, k)['C']
    Cx = solve_channel(t1, t23, tJ, k)['C']
    d1, d2, d3, d23, dJ = t1 + 1, t2 + 1, t3 + 1, t23 + 1, tJ + 1
    B = np.zeros((d1 * d2 * d3, dJ), dtype=complex)
    for i1 in range(d1):
        for i2 in range(d2):
            for i3 in range(d3):
                r = (i1 * d2 + i2) * d3 + i3
                r23 = i2 * d3 + i3
                for im in range(d23):
                    B[r, :] += C23[r23, im] * Cx[i1 * d23 + im, :]
    return B


def recoupling_panel(t1, t2, t3, tJ, k):
    max_t12 = k if k is not None else t1 + t2
    max_t23 = k if k is not None else t2 + t3
    left = [x for x in range(max_t12 + 1) if admissible(t1, t2, x, k) and admissible(x, t3, tJ, k)]
    right = [x for x in range(max_t23 + 1) if admissible(t2, t3, x, k) and admissible(t1, x, tJ, k)]
    As = [compose_left(t1, t2, t3, x, tJ, k) for x in left]
    Bs = [compose_right(t1, t2, t3, x, tJ, k) for x in right]
    Fs = []
    for Mcol in range(tJ + 1):
        F = np.array([[A[:, Mcol].T @ B[:, Mcol] for B in Bs] for A in As], dtype=complex)
        Fs.append(F)
    return left, right, Fs


def lane_recoupling():
    panels = [(1, 1, 1, 1), (2, 2, 2, 2)]
    rows = []
    global_m = global_orth = global_imag = 0.0
    passed = True
    for panel in panels:
        left, right, Fs = recoupling_panel(*panel, K_TARGET)
        square = len(left) == len(right)
        F0 = Fs[0]
        m_res = max(float(np.max(np.abs(F - F0))) for F in Fs)
        orth_res = max(float(np.max(np.abs(F.T @ F - np.eye(F.shape[0])))) for F in Fs)
        imag = max(float(np.max(np.abs(F.imag))) for F in Fs)
        global_m = max(global_m, m_res)
        global_orth = max(global_orth, orth_res)
        global_imag = max(global_imag, imag)
        row_pass = square and m_res < 2e-9 and orth_res < 2e-9 and imag < 2e-9
        passed = passed and row_pass
        rows.append({
            'twice_spins_j1_j2_j3_J': list(panel),
            'left_intermediate_twice_spins': left,
            'right_intermediate_twice_spins': right,
            'square': square,
            'M_independence_residual': m_res,
            'transpose_orthogonality_residual': orth_res,
            'max_imaginary_part': imag,
            'representative_F': [[[float(z.real), float(z.imag)] for z in row] for row in F0],
            'pass': row_pass,
        })
    return {
        'lane': 'recoupling',
        'k': K_TARGET,
        'panels': rows,
        'max_M_independence_residual': global_m,
        'max_transpose_orthogonality_residual': global_orth,
        'max_imaginary_part': global_imag,
        'threshold': 2e-9,
        'phase_or_row_column_sign_fit_performed': False,
        'pass': bool(passed),
    }


def lane_classical_limit():
    channels = [(1, 1, 0), (1, 1, 2), (2, 2, 0), (2, 2, 2), (2, 2, 4)]
    rows = []
    max_diff = 0.0
    for ch in channels:
        C0 = solve_channel(*ch, None)['C']
        Ck = solve_channel(*ch, 10000)['C']
        P0 = C0 @ C0.T
        Pk = Ck @ Ck.T
        diff = float(np.linalg.norm(P0 - Pk))
        max_diff = max(max_diff, diff)
        rows.append({'twice_spins': list(ch), 'projector_frobenius_difference': diff})
    return {
        'lane': 'classical-limit',
        'comparison_k': 10000,
        'channels': rows,
        'max_projector_frobenius_difference': max_diff,
        'threshold': 2e-3,
        'raw_sign_sensitive_coefficients_compared': False,
        'scope': 'continuity sanity check only; not a continuum quantum-gravity result',
        'pass': bool(max_diff < 2e-3),
    }


def write_evidence(ev):
    (OUT / 'evidence.json').write_text(json.dumps(ev, indent=2, sort_keys=True) + '\n')
    (OUT / 'evidence.md').write_text('# ITER019 lane evidence\n\n```json\n' + json.dumps(ev, indent=2, sort_keys=True) + '\n```\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', required=True, choices=['algebra', 'projector-cap', 'recoupling', 'classical-limit'])
    args = ap.parse_args()
    try:
        fn = {
            'algebra': lane_algebra,
            'projector-cap': lane_projector_cap,
            'recoupling': lane_recoupling,
            'classical-limit': lane_classical_limit,
        }[args.lane]
        ev = fn()
    except Exception as exc:
        ev = {'lane': args.lane, 'infrastructure_failure': True, 'scientific_negative': False, 'error': repr(exc)}
    write_evidence(ev)
    print(json.dumps(ev, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
