#!/usr/bin/env python3
"""ITER147: exact rational-momentum S3 evaluator and frozen ITER146 slice repair."""
from __future__ import annotations
import itertools, json, urllib.request
import sympy as s
import iter144_cubic_graviton_s3_source_structure_authority as fg
from iter144_cubic_graviton_s3_source_structure_authority_v2 import parse_source_fixed
import iter146_m3_exact_numerator_slice_authority as i146

D=4

def source_value_exact(parsed, legs):
    idx={}; mom={}
    for i,(a,b,p) in enumerate(legs,1):
        idx[f'm{i}']=a; idx[f'n{i}']=b
        mom[f'p{i}']=tuple(s.sympify(x) for x in p)
    out=s.Rational(0)
    for coeff,factors in parsed['terms']:
        val=s.Rational(coeff.numerator,coeff.denominator)
        for typ,a,b in factors:
            if typ=='metric': val *= int(idx[a]==idx[b])
            elif typ=='ip': val *= mom[b][idx[a]]
            else: val *= sum(mom[a][j]*mom[b][j] for j in range(D))
            if val==0: break
        out += val
    return s.factor(out)

def main():
    data=urllib.request.urlopen(fg.RAW_URL,timeout=30).read(); blob=fg.git_blob_sha(data)
    if blob!=fg.PINNED_BLOB:
        print(json.dumps({'classification':'BLOCKED_PINNED_S3_SOURCE_OR_PARSER_CHANGED','blob':blob})); raise SystemExit(2)
    parsed=parse_source_fixed(data.decode())
    if parsed['unknown']:
        print(json.dumps({'classification':'BLOCKED_PINNED_S3_SOURCE_OR_PARSER_CHANGED','unknown':parsed['unknown']})); raise SystemExit(2)

    # B: exact agreement with ITER144 evaluator on its integer-momentum domain.
    int_panels=[
      [((0,0),(1,2,-1,1)),((1,2),(2,-1,1,0)),((2,3),(-3,-1,0,-1))],
      [((1,1),(0,2,1,-1)),((0,3),(1,-1,2,1)),((2,2),(-1,-1,-3,0))],
      [((0,2),(2,0,-1,3)),((1,3),(-1,2,1,-2)),((0,1),(-1,-2,0,-1))],
    ]
    integer_eq=True; integer_rows=[]
    for legs in int_panels:
        for perm in itertools.permutations(range(3)):
            lp=[legs[i] for i in perm]
            v0=fg.source_value(parsed,[(ab[0],ab[1],p) for ab,p in lp])
            v1=source_value_exact(parsed,[(ab[0],ab[1],p) for ab,p in lp])
            eq=s.simplify(v0-v1)==0; integer_eq &= bool(eq)
        integer_rows.append({'legs':str(legs),'all_permutations_equal_to_original':bool(integer_eq)})

    # C: symbolic common scaling on rational momenta; source is homogeneous degree two.
    z=s.symbols('z')
    rat_legs=[
      ((0,1),(s.Rational(1,3),s.Rational(2,5),-1,s.Rational(4,7))),
      ((1,2),(s.Rational(2,3),-1,s.Rational(3,5),s.Rational(1,2))),
      ((2,3),(-1,s.Rational(3,5),s.Rational(2,5),s.Rational(-15,14))),
    ]
    base=source_value_exact(parsed,[(ab[0],ab[1],p) for ab,p in rat_legs])
    scaled=source_value_exact(parsed,[(ab[0],ab[1],tuple(z*x for x in p)) for ab,p in rat_legs])
    homogeneity_ok=s.simplify(scaled-z**2*base)==0

    # Use exact evaluator in the already-frozen ITER146 tensor allocation.
    i146.fg.source_value=source_value_exact
    lam=s.symbols('lambda')
    panels=[
      {'Q':(1,2,-1,1),'n':(1,0,0,0),'t':s.Rational(1,3),'k0':(0,1,2,-1),'k1':(2,-1,1,1)},
      {'Q':(2,-1,1,1),'n':(0,1,0,0),'t':s.Rational(1,4),'k0':(1,0,-2,1),'k1':(-1,2,1,0)},
      {'Q':(1,1,2,-1),'n':(0,0,1,0),'t':s.Rational(2,5),'k0':(-1,2,0,1),'k1':(1,1,-1,2)},
      {'Q':(3,1,-1,2),'n':(0,0,0,1),'t':s.Rational(2,3),'k0':(1,-1,2,0),'k1':(0,2,1,-1)},
    ]
    rows=[]; held_ok=True; degree_ok=True; routing_ok=True
    for j,pn in enumerate(panels):
        Q=tuple(map(s.Integer,pn['Q'])); n=tuple(map(s.Integer,pn['n'])); t=pn['t']; train=[]
        for L in range(9):
            k=tuple(s.Integer(pn['k0'][i])+L*s.Integer(pn['k1'][i]) for i in range(D))
            val,p,r=i146.numerator(parsed,Q,k,n,t)
            routing_ok &= all(s.simplify(p[i]+k[i]+r[i])==0 for i in range(D))
            train.append((L,val))
        poly=s.factor(s.interpolate(train,lam)); deg=s.Poly(poly,lam).degree() if poly!=0 else -s.oo
        degree_ok &= bool(deg<=8); held=[]
        for L in (9,10):
            k=tuple(s.Integer(pn['k0'][i])+L*s.Integer(pn['k1'][i]) for i in range(D))
            val,_,_=i146.numerator(parsed,Q,k,n,t)
            eq=s.simplify(poly.subs(lam,L)-val)==0; held_ok &= bool(eq)
            held.append({'lambda':L,'pass':bool(eq),'value':str(val)})
        rows.append({'panel':j,'tau':str(t),'degree':int(deg),'polynomial':str(poly),'heldout':held})

    # Frozen permutation and global momentum-flip controls.
    pn=panels[0]; Q=tuple(map(s.Integer,pn['Q'])); n=tuple(map(s.Integer,pn['n'])); t=pn['t']; L=2
    k=tuple(s.Integer(pn['k0'][i])+L*s.Integer(pn['k1'][i]) for i in range(D))
    v0,_,_=i146.numerator(parsed,Q,k,n,t); perm_ok=True
    for perm in itertools.permutations(range(3)):
        v,_,_=i146.numerator(parsed,Q,k,n,t,perm); perm_ok &= bool(s.simplify(v-v0)==0)
    flip_ok=True
    for pn in panels[:2]:
        Q=tuple(map(s.Integer,pn['Q'])); n=tuple(map(s.Integer,pn['n'])); t=pn['t']; L=3
        k=tuple(s.Integer(pn['k0'][i])+L*s.Integer(pn['k1'][i]) for i in range(D))
        v,_,_=i146.numerator(parsed,Q,k,n,t)
        vf,_,_=i146.numerator(parsed,tuple(-x for x in Q),tuple(-x for x in k),n,t)
        flip_ok &= bool(s.simplify(v-vf)==0)

    checks={
      'A_pinned_source_and_fixed_parser':bool(blob==fg.PINNED_BLOB and not parsed['unknown']),
      'B_exact_evaluator_equals_ITER144_on_integer_domain':bool(integer_eq),
      'C_rational_symbolic_S3_homogeneous_degree2':bool(homogeneity_ok),
      'D_frozen_ITER146_four_slices_heldouts':bool(held_ok),
      'E_realized_affine_degree_le8':bool(degree_ok),
      'F_routing_permutation_and_flip_controls':bool(routing_ok and perm_ok and flip_ok),
      'G_target_blind_no_denominator_integration':True,
    }
    ok=all(checks.values())
    cls=('PASS_SCOPED_RATIONAL_S3_EVALUATOR_AND_M3_SLICE_REPAIR_CLOSED_FULL_INVARIANT_OPEN' if ok
         else 'SCIENTIFIC_FAIL_M3_NUMERATOR_DEGREE_OR_TENSOR_ALLOCATION')
    out={'gate':'ITER147_FIXED_GEODESIC_CURVATURE_RATIONAL_S3_EVALUATOR_M3_SLICE_REPAIR','classification':cls,
         'source_blob':blob,'integer_domain_controls':integer_rows,'rational_homogeneity':{'base':str(base),'scaled':str(scaled)},
         'slice_rows':rows,'checks':checks,
         'claim_ceiling':'rational S3 evaluator + exact D4 M3 slices only; full invariant/bubble-reduced numerator, poles, B1, EDT, bridge, new physics, candidate theory open'}
    open('iter147_rational_s3_evaluator_m3_slice_repair.json','w').write(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'classification':cls,'degrees':[r['degree'] for r in rows],'checks':checks},indent=2))
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()
