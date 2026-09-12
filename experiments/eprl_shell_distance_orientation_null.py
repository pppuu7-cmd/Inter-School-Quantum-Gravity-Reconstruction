#!/usr/bin/env python3
"""Compare shared-unitary orientation sensitivity at two Lorentzian EPRL shell distances.

The rank-1 projector is trained once from the Dl=0 all-zero source slice for
each choice of two open intertwiner axes.  We then evaluate two holdout pairs:

  near: A1 from Dl=1, A2 from Dl=0
  far:  A1 from Dl=2, A2 from Dl=0

For each pair, the same Haar unitary is applied by similarity to both holdout
operators while P remains frozen.  This preserves each holdout spectrum and the
shared-similarity relation but scrambles orientation relative to P.

This extends the previous one-vertex orientation-null test in shell distance.
It remains a structural one-vertex diagnostic and is not a spin-foam
refinement/gluing calculation.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np

from eprl_crossshell_exhaustive import load_sl2t, top_basis, metrics, partial
from eprl_shared_unitary_orientation_null import haar_unitary


def eval_transition(t0, thigh, label: str, nnull: int, seed: int):
    rng=np.random.default_rng(seed)
    bitrows=list(itertools.product((0,1),repeat=3))
    rows=[]
    for open_axes in itertools.combinations(range(5),2):
        train=partial(t0,open_axes,(0,0,0))
        p=top_basis(train,1)
        for bh in bitrows:
            a1=np.asarray(partial(thigh,open_axes,bh),np.complex128)
            for b0 in bitrows:
                a2=np.asarray(partial(t0,open_axes,b0),np.complex128)
                _,src=metrics(a1,a2,p)
                vals=np.empty(nnull,float)
                for i in range(nnull):
                    u=haar_unitary(2,rng)
                    u1=u.conj().T@a1@u
                    u2=u.conj().T@a2@u
                    _,vals[i]=metrics(u1,u2,p)
                eps=np.finfo(float).eps
                rows.append({
                    'open_axes':list(open_axes),
                    'high_bits':''.join(map(str,bh)),
                    'dl0_bits':''.join(map(str,b0)),
                    'source_return_defect':float(src),
                    'null_mean_return_defect':float(vals.mean()),
                    'null_median_return_defect':float(np.median(vals)),
                    'mean_return_improvement':float(vals.mean()/max(src,eps)),
                    'median_return_improvement':float(np.median(vals)/max(src,eps)),
                    'fraction_null_worse_return':float(np.mean(vals>src)),
                })
    med=np.asarray([r['median_return_improvement'] for r in rows],float)
    mean=np.asarray([r['mean_return_improvement'] for r in rows],float)
    frac=np.asarray([r['fraction_null_worse_return'] for r in rows],float)
    summary={
        'n_cases':len(rows),
        'median_case_mean_return_improvement':float(np.median(mean)),
        'median_case_median_return_improvement':float(np.median(med)),
        'fraction_cases_median_improvement_gt_1':float(np.mean(med>1)),
        'fraction_cases_majority_null_worse':float(np.mean(frac>0.5)),
        'mean_fraction_null_worse':float(np.mean(frac)),
    }
    summary['natural_support']=bool(summary['median_case_median_return_improvement']>1 and summary['fraction_cases_majority_null_worse']>0.5)
    summary['strong_support']=bool(summary['median_case_median_return_improvement']>1 and summary['fraction_cases_majority_null_worse']>0.6)
    prior=next(r for r in rows if r['open_axes']==[0,1] and r['high_bits']=='001' and r['dl0_bits']=='111')
    return {'label':label,'summary':summary,'prior_slice_no_postselection':prior,'cases':rows}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--dl0',type=Path,required=True)
    p.add_argument('--dl1',type=Path,required=True)
    p.add_argument('--dl2',type=Path,required=True)
    p.add_argument('--gamma',type=float,required=True)
    p.add_argument('--n-null',type=int,default=128)
    p.add_argument('--seed',type=int,default=20260920)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    t0=load_sl2t(a.dl0); t1=load_sl2t(a.dl1); t2=load_sl2t(a.dl2)
    near=eval_transition(t0,t1,'Dl1_to_Dl0',a.n_null,a.seed)
    far=eval_transition(t0,t2,'Dl2_to_Dl0',a.n_null,a.seed+1000003)
    out={
        'test':'LORENTZIAN_EPRL_SHELL_DISTANCE_SHARED_UNITARY_ORIENTATION_NULL',
        'status':'PASS_EXECUTION','gamma':a.gamma,'n_null_per_case':a.n_null,
        'near':near,'far':far,
        'far_natural_support':far['summary']['natural_support'],
        'far_strong_support':far['summary']['strong_support'],
        'far_over_near_median_orientation_gain':float(
            far['summary']['median_case_median_return_improvement']/max(near['summary']['median_case_median_return_improvement'],np.finfo(float).eps)),
        'claim_lock':'Pinned one-vertex Lorentzian EPRL shell-distance structural audit. Dl=2 is a shell extension, not a genuine multi-vertex refinement or continuum calculation.'
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'gamma':a.gamma,'near':near['summary'],'far':far['summary'],'far_over_near_median_orientation_gain':out['far_over_near_median_orientation_gain']},indent=2,sort_keys=True))


if __name__=='__main__':
    main()
