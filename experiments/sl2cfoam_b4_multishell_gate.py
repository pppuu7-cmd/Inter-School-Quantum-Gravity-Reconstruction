#!/usr/bin/env python3
"""Prospective multi-shell numerical validity gate for the pinned Lorentzian EPRL B4 primitive.

This tests the upstream sl2cfoam-next fast-vs-adaptive B4 implementation for a
source-relevant uniform shell slice j_a=1, l_a=1+Delta l. It is deliberately a
kernel diagnostic only: no DVD2/DVD3 shell sum, convergence, refinement or bridge
claim is licensed by PASS.
"""
from pathlib import Path
import argparse, json, math, re

ap=argparse.ArgumentParser()
ap.add_argument('--log',required=True)
ap.add_argument('--gamma',type=float,required=True)
ap.add_argument('--dl',type=int,required=True)
ap.add_argument('--output',required=True)
a=ap.parse_args()

text=Path(a.log).read_text(errors='ignore')
vals=[]
for m in re.finditer(r'relative error\s*=\s*([0-9eE+\-.]+)', text):
    try: vals.append(float(m.group(1)))
    except ValueError: pass
finite=bool(vals) and all(math.isfinite(x) for x in vals)
mx=max(vals) if vals else None
threshold=1e-5
passed=bool(a.dl >= 0 and finite and mx is not None and mx <= threshold)
two_l=2+2*a.dl
out={
  'test':'PINNED_SL2CFOAM_B4_UNIFORM_MULTISHELL_FAST_VS_ACCURATE',
  'pinned_commit':'052e4346028870bd76f69a3034e6cae8defb8f7f',
  'gamma':a.gamma,
  'delta_l':a.dl,
  'two_j':[2,2,2,2],
  'two_l':[two_l,two_l,two_l,two_l],
  'comparison_count':len(vals),
  'max_relative_error':mx,
  'threshold':threshold,
  'all_finite':finite,
  'gate_pass':passed,
  'classification':'B4_MULTISHELL_NUMERICAL_KERNEL_PASS' if passed else 'B4_MULTISHELL_NUMERICAL_KERNEL_FAIL',
  'claim_lock':'Uniform-shell B4 numerical primitive only. No DVD2/DVD3 multi-shell amplitude, shell-sum convergence, refinement map, bridge, continuum or novelty claim.'
}
Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
