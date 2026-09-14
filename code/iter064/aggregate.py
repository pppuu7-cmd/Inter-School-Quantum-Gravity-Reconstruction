#!/usr/bin/env python3
import glob,json,math,statistics,os
ALPHAS=[0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80]; CENTRAL={0.55,0.60,0.65,0.70}; NAMES=['B2','P1','P2']
def load(n):
 p=glob.glob(f'artifacts/{n}.json'); return json.load(open(p[0])) if p else None
def vals(d,power,kind,a,key='value'):
 out=[]
 for row in d['rows']:
  if row['power']!=power: continue
  for r in row[kind]:
   if round(float(r['alpha']),2)==a: out.append(r[key])
 return out
def summarize(d):
 per={}; conv=[]; diffs={}
 for a in ALPHAS:
  c18=vals(d,18,'coarse',a); f18=vals(d,18,'fine',a); c16=vals(d,16,'coarse',a); f16=vals(d,16,'fine',a)
  ce=vals(d,18,'coarse',a,'ess_fraction'); fe=vals(d,18,'fine',a,'ess_fraction'); cf=vals(d,18,'coarse',a,'finite_fraction'); ff=vals(d,18,'fine',a,'finite_fraction')
  cv=lambda x: statistics.stdev(x)/max(abs(statistics.mean(x)),1e-300)
  rel=lambda x,y: abs(x-y)/max(abs(y),1e-300)
  cm,fm=statistics.mean(c18),statistics.mean(f18); ds=[f18[i]-c18[i] for i in range(len(c18))]; dm=statistics.mean(ds); se=statistics.stdev(ds)/math.sqrt(len(ds))
  chk={'finite':all(x==1.0 for x in cf+ff),'coarse_ess':statistics.median(ce)>=1e-4,'fine_ess':statistics.median(fe)>=1e-4,'coarse_cv':cv(c18)<=0.15,'fine_cv':cv(f18)<=0.15,'coarse_level':rel(statistics.mean(c16),cm)<=0.15,'fine_level':rel(statistics.mean(f16),fm)<=0.15}
  if a in CENTRAL: conv.extend(chk.values())
  per[str(a)]={'difference':dm,'stderr':se,'checks':chk}; diffs[a]=(dm,se)
 crossings=[]
 for a0,a1 in zip(ALPHAS[:-1],ALPHAS[1:]):
  d0,s0=diffs[a0]; d1,s1=diffs[a1]
  if d0*d1<0 and abs(d0)>s0 and abs(d1)>s1: crossings.append([a0,a1])
 return {'converged':all(conv),'crossings':crossings,'robust_crossing':bool(crossings),'per_alpha':per}
raw={n:load(n) for n in NAMES}; missing=[n for n,v in raw.items() if v is None]; s={n:summarize(v) for n,v in raw.items() if v}
if missing: cls='INFRASTRUCTURE_FAIL_PRE_SCIENCE'
elif not all(v['converged'] for v in s.values()): cls='NUMERICAL_UNRESOLVED_PERMUTATION_SEED_DIAGNOSTIC'
else:
 crosses=[s[n]['robust_crossing'] for n in NAMES]
 if all(crosses): cls='DIAGNOSTIC_PASS_PERMUTATION_CROSSING_STABLE'
 elif crosses[0] and (not crosses[1] or not crosses[2]): cls='DIAGNOSTIC_FAIL_INTEGRATED_PERMUTATION_MISMATCH'
 elif not any(crosses): cls='DIAGNOSTIC_PARENT_B2_CROSSING_NOT_SEED_STABLE'
 else: cls='DIAGNOSTIC_MIXED_SEED_TRANSPORT_UNRESOLVED'
out={'classification':cls,'missing':missing,'boundaries':s,'claim_locks':{'bridge_credit':False,'candidate_theory':'UNFORMED','scientific_gate_credit':False}}
os.makedirs('aggregate',exist_ok=True); open('aggregate/summary.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({'classification':cls,'summary':{k:{'converged':v['converged'],'crossings':v['crossings']} for k,v in s.items()}},indent=2))
