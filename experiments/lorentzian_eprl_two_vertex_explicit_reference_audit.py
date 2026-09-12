#!/usr/bin/env python3
"""Audit explicit TeX equation references near frozen two-vertex target anchors.

Searches the pinned source for source-authored \\eqref/\\ref links near occurrences
of the unchanged failed-gate target regexes, then resolves labels to exact math
environments. Diagnostic only; it does not replace or retroactively pass the
failed nearest-environment robustness gate.
"""
from pathlib import Path
import argparse, hashlib, json, re

TARGETS={
 'two_vertex_amplitude':[r'two[- ]vertex',r'transition amplitude',r'amplitude'],
 'internal_face_sum':[r'internal face',r'bulk face',r'\\sum'],
 'simplified_amplitude':[r'simplified EPRL',r'simplified amplitude'],
 'large_spin_scaling':[r'large spin',r'asymptotic',r'power[- ]law'],
 'immirzi':[r'Immirzi',r'gamma'],
 'cutoff_or_truncation':[r'cutoff',r'truncat',r'virtual spin',r'booster']
}
MATH=[r'\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}',r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}',r'\\\[(.*?)\\\]']
LABEL=re.compile(r'\\label\{([^}]*)\}')
REF=re.compile(r'\\(?:eqref|ref)\{([^}]*)\}')
SEC=re.compile(r'\\(?:sub)*section\{([^}]*)\}')

def norm(s): return re.sub(r'\s+','',s)
def line_no(text,pos): return text.count('\n',0,pos)+1

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--target',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 pats=TARGETS[a.target]; files=sorted(Path(a.source_dir).rglob('*.tex'))
 label_map={}; anchors=[]
 for f in files:
  t=f.read_text(errors='ignore')
  for pat in MATH:
   for m in re.finditer(pat,t,re.S):
    raw=m.group(0); h=hashlib.sha256(norm(raw).encode()).hexdigest(); labs=LABEL.findall(raw)
    secs=list(SEC.finditer(t[:m.start()])); sec=secs[-1].group(1) if secs else None
    rec={'path':str(f),'line_start':line_no(t,m.start()),'line_end':line_no(t,m.end()),'hash':h,'labels':labs,'section':sec}
    for lab in labs: label_map.setdefault(lab,[]).append(rec)
  for pi,p in enumerate(pats):
   for m in re.finditer(p,t,re.I|re.S): anchors.append((str(f),t,pi,p,m.start()))
 refs=[]
 for path,t,pi,p,pos in anchors:
  lo=max(0,pos-600); hi=min(len(t),pos+600); window=t[lo:hi]
  for rm in REF.finditer(window):
   lab=rm.group(1); resolved=label_map.get(lab,[])
   refs.append({'pattern_index':pi,'pattern':p,'anchor_line':line_no(t,pos),'path':path,'reference_label':lab,
                'reference_line':line_no(t,lo+rm.start()),'resolved':resolved})
 unique_labels=sorted({r['reference_label'] for r in refs})
 resolved_labels=sorted({r['reference_label'] for r in refs if r['resolved']})
 resolved_hashes=sorted({e['hash'] for r in refs for e in r['resolved']})
 if not files:
  cls='DIAGNOSTIC_INVALID'
 elif len(resolved_hashes)==1:
  cls='DIAGNOSTIC_UNIQUE_EXPLICIT_SOURCE_REFERENCE'
 elif len(resolved_hashes)>1:
  cls='DIAGNOSTIC_MULTIPLE_EXPLICIT_SOURCE_REFERENCES'
 else:
  cls='DIAGNOSTIC_NO_RESOLVED_EXPLICIT_SOURCE_REFERENCE'
 out={'test':'LORENTZIAN_EPRL_TWO_VERTEX_EXPLICIT_REFERENCE_AUDIT','target':a.target,'valid':bool(files),
      'anchor_occurrence_count':len(anchors),'nearby_reference_count':len(refs),'unique_reference_labels':unique_labels,
      'resolved_reference_labels':resolved_labels,'resolved_math_hashes':resolved_hashes,'resolved_math_hash_count':len(resolved_hashes),
      'references':refs,'classification':cls,
      'interpretation_lock':'Diagnostic source authority only. A unique explicit reference may motivate a new prospectively frozen source-lock, but does not retroactively change the 2/8 robustness FAIL or authorize numerical reproduction.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='references'},indent=2,sort_keys=True))
 if not out['valid']: raise SystemExit(2)
if __name__=='__main__': main()
