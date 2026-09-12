#!/usr/bin/env python3
"""Test whether source-native ribbon-observable sector support predicts later SVD support.

Nearest-framework control only.  The q-deformed lattice-gauge/TNR code prints
both singular values indexed by (i,j) sectors and ribbon-operator expectation
values in the same (k+1)x(k+1) sector ordering.  We freeze the same relative
1e-2 support threshold used by the previous SVD-envelope audit, and ask whether
pre-coarse-graining ribbon support predicts the two SVD supports generated in
the subsequent RG step better than rank-matched random sector labels.
"""
from __future__ import annotations
import argparse, json, math, random, re
from pathlib import Path

NUM = re.compile(r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?')

def nums(section):
    return [float(x) for x in NUM.findall(section)]

def support(v, rel=1e-2):
    if not v: return set()
    m=max(abs(x) for x in v)
    if m==0: return set()
    return {i for i,x in enumerate(v) if abs(x)/m >= rel}

def pr(v):
    a=[abs(x) for x in v]
    s=sum(a); s2=sum(x*x for x in a)
    return (s*s/s2) if s2 else 0.0

def metrics(a,b,n=9):
    inter=len(a&b); union=len(a|b)
    return {
      'jaccard': inter/union if union else 1.0,
      'precision': inter/len(a) if a else (1.0 if not b else 0.0),
      'recall': inter/len(b) if b else 1.0,
      'overlap': inter,
      'selector_rank': len(a), 'target_rank': len(b),
    }

def random_baseline(a,b,n=9,reps=512,seed=0):
    rng=random.Random(seed)
    vals=[]
    k=len(a)
    for _ in range(reps):
        aa=set(rng.sample(range(n),k)) if k else set()
        vals.append(metrics(aa,b,n)['jaccard'])
    vals.sort()
    return {'mean_jaccard':sum(vals)/len(vals),'p95_jaccard':vals[int(.95*(len(vals)-1))]}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--log',required=True); ap.add_argument('--g',type=float,required=True)
    ap.add_argument('--iterations',type=int,default=5); ap.add_argument('--output',required=True)
    args=ap.parse_args(); text=Path(args.log).read_text(errors='replace')
    if 'Singular values:' not in text or 'Expectation values of Ribbon operators' not in text:
        raise SystemExit('required output sections absent')
    svsec=text.split('Singular values:',1)[1].split('Expectation values of Ribbon operators',1)[0]
    exsec=text.split('Expectation values of Ribbon operators',1)[1]
    sv=nums(svsec); ex=nums(exsec)
    need_sv=18*args.iterations; need_ex=9*(args.iterations+1)
    if len(sv)<need_sv or len(ex)<need_ex:
        raise SystemExit(f'not enough values sv={len(sv)}/{need_sv} ex={len(ex)}/{need_ex}')
    sv=sv[-need_sv:]; ex=ex[-need_ex:]
    sm=[sv[i:i+9] for i in range(0,len(sv),9)]
    first=sm[0::2]; second=sm[1::2]
    exp=[ex[i:i+9] for i in range(0,len(ex),9)]
    rows=[]
    for t in range(args.iterations):
        src=support(exp[t]); s1=support(first[t]); s2=support(second[t])
        m1=metrics(src,s1); m2=metrics(src,s2)
        r1=random_baseline(src,s1,seed=10000+100*t+int(round(args.g*100)))
        r2=random_baseline(src,s2,seed=20000+100*t+int(round(args.g*100)))
        rows.append({'step':t+1,'ribbon_support':sorted(src),'svd1_support':sorted(s1),'svd2_support':sorted(s2),
                     'ribbon_participation_ratio':pr(exp[t]),'svd1':m1,'svd2':m2,
                     'random1':r1,'random2':r2,
                     'svd1_jaccard_gain_over_random_mean':m1['jaccard']/(r1['mean_jaccard']+1e-15),
                     'svd2_jaccard_gain_over_random_mean':m2['jaccard']/(r2['mean_jaccard']+1e-15)})
    avg=lambda key1,key2=None: sum((r[key1] if key2 is None else r[key1][key2]) for r in rows)/len(rows)
    out={'test':'FUSION_RIBBON_SOURCE_SELECTOR_PREDICTIVITY','g':args.g,'iterations':args.iterations,
         'threshold_relative':1e-2,'rows':rows,
         'summary':{'mean_svd1_jaccard':avg('svd1','jaccard'),'mean_svd2_jaccard':avg('svd2','jaccard'),
                    'mean_svd1_gain_over_random':avg('svd1_jaccard_gain_over_random_mean'),
                    'mean_svd2_gain_over_random':avg('svd2_jaccard_gain_over_random_mean'),
                    'fraction_steps_both_gain_gt_1':sum(r['svd1_jaccard_gain_over_random_mean']>1 and r['svd2_jaccard_gain_over_random_mean']>1 for r in rows)/len(rows)},
         'claim_lock':'Nearest-framework q-deformed lattice-gauge/TNR test. Positive predictivity would show that a source-native observable-labelled sector selector contains information beyond rank-matched random support. It would not establish a gravity selector, continuum QG, or new physics.'}
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
