#!/usr/bin/env python3
"""Held-out robustness/null calibration for RC006 ordered-context uniqueness.
Frozen interpretation: every leave-one-anchor-out lane must remain unique; the
null lane that removes ordered-neighbor/position information must be non-unique.
No rendered geometry or post-result convention choice is used.
"""
from pathlib import Path
import argparse,collections,json,math,re
ALL=('app:EPRL-diagram','app:EPRL-norm','app:graph','eq:BC-3-int','eq:BC-3-valent','eq:eprl-3-valent','eq:eprl-map','eq:recoupling-basis')
ROLES=ALL+('null_unordered',)
ENVS=('equation','equation*','align','align*','gather','gather*','multline','multline*','split','array','pmatrix','bmatrix','tikzpicture','figure','figure*')
PAT=re.compile(r'(?<![A-Za-z])([jJlmn])\s*((?:_\s*(?:\{[^{}]*\}|[A-Za-z0-9+\-]+)|\^\s*(?:\{[^{}]*\}|[A-Za-z0-9+\-]+)){1,2})')
def enclosing(t,p):
 c=[]
 for e in ENVS:
  for b in re.finditer(r'\\begin\{'+re.escape(e)+r'\}',t[:p]):
   z=re.search(r'\\end\{'+re.escape(e)+r'\}',t[p:])
   if z and not re.search(r'\\end\{'+re.escape(e)+r'\}',t[b.end():p]): c.append((p+z.end()-b.start(),b.start(),p+z.end()))
 return min(c) if c else None
def block(t,n):
 m=list(re.finditer(r'\\label\s*\{'+re.escape(n)+r'\}',t));
 if len(m)!=1:return ''
 p=m[0].start();e=enclosing(t,p)
 return t[e[1]:e[2]] if e else t[max(0,p-1200):min(len(t),p+2200)]
def seq(s):
 fr=[]
 for e in ENVS: fr += [m.group(0) for m in re.finditer(r'\\begin\{'+re.escape(e)+r'\}(.*?)\\end\{'+re.escape(e)+r'\}',s,re.S)]
 fr += [m.group(1) for m in re.finditer(r'(?<!\\)\$(?!\$)(.+?)(?<!\\)\$(?!\$)',s,re.S)]
 fr += [m.group(1) for m in re.finditer(r'\\\[(.*?)\\\]',s,re.S)]
 out=[]
 for f in fr:
  for m in PAT.finditer(f): out.append(m.group(1)+re.sub(r'\s+','',m.group(2)))
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--source-dir',required=True);ap.add_argument('--role',choices=ROLES,required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
 fs=list(Path(a.source_dir).rglob('*.tex'))
 if len(fs)!=1:raise SystemExit('monolithic prerequisite violated')
 t=fs[0].read_text(errors='ignore');S={n:seq(block(t,n)) for n in ALL}
 kept=ALL if a.role=='null_unordered' else tuple(n for n in ALL if n!=a.role)
 U=sorted(set(x for n in kept for x in S[n]));fps={}
 for x in U:
  parts=[]
  for n in kept:
   q=S[n];occ=[]
   for i,v in enumerate(q):
    if v==x:
     if a.role=='null_unordered': occ.append(('COUNT',))
     else: occ.append((q[i-1] if i else '<BOS>',q[i+1] if i+1<len(q) else '<EOS>',min(3,int(4*i/max(1,len(q))))))
   parts.append(tuple(sorted(occ)))
  fps[x]=tuple(parts)
 g=collections.defaultdict(list)
 for x,p in fps.items():g[(x[0],p)].append(x)
 inter=[sorted(v) for v in g.values() if len(v)>1];unique=len(inter)==0;valid=len(U)>=3 and len(kept)>=7
 if a.role=='null_unordered': sci='SCIENTIFIC_PASS_NULL_RESTORES_AMBIGUITY' if valid and not unique else 'SCIENTIFIC_FAIL_NULL_DID_NOT_RESTORE_AMBIGUITY'
 else:sci='SCIENTIFIC_PASS_HOLDOUT_UNIQUE' if valid and unique else ('SCIENTIFIC_FAIL_HOLDOUT_NONUNIQUE' if valid else 'BLOCKED_INVALID')
 o={'test':'RC006_ORDERED_CONTEXT_HOLDOUT','role':a.role,'kept_anchors':list(kept),'valid_computation':valid,'ordered_context_unique':unique,'interchangeable_group_count':len(inter),'interchangeable_groups':inter,'scientific_classification':sci,'interpretation_rule':'All eight holdouts must remain unique and null_unordered must be nonunique to authorize robust source-order mapping.','claim_lock':'No Eq29 amplitude/bridge/candidate-theory claim.'}
 Path(a.output).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');print(json.dumps(o,indent=2,sort_keys=True))
 if not valid:raise SystemExit(2)
if __name__=='__main__':main()
