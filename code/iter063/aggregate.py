#!/usr/bin/env python3
import glob,json,math,statistics,os
ALPHAS=[0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80]
CENTRAL={0.55,0.60,0.65,0.70}
NAMES=['P1','P2','H1','H2','H3','H4']

def load(name):
    p=glob.glob(f'artifacts/{name}.json')
    return json.load(open(p[0])) if p else None

def sample_map(d,power,kind):
    out={a:[] for a in ALPHAS}; ess={a:[] for a in ALPHAS}; fin={a:[] for a in ALPHAS}
    for row in d['rows']:
        if row['power']!=power: continue
        for r in row[kind]:
            a=round(float(r['alpha']),2); out[a].append(r['value']); ess[a].append(r['ess_fraction']); fin[a].append(r['finite_fraction'])
    return out,ess,fin

def summarize(d):
    c16,ce16,cf16=sample_map(d,16,'coarse'); f16,fe16,ff16=sample_map(d,16,'fine')
    c14,_,_=sample_map(d,14,'coarse'); f14,_,_=sample_map(d,14,'fine')
    checks=[]; per={}; diffs={}
    for a in ALPHAS:
        cv=lambda xs: statistics.stdev(xs)/max(abs(statistics.mean(xs)),1e-300) if len(xs)>1 else float('inf')
        rel=lambda x,y: abs(x-y)/max(abs(y),1e-300)
        cm=statistics.mean(c16[a]); fm=statistics.mean(f16[a]); ds=[f16[a][i]-c16[a][i] for i in range(3)]
        dm=statistics.mean(ds); se=statistics.stdev(ds)/math.sqrt(len(ds))
        chk={'finite':all(x==1.0 for x in cf16[a]+ff16[a]),'coarse_ess':statistics.median(ce16[a])>=1e-4,'fine_ess':statistics.median(fe16[a])>=1e-4,'coarse_cv':cv(c16[a])<=0.15,'fine_cv':cv(f16[a])<=0.15,'coarse_level':rel(statistics.mean(c14[a]),cm)<=0.20,'fine_level':rel(statistics.mean(f14[a]),fm)<=0.20}
        if a in CENTRAL: checks.extend(chk.values())
        per[str(a)]={'difference':dm,'difference_stderr':se,'coarse_mean':cm,'fine_mean':fm,'checks':chk,'coarse_ess_median':statistics.median(ce16[a]),'fine_ess_median':statistics.median(fe16[a]),'coarse_cv':cv(c16[a]),'fine_cv':cv(f16[a])}
        diffs[a]=(dm,se)
    crossings=[]
    for a0,a1 in zip(ALPHAS[:-1],ALPHAS[1:]):
        d0,s0=diffs[a0]; d1,s1=diffs[a1]
        if (d0==0 or d1==0 or d0*d1<0) and abs(d0)>s0 and abs(d1)>s1:
            root=a0+(a1-a0)*(-d0)/(d1-d0) if d1!=d0 else (a0+a1)/2
            crossings.append({'bracket':[a0,a1],'linear_report_only':root,'both_endpoint_signs_resolved':True})
    return {'converged':all(checks),'robust_crossing':bool(crossings),'crossings':crossings,'per_alpha':per}

cal=load('calibration'); raw={n:load(n) for n in NAMES}; missing=[n for n,v in [('calibration',cal),*raw.items()] if v is None]
summaries={n:summarize(v) for n,v in raw.items() if v is not None}
if missing:
    classification='INFRASTRUCTURE_FAIL_PRE_SCIENCE'; scientific_pass=False
elif not cal.get('pass',False):
    classification='INVALID_IMPLEMENTATION_CALIBRATION'; scientific_pass=False
else:
    parent=(0.50,0.55)
    def sym_ok(n):
        s=summaries[n]
        if not (s['converged'] and s['robust_crossing']): return False
        for c in s['crossings']:
            a,b=c['bracket']
            if not (b < 0.45 or a > 0.60): return True
        return False
    if not (sym_ok('P1') and sym_ok('P2')):
        classification='INVALID_IMPLEMENTATION_OR_SELECTOR_SYMMETRY_FAIL'; scientific_pass=False
    else:
        hc=[n for n in ['H1','H2','H3','H4'] if summaries[n]['converged']]
        hx=[n for n in hc if summaries[n]['robust_crossing']]
        if len(hc)<3:
            classification='NUMERICAL_FAIL_HELDOUT_PANEL_CONVERGENCE_NOT_ESTABLISHED'; scientific_pass=False
        elif len(hx)>=2:
            classification='SCIENTIFIC_PASS_RC008_HELDOUT_TRANSPORT_SCOPED'; scientific_pass=True
        else:
            classification='SCIENTIFIC_FAIL_RC008_HELDOUT_TRANSPORT_NOT_ROBUST'; scientific_pass=False
out={'classification':classification,'scientific_pass':scientific_pass,'missing':missing,'calibration':cal,'boundaries':summaries,'claim_locks':{'bridge_credit':False,'candidate_theory':'UNFORMED','full_eprl_refinement':False,'lorentzian_refinement':False,'new_physics':False}}
os.makedirs('aggregate',exist_ok=True); open('aggregate/summary.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'classification':classification,'scientific_pass':scientific_pass,'summary':{k:{'converged':v['converged'],'robust_crossing':v['robust_crossing'],'crossings':v['crossings']} for k,v in summaries.items()}},indent=2))
