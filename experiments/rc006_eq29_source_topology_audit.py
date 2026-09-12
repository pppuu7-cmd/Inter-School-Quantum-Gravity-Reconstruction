#!/usr/bin/env python3
"""RC-006 Eq.(29) source-topology/channel audit for k=12, gamma=1/3.

This audit intentionally stops before assigning a numerical value to the
non-trivial q-spin-network graph in Eq.(29).  It freezes only source-explicit
structure: EPRL map (22), SU(2)_k fusion, the J+/J- -> l coupling described
around Eq.(27)/(29), and the R-matrix intermediate channel appearing in the
Eq.(29) phase factor.  Any missing braiding/orientation contraction remains a
BLOCKER rather than being guessed.
"""
from fractions import Fraction
import argparse, json
from pathlib import Path

K=12
GAMMA=Fraction(1,3)
JMAX=K//2

def fuse(a,b):
    lo=abs(a-b); hi=min(a+b, K-a-b)
    return list(range(lo,hi+1)) if hi>=lo else []

def eprl_map(l):
    jp=Fraction(1+GAMMA,2)*l
    jm=Fraction(1-GAMMA,2)*l
    if jp.denominator!=1 or jm.denominator!=1: return None
    jp,jm=int(jp),int(jm)
    if 0<=jp<=JMAX and 0<=jm<=JMAX: return (jp,jm)
    return None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True)
    a=ap.parse_args()
    simple={l:eprl_map(l) for l in range(JMAX+1) if eprl_map(l) is not None}
    triples=[]
    for l1,m1 in simple.items():
      for l2,m2 in simple.items():
        for l,mt in simple.items():
          if l not in fuse(l1,l2): continue
          j1p,j1m=m1; j2p,j2m=m2; tp,tm=mt
          coarse=[]
          for Jp in fuse(j1p,j2p):
            for Jm in fuse(j1m,j2m):
              if l in fuse(Jp,Jm): coarse.append((Jp,Jm))
          crossing=fuse(j1p,j2m)
          phase_exponents=[]
          for j in crossing:
            x=-Fraction(1,2)*(j1p*(j1p+1)+j2m*(j2m+1)-j*(j+1))
            phase_exponents.append({'j':j,'q_exponent':[x.numerator,x.denominator]})
          target=(tp,tm)
          row={
            'l1':l1,'l2':l2,'l':l,
            'map_l1':list(m1),'map_l2':list(m2),'simplicity_target':list(target),
            'coarse_pairs':[list(x) for x in coarse],
            'coarse_pair_count':len(coarse),
            'simplicity_target_captured':target in coarse,
            'non_simple_coarse_pair_count':sum(x!=target for x in coarse),
            'r_crossing_channels':phase_exponents,
          }
          triples.append(row)
    total_pairs=sum(r['coarse_pair_count'] for r in triples)
    extra=sum(r['non_simple_coarse_pair_count'] for r in triples)
    structural_pass=bool(triples and all(r['simplicity_target_captured'] and r['r_crossing_channels'] for r in triples))
    out={
      'test':'RC006_EQ29_SOURCE_TOPOLOGY_CHANNEL_AUDIT',
      'source':'Dittrich-Schnetter-Seth-Steinhaus arXiv:1609.02429 Eq.(22), Eq.(26), Eq.(29), Appendix F',
      'k':K,'gamma':'1/3','integer_sector_source_map':{str(k):list(v) for k,v in simple.items()},
      'source_boundary_triple_count':len(triples),
      'total_admissible_coarse_pairs':total_pairs,
      'non_simple_coarse_pairs':extra,
      'non_simple_fraction':extra/max(total_pairs,1),
      'all_source_targets_captured':all(r['simplicity_target_captured'] for r in triples),
      'all_required_r_channels_nonempty':all(bool(r['r_crossing_channels']) for r in triples),
      'structural_channel_gate_pass':structural_pass,
      'full_eq29_numeric_amplitude_authorized':False,
      'remaining_blocker':'The exact oriented/braided Eq.(29) q-spin-network contraction must be mapped through Appendix-F/B15 plus the Eq.(26) R-matrix identity before numerical amplitudes are authorized. This audit does not replace that graph evaluation.',
      'claim_lock':'Support/topology prerequisite only; not an Eq.(29) amplitude, Appendix-C TNR flow, refinement, continuum, bridge, or new-physics result.',
      'triples':triples,
    }
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='triples'},indent=2,sort_keys=True))
    if not structural_pass: raise SystemExit(2)

if __name__=='__main__': main()
