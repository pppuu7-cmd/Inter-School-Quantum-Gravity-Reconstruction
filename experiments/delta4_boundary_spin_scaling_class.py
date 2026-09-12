#!/usr/bin/env python3
"""ISQGR Delta4 boundary-spin scaling-class audit.

Previous audits established that the finite-cutoff convergence exponents are
numerically identifiable, are not caused by the precision floor, and do not
collapse to one common alpha under a minimal 1/D local-exponent extrapolation.
The pattern is structured: j=1 trajectories are much more mutually consistent
across gamma than j=0.5 trajectories.

This audit therefore tests model hierarchy rather than another extrapolation:

  G: one shared power exponent alpha for all six (gamma,j) datasets;
  J: one exponent alpha_j for each boundary-spin j, with gamma-specific
     amplitudes/intercepts;
  S: one exponent for every (gamma,j) sector.

For each deterministic tail-fraction / chronological-holdout regime, models are
fit only on the training part of every retained trajectory and evaluated on the
future holdout in log-error space. Dataset-specific intercepts are always free,
so the comparison concerns exponent sharing rather than amplitude sharing.

24 preregistered regimes = 6 tail fractions x 4 holdout fractions.

Aggregate evidence for a boundary-spin scaling class requires:
  * all 24 regimes identifiable;
  * J improves held-out RMSE over G by >=10% in the median;
  * J beats G in >=18/24 regimes;
  * allowing fully sector-specific exponents improves on J by <5% in median;
  * each inferred alpha_j has relative spread <=35% across regimes;
  * the two median alpha_j values differ by >=20% relative to their midpoint.

Scope lock: positive support would establish only an empirical boundary-spin
classification for these pinned finite-cutoff Lorentzian EPRL Delta4 data.  It
would not prove a continuum universality class, RG fixed point, or new physics.
"""
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path

SOURCE_COMMIT = "4fa7e31ffc6553e56da94a443a53a4059a5d2035"
TAIL_FRACTIONS = (0.0, 0.10, 0.20, 0.30, 0.40, 0.50)
HOLDOUT_FRACTIONS = (0.20, 0.25, 0.30, 0.35)


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

def make_points(ds,root,tail,holdout):
    out=[]
    for g,j,dmax,path in ds:
        rows=parse_matrix(path); uu=[unit(r) for r in rows]
        if any(u is None for u in uu): raise ValueError('zero row')
        raw=[]
        for k in range(len(uu)-1):
            e=max(0.0,1.0-cosine(uu[k],uu[k+1]))
            if e>0.0: raw.append((k,math.log(k+1.0),math.log(e)))
        cut=int(math.floor(tail*len(raw)))
        pts=raw[cut:]
        nh=max(2,int(math.ceil(holdout*len(pts))))
        nt=len(pts)-nh
        if nt < 4 or nh < 2:
            return None
        out.append({'gamma':g,'j':j,'dmax':dmax,
                    'key':f'g={g},j={j}',
                    'train':pts[:nt],'holdout':pts[nt:],
                    'source_file':path.relative_to(root).as_posix()})
    return out

def fit_shared_slope(datasets, group_fn):
    # Fixed-effect regression. Center x and y within each dataset, then estimate
    # group slope y=b-alpha*x without allowing amplitude differences to bias alpha.
    groups={}
    for d in datasets:
        gr=group_fn(d)
        xs=[p[1] for p in d['train']]; ys=[p[2] for p in d['train']]
        mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
        q=groups.setdefault(gr,{'num':0.0,'den':0.0})
        q['num'] += sum((x-mx)*(y-my) for x,y in zip(xs,ys))
        q['den'] += sum((x-mx)**2 for x in xs)
    alpha={}
    for gr,q in groups.items():
        if q['den']<=0: return None
        alpha[gr]=-q['num']/q['den']
    intercept={}
    for d in datasets:
        a=alpha[group_fn(d)]
        intercept[d['key']]=sum(y+a*x for _,x,y in d['train'])/len(d['train'])
    return alpha,intercept

def score(datasets, fit, group_fn):
    if fit is None: return None
    alpha,intercept=fit
    sq=[]; per={}
    for d in datasets:
        a=alpha[group_fn(d)]; b=intercept[d['key']]
        errs=[(y-(b-a*x))**2 for _,x,y in d['holdout']]
        sq.extend(errs)
        per[d['key']]=math.sqrt(sum(errs)/len(errs))
    return {'rmse':math.sqrt(sum(sq)/len(sq)),
            'per_dataset_rmse':per,
            'alpha':{str(k):v for k,v in alpha.items()},
            'n_holdout':len(sq)}

def audit(ds,root,tail,holdout):
    data=make_points(ds,root,tail,holdout)
    if data is None:
        return {'tail_fraction':tail,'holdout_fraction':holdout,'identifiable':False}
    fg=fit_shared_slope(data,lambda d:'global')
    fj=fit_shared_slope(data,lambda d:d['j'])
    fs=fit_shared_slope(data,lambda d:d['key'])
    sg=score(data,fg,lambda d:'global'); sj=score(data,fj,lambda d:d['j']); ss=score(data,fs,lambda d:d['key'])
    if not all((sg,sj,ss)):
        return {'tail_fraction':tail,'holdout_fraction':holdout,'identifiable':False}
    improve_j=(sg['rmse']-sj['rmse'])/max(sg['rmse'],1e-15)
    improve_s=(sj['rmse']-ss['rmse'])/max(sj['rmse'],1e-15)
    return {'tail_fraction':tail,'holdout_fraction':holdout,'identifiable':True,
            'global_model':sg,'boundary_j_model':sj,'sector_model':ss,
            'j_vs_global_improvement':improve_j,
            'sector_vs_j_improvement':improve_s,
            'n_train_total':sum(len(d['train']) for d in data),
            'n_holdout_total':sum(len(d['holdout']) for d in data)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-root',required=True)
    ap.add_argument('--lane',type=int,required=True); ap.add_argument('--lanes',type=int,default=24)
    ap.add_argument('--output',required=True); args=ap.parse_args()
    root=Path(args.source_root); ds=select_datasets(root)
    if len(ds)!=6: raise RuntimeError(f'expected 6 datasets, found {len(ds)}')
    tasks=[(t,h) for t in TAIL_FRACTIONS for h in HOLDOUT_FRACTIONS]
    assigned=[x for i,x in enumerate(tasks) if i%args.lanes==args.lane]
    results=[audit(ds,root,t,h) for t,h in assigned]
    out={'test':'LORENTZIAN_EPRL_DELTA4_BOUNDARY_SPIN_SCALING_CLASS',
         'source_repository':'PietropaoloFrisoni/HowToSpinFoamAmplitude',
         'source_commit':SOURCE_COMMIT,'tail_fractions':TAIL_FRACTIONS,
         'holdout_fractions':HOLDOUT_FRACTIONS,'lane':args.lane,'lanes':args.lanes,
         'results':results,
         'claim_lock':'Positive support is only an empirical model-selection result for pinned finite-cutoff Delta4 trajectories; it is not a continuum universality or RG claim.'}
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
