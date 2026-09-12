#!/usr/bin/env python3
"""Diagnostic-only crossover test for the gamma=0.1 Lorentzian EPRL Delta4 sector.

This test is intentionally downstream of a FAILED preregistered all-gamma
boundary-spin transfer gate.  It cannot rescue or replace that gate.  It asks
whether gamma=0.1 is better described as a separate finite-cutoff convergence
regime with a training-identifiable slope crossover.

For each of the six pinned (gamma,j) datasets and each chronological holdout
fraction, construct normalized boundary-profile step error
  e_D = 1 - cos(u_D,u_{D+1}).
After a fixed 10% early-tail removal, fit on the training prefix:
  A) one log-log slope;
  B) a continuous two-slope hinge model with the change point chosen ONLY from
     a fixed training-internal candidate set {0.30,0.40,0.50,0.60} of the
     training range, requiring >=4 points on either side.
No holdout point participates in choosing the hinge.  Predict the untouched
chronological suffix.

Per-dataset crossover support (aggregated over holdout fractions) requires:
  * median piecewise-vs-single RMSE improvement >= 0.25;
  * piecewise beats single in >= 3/4 holdout windows;
  * median relative early/late slope separation >= 0.30;
  * chosen hinge Dl range across windows <= 4.

Diagnostic aggregate pattern support requires BOTH gamma=0.1 datasets to pass
and at least 3/4 gamma in {1.0,1.2} controls to NOT pass.

Claim lock: even a positive diagnostic only establishes a finite-cutoff regime
boundary in this pinned Delta4 dataset. It is not a continuum exponent,
refinement law, bridge derivation, or new physics.
"""
from __future__ import annotations
import argparse, json, math, re, statistics
from pathlib import Path

SOURCE_COMMIT='4fa7e31ffc6553e56da94a443a53a4059a5d2035'
HOLDOUTS=(0.20,0.25,0.30,0.35)
TAIL=0.10
HINGE_FRACS=(0.30,0.40,0.50,0.60)


def l2(v): return math.sqrt(sum(x*x for x in v))
def unit(v):
    n=l2(v); return None if n==0 else [x/n for x in v]
def cos(a,b): return max(-1.0,min(1.0,sum(x*y for x,y in zip(a,b))))

def parse_matrix(path):
    rows=[]
    for line in path.read_text().splitlines():
        if line.strip(): rows.append([float(x) for x in re.split(r'[\s,]+',line.strip()) if x])
    if not rows or any(len(r)!=len(rows[0]) for r in rows): raise ValueError(path)
    return rows

def select(root):
    pat=re.compile(r'Immirzi_([^/]+)/j_([^/]+)/CSV_format/Delta_4_ampls_Dl_max_(\d+)\.csv$')
    best={}
    for p in root.glob('Delta_4_ampls/Immirzi_*/j_*/CSV_format/Delta_4_ampls_Dl_max_*.csv'):
        m=pat.search(p.as_posix())
        if not m: continue
        g,j,d=float(m.group(1)),float(m.group(2)),int(m.group(3))
        if (g,j) not in best or d>best[(g,j)][0]: best[(g,j)]=(d,p)
    return [(g,j,d,p) for (g,j),(d,p) in sorted(best.items())]

def points(path):
    uu=[unit(r) for r in parse_matrix(path)]
    if any(x is None for x in uu): return []
    out=[]
    for k in range(len(uu)-1):
        e=max(0.0,1.0-cos(uu[k],uu[k+1]))
        if e>0: out.append((k+1.0,math.log(k+1.0),math.log(e)))
    cut=int(math.floor(TAIL*len(out)))
    return out[cut:]

def linear_fit(xs,ys):
    mx,my=sum(xs)/len(xs),sum(ys)/len(ys)
    den=sum((x-mx)**2 for x in xs)
    if den<=0: return None
    b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/den
    a=my-b*mx
    return a,b

def single_model(train):
    fit=linear_fit([p[1] for p in train],[p[2] for p in train])
    return None if fit is None else fit

def piecewise_fit(train):
    # Continuous hinge: y = a + b*x + c*max(0,x-xh).
    # Solve normal equations explicitly via Gaussian elimination; choose hinge by train SSE only.
    best=None
    n=len(train)
    for hf in HINGE_FRACS:
        idx=int(round(hf*(n-1)))
        if idx<4 or n-idx-1<4: continue
        xh=train[idx][1]; dl=train[idx][0]
        X=[]; y=[]
        for _,x,z in train:
            X.append([1.0,x,max(0.0,x-xh)]); y.append(z)
        A=[[sum(r[i]*r[j] for r in X) for j in range(3)] for i in range(3)]
        bvec=[sum(r[i]*z for r,z in zip(X,y)) for i in range(3)]
        M=[A[i]+[bvec[i]] for i in range(3)]
        ok=True
        for c in range(3):
            piv=max(range(c,3),key=lambda r:abs(M[r][c]))
            if abs(M[piv][c])<1e-12: ok=False; break
            M[c],M[piv]=M[piv],M[c]
            q=M[c][c]; M[c]=[v/q for v in M[c]]
            for r in range(3):
                if r==c: continue
                q=M[r][c]; M[r]=[M[r][k]-q*M[c][k] for k in range(4)]
        if not ok: continue
        a,s1,c=M[0][3],M[1][3],M[2][3]
        pred=[a+s1*x+c*max(0,x-xh) for _,x,_ in train]
        sse=sum((z-p)**2 for (_,_,z),p in zip(train,pred))
        cand=(sse,a,s1,c,xh,dl)
        if best is None or cand[0]<best[0]: best=cand
    return best

def rmse(vals): return math.sqrt(sum(x*x for x in vals)/len(vals))
def eval_dataset(g,j,d,path):
    ps=points(path); wins=[]
    for h in HOLDOUTS:
        nh=max(2,int(math.ceil(h*len(ps)))); nt=len(ps)-nh
        train,hold=ps[:nt],ps[nt:]
        if nt<10: wins.append({'holdout_fraction':h,'identifiable':False}); continue
        sm=single_model(train); pm=piecewise_fit(train)
        if sm is None or pm is None: wins.append({'holdout_fraction':h,'identifiable':False}); continue
        a,b=sm; _,pa,s1,c,xh,dl=pm; s2=s1+c
        es=[z-(a+b*x) for _,x,z in hold]
        ep=[z-(pa+s1*x+c*max(0,x-xh)) for _,x,z in hold]
        rs,rp=rmse(es),rmse(ep)
        sep=abs(s2-s1)/max(abs(s1),abs(s2),1e-12)
        wins.append({'holdout_fraction':h,'identifiable':True,'single_rmse':rs,'piecewise_rmse':rp,
                     'piecewise_improvement':(rs-rp)/max(rs,1e-15),'hinge_Dl':dl,
                     'early_slope':s1,'late_slope':s2,'relative_slope_separation':sep})
    good=[w for w in wins if w['identifiable']]
    if len(good)!=4:
        support=False; agg={}
    else:
        imps=[w['piecewise_improvement'] for w in good]
        seps=[w['relative_slope_separation'] for w in good]
        hinges=[w['hinge_Dl'] for w in good]
        agg={'median_piecewise_improvement':statistics.median(imps),
             'piecewise_beats_single_count':sum(x>0 for x in imps),
             'median_relative_slope_separation':statistics.median(seps),
             'hinge_Dl_range':max(hinges)-min(hinges)}
        support=(agg['median_piecewise_improvement']>=0.25 and agg['piecewise_beats_single_count']>=3 and
                 agg['median_relative_slope_separation']>=0.30 and agg['hinge_Dl_range']<=4.0)
    return {'gamma':g,'j':j,'dmax':d,'source_file':path.as_posix(),'windows':wins,
            'aggregate':agg,'dataset_crossover_support':support}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-root',required=True); ap.add_argument('--output',required=True); args=ap.parse_args()
    root=Path(args.source_root); ds=select(root)
    if len(ds)!=6: raise RuntimeError(f'expected 6 datasets got {len(ds)}')
    rows=[eval_dataset(*x) for x in ds]
    target=[r for r in rows if r['gamma']==0.1]; ctrl=[r for r in rows if r['gamma'] in (1.0,1.2)]
    pattern=(len(target)==2 and all(r['dataset_crossover_support'] for r in target) and
             len(ctrl)==4 and sum(not r['dataset_crossover_support'] for r in ctrl)>=3)
    out={'test':'LORENTZIAN_EPRL_DELTA4_GAMMA01_CROSSOVER_DIAGNOSTIC','source_commit':SOURCE_COMMIT,
         'tail_fraction':TAIL,'holdout_fractions':HOLDOUTS,'hinge_training_fractions':HINGE_FRACS,
         'datasets':rows,'gamma01_separate_crossover_pattern_support':pattern,
         'frozen_dataset_gate':{'median_piecewise_vs_single_improvement_min':0.25,
             'piecewise_beats_single_min_windows':3,'median_relative_slope_separation_min':0.30,
             'hinge_Dl_range_max':4.0},
         'frozen_aggregate_gate':'both gamma=0.1 datasets pass and at least 3/4 gamma=1.0/1.2 controls do not pass',
         'claim_lock':'Diagnostic boundary classification only; cannot rescue failed all-gamma scaling gate and is not continuum/refinement/bridge/new physics evidence.'}
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
