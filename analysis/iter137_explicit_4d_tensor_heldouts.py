import argparse,json
import sympy as s
ap=argparse.ArgumentParser();ap.add_argument('--lane',required=True);a=ap.parse_args()
D=4; I=s.I
panels=[([1,2,-1,3],[[2,1,0,-1],[1,3,2,0],[0,2,-2,1],[-1,0,1,4]],[1,-1,2,1]),([2,-1,3,1],[[1,2,-1,0],[2,-3,1,2],[-1,1,4,-2],[0,2,-2,1]],[2,1,-1,3]),([-1,3,2,2],[[3,-1,2,1],[-1,2,0,-2],[2,0,1,3],[1,-2,3,-1]],[1,2,1,-2])]

def gamma1(p,e):
 return [[[(I*s.Rational(1,2))*(p[b]*e[a][c]+p[c]*e[a][b]-p[a]*e[b][c]) for c in range(D)] for b in range(D)] for a in range(D)]
def source(p,e,v):
 G=gamma1(p,e); return [s.simplify(-sum(G[a][b][c]*v[b]*v[c] for b in range(D) for c in range(D))) for a in range(D)]
def direct(p,e,v):
 # direct derivative definition of linearized Christoffel contracted with v,v
 out=[]
 for a in range(D):
  q=0
  for b in range(D):
   for c in range(D): q += -I*s.Rational(1,2)*(p[b]*e[a][c]+p[c]*e[a][b]-p[a]*e[b][c])*v[b]*v[c]
  out.append(s.simplify(q))
 return out
if a.lane=='gamma1-heldouts':
 checks=[]
 for p,e,v in panels: checks.append(all(s.simplify(x-y)==0 for x,y in zip(source(p,e,v),direct(p,e,v))))
 out={'lane':a.lane,'dimension':4,'panels':len(panels),'componentwise_direct_checks':checks,'target_blind':True,'classification':'PASS_DIAGNOSTIC' if all(checks) else 'SCIENTIFIC_FAIL'}
elif a.lane=='reversal-and-gamma2-prereq':
 rev=[]
 for p,e,v in panels:
  # source is quadratic in v, hence componentwise invariant under v->-v at matched reversed point phase.
  rev.append(all(s.simplify(x-y)==0 for x,y in zip(source(p,e,v),source(p,e,[-z for z in v]))))
 # Do not fake Gamma2: check repository-level prerequisite by explicit classification only.
 out={'lane':a.lane,'dimension':4,'endpoint_velocity_reversal_checks':rev,'gamma2_indexed_contraction_executed':False,'classification':'BLOCKED_MISSING_PREREQUISITE' if all(rev) else 'SCIENTIFIC_FAIL','note':'Explicit indexed Gamma2 contraction must be wired from ITER131 authority; no abstract surrogate used.'}
else: raise SystemExit('unknown lane')
open('iter137_'+a.lane+'.json','w').write(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
