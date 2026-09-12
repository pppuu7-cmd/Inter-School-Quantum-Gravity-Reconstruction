#!/usr/bin/env python3
"""Parse pinned Fusion-basis-coarse-graining logs into preregistered SVD-flow invariants.

This is a nearest-framework q-deformed lattice-gauge/TNR control.  It does not
constitute an EPRL gravity refinement realization.  The goal is to determine
which parts of the ISQGR envelope/selector language are already generic to
ordinary SVD embedding-map coarse graining.
"""
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path


def parse_flat_section(text: str, start: str, end: str | None = None):
    if start not in text:
        return []
    s = text.split(start, 1)[1]
    if end and end in s:
        s = s.split(end, 1)[0]
    vals=[]
    for x in re.findall(r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?', s):
        try: vals.append(float(x))
        except ValueError: pass
    return vals


def entropy(weights):
    s=sum(weights)
    if s <= 0: return 0.0
    p=[x/s for x in weights if x>0]
    return -sum(x*math.log(x) for x in p)


def matrix_metrics(v):
    m=max(abs(x) for x in v) if v else 0.0
    n=[abs(x)/m if m else 0.0 for x in v]
    tot=sum(abs(x) for x in v)
    off=sum(abs(v[i]) for i in (1,2,3,5,6,7)) if len(v)==9 else 0.0
    return {
      'max':m,
      'effective_rank_1e2':sum(x>=1e-2 for x in n),
      'effective_rank_1e3':sum(x>=1e-3 for x in n),
      'normalized_entropy':entropy([abs(x) for x in v])/math.log(len(v)) if len(v)>1 else 0.0,
      'offdiag_mass_fraction':off/tot if tot else 0.0,
      'normalized_entries':n,
    }


def l2(a,b):
    return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--log',required=True)
    ap.add_argument('--g',type=float,required=True)
    ap.add_argument('--iterations',type=int,required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    text=Path(args.log).read_text(errors='replace')
    vals=parse_flat_section(text, 'Singular values:', 'Expectation values of Ribbon operators')
    expected=18*args.iterations
    if len(vals) < expected:
        raise SystemExit(f'expected at least {expected} final singular-value numbers, got {len(vals)}')
    # Use the last expected entries in case timestamps/headers contributed numeric text.
    vals=vals[-expected:]
    mats=[vals[i:i+9] for i in range(0,len(vals),9)]
    first=mats[0::2]; second=mats[1::2]
    fm=[matrix_metrics(x) for x in first]; sm=[matrix_metrics(x) for x in second]
    first_flow=[l2(fm[i-1]['normalized_entries'],fm[i]['normalized_entries']) for i in range(1,len(fm))]
    second_flow=[l2(sm[i-1]['normalized_entries'],sm[i]['normalized_entries']) for i in range(1,len(sm))]
    out={
      'test':'FUSION_BASIS_SVD_FLOW_INVARIANTS', 'g':args.g, 'iterations':args.iterations,
      'first_svd':fm, 'second_svd':sm,
      'first_svd_normalized_flow_l2':first_flow,
      'second_svd_normalized_flow_l2':second_flow,
      'first_svd_flow_contracts_last_vs_first': bool(first_flow and first_flow[-1] < first_flow[0]),
      'second_svd_flow_contracts_last_vs_first': bool(second_flow and second_flow[-1] < second_flow[0]),
      'persistent_multisector_envelope_1e2': all(x['effective_rank_1e2']>1 for x in fm+sm),
      'claim_lock':'Nearest-framework q-deformed lattice-gauge/TNR control only. Persistent SVD envelopes or contracting spectra show generic embedding-map structure and cannot by themselves establish an ISQGR quantum-gravity bridge or source-native selector.'
    }
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
