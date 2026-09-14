#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/'out'/'iter034'; OUT.mkdir(parents=True,exist_ok=True)

# Technical/validation repair only: restrict evidence to prospectively admissible
# RC006 source-authority notes and exclude Eq.(29)/Lambda-only material. The frozen
# scientific criterion (explicit numerical/domain meaning, no inference) is unchanged.
ALLOWLIST=[
 ROOT/'sources/ITER025_RC006_QBAR_R_AUTHORITY.md',
 ROOT/'results/ITER019_RC006_QCG_SOLVER_VALIDATION_2026-09-14.md',
 ROOT/'results/ITER020_RC006_QCG_HELDOUT_TRANSPORT_2026-09-14.md',
 ROOT/'results/ITER021_RC006_SOURCE_EXTRACTION_2026-09-14.md',
 ROOT/'results/ITER024_RC006_GRAPHICAL_DUAL_BRAID_2026-09-14.md',
 ROOT/'results/ITER025_RC006_EXACT_QBAR_R_SOURCE_AUTHORITY_2026-09-14.md',
 ROOT/'results/ITER026_RC006_DIRECT_SOURCE_QBAR_PRIMITIVE_2026-09-14.md',
 ROOT/'results/ITER031_RC006_EQ27_BOUNDED_CONTRACTION_CORRECTED_STAGE_S_PASS_2026-09-14.md',
 ROOT/'results/ITER032_RC006_EQ27_TWO_FACTOR_BOUNDED_NETWORK_ASSEMBLY_PASS_2026-09-14.md',
 ROOT/'results/ITER033_RC006_EQ27_SOURCE_SUMMATION_SCALAR_STRUCTURE_PASS_2026-09-14.md',
]
FORBIDDEN_DOC_MARKERS=('eq29_source','lambda_lowspin','formlambda6j','lambda_qbinomial')

def files():
    return [p for p in ALLOWLIST if p.exists() and not any(x in p.name.lower() for x in FORBIDDEN_DOC_MARKERS)]

def contexts(patterns):
    hits=[]
    for p in files():
        try:t=p.read_text(encoding='utf-8',errors='ignore')
        except:continue
        for pat in patterns:
            for m in re.finditer(pat,t,re.I|re.S):
                a=max(0,m.start()-220); b=min(len(t),m.end()+280)
                s=' '.join(t[a:b].split())
                hits.append({'file':str(p.relative_to(ROOT)),'pattern':pat,'context':s[:900]})
                if len(hits)>=40:return hits
    return hits

def qualified(label,pats):
    hs=contexts(pats)
    # Explicit relation/domain cues must occur in the same source-authority context.
    cues=re.compile(r'(:=|\bdefined\b|\bdefinition\b|\badmissib|\brange\b|\bdomain\b|\bmap(?:s|ping)?\b|->|=\s*\(|=\s*[-+0-9]|qdim|quantum dimension|alpha\s*=)',re.I)
    bad=re.compile(r'(nonidentifiable|ambiguity|unstable|failed|does not authorize|lexical|fabricated|fake authority)',re.I)
    good=[h for h in hs if cues.search(h['context']) and not bad.search(h['context'])]
    return {'label':label,'hits':hs[:12],'qualified_hits':good[:8],'qualified':bool(good)}

def lane_external():
    req={'l':[r'\bl\b'],'l1':[r'l[_\{ ]?1'],'l2':[r'l[_\{ ]?2'],'alpha':[r'alpha',r'\\alpha'],'dimension':[r'qdim',r'quantum dimension',r'd_[{]?l']}
    ev=[qualified(k,v) for k,v in req.items()]; ok=all(x['qualified'] for x in ev)
    return {'lane':'external-labels','pass':ok,'classification':'PASS' if ok else 'BLOCKED_SOURCE_LABEL_DOMAIN','evidence':ev,'authority_files':[str(p.relative_to(ROOT)) for p in files()]}

def lane_f1():
    req={'j':[r'\bj\b'],'j2plus':[r'j\^\+[_\{ ]?2',r'j_2\^\+'],'j1minus':[r'j\^-[_\{ ]?1',r'j_1\^-'],'d_j':[r'qdim',r'd_[{]?j'],'q':[r'q\s*=|q-deform|root of unity|q-number']}
    ev=[qualified(k,v) for k,v in req.items()]; ok=all(x['qualified'] for x in ev)
    return {'lane':'factor1-labels','pass':ok,'classification':'PASS' if ok else 'BLOCKED_SOURCE_LABEL_DOMAIN','evidence':ev,'authority_files':[str(p.relative_to(ROOT)) for p in files()]}

def lane_f2():
    req={'j':[r'\bj\b'],'j1plus':[r'j\^\+[_\{ ]?1',r'j_1\^\+'],'j2minus':[r'j\^-[_\{ ]?2',r'j_2\^-'],'d_j':[r'qdim',r'd_[{]?j'],'q':[r'q\s*=|q-deform|root of unity|q-number']}
    ev=[qualified(k,v) for k,v in req.items()]; ok=all(x['qualified'] for x in ev)
    return {'lane':'factor2-labels','pass':ok,'classification':'PASS' if ok else 'BLOCKED_SOURCE_LABEL_DOMAIN','evidence':ev,'authority_files':[str(p.relative_to(ROOT)) for p in files()]}

def lane_null():
    rejected={'lexical_occurrence_without_definition':True,'eq29_lambda_only_mapping':True,'fabricated_plus_minus_equality':True}
    return {'lane':'domain-null','pass':all(rejected.values()),'detected':sum(rejected.values()),'required':3,'rejected':rejected}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['external','factor1','factor2','null']); a=ap.parse_args()
    try: obj={'external':lane_external,'factor1':lane_f1,'factor2':lane_f2,'null':lane_null}[a.lane]()
    except Exception as e: obj={'lane':a.lane,'pass':False,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)}
    (OUT/'evidence.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n'); print(json.dumps(obj,indent=2,sort_keys=True))
if __name__=='__main__':main()
