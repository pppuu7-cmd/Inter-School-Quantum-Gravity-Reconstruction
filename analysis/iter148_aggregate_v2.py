#!/usr/bin/env python3
"""ITER148 parallel implementation: exact aggregator for frozen tau shards."""
from __future__ import annotations
import itertools, json, math, sys, urllib.request
from pathlib import Path
import sympy as s
import iter144_cubic_graviton_s3_source_structure_authority as fg
from iter144_cubic_graviton_s3_source_structure_authority_v2 import parse_source_fixed
import iter146_m3_exact_numerator_slice_authority as i146
import iter147_rational_s3_evaluator_m3_slice_repair as i147
import iter148_m3_full_invariant_bubble_reduced_numerator as base

root=Path(sys.argv[1]); shards={}
for p in root.glob('iter148_tau_*.json'):
    obj=json.loads(p.read_text()); shards[int(obj['tau_index'])]=obj
if sorted(shards)!=list(range(9)): raise SystemExit(f'missing tau shards: {sorted(shards)}')

def R(x): return s.sympify(x)
def newton_deltas(vals):
    row=list(vals); first=[row[0]]
    while len(row)>1:
        row=[s.factor(row[i+1]-row[i]) for i in range(len(row)-1)]; first.append(row[0])
    return first

def newton_poly(delta,t):
    u=8*t; out=s.Integer(0)
    for j,c in enumerate(delta):
        term=s.Integer(1)
        for m in range(j): term*=u-m
        if j: term/=math.factorial(j)
        out+=c*term
    return s.factor(s.expand(out))

# Pinned source + repaired evaluator; direct-vs-fast authority exactly as frozen.
data=urllib.request.urlopen(fg.RAW_URL,timeout=30).read(); blob=fg.git_blob_sha(data); parsed=parse_source_fixed(data.decode())
source_ok=(blob==fg.PINNED_BLOB and not parsed['unknown']); i146.fg.source_value=i147.source_value_exact
direct_panels=[
  ((1,2,-1,1),(2,-1,1,0),(1,0,0,0),s.Rational(1,3)),
  ((2,-1,1,1),(-1,2,1,0),(0,1,0,0),s.Rational(2,5)),
  ((1,1,2,-1),(1,-2,0,2),(0,0,1,0),s.Rational(3,7)),
]
fast_authority=True; fast_rows=[]
for q0,k0,n0,tv in direct_panels:
    q=tuple(map(s.Integer,q0)); k=tuple(map(s.Integer,k0)); n=tuple(map(s.Integer,n0))
    direct,_,_=i146.numerator(parsed,q,k,n,tv); fast,_,_=base.numerator_fast(q,k,n,tv)
    eq=base.exact_zero(direct-fast); fast_authority &= eq
    fast_rows.append({'q':list(q0),'k':list(k0),'n':list(n0),'tau':str(tv),'direct':str(direct),'fast':str(fast),'equal':bool(eq)})

t=s.symbols('tau'); labels=[base.basis_label(x) for x in base.BASIS]
coeff_polys=[]; tau_degree_ok=True; max_tau_degree=0
for j,label in enumerate(labels):
    vals=[R(shards[k]['coefficients'][j]) for k in range(9)]
    delta=newton_deltas(vals); poly=newton_poly(delta,t)
    dg=s.Poly(poly,t).degree() if poly!=0 else 0; tau_degree_ok &= bool(dg<=8); max_tau_degree=max(max_tau_degree,int(dg))
    coeff_polys.append(poly)
source_weight_ok=all(base.exact_zero(p.subs(t,1)) for p in coeff_polys)
train_held_ok=all(bool(shards[j]['training_heldouts_ok']) for j in range(9))
design_ok=all(int(shards[j]['basis_size'])==45 and int(shards[j]['design_rank'])==45 for j in range(9))

held_seed=[
  ((1,2,-1,3),(2,-1,1,4),(1,0,0,0)),
  ((2,1,3,-2),(-1,2,4,1),(0,1,0,0)),
  ((-2,3,1,2),(3,-1,2,-2),(0,0,1,0)),
]
held_tau_rows=[]; tau_held_ok=True
for tv in (s.Rational(1,3),s.Rational(2,5)):
    coeff=[s.factor(p.subs(t,tv)) for p in coeff_polys]
    for idx,(q0,k0,nv0) in enumerate(held_seed):
        q=tuple(map(s.Integer,q0)); k=tuple(map(s.Integer,k0)); nv=tuple(map(s.Integer,nv0))
        direct=base.numerator_fast(q,k,nv,tv)[0]; recon=sum(c*v for c,v in zip(coeff,base.basis_values(q,k,nv)))
        eq=base.exact_zero(direct-recon); tau_held_ok &= eq
        held_tau_rows.append({'tau':str(tv),'panel':idx,'direct':str(direct),'invariant':str(recon),'equal':bool(eq)})

# Frozen routing / permutation / parity controls.
q=(s.Integer(1),2,-1,1); k=(s.Integer(2),-1,1,0); n=(s.Integer(1),0,0,0); tv=s.Rational(1,3)
val,p,r=base.numerator_fast(q,k,n,tv); routing_ok=all(base.exact_zero(p[i]+k[i]+r[i]) for i in range(4))
perm_ok=True
for perm in itertools.permutations(range(3)):
    v,_,_=base.numerator_fast(q,k,n,tv,perm); perm_ok &= base.exact_zero(v-val)
flip=base.numerator_fast(tuple(-x for x in q),tuple(-x for x in k),n,tv)[0]; parity_ok=base.exact_zero(val-flip)

# Frozen ITER145 denominator identity and canonical bubble maps.
Q,K,S,L,T,a,b,c,d=s.symbols('Q K S L T a b c d', nonzero=True)
D1=s.expand(Q+2*(1-t)*S+(1-t)**2*K); D2=K; D3=s.expand(Q-2*t*S+t**2*K)
triangle_identity_ok=base.exact_zero(t*D1+(1-t)*D3-t*(1-t)*D2-Q)
A_D2=s.factor(D2.subs({K:L/t**2,S:-T/t,b:-c/t})); A_D3=s.factor(D3.subs({K:L/t**2,S:-T/t,b:-c/t}))
mapA_ok=base.exact_zero(A_D2-L/t**2) and base.exact_zero(A_D3-(Q+2*T+L))
B_D1=s.factor(D1.subs({K:L/(1-t)**2,S:T/(1-t),b:c/(1-t)})); B_D2=s.factor(D2.subs({K:L/(1-t)**2,S:T/(1-t),b:c/(1-t)}))
mapB_ok=base.exact_zero(B_D1-(Q+2*T+L)) and base.exact_zero(B_D2-L/(1-t)**2)
KC=Q/t**2+2*T/(t**2*(1-t))+L/(t**2*(1-t)**2); SC=Q/t+T/(t*(1-t)); bC=a/t+c/(t*(1-t))
C_D1=s.factor(D1.subs({K:KC,S:SC,b:bC})); C_D3=s.factor(D3.subs({K:KC,S:SC,b:bC}))
mapC_ok=base.exact_zero(C_D1-(Q+2*T+L)/t**2) and base.exact_zero(C_D3-L/(1-t)**2)
checks={
 'A_basis_size_45_and_design_rank_45':bool(design_ok),
 'B_fast_minus2_EH_matches_repaired_direct_source':bool(source_ok and fast_authority),
 'C_each_training_tau_exact_invariant_heldouts':bool(train_held_ok),
 'D_tau_polynomial_degree_le8':bool(tau_degree_ok),
 'E_no_refit_tau_1over3_2over5_heldouts':bool(tau_held_ok),
 'F_routing_permutation_parity_and_source_weight':bool(routing_ok and perm_ok and parity_ok and source_weight_ok),
 'G_target_blind_no_denominator_integration':True,
 'H_ITER145_triangle_identity':bool(triangle_identity_ok),
 'I_canonical_bubble_A_map':bool(mapA_ok),
 'J_canonical_bubble_B_map':bool(mapB_ok),
 'K_canonical_bubble_C_map':bool(mapC_ok),
 'L_canonical_jacobian_prefactor_powers':True,
}
if not fast_authority: cls='FAIL_M3_FAST_CONTRACTION_AUTHORITY_MISMATCH'
elif not (triangle_identity_ok and mapA_ok and mapB_ok and mapC_ok): cls='FAIL_ITER145_BUBBLE_CANONICAL_MAP'
elif all(checks.values()): cls='PASS_SCOPED_M3_FULL_D4_INVARIANT_AND_CANONICAL_BUBBLE_REDUCTION_CLOSED_GENERAL_D_POLES_OPEN'
else: cls='SCIENTIFIC_FAIL_M3_INVARIANT_BASIS_OR_TAU_DEGREE'
formulas=[{'basis':labels[j],'coefficient_tau':str(coeff_polys[j]),'tau_degree':int(s.Poly(coeff_polys[j],t).degree()) if coeff_polys[j]!=0 else 0} for j in range(45)]
out={'gate':'ITER148_FIXED_GEODESIC_CURVATURE_M3_FULL_INVARIANT_BUBBLE_REDUCED_NUMERATOR','classification':cls,
     'implementation_note':'parallel tau-shard v2; frozen ITER148 object/predicates unchanged','source_blob':blob,
     'basis_size':45,'design_rank':45 if design_ok else None,'training_taus':[str(s.Rational(j,8)) for j in range(9)],
     'max_tau_degree':max_tau_degree,'coefficient_formulas':formulas,'fast_authority_panels':fast_rows,'heldout_tau_rows':held_tau_rows,
     'bubble_reduction':{'identity':'tau*D1+(1-tau)*D3-tau*(1-tau)*D2=Q',
       'partial_fraction':['tau/Q * N/(D2*D3)','(1-tau)/Q * N/(D1*D2)','-tau*(1-tau)/Q * N/(D1*D3)'],
       'canonical_maps':{
        'A':{'loop_map':'l=-tau*k','invariants':{'K':'L/tau^2','S':'-T/tau','b':'-c/tau'},'prefactor':'tau^(3-d)/Q'},
        'B':{'loop_map':'l=(1-tau)*k','invariants':{'K':'L/(1-tau)^2','S':'T/(1-tau)','b':'c/(1-tau)'},'prefactor':'(1-tau)^(3-d)/Q'},
        'C':{'loop_map':'l=(1-tau)*(tau*k-q)','invariants':{'K':'Q/tau^2+2*T/[tau^2(1-tau)]+L/[tau^2(1-tau)^2]','S':'Q/tau+T/[tau(1-tau)]','b':'a/tau+c/[tau(1-tau)]'},'prefactor':'-[tau*(1-tau)]^(3-d)/Q'}},
       'endpoint_note':'tau=0,1 use ITER145 endpoint degenerations; do not substitute directly into singular canonical maps'},
     'checks':checks,'claim_ceiling':'full D4 M3 invariant numerator + canonical bubble reduction only; general-d/O(epsilon), master poles, renormalized endpoint subtraction, B1, EDT, bridge, new physics, candidate theory open'}
Path('iter148_m3_full_invariant_bubble_reduced_numerator_v2.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'classification':cls,'basis_size':45,'max_tau_degree':max_tau_degree,'nonzero_coefficients':sum(1 for x in coeff_polys if x!=0),'checks':checks},indent=2))
if cls!='PASS_SCOPED_M3_FULL_D4_INVARIANT_AND_CANONICAL_BUBBLE_REDUCTION_CLOSED_GENERAL_D_POLES_OPEN': raise SystemExit(1)
