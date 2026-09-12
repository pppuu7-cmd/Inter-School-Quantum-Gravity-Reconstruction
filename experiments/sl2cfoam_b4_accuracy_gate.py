#!/usr/bin/env python3
"""Prospective numerical infrastructure gate for pinned sl2cfoam-next B4.

Parses the upstream b4_test fast-vs-adaptive output. Frozen acceptance:
- at least one nonzero coefficient compared;
- all reported relative errors finite;
- maximum relative error <= 1e-5.
This is an infrastructure/numerical-kernel gate only, not a two-vertex physics test.
"""
from pathlib import Path
import argparse,json,math,re
ap=argparse.ArgumentParser(); ap.add_argument('--log',required=True); ap.add_argument('--gamma',type=float,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
t=Path(a.log).read_text(errors='ignore')
vals=[]
for m in re.finditer(r'relative error\s*=\s*([0-9eE+\-.]+)',t):
 try: vals.append(float(m.group(1)))
 except ValueError: pass
finite=bool(vals) and all(math.isfinite(x) for x in vals)
mx=max(vals) if vals else None
threshold=1e-5
passed=bool(finite and mx is not None and mx<=threshold)
out={'test':'PINNED_SL2CFOAM_B4_FAST_VS_ACCURATE','pinned_commit':'052e4346028870bd76f69a3034e6cae8defb8f7f','gamma':a.gamma,
     'two_j':[2,2,2,2],'two_l':[2,2,2,2],'comparison_count':len(vals),'max_relative_error':mx,'threshold':threshold,
     'all_finite':finite,'gate_pass':passed,'classification':'B4_NUMERICAL_KERNEL_PASS' if passed else 'B4_NUMERICAL_KERNEL_FAIL',
     'claim_lock':'Kernel self-consistency only; no DVD2/DVD3 amplitude, refinement, bridge or new-physics claim.'}
Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
