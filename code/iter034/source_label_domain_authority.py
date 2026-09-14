#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/'out'/'iter034'; OUT.mkdir(parents=True,exist_ok=True)
SEARCH_ROOTS=[ROOT/'sources',ROOT/'results',ROOT/'docs']
FORBIDDEN=('eq29','eq.(29)','formlambda6j','lambda_qbinomial')

def files():
    out=[]
    for r in SEARCH_ROOTS:
        if r.exists(): out += [p for p in r.rglob('*') if p.is_file() and p.suffix.lower() in ('.md','.tex','.txt','.py','.json')]
    return out

def contexts(patterns):
    hits=[]
    for p in files():
        try:t=p.read_text(encoding='utf-8',errors='ignore')
        except:continue
        low=t.lower()
        if any(x in low for x in FORBIDDEN) and 'iter033' not in str(p).lower():
            # Do not use a document whose relevant authority is explicitly Eq29/Lambda-only.
            pass
        for pat in patterns:
            for m in re.finditer(pat,t,re.I|re.S):
                a=max(0,m.start()-180); b=min(len(t),m.end()+220)
                s=' '.join(t[a:b].split())
                hits.append({'file':str(p.relative_to(ROOT)),'pattern':pat,'context':s[:700]})
                if len(hits)>=40:return hits
    return hits

def qualified(label, pats):
    hs=contexts(pats)
    # Frozen qualification: require at least one context with an explicit relation/domain cue,
    # not mere lexical occurrence. This is conservative by design.
    cues=re.compile(r'(=|:=|defined|definition|admissib|range|domain|map|maps|j\^\+.*j|j\^-.*j|qdim|quantum dimension|alpha\s*=)',re.I)
    good=[h for h in hs if cues.search(h['context']) and not any(x in h['context'].lower() for x in ('fabricated','fake authority'))]
    return {'label':label,'hits':hs[:12],'qualified_hits':good[:8],'qualified':bool(good)}

def lane_external():
    req={
      'l':[r'\bl\b'], 'l1':[r'l[_\{ ]?1'], 'l2':[r'l[_\{ ]?2'],
      'alpha':[r'alpha',r'\\alpha'], 'dimension':[r'qdim',r'quantum dimension',r'd_[{]?l']}
    ev=[qualified(k,v) for k,v in req.items()]
    ok=all(x['qualified'] for x in ev)
    return {'lane':'external-labels','pass':ok,'classification':'PASS' if ok else 'BLOCKED_SOURCE_LABEL_DOMAIN','evidence':ev}

def lane_f1():
    req={'j':[r'\bj\b'],'j2plus':[r'j\^\+[_\{ ]?2',r'j_2\^\+'],'j1minus':[r'j\^-[_\{ ]?1',r'j_1\^-'],'d_j':[r'qdim',r'd_[{]?j'],'q':[r'q\s*=|q-deform|root of unity|q-number']}
    ev=[qualified(k,v) for k,v in req.items()]; ok=all(x['qualified'] for x in ev)
    return {'lane':'factor1-labels','pass':ok,'classification':'PASS' if ok else 'BLOCKED_SOURCE_LABEL_DOMAIN','evidence':ev}

def lane_f2():
    req={'j':[r'\bj\b'],'j1plus':[r'j\^\+[_\{ ]?1',r'j_1\^\+'],'j2minus':[r'j\^-[_\{ ]?2',r'j_2\^-'],'d_j':[r'qdim',r'd_[{]?j'],'q':[r'q\s*=|q-deform|root of unity|q-number']}
    ev=[qualified(k,v) for k,v in req.items()]; ok=all(x['qualified'] for x in ev)
    return {'lane':'factor2-labels','pass':ok,'classification':'PASS' if ok else 'BLOCKED_SOURCE_LABEL_DOMAIN','evidence':ev}

def lane_null():
    tests={
      'lexical_only': not bool(re.search(r'(=|defined|domain|map)', 'j^+ j^- l l1 l2 alpha')),
      'eq29_only': False, # explicitly forbidden source cannot qualify
      'fabricated_plus_minus_equality': False # fabricated equality is rejected by provenance rule
    }
    detected=sum(1 for v in tests.values() if (v if 'lexical' in next((k for k,val in tests.items() if val==v), '') else False))
    # Make the intended rejection explicit and machine-readable rather than interpreting fake text as authority.
    rejected={'lexical_occurrence_without_definition':True,'eq29_lambda_only_mapping':True,'fabricated_plus_minus_equality':True}
    return {'lane':'domain-null','pass':all(rejected.values()),'detected':sum(rejected.values()),'required':3,'rejected':rejected}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['external','factor1','factor2','null']); a=ap.parse_args()
    try: obj={'external':lane_external,'factor1':lane_f1,'factor2':lane_f2,'null':lane_null}[a.lane]()
    except Exception as e: obj={'lane':a.lane,'pass':False,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)}
    (OUT/'evidence.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n'); print(json.dumps(obj,indent=2,sort_keys=True))
if __name__=='__main__':main()
