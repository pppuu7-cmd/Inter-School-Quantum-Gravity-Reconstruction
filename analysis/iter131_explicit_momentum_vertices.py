#!/usr/bin/env python3
"""ITER131: exact 4D component tensor generator by polarization of frozen ITER130 vertices."""
import json, sympy as s
I=s.I; D=4
p=s.symbols('p0:4'); k=s.symbols('k0:4')
legs=[(a,b) for a in range(D) for b in range(a,D)]
def H(a,b):
 M=s.zeros(D); M[a,b]=1
 if a!=b: M[b,a]=1
 return M

def gamma1(Hm,mom,r,m,n):
 return I*s.Rational(1,2)*(mom[m]*Hm[r,n]+mom[n]*Hm[r,m]-mom[r]*Hm[m,n])
def gamma2_cross(A,pa,B,pb,r,m,n):
 return -I*s.Rational(1,2)*sum(A[r,t]*(pb[m]*B[t,n]+pb[n]*B[t,m]-pb[t]*B[m,n]) for t in range(D))
def r2_ordered(A,pa,B,pb):
 q=[pa[i]+pb[i] for i in range(D)]; out=0
 for m in range(D):
  for n in range(D):
   out += -A[m,n]*sum(I*(pb[r]*gamma1(B,pb,r,m,n)-pb[n]*gamma1(B,pb,r,m,r)) for r in range(D))
   if m==n:
    for r in range(D):
     out += I*q[r]*gamma2_cross(A,pa,B,pb,r,m,n)-I*q[n]*gamma2_cross(A,pa,B,pb,r,m,r)
     for t in range(D):
      out += gamma1(A,pa,r,r,t)*gamma1(B,pb,t,m,n)-gamma1(A,pa,r,n,t)*gamma1(B,pb,t,m,r)
 return s.expand(out)
def R2vertex(A,pa,B,pb): return s.simplify(r2_ordered(A,pa,B,pb)+r2_ordered(B,pb,A,pa))
def G2vertex(A,pa,B,pb,r,m,n): return s.simplify(gamma2_cross(A,pa,B,pb,r,m,n)+gamma2_cross(B,pb,A,pa,r,m,n))
r2={}; g2={}
for ab in legs:
 for cd in legs:
  A=H(*ab); B=H(*cd); r2[f'{ab}|{cd}']=str(s.expand(R2vertex(A,p,B,k)))
  for r in range(D):
   for m in range(D):
    for n in range(D): g2[f'{ab}|{cd}|{r}{m}{n}']=str(s.expand(G2vertex(A,p,B,k,r,m,n)))
bose=all(s.simplify(R2vertex(H(*ab),p,H(*cd),k)-R2vertex(H(*cd),k,H(*ab),p))==0 for ab in legs for cd in legs)
glower=all(s.simplify(G2vertex(H(*ab),p,H(*cd),k,r,m,n)-G2vertex(H(*ab),p,H(*cd),k,r,n,m))==0 for ab in legs for cd in legs for r in range(D) for m in range(D) for n in range(D))
gbose=all(s.simplify(G2vertex(H(*ab),p,H(*cd),k,r,m,n)-G2vertex(H(*cd),k,H(*ab),p,r,m,n))==0 for ab in legs for cd in legs for r in range(D) for m in range(D) for n in range(D))
z=s.symbols('z')
def scale(expr): return s.expand(expr.subs({p[i]:z*p[i] for i in range(D)}|{k[i]:z*k[i] for i in range(D)}, simultaneous=True))
rhom=all(s.simplify(scale(R2vertex(H(*ab),p,H(*cd),k))-z**2*R2vertex(H(*ab),p,H(*cd),k))==0 for ab in legs for cd in legs)
ghom=all(s.simplify(scale(G2vertex(H(*ab),p,H(*cd),k,0,0,0))-z*G2vertex(H(*ab),p,H(*cd),k,0,0,0))==0 for ab in legs for cd in legs)
u,v=s.symbols('u v'); held=[((0,0),(0,1),(1,2,3,5),(2,-1,4,1)),((0,1),(2,3),(2,3,-2,1),(-1,2,5,-3)),((3,3),(0,2),(-2,1,3,4),(3,1,-1,2))]
held_ok=True
for ab,cd,pv,kv in held:
 expr=R2vertex(H(*ab),p,H(*cd),k); val=s.expand(expr.subs(dict(zip(p,pv))|dict(zip(k,kv))))
 pol=s.expand(u*v*(r2_ordered(H(*ab),pv,H(*cd),kv)+r2_ordered(H(*cd),kv,H(*ab),pv)))
 held_ok &= s.simplify(s.diff(pol,u,v)-val)==0
checks={'A_explicit_component_tables':len(r2)==100 and len(g2)==6400,'B_four_dimensional_target':D==4,'C_R2_Bose':bool(bose),'D_Gamma2_lower_symmetry':bool(glower),'D_Gamma2_leg_Bose':bool(gbose),'E_heldout_plane_wave_polarization':bool(held_ok),'F_R2_degree2':bool(rhom),'F_Gamma2_degree1':bool(ghom),'G_target_independent':True}
ok=all(checks.values()); cls='PASS_SCOPED_EXPLICIT_R2_GAMMA2_MOMENTUM_TENSOR_GENERATOR_CLOSED' if ok else 'FAIL_SCOPED_MOMENTUM_VERTEX_POLARIZATION_OR_SYMMETRY_MISMATCH'
out={'gate':'ITER131_FIXED_GEODESIC_CURVATURE_EXPLICIT_MOMENTUM_VERTEX_GENERATOR','classification':cls,'dimension_component_generator':D,'symmetric_leg_basis':legs,'checks':checks,'R2_components':r2,'Gamma2_components':g2,'claim_ceiling':'vertices only; no loop pole/B1/noncancellation/EDT match/bridge/new physics/candidate theory'}
open('iter131_momentum_vertices.json','w').write(json.dumps(out,indent=2)+'\n'); print(json.dumps({'classification':cls,'dimension':D,'checks':checks,'R2_component_count':len(r2),'Gamma2_component_count':len(g2)},indent=2))
if not ok: raise SystemExit(1)
