#!/usr/bin/env python3
import json,sys
from pathlib import Path
import sympy as s
import iter148_m3_full_invariant_bubble_reduced_numerator as base

p=Path(sys.argv[1]); o=json.loads(p.read_text())
expected='PASS_SCOPED_M3_FULL_D4_INVARIANT_AND_CANONICAL_BUBBLE_REDUCTION_CLOSED_GENERAL_D_POLES_OPEN'
if o.get('classification')!=expected or o.get('basis_size')!=45 or o.get('scientific_predicates_changed') is not False:
    raise SystemExit('invalid frozen ITER148 authority payload')
forms=o['coefficient_formulas']
if len(forms)!=45: raise SystemExit('invalid coefficient formula count')
t=s.symbols('tau')
coeff_polys=[s.sympify(r['coefficient_tau']) for r in forms]
# Frozen before production by prereg/ITER149_ITER148_NO_REFIT_TAU_TRANSPORT.md
taus=[s.Rational(3,10),s.Rational(5,12),s.Rational(7,13)]
panels=[
 ((3,-2,1,2),(1,3,-2,1),(1,0,0,0)),
 ((-1,2,4,-2),(2,-3,1,3),(0,1,0,0)),
 ((2,3,-1,4),(-2,1,3,-1),(0,0,1,0)),
 ((4,-1,2,1),(1,2,-3,2),(0,0,0,1)),
]
rows=[]; ok=True
for tv in taus:
    coeff=[s.factor(x.subs(t,tv)) for x in coeff_polys]
    for i,(q0,k0,n0) in enumerate(panels):
        q=tuple(map(s.Integer,q0)); k=tuple(map(s.Integer,k0)); n=tuple(map(s.Integer,n0))
        direct=base.numerator_fast(q,k,n,tv)[0]
        recon=s.factor(sum(c*v for c,v in zip(coeff,base.basis_values(q,k,n))))
        eq=base.exact_zero(direct-recon); ok &= bool(eq)
        rows.append({'tau':str(tv),'panel':i,'equal':bool(eq),'difference':str(s.factor(direct-recon))})
        print(json.dumps(rows[-1]),flush=True)
cls='PASS_SCOPED_ITER148_NO_REFIT_TAU_TRANSPORT_HELDOUTS' if ok else 'SCIENTIFIC_FAIL_ITER148_NO_REFIT_TAU_TRANSPORT'
out={'gate':'ITER149_ITER148_NO_REFIT_TAU_TRANSPORT','classification':cls,'source_run':35044099632,'source_artifact':10431996892,'refit':False,'heldout_taus':[str(x) for x in taus],'rows':rows,'checks':{'A_authoritative_payload':True,'B_basis45_frozen':True,'C_all_12_exact':bool(ok),'D_no_refit':True,'E_target_blind':True},'claim_ceiling':'D4 numerator no-refit tau transport only; general-D poles, endpoint subtraction, bridge, new physics and candidate theory open'}
Path('iter149_no_refit_tau_transport.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'classification':cls,'checks':out['checks']},indent=2))
if not ok: raise SystemExit(2)
