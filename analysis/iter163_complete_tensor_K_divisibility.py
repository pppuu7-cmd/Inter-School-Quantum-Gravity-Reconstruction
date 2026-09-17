#!/usr/bin/env python3
"""ITER163 exact K-divisibility kernel on the prospectively frozen 51-column closure.

Outcome-blind structural algebra: generate all 51 columns including N=n^2,
evaluate N=1 in unit-tangent frames, and compute exact normal forms modulo
<K=k^2> componentwise. D=4 and D=5 must agree. No source coefficients are used.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s
SEEDS=[("delta_ab",0,0),("q_aq_b",2,0),("q_(a_k_b)",2,0),("k_ak_b",2,0),("q_(a_n_b)",1,1),("k_(a_n_b)",1,1),("n_an_b",0,2)]
VARS=[("Q",2,0),("K",2,0),("S",2,0),("a",1,1),("b",1,1),("N",0,2)]
def exps(deg,tan):
 o=[]
 for i in range(3):
  for j in range(3):
   for l in range(3):
    for u in range(5):
     for v in range(5):
      for w in range(2):
       e=(i,j,l,u,v,w)
       if sum(x*y[1] for x,y in zip(e,VARS))==deg and sum(x*y[2] for x,y in zip(e,VARS))==tan:o.append(e)
 return o
def cols():
 o=[]
 for name,d,t in SEEDS:
  for e in exps(4-d,2-t):o.append((name,e))
 assert len(o)==51 and sum(bool(e[1]) for _,e in o)==16
 return o
COLS=cols()
def seedv(name,q,k,n,a,b):
 if name=="delta_ab":return s.Integer(a==b)
 if name=="q_aq_b":return q[a]*q[b]
 if name=="q_(a_k_b)":return(q[a]*k[b]+k[a]*q[b])/2
 if name=="k_ak_b":return k[a]*k[b]
 if name=="q_(a_n_b)":return(q[a]*n[b]+n[a]*q[b])/2
 if name=="k_(a_n_b)":return(k[a]*n[b]+n[a]*k[b])/2
 if name=="n_an_b":return n[a]*n[b]
 raise KeyError(name)
def expr(col,q,k,n,a,b):
 name,e=col;Q=sum(x*x for x in q);K=sum(x*x for x in k);S=sum(x*y for x,y in zip(q,k));aa=sum(x*y for x,y in zip(n,q));bb=sum(x*y for x,y in zip(n,k));N=sum(x*x for x in n);vals=(Q,K,S,aa,bb,N);z=s.Integer(1)
 for p,v in zip(e,vals):z*=v**p
 return s.expand(seedv(name,q,k,n,a,b)*z)
def modK(poly,k):
 rest=sum(x*x for x in k[1:]);P=s.Poly(s.expand(poly),k[0],domain="EX");out=s.Integer(0)
 for(power,),coeff in P.terms():out+=coeff*((-rest)**(power//2))*(k[0]**(power%2))
 return s.expand(out)
def qmap(D):
 q=s.symbols("q0:"+str(D));k=s.symbols("k0:"+str(D));n=(s.Integer(1),)+tuple(s.Integer(0) for _ in range(D-1));vars=q+k;rows={}
 for j,c in enumerate(COLS):
  for a in range(D):
   for b in range(a,D):
    P=s.Poly(modK(expr(c,q,k,n,a,b),k),*vars,domain=s.QQ)
    for mon,coeff in P.terms():
     key=(a,b,mon);rows.setdefault(key,[s.Rational(0) for _ in COLS]);rows[key][j]=s.Rational(coeff)
 M=s.Matrix(list(rows.values()));rank=int(M.rank());null=M.nullspace();explicit=[i for i,(_,e) in enumerate(COLS) if e[1]>0];non=[i for i in range(51) if i not in explicit];nonrank=int(M[:,non].rank());expzero=all(all(M[r,j]==0 for r in range(M.rows)) for j in explicit)
 return{"D":D,"constraint_rows":M.rows,"quotient_rank":rank,"kernel_dimension":len(null),"explicit_K_count":len(explicit),"nonexplicit_count":len(non),"nonexplicit_quotient_rank":nonrank,"all_explicit_K_zero_mod_K":bool(expzero),"kernel_exactly_explicit_K_span":bool(expzero and len(null)==len(explicit) and nonrank==len(non)),"nullspace_basis":[[str(x) for x in v] for v in null]}
def main():
 rr=[qmap(4),qmap(5)];agree=rr[0]["quotient_rank"]==rr[1]["quotient_rank"] and rr[0]["kernel_dimension"]==rr[1]["kernel_dimension"];exact=agree and all(r["kernel_exactly_explicit_K_span"] for r in rr)
 checks={"A_raw_51":len(COLS)==51,"B_explicit_K_count_16":sum(bool(e[1]) for _,e in COLS)==16,"C_D4_D5_agree":agree,"D_full_K_kernel_equals_explicit_K_span":exact,"E_no_source_coefficients":True,"F_no_ITER160_residue":True,"G_no_ITER118_solve":True}
 passed=all(checks.values());out={"gate":"ITER163_OPEN_G_COMPLETE_TWO_TANGENT_COVARIANT_CLOSURE","classification":"PASS_STRUCTURAL_ITER163_COMPLETE_51_SPAN_K_DIVISIBILITY_KERNEL" if passed else "SCIENTIFIC_FAIL_ITER163_REPAIRED_TWO_TANGENT_K_STRUCTURE_FALSE","dimension_results":rr,"checks":checks,"terminal_science":False,"claim_locks":{"ITER118_MATCHING_AUTHORIZED":False,"B1_total":"UNAUTHORIZED","BRIDGE_DERIVED":False,"candidate_theory":"UNFORMED / 0%"}}
 Path("iter163_complete_tensor_K_divisibility.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n");print(json.dumps({k:v for k,v in out.items() if k!="dimension_results"},indent=2,sort_keys=True));[print(json.dumps({k:v for k,v in r.items() if k!="nullspace_basis"},sort_keys=True)) for r in rr];raise SystemExit(0 if passed else 1)
if __name__=="__main__":main()
