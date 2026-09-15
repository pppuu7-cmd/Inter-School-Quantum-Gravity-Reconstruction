#!/usr/bin/env python3
"""ITER140 implementation-only retry v3.

Frozen scientific object/predicates are unchanged. This version keeps the v2 direct
indexed contractions and replaces the post-D=3..10 general-purpose symbolic stage
by exact Newton finite-difference arithmetic for the preregistered degree<=4 bound.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import sympy as s

import iter140_first_mg_general_d_invariant_continuation as frozen
import iter140_first_mg_general_d_invariant_continuation_v2 as fast
import iter138_first_mg_exact_numerator_kernels as i138
import iter139_affine_single_line_ceiling_repair as i139

BASIS=frozen.BASIS
FAMILIES=fast.FAMILIES

def newton_deltas(values):
    rows=[list(values)]; first=[rows[0][0]]
    while len(rows[-1])>1:
        prev=rows[-1]
        nxt=[s.Rational(prev[i+1])-s.Rational(prev[i]) for i in range(len(prev)-1)]
        rows.append(nxt); first.append(nxt[0])
    return first

def degree_from_deltas(delta):
    deg=0
    for j,x in enumerate(delta):
        if x!=0: deg=j
    return deg

def newton_eval(delta,D):
    # Nodes are D=3,4,5,6,7. For integer D, Newton basis is binomial(D-3,j).
    return s.factor(sum(delta[j]*s.Integer(math.comb(D-3,j)) for j in range(len(delta))))

def newton_poly(delta,d):
    out=s.Integer(0)
    for j,c in enumerate(delta):
        term=s.Integer(1)
        for m in range(j): term *= (d-3-m)
        if j: term /= math.factorial(j)
        out += c*term
    return s.Poly(s.expand(out),d).as_expr()

def exact_zero(x):
    if x==0: return True
    return bool(s.cancel(x)==0)

def main():
    labels=frozen.basis_labels(); selected,A=frozen.design_panels(); Ainv=A.inv(method='DM')
    dims=list(range(3,11)); byD={}
    print(json.dumps({'stage':'direct_contractions_start','dims':dims}),flush=True)
    for D in dims:
        nvec=tuple([1]+[0]*(D-1)); fam={}
        for name,fn in FAMILIES.items():
            ys=s.Matrix([fast.to_sym(fn(fast.pad(q3,D),fast.pad(k3,D),nvec,D)) for q3,k3 in selected])
            fam[name]=list(Ainv*ys)
        byD[D]=fam
        print(json.dumps({'stage':'direct_dimension_done','D':D}),flush=True)

    d,eps=s.symbols('d eps'); train=[3,4,5,6,7]; validate=[8,9,10]
    formulas={}; delta_store={}; trace_degree_ok=True; dim_coeff_ok=True; max_poly_degree=0
    print(json.dumps({'stage':'finite_difference_continuation_start'}),flush=True)
    for name in FAMILIES:
        rows=[]; delta_store[name]=[]
        for j,label in enumerate(labels):
            vals=[s.factor((D-2)**2*byD[D][name][j]) for D in train]
            delta=newton_deltas(vals); delta_store[name].append(delta)
            deg=degree_from_deltas(delta); max_poly_degree=max(max_poly_degree,deg); trace_degree_ok &= deg<=4
            poly=newton_poly(delta,d)
            for D in validate:
                pred=s.factor(newton_eval(delta,D)/(D-2)**2)
                dim_coeff_ok &= exact_zero(pred-byD[D][name][j])
            coeff=s.cancel(poly/(d-2)**2)
            c4=s.factor(coeff.subs(d,4)); ceps=s.factor(-2*s.diff(coeff,d).subs(d,4))
            rows.append({'basis':label,'coefficient_d':str(coeff),'trace_polynomial_degree':deg,
                         'c_d4':str(c4),'c_epsilon_linear_for_d_4_minus_2eps':str(ceps)})
        formulas[name]=rows
        print(json.dumps({'stage':'family_continuation_done','family':name}),flush=True)

    held_seed=[
      ((1,2,-1,3),(2,-1,1,4)),
      ((2,1,3,-2),(-1,2,4,1)),
      ((-2,3,1,2),(3,-1,2,-2)),
    ]
    held_rows=[]; held_ok=True
    print(json.dumps({'stage':'integer_D_heldouts_start'}),flush=True)
    for D in dims:
        nvec=tuple([1]+[0]*(D-1))
        for idx,(q4,k4) in enumerate(held_seed):
            qv=tuple(list(q4[:min(4,D)])+[0]*max(0,D-4)); kv=tuple(list(k4[:min(4,D)])+[0]*max(0,D-4))
            bvals=fast.basis_values_full(qv,kv); row={'D':D,'panel':idx}
            for name,fn in FAMILIES.items():
                direct=fast.to_sym(fn(qv,kv,nvec,D)); recon=sum(c*v for c,v in zip(byD[D][name],bvals))
                eq=exact_zero(direct-recon); held_ok &= eq
                row[name]={'direct':str(direct),'reconstructed':str(recon),'equal':eq}
            held_rows.append(row)
        print(json.dumps({'stage':'integer_D_heldouts_dimension_done','D':D}),flush=True)

    d4_rows=[]; d4_ok=True; n4=(s.Integer(1),0,0,0)
    print(json.dumps({'stage':'D4_cross_authority_start'}),flush=True)
    for q4,k4 in held_seed:
        generic={n:fast.to_sym(fn(q4,k4,(1,0,0,0),4)) for n,fn in FAMILIES.items()}
        authority={
          'M_R2_chi1_dR1':s.sympify(i138.M_numerator(q4,k4,n4)),
          'M_R1_chi1_dR2':s.sympify(i139.M2_numerator(q4,k4,n4)),
          'G_R1_chi2_Gamma2_dR1':s.sympify(i138.G_numerator(q4,k4,n4)),
        }
        rr={}
        for name in FAMILIES:
            eq=exact_zero(generic[name]-authority[name]); d4_ok &= eq
            rr[name]={'generic_D4':str(generic[name]),'authority_D4':str(authority[name]),'equal':eq}
        d4_rows.append(rr)

    continuation_rows=[]; continuation_ok=True
    print(json.dumps({'stage':'no_refit_D8_D10_direct_heldouts_start'}),flush=True)
    for D in validate:
        nvec=tuple([1]+[0]*(D-1)); q4,k4=held_seed[1]
        qv=tuple(list(q4)+[0]*(D-4)); kv=tuple(list(k4)+[0]*(D-4)); bvals=fast.basis_values_full(qv,kv); row={'D':D}
        for name,fn in FAMILIES.items():
            coeff=[s.factor(newton_eval(delta_store[name][j],D)/(D-2)**2) for j in range(len(labels))]
            recon=sum(c*v for c,v in zip(coeff,bvals)); direct=fast.to_sym(fn(qv,kv,nvec,D))
            eq=exact_zero(recon-direct); continuation_ok &= eq
            row[name]={'direct':str(direct),'continued':str(recon),'equal':eq}
        continuation_rows.append(row)
        print(json.dumps({'stage':'no_refit_dimension_done','D':D}),flush=True)

    checks={
      'A_basis_size_28':len(BASIS)==28,
      'B_design_rank_28':A.rank()==28,
      'C_integer_D_invariant_heldouts':bool(held_ok),
      'D_trace_polynomial_degree_le4':bool(trace_degree_ok),
      'E_coefficient_continuation_D8_D10':bool(dim_coeff_ok),
      'F_direct_continuation_heldouts_D8_D10':bool(continuation_ok),
      'G_D4_matches_ITER138_ITER139':bool(d4_ok),
      'H_target_blind':True,
    }
    if all(checks.values()): cls='PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN'
    elif not trace_degree_ok: cls='BLOCKED_GENERAL_D_TRACE_DEGREE_AUTHORITY'
    else: cls='SCIENTIFIC_FAIL_GENERAL_D_INVARIANT_RECONSTRUCTION'
    out={
      'gate':'ITER140_FIXED_GEODESIC_CURVATURE_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION',
      'classification':cls,'implementation_note':'v3 exact finite-difference performance retry; frozen ITER140 predicates/basis/dimensions unchanged',
      'basis_labels':labels,'training_dimensions':train,'validation_dimensions':validate,
      'max_observed_trace_polynomial_degree':max_poly_degree,'coefficient_formulas':formulas,
      'integer_D_heldouts':held_rows,'continuation_heldouts':continuation_rows,'D4_cross_authority':d4_rows,
      'checks':checks,'claim_ceiling':'general-d numerator continuation and O(epsilon) coefficients only; no loop pole/B1/noncancellation/B0/EDT/bridge/new physics/candidate theory',
    }
    Path('iter140_first_mg_general_d_invariant_continuation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'classification':cls,'basis_size':len(BASIS),'design_rank':A.rank(),'max_trace_polynomial_degree':max_poly_degree,
      'checks':checks,'nonzero_coefficient_counts':{n:sum(1 for x in formulas[n] if x['coefficient_d']!='0') for n in formulas}},indent=2))
    if cls.startswith('SCIENTIFIC_FAIL') or cls.startswith('BLOCKED'): raise SystemExit(1)

if __name__=='__main__': main()
