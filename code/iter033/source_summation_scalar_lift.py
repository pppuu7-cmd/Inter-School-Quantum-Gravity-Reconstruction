#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, pathlib, re

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/'out'/'iter033'; OUT.mkdir(parents=True,exist_ok=True)
spec=importlib.util.spec_from_file_location('iter030_stage_s',ROOT/'code/iter030/corrected_stage_s.py')
k30=importlib.util.module_from_spec(spec); spec.loader.exec_module(k30)
REQ=[ROOT/'prereg/ITER033_RC006_EQ27_SOURCE_SUMMATION_SCALAR_LIFT_2026-09-14.md',ROOT/'results/ITER032_RC006_EQ27_TWO_FACTOR_BOUNDED_NETWORK_ASSEMBLY_PASS_2026-09-14.md']
FACTOR_RE=re.compile(r'\\left\[\s*\\sum.*?\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\s*\\right\]',re.S)
SUM_RE=re.compile(r'\\sum\b|\\sum_')

def write(x):
    (OUT/'evidence.json').write_text(json.dumps(x,indent=2,sort_keys=True)+'\n'); print(json.dumps(x,indent=2,sort_keys=True))

def load():
    src,err=k30.load_source()
    if err: raise RuntimeError(json.dumps(err,sort_keys=True))
    missing=[str(p.relative_to(ROOT)) for p in REQ if not p.exists()]
    if missing: raise FileNotFoundError(','.join(missing))
    return src

def segment(d):
    ms=list(FACTOR_RE.finditer(d))
    if len(ms)!=2:
        return {'ok':False,'factor_count':len(ms),'sum_count':len(SUM_RE.findall(d))}
    f1,f2=ms
    prefix=d[:f1.start()]; sep=d[f1.end():f2.start()]; suffix=d[f2.end():]
    times=bool(re.search(r'\\times\b',sep))
    no_alt=not bool(re.search(r'[=,+]',sep))
    return {'ok':len(SUM_RE.findall(d))==2 and f1.end()<=f2.start() and times and no_alt,
            'factor_count':2,'sum_count':len(SUM_RE.findall(d)),'prefix':prefix,'factor1':f1.group(0),'separator':sep,'factor2':f2.group(0),'suffix':suffix}

def binder(factor):
    m=re.search(r'\\sum(?:_\{[^}]+\}|_[^\s]+)?(.*?)\\begin\{tikzpicture\}',factor,re.S)
    if not m: return None
    lead=factor[factor.find('\\sum')+4:factor.find('\\begin{tikzpicture}')]
    return lead.strip()

def lane_segmentation():
    src=load(); d=src['display']; s=segment(d)
    ok=bool(s.get('ok'))
    return {'lane':'segmentation','pass':ok,'archive_sha':src['archive_sha'],'eq_sha':src['eq_sha'],
            'factor_count':s.get('factor_count'),'sum_count':s.get('sum_count'),'prefix':s.get('prefix',''),
            'separator':s.get('separator',''),'suffix':s.get('suffix',''),'multiplicative_separator':bool(ok)}

def lane_binding():
    src=load(); s=segment(src['display'])
    if s.get('factor_count')!=2:
        return {'lane':'summation-binding','pass':False,'classification':'BLOCKED'}
    factors=[s['factor1'],s['factor2']]; binders=[binder(f) for f in factors]
    counts=[len(SUM_RE.findall(f)) for f in factors]
    sep_sums=len(SUM_RE.findall(s['separator']))
    ok=s.get('ok') and counts==[1,1] and sep_sums==0 and all(b is not None and b!='' for b in binders)
    return {'lane':'summation-binding','pass':bool(ok),'sum_counts_per_factor':counts,'separator_sum_count':sep_sums,'binders_verbatim':binders}

def lane_scalar():
    src=load(); s=segment(src['display'])
    if s.get('factor_count')!=2:
        return {'lane':'external-scalar-inventory','pass':False,'classification':'BLOCKED'}
    external=s['prefix']+'\n<FACTOR_SEPARATOR>\n'+s['separator']+'\n<AFTER_FACTOR2>\n'+s['suffix']
    extra_tikz=('\\begin{tikzpicture}' in external or '\\end{tikzpicture}' in external)
    extra_sum=bool(SUM_RE.search(external))
    # Strip TeX layout commands only for inventory visibility; verbatim source is retained separately.
    nonlayout=re.sub(r'\\(?:nonumber|quad|qquad)\b|\\\\|&',' ',external)
    nonlayout=' '.join(nonlayout.split())
    ok=s.get('ok') and not extra_tikz and not extra_sum
    return {'lane':'external-scalar-inventory','pass':bool(ok),'extra_tikz':extra_tikz,'extra_sum':extra_sum,
            'external_verbatim':external,'external_nonlayout_inventory':nonlayout}

def structural_ok(d):
    s=segment(d)
    if not s.get('ok') or s.get('factor_count')!=2: return False
    fs=[s['factor1'],s['factor2']]
    bs=[binder(f) for f in fs]
    return [len(SUM_RE.findall(f)) for f in fs]==[1,1] and len(SUM_RE.findall(s['separator']))==0 and all(b for b in bs)

def lane_nulls():
    src=load(); d=src['display']; base=segment(d)
    if not base.get('ok'):
        return {'lane':'syntax-nulls','pass':False,'infrastructure_failure':False,'base_invalid':True}
    # Mutation 1: source multiplicative separator -> plus, only in inter-factor region.
    d1=base['prefix']+base['factor1']+base['separator'].replace('\\times','+',1)+base['factor2']+base['suffix']
    # Mutation 2: remove first factor's first sum token.
    f1=base['factor1'].replace('\\sum','',1)
    d2=base['prefix']+f1+base['separator']+base['factor2']+base['suffix']
    # Mutation 3: append a third duplicate bracketed factor.
    d3=d+base['factor2']
    vals={'separator_times_to_plus':not structural_ok(d1),'delete_first_sum':not structural_ok(d2),'append_third_factor':not structural_ok(d3)}
    detected=sum(vals.values())
    return {'lane':'syntax-nulls','pass':detected==3,'detected':detected,'required':3,'nulls':vals}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['segmentation','binding','scalar','nulls']); a=ap.parse_args()
    try:
        obj={'segmentation':lane_segmentation,'binding':lane_binding,'scalar':lane_scalar,'nulls':lane_nulls}[a.lane]()
    except Exception as e:
        obj={'lane':a.lane,'pass':False,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)}
    write(obj)
if __name__=='__main__': main()
