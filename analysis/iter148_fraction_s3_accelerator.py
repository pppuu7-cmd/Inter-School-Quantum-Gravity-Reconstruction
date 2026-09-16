#!/usr/bin/env python3
"""Exact rational accelerator for the frozen ITER148 D=4 M3 fast contraction.

This is an auxiliary execution-only implementation.  It evaluates the same
-2*EH_GammaGamma cubic contraction used by frozen ITER148 after analytically
removing the fixed phase pattern: X is real while chi1 and dR1 are purely
imaginary.  No basis, tau grid, heldout, routing, degree bound, bubble map,
classification or claim ceiling is changed.
"""
from __future__ import annotations
from fractions import Fraction as F
import itertools
import sympy as s

D = 4
HALF = F(1, 2)


def _F(x):
    x = s.Rational(x)
    return F(int(x.p), int(x.q))


def _vec(v):
    return tuple(_F(x) for x in v)


def _dot(a, b):
    return sum((a[i] * b[i] for i in range(D)), F(0))


def _A_R1(q):
    q2 = _dot(q, q)
    return [[q2 * int(a == b) - q[a] * q[b] for b in range(D)] for a in range(D)]


def _proj(A):
    tr = sum((A[i][i] for i in range(D)), F(0))
    return [[A[a][b] - HALF * tr * int(a == b) for b in range(D)] for a in range(D)]


def _chi0(k, n, mu):
    """Real matrix Y0 defined by frozen chi_tensor = i*Y0."""
    kn = _dot(k, n)
    return [[
        -HALF * (
            kn * (int(mu == a) * n[b] + int(mu == b) * n[a])
            - k[mu] * n[a] * n[b]
        )
        for b in range(D)
    ] for a in range(D)]


def _dR0(r, mu):
    """Real matrix Z0 defined by frozen dR_tensor = i*Z0."""
    A = _A_R1(r)
    return [[r[mu] * A[a][b] for b in range(D)] for a in range(D)]


def _eh_core(Hs, ps, perm=(0, 1, 2)):
    """Rational core of frozen EH Gamma-Gamma cubic for phases (1,i,i)."""
    Hs = [Hs[i] for i in perm]
    ps = [ps[i] for i in perm]
    P = []
    G1 = []
    G2 = {}

    for A, p in zip(Hs, ps):
        tr = sum((A[i][i] for i in range(D)), F(0))
        P.append([[HALF * tr * int(m == n) - A[m][n] for n in range(D)] for m in range(D)])
        G1.append([[[
            HALF * (p[m] * A[r][n] + p[n] * A[r][m] - p[r] * A[m][n])
            for n in range(D)
        ] for m in range(D)] for r in range(D)])

    for ib, ic in itertools.permutations(range(3), 2):
        A = Hs[ib]
        B = Hs[ic]
        pb = ps[ic]
        G2[(ib, ic)] = [[[
            HALF * sum((
                A[r][tt] * (
                    pb[m] * B[tt][n] + pb[n] * B[tt][m] - pb[tt] * B[m][n]
                )
                for tt in range(D)
            ), F(0))
            for n in range(D)
        ] for m in range(D)] for r in range(D)]

    out = F(0)
    for ia, ib, ic in itertools.permutations(range(3), 3):
        Pi = P[ia]
        Gb = G1[ib]
        Gc = G1[ic]
        for m in range(D):
            for n in range(D):
                pv = Pi[m][n]
                if pv == 0:
                    continue
                for r in range(D):
                    for tt in range(D):
                        out += pv * (
                            Gb[r][m][tt] * Gc[tt][n][r]
                            - Gb[r][m][n] * Gc[tt][r][tt]
                        )

    # In every Gamma1*Gamma2 product the fixed H phase product is i*i=-1.
    # Removing those phases reverses the signs of the four terms relative to
    # the literal complex implementation, exactly as below.
    for ia, ib, ic in itertools.permutations(range(3), 3):
        Ga = G1[ia]
        Gbc = G2[(ib, ic)]
        for m in range(D):
            n = m
            for r in range(D):
                for tt in range(D):
                    out -= Ga[r][m][tt] * Gbc[tt][n][r] + Gbc[r][m][tt] * Ga[tt][n][r]
                    out += Ga[r][m][n] * Gbc[tt][r][tt] + Gbc[r][m][n] * Ga[tt][r][tt]
    return out


def numerator(q, k, n, tau, perm=(0, 1, 2)):
    """Drop-in exact replacement for frozen base.numerator_fast."""
    q = _vec(q)
    k = _vec(k)
    n = _vec(n)
    tau = _F(tau)
    one = F(1)
    p = tuple(-q[i] - (one - tau) * k[i] for i in range(D))
    r = tuple(q[i] - tau * k[i] for i in range(D))
    X = _proj(_A_R1(p))
    total = F(0)
    for mu in range(D):
        Y = _proj(_chi0(k, n, mu))
        Z = _proj(_dR0(r, mu))
        total += -2 * _eh_core([X, Y, Z], [p, k, r], perm)
    ans = (one - tau) * total
    return (
        s.Rational(ans.numerator, ans.denominator),
        tuple(s.Rational(x.numerator, x.denominator) for x in p),
        tuple(s.Rational(x.numerator, x.denominator) for x in r),
    )
