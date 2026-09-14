#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, pathlib, sys, numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[2]; OUT=ROOT/'out'/'iter040'; OUT.mkdir(parents=True,exist_ok=True)
def load(name,p): s=importlib.util.spec_from_file_location(name,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
i39=load('i39',ROOT/'code/iter039/bounded_central_component_closure.py')
PRIOR={(1,1),(2,1),(2,2),(4,2)}

def write(x): (OUT/'evidence.json').write_text(json.dumps(x,indent=2,sort_keys=True)+'\n'); print(json.dumps(x,indent=2,sort_keys=True))
def rows(panel=None):
 out=[]
 for x in i39.cases():
  if panel and x['case']['diag_panel']!=panel: continue
  for Jp,Jm,l in x['central']:
   r=i39.eval_tuple(x['case']['k'],Jp,Jm,l); a,b,c=r['twice'];
   r.update({'k':x['case']['k'],'panel':x['case']['diag_panel'],'prior_iter027_pair_scope':(a,b) in PRIOR,'root_tensor_boundary':a+b>x['case']['k']}); out.append(r)
 return out
def A():
 rs=rows(); pri=sum(r['panel']=='primary' for r in rs); held=sum(r['panel']=='heldout' for r in rs)
 write({'lane':'scope-census','tuple_count':len(rs),'primary':pri,'heldout':held,'prior_scope':sum(r['prior_iter027_pair_scope'] for r in rs),'root_boundary':sum(r['root_tensor_boundary'] for r in rs),'pass':bool(pri and held)})
def mapped(panel):
 rs=rows(panel); groups={}
 for r in rs:
  key=f"prior={int(r['prior_iter027_pair_scope'])};root={int(r['root_tensor_boundary'])}"; g=groups.setdefault(key,{'n':0,'fail':0,'max_R_inverse':0.0,'max_dual':0.0}); g['n']+=1; g['fail']+=int(not r['pass']); g['max_R_inverse']=max(g['max_R_inverse'],r['R_inverse']); g['max_dual']=max(g['max_dual'],r['dual'])
 write({'lane':panel+'-boundary-map','panel':panel,'tuple_count':len(rs),'failure_count':sum(not r['pass'] for r in rs),'groups':groups,'thresholds':i39.TH,'pass':bool(rs and sum(g['n'] for g in groups.values())==len(rs))})
def D():
 rs=rows(); classes={}
 for r in rs:
  key=(r['prior_iter027_pair_scope'],r['root_tensor_boundary'])
  classes.setdefault(key,r)
 out=[]
 for key,r in sorted(classes.items(),key=lambda kv:str(kv[0])):
  a,b,c=r['twice']; k=r['k']; swapped=None
  if i39.qcg.admissible(b,a,c,k):
   R=i39.db.Rmap(b,a,k); Ri=i39.db.Rmap(a,b,k,True); swapped=float(np.max(np.abs(Ri@R-np.eye((a+1)*(b+1)))))
  out.append({'class':list(key),'tuple':[k,r['Jp'],r['Jm'],r['l']],'identity':r['identity'],'dual':r['dual'],'R_inverse':r['R_inverse'],'swapped_R_inverse':swapped})
 # frozen ITER039 negative-control tuple
 k,Jp,Jm,l=6,1,2,1; a,b,c=2*Jp,2*Jm,2*l; good,_=i39.ds.cbar_source(a,b,c,k); legacy=i39.db.swap_ba_to_ab(a,b)@i39.db.solve_bar(b,a,c,k)[0]; diff=float(np.max(np.abs(good-legacy)))
 write({'lane':'orientation-reproduction','classes':out,'frozen_null_qbar_difference':diff,'pass':bool(out and diff>1e-6)})
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['A','B','C','D']); a=ap.parse_args()
 try: {'A':A,'B':lambda:mapped('primary'),'C':lambda:mapped('heldout'),'D':D}[a.lane]()
 except Exception as e: write({'lane':a.lane,'pass':False,'infrastructure_failure':True,'error':repr(e)})
if __name__=='__main__': main()
