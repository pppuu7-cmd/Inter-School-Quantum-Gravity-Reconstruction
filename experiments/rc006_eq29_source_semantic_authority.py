#!/usr/bin/env python3
"""Prospective source-semantic authority audit for RC006 Eq.(29).

After the frozen graphic-proximity gate failed, this audit searches only the
official arXiv source for explicit textual/equational authority. It does not
infer label assignments from picture geometry and does not evaluate amplitudes.
"""
from pathlib import Path
import argparse, hashlib, json, re

TARGET='Before we discuss the behaviour of the EPRL model under coarse graining'

def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def line(t,p): return t.count('\n',0,p)+1

def norm(s):
    s=re.sub(r'%.*',' ',s)
    return ' '.join(s.split())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--authority',required=True,choices=['braiding','representations','internal_channels','eq29_context']); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.source_dir); hit=None
    for p in root.rglob('*.tex'):
        text=p.read_text(errors='ignore')
        q=text.lower().find(TARGET.lower())
        if q>=0: hit=(p,text,q); break
    if not hit: raise SystemExit('Eq29 source region not found')
    p,text,q=hit
    # Search the full source file, but separately record the local Eq29 window.
    windows={
      'braiding':[r'R[- ]?matrix',r'braid',r'crossing',r'\\mathcal\{R\}',r'\\mathcal R'],
      'representations':[r'J\^\{?\\?\+\}?',r'J\^\{?\\?-\}?',r'j\^\{?\\?\+\}?',r'j\^\{?\\?-\}?'],
      'internal_channels':[r'l_\{?1\}?',r'l_\{?2\}?',r'\\ell_\{?1\}?',r'\\ell_\{?2\}?'],
      'eq29_context':[r'coarse graining',r'EPRL',r'R[- ]?matrix',r'crossing']
    }
    pats=windows[a.authority]; matches=[]
    for pat in pats:
        rx=re.compile(pat,re.I)
        for m in rx.finditer(text):
            lo=max(0,m.start()-500); hi=min(len(text),m.end()+500); ctx=norm(text[lo:hi])
            matches.append({'pattern':pat,'line':line(text,m.start()),'context_sha256':sha(ctx),'context_char_count':len(ctx),'distance_lines_to_eq29':abs(line(text,m.start())-line(text,q))})
    local=[x for x in matches if x['distance_lines_to_eq29']<=180]
    # Frozen authority gate is intentionally conservative: at least two distinct
    # preregistered source patterns must occur, one within 180 lines of Eq29.
    distinct=len({x['pattern'] for x in matches})
    ok=distinct>=2 and len(local)>=1
    out={'test':'RC006_EQ29_SOURCE_SEMANTIC_AUTHORITY','authority':a.authority,
         'source':'official arXiv 1609.02429 source archive','tex_path':str(p.relative_to(root)),
         'tex_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'eq29_anchor_line':line(text,q),
         'patterns':pats,'distinct_patterns_found':distinct,'match_count':len(matches),'local_match_count':len(local),
         'matches':matches,'frozen_gate_pass':ok,
         'interpretation':'PASS means explicit source material exists for a manual/contraction mapping; it does not assert that all graph labels/orientations are already uniquely reconstructed.',
         'claim_lock':'No geometry-only inference, no Eq29 amplitude, no BRIDGE_DERIVED claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='matches'},indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()
