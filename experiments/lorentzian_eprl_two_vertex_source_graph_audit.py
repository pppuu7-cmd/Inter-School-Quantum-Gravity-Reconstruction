#!/usr/bin/env python3
"""Source-authored provenance audits for arXiv:1801.03771.

Modes are independent diagnostics after the frozen proximity source-lock failed:
  label_graph          map labelled math objects to explicit source references;
  equation_bundle      extract exact selected labelled math objects + dependencies;
  resource_manifest    inventory source-authored computational URLs/code hints/files.
No mode authorizes numerical implementation or changes the preserved FAIL.
"""
from pathlib import Path
import argparse, hashlib, json, re

MATH_ENVS=('equation','equation*','align','align*','alignat','alignat*','gather','gather*','multline','multline*','eqnarray','eqnarray*')
LABEL=re.compile(r'\\label\{([^}]*)\}')
REF=re.compile(r'\\(eqref|ref)\{([^}]*)\}')
SEC=re.compile(r'\\(section|subsection|subsubsection)\{([^}]*)\}')
URL=re.compile(r'https?://[^\s}\]>)]+')
TITLE=re.compile(r'\\title\{([^}]*)\}',re.S)
TARGET_LABELS=['Wseries','Dortho','Bsn','B3InhomLim','ADLD5','giorgio','decaffeinato','DVD2','DVD3']

def line_no(t,p): return t.count('\n',0,p)+1

def section_at(t,p):
 ss=list(SEC.finditer(t,0,p)); return ss[-1].group(2) if ss else None

def env_spans(t,env):
 pat=re.compile(r'\\(begin|end)\{'+re.escape(env)+r'\}')
 stack=[]; out=[]
 for m in pat.finditer(t):
  if m.group(1)=='begin': stack.append(m.start())
  elif stack:
   s=stack.pop()
   if not stack: out.append((s,m.end()))
 return out

def root(source_dir):
 roots=[]
 for f in sorted(Path(source_dir).rglob('*.tex')):
  t=f.read_text(errors='ignore')
  if '\\documentclass' in t and '\\begin{document}' in t:
   mt=TITLE.search(t); title=re.sub(r'\s+',' ',mt.group(1)).strip() if mt else ''
   if re.search(r'Lorentzian',title,re.I) and re.search(r'Spin.?Foam',title,re.I): roots.append((f,t,title))
 return roots[0] if len(roots)==1 else (None,None,None)

def math_registry(t):
 rows=[]
 for env in MATH_ENVS:
  for s,e in env_spans(t,env):
   raw=t[s:e]; labs=LABEL.findall(raw)
   if not labs: continue
   rows.append({'labels':labs,'environment':env,'line_start':line_no(t,s),'line_end':line_no(t,e),'section':section_at(t,s),
                'hash':hashlib.sha256(re.sub(r'\s+','',raw).encode()).hexdigest(),'raw':raw})
 return sorted(rows,key=lambda x:x['line_start'])

def label_graph(path,t):
 reg=math_registry(t); owners={lab:r for r in reg for lab in r['labels']}
 edges=[]
 for m in REF.finditer(t):
  lab=m.group(2)
  if lab in owners:
   o=owners[lab]
   edges.append({'command':m.group(1),'label':lab,'reference_line':line_no(t,m.start()),'reference_section':section_at(t,m.start()),
                 'owner_line_start':o['line_start'],'owner_line_end':o['line_end'],'owner_section':o['section'],'owner_hash':o['hash']})
 nodes=[]
 for r in reg:
  for lab in r['labels']:
   es=[e for e in edges if e['label']==lab]
   nodes.append({'label':lab,'line_start':r['line_start'],'line_end':r['line_end'],'section':r['section'],'hash':r['hash'],
                 'reference_count':len(es),'reference_sections':sorted({e['reference_section'] for e in es if e['reference_section']})})
 return {'test':'LORENTZIAN_EPRL_TWO_VERTEX_SOURCE_LABEL_GRAPH','root_path':str(path),'math_node_count':len(nodes),'explicit_math_reference_edge_count':len(edges),
         'nodes':nodes,'edges':edges,'classification':'SOURCE_LABEL_GRAPH_COMPLETE','promotion_authorized':False,
         'interpretation_lock':'Source-authored graph only; no semantic target selection or numerical implementation is authorized.'}

def equation_bundle(path,t):
 reg=math_registry(t); by={lab:r for r in reg for lab in r['labels']}; rows=[]
 for lab in TARGET_LABELS:
  r=by.get(lab)
  if not r:
   rows.append({'label':lab,'present':False}); continue
  raw=r['raw']; refs=REF.findall(raw)
  # Compact exact math source retained for private/source reconstruction; artifact is not a scientific result.
  rows.append({'label':lab,'present':True,'environment':r['environment'],'line_start':r['line_start'],'line_end':r['line_end'],'section':r['section'],'hash':r['hash'],
               'references_inside':[x[1] for x in refs], 'normalized_math_source':re.sub(r'\s+',' ',raw).strip(),
               'operators':{'sum':raw.count('\\sum'),'prod':raw.count('\\prod'),'int':raw.count('\\int'),'gamma':raw.count('\\gamma'),
                            'booster_B':len(re.findall(r'B[_^{]',raw)),'amplitude_A_or_W':len(re.findall(r'(?<![A-Za-z])[AW][_^({]',raw))}})
 return {'test':'LORENTZIAN_EPRL_TWO_VERTEX_LABELLED_EQUATION_BUNDLE','root_path':str(path),'requested_label_count':len(TARGET_LABELS),
         'present_count':sum(bool(x.get('present')) for x in rows),'equations':rows,'classification':'LABELLED_EQUATION_BUNDLE_COMPLETE' if all(x.get('present') for x in rows) else 'LABELLED_EQUATION_BUNDLE_PARTIAL',
         'promotion_authorized':False,'interpretation_lock':'Exact source extraction only. No numerical output or source-lock promotion is implied.'}

def resource_manifest(source_dir,path,t):
 files=[]
 for f in sorted(Path(source_dir).rglob('*')):
  if f.is_file(): files.append({'path':str(f.relative_to(source_dir)),'suffix':f.suffix.lower(),'bytes':f.stat().st_size})
 urls=sorted(set(URL.findall(t)))
 # TeX href/url arguments can contain non-literal wrappers; keep compact raw arguments too.
 urlargs=sorted(set(re.findall(r'\\(?:url|href)\{([^}]+)\}',t)))
 code_hits=[]
 for pat in [r'code',r'Mathematica',r'Julia',r'Python',r'C\+\+',r'GitHub',r'numerical implementation',r'algorithm']:
  for m in re.finditer(pat,t,re.I): code_hits.append({'term':pat,'line':line_no(t,m.start()),'section':section_at(t,m.start())})
 ext_counts={}
 for x in files: ext_counts[x['suffix']]=ext_counts.get(x['suffix'],0)+1
 computational=[x for x in files if x['suffix'] in ('.py','.jl','.m','.nb','.cpp','.cc','.c','.h','.f','.f90','.ipynb','.sh')]
 return {'test':'LORENTZIAN_EPRL_TWO_VERTEX_RESOURCE_MANIFEST','root_path':str(path),'file_count':len(files),'extension_counts':ext_counts,
         'computational_file_count':len(computational),'computational_files':computational,'source_urls':urls,'tex_url_arguments':urlargs,'code_keyword_hits':code_hits,
         'classification':'SOURCE_RESOURCE_MANIFEST_COMPLETE','promotion_authorized':False,
         'interpretation_lock':'Resource/provenance diagnostic only; absence of code is BLOCKED/NOT_FOUND, never a physics failure.'}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--mode',required=True,choices=['label_graph','equation_bundle','resource_manifest']); ap.add_argument('--output',required=True); a=ap.parse_args()
 p,t,title=root(a.source_dir)
 if p is None:
  out={'test':'LORENTZIAN_EPRL_TWO_VERTEX_SOURCE_GRAPH_AUDIT','mode':a.mode,'valid':False,'classification':'PAPER_ROOT_AMBIGUOUS','promotion_authorized':False}
  Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2)); raise SystemExit(2)
 if a.mode=='label_graph': out=label_graph(p,t)
 elif a.mode=='equation_bundle': out=equation_bundle(p,t)
 else: out=resource_manifest(a.source_dir,p,t)
 out.update({'mode':a.mode,'valid':True,'root_title':title,'root_sha256':hashlib.sha256(t.encode()).hexdigest()})
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 small={k:v for k,v in out.items() if k not in ('nodes','edges','equations','code_keyword_hits')}
 print(json.dumps(small,indent=2,sort_keys=True))
if __name__=='__main__': main()
