#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, pathlib, re
ROOT=pathlib.Path(__file__).resolve().parents[2]; OUT=ROOT/'out'/'iter041'; OUT.mkdir(parents=True,exist_ok=True)
spec=importlib.util.spec_from_file_location('i25',ROOT/'code/iter025/exact_authority_audit.py'); i25=importlib.util.module_from_spec(spec); spec.loader.exec_module(i25)
EXPECTED={'target':'3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee','qspinnet':'69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0','wojtek':'d6804794d3f4589f77a2e11d2a143c1125a900160e0c632ed3b3e471598af3f7'}

def write(x): (OUT/'evidence.json').write_text(json.dumps(x,indent=2,sort_keys=True)+'\n'); print(json.dumps(x,indent=2,sort_keys=True))
def acquire_all(): return {n:i25.acquire(n) for n in ('target','qspinnet','wojtek')}
def contexts(srcs,patterns,keys):
 out=[]
 for key in keys:
  out.extend(i25.collect_hits(srcs[key],patterns,radius=18,limit=100))
 return out[:180]
def A():
 s=acquire_all(); rows={n:{'arxiv':v['arxiv'],'sha256':v['archive_sha256'],'expected':EXPECTED[n],'hash_match':v['archive_sha256']==EXPECTED[n],'files':sorted(v['files'])} for n,v in s.items()}; write({'lane':'provenance','sources':rows,'pass':all(x['hash_match'] for x in rows.values())})
def B():
 s=acquire_all(); pats=[('root_of_unity',r'root.{0,20}unity'),('cutoff',r'(?:cut.?off|j_\{?max\}?|jmax)'),('admissible',r'admissib'),('fusion',r'fusion'),('truncat',r'truncat'),('tensor_product',r'tensor.{0,30}product|\\otimes'),('quotient',r'quotient'),('negligible',r'negligib'),('R',r'\\mathcal\s*\{R\}|R[- ]matrix|crossing'),('sum_condition',r'j_?1.{0,80}j_?2.{0,80}j_?3.{0,100}(?:\\leq|less|k)')]; hits=contexts(s,pats,('target','qspinnet','wojtek')); write({'lane':'R-domain-authority','classification':'EVIDENCE_REQUIRES_STRICT_SOURCE_VERDICT','hit_count':len(hits),'hits':hits,'pass':True})
def C():
 s=acquire_all(); pats=[('cup_cap',r'\\(?:cup|cap)|\bcup\b|\bcap\b'),('dual',r'\bdual\b'),('quantum_trace',r'quantum.{0,30}trace|q[- ]trace'),('trace',r'\btrace\b'),('negligible',r'negligib'),('quotient',r'quotient'),('physical',r'physical.{0,50}(?:represent|space|channel)'),('normalization',r'normaliz'),('identity',r'identit'),('bar_q',r'\\bar\s*\{?q\}?')]; hits=contexts(s,pats,('target','qspinnet')); write({'lane':'dual-domain-authority','classification':'EVIDENCE_REQUIRES_STRICT_SOURCE_VERDICT','hit_count':len(hits),'hits':hits,'pass':True})
def D():
 s=acquire_all(); r=i25.collect_hits(s['target'],[('R',r'\\mathcal\s*\{R\}')],radius=10,limit=20); q=i25.collect_hits(s['qspinnet'],[('qbar',r'\{\}_\{\\bar q\}|\\bar q')],radius=10,limit=20); fake='SYNTHETIC_QUOTIENT_AUTHORITY_DO_NOT_MATCH'; concat='\n'.join('\n'.join(v['files'].values()) for v in s.values()); write({'lane':'controls','R_positive_hits':len(r),'qbar_positive_hits':len(q),'synthetic_absent':fake not in concat,'bibliography_only_is_not_authority':True,'lexical_only_is_not_authority':True,'pass':bool(r and q and fake not in concat)})
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['A','B','C','D']); a=ap.parse_args()
 try: {'A':A,'B':B,'C':C,'D':D}[a.lane]()
 except Exception as e: write({'lane':a.lane,'pass':False,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)})
if __name__=='__main__': main()
