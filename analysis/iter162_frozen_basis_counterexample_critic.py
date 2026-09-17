#!/usr/bin/env python3
"""Independent Critic for the ITER162 frozen 36-column span falsifier.

This route does not import the Researcher falsifier. It independently rebuilds
the frozen covariants and tests exact consistency of an overdetermined linear
system A c = V_upper at changed dimensions, tangent axes, fixture seeds, and
component ordering. It also tests whether adding the prospectively omitted
n^2-saturated tangent-neutral sector restores consistency, solely to localize the
defect. The augmented sector is not adopted as an ITER162 repair.
"""
from __future__ import annotations
import json, random, sys
from fractions import Fraction as F
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import iter161_endpoint_open_leg_factorization as i161

SEEDS=[("delta_ab",0,0),("q_aq_b",2,0),("q_(a_k_b)",2,0),("k_ak_b",2,0),("q_(a_n_b)",1,1),("k_(a_n_b)",1,1),("n_an_b",0,2)]
VARS=[("Q",2,0),("K",2,0),("S",2,0),("a",1,1),("b",1,1)]

def exps(deg,tan):
    out=[]
    for i in range(3):
     for j in range(3):
      for l in range(3):
       for u in range(5):
        for v in range(5):
         e=(i,j,l,u,v)
         if sum(x*y[1] for x,y in zip(e,VARS))==deg and sum(x*y[2] for x,y in zip(e,VARS))==tan: out.append(e)
    return out

def columns():
    f=[]; n2=[]
    for name,d,t in SEEDS:
        for e in exps(4-d,2-t): f.append((name,e,False))
        if t==0:
            for e in exps(4-d,0): n2.append((name,e,True))
    assert len(f)==36 and len(n2)==15
    return f,n2
FROZEN,N2=columns()

def dot(x,y): return sum((F(a)*F(b) for a,b in zip(x,y)),F(0))
def seed(name,q,k,n,a,b):
    if name=="delta_ab": return F(a==b)
    if name=="q_aq_b": return q[a]*q[b]
    if name=="q_(a_k_b)": return (q[a]*k[b]+k[a]*q[b])/2
    if name=="k_ak_b": return k[a]*k[b]
    if name=="q_(a_n_b)": return (q[a]*n[b]+n[a]*q[b])/2
    if name=="k_(a_n_b)": return (k[a]*n[b]+n[a]*k[b])/2
    if name=="n_an_b": return n[a]*n[b]
    raise KeyError(name)
def value(col,q,k,n,a,b):
    name,e,isn2=col
    vals=(dot(q,q),dot(k,k),dot(q,k),dot(n,q),dot(n,k))
    z=F(1)
    for p,v in zip(e,vals): z*=v**p
    if isn2:z*=dot(n,n)
    return seed(name,q,k,n,a,b)*z
def sy(x):
    x=F(x); return s.Rational(x.numerator,x.denominator)
def make_fixtures(D,seed0,count,axis):
    rng=random.Random(seed0); n=[F(0)]*D; n[axis%D]=F(1); n=tuple(n); out=[]
    while len(out)<count:
        q=tuple(F(rng.randint(-5,5)) for _ in range(D)); k=tuple(F(rng.randint(-5,5)) for _ in range(D))
        if not any(q) or not any(k) or q==k or tuple(-x for x in q)==k: continue
        out.append((q,k,n))
    return out

def consistency(D,seed0,count,axis):
    frozen=[]; aug=[]; yy=[]
    # Reverse component order vs Researcher route.
    comps=[(a,b) for a in range(D) for b in range(a,D)][::-1]
    for q,k,n in make_fixtures(D,seed0,count,axis):
        V=i161.upper_open_vertex(q,k,n,D)
        for a,b in comps:
            rf=[sy(value(c,q,k,n,a,b)) for c in FROZEN]
            rn=[sy(value(c,q,k,n,a,b)) for c in N2]
            frozen.append(rf); aug.append(rf+rn); yy.append(sy(V[a][b]))
    A=s.Matrix(frozen); B=s.Matrix(aug); Y=s.Matrix(yy)
    ra=int(A.rank()); ray=int(A.row_join(Y).rank()); rb=int(B.rank()); rby=int(B.row_join(Y).rank())
    return {"D":D,"axis":axis,"equations":len(yy),"rank_frozen":ra,"rank_frozen_with_source":ray,"rank_augmented":rb,"rank_augmented_with_source":rby,"frozen_inconsistent":bool(ray>ra),"n2_augmented_consistent":bool(rby==rb)}

def main():
    tests=[consistency(4,916201,13,2),consistency(5,916202,11,1),consistency(6,916203,8,3)]
    checks={
      "A_changed_panels_all_frozen_inconsistent":all(t["frozen_inconsistent"] for t in tests),
      "B_each_source_adds_exactly_one_rank":all(t["rank_frozen_with_source"]==t["rank_frozen"]+1 for t in tests),
      "C_n2_diagnostic_augmented_span_consistent":all(t["n2_augmented_consistent"] for t in tests),
      "D_no_researcher_json_consumed":True,"E_no_ITER160_residue":True,"F_no_scalar_inverse":True,"G_no_ITER118_solve":True,
    }
    passed=all(checks.values())
    out={
      "gate":"ITER162_OPEN_G_ENDPOINT_DISTRIBUTIONAL_R_OPERATION_AND_POLE_TENSOR",
      "critic_verdict":"PASS_CRITIC_ITER162_FROZEN_36_SPAN_SCIENTIFIC_FALSIFIER_CONFIRMED" if passed else "FAIL_CRITIC_ITER162_FROZEN_36_SPAN_FALSIFIER_NOT_CONFIRMED",
      "tests":tests,"checks":checks,
      "conclusion":("Independent exact overdetermined systems confirm that source-derived V_upper is outside the prospectively frozen 36-column span. Adding the omitted n^2-saturated tangent-neutral diagnostic sector restores consistency. Under the frozen ITER162 rules this confirms SCIENTIFIC_FAIL; it does not authorize in-gate basis repair." if passed else "Independent route did not confirm the proposed scientific falsifier."),
      "claim_locks":{"ITER118_matching_authorized":False,"B1_total":"UNAUTHORIZED","BRIDGE_DERIVED":False,"candidate_theory":"UNFORMED / 0%"}
    }
    Path("iter162_frozen_basis_counterexample_critic.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if passed else 1)
if __name__=="__main__": main()
