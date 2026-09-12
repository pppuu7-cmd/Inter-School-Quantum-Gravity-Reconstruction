#!/usr/bin/env python3
from pathlib import Path
import argparse,json,math

KEYS=['b4_i1_k0','b4_i1_k1','b4_i1_k2','weighted_k_sum','dvd2_dl0','dvd3_dl0']
def parse(path):
    d={}
    for line in Path(path).read_text().splitlines():
        if '=' not in line: continue
        k,v=line.split('=',1)
        if k in KEYS or k=='gamma':
            d[k]=float(v)
    return d

def rdiff(a,b):
    den=max(abs(a),abs(b),1e-300)
    return abs(a-b)/den

ap=argparse.ArgumentParser(); ap.add_argument('--run1',required=True); ap.add_argument('--run2',required=True); ap.add_argument('--gamma',type=float,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
x=parse(a.run1); y=parse(a.run2)
complete=all(k in x and k in y for k in KEYS)
finite=complete and all(math.isfinite(x[k]) and math.isfinite(y[k]) for k in KEYS)
diffs={k:rdiff(x[k],y[k]) for k in KEYS} if finite else {}
maxdiff=max(diffs.values()) if diffs else None
threshold=1e-12
passed=bool(finite and maxdiff is not None and maxdiff<=threshold)
out={
 'test':'LORENTZIAN_EPRL_DVD_DL0_TWO_VERTEX_PILOT',
 'gamma':a.gamma,
 'boundary':{'j':[1,1,1,1],'jp':[1,1,1,1],'i':1,'t':1,'ip':1,'tp':1,'delta_l':0},
 'values_first':{k:x.get(k) for k in KEYS},
 'repeat_relative_differences':diffs,
 'repeat_max_relative_difference':maxdiff,
 'repeat_threshold':threshold,
 'all_values_finite':finite,
 'gate_pass':passed,
 'classification':'DVD_DL0_NUMERICAL_PILOT_PASS' if passed else 'DVD_DL0_NUMERICAL_PILOT_FAIL',
 'claim_lock':'This is one frozen symmetric Dl=0 term of source-labelled genuine two-vertex Lorentzian EPRL DVD2/DVD3 only; not full spin-sum, convergence, refinement, continuum, bridge or new physics.'
}
Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
