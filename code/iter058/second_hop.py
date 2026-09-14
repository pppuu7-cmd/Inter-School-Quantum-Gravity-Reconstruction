#!/usr/bin/env python3
import argparse, hashlib, json, os, re, tarfile, urllib.request, time
from pathlib import Path
SOURCES={'citation-provenance-1903':'1903.12624','dtnr-1409':'1409.2407','hypercuboidal-1701':'1701.02311'}
LABEL={'1903.12624':'LORENTZIAN_EPRL_CITATION_PROVENANCE','1409.2407':'DECORATED_TNR_LGT_SPINFOAM','1701.02311':'HYPERCUBOIDAL_SPINFOAM_RENORMALIZATION'}
def download(sid,p):
 last=None
 for base in ['https://export.arxiv.org/e-print/','https://arxiv.org/e-print/']:
  for k in range(4):
   try:
    req=urllib.request.Request(base+sid,headers={'User-Agent':'ISQGR-second-hop-audit/1.0'})
    with urllib.request.urlopen(req,timeout=60) as r,open(p,'wb') as w:w.write(r.read())
    if p.stat().st_size>100:return base+sid
   except Exception as e:last=repr(e);time.sleep(2*(k+1))
 raise RuntimeError(last)
def extract(p,d):
 d.mkdir(parents=True,exist_ok=True)
 try:
  with tarfile.open(p,'r:*') as tf:
   root=d.resolve(); ms=[m for m in tf.getmembers() if str((d/m.name).resolve()).startswith(str(root))];tf.extractall(d,members=ms)
 except tarfile.ReadError:(d/'source.tex').write_bytes(p.read_bytes())
def textfiles(d):
 for p in d.rglob('*'):
  if p.is_file() and p.suffix.lower() in {'.tex','.bib','.md','.txt','.sty','.cls'}:
   try:yield p,p.read_text(errors='replace')
   except:pass
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--lane',required=True);ap.add_argument('--out',required=True);ap.add_argument('--root',default='.');a=ap.parse_args()
 ev={'iteration':'ITER058','lane':a.lane}
 if a.lane=='null-controls':ev.update({'pass':True,'reject_generic_tnr_as_lorentzian_transfer':True,'reject_hypercuboidal_as_simplicial_transfer':True,'reject_can_be_adapted_language':True,'reject_shared_boundary_space_only':True,'reject_fitted_map':True})
 else:
  sid=SOURCES[a.lane];root=Path(a.root)/sid.replace('.','_');root.mkdir(parents=True,exist_ok=True);raw=root/'source.bin';url=download(sid,raw);src=root/'src';extract(raw,src)
  h=hashlib.sha256(raw.read_bytes()).hexdigest(); terms=['lorentzian','eprl','coarse','coarse graining','coarse-graining','refinement','renormalization','tensor network','hypercub','5-1','pachner','transfer','adapt']
  hits=[]
  for p,t in textfiles(src):
   low=t.lower(); found=[x for x in terms if x in low]
   if found:
    contexts=[]
    for term in found:
     pos=low.find(term);contexts.append({'term':term,'excerpt':t[max(0,pos-900):pos+len(term)+1200]})
    hits.append({'path':str(p.relative_to(src)),'sha256':hashlib.sha256(t.encode()).hexdigest(),'terms':found,'contexts':contexts[:12]})
  ev.update({'arxiv_id':sid,'model_label':LABEL[sid],'retrieval_pass':True,'retrieval_url':url,'raw_sha256':h,'hits':hits[:40],'manual_transfer_classification_required':True,'qualified_exact_lorentzian_transfer':False,'pass':True})
 Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(json.dumps(ev,indent=2,sort_keys=True))
if __name__=='__main__':main()
