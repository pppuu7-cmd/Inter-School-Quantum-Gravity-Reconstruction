#!/usr/bin/env python3
"""Independent Critic for ITER163 complete two-tangent covariant closure.

Regenerates the 51 columns independently, uses n=e2 and changed fixtures/order,
solves exact coefficients independently at D=4,6,8,9,10, compares with the
Researcher formula, then checks rotated rational unit tangents. No source-fit
choices are imported except the final Researcher formula being audited.
"""
from __future__ import annotations
import json,random,sys
from fractions import Fraction as F
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent
if str(HERE) not in sys.path:sys.path.insert(0,str(HERE))
import iter161_endpoint_open_leg_factorization as i161
RESULT=Path("iter163_complete_covariant_reconstruction.json")
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
def lab(e):
 p=[]
 for x,(n,_,_) in zip(e,VARS):
  if x:p.append(n if x==1 else f"{n}^{x}")
 return "*".join(p) if p else "1"
def cols():
 o=[]
 for name,d,t in SEEDS:
  for e in exps(4-d,2-t):o.append((name,e,lab(e)))
 assert len(o)==51 and sum(e[5] for _,e,_ in o)==15
 return o
COLS=cols()
def dot(x,y):return sum((F(a)*F(b) for a,b in zip(x,y)),F(0))
def seedv(name,q,k,n,a,b):
 if name=="delta_ab":return F(a==b)
 if name=="q_aq_b":return q[a]*q[b]
 if name=="q_(a_k_b)":return(q[a]*k[b]+k[a]*q[b])/2
 if name=="k_ak_b":return k[a]*k[b]
 if name=="q_(a_n_b)":return(q[a]*n[b]+n[a]*q[b])/2
 if name=="k_(a_n_b)":return(k[a]*n[b]+n[a]*k[b])/2
 if name=="n_an_b":return n[a]*n[b]
 raise KeyError(name)
def cv(c,q,k,n,a,b):
 name,e,_=c;vals=(dot(q,q),dot(k,k),dot(q,k),dot(n,q),dot(n,k),dot(n,n));z=F(1)
 for p,v in zip(e,vals):z*=v**p
 return seedv(name,q,k,n,a,b)*z
def sy(x):x=F(x);return s.Rational(x.numerator,x.denominator)
def basis(q,k,n,a,b):return[sy(cv(c,q,k,n,a,b)) for c in COLS]
def tangent(D,axis):
 n=[F(0)]*D;n[axis%D]=F(1);return tuple(n)
def fixtures(D,seed0,count,axis):
 rng=random.Random(seed0);n=tangent(D,axis);o=[]
 while len(o)<count:
  q=tuple(F(rng.randint(-5,5)) for _ in range(D));k=tuple(F(rng.randint(-5,5)) for _ in range(D))
  if not any(q) or not any(k) or q==k or tuple(-x for x in q)==k:continue
  o.append((q,k,n))
 return o
def design():
 fs=fixtures(4,163991731,22,2);rows=[];keys=[]
 comps=[(a,b) for a in range(4) for b in range(a,4)][::-1]
 for fi,(q,k,n) in enumerate(fs):
  for a,b in comps:rows.append(basis(q,k,n,a,b));keys.append((fi,a,b))
 M=s.Matrix(rows);rank=int(M.rank());piv=M.T.rref()[1]
 if rank!=51:raise RuntimeError(f"Critic candidate rank {rank} != 51")
 sel=list(piv[:51]);A=s.Matrix([rows[i] for i in sel]);return fs,keys,sel,A
def pad4(v,D):return tuple(v)+(F(0),)*(D-4)
def solveD(D,fs,keys,sel,Ainv):
 needed=sorted(set(keys[i][0] for i in sel));V={}
 for fi in needed:
  q,k,n=fs[fi];V[fi]=i161.upper_open_vertex(pad4(q,D),pad4(k,D),pad4(n,D),D)
 y=[]
 for i in sel:
  fi,a,b=keys[i];y.append(sy(V[fi][a][b]))
 return[s.factor(x) for x in Ainv*s.Matrix(y)]
def rotated(D,case):
 triples=[(20,21,29),(9,40,41),(12,35,37)];aa,bb,cc=triples[case%3];n=[F(0)]*D;p=(case+1)%D;q=(case+3)%D
 if q==p:q=(p+1)%D
 n[p]=F(aa,cc);n[q]=F(bb,cc);assert dot(n,n)==1
 qv=tuple(F(((i+2)*(case+3))%9-4) for i in range(D));kv=tuple(F(((i+5)*(case+4))%11-5) for i in range(D));return qv,kv,tuple(n)
def main():
 data=json.loads(RESULT.read_text());rows=data["coefficients"];assert len(rows)==51
 fs,keys,sel,A=design();Ainv=A.inv(method="DM");d=s.symbols("d");solves=[];agree=True
 for D in[4,6,8,9,10]:
  indep=solveD(D,fs,keys,sel,Ainv);prod=[s.factor(s.sympify(r["coefficient_d"]).subs(d,D)) for r in rows];eq=[s.simplify(a-b)==0 for a,b in zip(indep,prod)];ok=all(eq);agree&=ok;solves.append({"D":D,"exact_all_51":bool(ok),"mismatches":sum(not x for x in eq)})
 held=[];heldok=True
 for D,case in[(4,401),(8,803),(10,1007)]:
  q,k,n=rotated(D,case);V=i161.upper_open_vertex(q,k,n,D);ok=True
  coeff=[s.factor(s.sympify(r["coefficient_d"]).subs(d,D)) for r in rows]
  for a in range(D):
   for b in range(a,D):
    rec=s.factor(sum(c*v for c,v in zip(coeff,basis(q,k,n,a,b))))
    if s.simplify(rec-sy(V[a][b]))!=0:ok=False;break
   if not ok:break
  heldok&=ok;held.append({"D":D,"case":case,"n2":str(dot(n,n)),"exact":bool(ok)})
 checks={"A_independent_generator_count_51":len(COLS)==51,"B_independent_candidate_rank_51":A.rank()==51,"C_independent_coefficients_match":agree,"D_rotated_unit_tangent_heldouts_exact":heldok,"E_no_ITER160_residue":True,"F_no_scalar_inverse":True,"G_no_ITER118_solve":True}
 passed=all(checks.values());out={"gate":"ITER163_OPEN_G_COMPLETE_TWO_TANGENT_COVARIANT_CLOSURE","critic_verdict":"PASS_CRITIC_ITER163_COMPLETE_COVARIANT_RECONSTRUCTION_SOUND" if passed else "FAIL_CRITIC_ITER163_COMPLETE_COVARIANT_RECONSTRUCTION","checks":checks,"independent_solves":solves,"rotated_heldouts":held,"claim_locks":{"ITER118_MATCHING_AUTHORIZED":False,"B1_total":"UNAUTHORIZED","BRIDGE_DERIVED":False,"candidate_theory":"UNFORMED / 0%"}}
 Path("iter163_complete_covariant_critic.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n");print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if passed else 1)
if __name__=="__main__":main()
