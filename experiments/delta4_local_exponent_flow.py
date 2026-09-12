#!/usr/bin/env python3
"""ISQGR Delta4 local-effective-exponent flow audit.

The precision-floor audit established that the sector-dependent power exponents
are numerically identifiable and are not created by floating-point censoring.
This audit asks the next question: is the sector dependence merely pre-asymptotic?

For each pinned (gamma,j) Delta4 dataset and trailing/sliding window W in
{4,5,6,7}, define local effective exponents from

    log e_D = c - alpha_eff log(D+1)

inside every W-point window, where e_D = 1-cos(u_D,u_{D+1}).  We then fit the
local-exponent flow to the minimal one-correction ansatz

    alpha_eff(D_mid) = alpha_inf + c/(D_mid+1).

The extrapolated alpha_inf is not assumed to be physical.  It is used only as a
falsifiable diagnostic: if sector spread contracts strongly and the inferred
alpha_inf is stable under W, a common asymptotic exponent remains plausible;
otherwise the currently available trajectories do not support that claim.

Preregistered aggregate gates:
  * each task must have >= 3 local windows;
  * within-dataset relative spread of alpha_inf across W <= 0.35;
  * for each boundary-j sector, cross-gamma alpha_inf spread <= 0.35;
  * asymptotic extrapolation must reduce cross-gamma spread by >=25% relative
    to the terminal local exponent in every j sector for 'collapse support'.

Scope lock: this is an empirical finite-cutoff diagnostic on pinned public
Lorentzian EPRL Delta4 amplitudes, not a continuum-limit or RG proof.
"""
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path

SOURCE_COMMIT = "4fa7e31ffc6553e56da94a443a53a4059a5d2035"
WINDOWS = (4,5,6,7)


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

def audit(dataset,W,root):
    g,j,dmax,path=dataset
    rows=parse_matrix(path); uu=[unit(r) for r in rows]
    if any(u is None for u in uu): raise ValueError('zero row')
    es=[max(0.0,1.0-cosine(uu[k],uu[k+1])) for k in range(len(uu)-1)]
    pts=[(k,e) for k,e in enumerate(es) if e>0.0]
    local=[]
    for s in range(0,len(pts)-W+1):
        seg=pts[s:s+W]
        xs=[math.log(k+1.0) for k,e in seg]
        ys=[math.log(e) for k,e in seg]
        _,b=linfit(xs,ys)
        dmid=sum(k for k,e in seg)/W
        local.append({'start':seg[0][0],'end':seg[-1][0],'D_mid':dmid,'alpha_eff':-b})
    identifiable=len(local)>=3
    if not identifiable:
        return {'gamma':g,'j_boundary':j,'Dl_max':dmax,'window':W,
                'n_transitions':len(es),'n_local_windows':len(local),
                'identifiable':False,'source_file':path.relative_to(root).as_posix()}
    # Minimal 1/D correction extrapolation of local exponents.
    xs=[1.0/(r['D_mid']+1.0) for r in local]
    ys=[r['alpha_eff'] for r in local]
    a,b=linfit(xs,ys)  # alpha_eff = a + b/(D+1)
    first=local[0]['alpha_eff']; last=local[-1]['alpha_eff']
    return {'gamma':g,'j_boundary':j,'Dl_max':dmax,'window':W,
            'n_transitions':len(es),'n_local_windows':len(local),
            'identifiable':True,'alpha_first':first,'alpha_terminal':last,
            'alpha_inf_extrapolated':a,'correction_coefficient':b,
            'flow_delta_terminal_minus_first':last-first,
            'local_exponents':local,
            'source_file':path.relative_to(root).as_posix()}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-root',required=True)
    ap.add_argument('--lane',type=int,required=True); ap.add_argument('--lanes',type=int,default=24)
    ap.add_argument('--output',required=True); args=ap.parse_args()
    root=Path(args.source_root); ds=select_datasets(root)
    if len(ds)!=6: raise RuntimeError(f'expected 6 datasets, found {len(ds)}')
    tasks=[(d,w) for w in WINDOWS for d in ds]
    assigned=[task for i,task in enumerate(tasks) if i%args.lanes==args.lane]
    results=[audit(d,w,root) for d,w in assigned]
    out={'test':'LORENTZIAN_EPRL_DELTA4_LOCAL_EXPONENT_FLOW',
         'source_repository':'PietropaoloFrisoni/HowToSpinFoamAmplitude',
         'source_commit':SOURCE_COMMIT,'windows':WINDOWS,
         'lane':args.lane,'lanes':args.lanes,'results':results,
         'claim_lock':'This finite-cutoff local-exponent audit can test whether sector spread appears pre-asymptotic. It does not establish RG flow, a continuum limit, universality, or new physics.'}
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
