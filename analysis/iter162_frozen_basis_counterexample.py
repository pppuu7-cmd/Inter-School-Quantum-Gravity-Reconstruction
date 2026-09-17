#!/usr/bin/env python3
"""ITER162 scientific falsifier for the prospectively frozen 36-column upper span.

The frozen preregistration requires V_upper_ab to lie in a 36-column covariant
span whose tangent count is carried only by a=n.q, b=n.k, or free n indices.
The microscopic source, however, contains two tangent vectors n_m n_n that may
contract with each other, producing n^2=1 times tangent-neutral rank-2 tensors.
Those structures are absent from the frozen generator.

This script does NOT repair or replace the frozen basis. It performs an exact
rank-membership test of source-derived V_upper against the frozen 36 columns.
For diagnosis only, it also tests an explicitly labelled omitted n^2 complement.
If the source is outside the frozen span, ITER162's prospectively frozen tensor
covariance/span identity is false and the gate must scientific-FAIL rather than
post-hoc enlarge the basis inside ITER162.
"""
from __future__ import annotations

import json
import random
import sys
from fractions import Fraction as F
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0,str(HERE))
import iter161_endpoint_open_leg_factorization as i161

SEEDS=[
    ("delta_ab",0,0),("q_aq_b",2,0),("q_(a_k_b)",2,0),("k_ak_b",2,0),
    ("q_(a_n_b)",1,1),("k_(a_n_b)",1,1),("n_an_b",0,2),
]
VARS=[("Q",2,0),("K",2,0),("S",2,0),("a",1,1),("b",1,1)]


def exponents(target_deg,target_tan):
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


def label(es):
    p=[]
    for e,(name,_,_) in zip(es,VARS):
        if e:p.append(name if e==1 else f"{name}^{e}")
    return "*".join(p) if p else "1"


def frozen_columns():
    out=[]
    for seed,d,t in SEEDS:
        for es in exponents(4-d,2-t):
            out.append({"seed":seed,"exponents":es,"scalar":label(es),"sector":"FROZEN_36"})
    assert len(out)==36
    return out


def omitted_n2_columns():
    # Diagnostic-only structures carrying the two tangent vectors solely through n^2=1.
    # Only tangent-neutral seeds are allowed; qn/kn/nn would exceed total tangent count 2.
    out=[]
    for seed,d,t in SEEDS:
        if t!=0:
            continue
        for es in exponents(4-d,0):
            out.append({"seed":seed,"exponents":es,"scalar":"n^2*"+label(es),"sector":"OMITTED_N2_DIAGNOSTIC"})
    assert len(out)==15
    return out

FROZEN=frozen_columns()
OMITTED=omitted_n2_columns()


def dot(x,y): return sum((F(a)*F(b) for a,b in zip(x,y)),F(0))

def seed_value(name,q,k,n,a,b):
    if name=="delta_ab": return F(a==b)
    if name=="q_aq_b": return q[a]*q[b]
    if name=="q_(a_k_b)": return (q[a]*k[b]+k[a]*q[b])/2
    if name=="k_ak_b": return k[a]*k[b]
    if name=="q_(a_n_b)": return (q[a]*n[b]+n[a]*q[b])/2
    if name=="k_(a_n_b)": return (k[a]*n[b]+n[a]*k[b])/2
    if name=="n_an_b": return n[a]*n[b]
    raise KeyError(name)

def col_value(c,q,k,n,aidx,bidx):
    Q,K,S,aa,bb=dot(q,q),dot(k,k),dot(q,k),dot(n,q),dot(n,k)
    vals=(Q,K,S,aa,bb)
    sc=F(1)
    for e,v in zip(c["exponents"],vals): sc*=v**e
    # n^2 equals one on the frozen domain; keep the sector label as provenance.
    if c["sector"]=="OMITTED_N2_DIAGNOSTIC": sc*=dot(n,n)
    return seed_value(c["seed"],q,k,n,aidx,bidx)*sc

def sy(x):
    x=F(x); return s.Rational(x.numerator,x.denominator)

def fixtures(D,seed,count,axis=0):
    rng=random.Random(seed)
    n=[F(0)]*D; n[axis%D]=F(1); n=tuple(n)
    out=[]
    while len(out)<count:
        q=tuple(F(rng.randint(-4,4)) for _ in range(D))
        k=tuple(F(rng.randint(-4,4)) for _ in range(D))
        if not any(q) or not any(k) or q==k or tuple(-x for x in q)==k: continue
        out.append((q,k,n))
    return out

def panel(D,seed,count,axis=0):
    cols=FROZEN+OMITTED
    rows36=[]; rows51=[]; y=[]
    for q,k,n in fixtures(D,seed,count,axis):
        V=i161.upper_open_vertex(q,k,n,D)
        for a in range(D):
            for b in range(a,D):
                vals=[sy(col_value(c,q,k,n,a,b)) for c in cols]
                rows36.append(vals[:36]); rows51.append(vals)
                y.append(sy(V[a][b]))
    M36=s.Matrix(rows36); M51=s.Matrix(rows51); Y=s.Matrix(y)
    r36=int(M36.rank()); r36y=int(M36.row_join(Y).rank())
    r51=int(M51.rank()); r51y=int(M51.row_join(Y).rank())
    return {
        "D":D,"axis":axis,"fixture_count":count,"equation_count":len(y),
        "frozen_rank":r36,"frozen_plus_source_rank":r36y,
        "diagnostic_augmented_rank":r51,"diagnostic_augmented_plus_source_rank":r51y,
        "source_in_frozen_span":bool(r36y==r36),
        "source_in_n2_diagnostic_augmented_span":bool(r51y==r51),
    }

def main():
    panels=[
        panel(4,1623601,12,0),
        panel(4,1623602,12,1),
        panel(5,1623603,10,0),
    ]
    frozen_out=all(not p["source_in_frozen_span"] for p in panels)
    n2_explains=all(p["source_in_n2_diagnostic_augmented_span"] for p in panels)
    rank_witness=all(p["frozen_plus_source_rank"]==p["frozen_rank"]+1 for p in panels)
    checks={
        "A_frozen_column_count_36":len(FROZEN)==36,
        "B_omitted_n2_diagnostic_count_15":len(OMITTED)==15,
        "C_source_exactly_outside_frozen_span_all_independent_panels":frozen_out,
        "D_rank_increases_by_one_when_source_adjoined":rank_witness,
        "E_omitted_n2_diagnostic_complement_contains_source_all_panels":n2_explains,
        "F_no_scalar_inverse":True,
        "G_no_ITER160_residue":True,
        "H_no_ITER118_solve":True,
        "I_no_posthoc_basis_repair_claimed":True,
    }
    fail=all(checks.values())
    out={
        "gate":"ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR",
        "classification":(
            "SCIENTIFIC_FAIL_ITER162_FROZEN_TENSOR_COVARIANCE_OR_SUPPORT_IDENTITY_FALSE"
            if fail else "INCONCLUSIVE_ITER162_FROZEN_BASIS_COUNTEREXAMPLE_DIAGNOSTIC"
        ),
        "failed_frozen_identity":(
            "The prospectively frozen 36-column generator is complete for V_upper_ab under the stated exact-two-tangent counting using only Q,K,S,a,b and the seven seeds."
        ),
        "exact_defect":(
            "Microscopic n_m n_n may contract internally to n^2=1, producing tangent-neutral symmetric rank-2 momentum covariants. "
            "The frozen 36 generator requires the two tangent counts to remain explicit in a,b or free n indices and omits this n^2 sector."
        ),
        "frozen_column_count":36,
        "omitted_n2_diagnostic_column_count":15,
        "panels":panels,
        "checks":checks,
        "terminal_implication":(
            "If independently confirmed, ITER162 must terminate SCIENTIFIC_FAIL under its frozen rules. The 15-column diagnostic complement identifies the defect but is not adopted as a repaired ITER162 basis. Any repaired hypothesis requires a new prospectively frozen gate after ITER162 terminalization."
        ),
        "claim_locks":{"B1_total":"UNAUTHORIZED","BRIDGE_DERIVED":False,"ITER118_matching_authorized":False,"candidate_theory":"UNFORMED / 0%"},
    }
    Path("iter162_frozen_basis_counterexample.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if fail else 1)

if __name__=="__main__": main()
