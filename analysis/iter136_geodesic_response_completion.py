import argparse, json
import sympy as s

ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); a=ap.parse_args()
t,u,L=s.symbols('t u L', real=True)
I=s.I
# Scalar phase reduction of the exact tensor contraction along v=L n.
# A denotes the frozen tensor contraction of Gamma1 with n,n for one plane wave;
# omega=L p.n.  This lane tests the line-response algebra without choosing a target.
A,w=s.symbols('A w', nonzero=True)
S=lambda q: -L**2*A*s.exp(I*w*q)
G_left=lambda tt,uu: -tt*(1-uu) # d_t^2 G=delta, Dirichlet
G_right=lambda tt,uu: -uu*(1-tt)

def xi(tt):
    return s.simplify(s.integrate(G_left(tt,u)*S(u),(u,tt,1))+s.integrate(G_right(tt,u)*S(u),(u,0,tt)))

if a.lane=='first-order-line-response':
    X=s.simplify(xi(t))
    checks={
      'xi_endpoint_0': s.simplify(X.subs(t,0))==0,
      'xi_endpoint_1': s.simplify(X.subs(t,1))==0,
      'xi_equation': s.simplify(s.diff(X,t,2)-S(t))==0,
    }
    # reversal: t->1-t, n->-n implies w invariant for reversed parametrized segment after p.z phase origin shift;
    # test Green kernel covariance independently.
    checks['green_reversal']=s.simplify(G_left(1-t,1-u)-G_right(t,u))==0
    out={'lane':a.lane,'xi1':str(X),'checks':checks,'classification':'PASS_DIAGNOSTIC' if all(checks.values()) else 'SCIENTIFIC_FAIL'}
elif a.lane=='heldout-direct-expansion':
    # Independent symbolic bookkeeping of the frozen second-order geodesic expansion.
    # Symbols stand for evaluated tensor contractions; direct polynomial expansion is compared to census.
    k=s.symbols('k'); G1,G2,dG1,x,xp=s.symbols('G1 G2 dG1 x xp')
    # Gamma(z)=k[G1+k*x*dG1]+k^2 G2; zdot=v+k*xp; set v=1 for coefficient identity.
    expr=k*(G1+k*x*dG1)*(1+k*xp)**2+k**2*G2*(1+k*xp)**2
    direct=s.expand(expr).coeff(k,2)
    census=G2+x*dG1+2*G1*xp
    base=s.simplify(direct-census)==0
    # three frozen held-outs substitute distinct exact integers; no retuning.
    panels=[{G1:2,G2:3,dG1:5,x:7,xp:11},{G1:-3,G2:2,dG1:7,x:-5,xp:13},{G1:5,G2:-7,dG1:-2,x:3,xp:-11}]
    checks=[s.simplify((direct-census).subs(P))==0 for P in panels]
    out={'lane':a.lane,'direct_Ok2':str(direct),'census':str(census),'symbolic_identity':base,'heldout_panels':checks,'target_blind':True,'classification':'PASS_DIAGNOSTIC' if base and all(checks) else 'SCIENTIFIC_FAIL'}
else: raise SystemExit('unknown lane')
open('iter136_'+a.lane+'.json','w').write(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
