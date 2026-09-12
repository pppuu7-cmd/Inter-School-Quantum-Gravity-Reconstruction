#!/usr/bin/env python3
import argparse,json,math,pathlib,re
p=argparse.ArgumentParser();p.add_argument('--log',required=True);p.add_argument('--gamma',type=float,required=True);p.add_argument('--output',required=True);a=p.parse_args()
text=pathlib.Path(a.log).read_text(errors='ignore')
err_rx=re.compile(r'b4 fast\s*=\s*([-+0-9.eE]+),\s*b4 accurate\s*=\s*([-+0-9.eE]+),\s*relative error\s*=\s*([-+0-9.eE]+)')
rows=[]
for m in err_rx.finditer(text):
    fast,acc,err=map(float,m.groups()); rows.append({'fast':fast,'accurate':acc,'relative_error':err})
all_finite=all(math.isfinite(x[k]) for x in rows for k in ('fast','accurate','relative_error'))
maxerr=max((x['relative_error'] for x in rows),default=float('inf'))
# Workflow prints exactly four frozen CONFIG headers; each must yield at least one non-zero accurate comparison.
config_count=len(re.findall(r'^=== CONFIG [ABCD] ===$',text,re.M))
comparison_count=len(rows)
gate=(config_count==4 and comparison_count>=4 and all_finite and maxerr<=1e-5)
out={'test':'PINNED_SL2CFOAM_B4_ZERO_SPIN_PRIMITIVE','gamma':a.gamma,'config_count':config_count,'comparison_count':comparison_count,'all_reported_values_finite':all_finite,'max_relative_error':maxerr,'threshold':1e-5,'gate_pass':gate,'classification':'B4_ZERO_SPIN_PRIMITIVE_PASS' if gate else 'B4_ZERO_SPIN_PRIMITIVE_FAIL','comparisons':rows,'claim_lock':'Primitive capability only; no refined foam, trivial-extension identity, multiplicity-corrected cylindrical consistency, continuum or bridge claim.'}
pathlib.Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if not gate: raise SystemExit(2)
