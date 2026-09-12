#!/usr/bin/env python3
"""Root-only provenance diagnostic for the eight two-vertex source targets.

Unlike the failed legacy selector, this script never concatenates TeX files.
It first identifies the paper root structurally, then reports the nearest labelled
math object(s) to target anchors inside that root only. Diagnostic only: no target
is promoted and no numerical implementation is authorized.
"""
from pathlib import Path
import argparse, hashlib, json, re
TARGETS={
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
SEC=re.compile(r'\\(?:sub)*section\{([^}]*)\}')
TITLE=re.compile(r'\\title\{([^}]*)\}',re.S)

def line_no(t,p): return t.count('\n',0,p)+1
def sec_at(t,p):
 ss=list(SEC.finditer(t,0,p)); return ss[-1].group(1) if ss else None
def sig(raw):
 return {'has_sum':'\\sum' in raw,'has_integral':'\\int' in raw,'has_asymptotic':('\\sim' in raw or '\\simeq' in raw),
         'has_gamma':('\\gamma' in raw or '\\g' in raw),'has_delta_l':'\\Delta l' in raw,
         'has_C':bool(re.search(r'(?<![A-Za-z])C[_^{]',raw)),'has_A_or_W':bool(re.search(r'(?<![A-Za-z])[AW][_^({]',raw)),
         'sum_count':raw.count('\\sum'),'integral_count':raw.count('\\int')}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--target',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 roots=[]
 for f in sorted(Path(a.source_dir).rglob('*.tex')):
  t=f.read_text(errors='ignore')
  if '\\documentclass' in t and '\\begin{document}' in t:
   mt=TITLE.search(t); title=re.sub(r'\s+',' ',mt.group(1)).strip() if mt else ''
   if re.search(r'Lorentzian',title,re.I) and re.search(r'Spin.?Foam',title,re.I): roots.append((f,t,title))
 valid=len(roots)==1
 if not valid:
  out={'test':'LORENTZIAN_EPRL_TWO_VERTEX_ROOT_TARGET_PROVENANCE','target':a.target,'valid':False,'root_count':len(roots),'classification':'ROOT_AMBIGUOUS','promotion_authorized':False}
  Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2)); raise SystemExit(2)
 f,t,title=roots[0]
 env=[]
 for typ,pat in MATH:
  for m in re.finditer(pat,t,re.S):
   raw=m.group(0); env.append({'start':m.start(),'end':m.end(),'type':typ,'hash':hashlib.sha256(re.sub(r'\s+','',raw).encode()).hexdigest(),
    'labels':re.findall(r'\\label\{([^}]+)\}',raw),'line_start':line_no(t,m.start()),'line_end':line_no(t,m.end()),'section':sec_at(t,m.start()),'signature':sig(raw)})
 anchors=[]
 for pi,p in enumerate(TARGETS[a.target]):
  for m in re.finditer(p,t,re.I|re.S): anchors.append({'pos':m.start(),'pattern_index':pi,'pattern':p,'line':line_no(t,m.start()),'section':sec_at(t,m.start())})
 candidates=[]
 for q in anchors:
  for e in sorted(env,key=lambda z:min(abs(z['start']-q['pos']),abs(z['end']-q['pos'])))[:3]:
   d=min(abs(e['start']-q['pos']),abs(e['end']-q['pos']))
   if d<=2500: candidates.append({**{k:v for k,v in e.items() if k not in ('start','end')},'distance':d,'anchor_pattern':q['pattern'],'anchor_line':q['line'],'anchor_section':q['section']})
 # unique exact objects, nearest occurrence first
 seen=set(); uniq=[]
 for c in sorted(candidates,key=lambda x:x['distance']):
  if c['hash'] not in seen: seen.add(c['hash']); uniq.append(c)
 out={'test':'LORENTZIAN_EPRL_TWO_VERTEX_ROOT_TARGET_PROVENANCE','target':a.target,'valid':True,'root_path':str(f),'root_title':title,
      'anchor_count':len(anchors),'candidate_count':len(uniq),'nearest_candidates':uniq[:12],
      'nearest_hash':uniq[0]['hash'] if uniq else None,'nearest_labels':uniq[0]['labels'] if uniq else [],'nearest_section':uniq[0]['section'] if uniq else None,
      'nearest_signature':uniq[0]['signature'] if uniq else None,
      'classification':'ROOT_ONLY_TARGET_PROVENANCE_LOCALIZED' if uniq else 'ROOT_TARGET_NO_NEARBY_MATH',
      'promotion_authorized':False,
      'interpretation_lock':'Diagnostic only. Root-only proximity is not a replacement source lock and cannot authorize numerical implementation.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='nearest_candidates'},indent=2,sort_keys=True))
if __name__=='__main__': main()
