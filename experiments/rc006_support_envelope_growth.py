#!/usr/bin/env python3
"""Multi-step support-envelope growth in the RC-006 EPRL/FK analogue.

State = (l, jplus, jminus), with l contained in the diagonal SU(2)_k coupling
of (jplus,jminus).  Start from the exact source simplicity states
(l, Y_gamma(l)).  A raw coarse-support step takes all pairwise recouplings of
the current support in l, plus and minus sectors, keeping only diagonal-
compatible triples.

At each step we record:
  * raw envelope size;
  * fraction exactly satisfying the original EPRL simplicity map;
  * whether every source target state remains represented;
  * size after applying the source-native local simplicity selector.

The selector is not fitted: it is exactly the frozen source Y_gamma relation.
This is a support-combinatorics audit, not a q-deformed amplitude/TNR flow.
"""
from __future__ import annotations

import argparse,json
from fractions import Fraction
from pathlib import Path

from rc006_eprl_fusion_support_closure import fusion,eprl_map

State=tuple[int,int,int]


def raw_step(k:int,states:set[State])->set[State]:
    out=set()
    ss=sorted(states)
    for l1,p1,m1 in ss:
        for l2,p2,m2 in ss:
            for l in fusion(k,l1,l2):
                for p in fusion(k,p1,p2):
                    for m in fusion(k,m1,m2):
                        if l in fusion(k,p,m):
                            out.add((l,p,m))
    return out


def analyze(k:int,gamma:Fraction,nsteps:int)->dict:
    jmax=k//2
    source={
        (l,*eprl_map(l,gamma,k))
        for l in range(jmax+1)
        if eprl_map(l,gamma,k) is not None
    }
    current=set(source)
    rows=[]
    for step in range(nsteps+1):
        simple={s for s in current if eprl_map(s[0],gamma,k)==(s[1],s[2])}
        targets={s for s in source if s[0] in {x[0] for x in current}}
        captured=targets.issubset(current)
        selected={s for s in current if s in simple}
        rows.append({
            'step':step,
            'raw_envelope_size':len(current),
            'simple_state_count':len(simple),
            'raw_simple_fraction':len(simple)/len(current) if current else 0.0,
            'raw_extra_state_count':len(current)-len(simple),
            'all_relevant_source_targets_captured':bool(captured),
            'post_local_selector_size':len(selected),
            'post_local_selector_equals_source_support':bool(selected==source),
            'raw_support': [list(x) for x in sorted(current)],
        })
        if step<nsteps:
            current=raw_step(k,current)
    return {
        'test':'RC006_EPRL_MULTI_STEP_SUPPORT_ENVELOPE_GROWTH',
        'status':'PASS_EXECUTION','k':k,'gamma':f'{gamma.numerator}/{gamma.denominator}',
        'source_support':[list(x) for x in sorted(source)],'nsteps':nsteps,'steps':rows,
        'raw_envelope_monotone_nondecreasing':all(rows[i+1]['raw_envelope_size']>=rows[i]['raw_envelope_size'] for i in range(len(rows)-1)),
        'source_targets_captured_all_steps':all(r['all_relevant_source_targets_captured'] for r in rows),
        'selector_restores_exact_source_all_steps':all(r['post_local_selector_equals_source_support'] for r in rows),
        'claim_lock':'Exact finite SU(2)_k support combinatorics only; no tensor weights, q-6j amplitudes, SVD/TNR spectra, or continuum inference.'
    }


def main():
    p=argparse.ArgumentParser();p.add_argument('--k',type=int,required=True);p.add_argument('--gamma-num',type=int,required=True);p.add_argument('--gamma-den',type=int,required=True);p.add_argument('--steps',type=int,default=3);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    out=analyze(a.k,Fraction(a.gamma_num,a.gamma_den),a.steps)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'k':out['k'],'gamma':out['gamma'],'sizes':[r['raw_envelope_size'] for r in out['steps']],'simple_fractions':[r['raw_simple_fraction'] for r in out['steps']],'selector_exact_all_steps':out['selector_restores_exact_source_all_steps']},indent=2))
if __name__=='__main__': main()
