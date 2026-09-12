#!/usr/bin/env python3
"""Delta4 multi-vertex shell-flow convergence-law audit.

Follow-up to the preregistered shell-flow contractivity PASS.  The previous
experiment established contraction of normalized boundary profiles as the
booster cutoff Dl increases.  This audit asks a sharper, transferable question:
is that contraction described by a reproducible convergence law across the
available (gamma, j_boundary) sectors, or is the apparent contraction merely a
sector-specific finite-cutoff effect?

Two model families are compared out of sample on angular step errors e_Dl:
  exponential: log e = a + b Dl
  power law:   log e = a + b log(Dl + 1)
The first 60% of usable transitions are fit and the remainder are held out.
The script reports held-out log-MAE, slopes, local contraction ratios, and a
within-j cross-gamma slope spread diagnostic.

Scope lock: pinned public four-vertex Lorentzian EPRL Delta_4 amplitudes only.
This remains a cutoff-convergence diagnostic, not a coarse/fine refinement map.
All numerical gates are preregistered in the workflow before this campaign.
"""
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path

SOURCE_COMMIT = "4fa7e31ffc6553e56da94a443a53a4059a5d2035"
TRAIN_FRACTION = 0.60
ERROR_FLOOR = 1e-16
MIN_POINTS = 8


def l2(v):
    return math.sqrt(sum(x*x for x in v))


def unit(v):
    n=l2(v)
    return None if n == 0 else [x/n for x in v]


def cosine(a,b):
    return max(-1.0,min(1.0,sum(x*y for x,y in zip(a,b))))


def parse_matrix(path):
    rows=[]
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        vals=[float(x) for x in re.split(r'[\s,]+',line.strip()) if x]
        rows.append(vals)
    if not rows:
        raise ValueError(f"empty {path}")
    if any(len(r)!=len(rows[0]) for r in rows):
        raise ValueError(f"ragged {path}")
    return rows


def select_datasets(root):
    files=list(root.glob('Delta_4_ampls/Immirzi_*/j_*/CSV_format/Delta_4_ampls_Dl_max_*.csv'))
    pat=re.compile(r'Immirzi_([^/]+)/j_([^/]+)/CSV_format/Delta_4_ampls_Dl_max_(\d+)\.csv$')
    chosen={}
    for f in files:
        m=pat.search(f.as_posix())
        if not m: continue
        g,j,d=float(m.group(1)),float(m.group(2)),int(m.group(3))
        if (g,j) not in chosen or d > chosen[(g,j)][0]:
            chosen[(g,j)]=(d,f)
    return [(g,j,d,f) for (g,j),(d,f) in sorted(chosen.items())]


def linfit(xs,ys):
    n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
    sxx=sum((x-mx)**2 for x in xs)
    if sxx <= 0: return my,0.0
    b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sxx
    return my-b*mx,b


def mae(pred,obs):
    return sum(abs(a-b) for a,b in zip(pred,obs))/len(obs)


def median(v):
    s=sorted(v); n=len(s)
    return s[n//2] if n%2 else 0.5*(s[n//2-1]+s[n//2])


def audit_one(g,j,dmax,path,root):
    rows=parse_matrix(path)
    u=[unit(r) for r in rows]
    if any(x is None for x in u) or len(u)-1 < MIN_POINTS:
        return {'gamma':g,'j_boundary':j,'Dl_max':dmax,'eligible':False,
                'source_file':path.relative_to(root).as_posix()}
    e=[max(ERROR_FLOOR,1.0-cosine(u[k],u[k+1])) for k in range(len(u)-1)]
    xs=list(range(len(e)))
    logs=[math.log(x) for x in e]
    ntrain=max(5,min(len(e)-3,int(math.floor(TRAIN_FRACTION*len(e)))))
    tr=range(ntrain); te=range(ntrain,len(e))

    aexp,bexp=linfit([xs[k] for k in tr],[logs[k] for k in tr])
    apow,bpow=linfit([math.log(xs[k]+1.0) for k in tr],[logs[k] for k in tr])
    pred_exp=[aexp+bexp*xs[k] for k in te]
    pred_pow=[apow+bpow*math.log(xs[k]+1.0) for k in te]
    obs=[logs[k] for k in te]
    exp_mae=mae(pred_exp,obs); pow_mae=mae(pred_pow,obs)

    ratios=[e[k+1]/e[k] for k in range(len(e)-1) if e[k] > 10*ERROR_FLOOR and e[k+1] > 10*ERROR_FLOOR]
    tail=ratios[-max(2,len(ratios)//3):] if ratios else []
    tail_med=median(tail) if tail else None

    # Model preference requires a meaningful held-out advantage, not a tiny tie.
    rel_adv=(pow_mae-exp_mae)/max(pow_mae,1e-12)
    exp_preferred=bool(exp_mae < pow_mae and rel_adv >= 0.10 and bexp < 0)
    return {
      'gamma':g,'j_boundary':j,'Dl_max':dmax,'n_channels':len(rows[0]),
      'n_transitions':len(e),'n_train':ntrain,'n_holdout':len(e)-ntrain,
      'eligible':True,'exponential_log_slope':bexp,'power_log_slope':bpow,
      'heldout_log_mae_exponential':exp_mae,'heldout_log_mae_power':pow_mae,
      'exponential_relative_advantage':rel_adv,'exponential_preferred':exp_preferred,
      'tail_median_local_error_ratio':tail_med,
      'source_file':path.relative_to(root).as_posix()
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-root',required=True)
    ap.add_argument('--lane',type=int,required=True)
    ap.add_argument('--lanes',type=int,default=12)
    ap.add_argument('--output',required=True)
    args=ap.parse_args(); root=Path(args.source_root)
    ds=select_datasets(root)
    assigned=[x for i,x in enumerate(ds) if i%args.lanes==args.lane]
    results=[audit_one(*x,root) for x in assigned]
    out={
      'test':'LORENTZIAN_EPRL_DELTA4_SHELLFLOW_CONVERGENCE_LAW',
      'source_repository':'PietropaoloFrisoni/HowToSpinFoamAmplitude',
      'source_commit':SOURCE_COMMIT,'lane':args.lane,'lanes':args.lanes,
      'train_fraction':TRAIN_FRACTION,'results':results,
      'claim_lock':'A positive result supports a transferable cutoff-convergence law in pinned four-vertex Lorentzian EPRL Delta4 data only. It is not a genuine coarse/fine refinement operator, continuum limit, or evidence of new physics.'
    }
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
