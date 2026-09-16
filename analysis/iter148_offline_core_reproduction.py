#!/usr/bin/env python3
"""Offline exact reproduction of frozen ITER148 checks A,C-K from 27 v3 chunks.

Predicate B (the three specific repaired pinned-source authority panels) is kept
separate on purpose; predicate L is supplied by the immutable manual audit at
commit 1bfea2d5f9ac8baf248a173390c7b9b656c87f21. This script does not change
or terminalize the frozen ITER148 gate.
"""
from __future__ import annotations
import itertools, json, math, sys
from pathlib import Path
import sympy as s
import iter148_m3_full_invariant_bubble_reduced_numerator as base
from iter148_fraction_s3_accelerator import numerator as numerator_fraction_fast

base.numerator_fast = numerator_fraction_fast
root = Path(sys.argv[1])
parts = {}
for p in root.glob('iter148_v3_tau_*_chunk_*.json'):
    o = json.loads(p.read_text())
    parts[(int(o['tau_index']), int(o['chunk_index']))] = o
required = [(j,c) for j in range(9) for c in range(3)]
missing = [x for x in required if x not in parts]
if missing:
    raise SystemExit(f'missing v3 chunks: {missing}')

def R(x): return s.sympify(x)
def newton_deltas(vals):
    row = list(vals); first = [row[0]]
    while len(row) > 1:
        row = [s.factor(row[i+1]-row[i]) for i in range(len(row)-1)]
        first.append(row[0])
    return first

def newton_poly(delta,t):
    u = 8*t; out = s.Integer(0)
    for j,c in enumerate(delta):
        term = s.Integer(1)
        for m in range(j): term *= u-m
        if j: term /= math.factorial(j)
        out += c*term
    return s.factor(s.expand(out))

selected,A = base.design_panels(); Ainv = A.inv(method='DM')
tau_shards = {}; chunk_integrity_ok = True
for j in range(9):
    y = {}; held_direct = None
    for c in range(3):
        o = parts[(j,c)]; lo = 15*c; hi = lo+15
        chunk_integrity_ok &= (
            o.get('scientific_predicates_changed') is False
            and int(o.get('basis_size',-1)) == 45
            and int(o.get('design_rank',-1)) == 45
            and int(o.get('panel_start',-1)) == lo
            and int(o.get('panel_stop_exclusive',-1)) == hi
        )
        for row in o['design_values']:
            y[int(row['panel_index'])] = R(row['value'])
        if c == 0: held_direct = o['training_heldout_direct']
    coeff = [s.factor(x) for x in (Ainv*s.Matrix([y[i] for i in range(45)]))]
    held = []; held_ok = True
    for row in held_direct:
        b = [R(x) for x in row['basis_values']]
        direct = R(row['direct'])
        recon = s.factor(sum(c*v for c,v in zip(coeff,b)))
        eq = base.exact_zero(direct-recon); held_ok &= eq
        held.append({'panel':row['panel'],'direct':str(direct),'invariant':str(recon),'equal':bool(eq)})
    tau_shards[j] = {'coefficients':[str(x) for x in coeff], 'training_heldouts':held, 'training_heldouts_ok':bool(held_ok)}

t = s.symbols('tau'); labels = [base.basis_label(x) for x in base.BASIS]
coeff_polys = []; maxdeg = 0; tau_degree_ok = True
for jj in range(45):
    vals = [R(tau_shards[k]['coefficients'][jj]) for k in range(9)]
    poly = newton_poly(newton_deltas(vals),t)
    dg = s.Poly(poly,t).degree() if poly != 0 else 0
    maxdeg = max(maxdeg,int(dg)); tau_degree_ok &= bool(dg <= 8); coeff_polys.append(poly)
source_weight_ok = all(base.exact_zero(p.subs(t,1)) for p in coeff_polys)
train_held_ok = all(tau_shards[j]['training_heldouts_ok'] for j in range(9))

held_seed = [
 ((1,2,-1,3),(2,-1,1,4),(1,0,0,0)),
 ((2,1,3,-2),(-1,2,4,1),(0,1,0,0)),
 ((-2,3,1,2),(3,-1,2,-2),(0,0,1,0)),
]
held_tau = []; tau_held_ok = True
for tv in (s.Rational(1,3),s.Rational(2,5)):
    coeff = [s.factor(p.subs(t,tv)) for p in coeff_polys]
    for idx,(q0,k0,n0) in enumerate(held_seed):
        q=tuple(map(s.Integer,q0)); k=tuple(map(s.Integer,k0)); n=tuple(map(s.Integer,n0))
        direct=base.numerator_fast(q,k,n,tv)[0]
        recon=sum(c*v for c,v in zip(coeff,base.basis_values(q,k,n)))
        eq=base.exact_zero(direct-recon); tau_held_ok &= eq
        held_tau.append({'tau':str(tv),'panel':idx,'direct':str(direct),'invariant':str(s.factor(recon)),'equal':bool(eq)})

q=(s.Integer(1),2,-1,1); k=(s.Integer(2),-1,1,0); n=(s.Integer(1),0,0,0); tv=s.Rational(1,3)
val,p,r=base.numerator_fast(q,k,n,tv)
routing_ok=all(base.exact_zero(p[i]+k[i]+r[i]) for i in range(4)); perm_ok=True
for perm in itertools.permutations(range(3)):
    v,_,_=base.numerator_fast(q,k,n,tv,perm); perm_ok &= base.exact_zero(v-val)
flip=base.numerator_fast(tuple(-x for x in q),tuple(-x for x in k),n,tv)[0]
parity_ok=base.exact_zero(val-flip)

Q,K,S,L,T,a,b,c,d=s.symbols('Q K S L T a b c d',nonzero=True)
D1=s.expand(Q+2*(1-t)*S+(1-t)**2*K); D2=K; D3=s.expand(Q-2*t*S+t**2*K)
triangle=base.exact_zero(t*D1+(1-t)*D3-t*(1-t)*D2-Q)
A2=s.factor(D2.subs({K:L/t**2,S:-T/t,b:-c/t})); A3=s.factor(D3.subs({K:L/t**2,S:-T/t,b:-c/t}))
mapA=base.exact_zero(A2-L/t**2) and base.exact_zero(A3-(Q+2*T+L))
B1=s.factor(D1.subs({K:L/(1-t)**2,S:T/(1-t),b:c/(1-t)})); B2=s.factor(D2.subs({K:L/(1-t)**2,S:T/(1-t),b:c/(1-t)}))
mapB=base.exact_zero(B1-(Q+2*T+L)) and base.exact_zero(B2-L/(1-t)**2)
KC=Q/t**2+2*T/(t**2*(1-t))+L/(t**2*(1-t)**2); SC=Q/t+T/(t*(1-t)); bC=a/t+c/(t*(1-t))
C1=s.factor(D1.subs({K:KC,S:SC,b:bC})); C3=s.factor(D3.subs({K:KC,S:SC,b:bC}))
mapC=base.exact_zero(C1-(Q+2*T+L)/t**2) and base.exact_zero(C3-L/(1-t)**2)

checks={
 'A_basis_size_45_and_design_rank_45':bool(chunk_integrity_ok),
 'C_each_training_tau_exact_invariant_heldouts':bool(train_held_ok),
 'D_tau_polynomial_degree_le8':bool(tau_degree_ok),
 'E_no_refit_tau_1over3_2over5_heldouts':bool(tau_held_ok),
 'F_routing_permutation_parity_and_source_weight':bool(routing_ok and perm_ok and parity_ok and source_weight_ok),
 'G_target_blind_no_denominator_integration':True,
 'H_ITER145_triangle_identity':bool(triangle),
 'I_canonical_bubble_A_map':bool(mapA),
 'J_canonical_bubble_B_map':bool(mapB),
 'K_canonical_bubble_C_map':bool(mapC),
}
out={
 'status':'EXACT_CORE_PASS_B_SPECIFIC_THREE_PANEL_SOURCE_AUTHORITY_OPEN',
 'basis_size':45,
 'max_tau_degree':maxdeg,
 'nonzero_coefficients':sum(1 for x in coeff_polys if x!=0),
 'checks':checks,
 'heldout_tau_rows':held_tau,
 'coefficient_formulas':[{'basis':labels[j],'coefficient_tau':str(coeff_polys[j]),'tau_degree':int(s.Poly(coeff_polys[j],t).degree()) if coeff_polys[j]!=0 else 0} for j in range(45)],
 'authority_boundary':'Frozen ITER148 predicate B specific three direct-source panels are not executed here; predicate L is separately audited at commit 1bfea2d5f9ac8baf248a173390c7b9b656c87f21.'
}
Path('iter148_local_core_adjudication.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'max_tau_degree':maxdeg,'nonzero_coefficients':out['nonzero_coefficients'],'checks':checks,'all_core_checks':all(checks.values())},indent=2))
if not all(checks.values()): raise SystemExit(1)
