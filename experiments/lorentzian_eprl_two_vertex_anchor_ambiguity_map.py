#!/usr/bin/env python3
"""Diagnostic map for the failed two-vertex source-selection gate.

This preserves the frozen target regexes from the robustness test and reports
which exact math environment each anchor occurrence selects, with source file,
line range, labels and section context. Diagnostic only: it cannot authorize
numerical implementation or alter the failed frozen gate.
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
SEC=re.compile(r'\\(?:sub)*section\{([^}]*)\}')
LABEL=re.compile(r'\\label\{([^}]*)\}')

def norm(s): return re.sub(r'\s+','',s)
def line_no(text,pos): return text.count('\n',0,pos)+1

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--target',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 pats=TARGETS[a.target]
 files=sorted(Path(a.source_dir).rglob('*.tex'))
 parts=[]; ranges=[]; off=0
 for f in files:
  t=f.read_text(errors='ignore'); parts.append(t); ranges.append((off,off+len(t),str(f),t)); off+=len(t)+1
 text='\n'.join(parts)
 env=[]
 for pat in MATH:
  for m in re.finditer(pat,text,re.S):
   raw=m.group(0); h=hashlib.sha256(norm(raw).encode()).hexdigest()
   rr=next((x for x in ranges if x[0] <= m.start() <= x[1]),None)
   path=rr[2] if rr else None; local=(m.start()-rr[0]) if rr else 0; ft=rr[3] if rr else ''
   secs=list(SEC.finditer(ft[:local])); sec=secs[-1].group(1) if secs else None
   labels=LABEL.findall(raw)
   env.append({'start':m.start(),'end':m.end(),'hash':h,'path':path,'line_start':line_no(ft,local) if rr else None,
               'line_end':line_no(ft,local+len(raw)) if rr else None,'labels':labels,'section':sec})
 env.sort(key=lambda x:x['start'])
 anchors=[]
 for pi,p in enumerate(pats):
  for m in re.finditer(p,text,re.I|re.S):
   if not env: continue
   z=min(env,key=lambda e:min(abs(e['start']-m.start()),abs(e['end']-m.start())))
   d=min(abs(z['start']-m.start()),abs(z['end']-m.start()))
   if d<=2500:
    anchors.append({'pattern_index':pi,'pattern':p,'anchor_start':m.start(),'anchor_line_global':line_no(text,m.start()),'distance':d,
                    'selected_hash':z['hash'],'path':z['path'],'line_start':z['line_start'],'line_end':z['line_end'],
                    'labels':z['labels'],'section':z['section']})
 # Reproduce full and leave-one-pattern-out winners exactly by minimum distance.
 def winner(drop=None):
  q=[x for x in anchors if x['pattern_index']!=drop]
  return min(q,key=lambda x:x['distance']) if q else None
 full=winner(); hold=[]
 for i,p in enumerate(pats):
  w=winner(i); hold.append({'drop_index':i,'drop_pattern':p,'winner':w,'agrees_full':bool(w and full and w['selected_hash']==full['selected_hash'])})
 hashes=sorted({x['selected_hash'] for x in anchors})
 out={'test':'LORENTZIAN_EPRL_TWO_VERTEX_ANCHOR_AMBIGUITY_MAP','target':a.target,'valid':bool(files and env and full),
      'pattern_count':len(pats),'anchor_candidate_count':len(anchors),'distinct_selected_hash_count':len(hashes),
      'distinct_selected_hashes':hashes,'full_winner':full,'holdouts':hold,'anchor_candidates':anchors,
      'classification':'DIAGNOSTIC_SOURCE_AMBIGUITY_LOCALIZED' if files and env and full else 'DIAGNOSTIC_INVALID',
      'interpretation_lock':'Diagnostic only. It preserves the failed frozen source-lock and cannot authorize amplitude implementation or relax any criterion.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('anchor_candidates','holdouts')},indent=2,sort_keys=True))
 if not out['valid']: raise SystemExit(2)
if __name__=='__main__': main()
