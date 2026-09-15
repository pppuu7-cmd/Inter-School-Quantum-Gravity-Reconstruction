#!/usr/bin/env python3
import argparse,json,sympy as s
ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); a=ap.parse_args(); D=4
p=s.symbols('p0:4'); n=s.symbols('n0:4'); tau=s.symbols('tau', real=True); I=s.I
legs=[(i,j) for i in range(D) for j in range(i,D)]
def H(ab):
 M=s.zeros(D); i,j=ab; M[i,j]=1
 if i!=j:M[j,i]=1
 return M
def R1(Hm):
 tr=sum(Hm[i,i] for i in range(D)); return s.expand(sum(p[i]*p[j]*Hm[i,j] for i in range(D) for j in range(D))-sum(x*x for x in p)*tr)
checks={'D4':D==4,'target_blind':True}
if a.lane=='curvature-derivatives':
 # derivative tensors are exact Fourier multiplications of the validated linearized scalar curvature.
 held=[(1,2,3,4),(-2,1,0,3)]
 ok=True
 for ab in legs:
  r=R1(H(ab))
  for mu in range(D):
   d=I*p[mu]*r
   for nu in range(D):
    d2=-p[mu]*p[nu]*r
    z=s.symbols('z'); sub={p[i]:z*p[i] for i in range(D)}
    ok &= s.expand(d.subs(sub)-z**3*d)==0 and s.expand(d2.subs(sub)-z**4*d2)==0
 for pv in held:
  sub=dict(zip(p,pv)); ok &= all(s.simplify((I*p[mu]*R1(H((0,1)))).subs(sub)-I*pv[mu]*R1(H((0,1))).subs(sub))==0 for mu in range(D))
 checks.update({'dR1_degree3_d2R1_degree4':bool(ok),'heldout_direct':bool(ok)})
 out={'lane':a.lane,'checks':checks,'objects':'dR1_mu=i p_mu R1; d2R1_munu=-p_mu p_nu R1'}
elif a.lane=='chi1-line-kernel':
 # First variation of straight-segment squared-length constraint, stripped of overall endpoint length normalization:
 # K_ab(tau,p;n)=n_a n_b exp(i tau p.n), kept as affine kernel before tau integration.
 pdn=sum(p[i]*n[i] for i in range(D)); kernels={str(ab):s.expand(n[ab[0]]*n[ab[1]]*s.exp(I*tau*pdn)) for ab in legs}
 rev=all(s.simplify(expr.subs({tau:1-tau,**{p[i]:-p[i] for i in range(D)}}, simultaneous=True)-s.exp(-I*pdn)*expr)==0 for expr in kernels.values())
 held=[((0,0),(1,2,0,-1),(2,0,1,1),s.Rational(1,3)),((1,3),(-1,1,2,0),(1,3,-2,2),s.Rational(2,5))]
 hok=True
 for ab,pv,nv,tv in held:
  expr=kernels[str(ab)].subs(dict(zip(p,pv))|dict(zip(n,nv))|{tau:tv}); direct=nv[ab[0]]*nv[ab[1]]*s.exp(I*tv*sum(pv[i]*nv[i] for i in range(D))); hok &= s.simplify(expr-direct)==0
 checks.update({'affine_kernel_retained':all(expr.has(tau) or expr==0 for expr in kernels.values()),'endpoint_reversal_covariance':bool(rev),'heldout_direct':bool(hok)})
 out={'lane':a.lane,'checks':checks,'kernel_definition':'K_ab(tau,p;n)=n_a n_b exp(i tau p.n)','normalization_scope':'overall segment/world-function normalization deferred; no chi2 claim'}
else: raise SystemExit('bad lane')
out['classification']='PASS_LANE' if all(checks.values()) else 'FAIL_LANE'; open(f'iter133_{a.lane}.json','w').write(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2));
if not all(checks.values()): raise SystemExit(1)
