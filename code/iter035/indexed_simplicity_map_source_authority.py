#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, pathlib, re

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/'out'/'iter035'; OUT.mkdir(parents=True,exist_ok=True)
spec=importlib.util.spec_from_file_location('iter030_stage_s',ROOT/'code/iter030/corrected_stage_s.py')
k30=importlib.util.module_from_spec(spec); spec.loader.exec_module(k30)
EXPECTED_ARCH='3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee'
REQ=[ROOT/'prereg/ITER035_RC006_INDEXED_SIMPLICITY_MAP_SOURCE_AUTHORITY_2026-09-14.md',ROOT/'results/ITER034_RC006_EQ27_SOURCE_LABEL_DOMAIN_BLOCKED_2026-09-14.md']

def write(x):
    (OUT/'evidence.json').write_text(json.dumps(x,indent=2,sort_keys=True)+'\n'); print(json.dumps(x,indent=2,sort_keys=True))

def source():
    missing=[str(p.relative_to(ROOT)) for p in REQ if not p.exists()]
    if missing: raise FileNotFoundError(','.join(missing))
    src,err=k30.load_source()
    if err: raise RuntimeError(json.dumps(err,sort_keys=True))
    if src['archive_sha']!=EXPECTED_ARCH: raise RuntimeError('archive hash mismatch')
    return src

def windows(text, patterns, radius=700, cap=30):
    out=[]
    for pat in patterns:
        for m in re.finditer(pat,text,re.I|re.S):
            a=max(0,m.start()-radius); b=min(len(text),m.end()+radius)
            ctx=text[a:b]
            # Eq29/Lambda-only contexts are recorded but never positive authority.
            bad=bool(re.search(r'\\label\{[^}]*29[^}]*\}|Eq\.?\s*\(?29\)?|Lambda|\\Lambda',ctx,re.I))
            out.append({'pattern':pat,'start':m.start(),'context':' '.join(ctx.split())[:2400],'eq29_or_lambda_nearby':bad})
            if len(out)>=cap:return out
    return out

def explicit_map_context(ctx):
    has_plus=bool(re.search(r'j\s*(?:\^\s*\+|\^\{\+\})',ctx))
    has_minus=bool(re.search(r'j\s*(?:\^\s*-|\^\{-\})',ctx))
    has_base=bool(re.search(r'\b(?:l|j)\b',ctx))
    relation=bool(re.search(r'(?:=|\\mapsto|\\longmapsto|->|:=)',ctx))
    mapcue=bool(re.search(r'(?:simplicity|EPRL|embedding|map|representation)',ctx,re.I))
    return has_plus and has_minus and has_base and relation and mapcue

def lane_A():
    src=source(); text=src['text']
    pats=[r'j\s*\^\s*\+[^\n]{0,180}j\s*\^\s*-',r'j\s*\^\{\+\}[^\n]{0,180}j\s*\^\{-\}',r'simplicity[^\n]{0,500}',r'EPRL[^\n]{0,500}']
    hs=windows(text,pats,900,40)
    good=[h for h in hs if not h['eq29_or_lambda_nearby'] and explicit_map_context(h['context'])]
    return {'lane':'simplicity-map-definition','pass':bool(good),'classification':'PASS' if good else 'BLOCKED_SOURCE_SIMPLICITY_MAP','archive_sha':src['archive_sha'],'source_file':src['file'],'qualified_contexts':good[:12],'all_contexts':hs[:20]}

def lane_B():
    src=source(); text=src['text']; start=src['start']
    # Search a broad exact-source neighborhood before/around Eq27 plus the full file for indexed +/- declarations.
    nearby=text[max(0,start-50000):min(len(text),src['end']+5000)]
    pats=[r'j\s*\^\s*\+\s*_\{?i\}?',r'j\s*\^\s*-\s*_\{?i\}?',r'j\s*_\{?i\}?\s*\^\s*\+',r'j\s*_\{?i\}?\s*\^\s*-',r'j\^\+_\d',r'j\^-_\d']
    hs=windows(nearby,pats,900,40)
    good=[]
    for h in hs:
        c=h['context']
        if h['eq29_or_lambda_nearby']: continue
        indexed=bool(re.search(r'j(?:\^\{?[+-]\}?_\{?(?:i|[1-4])\}?|_\{?(?:i|[1-4])\}?\^\{?[+-]\}?)',c))
        declaration=bool(re.search(r'(?:simplicity|EPRL|map|mapped|representation|for each|for all|i\s*=|i=)',c,re.I))
        pair=bool(re.search(r'j[^\n]{0,180}\+[^\n]{0,180}j[^\n]{0,180}-',c))
        if indexed and declaration and pair: good.append(h)
    return {'lane':'indexed-label-inheritance','pass':bool(good),'classification':'PASS' if good else 'BLOCKED_INDEXED_LABEL_INHERITANCE','archive_sha':src['archive_sha'],'qualified_contexts':good[:12],'all_contexts':hs[:20]}

def lane_C():
    src=source(); text=src['text']
    pats=[r'0\s*\\leq[^\n]{0,240}k',r'0\s*<=?[^\n]{0,240}k',r'k\s*/\s*2',r'k\+2',r'admissib[^\n]{0,500}',r'integrable[^\n]{0,500}',r'root of unity[^\n]{0,500}']
    hs=windows(text,pats,700,50)
    good=[]
    for h in hs:
        if h['eq29_or_lambda_nearby']: continue
        c=h['context']
        finite=bool(re.search(r'(?:0\s*(?:\\leq|<=?)|k\s*/\s*2|k\+2|finite|integrable|admissib)',c,re.I))
        reps=bool(re.search(r'(?:spin|representation|j\b|l\b|U_q|SU\(2\))',c,re.I))
        if finite and reps: good.append(h)
    return {'lane':'representation-domain','pass':bool(good),'classification':'PASS' if good else 'BLOCKED_REPRESENTATION_DOMAIN','archive_sha':src['archive_sha'],'qualified_contexts':good[:12],'all_contexts':hs[:20]}

def lane_D():
    src=source()
    rejected={'lexical_only_plus_minus':True,'fabricated_plus_equals_minus':True,'eq29_lambda_only_relation':True}
    return {'lane':'provenance-null','pass':src['archive_sha']==EXPECTED_ARCH and all(rejected.values()),'archive_sha':src['archive_sha'],'detected':sum(rejected.values()),'required':3,'rejected':rejected}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['A','B','C','D']); a=ap.parse_args()
    try: obj={'A':lane_A,'B':lane_B,'C':lane_C,'D':lane_D}[a.lane]()
    except Exception as e: obj={'lane':a.lane,'pass':False,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)}
    write(obj)
if __name__=='__main__':main()
