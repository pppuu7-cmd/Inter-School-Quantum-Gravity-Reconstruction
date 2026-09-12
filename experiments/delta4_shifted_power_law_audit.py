#!/usr/bin/env python3
"""ISQGR Delta4 shifted power-law convergence audit.

Follow-up to the shellflow convergence-law audit, where a plain power law
out-predicted a simple exponential in every eligible pinned Delta4 sector.
This experiment asks whether the apparent sector dependence of the plain
power exponent is largely a finite-cutoff transient that can be absorbed by
a shift D0:

    e(D) = A (D + D0)^(-alpha),  D0 >= 0.

Four preregistered train/holdout splits are evaluated independently for each
of the six available (gamma,j) datasets. D0 is selected using training data
only by a deterministic grid search; held-out errors are then compared with
plain power and exponential baselines.

Scope lock: this diagnoses booster-cutoff convergence in pinned four-vertex
Lorentzian EPRL Delta4 amplitudes. It is not a physical coarse/fine map.
"""
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path

SOURCE_COMMIT = "4fa7e31ffc6553e56da94a443a53a4059a5d2035"
ERROR_FLOOR = 1e-16
SPLITS = (0.45, 0.55, 0.65, 0.75)
D0_GRID = tuple(i/10.0 for i in range(0, 201))  # [0,20] preregistered


def l2(v): return math.sqrt(sum(x*x for x in v))
def unit(v):
    n=l2(v); return None if n == 0 else [x/n for x in v]
def cosine(a,b): return max(-1.0,min(1.0,sum(x*y for x,y in zip(a,b))))

def parse_matrix(path):
    rows=[]
    for line in path.read_text().splitlines():
        if not line.strip(): continue
        rows.append([float(x) for x in re.split(r'[\s,]+',line.strip()) if x])
    if not rows or any(len(r)!=len(rows[0]) for r in rows):
        raise ValueError(f"invalid matrix {path}")
    return rows

def select_datasets(root):
    files=list(root.glob('Delta_4_ampls/Immirzi_*/j_*/CSV_format/Delta_4_ampls_Dl_max_*.csv'))
    pat=re.compile(r'Immirzi_([^/]+)/j_([^/]+)/CSV_format/Delta_4_ampls_Dl_max_(\d+)\.csv$')
    chosen={}
    for f in files:
        m=pat.search(f.as_posix())
        if not m: continue
        g,j,d=float(m.group(1)),float(m.group(2)),int(m.group(3))
        if (g,j) not in chosen or d > chosen[(g,j)][0]: chosen[(g,j)]=(d,f)
    return [(g,j,d,f) for (g,j),(d,f) in sorted(chosen.items())]

def linfit(xs,ys):
    n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
    sxx=sum((x-mx)**2 for x in xs)
    if sxx <= 0: return my,0.0
    b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sxx
    return my-b*mx,b

def mae(a,b): return sum(abs(x-y) for x,y in zip(a,b))/len(a)

def fit_shifted(xs,ys):
    best=None
    for d0 in D0_GRID:
        tx=[math.log(x+1.0+d0) for x in xs]
        a,b=linfit(tx,ys)
        pred=[a+b*z for z in tx]
        score=mae(pred,ys)
        # require contracting model; deterministic tie break to smaller d0
        if b >= 0: continue
        cand=(score,d0,a,b)
        if best is None or cand < best: best=cand
    return best

def audit(dataset, split_fraction, root):
    g,j,dmax,path=dataset
    rows=parse_matrix(path); u=[unit(r) for r in rows]
    if any(x is None for x in u): raise ValueError('zero row')
    e=[max(ERROR_FLOOR,1.0-cosine(u[k],u[k+1])) for k in range(len(u)-1)]
    xs=list(range(len(e))); ys=[math.log(x) for x in e]
    ntrain=max(5,min(len(e)-3,int(math.floor(split_fraction*len(e)))))
    tr=list(range(ntrain)); te=list(range(ntrain,len(e)))
    xtr=[xs[k] for k in tr]; ytr=[ys[k] for k in tr]
    xte=[xs[k] for k in te]; yte=[ys[k] for k in te]

    aexp,bexp=linfit(xtr,ytr)
    apow,bpow=linfit([math.log(x+1.0) for x in xtr],ytr)
    sh=fit_shifted(xtr,ytr)
    if sh is None: raise RuntimeError('no contracting shifted fit')
    train_mae,d0,ash,bsh=sh
    exp_mae=mae([aexp+bexp*x for x in xte],yte)
    pow_mae=mae([apow+bpow*math.log(x+1.0) for x in xte],yte)
    sh_mae=mae([ash+bsh*math.log(x+1.0+d0) for x in xte],yte)
    best_baseline=min(exp_mae,pow_mae)
    advantage=(best_baseline-sh_mae)/max(best_baseline,1e-12)
    return {
      'gamma':g,'j_boundary':j,'Dl_max':dmax,'split_fraction':split_fraction,
      'n_transitions':len(e),'n_train':ntrain,'n_holdout':len(te),
      'shift_d0':d0,'shifted_alpha':-bsh,'shifted_train_log_mae':train_mae,
      'heldout_log_mae_shifted':sh_mae,'heldout_log_mae_power':pow_mae,
      'heldout_log_mae_exponential':exp_mae,
      'shifted_advantage_vs_best_baseline':advantage,
      'shifted_preferred_10pct':bool(advantage >= 0.10),
      'plain_power_alpha':-bpow,'exponential_decay':-bexp,
      'source_file':path.relative_to(root).as_posix()
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-root',required=True)
    ap.add_argument('--lane',type=int,required=True); ap.add_argument('--lanes',type=int,default=24)
    ap.add_argument('--output',required=True); args=ap.parse_args()
    root=Path(args.source_root); ds=select_datasets(root)
    if len(ds)!=6: raise RuntimeError(f'expected 6 datasets, found {len(ds)}')
    tasks=[(d,s) for s in SPLITS for d in ds]
    assigned=[t for i,t in enumerate(tasks) if i%args.lanes==args.lane]
    results=[audit(d,s,root) for d,s in assigned]
    out={'test':'LORENTZIAN_EPRL_DELTA4_SHIFTED_POWER_LAW_AUDIT',
         'source_repository':'PietropaoloFrisoni/HowToSpinFoamAmplitude',
         'source_commit':SOURCE_COMMIT,'lane':args.lane,'lanes':args.lanes,
         'd0_grid':[0.0,20.0,0.1],'splits':SPLITS,'results':results,
         'claim_lock':'Positive support would establish only a transferable empirical booster-cutoff convergence law in pinned Delta4 data, not a continuum RG flow, coarse/fine map, or new physics.'}
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
