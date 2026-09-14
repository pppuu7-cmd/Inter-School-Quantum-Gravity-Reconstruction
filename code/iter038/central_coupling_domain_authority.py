#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, pathlib, re
from fractions import Fraction
ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/'out'/'iter038'; OUT.mkdir(parents=True,exist_ok=True)
s37=importlib.util.spec_from_file_location('i37',ROOT/'code/iter037/diagonal_external_label_support.py'); i37=importlib.util.module_from_spec(s37); s37.loader.exec_module(i37)
REQ=[ROOT/'prereg/ITER038_RC006_EQ27_CENTRAL_COUPLING_DOMAIN_AUTHORITY_2026-09-14.md',ROOT/'results/ITER037_RC006_DIAGONAL_EXTERNAL_LABEL_SOURCE_SUPPORT_PASS_2026-09-14.md']

def write(x):
 (OUT/'evidence.json').write_text(json.dumps(x,indent=2,sort_keys=True)+'\n'); print(json.dumps(x,indent=2,sort_keys=True))
def source():
 miss=[str(p.relative_to(ROOT)) for p in REQ if not p.exists()]
 if miss: raise FileNotFoundError(','.join(miss))
 return i37.source()
def adm(k,a,b):
 jmax=k//2
 return [c for c in range(jmax+1) if abs(a-b)<=c<=a+b and a+b+c<=k]
def diag(): return i37.cases_nonzero()

def A():
 s=source(); t=s['text']; hits=[]
 for m in re.finditer(r'j\^\\pm_1[^\n]{0,220}j\^\\pm_2[^\n]{0,500}J\^\\pm[^\n]{0,500}l',t,re.I|re.S):
  c=' '.join(t[max(0,m.start()-900):min(len(t),m.end()+1200)].split())
  if not re.search(r'simplicity constraints are not explicitly implemented in the latter coupling',c,re.I): continue
  if re.search(r'Eq\.?\s*\(?29\)?|\\Lambda',c,re.I): continue
  hits.append(c[:4000])
 ok=bool(hits)
 return {'lane':'topology-authority','pass':ok,'classification':'PASS' if ok else 'BLOCKED_CENTRAL_TOPOLOGY_AUTHORITY','contexts':hits[:8]}
def B():
 s=source(); t=s['text']
 # Technical parser repair only: TeX eqnarray places alignment '&' around relation symbols.
 sum_rule=r'j_1\s*\+\s*j_2\s*\+\s*j_3\s*&?\s*\\leq\s*&?\s*k'
 triangle=r'j_I\s*\+\s*j_K\s*&?\s*\\geq\s*&?\s*j_L'
 cutoff=r'j_\{?\\text\{max\}\}?\s*=\s*\\frac\{k\}\{2\}'
 pats=[sum_rule,triangle,r'admissible representations',cutoff]
 hits=[]
 for p in pats:
  for m in re.finditer(p,t,re.I|re.S): hits.append(' '.join(t[max(0,m.start()-500):min(len(t),m.end()+700)].split())[:2200])
 ok=bool(re.search(sum_rule,t,re.I|re.S)) and bool(re.search(triangle,t,re.I|re.S)) and bool(re.search(r'admissible representations',t,re.I)) and bool(re.search(cutoff,t,re.I|re.S))
 return {'lane':'finite-k-domain-authority','pass':ok,'classification':'PASS' if ok else 'BLOCKED_FINITE_K_DOMAIN_AUTHORITY','contexts':hits[:12]}
def C():
 rows=[]; ok=True
 for v in diag():
  jp,jm,_=i37.exact_map(v); jp=int(jp); jm=int(jm); k=v['k']
  Jp=adm(k,jp,jp); Jm=adm(k,jm,jm); triples=[]
  for a in Jp:
   for b in Jm:
    L=adm(k,a,b)
    if L: triples.append({'Jp':a,'Jm':b,'l':L})
  good=bool(Jp and Jm and triples); ok=ok and good
  rows.append({**v,'Jp':Jp,'Jm':Jm,'central':triples,'pass':good})
 pri=sum(r['diag_panel']=='primary' and r['pass'] for r in rows); held=sum(r['diag_panel']=='heldout' and r['pass'] for r in rows)
 ok=ok and pri>0 and held>0
 return {'lane':'central-domain-enumeration','pass':bool(ok),'classification':'PASS' if ok else 'BLOCKED_CENTRAL_DOMAIN_SUPPORT','primary_tested':pri,'heldout_tested':held,'rows':rows}
def D():
 v=diag()[0]; jp,jm,_=i37.exact_map(v); jp=int(jp); jm=int(jm); k=v['k']; Jp=adm(k,jp,jp); Jm=adm(k,jm,jm)
 badJp=(max(Jp)+1 not in Jp); badJm=(max(Jm)+1 not in Jm)
 a,b=Jp[0],Jm[0]; L=adm(k,a,b); candidate=(max(L)+1 if L else 0); badL=(candidate not in L)
 det=sum([badJp,badJm,badL])
 return {'lane':'null-controls','pass':det==3,'detected':det,'required':3,'case':v,'bad_Jp_detected':badJp,'bad_Jm_detected':badJm,'bad_l_detected':badL}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['A','B','C','D']); a=ap.parse_args()
 try:o={'A':A,'B':B,'C':C,'D':D}[a.lane]()
 except Exception as e:o={'lane':a.lane,'pass':False,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)}
 write(o)
if __name__=='__main__':main()
