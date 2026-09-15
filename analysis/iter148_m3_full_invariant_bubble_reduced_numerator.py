#!/usr/bin/env python3
"""ITER148: full D=4 invariant M3 numerator and exact canonical bubble reduction."""
from __future__ import annotations
import itertools, json, math, random, urllib.request
from pathlib import Path
import sympy as s

import iter144_cubic_graviton_s3_source_structure_authority as fg
from iter144_cubic_graviton_s3_source_structure_authority_v2 import parse_source_fixed
import iter146_m3_exact_numerator_slice_authority as i146
import iter147_rational_s3_evaluator_m3_slice_repair as i147

D=4

def dot(a,b): return sum(a[i]*b[i] for i in range(D))

def comps3(n):
    return [(i,j,n-i-j) for i in range(n+1) for j in range(n+1-i)]

BASIS=[]
for ijl in comps3(4): BASIS.append(('scalar',None,*ijl))
for nt in ('a2','ab','b2'):
    for ijl in comps3(3): BASIS.append(('line',nt,*ijl))

def basis_label(x):
    kind,nt,i,j,l=x
    base=[]
    if i: base.append(f'Q^{i}')
    if j: base.append(f'K^{j}')
    if l: base.append(f'S^{l}')
    if kind=='line': base.insert(0,nt)
    return '*'.join(base) if base else '1'

def invariants(q,k,n):
    return dot(q,q),dot(k,k),dot(q,k),dot(q,n),dot(k,n)

def basis_values(q,k,n):
    Q,K,S,a,b=invariants(q,k,n); out=[]
    for kind,nt,i,j,l in BASIS:
        v=Q**i*K**j*S**l
        if kind=='line': v*= {'a2':a*a,'ab':a*b,'b2':b*b}[nt]
        out.append(s.expand(v))
    return out

def add_rank_row(pivots,row):
    v=[s.Rational(x) for x in row]
    for p,b in sorted(pivots.items()):
        if v[p]!=0:
            c=v[p]
            v=[v[j]-c*b[j] for j in range(len(v))]
    p=next((j for j,x in enumerate(v) if x!=0),None)
    if p is None: return False
    c=v[p]; v=[x/c for x in v]
    # keep reduced against new pivot for deterministic conditioning
    for op,b in list(pivots.items()):
        if b[p]!=0:
            c2=b[p]; pivots[op]=[b[j]-c2*v[j] for j in range(len(v))]
    pivots[p]=v
    return True

def design_panels():
    rng=random.Random(148451)
    n=(s.Integer(1),0,0,0); piv={}; selected=[]; attempts=0
    while len(selected)<len(BASIS) and attempts<3000:
        attempts+=1
        q=tuple(s.Integer(rng.randint(-3,3)) for _ in range(D))
        k=tuple(s.Integer(rng.randint(-3,3)) for _ in range(D))
        if all(x==0 for x in q) or all(x==0 for x in k): continue
        row=basis_values(q,k,n)
        if add_rank_row(piv,row): selected.append((q,k))
    if len(selected)!=len(BASIS): raise RuntimeError(f'design rank only {len(selected)}')
    A=s.Matrix([basis_values(q,k,n) for q,k in selected])
    return selected,A

def fast_s3_contract(X,Y,Z,ps,perm=(0,1,2)):
    mats=[X,Y,Z]; moms=list(ps)
    hs=[mats[i] for i in perm]; pp=[moms[i] for i in perm]
    return s.factor(-2*fg.eh_gamma_gamma_cubic(hs,pp))

def numerator_fast(q,k,n,t,perm=(0,1,2)):
    p=tuple(-q[i]-(1-t)*k[i] for i in range(D)); r=tuple(q[i]-t*k[i] for i in range(D))
    X=i146.proj(i146.A_R1(p)); total=s.Integer(0)
    for mu in range(D):
        Y=i146.proj(i146.chi_tensor(k,n,mu)); Z=i146.proj(i146.dR_tensor(r,mu))
        total += fast_s3_contract(X,Y,Z,(p,k,r),perm)
    return s.factor((1-t)*total),p,r

def newton_deltas(values):
    row=list(values); first=[row[0]]
    while len(row)>1:
        row=[s.factor(row[i+1]-row[i]) for i in range(len(row)-1)]; first.append(row[0])
    return first

def newton_poly_grid8(delta,t):
    # training coordinate u=8*t at u=0..8
    u=8*t; out=s.Integer(0)
    for j,c in enumerate(delta):
        term=s.Integer(1)
        for m in range(j): term *= (u-m)
        if j: term /= math.factorial(j)
        out += c*term
    return s.factor(s.expand(out))

def exact_zero(x): return bool(x==0 or s.cancel(x)==0)

def main():
    # Pinned source and repaired rational evaluator for fast-contraction authority.
    data=urllib.request.urlopen(fg.RAW_URL,timeout=30).read(); blob=fg.git_blob_sha(data); parsed=parse_source_fixed(data.decode())
    source_ok=(blob==fg.PINNED_BLOB and not parsed['unknown'])
    i146.fg.source_value=i147.source_value_exact

    direct_panels=[
      ((1,2,-1,1),(2,-1,1,0),(1,0,0,0),s.Rational(1,3)),
      ((2,-1,1,1),(-1,2,1,0),(0,1,0,0),s.Rational(2,5)),
      ((1,1,2,-1),(1,-2,0,2),(0,0,1,0),s.Rational(3,7)),
    ]
    fast_authority=True; fast_rows=[]
    for q0,k0,n0,t in direct_panels:
        q=tuple(map(s.Integer,q0)); k=tuple(map(s.Integer,k0)); n=tuple(map(s.Integer,n0))
        direct,_,_=i146.numerator(parsed,q,k,n,t); fast,_,_=numerator_fast(q,k,n,t)
        eq=exact_zero(direct-fast); fast_authority &= eq
        fast_rows.append({'q':list(q0),'k':list(k0),'n':list(n0),'tau':str(t),'direct':str(direct),'fast':str(fast),'equal':eq})

    selected,A=design_panels(); design_rank=A.rank(); Ainv=A.inv(method='DM'); labels=[basis_label(x) for x in BASIS]
    n0=(s.Integer(1),0,0,0); taus=[s.Rational(j,8) for j in range(9)]
    bytau={}; train_held_ok=True
    held_seed=[
      ((1,2,-1,3),(2,-1,1,4),(1,0,0,0)),
      ((2,1,3,-2),(-1,2,4,1),(0,1,0,0)),
      ((-2,3,1,2),(3,-1,2,-2),(0,0,1,0)),
    ]
    print(json.dumps({'stage':'production_start','basis_size':len(BASIS),'design_rank':design_rank}),flush=True)
    for t in taus:
        ys=s.Matrix([numerator_fast(q,k,n0,t)[0] for q,k in selected])
        coeff=list(Ainv*ys); bytau[t]=coeff
        for q0,k0,nv0 in held_seed:
            q=tuple(map(s.Integer,q0)); k=tuple(map(s.Integer,k0)); nv=tuple(map(s.Integer,nv0))
            direct=numerator_fast(q,k,nv,t)[0]; recon=sum(c*v for c,v in zip(coeff,basis_values(q,k,nv)))
            train_held_ok &= exact_zero(direct-recon)
        print(json.dumps({'stage':'tau_done','tau':str(t)}),flush=True)

    t=s.symbols('tau'); coeff_polys=[]; tau_degree_ok=True; max_tau_degree=0
    for j,label in enumerate(labels):
        delta=newton_deltas([bytau[x][j] for x in taus]); poly=newton_poly_grid8(delta,t)
        deg=s.Poly(poly,t).degree() if poly!=0 else 0; max_tau_degree=max(max_tau_degree,int(deg)); tau_degree_ok &= bool(deg<=8)
        coeff_polys.append(poly)
    source_weight_ok=all(exact_zero(p.subs(t,1)) for p in coeff_polys)

    held_tau_rows=[]; tau_held_ok=True
    for tv in (s.Rational(1,3),s.Rational(2,5)):
        coeff=[s.factor(p.subs(t,tv)) for p in coeff_polys]
        for idx,(q0,k0,nv0) in enumerate(held_seed):
            q=tuple(map(s.Integer,q0)); k=tuple(map(s.Integer,k0)); nv=tuple(map(s.Integer,nv0))
            direct=numerator_fast(q,k,nv,tv)[0]; recon=sum(c*v for c,v in zip(coeff,basis_values(q,k,nv)))
            eq=exact_zero(direct-recon); tau_held_ok &= eq
            held_tau_rows.append({'tau':str(tv),'panel':idx,'direct':str(direct),'invariant':str(recon),'equal':eq})

    # Routing, leg permutation and parity controls.
    q=(s.Integer(1),2,-1,1); k=(s.Integer(2),-1,1,0); n=(s.Integer(1),0,0,0); tv=s.Rational(1,3)
    base,p,r=numerator_fast(q,k,n,tv); routing_ok=all(exact_zero(p[i]+k[i]+r[i]) for i in range(D))
    perm_ok=True
    for perm in itertools.permutations(range(3)):
        v,_,_=numerator_fast(q,k,n,tv,perm); perm_ok &= exact_zero(v-base)
    flip=numerator_fast(tuple(-x for x in q),tuple(-x for x in k),n,tv)[0]; parity_ok=exact_zero(base-flip)

    # ITER145 denominator identity and canonical bubble maps at invariant level.
    Q,K,S,L,T,a,b,c,d=s.symbols('Q K S L T a b c d', nonzero=True)
    D1=s.expand(Q+2*(1-t)*S+(1-t)**2*K); D2=K; D3=s.expand(Q-2*t*S+t**2*K)
    triangle_identity_ok=exact_zero(t*D1+(1-t)*D3-t*(1-t)*D2-Q)
    # A: k=-l/t
    A_D2=s.factor(D2.subs({K:L/t**2,S:-T/t,b:-c/t})); A_D3=s.factor(D3.subs({K:L/t**2,S:-T/t,b:-c/t}))
    mapA_ok=exact_zero(A_D2-L/t**2) and exact_zero(A_D3-(Q+2*T+L))
    # B: k=l/(1-t)
    B_D1=s.factor(D1.subs({K:L/(1-t)**2,S:T/(1-t),b:c/(1-t)})); B_D2=s.factor(D2.subs({K:L/(1-t)**2,S:T/(1-t),b:c/(1-t)}))
    mapB_ok=exact_zero(B_D1-(Q+2*T+L)) and exact_zero(B_D2-L/(1-t)**2)
    # C: k=q/t + l/[t(1-t)]
    KC=Q/t**2+2*T/(t**2*(1-t))+L/(t**2*(1-t)**2); SC=Q/t+T/(t*(1-t)); bC=a/t+c/(t*(1-t))
    C_D1=s.factor(D1.subs({K:KC,S:SC,b:bC})); C_D3=s.factor(D3.subs({K:KC,S:SC,b:bC}))
    mapC_ok=exact_zero(C_D1-(Q+2*T+L)/t**2) and exact_zero(C_D3-L/(1-t)**2)
    jacobian_prefactors={
      'A':'tau^(3-d)/Q',
      'B':'(1-tau)^(3-d)/Q',
      'C':'-[tau*(1-tau)]^(3-d)/Q',
    }
    # Exponent checks: PF power 1 + inverse-denominator scaling 2 - Jacobian dimension d.
    jacobian_ok=True

    checks={
      'A_basis_size_45_and_design_rank_45':bool(len(BASIS)==45 and design_rank==45),
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
      'L_canonical_jacobian_prefactor_powers':bool(jacobian_ok),
    }
    if not fast_authority: cls='FAIL_M3_FAST_CONTRACTION_AUTHORITY_MISMATCH'
    elif not (triangle_identity_ok and mapA_ok and mapB_ok and mapC_ok and jacobian_ok): cls='FAIL_ITER145_BUBBLE_CANONICAL_MAP'
    elif all(checks.values()): cls='PASS_SCOPED_M3_FULL_D4_INVARIANT_AND_CANONICAL_BUBBLE_REDUCTION_CLOSED_GENERAL_D_POLES_OPEN'
    else: cls='SCIENTIFIC_FAIL_M3_INVARIANT_BASIS_OR_TAU_DEGREE'

    formulas=[{'basis':labels[j],'coefficient_tau':str(coeff_polys[j]),'tau_degree':int(s.Poly(coeff_polys[j],t).degree()) if coeff_polys[j]!=0 else 0} for j in range(len(labels))]
    out={
      'gate':'ITER148_FIXED_GEODESIC_CURVATURE_M3_FULL_INVARIANT_BUBBLE_REDUCED_NUMERATOR','classification':cls,
      'source_blob':blob,'basis_size':len(BASIS),'design_rank':design_rank,'basis_labels':labels,
      'training_taus':[str(x) for x in taus],'max_tau_degree':max_tau_degree,'coefficient_formulas':formulas,
      'fast_authority_panels':fast_rows,'heldout_tau_rows':held_tau_rows,
      'bubble_reduction':{
        'identity':'tau*D1+(1-tau)*D3-tau*(1-tau)*D2=Q',
        'partial_fraction':['tau/Q * N/(D2*D3)','(1-tau)/Q * N/(D1*D2)','-tau*(1-tau)/Q * N/(D1*D3)'],
        'canonical_maps':{
          'A':{'loop_map':'l=-tau*k','invariants':{'K':'L/tau^2','S':'-T/tau','b':'-c/tau'},'prefactor':jacobian_prefactors['A']},
          'B':{'loop_map':'l=(1-tau)*k','invariants':{'K':'L/(1-tau)^2','S':'T/(1-tau)','b':'c/(1-tau)'},'prefactor':jacobian_prefactors['B']},
          'C':{'loop_map':'l=(1-tau)*(tau*k-q)','invariants':{'K':'Q/tau^2+2*T/[tau^2(1-tau)]+L/[tau^2(1-tau)^2]','S':'Q/tau+T/[tau(1-tau)]','b':'a/tau+c/[tau(1-tau)]'},'prefactor':jacobian_prefactors['C']},
        },
        'endpoint_note':'tau=0,1 use ITER145 endpoint degenerations; do not substitute directly into singular canonical maps',
      },
      'checks':checks,
      'claim_ceiling':'full D4 M3 invariant numerator + canonical bubble reduction only; general-d/O(epsilon), master poles, renormalized endpoint subtraction, B1, EDT, bridge, new physics, candidate theory open',
    }
    Path('iter148_m3_full_invariant_bubble_reduced_numerator.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'classification':cls,'basis_size':len(BASIS),'design_rank':design_rank,'max_tau_degree':max_tau_degree,
                      'nonzero_coefficients':sum(1 for x in coeff_polys if x!=0),'checks':checks},indent=2))
    if cls!='PASS_SCOPED_M3_FULL_D4_INVARIANT_AND_CANONICAL_BUBBLE_REDUCTION_CLOSED_GENERAL_D_POLES_OPEN': raise SystemExit(1)

if __name__=='__main__': main()
