#!/usr/bin/env python3
"""Source-faithful serialization of the labelled DVD2/DVD3 amplitudes into B4 calls.

The new prospective rule is structural, not proximity-based:
- unique paper root for arXiv:1801.03771;
- exact labelled equation DVD2 or DVD3;
- exact owner section `Evaluations of the `face-rigid' DVD foams`;
- every `_images/B4.eps` factor must carry exactly the ten source psfrag slots
  a,b,c,d,e,f,g,h,i,k;
- source convention from Bsn/sl2cfoam API: a-d -> j1..j4, e-h -> l1..l4,
  i,k -> intertwiner indices;
- exactly three B4 factors are required for each labelled amplitude.
This gate serializes source syntax only and contains no numerical amplitude result.
"""
from pathlib import Path
import argparse, hashlib, json, re

TITLE=re.compile(r'\\title\{([^}]*)\}',re.S)
SEC=re.compile(r'\\(section|subsection|subsubsection)\{([^}]*)\}')
REQUIRED=list('abcdefgh')+['i','k']
EXPECTED_SECTION="Evaluations of the `face-rigid' DVD foams"

def line_no(t,p): return t.count('\n',0,p)+1
def sec_at(t,p):
 ss=list(SEC.finditer(t,0,p)); return ss[-1].group(2) if ss else None

def root(source_dir):
 rr=[]
 for f in Path(source_dir).rglob('*.tex'):
  t=f.read_text(errors='ignore')
  if '\\documentclass' in t and '\\begin{document}' in t:
   mt=TITLE.search(t); title=re.sub(r'\s+',' ',mt.group(1)).strip() if mt else ''
   if re.search(r'Lorentzian',title,re.I) and re.search(r'Spin.?Foam',title,re.I): rr.append((f,t,title))
 return rr[0] if len(rr)==1 else (None,None,None)

def labelled_environment(t,label):
 lm=re.search(r'\\label\{'+re.escape(label)+r'\}',t)
 if not lm: return None
 # Both targets are ordinary equation environments. Find nearest enclosing begin/end.
 starts=[m for m in re.finditer(r'\\begin\{equation\}',t[:lm.start()])]
 if not starts: return None
 s=starts[-1].start(); em=re.search(r'\\end\{equation\}',t[lm.end():])
 if not em: return None
 e=lm.end()+em.end()
 return s,e,t[s:e]

def arrays(raw,base_offset,t):
 # Each B4 source factor is an array ending at an includegraphics of B4.eps.
 out=[]
 for gm in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\{_images/B4\.eps\}',raw):
  # nearest array begin before graphics, with no later begin after it intended as another factor
  begins=[m for m in re.finditer(r'\\begin\{array\}\{c\}',raw[:gm.start()])]
  if not begins: continue
  s=begins[-1].start()
  em=re.search(r'\\end\{array\}',raw[gm.end():])
  if not em: continue
  e=gm.end()+em.end(); chunk=raw[s:e]
  pairs=re.findall(r'\\psfrag\{([^}]+)\}\{\$([^$]+)\$\}',chunk)
  mp={}; dup=[]
  for k,v in pairs:
   if k in mp: dup.append(k)
   mp[k]=v.strip()
  out.append({'source_line':line_no(t,base_offset+s),'slot_keys':sorted(mp),'duplicate_keys':sorted(set(dup)),
              'j':[mp.get(x) for x in 'abcd'],'l':[mp.get(x) for x in 'efgh'],'i':mp.get('i'),'k':mp.get('k'),
              'all_required_present':all(x in mp for x in REQUIRED),'unexpected_keys':sorted(set(mp)-set(REQUIRED))})
 return out

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--label',required=True,choices=['DVD2','DVD3']); ap.add_argument('--output',required=True); a=ap.parse_args()
 f,t,title=root(a.source_dir); valid_root=f is not None
 env=labelled_environment(t,a.label) if valid_root else None
 if env:
  s,e,raw=env; section=sec_at(t,s); fac=arrays(raw,s,t); equation_hash=hashlib.sha256(re.sub(r'\s+','',raw).encode()).hexdigest()
 else:
  s=e=0; raw=''; section=None; fac=[]; equation_hash=None
 factor_ok=len(fac)==3 and all(x['all_required_present'] and not x['duplicate_keys'] and not x['unexpected_keys'] for x in fac)
 gate=bool(valid_root and env and section==EXPECTED_SECTION and raw.count('\\sum')==1 and factor_ok)
 out={'test':'LORENTZIAN_EPRL_DVD_B4_SERIALIZATION','label':a.label,'valid':bool(valid_root and env),
      'root_path':str(f) if f else None,'root_sha256':hashlib.sha256(t.encode()).hexdigest() if valid_root else None,'root_title':title,
      'equation_hash':equation_hash,'line_start':line_no(t,s) if env else None,'line_end':line_no(t,e) if env else None,'section':section,
      'sum_count':raw.count('\\sum'),'b4_factor_count':len(fac),'factors':fac,
      'serialization_gate_pass':gate,'classification':'SOURCE_B4_SERIALIZATION_PASS' if gate else 'SOURCE_B4_SERIALIZATION_FAIL',
      'mapping_rule':'a-d => j1..j4; e-h => l1..l4; i,k => B4 intertwiner indices',
      'promotion_authorized':False,
      'interpretation_lock':'Source syntax serialization only. PASS authorizes an independent numerical B4 infrastructure pilot, not a paper reproduction/refinement/bridge claim.'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='factors'},indent=2,sort_keys=True))
 if not gate: raise SystemExit(2)
if __name__=='__main__': main()
