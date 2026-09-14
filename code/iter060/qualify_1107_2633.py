#!/usr/bin/env python3
import argparse, hashlib, io, json, re, tarfile, time, urllib.request
from pathlib import Path

ARXIV_ID='1107.2633'
TITLE='Many-nodes/many-links spinfoam: the homogeneous and isotropic case'
UA='ISQGR-source-audit/1.0 (research reproducibility)'

def fetch(url, tries=4, timeout=60):
    last=None
    for i in range(tries):
        try:
            req=urllib.request.Request(url, headers={'User-Agent':UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.geturl(), r.read(), dict(r.headers)
        except Exception as e:
            last=repr(e); time.sleep(4*(i+1))
    raise RuntimeError(last)

def get_source():
    errs=[]
    for url in [f'https://export.arxiv.org/e-print/{ARXIV_ID}', f'https://arxiv.org/e-print/{ARXIV_ID}']:
        try:
            final,data,headers=fetch(url)
            return final,data,headers
        except Exception as e: errs.append([url,repr(e)])
    raise RuntimeError(json.dumps(errs))

def extract_text(data):
    files=[]
    try:
        tf=tarfile.open(fileobj=io.BytesIO(data), mode='r:*')
        for m in tf.getmembers():
            if not m.isfile() or m.size>5_000_000: continue
            name=m.name.lower()
            if not any(name.endswith(x) for x in ('.tex','.txt','.bib','.sty')): continue
            b=tf.extractfile(m).read()
            s=b.decode('utf-8','replace')
            files.append((m.name,s))
    except tarfile.ReadError:
        try: files=[('source.txt',data.decode('utf-8','replace'))]
        except Exception: files=[]
    return files

def compact(s): return re.sub(r'\s+',' ',s).strip()

def snippets(text, patterns, radius=180, maxn=12):
    out=[]
    for pat in patterns:
        for m in re.finditer(pat,text,re.I):
            a=max(0,m.start()-radius); b=min(len(text),m.end()+radius)
            z=compact(text[a:b])[:500]
            if z not in out: out.append(z)
            if len(out)>=maxn: return out
    return out

def source_bundle():
    final,data,headers=get_source(); files=extract_text(data)
    text='\n'.join(s for _,s in files)
    return {
      'final_url':final,'source_sha256':hashlib.sha256(data).hexdigest(),
      'source_bytes':len(data),'files':[n for n,_ in files],
      'text_sha256':hashlib.sha256(text.encode()).hexdigest(),'text':text
    }

def lane_exact():
    b=source_bundle(); t=b.pop('text')
    return {'iteration':'ITER060','lane':'exact-source','retrieval_pass':True,
      'arxiv_id':ARXIV_ID,'expected_title':TITLE,**b,
      'title_token_present':('many-nodes' in t.lower() and 'spinfoam' in t.lower()),
      'lorentzian_eprl_token_present':bool(re.search(r'Lorentzian.{0,80}EPRL|EPRL.{0,80}Lorentzian',t,re.I|re.S))}

def lane_language():
    b=source_bundle(); t=b['text']; low=t.lower()
    pats=[r'refin\w*',r'coarse\w*',r'fine\w*',r'embed\w*',r'cylindrical',r'graph\w*',r'map\w*',r'same support',r'large.?j']
    return {'iteration':'ITER060','lane':'refinement-language','retrieval_pass':True,
      'source_sha256':b['source_sha256'],
      'counts':{p:len(re.findall(p,t,re.I)) for p in pats},
      'snippets':snippets(t,pats),
      'explicit_map_phrase':bool(re.search(r'(refinement|coarse|fine|embedding).{0,120}\bmap\b|\bmap\b.{0,120}(refinement|coarse|fine|embedding)',t,re.I|re.S)),
      'same_support_language':('same support' in low)}

def lane_object():
    b=source_bundle(); t=b['text'];
    lor=bool(re.search(r'Lorentzian.{0,100}EPRL|EPRL.{0,100}Lorentzian',t,re.I|re.S))
    multi=bool(re.search(r'(different|arbitrary|many).{0,80}(graph|nodes|links)|(graph|nodes|links).{0,80}(different|arbitrary|many)',t,re.I|re.S))
    coarsefine=bool(re.search(r'\b(coarse|coarser)\b.{0,180}\b(fine|finer|refin\w*)\b|\b(fine|finer|refin\w*)\b.{0,180}\b(coarse|coarser)\b',t,re.I|re.S))
    explicit=bool(re.search(r'(embedding|refinement|coarse.?graining).{0,160}(map|transform|operator)|(?:map|transform|operator).{0,160}(embedding|refinement|coarse.?graining)',t,re.I|re.S))
    simplicial=bool(re.search(r'4-simplex|simplicial|simplex',t,re.I))
    trunc=bool(re.search(r'homogeneous.{0,50}isotropic|isotropic.{0,50}homogeneous',t,re.I|re.S))
    qualifies=lor and multi and coarsefine and explicit and simplicial and not trunc
    classification='SOURCE_AUTHORITY_PASS_SCOPED' if qualifies else 'SCOPED_BLOCKED_NO_EXPLICIT_REFINEMENT_MAP'
    return {'iteration':'ITER060','lane':'object-match','retrieval_pass':True,'source_sha256':b['source_sha256'],
      'lorentzian_eprl':lor,'multiple_graph_objects':multi,'distinct_coarse_fine':coarsefine,
      'explicit_refinement_map':explicit,'simplicial_token':simplicial,'homogeneous_isotropic_truncation':trunc,
      'qualifies':qualifies,'classification':classification,
      'evidence':snippets(t,[r'Lorentzian.{0,100}EPRL',r'same support',r'refin\w*',r'coarse\w*',r'4-simplex'],maxn=10)}

def lane_null():
    return {'iteration':'ITER060','lane':'null-controls','retrieval_pass':True,
      'metadata_only_is_not_map':True,'same_support_is_not_map':True,'same_semiclassical_limit_is_not_map':True,
      'multiple_graphs_is_not_map':True,'numerical_matching_for_convention_choice_forbidden':True,'bridge_credit':False,
      'candidate_theory':'UNFORMED','candidate_theory_percent':0}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    try:
        f={'exact-source':lane_exact,'refinement-language':lane_language,'object-match':lane_object,'null-controls':lane_null}[a.lane]
        out=f()
    except Exception as e:
        out={'iteration':'ITER060','lane':a.lane,'retrieval_pass':False,'classification':'INFRASTRUCTURE_FAIL_PRE_SCIENCE','error':repr(e)}
        Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2)); raise
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
