#!/usr/bin/env python3
"""Exhaustive, preregistered partial-slice Lorentzian EPRL cross-shell diagnostic.

For a 2x2x2x2x2 vertex tensor pair (Dl=0,Dl=1), every choice of two open
intertwiner axes (10 choices) and every Dl1->Dl0 fixed-boundary pair (8x8)
is evaluated.  For each open-axis choice the rank-1 projector is learned only
from the Dl=0 all-zero fixed slice and then frozen.  This removes post-selection
of the previously strong 001->111 slice.

The repeated slices are symmetry-related and are not treated as independent
statistical trials. This is a robustness map, not a p-value generator.
"""
from __future__ import annotations
import argparse, itertools, json, math, struct
from pathlib import Path
import numpy as np

HEADER_DIMS=128; TAG_BYTES=1024

def load_sl2t(path: Path) -> np.ndarray:
    raw=path.read_bytes(); word=struct.calcsize('P'); header=HEADER_DIMS*word+TAG_BYTES
    if len(raw)<header: raise RuntimeError(f'short sl2t file: {path}')
    fmt='=' + ('Q' if word==8 else 'I')*HEADER_DIMS
    ds=struct.unpack_from(fmt,raw,0); dims=tuple(int(x) for x in ds[:5])
    if dims!=(2,2,2,2,2): raise RuntimeError(f'expected 2^5 tensor, got {dims}')
    n=math.prod(dims); need=header+8*n
    if len(raw)!=need: raise RuntimeError(f'unexpected file size {len(raw)} != {need}')
    a=np.frombuffer(raw,dtype=np.float64,count=n,offset=header).copy().reshape(dims,order='F')
    if not np.all(np.isfinite(a)) or not np.any(a!=0): raise RuntimeError('invalid tensor entries')
    return a

def haar_basis(n,r,rng):
    z=rng.normal(size=(n,r))+1j*rng.normal(size=(n,r)); q,_=np.linalg.qr(z); return q[:,:r]

def top_basis(a,r=1):
    _,_,vh=np.linalg.svd(np.asarray(a,np.complex128),full_matrices=False); return vh.conj().T[:,:r]

def metrics(a1,a2,v):
    a1=np.asarray(a1,np.complex128); a2=np.asarray(a2,np.complex128)
    a1v=a1@v; q=a1v-v@(v.conj().T@a1v)
    leak=np.linalg.norm(q)/max(np.linalg.norm(a1v),np.finfo(float).eps)
    ret=np.linalg.norm(v.conj().T@(a2@q))/max(np.linalg.norm(v.conj().T@(a2@(a1@v))),np.finfo(float).eps)
    return float(leak),float(ret)

def partial(t,open_axes,bits):
    fixed=[a for a in range(5) if a not in open_axes]
    idx=[slice(None)]*5
    for a,b in zip(fixed,bits): idx[a]=b
    out=np.asarray(t[tuple(idx)],dtype=float)
    if out.shape!=(2,2): raise RuntimeError((open_axes,bits,out.shape))
    return out

def run(t0,t1,nrandom,seed,gamma):
    rng=np.random.default_rng(seed); rows=[]; bitrows=list(itertools.product((0,1),repeat=3))
    for open_axes in itertools.combinations(range(5),2):
        train=partial(t0,open_axes,(0,0,0)); p=top_basis(train,1)
        for b1 in bitrows:
            a1=partial(t1,open_axes,b1)
            for b2 in bitrows:
                a2=partial(t0,open_axes,b2); pl,pr=metrics(a1,a2,p); rr=[]
                for _ in range(nrandom):
                    v=haar_basis(2,1,rng); _,r=metrics(a1,a2,v); rr.append(r)
                rr=np.asarray(rr)
                rows.append({'open_axes':list(open_axes),'dl1_bits':''.join(map(str,b1)),'dl0_bits':''.join(map(str,b2)),
                    'source_return_defect':pr,'mean_random_return_defect':float(rr.mean()),
                    'return_improvement':float(rr.mean()/max(pr,np.finfo(float).eps)),
                    'fraction_random_worse_return':float(np.mean(rr>pr))})
    im=np.asarray([r['return_improvement'] for r in rows]); fw=np.asarray([r['fraction_random_worse_return'] for r in rows])
    prior=next(r for r in rows if r['open_axes']==[0,1] and r['dl1_bits']=='001' and r['dl0_bits']=='111')
    return {'test':'LORENTZIAN_EPRL_EXHAUSTIVE_CROSSSHELL_PARTIAL_SLICES','status':'PASS_EXECUTION','gamma':gamma,
      'n_cases':len(rows),'n_random_per_case':nrandom,'tensor_dl0_norm':float(np.linalg.norm(t0)),'tensor_dl1_norm':float(np.linalg.norm(t1)),
      'summary':{'fraction_return_improvement_gt_1':float(np.mean(im>1)),'fraction_control_majority':float(np.mean(fw>0.5)),
                 'median_return_improvement':float(np.median(im)),'mean_return_improvement':float(np.mean(im)),
                 'min_return_improvement':float(np.min(im)),'max_return_improvement':float(np.max(im))},
      'prior_slice_no_postselection':prior,'cases':rows,
      'claim_lock':'Exhaustive partial-slice robustness map for one pinned Lorentzian EPRL 4-simplex vertex realization. Symmetry-related slices are not independent trials. This is not full spinfoam gluing, refinement, or a complete QG theory.'}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--dl0',type=Path,required=True); p.add_argument('--dl1',type=Path,required=True)
    p.add_argument('--gamma',type=float,required=True); p.add_argument('--n-random',type=int,default=512); p.add_argument('--seed',type=int,default=20260918); p.add_argument('--output',type=Path,required=True)
    a=p.parse_args(); out=run(load_sl2t(a.dl0),load_sl2t(a.dl1),a.n_random,a.seed,a.gamma)
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out['summary'],indent=2,sort_keys=True))
if __name__=='__main__': main()
