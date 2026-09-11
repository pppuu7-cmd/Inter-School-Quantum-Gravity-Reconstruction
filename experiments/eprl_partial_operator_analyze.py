#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
from numpy.linalg import norm, svd, qr


def parse_extract(path: Path):
    lines=[x.strip() for x in path.read_text().splitlines() if x.strip()]
    if not lines or not lines[0].startswith('META '):
        raise RuntimeError('missing META line')
    toks=lines[0].split()
    meta={'gamma':float(toks[2]),'Dl':int(toks[4]),'spin_j':float(toks[6])}
    ops={}; i=1
    while i < len(lines):
        if not lines[i].startswith('OP '):
            raise RuntimeError(f'expected OP line at {i}: {lines[i]}')
        name=lines[i].split()[1]; i += 1
        A=np.zeros((3,3),dtype=np.complex128)
        for r in range(3):
            vals=[float(x) for x in lines[i+r].split()]
            if len(vals)!=6: raise RuntimeError('expected 3 complex entries per row')
            for c in range(3): A[r,c]=vals[2*c]+1j*vals[2*c+1]
        ops[name]=A; i += 3
    return meta,ops


def random_basis(n,r,rng):
    z=rng.normal(size=(n,r))+1j*rng.normal(size=(n,r))
    q,_=qr(z,mode='reduced')
    return q[:,:r]


def metrics(a1,a2,v):
    a1v=a1@v
    pa1=v@(v.conj().T@a1v)
    qa1=a1v-pa1
    leak=float(norm(qa1)/max(norm(a1v),1e-30))
    num=v.conj().T@(a2@qa1)
    den=v.conj().T@(a2@(a1@v))
    ret=float(norm(num)/max(norm(den),1e-30))
    return leak,ret


def run(source:Path,seed:int,nrandom:int):
    meta,ops=parse_extract(source)
    required={'train','a','b','c','d'}
    if set(ops)!=required: raise RuntimeError(f'operator labels mismatch: {set(ops)}')
    train=ops['train']
    u,s,vh=svd(train,full_matrices=False)
    rank=int(np.sum(s>max(float(s.max()),1e-300)*1e-12))
    if rank < 2: raise RuntimeError(f'SCIENTIFIC_GATE_FAIL train rank={rank}, singular_values={s.tolist()}')
    if not np.all(np.isfinite(train)): raise RuntimeError('nonfinite train operator')
    if norm(train)<=0: raise RuntimeError('zero train operator')
    v=vh.conj().T[:,:2]
    rng=np.random.default_rng(seed)
    rows=[]
    names=['a','b','c','d']
    for first in names:
      for second in names:
        if first==second: continue
        a1,a2=ops[first],ops[second]
        pl,pr=metrics(a1,a2,v)
        rl=[]; rr=[]
        for _ in range(nrandom):
            vr=random_basis(3,2,rng)
            l,r=metrics(a1,a2,vr); rl.append(l); rr.append(r)
        rl=np.asarray(rl); rr=np.asarray(rr)
        rows.append({
          'first':first,'second':second,
          'a1_a2_relative_difference':float(norm(a2-a1)/max(norm(a1),1e-30)),
          'train_sector':{'leakage':pl,'return_defect':pr},
          'random_controls':{
            'n':nrandom,
            'mean_leakage':float(rl.mean()),'mean_return':float(rr.mean()),
            'fraction_random_worse_leakage':float(np.mean(rl>pl)),
            'fraction_random_worse_return':float(np.mean(rr>pr))},
          'improvement':{
            'random_mean_over_train_leakage':float(rl.mean()/pl) if pl>0 else None,
            'random_mean_over_train_return':float(rr.mean()/pr) if pr>0 else None}
        })
    diag={}
    for k,A in ops.items():
        ss=svd(A,compute_uv=False)
        diag[k]={
          'frobenius_norm':float(norm(A)),
          'singular_values':[float(x) for x in ss],
          'numerical_rank':int(np.sum(ss>max(float(ss.max()),1e-300)*1e-12)),
          'relative_to_train':float(norm(A-train)/max(norm(train),1e-30))}
    return {
      'test':'LORENTZIAN_EPRL_PARTIAL_OPERATOR_HETEROGENEOUS_RETURN',
      'source_repository':'qg-cpt-marseille/sl2cfoam-next',
      'source_commit':'052e4346028870bd76f69a3034e6cae8defb8f7f',
      **meta,
      'partial_operator_dimensions':[3,3],
      'train_singular_values':[float(x) for x in s],
      'train_numerical_rank':rank,
      'operator_diagnostics':diag,
      'rows':rows,
      'summary':{
        'n_ordered_pairs':len(rows),
        'mean_fraction_random_worse_return':float(np.mean([r['random_controls']['fraction_random_worse_return'] for r in rows])),
        'mean_fraction_random_worse_leakage':float(np.mean([r['random_controls']['fraction_random_worse_leakage'] for r in rows])),
        'mean_relative_operator_difference':float(np.mean([r['a1_a2_relative_difference'] for r in rows]))},
      'claim_lock':(
        'Source-native Lorentzian EPRL vertex and source-native Livine-Speziale coherent states, contracted in C exactly as the official Julia wrapper orders i5->i4->i3. '
        'The retained sector is SVD-defined from the regular-boundary train operator, not an independently physical coarse-graining prescription. '
        'Equal-spin matrix composition remains operator-level until a multi-vertex EPRL gluing audit is passed.')}


def main():
    p=argparse.ArgumentParser(); p.add_argument('--input',type=Path,required=True); p.add_argument('--seed',type=int,required=True); p.add_argument('--n-random',type=int,default=256); p.add_argument('--output',type=Path,required=True)
    a=p.parse_args(); out=run(a.input,a.seed,a.n_random); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
