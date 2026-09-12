#!/usr/bin/env python3
"""Localize RC006 contraction-serialization instability without changing its failed gate.

This diagnostic reuses the frozen source fingerprint construction, compares each
single-anchor deletion against the full-source canonical order, and records which
pairwise symbol relations flip or become ambiguous. It cannot authorize Eq.(29);
it only identifies where additional source authority would have to enter.
"""
from pathlib import Path
import argparse,json,sys
sys.path.insert(0,str(Path(__file__).parent))
import rc006_contraction_serialization_stability as base

def build(source_dir, role):
    fs=list(Path(source_dir).rglob('*.tex'))
    if len(fs)!=1: raise SystemExit('monolithic source prerequisite violated')
    t=fs[0].read_text(errors='ignore'); S={n:base.seq(base.block(t,n)) for n in base.ALL}
    universe=sorted(set(x for q in S.values() for x in q))
    active=list(base.ALL) if role=='full' else [n for n in base.ALL if n!=role]
    fps={}
    for x in universe:
        parts=[]
        for n in active:
            q=S[n]; occ=[]
            for i,v in enumerate(q):
                if v==x:
                    prev=q[i-1] if i else '<BOS>'; nxt=q[i+1] if i+1<len(q) else '<EOS>'; pos=min(3,int(4*i/max(1,len(q))))
                    occ.append((prev,nxt,pos))
            parts.append((n,tuple(sorted(occ))))
        fps[x]=(x[0],tuple(parts))
    groups={}
    for x,p in fps.items(): groups.setdefault(repr(p),[]).append(x)
    amb=[sorted(v) for v in groups.values() if len(v)>1]
    order=sorted(universe,key=lambda x:(fps[x],x)); rank={x:i for i,x in enumerate(order)}
    return S,universe,amb,order,rank

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--drop',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    if a.drop not in base.ALL: raise SystemExit('drop must be qualified anchor')
    S,U,amb0,o0,r0=build(a.source_dir,'full'); _,_,amb,o,r=build(a.source_dir,a.drop)
    flips=[]
    for i,x in enumerate(U):
      for y in U[i+1:]:
        s0=r0[x]<r0[y]; s=r[x]<r[y]
        if s0!=s: flips.append([x,y])
    affected=sorted(set(z for p in flips for z in p))
    dropped_seq=S[a.drop]
    out={'test':'RC006_SERIALIZATION_FAILURE_LOCALIZATION','drop_anchor':a.drop,'valid':len(U)>=30,
         'full_ambiguous_group_count':len(amb0),'holdout_ambiguous_group_count':len(amb),
         'holdout_ambiguous_groups':amb,'pairwise_flip_count':len(flips),'pairwise_total':len(U)*(len(U)-1)//2,
         'pairwise_agreement':1-len(flips)/(len(U)*(len(U)-1)//2),'affected_symbol_count':len(affected),'affected_symbols':affected,
         'dropped_anchor_sequence_length':len(dropped_seq),'dropped_anchor_symbols':dropped_seq,
         'diagnostic_classification':'CRITICAL_SOURCE_ANCHOR' if (amb or flips) else 'NONCRITICAL_SOURCE_ANCHOR',
         'interpretation_lock':'Diagnostic only. The failed serialization gate remains failed; this output cannot authorize Eq29 or relax thresholds.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
