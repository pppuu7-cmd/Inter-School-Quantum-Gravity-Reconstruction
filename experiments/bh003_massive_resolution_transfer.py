#!/usr/bin/env python3
"""BH-003 dynamics-deformation holdout: massive 1+1D causal-set SSEE.

The retained spectral rule is frozen to the massless source prescription
|lambda(iDelta)| >= sqrt(N)/(4 pi).  The only dynamical deformation is the
source-native 2D massive retarded Green function

    K_m = K_0 [I + (m^2/rho) K_0]^{-1},  K_0 = C/2.

For the unit-volume parent diamond used here rho=N.  No entropy target enters
cutoff selection.  This is a validation of transfer under a known free-field
dynamical deformation, not a quantum-gravity result.
"""
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


def massive_retarded(c, mass, rho):
    k0=0.5*c
    # K_m = K_0 (I + (m^2/rho) K_0)^(-1).
    # Solve on the right without constructing an explicit inverse.
    a=np.eye(c.shape[0]) + (mass*mass/rho)*k0
    return linalg.solve(a.T, k0.T, assume_a='gen', check_finite=False).T


def sj_from_retarded(gr):
    delta=gr-gr.T
    i_delta=1j*delta
    evals,evecs=linalg.eigh(i_delta,check_finite=False)
    pos=evals>1e-12
    w=(evecs[:,pos]*evals[pos]) @ evecs[:,pos].conj().T
    return i_delta,w,evals


def spectral_project(i_delta,w,cutoff):
    evals,evecs=linalg.eigh(i_delta,check_finite=False)
    keep=np.abs(evals)>=cutoff
    vk=evecs[:,keep]; jk=evals[keep]
    jt=(vk*jk)@vk.conj().T
    wt=vk@(vk.conj().T@w@vk)@vk.conj().T
    return jt,wt,int(np.sum(keep))


def ssee(w,i_delta,support_rtol=1e-9):
    je,ju=linalg.eigh(i_delta,check_finite=False)
    scale=max(float(np.max(np.abs(je))),1.0)
    keep=np.abs(je)>support_rtol*scale
    if not np.any(keep): return 0.0,0
    uk=ju[:,keep]; jk=je[keep]
    wk=uk.conj().T@w@uk
    m=(1.0/jk)[:,None]*wk
    lam=linalg.eigvals(m,check_finite=False)
    lam=lam[np.isfinite(lam)]
    lam=lam[np.abs(lam.imag)<1e-6].real
    lam=lam[np.abs(lam)>1e-12]
    return float(np.sum(lam*np.log(np.abs(lam))).real),int(len(lam))


def nested_indices(uv,ratio):
    lo=.5*(1-ratio); hi=.5*(1+ratio)
    return np.where((uv[:,0]>=lo)&(uv[:,0]<=hi)&(uv[:,1]>=lo)&(uv[:,1]<=hi))[0]


def run(n,mass,seed,side_ratio):
    rng=np.random.default_rng(seed)
    uv=sprinkle_diamond(n,rng)
    c=causal_matrix(uv)
    rho=float(n)  # unit parent-volume convention
    gr=massive_retarded(c,mass,rho)
    i_delta,w,evals=sj_from_retarded(gr)
    idx=nested_indices(uv,side_ratio)
    ns=len(idx)
    if ns<8: raise RuntimeError('subdiamond too small')

    cutoff_parent=math.sqrt(n)/(4*math.pi)
    jp,wp,kp=spectral_project(i_delta,w,cutoff_parent)
    jr=jp[np.ix_(idx,idx)]; wr=wp[np.ix_(idx,idx)]
    cutoff_sub=math.sqrt(ns)/(4*math.pi)
    js,ws,ks=spectral_project(jr,wr,cutoff_sub)
    entropy,modes=ssee(ws,js)

    pos=np.sort(evals[evals>1e-12])[::-1]
    return {
      'test':'BH003_MASSIVE_RESOLUTION_TRANSFER',
      'n_parent':n,'n_sub':int(ns),'mass':mass,'seed':seed,
      'rho_parent':rho,'m2_over_rho':mass*mass/rho,
      'side_ratio':side_ratio,
      'cutoff_parent':cutoff_parent,'cutoff_sub':cutoff_sub,
      'retained_parent_modes_both_signs':kp,
      'retained_sub_modes_both_signs':ks,
      'truncated_generalized_modes':modes,
      'truncated_entropy':entropy,
      'positive_parent_modes_above_rule':int(np.sum(pos>=cutoff_parent)),
      'log_cutoff_proxy':math.log(math.sqrt(ns)/(4*math.pi)),
      'claim_lock':(
        'Known 1+1D free massive scalar causal-set deformation with the massless source cutoff frozen. '
        'No entropy target or fitted cutoff enters the selection; this is not QG dynamics.'
      )
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--n',type=int,required=True); p.add_argument('--mass',type=float,required=True)
    p.add_argument('--seed',type=int,required=True); p.add_argument('--side-ratio',type=float,default=.5)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args(); out=run(a.n,a.mass,a.seed,a.side_ratio)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
