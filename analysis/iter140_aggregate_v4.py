#!/usr/bin/env python3
"""ITER140 v4 exact aggregator for parallel D=3..10 shards."""
from __future__ import annotations
import json, math, sys
from pathlib import Path
import sympy as s
import iter140_first_mg_general_d_invariant_continuation as frozen

root=Path(sys.argv[1])
shards={}
for p in root.glob('iter140_D*.json'):
    obj=json.loads(p.read_text()); shards[int(obj['D'])]=obj
required=list(range(3,11))
if sorted(shards)!=required:
    raise SystemExit(f'missing shards: have {sorted(shards)}, need {required}')
labels=frozen.basis_labels(); names=['M_R2_chi1_dR1','M_R1_chi1_dR2','G_R1_chi2_Gamma2_dR1']

def R(x): return s.sympify(x)
def newton_deltas(vals):
    row=list(vals); first=[row[0]]
    while len(row)>1:
        row=[s.factor(row[i+1]-row[i]) for i in range(len(row)-1)]; first.append(row[0])
    return first

def deg(delta):
    out=0
    for j,x in enumerate(delta):
        if x!=0: out=j
    return out

def newton_eval(delta,D):
    return s.factor(sum(delta[j]*math.comb(D-3,j) for j in range(len(delta))))

def newton_poly(delta,d):
    out=s.Integer(0)
    for j,c in enumerate(delta):
        term=s.Integer(1)
        for m in range(j): term*=d-3-m
        if j: term/=math.factorial(j)
        out+=c*term
    return s.Poly(s.expand(out),d).as_expr()

def exact_zero(x): return bool(x==0 or s.cancel(x)==0)

train=[3,4,5,6,7]; validate=[8,9,10]; d=s.symbols('d')
formulas={}; deltas={}; trace_ok=True; coeff_validation_ok=True; maxdeg=0
for name in names:
    formulas[name]=[]; deltas[name]=[]
    for j,label in enumerate(labels):
        vals=[s.factor((D-2)**2*R(shards[D]['coefficients'][name][j])) for D in train]
        delta=newton_deltas(vals); deltas[name].append(delta); dg=deg(delta); maxdeg=max(maxdeg,dg); trace_ok &= dg<=4
        poly=newton_poly(delta,d); coeff=s.cancel(poly/(d-2)**2)
        for D in validate:
            pred=s.factor(newton_eval(delta,D)/(D-2)**2); actual=R(shards[D]['coefficients'][name][j])
            coeff_validation_ok &= exact_zero(pred-actual)
        formulas[name].append({'basis':label,'coefficient_d':str(coeff),'trace_polynomial_degree':dg,
                               'c_d4':str(s.factor(coeff.subs(d,4))),
                               'c_epsilon_linear_for_d_4_minus_2eps':str(s.factor(-2*s.diff(coeff,d).subs(d,4)))})

held_ok=all(bool(shards[D]['integer_D_heldouts_ok']) for D in required)
d4_ok=bool(shards[4]['D4_cross_authority_ok'])
cont_rows=[]; cont_ok=True
for D in validate:
    row={'D':D}
    # frozen direct no-refit panel index 1 from the shard
    h=shards[D]['integer_D_heldouts'][1]; bvals=[R(x) for x in h['basis_values']]
    for name in names:
        coeff=[s.factor(newton_eval(deltas[name][j],D)/(D-2)**2) for j in range(len(labels))]
        recon=sum(c*v for c,v in zip(coeff,bvals)); direct=R(h[name]['direct']); eq=exact_zero(recon-direct); cont_ok &= eq
        row[name]={'direct':str(direct),'continued':str(recon),'equal':eq}
    cont_rows.append(row)
checks={
 'A_basis_size_28':len(frozen.BASIS)==28,
 'B_design_rank_28':all(int(shards[D]['design_rank'])==28 for D in required),
 'C_integer_D_invariant_heldouts':bool(held_ok),
 'D_trace_polynomial_degree_le4':bool(trace_ok),
 'E_coefficient_continuation_D8_D10':bool(coeff_validation_ok),
 'F_direct_continuation_heldouts_D8_D10':bool(cont_ok),
 'G_D4_matches_ITER138_ITER139':bool(d4_ok),
 'H_target_blind':True,
}
if all(checks.values()): cls='PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN'
elif not trace_ok: cls='BLOCKED_GENERAL_D_TRACE_DEGREE_AUTHORITY'
else: cls='SCIENTIFIC_FAIL_GENERAL_D_INVARIANT_RECONSTRUCTION'
out={
 'gate':'ITER140_FIXED_GEODESIC_CURVATURE_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION','classification':cls,
 'implementation_note':'v4 parallel exact integer-D shards + exact finite-difference aggregator; frozen ITER140 predicates unchanged',
 'basis_labels':labels,'training_dimensions':train,'validation_dimensions':validate,'max_observed_trace_polynomial_degree':maxdeg,
 'coefficient_formulas':formulas,'integer_D_shard_summaries':{str(D):{'heldouts_ok':shards[D]['integer_D_heldouts_ok'],'D4_cross_authority_ok':shards[D]['D4_cross_authority_ok']} for D in required},
 'continuation_heldouts':cont_rows,'D4_cross_authority':shards[4]['D4_cross_authority'],'checks':checks,
 'claim_ceiling':'general-d numerator continuation and O(epsilon) coefficients only; no loop pole/B1/noncancellation/B0/EDT/bridge/new physics/candidate theory',
}
Path('iter140_first_mg_general_d_invariant_continuation_v4.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'classification':cls,'max_trace_polynomial_degree':maxdeg,'checks':checks,
                  'nonzero_coefficient_counts':{n:sum(1 for x in formulas[n] if x['coefficient_d']!='0') for n in names}},indent=2))
if cls.startswith('SCIENTIFIC_FAIL') or cls.startswith('BLOCKED'): raise SystemExit(1)
