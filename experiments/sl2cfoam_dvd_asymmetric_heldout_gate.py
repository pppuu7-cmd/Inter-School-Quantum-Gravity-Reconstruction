#!/usr/bin/env python3
import argparse,json,math,re
from pathlib import Path
ROW=re.compile(r'^D=(\d+)\s+dvd2=([^\s]+)\s+dvd3=([^\s]+)\s+terms2=(\d+)\s+nonzero2=(\d+)\s+terms3=(\d+)\s+nonzero3=(\d+)\s+cache=(\d+)\s*$')
def parse(p):
    o={}
    for line in Path(p).read_text().splitlines():
        m=ROW.match(line.strip())
        if m:o[int(m.group(1))]={'dvd2':float(m.group(2)),'dvd3':float(m.group(3)),'terms2':int(m.group(4)),'nonzero2':int(m.group(5)),'terms3':int(m.group(6)),'nonzero3':int(m.group(7)),'cache':int(m.group(8))}
    return o
def rel(a,b):return abs(a-b)/max(abs(a),abs(b),1e-300)
ap=argparse.ArgumentParser();ap.add_argument('--run1',required=True);ap.add_argument('--run2',required=True);ap.add_argument('--gamma',type=float,required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
r1,r2=parse(a.run1),parse(a.run2);Ds=[0,1,2];shape=sorted(r1)==Ds and sorted(r2)==Ds
finite=shape and all(math.isfinite(r1[D][k]) and math.isfinite(r2[D][k]) for D in Ds for k in ('dvd2','dvd3'))
repeat=max([rel(r1[D][k],r2[D][k]) for D in Ds for k in ('dvd2','dvd3')]) if shape else float('inf')
diag=[]
for D in Ds if shape else []:
    x,y=r1[D]['dvd2'],r1[D]['dvd3'];diag.append({'D':D,'dvd2':x,'dvd3':y,'dvd2_over_dvd3':x/y if y else None,'normalized_split':rel(x,y),'dvd2_relative_increment':None if D==0 else rel(x,r1[D-1]['dvd2']),'dvd3_relative_increment':None if D==0 else rel(y,r1[D-1]['dvd3']),'terms2':r1[D]['terms2'],'nonzero2':r1[D]['nonzero2'],'terms3':r1[D]['terms3'],'nonzero3':r1[D]['nonzero3']})
pattern=bool(shape and diag[2]['dvd2_relative_increment']<diag[1]['dvd2_relative_increment'] and diag[2]['dvd3_relative_increment']<diag[1]['dvd3_relative_increment'])
numerical=bool(shape and finite and repeat<=1e-12)
out={'test':'LORENTZIAN_EPRL_DVD_ASYMMETRIC_HELDOUT_GAMMA','gamma':a.gamma,'numerical_gate_pass':numerical,'repeat_max_relative_difference':repeat,'heldout_stabilization_pattern_pass':pattern,'diagnostics':diag,'classification':'DVD_ASYMMETRIC_HELDOUT_LANE_PASS' if numerical else 'DVD_ASYMMETRIC_HELDOUT_LANE_NUMERICAL_FAIL','claim_lock':'Asymmetric heldout pattern support is finite-cutoff robustness only; not convergence, refinement, continuum, bridge, novelty or new physics.'}
Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
if not numerical:raise SystemExit(2)
