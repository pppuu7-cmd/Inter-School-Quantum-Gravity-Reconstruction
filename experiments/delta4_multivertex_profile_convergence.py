#!/usr/bin/env python3
"""Pinned multi-vertex Lorentzian EPRL Delta_4 convergence audit.

Consumes the public precomputed Delta_4 amplitudes from
PietropaoloFrisoni/HowToSpinFoamAmplitude.  Each CSV/TSV matrix has rows
Dl=0..Dl_max and columns for symmetric boundary-intertwiner choices.

Question fixed before inspecting aggregate results:
Does the *direction* of the boundary-intertwiner amplitude profile converge
under shell extension independently of the overall scalar amplitude norm?
This is a true multi-vertex diagnostic (four contracted EPRL vertices), but
it is not itself a coarse-graining/refinement map.
"""

from __future__ import annotations
import argparse, json, math, re
from pathlib import Path

DIR_TOL=5e-3
NORM_UNSETTLED=5e-2
EFFECTIVE_COMPONENTS_MIN=1.20


def norm(v): return math.sqrt(sum(x*x for x in v))
def cosine(a,b):
    na,nb=norm(a),norm(b)
    if na==0 or nb==0: return float('nan')
    return sum(x*y for x,y in zip(a,b))/(na*nb)

def effective_components(v):
    s=sum(abs(x) for x in v)
    if s==0: return 0.0
    p=[abs(x)/s for x in v]
    return 1.0/sum(x*x for x in p)

def parse_matrix(path):
    rows=[]
    for line in path.read_text().splitlines():
        if not line.strip(): continue
        vals=[float(x) for x in re.split(r'[\s,]+',line.strip()) if x]
        rows.append(vals)
    if not rows: raise ValueError(f'empty {path}')
    n=len(rows[0])
    if any(len(r)!=n for r in rows): raise ValueError(f'ragged {path}')
    return rows

def stable_shell(errors,tol):
    for i in range(len(errors)):
        tail=errors[i:]
        if all(math.isfinite(x) and x<=tol for x in tail): return i
    return None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-root',required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    root=Path(args.source_root)
    files=list(root.glob('Delta_4_ampls/Immirzi_*/j_*/CSV_format/Delta_4_ampls_Dl_max_*.csv'))
    if not files: raise SystemExit('no Delta_4 CSV data found')

    # Keep only largest Dl_max per (gamma,j) leaf.
    chosen={}
    pat=re.compile(r'Immirzi_([^/]+)/j_([^/]+)/CSV_format/Delta_4_ampls_Dl_max_(\d+)\.csv$')
    for f in files:
        m=pat.search(f.as_posix())
        if not m: continue
        g,j,d=float(m.group(1)),float(m.group(2)),int(m.group(3))
        key=(g,j)
        if key not in chosen or d>chosen[key][0]: chosen[key]=(d,f)

    datasets=[]
    for (g,j),(dmax,f) in sorted(chosen.items()):
        rows=parse_matrix(f)
        final=rows[-1]; nf=norm(final)
        dir_err=[]; norm_err=[]
        for v in rows:
            c=cosine(v,final)
            dir_err.append(float('inf') if not math.isfinite(c) else max(0.0,1.0-c))
            nv=norm(v)
            norm_err.append(abs(nv-nf)/max(nf,1e-300))
        dir_shell=stable_shell(dir_err,DIR_TOL)
        norm_shell=stable_shell(norm_err,DIR_TOL)
        eff=effective_components(final)
        witness=[]
        for dl,(de,ne) in enumerate(zip(dir_err,norm_err)):
            if de<=DIR_TOL and ne>=NORM_UNSETTLED:
                witness.append({'Dl':dl,'direction_error':de,'norm_relative_error':ne})
        lane=bool(len(final)>1 and eff>=EFFECTIVE_COMPONENTS_MIN and witness)
        shares=[]
        sa=sum(abs(x) for x in final)
        if sa>0: shares=[abs(x)/sa for x in final]
        datasets.append({
          'gamma':g,'j_boundary':j,'Dl_max':dmax,'n_rows':len(rows),'n_boundary_intertwiner_channels':len(final),
          'final_effective_components_L1_IPR':eff,
          'final_absolute_channel_shares':shares,
          'direction_stable_shell_tol_5e-3':dir_shell,
          'norm_stable_shell_tol_5e-3':norm_shell,
          'direction_stabilizes_before_norm':bool(dir_shell is not None and norm_shell is not None and dir_shell<norm_shell),
          'stable_direction_unsettled_norm_witnesses':witness,
          'multi_vertex_profile_lane_pass':lane,
          'direction_error_by_Dl':dir_err,
          'norm_relative_error_by_Dl':norm_err,
          'source_file':f.relative_to(root).as_posix(),
        })

    nontrivial=[d for d in datasets if d['n_boundary_intertwiner_channels']>1]
    passed=sum(d['multi_vertex_profile_lane_pass'] for d in nontrivial)
    natural=bool(nontrivial and passed>=math.ceil(len(nontrivial)/2))
    strong=bool(nontrivial and passed==len(nontrivial))
    out={
      'test':'LORENTZIAN_EPRL_DELTA4_MULTIVERTEX_PROFILE_CONVERGENCE',
      'status':'PASS_EXECUTION',
      'source_repository':'PietropaoloFrisoni/HowToSpinFoamAmplitude',
      'source_commit':'4fa7e31ffc6553e56da94a443a53a4059a5d2035',
      'preregistered_gate':{
        'direction_tol':DIR_TOL,
        'norm_unsettled_threshold':NORM_UNSETTLED,
        'effective_components_min':EFFECTIVE_COMPONENTS_MIN,
        'lane_pass':'more than one channel, final effective components >=1.20, and exists Dl with direction error <=0.005 while scalar norm error >=0.05',
        'natural_support':'lane pass in >= half of nontrivial datasets',
        'strong_support':'lane pass in all nontrivial datasets'
      },
      'n_datasets':len(datasets),'n_nontrivial_datasets':len(nontrivial),'lanes_passed':passed,
      'natural_multivertex_profile_support':natural,
      'strong_multivertex_profile_support':strong,
      'datasets':datasets,
      'interpretation_lock':'Positive result shows that a multi-vertex Lorentzian EPRL boundary-intertwiner profile can stabilize in direction while its scalar normalization is still cutoff-sensitive. This is evidence for retained-sector information beyond one scalar amplitude, not evidence of new physics and not a genuine coarse/fine refinement map.'
    }
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
