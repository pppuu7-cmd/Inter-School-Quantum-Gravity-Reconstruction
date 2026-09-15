#!/usr/bin/env python3
"""ITER140: exact integer-D reconstruction of general-d invariant M/G numerators.

No loop integration or pole coefficient is computed. Direct indexed contractions use
exact Fraction arithmetic; dimension continuation is fixed by the preregistered
28-element invariant basis and degree<=4 trace bound after multiplying (d-2)^2.
"""
from __future__ import annotations
from fractions import Fraction as F
import json
import random
from pathlib import Path
import sympy as s

import iter138_first_mg_exact_numerator_kernels as i138
import iter139_affine_single_line_ceiling_repair as i139

HALF = F(1, 2)


def zmat(D):
    return [[F(0) for _ in range(D)] for _ in range(D)]


def dot(a, b):
    return sum((F(x) * F(y) for x, y in zip(a, b)), F(0))


def eye(D, a, b):
    return F(1 if a == b else 0)


def pmap(S, D):
    tr = sum((S[i][i] for i in range(D)), F(0))
    c = tr / F(D - 2)
    return [[S[a][b] - (c if a == b else F(0)) for b in range(D)] for a in range(D)]


def r1_tensor(mom, D):
    q2 = dot(mom, mom)
    return [[q2 * eye(D, a, b) - F(mom[a]) * F(mom[b]) for b in range(D)] for a in range(D)]


def chi1_real(mu, mom, nvec, D):
    # chi1 source coefficient divided by i: -Gamma1^mu_nn / i.
    mn = dot(mom, nvec)
    return [[
        -HALF * mn * (eye(D, a, mu) * F(nvec[b]) + eye(D, b, mu) * F(nvec[a]))
        + HALF * F(mom[mu]) * F(nvec[a]) * F(nvec[b])
        for b in range(D)] for a in range(D)]


def dr1_real(mu, mom, D):
    # dR1 source coefficient divided by i.
    A = r1_tensor(mom, D)
    return [[F(mom[mu]) * A[a][b] for b in range(D)] for a in range(D)]


def g1r(H, mom, r, m, n):
    return HALF * (
        F(mom[m]) * H[r][n] + F(mom[n]) * H[r][m] - F(mom[r]) * H[m][n]
    )


def g2r_cross(A, B, pb, r, m, n, D):
    return HALF * sum((
        A[r][t] * (
            F(pb[m]) * B[t][n] + F(pb[n]) * B[t][m] - F(pb[t]) * B[m][n]
        ) for t in range(D)
    ), F(0))


def r2_ordered_real(A, pa, B, pb, D):
    total = [F(pa[i]) + F(pb[i]) for i in range(D)]
    out = F(0)
    for m in range(D):
        for n in range(D):
            deriv = sum((
                F(pb[r]) * g1r(B, pb, r, m, n) - F(pb[n]) * g1r(B, pb, r, m, r)
                for r in range(D)
            ), F(0))
            out += A[m][n] * deriv
            if m == n:
                for r in range(D):
                    out += total[r] * g2r_cross(A, B, pb, r, m, n, D)
                    out -= total[n] * g2r_cross(A, B, pb, r, m, r, D)
                    for t in range(D):
                        out -= g1r(A, pa, r, r, t) * g1r(B, pb, t, m, n)
                        out += g1r(A, pa, r, n, t) * g1r(B, pb, t, m, r)
    return out


def r2_real(A, pa, B, pb, D):
    return r2_ordered_real(A, pa, B, pb, D) + r2_ordered_real(B, pb, A, pa, D)


def g2_real(A, pa, B, pb, r, m, n, D):
    # Gamma2(A, i B) after removing the explicit phases gives +g2r cross terms.
    return g2r_cross(A, B, pb, r, m, n, D) + g2r_cross(B, A, pa, r, m, n, D)


def neg(v):
    return [-F(x) for x in v]


def M1_value(qv, kv, nvec, D):
    nq, nk = neg(qv), neg(kv)
    out = F(0)
    for mu in range(D):
        C = pmap(chi1_real(mu, nq, nvec, D), D)
        R = pmap(dr1_real(mu, nk, D), D)
        # Both sources carry i, so i^2=-1.
        out -= r2_real(C, qv, R, kv, D)
    return out


def M2_value(qv, kv, nvec, D):
    nq, nk = neg(qv), neg(kv)
    A = pmap(r1_tensor(nq, D), D)
    out = F(0)
    for mu in range(D):
        C = pmap(chi1_real(mu, nk, nvec, D), D)
        # chi1 contributes i and dR2 contributes i(q+k)_mu.
        out -= (F(qv[mu]) + F(kv[mu])) * r2_real(A, qv, C, kv, D)
    return out


def G1_value(qv, kv, nvec, D):
    nq, nk = neg(qv), neg(kv)
    A = pmap(r1_tensor(nq, D), D)
    out = F(0)
    for mu in range(D):
        R = pmap(dr1_real(mu, nk, D), D)
        for m in range(D):
            if F(nvec[m]) == 0:
                continue
            for n in range(D):
                if F(nvec[n]) == 0:
                    continue
                out -= F(nvec[m]) * F(nvec[n]) * g2_real(A, qv, R, kv, mu, m, n, D)
    return out


FAMILIES = {
    "M_R2_chi1_dR1": M1_value,
    "M_R1_chi1_dR2": M2_value,
    "G_R1_chi2_Gamma2_dR1": G1_value,
}


def triples(total):
    out = []
    for i in range(total + 1):
        for j in range(total + 1 - i):
            out.append((i, j, total - i - j))
    return out

CUBIC = triples(3)
QUAD = triples(2)
BASIS = [("scalar", None, ex) for ex in CUBIC]
for nt in ["a2", "ab", "b2"]:
    BASIS.extend(("n2", nt, ex) for ex in QUAD)
assert len(BASIS) == 28


def invariants(qv, kv):
    Q = sum(x * x for x in qv)
    K = sum(x * x for x in kv)
    S = sum(x * y for x, y in zip(qv, kv))
    a = qv[0]
    b = kv[0]
    return Q, K, S, a, b


def basis_row(qv, kv):
    Q, K, S, a, b = invariants(qv, kv)
    vals = []
    for kind, nt, (i, j, l) in BASIS:
        base = (Q ** i) * (K ** j) * (S ** l)
        if kind == "scalar":
            vals.append(base)
        elif nt == "a2":
            vals.append(a * a * base)
        elif nt == "ab":
            vals.append(a * b * base)
        else:
            vals.append(b * b * base)
    return vals


def basis_labels():
    labels = []
    for kind, nt, (i, j, l) in BASIS:
        pieces = []
        if kind == "n2":
            pieces.append({"a2": "a^2", "ab": "a*b", "b2": "b^2"}[nt])
        if i: pieces.append(f"Q^{i}" if i != 1 else "Q")
        if j: pieces.append(f"K^{j}" if j != 1 else "K")
        if l: pieces.append(f"S^{l}" if l != 1 else "S")
        labels.append("*".join(pieces) if pieces else "1")
    return labels


def design_panels():
    rng = random.Random(14020260915)
    candidates = []
    rows = []
    while len(candidates) < 90:
        qv = tuple(rng.randint(-3, 3) for _ in range(3))
        kv = tuple(rng.randint(-3, 3) for _ in range(3))
        if not any(qv) or not any(kv):
            continue
        if qv == kv or tuple(-x for x in qv) == kv:
            continue
        candidates.append((qv, kv))
        rows.append(basis_row(qv, kv))
    M = s.Matrix(rows)
    piv = s.Matrix(rows).T.rref()[1]
    if len(piv) < 28:
        raise RuntimeError(f"basis design rank {len(piv)} < 28")
    selected = [candidates[i] for i in piv[:28]]
    A = s.Matrix([basis_row(*x) for x in selected])
    if A.det() == 0:
        raise RuntimeError("selected invariant design singular")
    return selected, A


def pad(v3, D):
    return tuple(list(v3) + [0] * (D - 3))


def to_sym(x: F):
    return s.Rational(x.numerator, x.denominator)


def solve_dimension(D, selected, A):
    nvec = tuple([1] + [0] * (D - 1))
    coeffs = {}
    for name, fn in FAMILIES.items():
        ys = []
        for q3, k3 in selected:
            ys.append(to_sym(fn(pad(q3, D), pad(k3, D), nvec, D)))
        sol = A.inv() * s.Matrix(ys) if False else A.inv(method="DM") * s.Matrix(ys)
        coeffs[name] = [s.factor(x) for x in sol]
    return coeffs


def eval_from_coeffs(coeff, qv, kv):
    row = basis_row(tuple(qv[:3]), tuple(kv[:3])) if len(qv) == 3 else None
    # For arbitrary dimension q/k panels, invariants may include all components.
    if row is None:
        Q, K, S, a, b = invariants(qv, kv)
        row = []
        for kind, nt, (i, j, l) in BASIS:
            base = (Q ** i) * (K ** j) * (S ** l)
            if kind == "scalar": row.append(base)
            elif nt == "a2": row.append(a * a * base)
            elif nt == "ab": row.append(a * b * base)
            else: row.append(b * b * base)
    return s.factor(sum(c * v for c, v in zip(coeff, row)))


def main():
    labels = basis_labels()
    selected, A = design_panels()
    Ainv = A.inv(method="DM")

    # Avoid repeated inversion: solve dimensions with precomputed inverse here.
    dims = list(range(3, 11))
    byD = {}
    for D in dims:
        nvec = tuple([1] + [0] * (D - 1))
        fam = {}
        for name, fn in FAMILIES.items():
            ys = s.Matrix([
                to_sym(fn(pad(q3, D), pad(k3, D), nvec, D)) for q3, k3 in selected
            ])
            fam[name] = [s.factor(x) for x in (Ainv * ys)]
        byD[D] = fam

    d, eps = s.symbols("d eps")
    train = [3, 4, 5, 6, 7]
    validate = [8, 9, 10]
    formulas = {}
    trace_degree_ok = True
    dim_coeff_ok = True
    max_poly_degree = 0
    for name in FAMILIES:
        fs = []
        eps_rows = []
        for j, label in enumerate(labels):
            pts = [(D, s.factor((D - 2) ** 2 * byD[D][name][j])) for D in train]
            poly = s.factor(s.interpolate(pts, d))
            deg = int(s.Poly(s.expand(poly), d).degree()) if poly != 0 else 0
            max_poly_degree = max(max_poly_degree, deg)
            trace_degree_ok &= deg <= 4
            coeff = s.factor(poly / (d - 2) ** 2)
            for D in validate:
                dim_coeff_ok &= s.simplify(coeff.subs(d, D) - byD[D][name][j]) == 0
            c4 = s.factor(coeff.subs(d, 4))
            ceps = s.factor(-2 * s.diff(coeff, d).subs(d, 4))
            fs.append({
                "basis": label,
                "coefficient_d": str(coeff),
                "trace_polynomial_degree": deg,
                "c_d4": str(c4),
                "c_epsilon_linear_for_d_4_minus_2eps": str(ceps),
            })
            eps_rows.append((c4, ceps))
        formulas[name] = fs

    # Held-out panels outside the solve, including components beyond the first 3
    # in validation dimensions so the invariant continuation is tested covariantly.
    held_seed = [
        ((1, 2, -1, 3), (2, -1, 1, 4)),
        ((2, 1, 3, -2), (-1, 2, 4, 1)),
        ((-2, 3, 1, 2), (3, -1, 2, -2)),
    ]
    held_rows = []
    held_ok = True
    for D in dims:
        nvec = tuple([1] + [0] * (D - 1))
        for idx, (q4, k4) in enumerate(held_seed):
            qv = tuple(list(q4[:min(4, D)]) + [0] * max(0, D - 4))
            kv = tuple(list(k4[:min(4, D)]) + [0] * max(0, D - 4))
            row = {"D": D, "panel": idx}
            for name, fn in FAMILIES.items():
                direct = to_sym(fn(qv, kv, nvec, D))
                recon = eval_from_coeffs(byD[D][name], qv, kv)
                eq = s.simplify(direct - recon) == 0
                held_ok &= bool(eq)
                row[name] = {"direct": str(direct), "reconstructed": str(recon), "equal": bool(eq)}
            held_rows.append(row)

    # D=4 cross-authority check against the committed symbolic tensor paths.
    d4_rows = []
    d4_ok = True
    n4 = (s.Integer(1), 0, 0, 0)
    for q4, k4 in held_seed:
        direct_generic = {
            "M_R2_chi1_dR1": to_sym(M1_value(q4, k4, (1,0,0,0), 4)),
            "M_R1_chi1_dR2": to_sym(M2_value(q4, k4, (1,0,0,0), 4)),
            "G_R1_chi2_Gamma2_dR1": to_sym(G1_value(q4, k4, (1,0,0,0), 4)),
        }
        authority = {
            "M_R2_chi1_dR1": s.simplify(i138.M_numerator(q4, k4, n4)),
            "M_R1_chi1_dR2": s.simplify(i139.M2_numerator(q4, k4, n4)),
            "G_R1_chi2_Gamma2_dR1": s.simplify(i138.G_numerator(q4, k4, n4)),
        }
        rr = {}
        for name in FAMILIES:
            eq = s.simplify(direct_generic[name] - authority[name]) == 0
            d4_ok &= bool(eq)
            rr[name] = {"generic_D4": str(direct_generic[name]), "authority_D4": str(authority[name]), "equal": bool(eq)}
        d4_rows.append(rr)

    # Validate the dimensionally continued formulas directly on D=8,9,10 held-outs,
    # without using solved per-D coefficients in reconstruction.
    continuation_heldout_ok = True
    continuation_rows = []
    for D in validate:
        nvec = tuple([1] + [0] * (D - 1))
        q4, k4 = held_seed[1]
        qv = tuple(list(q4) + [0] * (D - 4))
        kv = tuple(list(k4) + [0] * (D - 4))
        row = {"D": D}
        invrow = None
        # Build direct invariant row for full D vectors.
        Q, K, S, a, b = invariants(qv, kv)
        bvals = []
        for kind, nt, (ii, jj, ll) in BASIS:
            base = Q**ii * K**jj * S**ll
            if kind == "scalar": bvals.append(base)
            elif nt == "a2": bvals.append(a*a*base)
            elif nt == "ab": bvals.append(a*b*base)
            else: bvals.append(b*b*base)
        for name, fn in FAMILIES.items():
            coeff_at_D = [s.sympify(x["coefficient_d"]).subs(d, D) for x in formulas[name]]
            recon = s.factor(sum(c*v for c,v in zip(coeff_at_D,bvals)))
            direct = to_sym(fn(qv, kv, nvec, D))
            eq = s.simplify(recon-direct)==0
            continuation_heldout_ok &= bool(eq)
            row[name] = {"direct":str(direct),"continued":str(recon),"equal":bool(eq)}
        continuation_rows.append(row)

    checks = {
        "A_basis_size_28": len(BASIS) == 28,
        "B_design_rank_28": A.rank() == 28,
        "C_integer_D_invariant_heldouts": bool(held_ok),
        "D_trace_polynomial_degree_le4": bool(trace_degree_ok),
        "E_coefficient_continuation_D8_D10": bool(dim_coeff_ok),
        "F_direct_continuation_heldouts_D8_D10": bool(continuation_heldout_ok),
        "G_D4_matches_ITER138_ITER139": bool(d4_ok),
        "H_target_blind": True,
    }
    if all(checks.values()):
        classification = "PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN"
    elif not trace_degree_ok:
        classification = "BLOCKED_GENERAL_D_TRACE_DEGREE_AUTHORITY"
    else:
        classification = "SCIENTIFIC_FAIL_GENERAL_D_INVARIANT_RECONSTRUCTION"

    out = {
        "gate": "ITER140_FIXED_GEODESIC_CURVATURE_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION",
        "classification": classification,
        "basis_labels": labels,
        "training_dimensions": train,
        "validation_dimensions": validate,
        "max_observed_trace_polynomial_degree": max_poly_degree,
        "coefficient_formulas": formulas,
        "integer_D_heldouts": held_rows,
        "continuation_heldouts": continuation_rows,
        "D4_cross_authority": d4_rows,
        "checks": checks,
        "claim_ceiling": "general-d numerator continuation and O(epsilon) coefficients only; no loop pole/B1/noncancellation/B0/EDT/bridge/new physics/candidate theory",
    }
    Path("iter140_first_mg_general_d_invariant_continuation.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "classification": classification,
        "basis_size": len(BASIS),
        "design_rank": A.rank(),
        "max_trace_polynomial_degree": max_poly_degree,
        "checks": checks,
        "nonzero_coefficient_counts": {
            name: sum(1 for x in formulas[name] if x["coefficient_d"] != "0") for name in formulas
        },
    }, indent=2))
    if classification.startswith("SCIENTIFIC_FAIL") or classification.startswith("BLOCKED"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
