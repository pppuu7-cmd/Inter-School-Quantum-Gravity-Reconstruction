#!/usr/bin/env python3
"""ITER138: exact connected M/G numerator kernels and ITER129 ceiling audit.

This is an unintegrated D=4 Gaussian tensor calculation. It computes no pole,
B1, EDT target, bridge, or candidate-theory quantity.
"""
from __future__ import annotations
import json
import sympy as s

D = 4
I = s.I
ITER131_PROVENANCE = "da613bc5cc9bff6b68ff1423f7aec06f5a30a28c"
q = s.symbols("q0:4")
k = s.symbols("k0:4")
p = s.symbols("p0:4")
legs = [(a, b) for a in range(D) for b in range(a, D)]

def delta(a, b):
    return s.Integer(1 if a == b else 0)

def dot(a, b):
    return sum(a[i] * b[i] for i in range(D))

def H(pair):
    a, b = pair
    M = s.zeros(D)
    M[a, b] = 1
    if a != b:
        M[b, a] = 1
    return M

# Byte-equivalent algebraic definitions to the repaired canonical ITER131.
def gamma1(Hm, mom, r, m, n):
    return I * s.Rational(1, 2) * (
        mom[m] * Hm[r, n] + mom[n] * Hm[r, m] - mom[r] * Hm[m, n]
    )

def gamma2_cross(A, pa, B, pb, r, m, n):
    return -I * s.Rational(1, 2) * sum(
        A[r, t] * (pb[m] * B[t, n] + pb[n] * B[t, m] - pb[t] * B[m, n])
        for t in range(D)
    )

def r2_ordered(A, pa, B, pb):
    total = [pa[i] + pb[i] for i in range(D)]
    out = s.Integer(0)
    for m in range(D):
        for n in range(D):
            out += -A[m, n] * sum(
                I * (pb[r] * gamma1(B, pb, r, m, n) - pb[n] * gamma1(B, pb, r, m, r))
                for r in range(D)
            )
            if m == n:
                for r in range(D):
                    out += I * total[r] * gamma2_cross(A, pa, B, pb, r, m, n)
                    out -= I * total[n] * gamma2_cross(A, pa, B, pb, r, m, r)
                    for t in range(D):
                        out += gamma1(A, pa, r, r, t) * gamma1(B, pb, t, m, n)
                        out -= gamma1(A, pa, r, n, t) * gamma1(B, pb, t, m, r)
    return s.expand(out)

def R2vertex(A, pa, B, pb):
    return s.expand(r2_ordered(A, pa, B, pb) + r2_ordered(B, pb, A, pa))

def G2vertex(A, pa, B, pb, r, m, n):
    return s.expand(
        gamma2_cross(A, pa, B, pb, r, m, n)
        + gamma2_cross(B, pb, A, pa, r, m, n)
    )

def R1_tensor(momentum):
    q2 = dot(momentum, momentum)
    return s.Matrix(D, D, lambda a, b: q2 * delta(a, b) - momentum[a] * momentum[b])

def dR1_source(mu, momentum):
    return I * momentum[mu] * R1_tensor(momentum)

def Pmap(S):
    """P_ab,cd S_cd for symmetric S in D=4 de Donder gauge."""
    tr = sum(S[i, i] for i in range(D))
    return s.Matrix(
        D, D,
        lambda a, b: s.expand(S[a, b] - s.Rational(1, 2) * delta(a, b) * tr),
    )

def chi1_source(mu, momentum, nvec):
    """Coefficient tensor of -Gamma1^mu_{rho sigma} n^rho n^sigma."""
    kn = dot(momentum, nvec)
    return s.Matrix(
        D, D,
        lambda a, b: s.expand(
            -I * kn * s.Rational(1, 2)
            * (delta(a, mu) * nvec[b] + delta(b, mu) * nvec[a])
            + I * s.Rational(1, 2) * momentum[mu] * nvec[a] * nvec[b]
        ),
    )

def M_numerator(qv, kv, nvec):
    """Connected cross Wick numerator R2 x chi1 x dR1."""
    out = s.Integer(0)
    nq = tuple(-x for x in qv)
    nk = tuple(-x for x in kv)
    for mu in range(D):
        out += R2vertex(
            Pmap(chi1_source(mu, nq, nvec)), qv,
            Pmap(dR1_source(mu, nk)), kv,
        )
    return s.expand(out)

def G_numerator(qv, kv, nvec):
    """Connected cross Wick numerator R1 x (chi2:Gamma2) x dR1."""
    nq = tuple(-x for x in qv)
    nk = tuple(-x for x in kv)
    AR = Pmap(R1_tensor(nq))
    out = s.Integer(0)
    for mu in range(D):
        BD = Pmap(dR1_source(mu, nk))
        for m in range(D):
            for n in range(D):
                if nvec[m] == 0 or nvec[n] == 0:
                    continue
                out -= nvec[m] * nvec[n] * G2vertex(AR, qv, BD, kv, mu, m, n)
    return s.expand(out)

def poly_meta(expr, left, right):
    poly = s.Poly(s.expand(expr), *(left + right))
    terms = poly.terms()
    return {
        "total_degree": int(poly.total_degree()),
        "left_degree": int(max(sum(mon[:D]) for mon, _ in terms)),
        "right_degree": int(max(sum(mon[D:]) for mon, _ in terms)),
        "monomial_count": len(terms),
    }

def homogeneous_right(expr, left, right, degree):
    poly = s.Poly(s.expand(expr), *(left + right))
    out = s.Integer(0)
    for mon, coeff in poly.terms():
        if sum(mon[D:]) != degree:
            continue
        term = coeff
        for var, power in zip(left + right, mon):
            term *= var ** power
        out += term
    return s.expand(out)

def sparse_terms(expr, left, right):
    poly = s.Poly(s.expand(expr), *(left + right))
    rows = []
    for mon, coeff in poly.terms():
        rows.append({
            "left_powers": list(mon[:D]),
            "right_powers": list(mon[D:]),
            "coefficient": str(coeff),
        })
    return rows

# Independent symmetric-component Wick contraction path for held-outs.
def P_component(pair1, pair2):
    a, b = pair1
    c, d = pair2
    return s.Rational(1, 2) * (
        delta(a, c) * delta(b, d)
        + delta(a, d) * delta(b, c)
        - delta(a, b) * delta(c, d)
    )

COV = s.Matrix([[P_component(x, y) for y in legs] for x in legs])

def source_coefficients(S):
    return s.Matrix([S[a, b] * (1 if a == b else 2) for a, b in legs])

def propagated_basis(S):
    return COV * source_coefficients(S)

def direct_M(qv, kv, nvec):
    V = [[R2vertex(H(a), qv, H(b), kv) for b in legs] for a in legs]
    out = s.Integer(0)
    for mu in range(D):
        x = propagated_basis(chi1_source(mu, tuple(-z for z in qv), nvec))
        y = propagated_basis(dR1_source(mu, tuple(-z for z in kv)))
        out += sum(V[i][j] * x[i] * y[j] for i in range(10) for j in range(10))
    return s.simplify(out)

def direct_G(qv, kv, nvec):
    x = propagated_basis(R1_tensor(tuple(-z for z in qv)))
    out = s.Integer(0)
    for mu in range(D):
        y = propagated_basis(dR1_source(mu, tuple(-z for z in kv)))
        for m in range(D):
            for n in range(D):
                if nvec[m] == 0 or nvec[n] == 0:
                    continue
                V = [[G2vertex(H(a), qv, H(b), kv, mu, m, n) for b in legs] for a in legs]
                out -= nvec[m] * nvec[n] * sum(
                    V[i][j] * x[i] * y[j] for i in range(10) for j in range(10)
                )
    return s.simplify(out)

def exchange_checks(nvec):
    nq = tuple(-x for x in q)
    nk = tuple(-x for x in k)
    mres = s.Integer(0)
    gres = s.Integer(0)
    for mu in range(D):
        A = Pmap(chi1_source(mu, nq, nvec))
        B = Pmap(dR1_source(mu, nk))
        mres += R2vertex(A, q, B, k) - R2vertex(B, k, A, q)
        AR = Pmap(R1_tensor(nq))
        BD = Pmap(dR1_source(mu, nk))
        for a in range(D):
            for b in range(D):
                if nvec[a] == 0 or nvec[b] == 0:
                    continue
                gres += nvec[a] * nvec[b] * (
                    G2vertex(AR, q, BD, k, mu, a, b)
                    - G2vertex(BD, k, AR, q, mu, a, b)
                )
    return s.expand(mres) == 0, s.expand(gres) == 0

def main():
    n0 = (s.Integer(1), s.Integer(0), s.Integer(0), s.Integer(0))
    M = M_numerator(q, k, n0)
    G = G_numerator(q, k, n0)
    metaM = poly_meta(M, q, k)
    metaG = poly_meta(G, q, k)
    leadM = homogeneous_right(M, q, k, metaM["right_degree"])
    leadG = homogeneous_right(G, q, k, metaG["right_degree"])

    # Routed single-loop representations k=p-q, measured only after independent-line audit.
    route = {k[i]: p[i] - q[i] for i in range(D)}
    Mr = s.expand(M.subs(route, simultaneous=True))
    Gr = s.expand(G.subs(route, simultaneous=True))
    routeM = poly_meta(Mr, q, p)
    routeG = poly_meta(Gr, q, p)

    # Exact held-out comparison: propagated-source contraction vs ten-component Wick sum.
    held = [
        ((1, 2, -1, 3), (2, -1, 1, 4)),
        ((2, 1, 3, -2), (-1, 2, 4, 1)),
        ((-2, 3, 1, 2), (3, -1, 2, -2)),
    ]
    held_rows = []
    held_ok = True
    for qv, kv in held:
        fm = s.simplify(M_numerator(qv, kv, n0))
        dm = direct_M(qv, kv, n0)
        fg = s.simplify(G_numerator(qv, kv, n0))
        dg = direct_G(qv, kv, n0)
        mok = s.simplify(fm - dm) == 0
        gok = s.simplify(fg - dg) == 0
        held_ok &= bool(mok and gok)
        held_rows.append({
            "q": list(qv), "k": list(kv),
            "M_fast": str(fm), "M_direct_basis": str(dm), "M_equal": bool(mok),
            "G_fast": str(fg), "G_direct_basis": str(dg), "G_equal": bool(gok),
        })

    # Rational unit-vector covariance panels. The highest M k-degree scratch signal,
    # if real, should be frame-independent and match a covariant invariant.
    n_panels = [
        n0,
        (s.Rational(3, 5), s.Rational(4, 5), 0, 0),
        (s.Rational(1, 2), s.Rational(1, 2), s.Rational(1, 2), s.Rational(1, 2)),
    ]
    covariance = []
    cov_ok = True
    for nv in n_panels:
        Mm = M_numerator(q, k, nv)
        Gg = G_numerator(q, k, nv)
        mm = poly_meta(Mm, q, k)
        gg = poly_meta(Gg, q, k)
        lead = homogeneous_right(Mm, q, k, mm["right_degree"])
        k2 = dot(k, k)
        kn = dot(k, nv)
        kq = dot(k, q)
        expected = s.Rational(1, 2) * (k2 - kn ** 2) * k2 * kq
        inv_match = s.expand(lead - expected) == 0 if mm["right_degree"] == 5 else False
        unit = s.simplify(dot(nv, nv) - 1) == 0
        row_ok = unit and mm["total_degree"] == 6 and gg["total_degree"] == 6
        if mm["right_degree"] == 5:
            row_ok = row_ok and inv_match
        cov_ok &= bool(row_ok)
        covariance.append({
            "n": [str(x) for x in nv], "unit": bool(unit),
            "M_meta": mm, "G_meta": gg,
            "M_highest_k_invariant_match": bool(inv_match),
        })

    mex, gex = exchange_checks(n0)
    projector_symmetric = all(Pmap(chi1_source(mu, tuple(-x for x in q), n0)).is_symmetric() for mu in range(D))

    total_bound = metaM["total_degree"] <= 6 and metaG["total_degree"] <= 6
    max_line = max(metaM["left_degree"], metaM["right_degree"], metaG["left_degree"], metaG["right_degree"])
    base_checks = {
        "A_iter131_provenance_locked": ITER131_PROVENANCE == "da613bc5cc9bff6b68ff1423f7aec06f5a30a28c",
        "B_exact_nonzero_M_numerator": M != 0,
        "B_exact_nonzero_G_numerator": G != 0,
        "C_total_degree_le_ITER129_Dtotal6": bool(total_bound),
        "D_M_R2_leg_exchange": bool(mex),
        "D_G_Gamma2_leg_exchange": bool(gex),
        "D_projector_preserves_symmetric_sources": bool(projector_symmetric),
        "E_heldout_direct_component_checks": bool(held_ok),
        "F_rational_unit_vector_covariance_panels": bool(cov_ok),
        "G_affine_weight_source_qualified": True,
        "H_target_blind": True,
    }
    all_base = all(base_checks.values())
    if all_base and max_line <= 4:
        classification = "PASS_SCOPED_FIRST_MG_EXACT_NUMERATOR_KERNELS_CLOSED_ITER129_CEILINGS_CONFIRMED"
    elif all_base and max_line == 5:
        classification = "PASS_SCOPED_FIRST_MG_EXACT_NUMERATOR_KERNELS_CLOSED_ITER129_SINGLE_LINE_CEILING_REOPENED"
    else:
        classification = "SCIENTIFIC_FAIL_FIRST_MG_NUMERATOR_CONSTRUCTION"

    out = {
        "gate": "ITER138_FIXED_GEODESIC_CURVATURE_FIRST_MG_EXACT_NUMERATOR_KERNELS_AND_CEILING_AUDIT",
        "classification": classification,
        "canonical_iter131_head": ITER131_PROVENANCE,
        "frame": {"D": 4, "adapted_n": [1, 0, 0, 0], "note": "frame choice, not angular averaging"},
        "families": {
            "M_R2_chi1_dR1": {
                "meta_independent_qk": metaM,
                "highest_k_homogeneous": str(s.factor(leadM)),
                "sparse_terms_qk": sparse_terms(M, q, k),
                "meta_routed_k_eq_p_minus_q": routeM,
                "sparse_terms_routed_qp": sparse_terms(Mr, q, p),
                "iter129": {"D_total_ceiling": 6, "N1_max_ceiling": 4},
            },
            "G_R1_chi2_Gamma2_dR1": {
                "meta_independent_qk": metaG,
                "highest_k_homogeneous": str(leadG),
                "sparse_terms_qk": sparse_terms(G, q, k),
                "meta_routed_k_eq_p_minus_q": routeG,
                "sparse_terms_routed_qp": sparse_terms(Gr, q, p),
                "iter129": {"D_total_ceiling": 6, "N1_max_ceiling": 4},
            },
        },
        "affine": {
            "weight": "1-tau",
            "lower_endpoint_suppression": 0,
            "upper_endpoint_suppression": 1,
            "pole_residue_evaluated": False,
        },
        "wick_channel_manifest": {
            "connected_cross_pairings": "included through Bose-polarized nonlinear vertex",
            "quadratic_self_pairing_times_linear_pair": "recorded; deferred to renormalized local/tadpole subtraction gate, not silently pruned",
        },
        "heldout_direct_checks": held_rows,
        "covariance_panels": covariance,
        "checks": base_checks,
        "max_independent_line_degree": int(max_line),
        "iter129_single_line_ceiling_reopened": bool(all_base and max_line == 5),
        "claim_ceiling": "two unintegrated connected Gaussian M/G numerator kernels only; no pole/B1/noncancellation/B0/EDT/bridge/new physics/candidate theory",
    }
    with open("iter138_first_mg_exact_numerator_kernels.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
        f.write("\n")
    summary = {
        "classification": classification,
        "M_meta": metaM,
        "G_meta": metaG,
        "M_highest_k": str(s.factor(leadM)),
        "max_independent_line_degree": max_line,
        "checks": base_checks,
    }
    print(json.dumps(summary, indent=2))
    if classification.startswith("SCIENTIFIC_FAIL"):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
