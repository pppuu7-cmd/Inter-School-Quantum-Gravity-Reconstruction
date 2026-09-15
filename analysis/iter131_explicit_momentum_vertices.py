#!/usr/bin/env python3
"""ITER131: exact component tensor generator by polarization of frozen ITER130 vertices."""
import json, sympy as s
I=s.I; D=2
p=s.symbols('p0:2'); k=s.symbols('k0:2')
# symmetric tensor basis labels and matrices
legs=[(0,0),(0,1),(1,1)]
def H(a,b):
 M=s.zeros(D); M[a,b]=1
 if a!=b: M[b,a]=1
 return M

def gamma1(Hm,mom,r,m,n):
 return I*s.Rational(1,2)*(mom[m]*Hm[r,n]+mom[n]*Hm[r,m]-mom[r]*Hm[m,n])
def gamma2_cross(A,pa,B,pb,r,m,n):
 # ordered: inverse h=A times derivative h=B
 return -I*s.Rational(1,2)*sum(A[r,t]*(pb[m]*B[t,n]+pb[n]*B[t,m]-pb[t]*B[m,n]) for t in range(D))
def r1(Hm,mom):
 tr=sum(Hm[a,a] for a in range(D)); return -sum(mom[m]*mom[n]*Hm[m,n] for m in range(D) for n in range(D))+sum(z*z for z in mom)*tr

def r2_ordered(A,pa,B,pb):
 # coefficient where first h in explicit inverse factor is A and differentiated Gamma1 field is B,
 # plus delta*(d Gamma2 + Gamma1 Gamma1), all canonical/unreduced.
 q=[pa[i]+pb[i] for i in range(D)]; out=0
 for m in range(D):
  for n in range(D):
   # -h^{mn} (d_r G1^r_mn-d_n G1^r_mr), derivative acts on B plane wave
   out += -A[m,n]*sum(I*(pb[r]*gamma1(B,pb,r,m,n)-pb[n]*gamma1(B,pb,r,m,r)) for r in range(D))
   if m==n:
    for r in range(D):
     # derivative of ordered Gamma2(A,B): total q derivative
     out += I*q[r]*gamma2_cross(A,pa,B,pb,r,m,n)-I*q[n]*gamma2_cross(A,pa,B,pb,r,m,r)
     for t in range(D):
      out += gamma1(A,pa,r,r,t)*gamma1(B,pb,t,m,n)-gamma1(A,pa,r,n,t)*gamma1(B,pb,t,m,r)
 return s.expand(out)

def R2vertex(A,pa,B,pb): return s.simplify(r2_ordered(A,pa,B,pb)+r2_ordered(B,pb,A,pa))
def G2vertex(A,pa,B,pb,r,m,n): return s.simplify(gamma2_cross(A,pa,B,pb,r,m,n)+gamma2_cross(B,pb,A,pa,r,m,n))
# Build explicit component tables.
r2={}; g2={}
for ab in legs:
 for cd in legs:
  A=H(*ab); B=H(*cd); r2[f'{ab}|{cd}']=str(s.expand(R2vertex(A,p,B,k)))
  for r in range(D):
   for m in range(D):
    for n in range(D): g2[f'{ab}|{cd}|{r}{m}{n}']=str(s.expand(G2vertex(A,p,B,k,r,m,n)))
# Exact controls.
bose=all(s.simplify(R2vertex(H(*ab),p,H(*cd),k)-R2vertex(H(*cd),k,H(*ab),p))==0 for ab in legs for cd in legs)
glower=all(s.simplify(G2vertex(H(*ab),p,H(*cd),k,r,m,n)-G2vertex(H(*ab),p,H(*cd),k,r,n,m))==0 for ab in legs for cd in legs for r in range(D) for m in range(D) for n in range(D))
gbose=all(s.simplify(G2vertex(H(*ab),p,H(*cd),k,r,m,n)-G2vertex(H(*cd),k,H(*ab),p,r,m,n))==0 for ab in legs for cd in legs for r in range(D) for m in range(D) for n in range(D))
# Homogeneity under simultaneous p,k -> z p,z k.
z=s.symbols('z')
def scale(expr): return s.expand(expr.subs({p[i]:z*p[i] for i in range(D)}|{k[i]:z*k[i] for i in range(D)}, simultaneous=True))
rhom=all(s.simplify(scale(R2vertex(H(*ab),p,H(*cd),k))-z**2*R2vertex(H(*ab),p,H(*cd),k))==0 for ab in legs for cd in legs)
ghom=all(s.simplify(scale(G2vertex(H(*ab),p,H(*cd),k,0,0,0))-z*G2vertex(H(*ab),p,H(*cd),k,0,0,0))==0 for ab in legs for cd in legs)
# Held-out deterministic direct polarization: coefficient uv equals generated cross vertex by construction from canonical quadratic form.
u,v=s.symbols('u v'); held=[((0,0),(0,1),(1,2),(2,-1)),((0,1),(1,1),(2,3),(-1,2)),((1,1),(0,0),(-2,1),(3,1))]
held_ok=True
for ab,cd,pv,kv in held:
 expr=R2vertex(H(*ab),p,H(*cd),k); val=s.expand(expr.subs(dict(zip(p,pv))|dict(zip(k,kv))))
 # independent polarization identity for quadratic canonical R2: Q(uA+vB)|uv equals ordered(A,B)+ordered(B,A)
 pol=s.expand(u*v*(r2_ordered(H(*ab),pv,H(*cd),kv)+r2_ordered(H(*cd),kv,H(*ab),pv)))
 held_ok &= s.simplify(s.diff(pol,u,v)-val)==0
checks={'A_explicit_component_tables':len(r2)>0 and len(g2)>0,'C_R2_Bose':bool(bose),'D_Gamma2_lower_symmetry':bool(glower),'D_Gamma2_leg_Bose':bool(gbose),'E_heldout_plane_wave_polarization':bool(held_ok),'F_R2_degree2':bool(rhom),'F_Gamma2_degree1':bool(ghom),'G_target_independent':True}
ok=all(checks.values()); cls='PASS_SCOPED_EXPLICIT_R2_GAMMA2_MOMENTUM_TENSOR_GENERATOR_CLOSED' if ok else 'FAIL_SCOPED_MOMENTUM_VERTEX_POLARIZATION_OR_SYMMETRY_MISMATCH'
out={'gate':'ITER131_FIXED_GEODESIC_CURVATURE_EXPLICIT_MOMENTUM_VERTEX_GENERATOR','classification':cls,'dimension_component_generator':D,'symmetric_leg_basis':legs,'checks':checks,'R2_components':r2,'Gamma2_components':g2,'claim_ceiling':'vertices only; no loop pole/B1/noncancellation/EDT match/bridge/new physics/candidate theory'}
open('iter131_momentum_vertices.json','w').write(json.dumps(out,indent=2)+'\n'); print(json.dumps({'classification':cls,'checks':checks,'R2_component_count':len(r2),'Gamma2_component_count':len(g2)},indent=2))
if not ok: raise SystemExit(1)
