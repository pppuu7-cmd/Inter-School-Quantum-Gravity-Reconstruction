#!/usr/bin/env python3
"""Lorentzian EPRL Delta_4 multi-vertex shell-flow contractivity audit.

This is a stronger follow-up to the static boundary-profile convergence test.
It asks whether successive normalized boundary-intertwiner profiles form a
contracting shell flow as the booster cutoff Dl is enlarged.

Scope lock: four contracted EPRL vertices from the pinned public Delta_4 data.
This is a cutoff-shell flow diagnostic, not a genuine coarse/fine refinement
map and not evidence of new physics.
"""
from __future__ import annotations
import argparse, json, math, re, statistics
from pathlib import Path

SOURCE_COMMIT = "4fa7e31ffc6553e56da94a443a53a4059a5d2035"
TAIL_FRACTION = 0.40
CONTRACTION_RATIO_MAX = 0.50
TAIL_DIRECTION_ERROR_MAX = 5e-3
MONOTONE_FRACTION_MIN = 0.60
MIN_TRANSITIONS = 5


def l2(v):
    return math.sqrt(sum(x*x for x in v))


def unit(v):
    n=l2(v)
    if n == 0:
        return None
    return [x/n for x in v]


def cosine(a,b):
    return max(-1.0,min(1.0,sum(x*y for x,y in zip(a,b))))


def parse_matrix(path):
    rows=[]
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        vals=[float(x) for x in re.split(r'[\s,]+', line.strip()) if x]
        rows.append(vals)
    if not rows:
        raise ValueError(f"empty {path}")
    n=len(rows[0])
    if any(len(r)!=n for r in rows):
        raise ValueError(f"ragged {path}")
    return rows


def select_datasets(root):
    files=list(root.glob('Delta_4_ampls/Immirzi_*/j_*/CSV_format/Delta_4_ampls_Dl_max_*.csv'))
    pat=re.compile(r'Immirzi_([^/]+)/j_([^/]+)/CSV_format/Delta_4_ampls_Dl_max_(\d+)\.csv$')
    chosen={}
    for f in files:
        m=pat.search(f.as_posix())
        if not m:
            continue
        g,j,d=float(m.group(1)),float(m.group(2)),int(m.group(3))
        key=(g,j)
        if key not in chosen or d > chosen[key][0]:
            chosen[key]=(d,f)
    return [(g,j,d,f) for (g,j),(d,f) in sorted(chosen.items())]


def audit_one(g,j,dmax,path,root):
    rows=parse_matrix(path)
    u=[unit(r) for r in rows]
    valid=[x for x in u if x is not None]
    if len(valid) != len(rows) or len(rows) < MIN_TRANSITIONS+1 or len(rows[0]) < 2:
        return {
            'gamma':g,'j_boundary':j,'Dl_max':dmax,
            'n_rows':len(rows),'n_channels':len(rows[0]),
            'eligible':False,'lane_pass':False,
            'source_file':path.relative_to(root).as_posix()
        }

    final=u[-1]
    step_errors=[max(0.0,1.0-cosine(u[k],u[k+1])) for k in range(len(u)-1)]
    final_errors=[max(0.0,1.0-cosine(x,final)) for x in u]
    n=len(step_errors)
    tail_n=max(2,int(math.ceil(TAIL_FRACTION*n)))
    head_n=max(2,min(n-tail_n,tail_n))
    head=step_errors[:head_n]
    tail=step_errors[-tail_n:]
    head_med=statistics.median(head)
    tail_med=statistics.median(tail)
    ratio=tail_med/max(head_med,1e-300)
    monotone=sum(step_errors[k+1] <= step_errors[k] for k in range(n-1))/max(n-1,1)
    tail_final=max(final_errors[-tail_n:])

    # Held-out one-step prediction: profile at Dl predicts Dl+1 by persistence.
    # Compare with a label-destroying cyclic-shift null of identical norm.
    pred_err=[]
    null_err=[]
    for k in range(1,len(u)):
        pred=max(0.0,1.0-cosine(u[k-1],u[k]))
        shifted=u[k-1][1:]+u[k-1][:1]
        nul=max(0.0,1.0-cosine(shifted,u[k]))
        pred_err.append(pred); null_err.append(nul)
    better_fraction=sum(a < b for a,b in zip(pred_err,null_err))/len(pred_err)

    lane_pass=bool(
        ratio <= CONTRACTION_RATIO_MAX and
        monotone >= MONOTONE_FRACTION_MIN and
        tail_final <= TAIL_DIRECTION_ERROR_MAX and
        better_fraction >= 0.80
    )
    return {
        'gamma':g,'j_boundary':j,'Dl_max':dmax,
        'n_rows':len(rows),'n_channels':len(rows[0]),'eligible':True,
        'step_direction_errors':step_errors,
        'final_direction_errors':final_errors,
        'head_median_step_error':head_med,
        'tail_median_step_error':tail_med,
        'tail_to_head_contraction_ratio':ratio,
        'fraction_nonincreasing_step_error':monotone,
        'tail_max_final_direction_error':tail_final,
        'persistence_beats_cyclic_label_null_fraction':better_fraction,
        'lane_pass':lane_pass,
        'source_file':path.relative_to(root).as_posix()
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-root',required=True)
    ap.add_argument('--lane',type=int,required=True)
    ap.add_argument('--lanes',type=int,default=8)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    root=Path(args.source_root)
    ds=select_datasets(root)
    assigned=[x for idx,x in enumerate(ds) if idx % args.lanes == args.lane]
    results=[audit_one(*x,root) for x in assigned]
    eligible=[r for r in results if r['eligible']]
    passed=sum(r['lane_pass'] for r in eligible)
    out={
        'test':'LORENTZIAN_EPRL_DELTA4_MULTIVERTEX_SHELLFLOW_CONTRACTIVITY',
        'source_repository':'PietropaoloFrisoni/HowToSpinFoamAmplitude',
        'source_commit':SOURCE_COMMIT,
        'lane':args.lane,'lanes':args.lanes,
        'n_assigned':len(results),'n_eligible':len(eligible),'n_passed':passed,
        'preregistered_gate':{
            'tail_fraction':TAIL_FRACTION,
            'tail_to_head_contraction_ratio_max':CONTRACTION_RATIO_MAX,
            'fraction_nonincreasing_step_error_min':MONOTONE_FRACTION_MIN,
            'tail_max_final_direction_error_max':TAIL_DIRECTION_ERROR_MAX,
            'persistence_beats_cyclic_label_null_fraction_min':0.80,
            'lane_pass':'all four criteria simultaneously'
        },
        'results':results,
        'claim_lock':'A positive lane supports a contracting cutoff-shell flow of a true multi-vertex Lorentzian EPRL boundary profile. It is not a coarse/fine refinement map, does not derive BH-004B, and does not establish continuum quantum gravity or new physics.'
    }
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
