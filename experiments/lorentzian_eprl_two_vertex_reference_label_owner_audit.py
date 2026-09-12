#!/usr/bin/env python3
"""Classify source-authored TeX reference labels near two-vertex targets.

This is a follow-up to the preserved 2/8 equation-selection robustness FAIL.
It does not alter any prior gate.  For each reference near an unchanged target
anchor it resolves the raw label definition and records the enclosing TeX
environment stack, source file/line and whether the owner is math-like.
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
LABEL=re.compile(r'\\label\{([^}]*)\}')
REF=re.compile(r'\\(eqref|ref)\{([^}]*)\}')
TOK=re.compile(r'\\(begin|end)\{([^}]*)\}')
SEC=re.compile(r'\\(section|subsection|subsubsection)\{([^}]*)\}')
MATH_ENVS={'equation','equation*','align','align*','alignat','alignat*','gather','gather*','multline','multline*','split','cases','eqnarray','eqnarray*'}
DISPLAY_MATH=re.compile(r'\\\[(.*?)\\\]',re.S)

def line_no(t,p): return t.count('\n',0,p)+1

def stack_at(t,pos):
 st=[]
 for m in TOK.finditer(t,0,pos):
  kind,env=m.group(1),m.group(2)
  if kind=='begin': st.append(env)
  else:
   if env in st:
    i=len(st)-1-st[::-1].index(env); st=st[:i]
 return st

def enclosing_env_span(t,pos,env):
 # Locate nearest unmatched begin{env} before pos and its matching end after pos.
 starts=[m for m in re.finditer(r'\\begin\{'+re.escape(env)+r'\}',t[:pos])]
 if not starts: return None
 s=starts[-1].start(); depth=0
 pat=re.compile(r'\\(begin|end)\{'+re.escape(env)+r'\}')
 for m in pat.finditer(t,s):
  depth += 1 if m.group(1)=='begin' else -1
  if depth==0: return (s,m.end())
 return None

def owner_record(path,t,pos,label):
 st=stack_at(t,pos)
 math_env=next((e for e in reversed(st) if e in MATH_ENVS),None)
 span=enclosing_env_span(t,pos,math_env) if math_env else None
 mh=None
 if span: mh=hashlib.sha256(re.sub(r'\s+','',t[span[0]:span[1]]).encode()).hexdigest()
 secs=list(SEC.finditer(t,0,pos)); sec=secs[-1].group(2) if secs else None
 return {'label':label,'path':path,'line':line_no(t,pos),'environment_stack':st[-6:],
         'owner_environment':st[-1] if st else None,'math_environment':math_env,'math_hash':mh,'section':sec,
         'math_like':bool(math_env)}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--target',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 files=sorted(Path(a.source_dir).rglob('*.tex')); defs={}; data={}
 for f in files:
  t=f.read_text(errors='ignore'); data[str(f)]=t
  for m in LABEL.finditer(t): defs.setdefault(m.group(1),[]).append(owner_record(str(f),t,m.start(),m.group(1)))
 anchors=[]
 for path,t in data.items():
  for pi,p in enumerate(TARGETS[a.target]):
   for m in re.finditer(p,t,re.I|re.S): anchors.append((path,t,pi,p,m.start()))
 refs=[]
 for path,t,pi,p,pos in anchors:
  lo=max(0,pos-600); hi=min(len(t),pos+600)
  for rm in REF.finditer(t[lo:hi]):
   lab=rm.group(2); refs.append({'pattern_index':pi,'pattern':p,'anchor_line':line_no(t,pos),'path':path,
     'reference_command':rm.group(1),'reference_label':lab,'reference_line':line_no(t,lo+rm.start()),'owners':defs.get(lab,[])})
 labels=sorted({r['reference_label'] for r in refs}); resolved=sorted({r['reference_label'] for r in refs if r['owners']})
 math_labels=sorted({r['reference_label'] for r in refs if any(o['math_like'] for o in r['owners'])})
 eqref_labels=sorted({r['reference_label'] for r in refs if r['reference_command']=='eqref'})
 unique_math_hashes=sorted({o['math_hash'] for r in refs for o in r['owners'] if o['math_hash']})
 out={'test':'LORENTZIAN_EPRL_TWO_VERTEX_REFERENCE_LABEL_OWNER_AUDIT','target':a.target,'valid':bool(files),
      'anchor_occurrence_count':len(anchors),'nearby_reference_count':len(refs),'referenced_label_count':len(labels),
      'resolved_label_count':len(resolved),'math_owner_label_count':len(math_labels),'math_owner_labels':math_labels,
      'eqref_labels':eqref_labels,'math_owner_hash_count':len(unique_math_hashes),'math_owner_hashes':unique_math_hashes,
      'references':refs,
      'classification':'LABEL_OWNERS_LOCALIZED' if files else 'DIAGNOSTIC_INVALID',
      'promotion_authorized':False,
      'interpretation_lock':'Diagnostic only. The old 2/8 source-lock FAIL remains authoritative; this audit can only motivate a new prospective label-first authority rule.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='references'},indent=2,sort_keys=True))
 if not out['valid']: raise SystemExit(2)
if __name__=='__main__': main()
