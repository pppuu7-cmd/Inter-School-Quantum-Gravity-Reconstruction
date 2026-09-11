#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy import linalg


def sprinkle_diamond(n, rng):
    return rng.random((n,2))

def causal_matrix(uv):
    u=uv[:,0]; v=uv[:,1]
    return ((u[:,None] < u[None,:]) & (v[:,None] < v[None,:])).astype(float)

def massive_retarded(c, mu):
    # mu = m^2/rho is held fixed so the deformation strength is resolution-independent.
    k0=0.5*c
    a=np.eye(c.shape[0]) + mu*k0
    return linalg.solve(a.T, k0.T, assume_a='gen', check_finite=False).T

def retained_basis(c):
    delta=0.5*(c-c.T)
    evals,evecs=linalg.eigh(1j*delta,check_finite=False)
    cutoff=math.sqrt(c.shape[0])/(4*math.pi)
    keep=np.abs(evals)>=cutoff
    return evecs[:,keep], cutoff

def random_basis(n,r,rng):
    z=rng.normal(size=(n,r))+1j*rng.normal(size=(n,r))
    q,_=np.linalg.qr(z,mode='reduced')
    return q

def metrics(g1,g2,v):
    a1=g1@v
    pa1=v@(v.conj().T@a1)
    qa1=a1-pa1
    leakage=float(linalg.norm(qa1,'fro')/max(linalg.norm(a1,'fro'),1e-30))
    num=v.conj().T@(g2@qa1)
    den=v.conj().T@(g2@(g1@v))
    ret=float(linalg.norm(num,'fro')/max(linalg.norm(den,'fro'),1e-30))
    return leakage,ret

def run(n,seed,mu1,mu2,nrandom):
    rng=np.random.default_rng(seed)
    uv=sprinkle_diamond(n,rng); c=causal_matrix(uv)
    v,cutoff=retained_basis(c); r=v.shape[1]
    if r<2 or r>=n: raise RuntimeError('invalid retained rank')
    g1=massive_retarded(c,mu1); g2=massive_retarded(c,mu2)
    pleak,pret=metrics(g1,g2,v)
    rl=[]; rr=[]
    for _ in range(nrandom):
        vr=random_basis(n,r,rng)
        x,y=metrics(g1,g2,vr); rl.append(x); rr.append(y)
    rl=np.asarray(rl); rr=np.asarray(rr)
    rel=float(linalg.norm(g2-g1,'fro')/max(linalg.norm(g1,'fro'),1e-30))
    return {
      'test':'CAUSAL_SET_HETEROGENEOUS_MASS_COMPOSITION',
      'n':n,'seed':seed,'mu1':mu1,'mu2':mu2,'operator_relative_difference':rel,
      'source_cutoff':cutoff,'retained_rank':r,'retained_fraction':r/n,
      'source_sector':{'leakage':pleak,'heterogeneous_return_defect':pret},
      'random_controls':{
        'n':nrandom,'mean_leakage':float(rl.mean()),'mean_return_defect':float(rr.mean()),
        'fraction_random_worse_leakage':float(np.mean(rl>pleak)),
        'fraction_random_worse_return':float(np.mean(rr>pret))},
      'improvement':{
        'random_mean_over_source_leakage':float(rl.mean()/pleak) if pleak>0 else None,
        'random_mean_over_source_return':float(rr.mean()/pret) if pret>0 else None},
      'claim_lock':'Mass-deformed 1+1D causal-set propagator composition on one causal set. P is fixed by the massless source SSEE spectral rule; no target metric enters P. This is a structural closure test, not QG dynamics.'
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument('--n',type=int,required=True); p.add_argument('--seed',type=int,required=True)
    p.add_argument('--mu1',type=float,required=True); p.add_argument('--mu2',type=float,required=True); p.add_argument('--n-random',type=int,default=24)
    p.add_argument('--output',type=Path,required=True); a=p.parse_args(); out=run(a.n,a.seed,a.mu1,a.mu2,a.n_random)
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
