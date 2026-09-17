#!/usr/bin/env python3
"""ITER162: exact structural K-divisibility kernel of the frozen upper tensor span.

This operation is outcome-blind with respect to the source coefficients. It asks:
which linear combinations of the prospectively frozen 36 symmetric covariants are
exactly divisible by K=k^2 as tensor polynomials before external-source contraction?

Method: fix the frozen unit-tangent domain n=e0 by covariance, represent every
symmetric tensor component as an exact polynomial in generic q,k components, and
compute its normal form modulo the principal ideal <K>. The stacked normal-form
coefficient matrix defines the quotient map. Its exact nullspace is the full
K-divisible subspace on that dimension. D=4 and D=5 are evaluated independently;
agreement is required to reject dimension-specific accidental identities.

No source coefficient, ITER160 residue, scalar 28-invariant inverse, ITER118 solve,
or contact-zero convention is used.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as s

SEEDS = [
    ("delta_ab", 0, 0),
    ("q_aq_b", 2, 0),
    ("q_(a_k_b)", 2, 0),
    ("k_ak_b", 2, 0),
    ("q_(a_n_b)", 1, 1),
    ("k_(a_n_b)", 1, 1),
    ("n_an_b", 0, 2),
]
VARS = [("Q",2,0),("K",2,0),("S",2,0),("a",1,1),("b",1,1)]


def exponent_solutions(target_deg, target_tan):
    out=[]
    for eQ in range(3):
      for eK in range(3):
       for eS in range(3):
        for ea in range(5):
         for eb in range(5):
          es=(eQ,eK,eS,ea,eb)
          if sum(e*v[1] for e,v in zip(es,VARS))==target_deg and sum(e*v[2] for e,v in zip(es,VARS))==target_tan:
              out.append(es)
    return out


def scalar_label(es):
    parts=[]
    for e,(name,_,_) in zip(es,VARS):
        if e:
            parts.append(name if e==1 else f"{name}^{e}")
    return "*".join(parts) if parts else "1"


def frozen_columns():
    cols=[]
    for seed,d,t in SEEDS:
        for es in exponent_solutions(4-d,2-t):
            cols.append({
                "seed":seed,
                "exponents":es,
                "scalar":scalar_label(es),
                "explicit_K_factor": bool(es[1] > 0),
            })
    assert len(cols)==36
    assert sum(c["explicit_K_factor"] for c in cols)==10
    return cols

COLS=frozen_columns()


def seed_expr(name,q,k,n,a,b):
    if name=="delta_ab": return s.Integer(a==b)
    if name=="q_aq_b": return q[a]*q[b]
    if name=="q_(a_k_b)": return (q[a]*k[b]+k[a]*q[b])/2
    if name=="k_ak_b": return k[a]*k[b]
    if name=="q_(a_n_b)": return (q[a]*n[b]+n[a]*q[b])/2
    if name=="k_(a_n_b)": return (k[a]*n[b]+n[a]*k[b])/2
    if name=="n_an_b": return n[a]*n[b]
    raise KeyError(name)


def column_expr(col,q,k,n,aidx,bidx):
    Q=sum(x*x for x in q)
    K=sum(x*x for x in k)
    S=sum(x*y for x,y in zip(q,k))
    aa=sum(x*y for x,y in zip(n,q))
    bb=sum(x*y for x,y in zip(n,k))
    vals=(Q,K,S,aa,bb)
    sc=s.Integer(1)
    for e,v in zip(col["exponents"],vals):
        sc *= v**e
    return s.expand(seed_expr(col["seed"],q,k,n,aidx,bidx)*sc)


def reduce_mod_K(poly, q, k):
    """Exact normal form modulo K using k0^2 = -sum_{i>0} ki^2.

    All frozen covariants have k-degree <=4. Repeated exact replacement yields the
    unique remainder of degree <2 in k0 for lex order with k0 leading.
    """
    rest = sum(x*x for x in k[1:])
    p=s.Poly(s.expand(poly), k[0], domain="EX")
    out=s.Integer(0)
    for (power,), coeff in p.terms():
        m=power//2
        r=power%2
        out += coeff * ((-rest)**m) * (k[0]**r)
    return s.expand(out)


def quotient_matrix(D):
    q=s.symbols("q0:"+str(D))
    k=s.symbols("k0:"+str(D))
    n=(s.Integer(1),)+tuple(s.Integer(0) for _ in range(D-1))
    all_vars=q+k

    # key -> 36 coefficient row, where key includes tensor component and monomial.
    coeff_rows={}
    for j,col in enumerate(COLS):
        for a in range(D):
            for b in range(a,D):
                rem=reduce_mod_K(column_expr(col,q,k,n,a,b), q, k)
                P=s.Poly(rem,*all_vars,domain=s.QQ)
                for mon, coeff in P.terms():
                    key=(a,b,mon)
                    if key not in coeff_rows:
                        coeff_rows[key]=[s.Rational(0) for _ in COLS]
                    coeff_rows[key][j]=s.Rational(coeff)

    M=s.Matrix(list(coeff_rows.values()))
    rank=int(M.rank())
    null=M.nullspace()
    null_dim=len(null)

    explicit=[i for i,c in enumerate(COLS) if c["explicit_K_factor"]]
    nonexplicit=[i for i,c in enumerate(COLS) if not c["explicit_K_factor"]]
    # Explicit-K columns must map exactly to zero.
    explicit_zero=all(all(M[r,j]==0 for r in range(M.rows)) for j in explicit)
    # If the quotient images of all 26 nonexplicit columns are independent,
    # then the complete K-divisible kernel is exactly the 10 explicit-K columns.
    nonexp_rank=int(M[:,nonexplicit].rank())
    kernel_exactly_explicit = explicit_zero and nonexp_rank==len(nonexplicit) and null_dim==len(explicit)

    return {
        "D":D,
        "quotient_constraint_rows":int(M.rows),
        "quotient_map_rank":rank,
        "kernel_dimension":null_dim,
        "explicit_K_column_count":len(explicit),
        "nonexplicit_column_count":len(nonexplicit),
        "nonexplicit_quotient_rank":nonexp_rank,
        "all_explicit_K_columns_reduce_to_zero":bool(explicit_zero),
        "kernel_exactly_explicit_K_span":bool(kernel_exactly_explicit),
        "nullspace_basis": [[str(x) for x in v] for v in null],
    }


def main():
    rows=[quotient_matrix(4), quotient_matrix(5)]
    agree=(rows[0]["kernel_dimension"]==rows[1]["kernel_dimension"] and rows[0]["quotient_map_rank"]==rows[1]["quotient_map_rank"])
    exact=agree and all(r["kernel_exactly_explicit_K_span"] for r in rows)

    checks={
        "A_frozen_36_columns": len(COLS)==36,
        "B_frozen_explicit_K_count_10": sum(c["explicit_K_factor"] for c in COLS)==10,
        "C_D4_D5_quotient_rank_agree": agree,
        "D_complete_K_kernel_equals_explicit_K_span": exact,
        "E_no_source_coefficients_consumed": True,
        "F_no_ITER160_residue_consumed": True,
        "G_no_scalar28_inverse": True,
        "H_no_ITER118_solve": True,
        "I_contacts_not_set_zero": True,
    }
    out={
        "gate":"ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR",
        "classification": (
            "PASS_STRUCTURAL_ITER162_COMPLETE_FROZEN_SPAN_TENSOR_K_DIVISIBILITY_KERNEL"
            if all(checks.values()) else
            "SCIENTIFIC_FAIL_ITER162_FROZEN_TENSOR_K_DIVISIBILITY_STRUCTURE"
        ),
        "method":"exact polynomial normal forms modulo principal ideal <K>, n=e0 with n^2=1, independent D=4 and D=5",
        "dimension_results":rows,
        "checks":checks,
        "interpretation": (
            "If PASS, there are no hidden K-divisible linear combinations among the 26 no-explicit-K covariants: "
            "the full K-divisible subspace of the frozen 36-column tensor span is exactly the 10-column explicit-K span. "
            "This is structural support algebra only; source coefficients and the distributional Laurent extension remain separate operations."
        ),
        "terminal_science":False,
        "locks":{
            "ITER160_minus525_consumed":False,
            "source_coefficients_consumed":False,
            "inverse_28_scalar_map":False,
            "ITER118_coefficient_solve":False,
            "contacts_set_zero":False,
            "B1_total":"UNAUTHORIZED",
            "BRIDGE_DERIVED":False,
            "candidate_theory":"UNFORMED / 0%",
        },
    }
    Path("iter162_tensor_K_divisibility_span.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in out.items() if k!="dimension_results"},indent=2,sort_keys=True))
    for r in rows:
        print(json.dumps({k:v for k,v in r.items() if k!="nullspace_basis"},sort_keys=True))
    raise SystemExit(0 if all(checks.values()) else 1)

if __name__=="__main__":
    main()
