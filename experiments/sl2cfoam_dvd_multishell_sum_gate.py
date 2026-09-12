#!/usr/bin/env python3
import argparse,json,math,re
from pathlib import Path

REF={
  0.5:5.496983896037186e-4,
  1.2:1.2780379206216302e-5,
  2.0:3.7591052442651034e-7,
}
ROW=re.compile(r'^D=(\d+)\s+dvd2=([^\s]+)\s+dvd3=([^\s]+)\s+terms2=(\d+)\s+nonzero2=(\d+)\s+terms3=(\d+)\s+nonzero3=(\d+)\s+cache=(\d+)\s*$')

def parse(p):
    rows={}
    for line in Path(p).read_text().splitlines():
        m=ROW.match(line.strip())
        if not m: continue
        D=int(m.group(1)); rows[D]={
          'dvd2':float(m.group(2)),'dvd3':float(m.group(3)),
          'terms2':int(m.group(4)),'nonzero2':int(m.group(5)),
          'terms3':int(m.group(6)),'nonzero3':int(m.group(7)),'cache':int(m.group(8))}
    return rows

def rel(a,b): return abs(a-b)/max(abs(a),abs(b),1e-300)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--run1',required=True); ap.add_argument('--run2',required=True); ap.add_argument('--gamma',type=float,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    r1=parse(a.run1); r2=parse(a.run2)
    expected_D=[0,1,2]
    shape_ok=(sorted(r1)==expected_D and sorted(r2)==expected_D)
    allfinite=shape_ok and all(math.isfinite(r1[D][k]) and math.isfinite(r2[D][k]) for D in expected_D for k in ('dvd2','dvd3'))
    repeats=[]
    if shape_ok:
        for D in expected_D:
            for k in ('dvd2','dvd3'): repeats.append(rel(r1[D][k],r2[D][k]))
    repeat_max=max(repeats) if repeats else float('inf')
    ref=REF[a.gamma]
    d0err=max(rel(r1[0]['dvd2'],ref),rel(r1[0]['dvd3'],ref)) if shape_ok else float('inf')
    diag=[]
    if shape_ok:
        for D in expected_D:
            x=r1[D]['dvd2']; y=r1[D]['dvd3']
            diag.append({
              'D':D,'dvd2':x,'dvd3':y,
              'dvd2_over_dvd3': x/y if y!=0 else None,
              'normalized_split':abs(x-y)/max(abs(x),abs(y),1e-300),
              'dvd2_relative_increment': None if D==0 else rel(x,r1[D-1]['dvd2']),
              'dvd3_relative_increment': None if D==0 else rel(y,r1[D-1]['dvd3']),
              'terms2':r1[D]['terms2'],'nonzero2':r1[D]['nonzero2'],'terms3':r1[D]['terms3'],'nonzero3':r1[D]['nonzero3'],
              'cache_entries':r1[D]['cache']})
    gate=bool(shape_ok and allfinite and repeat_max<=1e-12 and d0err<=1e-12)
    out={
      'test':'LORENTZIAN_EPRL_DVD_FINITE_MULTISHELL_SUM', 'gamma':a.gamma,
      'shape_pass':shape_ok,'finite_pass':allfinite,
      'repeat_max_relative_difference':repeat_max,'repeat_gate':repeat_max<=1e-12,
      'dl0_reference':ref,'dl0_max_relative_error':d0err,'dl0_regression_gate':d0err<=1e-12,
      'diagnostics':diag,'gate_pass':gate,
      'classification':'DVD_FINITE_MULTISHELL_SUM_PASS' if gate else 'DVD_FINITE_MULTISHELL_SUM_FAIL',
      'claim_lock':'Finite source-labelled shell-sum diagnostic only. No convergence-direction, refinement-map, cylindrical-consistency, continuum, bridge, novelty, or new-physics claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not gate: raise SystemExit(2)
if __name__=='__main__': main()
