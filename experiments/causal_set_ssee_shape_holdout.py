#!/usr/bin/env python3
"""BH-003 geometry holdout: move/boost the nested causal diamond.

The spectral cutoff rule remains frozen at sqrt(N)/(4*pi).  Only the nested
causal interval changes position and null-coordinate aspect ratio.  Any axis-
aligned rectangle in (u,v) is a 1+1D causal interval; unequal u/v side lengths
are related to boosted diamonds rather than a new cutoff prescription.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from causal_set_ssee_2d_reproduction import (
    sprinkle_diamond,
    sj_matrices,
    spectral_project,
    ssee,
)

SHAPES = {
    'central_square': (0.50, 0.50, 0.50, 0.50),
    'central_boosted': (0.50, 0.50, 0.35, 0.70),
    'offset_square': (0.35, 0.65, 0.50, 0.50),
    'offset_boosted': (0.40, 0.60, 0.40, 0.60),
}


def rect_indices(uv: np.ndarray, shape: str) -> np.ndarray:
    if shape not in SHAPES:
        raise ValueError(f'unknown shape {shape}')
    cu, cv, su, sv = SHAPES[shape]
    ulo, uhi = cu - su/2.0, cu + su/2.0
    vlo, vhi = cv - sv/2.0, cv + sv/2.0
    if not (0 <= ulo < uhi <= 1 and 0 <= vlo < vhi <= 1):
        raise ValueError('shape leaves parent diamond')
    return np.where(
        (uv[:,0] >= ulo) & (uv[:,0] <= uhi) &
        (uv[:,1] >= vlo) & (uv[:,1] <= vhi)
    )[0]


def run(n: int, seed: int, shape: str) -> dict:
    rng=np.random.default_rng(seed)
    uv=sprinkle_diamond(n,rng)
    i_delta,w,_,_=sj_matrices(uv)
    idx=rect_indices(uv,shape)
    n_sub=int(len(idx))
    if n_sub < 16:
        raise RuntimeError('holdout causal interval too small')

    jr=i_delta[np.ix_(idx,idx)]
    wr=w[np.ix_(idx,idx)]
    s_raw,_=ssee(wr,jr)

    cp=math.sqrt(n)/(4.0*math.pi)
    jpt,wpt,kp=spectral_project(i_delta,w,cp)
    jr1=jpt[np.ix_(idx,idx)]
    wr1=wpt[np.ix_(idx,idx)]
    cs=math.sqrt(n_sub)/(4.0*math.pi)
    jst,wst,ks=spectral_project(jr1,wr1,cs)
    s_trunc,modes=ssee(wst,jst,support_rtol=1e-9)

    cu,cv,su,sv=SHAPES[shape]
    return {
        'test':'BH003_SSEE_GEOMETRY_HOLDOUT',
        'n_parent':n,
        'n_sub':n_sub,
        'seed':seed,
        'shape':shape,
        'center_u':cu,
        'center_v':cv,
        'side_u':su,
        'side_v':sv,
        'expected_area_fraction':su*sv,
        'raw_entropy':float(s_raw),
        'truncated_entropy':float(s_trunc),
        'cutoff_parent':cp,
        'cutoff_sub':cs,
        'retained_parent_modes_both_signs':int(kp),
        'retained_sub_modes_both_signs':int(ks),
        'truncated_generalized_modes':int(modes),
        'log_size_proxy':math.log(math.sqrt(n_sub)/(4.0*math.pi)),
        'claim_lock':'Frozen source rule; geometry/position/boost holdout only.'
    }


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument('--n',type=int,required=True)
    p.add_argument('--seed',type=int,required=True)
    p.add_argument('--shape',choices=sorted(SHAPES),required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    out=run(a.n,a.seed,a.shape)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
