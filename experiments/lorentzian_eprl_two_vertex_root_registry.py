#!/usr/bin/env python3
"""Build a provenance registry for the actual arXiv paper root document.

Diagnostic prerequisite after the failed proximity-based source lock.  It finds
TeX root documents structurally, identifies the root containing the paper title,
and inventories labelled math environments, sections, references and compact
operator signatures without selecting an equation for any target.
"""
from pathlib import Path
import argparse, hashlib, json, re

MATH_ENVS=('equation','equation*','align','align*','alignat','alignat*','gather','gather*','multline','multline*','eqnarray','eqnarray*')
BEGIN=re.compile(r'\\begin\{([^}]*)\}')
LABEL=re.compile(r'\\label\{([^}]*)\}')
REF=re.compile(r'\\(?:eqref|ref)\{([^}]*)\}')
SEC=re.compile(r'\\(section|subsection|subsubsection)\{([^}]*)\}')
TITLE_RE=re.compile(r'\\title\{([^}]*)\}',re.S)

def line_no(t,p): return t.count('\n',0,p)+1

def env_spans(t,env):
 pat=re.compile(r'\\(begin|end)\{'+re.escape(env)+r'\}')
 stack=[]; out=[]
 for m in pat.finditer(t):
  if m.group(1)=='begin': stack.append(m.start())
  elif stack:
   s=stack.pop()
   if not stack: out.append((s,m.end()))
 return out

def section_at(t,pos):
 ss=list(SEC.finditer(t,0,pos)); return ss[-1].group(2) if ss else None

def signature(raw):
 return {
  'has_sum': '\\sum' in raw,
  'has_prod': '\\prod' in raw,
  'has_integral': any(x in raw for x in ('\\int','\\mathrm{d}','\\dd')),
  'has_asymptotic': ('\\sim' in raw or '\\simeq' in raw),
  'has_gamma': ('\\gamma' in raw or '\\g' in raw),
  'has_delta_l': ('Delta l' in raw or '\\Delta l' in raw),
  'has_correlation_C': bool(re.search(r'\bC[_^{]',raw)),
  'has_amplitude_A_or_W': bool(re.search(r'(?<![A-Za-z])[AW][_^({]',raw)),
  'sum_count': raw.count('\\sum'),
  'integral_count': raw.count('\\int'),
  'length': len(raw)
 }

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 files=sorted(Path(a.source_dir).rglob('*.tex')); roots=[]
 for f in files:
  t=f.read_text(errors='ignore')
  if '\\documentclass' in t and '\\begin{document}' in t:
   mt=TITLE_RE.search(t); roots.append({'path':str(f),'title':re.sub(r'\s+',' ',mt.group(1)).strip() if mt else None,'sha256':hashlib.sha256(t.encode()).hexdigest(),'bytes':len(t)})
 # Prefer the structurally unique root whose title contains both Lorentzian and Spin Foam.
 cands=[r for r in roots if r['title'] and re.search(r'Lorentzian',r['title'],re.I) and re.search(r'Spin.?Foam',r['title'],re.I)]
 root=(cands[0] if len(cands)==1 else None)
 registry=[]; duplicates=[]; refs=[]
 if root:
  p=Path(root['path']); t=p.read_text(errors='ignore')
  for env in MATH_ENVS:
   for s,e in env_spans(t,env):
    raw=t[s:e]; labs=LABEL.findall(raw)
    if not labs: continue
    h=hashlib.sha256(re.sub(r'\s+','',raw).encode()).hexdigest()
    registry.append({'labels':labs,'environment':env,'line_start':line_no(t,s),'line_end':line_no(t,e),'section':section_at(t,s),'math_hash':h,'signature':signature(raw)})
  label_occ={}
  for rec in registry:
   for lab in rec['labels']: label_occ.setdefault(lab,[]).append(rec['math_hash'])
  duplicates=sorted([k for k,v in label_occ.items() if len(v)>1])
  for m in REF.finditer(t): refs.append({'label':m.group(1),'line':line_no(t,m.start()),'section':section_at(t,m.start())})
 out={'test':'LORENTZIAN_EPRL_TWO_VERTEX_ROOT_REGISTRY','source':'arXiv:1801.03771','valid':bool(files),
      'tex_file_count':len(files),'root_document_count':len(roots),'paper_root_candidate_count':len(cands),'paper_root':root,
      'labelled_math_environment_count':len(registry),'duplicate_math_labels':duplicates,'reference_count':len(refs),
      'registry':sorted(registry,key=lambda x:x['line_start']),'references':refs,
      'classification':'PAPER_ROOT_REGISTRY_COMPLETE' if root and not duplicates else ('PAPER_ROOT_AMBIGUOUS' if not root else 'PAPER_ROOT_DUPLICATE_MATH_LABELS'),
      'promotion_authorized':False,
      'interpretation_lock':'Provenance registry only. It selects no target equation and cannot authorize numerical implementation; a new semantic source lock must be preregistered separately.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('registry','references')},indent=2,sort_keys=True))
 if not root: raise SystemExit(2)
if __name__=='__main__': main()
