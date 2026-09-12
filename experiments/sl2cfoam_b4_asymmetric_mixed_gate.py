#!/usr/bin/env python3
from pathlib import Path
import argparse,json,math,re
ap=argparse.ArgumentParser(); ap.add_argument('--log',required=True); ap.add_argument('--gamma',type=float,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
text=Path(a.log).read_text(errors='ignore')
configs=re.findall(r'^=== CONFIG ([A-F]) ===$',text,re.M)
errs=[]
for m in re.finditer(r'relative error\s*=\s*([0-9eE+\-.]+)',text):
    try: errs.append(float(m.group(1)))
    except ValueError: pass
finite=bool(errs) and all(math.isfinite(x) for x in errs)
mx=max(errs) if errs else None
threshold=1e-5
ok=(configs==list('ABCDEF') and finite and mx is not None and mx<=threshold)
out={'test':'PINNED_SL2CFOAM_B4_ASYMMETRIC_MIXED_FAST_VS_ACCURATE','gamma':a.gamma,
     'pinned_commit':'052e4346028870bd76f69a3034e6cae8defb8f7f','config_sequence':configs,
     'comparison_count':len(errs),'max_relative_error':mx,'threshold':threshold,'all_finite':finite,'gate_pass':ok,
     'classification':'B4_ASYMMETRIC_MIXED_KERNEL_PASS' if ok else 'B4_ASYMMETRIC_MIXED_KERNEL_FAIL',
     'claim_lock':'Representative source-relevant mixed-spin B4 primitive validation only; no asymmetric DVD amplitude, refinement, continuum, bridge or novelty claim.'}
Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)
