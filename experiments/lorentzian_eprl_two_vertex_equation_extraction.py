#!/usr/bin/env python3
"""Exact source equation/observable extraction for arXiv:1801.03771.

This gate follows successful source qualification. It extracts labelled/nearby
mathematical environments for prospectively frozen numerical targets without
introducing any ansatz. PASS only authorizes implementation of the extracted
objects; it is not numerical reproduction or refinement.
"""
from pathlib import Path
import argparse,json,re
REQ={
 'two_vertex_amplitude':[r'two[- ]vertex',r'transition amplitude',r'amplitude'],
 'internal_face_sum':[r'internal face',r'bulk face',r'\\sum'],
 'full_amplitude':[r'full EPRL',r'full amplitude'],
 'simplified_amplitude':[r'simplified EPRL',r'simplified amplitude'],
 'correlation_observable':[r'correlation',r'correlator'],
 'large_spin_scaling':[r'large spin',r'asymptotic',r'power[- ]law'],
 'immirzi':[r'Immirzi',r'gamma'],
 'cutoff_or_truncation':[r'cutoff',r'truncat',r'virtual spin',r'booster']
}
MATH=[('equation',r'\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}'),('align',r'\\begin\{align\*?\}(.*?)\\end\{align\*?\}'),('display',r'\\\[(.*?)\\\]')]
def envs(text):
 out=[]
 for typ,pat in MATH:
  for m in re.finditer(pat,text,re.S): out.append((m.start(),m.end(),typ,m.group(0)))
 return sorted(out)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--target',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 if a.target not in REQ: raise SystemExit('bad target')
 fs=list(Path(a.source_dir).rglob('*.tex')); text='\n'.join(f.read_text(errors='ignore') for f in fs); ee=envs(text)
 anchors=[]
 for pat in REQ[a.target]:
  for m in re.finditer(pat,text,re.I|re.S): anchors.append((m.start(),pat,re.sub(r'\s+',' ',text[max(0,m.start()-160):min(len(text),m.end()+220)])[:440]))
 cand=[]
 for pos,pat,snip in anchors[:50]:
  near=sorted(ee,key=lambda z:min(abs(z[0]-pos),abs(z[1]-pos)))[:4]
  for lo,hi,typ,raw in near:
   dist=min(abs(lo-pos),abs(hi-pos))
   if dist<=2500:
    labels=re.findall(r'\\label\{([^}]+)\}',raw)
    cand.append({'distance':dist,'type':typ,'labels':labels,'math':raw[:5000],'anchor_pattern':pat,'anchor_context':snip})
 # exact de-duplicate by math
 seen=set(); uniq=[]
 for c in sorted(cand,key=lambda x:x['distance']):
  k=c['math']
  if k not in seen: seen.add(k); uniq.append(c)
 present=bool(anchors); equation_available=bool(uniq)
 out={'test':'LORENTZIAN_EPRL_TWO_VERTEX_EQUATION_EXTRACTION','source':'arXiv:1801.03771','target':a.target,
      'valid':bool(fs and text),'anchor_count':len(anchors),'source_object_present':present,'nearby_math_environment_count':len(uniq),
      'equation_available':equation_available,'candidates':uniq[:12],
      'classification':'SOURCE_EQUATION_OBJECT_EXTRACTED' if present and equation_available else ('SOURCE_OBJECT_TEXT_ONLY_NO_NEARBY_MATH' if present else 'SOURCE_OBJECT_NOT_LOCATED'),
      'interpretation_lock':'Extraction prerequisite only; equations must be independently reviewed/frozen before numerical reproduction. No refinement or bridge claim.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='candidates'},indent=2,sort_keys=True))
if __name__=='__main__': main()
