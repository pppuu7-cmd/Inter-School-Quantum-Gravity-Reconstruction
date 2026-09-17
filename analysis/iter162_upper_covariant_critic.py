#!/usr/bin/env python3
"""Independent Critic for the ITER162 upper covariant reconstruction sub-result.

The Critic does not reuse the Researcher design matrix, fixture generator, or
linear solve. It independently solves the same 36 coefficient system in an n=e1
unit-tangent frame with changed q/k fixtures, compares every exact coefficient
against the producer formula at D=4,6,8,9,10, and then tests the producer formula
on rotated rational unit tangents not used by either solve.

The K-divisibility theorem is certified by a separate exact quotient job and is
not re-derived here. No ITER160 normalization, scalar inverse, contact-zero
shortcut, or ITER118 solve is allowed.
"""
from __future__ import annotations

import json
import random
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import iter161_endpoint_open_leg_factorization as i161

RESULT = Path("iter162_upper_covariant_reconstruction.json")


def dot(x, y):
    return sum((F(a) * F(b) for a, b in zip(x, y)), F(0))


def axis_tangent(D, axis=1):
    n = [F(0) for _ in range(D)]
    n[axis % D] = F(1)
    return tuple(n)


def rotated_tangent(D, case):
    triples = [(20, 21, 29), (9, 40, 41), (12, 35, 37)]
    aa, bb, cc = triples[case % len(triples)]
    n = [F(0) for _ in range(D)]
    p = (case + 1) % D
    q = (case + 3) % D
    if q == p:
        q = (p + 1) % D
    n[p] = F(aa, cc)
    n[q] = F(bb, cc)
    assert dot(n, n) == 1
    return tuple(n)


def invs(q, k, n):
    return {"Q": dot(q,q), "K": dot(k,k), "S": dot(q,k), "a": dot(n,q), "b": dot(n,k)}


def scalar_from_label(label, q, k, n):
    if label == "1":
        return F(1)
    vals = invs(q,k,n)
    out = F(1)
    for piece in label.split("*"):
        if "^" in piece:
            name,power = piece.split("^")
            out *= vals[name] ** int(power)
        else:
            out *= vals[piece]
    return out


def seed(seed_name,q,k,n,a,b):
    if seed_name == "delta_ab": return F(a == b)
    if seed_name == "q_aq_b": return F(q[a])*F(q[b])
    if seed_name == "q_(a_k_b)": return (F(q[a])*F(k[b])+F(k[a])*F(q[b]))/2
    if seed_name == "k_ak_b": return F(k[a])*F(k[b])
    if seed_name == "q_(a_n_b)": return (F(q[a])*F(n[b])+F(n[a])*F(q[b]))/2
    if seed_name == "k_(a_n_b)": return (F(k[a])*F(n[b])+F(n[a])*F(k[b]))/2
    if seed_name == "n_an_b": return F(n[a])*F(n[b])
    raise KeyError(seed_name)


def as_sym(x):
    x=F(x)
    return s.Rational(x.numerator,x.denominator)


def basis_row(rows,q,k,n,a,b):
    return [as_sym(seed(r["seed"],q,k,n,a,b)*scalar_from_label(r["scalar"],q,k,n)) for r in rows]


def reconstruct_component(rows,D,q,k,n,a,b):
    d=s.symbols("d")
    return s.factor(sum(
        s.sympify(r["coefficient_d"]).subs(d,D) * basis_row([r],q,k,n,a,b)[0]
        for r in rows
    ))


def critic_design(rows):
    rng=random.Random(162991731)
    fixtures=[]
    n=axis_tangent(4,1)
    while len(fixtures)<8:
        q=tuple(F(rng.randint(-4,4)) for _ in range(4))
        k=tuple(F(rng.randint(-4,4)) for _ in range(4))
        if not any(q) or not any(k) or q==k or tuple(-x for x in q)==k:
            continue
        fixtures.append((q,k,n))
    matrix_rows=[]
    keys=[]
    for fi,(q,k,n) in enumerate(fixtures):
        for a in range(4):
            for b in range(a,4):
                matrix_rows.append(basis_row(rows,q,k,n,a,b))
                keys.append((fi,a,b))
    M=s.Matrix(matrix_rows)
    piv=M.T.rref()[1]
    if len(piv)!=36:
        raise RuntimeError(f"Critic design rank {len(piv)} != 36")
    sel=list(piv[:36])
    A=s.Matrix([matrix_rows[i] for i in sel])
    if A.rank()!=36:
        raise RuntimeError("Critic selected design singular")
    return fixtures,keys,sel,A


def pad4(v,D):
    return tuple(v)+(F(0),)*(D-4)


def independent_solve_D(rows,D,fixtures,keys,sel,Ainv):
    needed=sorted(set(keys[i][0] for i in sel))
    vertices={}
    for fi in needed:
        q4,k4,n4=fixtures[fi]
        vertices[fi]=i161.upper_open_vertex(pad4(q4,D),pad4(k4,D),pad4(n4,D),D)
    y=[]
    for idx in sel:
        fi,a,b=keys[idx]
        y.append(as_sym(vertices[fi][a][b]))
    return [s.factor(x) for x in (Ainv*s.Matrix(y))]


def rotated_fixture(D,case):
    q=tuple(F(((i+2)*(case+3))%7-3) for i in range(D))
    k=tuple(F(((i+5)*(case+4))%9-4) for i in range(D))
    if not any(q): q=(F(1),)+q[1:]
    if not any(k): k=(F(2),)+k[1:]
    return q,k,rotated_tangent(D,case)


def main():
    if not RESULT.exists():
        raise RuntimeError("producer JSON missing")
    data=json.loads(RESULT.read_text(encoding="utf-8"))
    rows=data["coefficients"]
    d=s.symbols("d")

    checks={}
    checks["A_manifest_has_36_frozen_covariants"] = len(rows)==36
    checks["B_producer_scoped_nonterminal"] = data.get("terminal_science") is False
    checks["C_no_ITER160_normalization"] = data["locks"].get("ITER160_minus525_consumed") is False
    checks["D_no_scalar28_inverse"] = data["locks"].get("inverse_28_scalar_map") is False
    checks["E_no_ITER118_solve"] = data["locks"].get("ITER118_coefficient_solve") is False
    checks["F_no_contacts_zero"] = data["locks"].get("contacts_set_zero") is False

    fixtures,keys,sel,A=critic_design(rows)
    Ainv=A.inv(method="DM")
    solve_rows=[]
    coeff_agree=True
    for D in [4,6,8,9,10]:
        independent=independent_solve_D(rows,D,fixtures,keys,sel,Ainv)
        producer=[s.factor(s.sympify(r["coefficient_d"]).subs(d,D)) for r in rows]
        equal=[s.simplify(a-b)==0 for a,b in zip(independent,producer)]
        ok=all(bool(x) for x in equal)
        coeff_agree &= ok
        solve_rows.append({"D":D,"all_36_coefficients_exactly_equal":bool(ok),"mismatch_count":sum(not bool(x) for x in equal)})
    checks["G_independent_axis_e1_coefficient_solve_matches_producer"] = coeff_agree

    held=[]
    rotated_ok=True
    for D,case in [(4,401),(8,803),(10,1007)]:
        q,k,n=rotated_fixture(D,case)
        direct=i161.upper_open_vertex(q,k,n,D)
        ok=True
        for a in range(D):
            for b in range(a,D):
                rec=reconstruct_component(rows,D,q,k,n,a,b)
                if s.simplify(rec-as_sym(direct[a][b]))!=0:
                    ok=False
                    break
            if not ok:
                break
        rotated_ok &= ok
        held.append({"D":D,"case":case,"n_squared":str(dot(n,n)),"all_symmetric_components_exact":bool(ok)})
    checks["H_rotated_rational_unit_tangent_covariance_heldouts_exact"] = rotated_ok
    checks["I_critic_design_rank_36"] = A.rank()==36

    passed=all(bool(v) for v in checks.values())
    out={
        "gate":"ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR",
        "critic_verdict": (
            "PASS_CRITIC_ITER162_INDEPENDENT_UPPER_COVARIANT_RECONSTRUCTION_SOUND"
            if passed else
            "FAIL_CRITIC_ITER162_UPPER_COVARIANT_RECONSTRUCTION"
        ),
        "checks":checks,
        "independent_coefficient_solves":solve_rows,
        "rotated_covariance_heldout":held,
        "scope":(
            "independent source-derived V_upper coefficient reconstruction and covariance held-outs only; "
            "K-divisibility is separately certified; Laurent extension, A_local quotient, ITER118 coefficients, "
            "B1_total, bridge and candidate theory remain unauthorized"
        ),
        "next_required_operation":(
            "consume the exact K-divisibility certificate and construct the unseparated open-tensor distributional "
            "Laurent/R-operation, complete local ambiguity span, and exact quotient P_open/A_local"
        ),
    }
    Path("iter162_upper_covariant_critic.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__=="__main__":
    main()
