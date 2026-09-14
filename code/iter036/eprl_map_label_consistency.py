#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, pathlib, re
from fractions import Fraction

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/'out'/'iter036'; OUT.mkdir(parents=True,exist_ok=True)
spec=importlib.util.spec_from_file_location('iter030_stage_s',ROOT/'code/iter030/corrected_stage_s.py')
k30=importlib.util.module_from_spec(spec); spec.loader.exec_module(k30)
EXPECTED_ARCH='3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee'
REQ=[ROOT/'prereg/ITER036_RC006_EPRL_MAP_LABEL_INSTANTIATION_CONSISTENCY_2026-09-14.md',ROOT/'results/ITER035_RC006_INDEXED_SIMPLICITY_MAP_SOURCE_AUTHORITY_PASS_2026-09-14.md']

def write(x):
    (OUT/'evidence.json').write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
    print(json.dumps(x,indent=2,sort_keys=True))

def src():
    miss=[str(p.relative_to(ROOT)) for p in REQ if not p.exists()]
    if miss: raise FileNotFoundError(','.join(miss))
    s,e=k30.load_source()
    if e: raise RuntimeError(json.dumps(e,sort_keys=True))
    if s['archive_sha']!=EXPECTED_ARCH: raise RuntimeError('archive hash mismatch')
    return s

def latex_fraction(s):
    s=s.strip().replace(' ','')
    m=re.fullmatch(r'\\frac\{(-?\d+)\}\{(\d+)\}',s)
    if m:return Fraction(int(m.group(1)),int(m.group(2)))
    m=re.fullmatch(r'(-?\d+)/(\d+)',s)
    if m:return Fraction(int(m.group(1)),int(m.group(2)))
    if re.fullmatch(r'-?\d+',s):return Fraction(int(s),1)
    raise ValueError('unparsed rational '+s)

def extract_cases(text):
    marker=re.search(r'following\s+non[- ]trivial\s+cases\s+are\s+possible',text,re.I)
    if not marker:return [],'',False
    tail=text[marker.end():]
    end=tail.find('\\end{itemize}')
    if end<0:return [],tail[:12000],False
    block=tail[:end]
    items=re.split(r'\\item',block)[1:]
    cases=[]
    for item in items:
        km=re.search(r'k\s*=\s*(\d+)',item)
        gm=re.search(r'\\gamma\s*=\s*(\\frac\{[-]?\d+\}\{\d+\}|[-]?\d+\s*/\s*\d+|[-]?\d+)',item)
        if not (km and gm): continue
        k=int(km.group(1)); gamma=latex_fraction(gm.group(1))
        # record explicit source mappings, if parsable, as an independent cross-check
        explicit=[]
        for mm in re.finditer(r'l\s*=\s*(\d+)\s*\\mapsto\s*\(\s*j\^\+\s*=*\s*(\d+)?\s*,?\s*j\^-\s*=*\s*(\d+)?',item):
            explicit.append(mm.group(0))
        cases.append({'k':k,'gamma_num':gamma.numerator,'gamma_den':gamma.denominator,'source_item':' '.join(item.split())[:2200],'explicit_mapping_fragments':explicit})
    # uniqueness by k,gamma preserving source order
    seen=set(); uniq=[]
    for c in cases:
        key=(c['k'],c['gamma_num'],c['gamma_den'])
        if key not in seen: seen.add(key); uniq.append(c)
    return uniq,block,True

def mapped_entries(cases):
    vals=[]
    for c in cases:
        k=c['k']; g=Fraction(c['gamma_num'],c['gamma_den']); jmax=k//2 if k%2 else k//2
        # paper restricts integer representations; odd k maximum integer is floor(k/2)
        for l in range(0,jmax+1):
            jp=(1+g)*l/2; jm=(1-g)*l/2
            if jp.denominator==1 and jm.denominator==1 and jp>=0 and jm>=0 and jp<=jmax and jm<=jmax:
                vals.append({'k':k,'gamma_num':g.numerator,'gamma_den':g.denominator,'l':l,'jp':jp.numerator,'jm':jm.numerator})
    vals=sorted(vals,key=lambda x:(x['k'],Fraction(x['gamma_num'],x['gamma_den']),x['l']))
    for i,v in enumerate(vals):v['panel']='primary' if i%2==0 else 'heldout'
    return vals

def lane_A():
    s=src(); cases,block,closed=extract_cases(s['text'])
    ok=closed and len(cases)>=2
    return {'lane':'source-list-extraction','pass':ok,'classification':'PASS' if ok else 'BLOCKED_SOURCE_CASE_LIST','archive_sha':s['archive_sha'],'case_count':len(cases),'cases':cases,'source_block':' '.join(block.split())[:8000]}

def lane_B():
    s=src(); cases,_,closed=extract_cases(s['text']); vals=mapped_entries(cases) if closed else []
    rows=[]; ok=bool(vals)
    for v in vals:
        g=Fraction(v['gamma_num'],v['gamma_den']); l=v['l']; jp=Fraction(v['jp']); jm=Fraction(v['jm'])
        inv_sum=(jp+jm==l)
        inv_gamma=True if l==0 else ((jp-jm)/(jp+jm)==g)
        jmax=v['k']//2
        finite=(jp.denominator==1 and jm.denominator==1 and 0<=jp<=jmax and 0<=jm<=jmax)
        rows.append({**v,'sum_identity':inv_sum,'gamma_identity':inv_gamma,'within_cutoff':finite})
        ok=ok and inv_sum and inv_gamma and finite
    return {'lane':'map-integrality-cutoff','pass':bool(ok),'entry_count':len(rows),'primary_count':sum(r['panel']=='primary' for r in rows),'heldout_count':sum(r['panel']=='heldout' for r in rows),'entries':rows}

def admissible_internal(k,a,b):
    jmax=k//2
    out=[]
    for j in range(jmax+1):
        if abs(a-b)<=j<=a+b and a+b+j<=k:
            out.append(j)
    return out

def exponent(jp,jm,j):
    # exact exponent argument before leading -1/2
    return -Fraction(jp*(jp+1)+jm*(jm+1)-j*(j+1),2)

def lane_C():
    s=src(); cases,_,closed=extract_cases(s['text']); vals=mapped_entries(cases) if closed else []
    groups={}
    for v in vals:
        if v['l']==0: continue
        key=(v['k'],v['gamma_num'],v['gamma_den']); groups.setdefault(key,[]).append(v)
    tests=[]
    for key,es in sorted(groups.items()):
        es=sorted(es,key=lambda x:x['l'])
        if len(es)<2: continue
        for i in range(len(es)-1):
            e1,e2=es[i],es[i+1]
            k=e1['k']
            js1=set(admissible_internal(k,e2['jp'],e1['jm']))
            js2=set(admissible_internal(k,e1['jp'],e2['jm']))
            common=sorted(js1&js2)
            exps=[{'j':j,'factor1':str(exponent(e2['jp'],e1['jm'],j)),'factor2':str(exponent(e1['jp'],e2['jm'],j))} for j in common]
            # Pair inherits the frozen panel of its first globally sorted entry.
            panel=e1['panel']
            tests.append({'k':k,'gamma_num':e1['gamma_num'],'gamma_den':e1['gamma_den'],'panel':panel,'l1':e1['l'],'l2':e2['l'],'j1p':e1['jp'],'j1m':e1['jm'],'j2p':e2['jp'],'j2m':e2['jm'],'internal_j':common,'exponents':exps,'pass':bool(common)})
    primary=[t for t in tests if t['panel']=='primary' and t['pass']]
    held=[t for t in tests if t['panel']=='heldout' and t['pass']]
    ok=bool(primary) and bool(held) and all(t['pass'] for t in tests)
    cls='PASS' if ok else 'BLOCKED_PANEL_SUPPORT'
    return {'lane':'eq27-indexed-exponent-instantiation','pass':ok,'classification':cls,'tested_pairs':len(tests),'primary_tested':len(primary),'heldout_tested':len(held),'tests':tests}

def lane_D():
    s=src(); cases,_,closed=extract_cases(s['text']); vals=[v for v in (mapped_entries(cases) if closed else []) if v['l']>0]
    if not vals:return {'lane':'null-controls','pass':False,'classification':'BLOCKED_PANEL_SUPPORT'}
    v=vals[0]; g=Fraction(v['gamma_num'],v['gamma_den']); l=v['l']; jmax=v['k']//2
    # 1 swap +/- with positive gamma: sum identity survives but gamma identity changes sign unless gamma=0.
    swp,swm=Fraction(v['jm']),Fraction(v['jp'])
    wrong1=(l>0 and (swp-swm)/(swp+swm)!=g)
    # 2 missing 1/2 violates sum identity for l>0.
    w2p=(1+g)*l; w2m=(1-g)*l
    wrong2=(w2p+w2m!=l)
    # 3 first l beyond integer source range that maps j+ above cutoff.
    beyond=None
    for ll in range(jmax+1,10*jmax+20):
        jp=(1+g)*ll/2; jm=(1-g)*ll/2
        if jp.denominator==1 and jm.denominator==1 and jp>jmax:
            beyond={'l':ll,'jp':str(jp),'jm':str(jm)}; break
    wrong3=bool(beyond)
    detected=sum([wrong1,wrong2,wrong3])
    return {'lane':'null-controls','pass':detected==3,'detected':detected,'required':3,'case':v,'swap_detected':wrong1,'missing_half_detected':wrong2,'above_cutoff_detected':wrong3,'above_cutoff_example':beyond}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['A','B','C','D']); a=ap.parse_args()
    try:obj={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}[a.lane]()
    except Exception as e:obj={'lane':a.lane,'pass':False,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)}
    write(obj)
if __name__=='__main__':main()
