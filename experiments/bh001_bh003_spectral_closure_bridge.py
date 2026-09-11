#!/usr/bin/env python3
"""Bridge test between BH-001 composition closure and BH-003 spectral truncation.

Question: does the BH-003 iDelta spectral projector pick a subspace that is
more nearly closed under causal/retarded propagation than a rank-matched random
projector?  This is a falsifiable cross-hypothesis test, not a theorem.

For G_R=C/2 and an orthonormal retained basis V, define
  leakage = ||(I-P) G_R P||_F / ||G_R P||_F,
  seq_defect = ||P G_R (I-P) G_R P||_F / ||P G_R G_R P||_F.
The same quantities are evaluated for Haar-random rank-matched projectors.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy import linalg

from causal_set_ssee_2d_reproduction import sprinkle_diamond, causal_matrix


def retained_basis_from_idelta(c: np.ndarray, cutoff: float) -> tuple[np.ndarray,int]:
    delta=0.5*(c-c.T)
    i_delta=1j*delta
    evals,evecs=linalg.eigh(i_delta,check_finite=False)
    keep=np.abs(evals)>=cutoff
    return evecs[:,keep],int(np.sum(keep))


def closure_metrics(g: np.ndarray, v: np.ndarray) -> dict:
    gv=g@v
    pgv=v@(v.conj().T@gv)
    qgv=gv-pgv
    den_leak=float(linalg.norm(gv,'fro'))
    leakage=float(linalg.norm(qgv,'fro')/den_leak) if den_leak>0 else 0.0

    # Restricted numerator/denominator; Frobenius norms are invariant under the
    # outer isometry V so there is no need to materialize P as an n x n matrix.
    gqgv=g@qgv
    num=v.conj().T@gqgv
    ggv=g@gv
    den=v.conj().T@ggv
    den_norm=float(linalg.norm(den,'fro'))
    seq=float(linalg.norm(num,'fro')/den_norm) if den_norm>0 else 0.0
    return {'leakage':leakage,'sequential_defect':seq}


def random_basis(n:int,r:int,rng:np.random.Generator)->np.ndarray:
    z=rng.normal(size=(n,r))+1j*rng.normal(size=(n,r))
    q,_=np.linalg.qr(z,mode='reduced')
    return q


def run(n:int,seed:int,n_random:int)->dict:
    rng=np.random.default_rng(seed)
    uv=sprinkle_diamond(n,rng)
    c=causal_matrix(uv)
    g=0.5*c
    cutoff=math.sqrt(n)/(4.0*math.pi)
    vs,r=retained_basis_from_idelta(c,cutoff)
    if r<2 or r>=n:
        raise RuntimeError('invalid retained rank')
    spectral=closure_metrics(g,vs)

    random_rows=[]
    for _ in range(n_random):
        vr=random_basis(n,r,rng)
        random_rows.append(closure_metrics(g,vr))
    rand_leak=np.array([x['leakage'] for x in random_rows],float)
    rand_seq=np.array([x['sequential_defect'] for x in random_rows],float)

    def pct_better(x:float,arr:np.ndarray)->float:
        # Fraction of random projectors with a larger (worse) metric.
        return float(np.mean(arr>x))

    return {
        'test':'BH001_BH003_SPECTRAL_CLOSURE_BRIDGE',
        'n_parent':n,
        'seed':seed,
        'cutoff':cutoff,
        'retained_rank':r,
        'retained_fraction':r/n,
        'spectral':spectral,
        'random':{
            'n':n_random,
            'mean_leakage':float(rand_leak.mean()),
            'std_leakage':float(rand_leak.std()),
            'mean_sequential_defect':float(rand_seq.mean()),
            'std_sequential_defect':float(rand_seq.std()),
            'spectral_leakage_percentile_better':pct_better(spectral['leakage'],rand_leak),
            'spectral_seq_defect_percentile_better':pct_better(spectral['sequential_defect'],rand_seq),
        },
        'improvement_ratios':{
            'random_mean_over_spectral_leakage':float(rand_leak.mean()/spectral['leakage']) if spectral['leakage']>0 else None,
            'random_mean_over_spectral_seq_defect':float(rand_seq.mean()/spectral['sequential_defect']) if spectral['sequential_defect']>0 else None,
        },
        'claim_lock':(
            'Linear causal-set retarded-propagator closure diagnostic only. '
            'A positive result would link spectral truncation to BH-001 style closure, not prove quantum-gravity dynamics.'
        )
    }


def main()->int:
    p=argparse.ArgumentParser()
    p.add_argument('--n',type=int,required=True)
    p.add_argument('--seed',type=int,required=True)
    p.add_argument('--n-random',type=int,default=16)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    out=run(a.n,a.seed,a.n_random)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
