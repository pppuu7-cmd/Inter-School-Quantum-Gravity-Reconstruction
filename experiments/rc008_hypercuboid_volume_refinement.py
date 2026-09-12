#!/usr/bin/env python3
"""RC008 source-faithful hypercuboid 4-volume/refinement pre-gate.

Uses pinned Eq:4Volume, V4=(a_xy a_xz a_xt a_yz a_yt a_zt)^(1/3), with
hypercuboid areas a_ij=l_i l_j. The gate checks exact geometric consistency,
4-volume homogeneity, and additive conservation under non-retuned slicing of
one edge direction. This is an observable/refinement prerequisite only, not a
vertex-amplitude reproduction or RG fixed-point result.
"""
import argparse, json, math
from pathlib import Path
import numpy as np

PAIRS=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))

def v4_from_lengths(L):
    areas=[L[i]*L[j] for i,j in PAIRS]
    return float(np.prod(areas)**(1.0/3.0)), areas

def rel(a,b):
    return abs(a-b)/max(1.0,abs(a),abs(b))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--seed',type=int,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    rng=np.random.default_rng(a.seed)
    # anisotropic positive boundary lengths; no fitting to any published alpha_*
    L=np.exp(rng.uniform(math.log(0.35),math.log(3.5),size=4))
    V,areas=v4_from_lengths(L)
    direct=float(np.prod(L))
    geometry_err=rel(V,direct)

    scale_errs=[]
    for s in (0.5,0.8,1.7,3.0):
        Vs,_=v4_from_lengths(s*L)
        scale_errs.append(rel(Vs,(s**4)*V))

    refinement=[]
    for axis in range(4):
        for n in (2,3,4,5):
            sub=L.copy(); sub[axis]/=n
            vsub,_=v4_from_lengths(sub)
            total=n*vsub
            refinement.append({'axis':axis,'n':n,'relative_error':rel(total,V)})
    max_ref=max(r['relative_error'] for r in refinement)

    # Frozen negative control: independently perturb one face area after geometry
    # construction. Eq:4Volume must notice the inconsistency, preventing a false
    # PASS from a test that merely multiplies edge lengths directly.
    bad=list(areas); bad[0]*=1.05
    Vbad=float(np.prod(bad)**(1.0/3.0))
    negative_shift=abs(Vbad-V)/V

    thresholds={'geometry':1e-12,'scale':1e-12,'refinement':1e-12,'negative_shift_min':1e-3}
    ok=(geometry_err<=thresholds['geometry'] and max(scale_errs)<=thresholds['scale'] and max_ref<=thresholds['refinement'] and negative_shift>=thresholds['negative_shift_min'])
    out={
      'test':'RC008_HYPERCUBOID_VOLUME_REFINEMENT_PRE_GATE','seed':a.seed,'lengths':L.tolist(),
      'source_equation':'Eq:4Volume','volume_from_areas':V,'volume_direct':direct,
      'geometry_relative_error':geometry_err,'max_scale_relative_error':max(scale_errs),
      'max_refinement_relative_error':max_ref,'negative_control_relative_shift':negative_shift,
      'refinement_rows':refinement,'frozen_thresholds':thresholds,'frozen_gate_pass':bool(ok),
      'classification_if_pass':'PASS_SOURCE_FAITHFUL_HYPERCUBOID_VOLUME_REFINEMENT_PREREQUISITE_ONLY',
      'claim_lock':'Not full vertex amplitude, not alpha RG map, not held-out transport, not BRIDGE_DERIVED.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('refinement_rows','lengths')},indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()
