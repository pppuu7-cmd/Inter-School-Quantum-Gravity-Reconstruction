#!/usr/bin/env python3
"""Prospective RC006 Eq.(29) / Appendix-F source-relation extraction gate.

This does not infer graph edges from drawing geometry.  It extracts exact source
contexts for independently preregistered semantic objects needed to turn the
Eq.(29) braided diagram into a contraction: coarse-graining Eq29 context,
R-matrix/crossing authority, EPRL representation labels, internal l channels,
recoupling/6j identities, Appendix-F derivation context, simplicity-map context,
and braiding language.  PASS means the source contains a stable machine-readable
context for the role; it does not mean the final contraction mapping is unique.
"""
from pathlib import Path
import argparse, hashlib, json, re

ROLE_PATTERNS={
 'eq29_context':[r'Before we discuss the behaviour of the EPRL model under coarse graining'],
 'rmatrix':[r'R[- ]?matrix',r'\\mathcal\{R\}',r'\\mathcal R'],
 'crossing':[r'crossing',r'crossed',r'braid'],
 'representations':[r'J\^\{?\\?\+\}?',r'J\^\{?\\?-\}?',r'j\^\{?\\?\+\}?',r'j\^\{?\\?-\}?'],
 'internal_l':[r'l_\{?1\}?',r'l_\{?2\}?',r'\\ell_\{?1\}?',r'\\ell_\{?2\}?'],
 'recoupling':[r'6j',r'six[- ]?j',r'recoupl'],
 'appendix_f':[r'Appendix\s*F',r'appendix\{[^}]*EPRL',r'appendix\{[^}]*coarse'],
 'simplicity':[r'simplicity',r'EPRL map',r'Y_\\gamma',r'Y\^\\gamma'],
}

def normalize(s):
    s=re.sub(r'%.*',' ',s)
    return ' '.join(s.split())

def line(t,p): return t.count('\n',0,p)+1

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--role',required=True,choices=sorted(ROLE_PATTERNS)); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.source_dir)
    files=[]
    for p in root.rglob('*.tex'):
        text=p.read_text(errors='ignore'); files.append((p,text))
    rows=[]
    for p,text in files:
        for pat in ROLE_PATTERNS[a.role]:
            for m in re.finditer(pat,text,re.I):
                lo=max(0,m.start()-700); hi=min(len(text),m.end()+700)
                ctx=normalize(text[lo:hi])
                rows.append({'tex_path':str(p.relative_to(root)),'pattern':pat,'line':line(text,m.start()),'context_sha256':hashlib.sha256(ctx.encode()).hexdigest(),'context':ctx})
    distinct_patterns=len({r['pattern'] for r in rows})
    # Frozen before result: anchor role requires one exact anchor; multi-pattern
    # roles require at least one source hit, with >=2 pattern forms when >=2 forms
    # were preregistered. This is source-readability qualification, not physics.
    required=1 if len(ROLE_PATTERNS[a.role])==1 else min(2,len(ROLE_PATTERNS[a.role]))
    ok=bool(rows) and distinct_patterns>=required
    out={'test':'RC006_EQ29_APPENDIXF_SOURCE_RELATION_EXTRACT','role':a.role,
         'source':'official arXiv 1609.02429 source archive','patterns':ROLE_PATTERNS[a.role],
         'match_count':len(rows),'distinct_patterns_found':distinct_patterns,'frozen_required_distinct_patterns':required,
         'source_contexts':rows,'frozen_gate_pass':ok,
         'classification_if_pass':'PASS_SOURCE_RELATION_CONTEXT_AVAILABLE_ONLY',
         'claim_lock':'No geometry inference; no unique contraction asserted; no Eq29 amplitude, TNR/refinement, bridge, or candidate-theory claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='source_contexts'},indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()
