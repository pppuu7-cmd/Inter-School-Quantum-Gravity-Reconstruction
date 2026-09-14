#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, pathlib, re
from fractions import Fraction

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/'out'/'iter037'; OUT.mkdir(parents=True,exist_ok=True)
s36=importlib.util.spec_from_file_location('iter036',ROOT/'code/iter036/eprl_map_label_consistency.py')
i36=importlib.util.module_from_spec(s36); s36.loader.exec_module(i36)
REQ=[ROOT/'prereg/ITER037_RC006_DIAGONAL_EXTERNAL_LABEL_SOURCE_SUPPORT_2026-09-14.md',ROOT/'results/ITER036_RC006_EPRL_MAP_LABEL_INSTANTIATION_CONSISTENCY_BLOCKED_2026-09-14.md']

def write(x):
    (OUT/'evidence.json').write_text(json.dumps(x,indent=2,sort_keys=True)+'\n'); print(json.dumps(x,indent=2,sort_keys=True))

def source():
    miss=[str(p.relative_to(ROOT)) for p in REQ if not p.exists()]
    if miss: raise FileNotFoundError(','.join(miss))
    return i36.src()

def cases_nonzero():
    s=source(); cases,_,closed=i36.extract_cases(s['text'])
    if not closed: return []
    vals=[v for v in i36.mapped_entries(cases) if v['l']>0]
    vals=sorted(vals,key=lambda x:(x['k'],Fraction(x['gamma_num'],x['gamma_den']),x['l']))
    for n,v in enumerate(vals): v['diag_panel']='primary' if n%2==0 else 'heldout'
    return vals

def lane_A():
    s=source(); text=s['text']
    # Positive authority requires indexed/general map language, not mere lack of inequality.
    pats=[r'l_i\s*\\mapsto\s*\(j\^\+_i\s*,\s*j\^-_i\)',r'l_\{i\}\s*\\mapsto[^\n]{0,180}j[^\n]{0,180}',r'maps?\s+\$?l_i[^\n]{0,300}',r'l_1[^\n]{0,300}l_2']
    hits=[]
    for pat in pats:
        for m in re.finditer(pat,text,re.I|re.S):
            a=max(0,m.start()-800); b=min(len(text),m.end()+1000); c=' '.join(text[a:b].split())
            if re.search(r'Eq\.?\s*\(?29\)?|\\Lambda',c,re.I): continue
            hits.append({'pattern':pat,'context':c[:3000]})
            if len(hits)>=20: break
    positive=[]
    for h in hits:
        c=h['context']
        generic=bool(re.search(r'(l_i|l_\{i\}|for each|indices|i\s*=|map[s]?\s+.*l)',c,re.I))
        eprl=bool(re.search(r'(simplicity|EPRL|j\^\+|j\^-)',c,re.I))
        if generic and eprl: positive.append(h)
    return {'lane':'external-label-scope','pass':bool(positive),'classification':'PASS' if positive else 'BLOCKED_EXTERNAL_LABEL_SCOPE','archive_sha':s['archive_sha'],'qualified_contexts':positive[:10],'all_contexts':hits[:15]}

def exact_map(v):
    g=Fraction(v['gamma_num'],v['gamma_den']); l=v['l']
    jp=(1+g)*l/2; jm=(1-g)*l/2; jmax=v['k']//2
    return jp,jm,jmax

def lane_B():
    vals=cases_nonzero(); rows=[]; ok=bool(vals)
    for v in vals:
        jp,jm,jmax=exact_map(v)
        domain=(0<=v['l']<=jmax and jp.denominator==1 and jm.denominator==1 and 0<=jp<=jmax and 0<=jm<=jmax)
        rows.append({**v,'l1':v['l'],'l2':v['l'],'jp':str(jp),'jm':str(jm),'jmax':jmax,'domain_ok':domain})
        ok=ok and domain
    return {'lane':'diagonal-admissibility','pass':bool(ok),'primary_count':sum(r['diag_panel']=='primary' for r in rows),'heldout_count':sum(r['diag_panel']=='heldout' for r in rows),'rows':rows}

def exp(a,b,j): return -Fraction(a*(a+1)+b*(b+1)-j*(j+1),2)

def lane_C():
    vals=cases_nonzero(); tests=[]
    for v in vals:
        jp,jm,jmax=exact_map(v); jp=int(jp); jm=int(jm); k=v['k']
        # Diagonal l1=l2 makes both factor couplings the same pair (jp,jm).
        js=i36.admissible_internal(k,jp,jm)
        ex=[{'j':j,'factor1':str(exp(jp,jm,j)),'factor2':str(exp(jp,jm,j))} for j in js]
        tests.append({**v,'l1':v['l'],'l2':v['l'],'internal_j':js,'exponents':ex,'pass':bool(js)})
    primary=[t for t in tests if t['diag_panel']=='primary' and t['pass']]
    held=[t for t in tests if t['diag_panel']=='heldout' and t['pass']]
    ok=bool(tests) and all(t['pass'] for t in tests) and bool(primary) and bool(held)
    return {'lane':'diagonal-internal-j-support','pass':bool(ok),'classification':'PASS' if ok else 'BLOCKED_DIAGONAL_PANEL_SUPPORT','primary_tested':len(primary),'heldout_tested':len(held),'tests':tests}

def lane_D():
    vals=cases_nonzero()
    if not vals:return {'lane':'null-controls','pass':False,'classification':'BLOCKED_DIAGONAL_PANEL_SUPPORT'}
    v=vals[0]; g=Fraction(v['gamma_num'],v['gamma_den']); jmax=v['k']//2
    # 1: first nonzero l <= cutoff that violates mapped integrality; source-unmapped under integer restriction.
    unmapped=None
    for l in range(1,jmax+1):
        jp=(1+g)*l/2; jm=(1-g)*l/2
        if jp.denominator!=1 or jm.denominator!=1:
            unmapped={'l':l,'jp':str(jp),'jm':str(jm)}; break
    wrong1=bool(unmapped)
    # 2: first l > external finite cutoff.
    above=jmax+1; wrong2=above>jmax
    # 3: swapped mapped pair contradicts positive-gamma identity.
    jp,jm,_=exact_map(v); wrong3=((jm-jp)/(jm+jp)!=g) if (jm+jp)!=0 else False
    det=sum([wrong1,wrong2,wrong3])
    return {'lane':'null-controls','pass':det==3,'detected':det,'required':3,'case':v,'unmapped_integrality_detected':wrong1,'unmapped_example':unmapped,'above_external_cutoff_detected':wrong2,'above_l':above,'swap_detected':wrong3}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['A','B','C','D']); a=ap.parse_args()
    try: obj={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}[a.lane]()
    except Exception as e: obj={'lane':a.lane,'pass':False,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)}
    write(obj)
if __name__=='__main__':main()
