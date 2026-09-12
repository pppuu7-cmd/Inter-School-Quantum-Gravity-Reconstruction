#!/usr/bin/env python3
"""Cross-lag audit: does the SVD transport spectrum improve prediction of the next ribbon observable?

For each RG step, the current ribbon sector distribution is a persistence
baseline for the next ribbon distribution.  A preregistered 50/50 mixture of
that baseline with the combined normalized SVD1+SVD2 spectrum is tested against
sector-label permutations of the SVD contribution.  No coefficient is fitted.
"""
from __future__ import annotations
import argparse, json, random, re, statistics
from pathlib import Path

NUM=re.compile(r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?')
def nums(s): return [float(x) for x in NUM.findall(s)]
def prob(v):
    a=[abs(float(x)) for x in v]; s=sum(a)
    return [x/s for x in a] if s else [0.0]*len(a)
def l1(a,b): return sum(abs(x-y) for x,y in zip(a,b))
def mix(a,b,w=.5): return [(1-w)*x+w*y for x,y in zip(a,b)]
def combine(a,b): return prob([abs(x)+abs(y) for x,y in zip(a,b)])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--log',required=True); ap.add_argument('--g',type=float,required=True)
    ap.add_argument('--iterations',type=int,default=5); ap.add_argument('--reps',type=int,default=4096); ap.add_argument('--output',required=True)
    args=ap.parse_args(); text=Path(args.log).read_text(errors='replace')
    if 'Singular values:' not in text or 'Expectation values of Ribbon operators' not in text: raise SystemExit('required output sections absent')
    svsec=text.split('Singular values:',1)[1].split('Expectation values of Ribbon operators',1)[0]
    exsec=text.split('Expectation values of Ribbon operators',1)[1]
    sv=nums(svsec); ex=nums(exsec); need_sv=18*args.iterations; need_ex=9*(args.iterations+1)
    if len(sv)<need_sv or len(ex)<need_ex: raise SystemExit(f'not enough values sv={len(sv)}/{need_sv} ex={len(ex)}/{need_ex}')
    sv=sv[-need_sv:]; ex=ex[-need_ex:]
    sm=[sv[i:i+9] for i in range(0,len(sv),9)]; first=sm[0::2]; second=sm[1::2]
    exp=[ex[i:i+9] for i in range(0,len(ex),9)]
    rows=[]
    for t in range(args.iterations):
        cur=prob(exp[t]); nxt=prob(exp[t+1]); trans=combine(first[t],second[t])
        base=l1(cur,nxt); pred=l1(mix(cur,trans,.5),nxt); improvement=base-pred
        rng=random.Random(31000+100*t+int(round(args.g*100))); null=[]; idx=list(range(9))
        for _ in range(args.reps):
            p=idx[:]; rng.shuffle(p); tp=[trans[i] for i in p]
            null.append(base-l1(mix(cur,tp,.5),nxt))
        null.sort(); p95=null[int(.95*(len(null)-1))]; p99=null[int(.99*(len(null)-1))]
        empirical=(sum(x>=improvement for x in null)+1)/(len(null)+1)
        rows.append({'step':t+1,'baseline_l1':base,'svd_augmented_l1':pred,'improvement':improvement,
                     'null_mean_improvement':sum(null)/len(null),'null_p95_improvement':p95,'null_p99_improvement':p99,
                     'empirical_p':empirical,'above_p95':improvement>p95,'above_p99':improvement>p99})
    imps=[r['improvement'] for r in rows]; pvals=[r['empirical_p'] for r in rows]
    out={'test':'FUSION_RIBBON_CROSSLAG_INCREMENTAL_PREDICTIVITY','g':args.g,'iterations':args.iterations,'mixture_weight_svd':0.5,'permutations':args.reps,'rows':rows,
         'summary':{'mean_improvement_l1':statistics.mean(imps),'median_improvement_l1':statistics.median(imps),
                    'fraction_steps_positive_improvement':sum(x>0 for x in imps)/len(imps),
                    'fraction_steps_above_permutation_p95':sum(r['above_p95'] for r in rows)/len(rows),
                    'min_empirical_p':min(pvals)},
         'claim_lock':'Nearest-framework dynamical control. Positive incremental predictivity means the SVD transport spectrum improves next-step ribbon-observable prediction beyond persistence and label-permuted SVD controls under a frozen 50/50 mixture; it is not evidence by itself for quantum gravity or new physics.'}
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
