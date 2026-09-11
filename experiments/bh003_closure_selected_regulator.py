#!/usr/bin/env python3
"""BH-003 entropy-blind regulator selected by native causal closure.

Selection rule (pre-entropy):
1. diagonalize iDelta for a causal interval;
2. form nested spectral projectors retaining the largest |lambda| modes;
3. for a fixed log-spaced retained-fraction grid, measure one-step leakage under
   the native retarded propagator G_R=C/2;
4. choose the maximum-curvature corner of the log(retained fraction) versus
   log(leakage) L-curve;
5. freeze the resulting spectral threshold.

Only after selection do we compute SSEE.  Entropy values and the source cutoff
sqrt(N)/(4*pi) never enter the selection rule.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy import linalg

from causal_set_ssee_2d_reproduction import (
    sprinkle_diamond,
    causal_matrix,
    sj_matrices,
    nested_indices,
    spectral_project,
    ssee,
)


def _curvature(p0: np.ndarray, p1: np.ndarray, p2: np.ndarray) -> float:
    a=float(np.linalg.norm(p1-p0)); b=float(np.linalg.norm(p2-p1)); c=float(np.linalg.norm(p2-p0))
    if min(a,b,c) <= 1e-14:
        return 0.0
    cross=abs(float(np.cross(p1-p0,p2-p0)))
    return 2.0*cross/(a*b*c)


def closure_selected_cutoff(c: np.ndarray) -> dict:
    n=c.shape[0]
    delta=0.5*(c-c.T)
    j=1j*delta
    evals,u=linalg.eigh(j,check_finite=False)
    order=np.argsort(np.abs(evals))[::-1]
    evals=evals[order]
    u=u[:,order]

    g=0.5*c
    # Transform once.  Leakage for any nested projector is then computable from
    # Frobenius norms of blocks, avoiding repeated n x n projector products.
    b=u.conj().T @ g @ u
    col_energy=np.cumsum(np.sum(np.abs(b)**2,axis=0))

    # Fixed, source-independent retained-fraction grid.
    fractions=np.geomspace(0.035,0.80,18)
    rows=[]
    used=set()
    abs_e=np.abs(evals)
    for f in fractions:
        r=int(round(float(f)*n))
        r=max(4,min(n-4,r))
        # Preserve the +/- pairing approximately by using an even retained rank.
        if r%2: r+=1
        r=min(n-4,r)
        if r in used: continue
        used.add(r)
        pblock=b[:r,:r]
        p_energy=float(np.sum(np.abs(pblock)**2))
        gp_energy=float(col_energy[r-1])
        qgp2=max(0.0,gp_energy-p_energy)
        leakage=math.sqrt(qgp2/gp_energy) if gp_energy>0 else 0.0
        # Threshold halfway in log magnitude between retained/discarded modes.
        hi=max(float(abs_e[r-1]),1e-300); lo=max(float(abs_e[r]),1e-300)
        cutoff=math.sqrt(hi*lo)
        rows.append({'retained_rank':r,'retained_fraction':r/n,'leakage':leakage,'cutoff':cutoff})

    pts=np.array([[math.log(r['retained_fraction']),math.log(max(r['leakage'],1e-15))] for r in rows])
    curv=[0.0]*len(rows)
    for i in range(1,len(rows)-1):
        curv[i]=_curvature(pts[i-1],pts[i],pts[i+1])
    # Endpoints are forbidden by construction.
    idx=max(range(1,len(rows)-1),key=lambda i:curv[i])
    chosen=rows[idx].copy()
    chosen['curvature']=curv[idx]
    chosen['grid_index']=idx

    # Evaluate the stronger two-step return defect only at the chosen corner.
    r=chosen['retained_rank']
    br=b[:r,:r]
    # In eigenbasis, (G^2)_RR includes both retained and discarded paths.
    b2rr=(b @ b)[:r,:r]
    return_block=b2rr - br@br
    den=float(linalg.norm(b2rr,'fro'))
    chosen['sequential_return_defect']=float(linalg.norm(return_block,'fro')/den) if den>0 else 0.0
    chosen['scan']=rows
    return chosen


def run(n:int,seed:int,side_ratio:float)->dict:
    rng=np.random.default_rng(seed)
    uv=sprinkle_diamond(n,rng)
    c=causal_matrix(uv)
    i_delta,w,_,_=sj_matrices(uv)
    idx=nested_indices(uv,side_ratio)
    n_sub=int(len(idx))
    if n_sub<24:
        raise RuntimeError('subdiamond too small for closure selection')

    # Raw entropy is evaluated only after the regulator selections below.
    parent_sel=closure_selected_cutoff(c)
    c_sub=c[np.ix_(idx,idx)]
    sub_sel=closure_selected_cutoff(c_sub)

    jpt,wpt,kp=spectral_project(i_delta,w,parent_sel['cutoff'])
    jr1=jpt[np.ix_(idx,idx)]
    wr1=wpt[np.ix_(idx,idx)]
    jst,wst,ks=spectral_project(jr1,wr1,sub_sel['cutoff'])
    s_selected,modes=ssee(wst,jst,support_rtol=1e-9)

    jr=i_delta[np.ix_(idx,idx)]
    wr=w[np.ix_(idx,idx)]
    s_raw,_=ssee(wr,jr)

    source_parent=math.sqrt(n)/(4.0*math.pi)
    source_sub=math.sqrt(n_sub)/(4.0*math.pi)
    # Store compact selections; full scans are useful diagnostics but keep output manageable.
    def compact(sel):
        return {k:v for k,v in sel.items() if k!='scan'}
    return {
        'test':'BH003_CLOSURE_SELECTED_REGULATOR',
        'n_parent':n,
        'n_sub':n_sub,
        'seed':seed,
        'side_ratio':side_ratio,
        'raw_entropy':float(s_raw),
        'closure_selected_entropy':float(s_selected),
        'parent_selection':compact(parent_sel),
        'sub_selection':compact(sub_sel),
        'parent_cutoff_over_source':parent_sel['cutoff']/source_parent,
        'sub_cutoff_over_source':sub_sel['cutoff']/source_sub,
        'retained_parent_modes_both_signs':int(kp),
        'retained_sub_modes_both_signs':int(ks),
        'generalized_modes':int(modes),
        'log_size_proxy':math.log(math.sqrt(n_sub)/(4.0*math.pi)),
        'claim_lock':(
            'Regulator selected from causal-propagator closure/compression L-curve only. '
            'Entropy and source cutoff are post-selection diagnostics.'
        )
    }


def main()->int:
    p=argparse.ArgumentParser()
    p.add_argument('--n',type=int,required=True)
    p.add_argument('--seed',type=int,required=True)
    p.add_argument('--side-ratio',type=float,default=0.5)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    out=run(a.n,a.seed,a.side_ratio)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
