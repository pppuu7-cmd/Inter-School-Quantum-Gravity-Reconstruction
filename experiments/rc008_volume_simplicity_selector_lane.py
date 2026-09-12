#!/usr/bin/env python3
"""Distributed lane wrapper for the preregistered RC008 asymptotic amplitude selector audit.

No alpha is fitted: the five alpha values were frozen in the existing audit before
this distributed execution. Each lane independently samples equal-scale departures
from exact volume simplicity and applies the same preregistered criterion.
"""
from pathlib import Path
import argparse,json,math,random,statistics,sys
sys.path.insert(0,str(Path(__file__).parent))
import rc008_volume_simplicity_dynamic_selector_audit as core

N_BASE=256
PERT=4
EPS=(0.15,0.30,0.45,0.60)
PERM=200

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--alpha',type=float,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    if a.alpha not in core.ALPHAS: raise SystemExit('alpha not in prospectively frozen set')
    seed=core.SEED+int(round(a.alpha*10000)); rng=random.Random(seed)
    # exact homogeneity positive control for the same source asymptotic amplitude
    target=12.0*a.alpha-9.0; herr=[]
    for _ in range(64):
        j=core.geometric_spins(rng); lam=math.exp(rng.uniform(-1,1));
        A=core.log_dressed_amplitude(j,a.alpha); B=core.log_dressed_amplitude([lam*x for x in j],a.alpha)
        obs=(B-A)/math.log(lam); herr.append(abs(obs-target))
    hom=max(herr)<=2e-9
    residual=[]; delta=[]; byeps={e:[] for e in EPS}; invalid=0; base_res=[]
    for _ in range(N_BASE):
        b=core.geometric_spins(rng); base_res.append(core.volume_simplicity_residual(b)); lb=core.log_dressed_amplitude(b,a.alpha)
        for e in EPS:
            for _ in range(PERT):
                p=core.perturb_equal_scale(b,e,rng); lp=core.log_dressed_amplitude(p,a.alpha)
                if not(math.isfinite(lp) and math.isfinite(lb)): invalid+=1; continue
                r=core.volume_simplicity_residual(p); d=lp-lb; residual.append(r); delta.append(d); byeps[e].append(d)
    rho=core.spearman(residual,delta); frac=sum(x<0 for x in delta)/len(delta); med=statistics.median(delta)
    null=[]; pr=random.Random(seed+991)
    for _ in range(PERM):
        rr=residual[:]; pr.shuffle(rr); null.append(core.spearman(rr,delta))
    p=(1+sum(x<=rho for x in null))/(1+len(null))
    lane=bool(hom and invalid==0 and frac>=0.75 and rho<=-0.20 and p<=0.05)
    out={'test':'RC008_VOLUME_SIMPLICITY_SELECTOR_DISTRIBUTED_LANE','alpha':a.alpha,'seed':seed,'valid':invalid==0 and len(delta)>0,
         'homogeneity_target_degree':target,'homogeneity_max_abs_error':max(herr),'homogeneity_pass':hom,
         'base_volume_simplicity_residual_max':max(base_res),'fraction_perturbed_lower_amplitude':frac,
         'spearman_residual_vs_logamp_delta':rho,'permutation_lower_tail_p':p,'median_log_amplitude_delta':med,
         'by_epsilon':{str(e):{'n':len(ds),'fraction_lower':sum(x<0 for x in ds)/len(ds),'median_delta':statistics.median(ds)} for e,ds in byeps.items()},
         'lane_pass':lane,
         'frozen_lane_rule':'homogeneity error <=2e-9; zero invalid evaluations; fraction lower >=0.75; Spearman <=-0.20; permutation lower-tail p <=0.05',
         'interpretation_lock':'Amplitude-level asymptotic local selector diagnostic only; not a full coarse/refined RC008 reproduction, refinement map, or bridge.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
