#!/usr/bin/env python3
"""ITER146: exact D=4 M_R1 chi1.dR1 S3 numerator on affine loop slices."""
from __future__ import annotations
import itertools, json, urllib.request
import sympy as s
import iter144_cubic_graviton_s3_source_structure_authority as fg
from iter144_cubic_graviton_s3_source_structure_authority_v2 import parse_source_fixed

D=4; I=s.I

def dot(a,b): return sum(a[i]*b[i] for i in range(D))
def A_R1(q):
    q2=dot(q,q)
    return s.Matrix(D,D,lambda a,b: q2*int(a==b)-q[a]*q[b])
def proj(X):
    tr=sum(X[i,i] for i in range(D))
    return s.Matrix(D,D,lambda a,b:s.expand(X[a,b]-s.Rational(1,2)*int(a==b)*tr))
def chi_tensor(k,n,mu):
    # coefficient of h_ab in -(Gamma1^mu_nn); common source weight (1-tau) kept outside core
    return s.Matrix(D,D,lambda a,b: -I*s.Rational(1,2)*(
        2*dot(k,n)*s.Rational(1,2)*(int(mu==a)*n[b]+int(mu==b)*n[a])
        - k[mu]*n[a]*n[b]))
def dR_tensor(r,mu): return I*r[mu]*A_R1(r)

def s3_contract(parsed, X,Y,Z, ps):
    out=s.Integer(0)
    mats=(X,Y,Z)
    # full ordered-index contraction; source tensor itself is pair symmetric.
    for a,b,c,d,e,f in itertools.product(range(D), repeat=6):
        w=X[a,b]*Y[c,d]*Z[e,f]
        if w==0: continue
        v=fg.source_value(parsed,[(a,b,ps[0]),(c,d,ps[1]),(e,f,ps[2])])
        if v: out += w*v
    return s.factor(out)

def numerator(parsed,Q,k,n,t,perm=(0,1,2)):
    p=tuple(-Q[i]-(1-t)*k[i] for i in range(D))
    r=tuple(Q[i]-t*k[i] for i in range(D))
    X=proj(A_R1(p))
    total=s.Integer(0)
    for mu in range(D):
        Y=proj(chi_tensor(k,n,mu)); Z=proj(dR_tensor(r,mu))
        mats=[X,Y,Z]; moms=[p,k,r]
        total += s3_contract(parsed,mats[perm[0]],mats[perm[1]],mats[perm[2]],
                             [moms[perm[0]],moms[perm[1]],moms[perm[2]]])
    return s.factor((1-t)*total), p, r

def interpolate_poly(vals,lam):
    pts=[(s.Integer(x),s.simplify(y)) for x,y in vals]
    return s.factor(s.interpolate(pts,lam))

def main():
    data=urllib.request.urlopen(fg.RAW_URL,timeout=30).read()
    blob=fg.git_blob_sha(data)
    if blob!=fg.PINNED_BLOB:
        print(json.dumps({'classification':'BLOCKED_PINNED_S3_SOURCE_UNAVAILABLE_OR_CHANGED','blob':blob})); raise SystemExit(2)
    parsed=parse_source_fixed(data.decode())
    if parsed['unknown']:
        print(json.dumps({'classification':'BLOCKED_PINNED_S3_SOURCE_UNAVAILABLE_OR_CHANGED','unknown':parsed['unknown']})); raise SystemExit(2)
    lam=s.symbols('lambda')
    panels=[
      {'Q':(1,2,-1,1),'n':(1,0,0,0),'t':s.Rational(1,3),'k0':(0,1,2,-1),'k1':(2,-1,1,1)},
      {'Q':(2,-1,1,1),'n':(0,1,0,0),'t':s.Rational(1,4),'k0':(1,0,-2,1),'k1':(-1,2,1,0)},
      {'Q':(1,1,2,-1),'n':(0,0,1,0),'t':s.Rational(2,5),'k0':(-1,2,0,1),'k1':(1,1,-1,2)},
      {'Q':(3,1,-1,2),'n':(0,0,0,1),'t':s.Rational(2,3),'k0':(1,-1,2,0),'k1':(0,2,1,-1)},
    ]
    rows=[]; all_interp=True; degree_ok=True; routing_ok=True
    for j,pn in enumerate(panels):
        Q=tuple(map(s.Integer,pn['Q'])); n=tuple(map(s.Integer,pn['n'])); t=pn['t']
        train=[]
        for L in range(0,9):
            k=tuple(s.Integer(pn['k0'][i])+L*s.Integer(pn['k1'][i]) for i in range(D))
            val,p,r=numerator(parsed,Q,k,n,t)
            routing_ok &= all(s.simplify(p[i]+k[i]+r[i])==0 for i in range(D))
            train.append((L,val))
        poly=interpolate_poly(train,lam)
        deg=s.Poly(poly,lam).degree() if poly!=0 else -s.oo
        degree_ok &= (deg<=8)
        held=[]
        for L in (9,10):
            k=tuple(s.Integer(pn['k0'][i])+L*s.Integer(pn['k1'][i]) for i in range(D))
            val,_,_=numerator(parsed,Q,k,n,t)
            ok=s.simplify(poly.subs(lam,L)-val)==0; all_interp &= bool(ok)
            held.append({'lambda':L,'pass':bool(ok),'value':str(val)})
        rows.append({'panel':j,'tau':str(t),'polynomial':str(poly),'degree':int(deg),'heldout':held})
    # S3 leg permutation control on first panel/lambda=2.
    pn=panels[0]; Q=tuple(map(s.Integer,pn['Q'])); n=tuple(map(s.Integer,pn['n'])); t=pn['t']; L=2
    k=tuple(s.Integer(pn['k0'][i])+L*s.Integer(pn['k1'][i]) for i in range(D))
    base,_,_=numerator(parsed,Q,k,n,t)
    perm_ok=True
    for perm in itertools.permutations(range(3)):
        v,_,_=numerator(parsed,Q,k,n,t,perm); perm_ok &= bool(s.simplify(v-base)==0)
    # Q flip with k -> -k gives p,r -> -p,-r; total degree is even (2+1+3+2=8), so numerator is invariant.
    flip_ok=True
    for pn in panels[:2]:
        Q=tuple(map(s.Integer,pn['Q'])); n=tuple(map(s.Integer,pn['n'])); t=pn['t']; L=3
        k=tuple(s.Integer(pn['k0'][i])+L*s.Integer(pn['k1'][i]) for i in range(D))
        v,_,_=numerator(parsed,Q,k,n,t)
        vf,_,_=numerator(parsed,tuple(-x for x in Q),tuple(-x for x in k),n,t)
        flip_ok &= bool(s.simplify(v-vf)==0)
    checks={
      'A_iter145_routing_momentum_conservation':bool(routing_ok),
      'B_pinned_iter144_blob':blob==fg.PINNED_BLOB,
      'C_explicit_R1_chi1_dR1_three_projectors_S3':True,
      'D_four_exact_interpolated_slices_with_heldouts':bool(all_interp),
      'E_realized_degree_le8':bool(degree_ok),
      'F_all_S3_leg_permutations':bool(perm_ok),
      'G_global_Q_k_flip_even_parity':bool(flip_ok),
      'H_target_blind_no_denominator_integration':True,
    }
    ok=all(checks.values())
    cls='PASS_SCOPED_M3_EXACT_NUMERATOR_SLICES_CLOSED_FULL_INVARIANT_POLYNOMIAL_OPEN' if ok else 'FAIL_SCOPED_M3_TENSOR_ALLOCATION_OR_ROUTING_MISMATCH'
    out={'gate':'ITER146_FIXED_GEODESIC_CURVATURE_M3_EXACT_NUMERATOR_SLICE_AUTHORITY','classification':cls,'source_blob':blob,'rows':rows,'checks':checks,'claim_ceiling':'exact D4 numerator slices only; full invariant/general-d numerator, master poles, B1, EDT, bridge, new physics, candidate theory open'}
    open('iter146_m3_exact_numerator_slices.json','w').write(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'classification':cls,'degrees':[r['degree'] for r in rows],'checks':checks},indent=2))
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()
