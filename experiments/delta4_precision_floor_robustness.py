#!/usr/bin/env python3
"""ISQGR Delta4 precision-floor robustness audit.

The preceding shifted-power campaign improved held-out prediction in 16/24
(split,dataset) tasks but produced unstable exponents, especially in j=0.5.
Before interpreting that instability physically, test whether it is generated
by machine-precision saturation of the shellflow angular error

    e_D = 1 - cos(u_D,u_{D+1}).

For each pinned (gamma,j) dataset and each preregistered censor threshold tau,
only transitions with e_D > tau are used. A 70/30 chronological train/holdout
split then compares a plain power law with a simple exponential. The power
exponent is meaningful only if it is stable as tau is varied.

Scope lock: this is a numerical-identifiability diagnostic for pinned Delta4
booster-cutoff data. It is not a refinement operator or continuum-limit test.
"""
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path

SOURCE_COMMIT = "4fa7e31ffc6553e56da94a443a53a4059a5d2035"
THRESHOLDS = (1e-12, 1e-13, 1e-14, 1e-15)
TRAIN_FRACTION = 0.70

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

def mae(pred,obs): return sum(abs(a-b) for a,b in zip(pred,obs))/len(obs)

def audit(dataset,tau,root):
    g,j,dmax,path=dataset
    rows=parse_matrix(path); uu=[unit(r) for r in rows]
    if any(u is None for u in uu): raise ValueError('zero row')
    raw=[max(0.0,1.0-cosine(uu[k],uu[k+1])) for k in range(len(uu)-1)]
    kept=[(k,e) for k,e in enumerate(raw) if e > tau]
    # We preregister a minimum sample size; insufficient sectors are reported,
    # not silently rescued by changing tau or split rules.
    if len(kept) < 8:
        return {'gamma':g,'j_boundary':j,'Dl_max':dmax,'tau':tau,
                'n_transitions':len(raw),'n_kept':len(kept),
                'floor_fraction':1.0-len(kept)/max(len(raw),1),
                'identifiable':False,'source_file':path.relative_to(root).as_posix()}
    ntr=max(5,min(len(kept)-3,int(math.floor(TRAIN_FRACTION*len(kept)))))
    train=kept[:ntr]; test=kept[ntr:]
    xtr=[k for k,e in train]; ytr=[math.log(e) for k,e in train]
    xte=[k for k,e in test]; yte=[math.log(e) for k,e in test]
    ap,bp=linfit([math.log(k+1.0) for k in xtr],ytr)
    ae,be=linfit(xtr,ytr)
    predp=[ap+bp*math.log(k+1.0) for k in xte]
    prede=[ae+be*k for k in xte]
    mp=mae(predp,yte); me=mae(prede,yte)
    return {
      'gamma':g,'j_boundary':j,'Dl_max':dmax,'tau':tau,
      'n_transitions':len(raw),'n_kept':len(kept),
      'floor_fraction':1.0-len(kept)/len(raw),'identifiable':True,
      'power_alpha':-bp,'exponential_decay':-be,
      'heldout_log_mae_power':mp,'heldout_log_mae_exponential':me,
      'power_preferred':bool(mp < me),
      'power_advantage':(me-mp)/max(me,1e-15),
      'source_file':path.relative_to(root).as_posix()
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-root',required=True)
    ap.add_argument('--lane',type=int,required=True); ap.add_argument('--lanes',type=int,default=24)
    ap.add_argument('--output',required=True); args=ap.parse_args()
    root=Path(args.source_root); ds=select_datasets(root)
    if len(ds)!=6: raise RuntimeError(f'expected 6 datasets, found {len(ds)}')
    tasks=[(d,t) for t in THRESHOLDS for d in ds]
    assigned=[task for i,task in enumerate(tasks) if i%args.lanes==args.lane]
    results=[audit(d,t,root) for d,t in assigned]
    out={'test':'LORENTZIAN_EPRL_DELTA4_PRECISION_FLOOR_ROBUSTNESS',
         'source_repository':'PietropaoloFrisoni/HowToSpinFoamAmplitude',
         'source_commit':SOURCE_COMMIT,'thresholds':THRESHOLDS,
         'train_fraction':TRAIN_FRACTION,'lane':args.lane,'lanes':args.lanes,
         'results':results,
         'claim_lock':'This audit can diagnose numerical-floor contamination of empirical cutoff exponents only. It does not establish physical RG flow, continuum dynamics, or new physics.'}
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
