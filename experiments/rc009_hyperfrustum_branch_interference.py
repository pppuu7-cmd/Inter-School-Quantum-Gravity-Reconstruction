#!/usr/bin/env python3
"""RC-009 asymptotic hyperfrustum EPRL branch-interference audit.

Implements the shape-dependent oscillatory part of Bahr-Rabuffo-Steinhaus
arXiv:1804.00023v3 Eqs. (32),(35)-(39).  It tests whether the additional
Riemannian EPRL asymptotic branch can materially interfere with the
Regge/cosmological branch across source-admissible hyperfrustum shapes.

This is a local amplitude audit, NOT a reproduction of the coarse/fine RG
integrals or a verdict on full EPRL-FK.
"""
from __future__ import annotations
import argparse,cmath,json,math,random,statistics
from pathlib import Path

SEED=260912009
N_ACCEPT=12000
GAMMA=0.5
LANES=[
 {'name':'fixed_candidate','G':0.037,'Lambda':0.008},
 {'name':'lower_G','G':0.020,'Lambda':0.008},
 {'name':'higher_G','G':0.070,'Lambda':0.008},
 {'name':'zero_Lambda','G':0.037,'Lambda':0.0},
 {'name':'double_Lambda','G':0.037,'Lambda':0.016},
]
STRONG_CANCEL=0.10
BRANCH_RATIO_MIN=0.50
CANCEL_FRACTION_MIN=0.10


def shape_quantities(j0,j1,k):
    c=(j1-j0)/(4.0*k)
    if not -1.0 < c < 1.0: return None
    phi=math.acos(c)
    t=math.tan(phi)
    if abs(t)<1e-14: return None
    invt=1.0/t
    if not -1.0 <= invt <= 1.0: return None
    theta=math.acos(invt)
    q=2.0+(j0+j1)/(2.0*k)
    kc=-math.cos(2.0*theta)
    if kc <= 0.0: return None
    K=math.sqrt(kc)
    x=1.0+K*K-2.0*q
    # Eq. (35/39) Hessian determinant.
    D=(j0**3*j1**3*k**15/16.0)*K*(K-1j*K*K+1j*q)**3*(x**3)*(K+1j)**6*(K-3j)**2*(1+3*K*K-2*q-2j*K*(q-1))**3
    if abs(D)==0 or not math.isfinite(abs(D)): return None
    th0=theta
    th1=math.pi-theta
    ths=math.acos(max(-1.0,min(1.0,math.cos(theta)**2)))
    SR=6*j0*(math.pi/2-th0)+6*j1*(math.pi/2-th1)+12*k*(math.pi/2-ths)
    V=k*k*K*(q-2.0)
    return SR,V,cmath.phase(D),K,q


def sample_shapes(n):
    rng=random.Random(SEED)
    out=[]; trials=0
    while len(out)<n and trials<100*n:
        trials+=1
        # Equal log-volume-ish broad local shape ensemble around O(1) boundary areas.
        j0=math.exp(rng.uniform(math.log(0.25),math.log(2.5)))
        j1=math.exp(rng.uniform(math.log(0.25),math.log(2.5)))
        k=math.exp(rng.uniform(math.log(0.20),math.log(3.0)))
        q=shape_quantities(j0,j1,k)
        if q is not None: out.append((j0,j1,k,*q))
    if len(out)<n: raise RuntimeError(f'only accepted {len(out)} of requested {n}')
    return out,trials


def qtile(xs,q):
    ys=sorted(xs); p=(len(ys)-1)*q; lo=int(p); hi=min(lo+1,len(ys)-1); f=p-lo
    return ys[lo]*(1-f)+ys[hi]*f


def lane_stats(shapes,lane):
    G=lane['G']; Lam=lane['Lambda']
    canc=[]; ratios=[]; deltas=[]; flips=0
    for j0,j1,k,SR,V,varphi,K,Q in shapes:
        weird=math.cos(SR/G+varphi)
        phys=math.cos(GAMMA*SR/G-Lam*V/G)
        full=weird+phys
        denom=abs(weird)+abs(phys)
        cf=abs(full)/max(denom,1e-15)
        canc.append(cf)
        ratios.append(abs(weird)/max(abs(phys),1e-12))
        deltas.append(abs(full)-abs(phys))
        if phys*full < 0: flips += 1
    frac_cancel=sum(x<=STRONG_CANCEL for x in canc)/len(canc)
    median_ratio=statistics.median(ratios)
    material=bool(frac_cancel>=CANCEL_FRACTION_MIN and median_ratio>=BRANCH_RATIO_MIN)
    return {
      **lane,'n':len(canc),
      'strong_destructive_interference_fraction':frac_cancel,
      'median_abs_weird_over_abs_regge_branch':median_ratio,
      'median_interference_factor_abs_full_over_sum_abs_branches':statistics.median(canc),
      'interference_factor_q10':qtile(canc,0.1),'interference_factor_q90':qtile(canc,0.9),
      'fraction_full_sign_differs_from_regge_branch':flips/len(canc),
      'median_abs_full_minus_abs_regge_branch':statistics.median(deltas),
      'material_branch_interference_lane_pass':material,
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True); args=ap.parse_args()
    shapes,trials=sample_shapes(N_ACCEPT)
    lanes=[lane_stats(shapes,l) for l in LANES]
    npass=sum(l['material_branch_interference_lane_pass'] for l in lanes)
    out={
      'test':'RC009_HYPERFRUSTUM_BRANCH_INTERFERENCE_AUDIT','status':'PASS_EXECUTION',
      'seed':SEED,'gamma':GAMMA,'accepted_shapes':len(shapes),'sampling_trials':trials,
      'preregistered_gate':{
        'strong_cancellation':'abs(weird+Regge)/(abs(weird)+abs(Regge)) <= 0.10',
        'lane_pass':'strong-cancellation fraction >=0.10 and median abs(weird)/abs(Regge) >=0.50',
        'natural_support':'lane pass >=3/5','strong_support':'lane pass 5/5'
      },
      'lanes':lanes,'lanes_passed':npass,
      'natural_material_branch_interference':npass>=3,
      'strong_material_branch_interference':npass==len(lanes),
      'interpretation_lock':'Positive result means the second asymptotic Riemannian EPRL branch is numerically capable of substantial local interference with the Regge/cosmological branch in a broad admissible hyperfrustum shape ensemble. It does not reproduce the RG flow and does not imply failure of Lorentzian EPRL, where the asymptotic branch structure differs.',
      'source_equations':'arXiv:1804.00023v3 Eqs. 32, 35-39'
    }
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
