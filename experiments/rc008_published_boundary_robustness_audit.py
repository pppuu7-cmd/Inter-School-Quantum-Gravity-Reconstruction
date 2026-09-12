#!/usr/bin/env python3
"""Source-data robustness audit for quantum-cuboid hypercuboidal renormalization.

This is NOT a re-computation of the 16-hypercuboid path integral.  It takes the
boundary-specific RG fixed points alpha_* and vertex-translation critical
values alpha_c reported in Bahr & Steinhaus, arXiv:1701.02311, and computes
simple source-data diagnostics before an amplitude-level reproduction is built.

Published values used (paper Sec. V.1-V.2):
  regular X=Y=Z=T=1: alpha_* ~0.628; alpha_c ~0.60667
  T=3:                alpha_*  0.662; alpha_c  0.549942
  X=3:                alpha_*  0.614; alpha_c  0.557808
  X=3,Y=5:            alpha_*  0.607; alpha_c  0.539846

The audit asks how stable alpha_* is across boundary/truncation choices and
whether alpha_* and alpha_c should be treated as identical quantities.
"""
from __future__ import annotations
import json, argparse, statistics, math
from pathlib import Path

ROWS=[
    {"boundary":"X=Y=Z=T=1","alpha_star":0.628,"alpha_c":0.60667},
    {"boundary":"X=Y=Z=1,T=3","alpha_star":0.662,"alpha_c":0.549942},
    {"boundary":"X=3,Y=Z=T=1","alpha_star":0.614,"alpha_c":0.557808},
    {"boundary":"X=3,Y=5,Z=T=1","alpha_star":0.607,"alpha_c":0.539846},
]

def pearson(xs,ys):
    xm=statistics.fmean(xs); ym=statistics.fmean(ys)
    num=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))
    den=math.sqrt(sum((x-xm)**2 for x in xs)*sum((y-ym)**2 for y in ys))
    return num/den if den else float('nan')

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    stars=[r['alpha_star'] for r in ROWS]; cs=[r['alpha_c'] for r in ROWS]
    enriched=[]
    for r in ROWS:
        d=abs(r['alpha_star']-r['alpha_c'])
        m=(abs(r['alpha_star'])+abs(r['alpha_c']))/2
        enriched.append({**r,"abs_gap":d,"relative_gap":d/m})
    mean=statistics.fmean(stars); sd=statistics.stdev(stars)
    out={
      "test":"RC008_PUBLISHED_BOUNDARY_ROBUSTNESS_AUDIT",
      "status":"PASS_EXECUTION",
      "n_boundary_states":len(ROWS),
      "alpha_star":{
        "mean":mean,"stdev":sd,"coefficient_of_variation":sd/mean,
        "min":min(stars),"max":max(stars),"range":max(stars)-min(stars),
        "max_relative_deviation_from_mean":max(abs(x-mean)/mean for x in stars),
      },
      "alpha_star_vs_alpha_c":{
        "median_abs_gap":statistics.median(r['abs_gap'] for r in enriched),
        "median_relative_gap":statistics.median(r['relative_gap'] for r in enriched),
        "max_abs_gap":max(r['abs_gap'] for r in enriched),
        "pearson_descriptive_only_n4":pearson(stars,cs),
        "all_exactly_equal":all(r['abs_gap']<1e-12 for r in enriched),
      },
      "by_boundary":enriched,
      "interpretation_lock":"Published-data audit only. Small-n correlation is descriptive. alpha_* and alpha_c arise from different diagnostics and must not be identified merely because some values are numerically close.",
      "source":"Bahr & Steinhaus, Hypercuboidal renormalization in spin foam quantum gravity, arXiv:1701.02311, Sec. V.1-V.2."
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
