#!/usr/bin/env python3
"""ITER163 Researcher: exact complete two-tangent covariant reconstruction.

Prospectively frozen by ITER163 before source coefficients:
seven symmetric seeds times scalar monomials in Q,K,S,a,b,N=n^2, with total
momentum degree four and total tangent count two. The mechanical raw count must
be 51 = 36 explicit-tangent + 15 N-saturated tangent-neutral columns.

The physical fixture domain has N=n^2=1. Candidate rank is computed before
source values. Source coefficients come only from ITER161 upper_open_vertex.
No ITER160 residue, scalar 28-map inverse, contact-zero convention, or ITER118
solve is consumed.
"""
from __future__ import annotations
import json, random, sys
from fractions import Fraction as F
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path: sys.path.insert(0,str(HERE))
import iter161_endpoint_open_leg_factorization as i161

SEEDS=[
 ("delta_ab",0,0),("q_aq_b",2,0),("q_(a_k_b)",2,0),("k_ak_b",2,0),
 ("q_(a_n_b)",1,1),("k_(a_n_b)",1,1),("n_an_b",0,2),
]
VARS=[("Q",2,0),("K",2,0),("S",2,0),("a",1,1),("b",1,1),("N",0,2)]


def exponent_solutions(target_deg,target_tan):
    out=[]
    for eQ in range(3):
     for eK in range(3):
      for eS in range(3):
       for ea in range(5):
        for eb in range(5):
         for eN in range(2):
          es=(eQ,eK,eS,ea,eb,eN)
          if sum(e*v[1] for e,v in zip(es,VARS))==target_deg and sum(e*v[2] for e,v in zip(es,VARS))==target_tan:
              out.append(es)
    return out

def monomial_label(es):
    parts=[]
    for e,(name,_,_) in zip(es,VARS):
        if e: parts.append(name if e==1 else f"{name}^{e}")
    return "*".join(parts) if parts else "1"

def columns():
    out=[]
    for seed,d,t in SEEDS:
        for es in exponent_solutions(4-d,2-t):
            out.append({"seed":seed,"exponents":es,"scalar":monomial_label(es),"N_saturated":bool(es[5]),"explicit_K_factor":bool(es[1])})
    assert len(out)==51, len(out)
    assert sum(c["N_saturated"] for c in out)==15
    assert sum(c["explicit_K_factor"] for c in out)==16
    return out
COLS=columns()

def dot(x,y): return sum((F(a)*F(b) for a,b in zip(x,y)),F(0))
def axis_tangent(D,axis=0):
    n=[F(0)]*D; n[axis%D]=F(1); return tuple(n)
def scalar_value(es,q,k,n):
    vals=(dot(q,q),dot(k,k),dot(q,k),dot(n,q),dot(n,k),dot(n,n))
    z=F(1)
    for e,v in zip(es,vals): z*=v**e
    return z
def seed_value(name,q,k,n,a,b):
    if name=="delta_ab": return F(a==b)
    if name=="q_aq_b": return q[a]*q[b]
    if name=="q_(a_k_b)": return (q[a]*k[b]+k[a]*q[b])/2
    if name=="k_ak_b": return k[a]*k[b]
    if name=="q_(a_n_b)": return (q[a]*n[b]+n[a]*q[b])/2
    if name=="k_(a_n_b)": return (k[a]*n[b]+n[a]*k[b])/2
    if name=="n_an_b": return n[a]*n[b]
    raise KeyError(name)
def basis_row(q,k,n,a,b):
    assert dot(n,n)==1
    return [seed_value(c["seed"],q,k,n,a,b)*scalar_value(c["exponents"],q,k,n) for c in COLS]
def sy(x):
    x=F(x); return s.Rational(x.numerator,x.denominator)
def fixtures(D,seed,count,axis=0,span=4):
    rng=random.Random(seed); n=axis_tangent(D,axis); out=[]
    while len(out)<count:
        q=tuple(F(rng.randint(-span,span)) for _ in range(D)); k=tuple(F(rng.randint(-span,span)) for _ in range(D))
        if not any(q) or not any(k) or q==k or tuple(-x for x in q)==k: continue
        out.append((q,k,n))
    return out

def design_4d():
    fs=fixtures(4,16320260917,20,axis=0)
    rows=[]; keys=[]
    for fi,(q,k,n) in enumerate(fs):
        for a in range(4):
            for b in range(a,4):
                rows.append([sy(x) for x in basis_row(q,k,n,a,b)]); keys.append((fi,a,b))
    M=s.Matrix(rows); rank=int(M.rank()); piv=M.T.rref()[1]
    if rank!=51 or len(piv)<51: raise RuntimeError(f"ITER163 candidate rank {rank} != 51")
    sel=list(piv[:51]); A=s.Matrix([rows[i] for i in sel])
    assert A.rank()==51
    return fs,keys,sel,A

def pad4(v,D): return tuple(v)+(F(0),)*(D-4)
def solve_D(D,fs,keys,sel,Ainv):
    needed=sorted(set(keys[i][0] for i in sel)); V={}
    for fi in needed:
        q,k,n=fs[fi]; V[fi]=i161.upper_open_vertex(pad4(q,D),pad4(k,D),pad4(n,D),D)
    y=[]
    for i in sel:
        fi,a,b=keys[i]; y.append(sy(V[fi][a][b]))
    return [s.factor(x) for x in Ainv*s.Matrix(y)]
def eval_component(coeffs,q,k,n,a,b):
    return s.factor(sum(c*sy(v) for c,v in zip(coeffs,basis_row(q,k,n,a,b))))
def verify_changed(D,coeffs,seed,count=2):
    out=[]; okall=True
    for case,(q,k,n) in enumerate(fixtures(D,seed,count,axis=0,span=5)):
        V=i161.upper_open_vertex(q,k,n,D); ok=True
        for a in range(D):
            for b in range(a,D):
                if s.simplify(eval_component(coeffs,q,k,n,a,b)-sy(V[a][b]))!=0: ok=False; break
            if not ok: break
        okall &= ok; out.append({"D":D,"case":case,"exact":bool(ok)})
    return bool(okall),out

def direct_iter162_regression(coeffs_D4):
    q=tuple(F(x) for x in (0,1,2,0)); k=tuple(F(x) for x in (0,2,-1,1)); n=(F(1),F(0),F(0),F(0))
    V=i161.upper_open_vertex(q,k,n,4); rows=[]; ok=True
    for a in range(1,4):
        for b in range(a,4):
            rec=eval_component(coeffs_D4,q,k,n,a,b); eq=s.simplify(rec-sy(V[a][b]))==0; ok &= bool(eq)
            rows.append({"component":[a,b],"source":str(V[a][b]),"reconstructed":str(rec),"exact":bool(eq)})
    return bool(ok),rows

def main():
    fs,keys,sel,A=design_4d(); Ainv=A.inv(method="DM")
    train=[4,5,6,7,8]; validate=[9,10]; dims=train+validate
    byD={D:solve_D(D,fs,keys,sel,Ainv) for D in dims}
    over=[]; over_ok=True
    for D in dims:
        ok,rows=verify_changed(D,byD[D],16381000000+D,2); over_ok &= ok; over.extend(rows)
    d=s.symbols("d"); formulas=[]; interp_ok=True; maxdeg=0
    for j,c in enumerate(COLS):
        pts=[(D,s.factor((D-2)*byD[D][j])) for D in train]
        poly=s.factor(s.interpolate(pts,d)); deg=int(s.Poly(s.expand(poly),d).degree()) if poly!=0 else 0; maxdeg=max(maxdeg,deg)
        coeff=s.factor(poly/(d-2)); valid=all(s.simplify(coeff.subs(d,D)-byD[D][j])==0 for D in validate)
        interp_ok &= bool(valid and deg<=4)
        formulas.append({"seed":c["seed"],"scalar":c["scalar"],"N_saturated":c["N_saturated"],"explicit_K_factor":c["explicit_K_factor"],"coefficient_d":str(coeff),"scaled_polynomial_degree":deg,"heldout_D9_D10_equal":bool(valid)})
    regression_ok,regression=direct_iter162_regression(byD[4])
    nonzero=[r for r in formulas if s.sympify(r["coefficient_d"])!=0]
    checks={
      "A_raw_candidate_count_51":len(COLS)==51,"B_N_saturated_count_15":sum(c["N_saturated"] for c in COLS)==15,
      "C_explicit_K_count_16":sum(c["explicit_K_factor"] for c in COLS)==16,"D_candidate_exact_rank_51_before_source":A.rank()==51,
      "E_changed_qk_heldouts_D4_to_D10_exact":over_ok,"F_D_interpolation_and_D9_D10_holdouts_exact":interp_ok and maxdeg<=4,
      "G_ITER162_direct_counterexample_regression_reconstructed":regression_ok,"H_unit_tangent_domain":all(dot(n,n)==1 for _,_,n in fs),
      "I_ITER160_minus525_not_consumed":True,"J_no_scalar28_inverse":True,"K_contacts_not_set_zero":True,"L_no_ITER118_solve":True,
    }
    passed=all(checks.values())
    out={"gate":"ITER163_OPEN_G_COMPLETE_TWO_TANGENT_COVARIANT_CLOSURE","classification":"PARTIAL_PASS_ITER163_RESEARCHER_COMPLETE_COVARIANT_RECONSTRUCTION" if passed else "SCIENTIFIC_FAIL_ITER163_REPAIRED_TWO_TANGENT_COVARIANT_CLOSURE_FALSE","raw_candidate_count":51,"exact_candidate_rank":int(A.rank()),"N_saturated_candidate_count":15,"explicit_K_candidate_count":16,"source_nonzero_coefficients":len(nonzero),"source_nonzero_N_saturated_coefficients":sum(r["N_saturated"] for r in nonzero),"max_scaled_coefficient_polynomial_degree":maxdeg,"D_train":train,"D_validate":validate,"coefficients":formulas,"changed_qk_heldouts":over,"iter162_direct_regression":regression,"checks":checks,"terminal_science":False,"claim_locks":{"ITER160_minus525_consumed":False,"contacts_set_zero":False,"ITER118_MATCHING_AUTHORIZED":False,"B1_total":"UNAUTHORIZED","BRIDGE_DERIVED":False,"candidate_theory":"UNFORMED / 0%"}}
    Path("iter163_complete_covariant_reconstruction.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in out.items() if k not in {"coefficients","changed_qk_heldouts","iter162_direct_regression"}},indent=2,sort_keys=True))
    raise SystemExit(0 if passed else 1)
if __name__=="__main__": main()
