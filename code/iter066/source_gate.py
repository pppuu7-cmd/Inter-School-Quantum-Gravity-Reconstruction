#!/usr/bin/env python3
import argparse, io, json, re, time
from pathlib import Path
import requests
from pypdf import PdfReader

SOURCES={
 '1903.11544':'Surya causal-set QG review',
 '2007.13192':'Machet-Wang BDG continuum limit',
 'gr-qc/0212064':'Rideout causal-set dynamics',
}
QTERMS=('quantum measure','decoherence functional','sum over histories','path integral','amplitude','partition function')
STERMS=('coarse grain','coarse-grain','renormal','refinement','growth','sequential','composition','cylinder')
ATERMS=('benincasa','dowker','glaser','action')

def get_pdf(aid):
    urls=[f'https://arxiv.org/pdf/{aid}',f'https://export.arxiv.org/pdf/{aid}']
    errs=[]
    for url in urls:
      for k in range(3):
        try:
          r=requests.get(url,timeout=45,headers={'User-Agent':'ISQGR-source-audit/1.0'})
          if r.status_code==200 and r.content[:4]==b'%PDF': return r.content,errs
          errs.append(f'{url}:HTTP{r.status_code}')
        except Exception as e: errs.append(f'{url}:{type(e).__name__}:{e}')
        time.sleep(2*(k+1))
    return None,errs

def hits(text):
    low=text.lower(); out=[]
    terms=QTERMS+STERMS+ATERMS
    for term in terms:
      for m in re.finditer(re.escape(term),low):
        lo=max(0,m.start()-900); hi=min(len(text),m.end()+900)
        sn=re.sub(r'\s+',' ',text[lo:hi])
        sl=sn.lower()
        qs=[x for x in QTERMS if x in sl]; ss=[x for x in STERMS if x in sl]; aa=[x for x in ATERMS if x in sl]
        out.append({'trigger':term,'quantum_terms':qs,'scale_terms':ss,'action_terms':aa,'joint_quantum_scale':bool(qs and ss),'snippet':sn[:2000]})
    uniq=[]; seen=set()
    for x in out:
      key=x['snippet'][:300]
      if key not in seen: seen.add(key); uniq.append(x)
    return uniq

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source',required=True,choices=SOURCES); ap.add_argument('--out',required=True); a=ap.parse_args()
    data,errs=get_pdf(a.source)
    if data is None:
      res={'source':a.source,'label':SOURCES[a.source],'classification':'INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION','errors':errs}
    else:
      try:
        rd=PdfReader(io.BytesIO(data)); text='\n'.join((p.extract_text() or '') for p in rd.pages); hs=hits(text)
        joint=[x for x in hs if x['joint_quantum_scale']]
        q=[x for x in hs if x['quantum_terms']]
        if joint: cls='SOURCE_CANDIDATE_AMPLITUDE_REFINEMENT_PRESENT'
        elif q: cls='SOURCE_CANDIDATE_QUANTUM_DYNAMICS_ONLY'
        else: cls='NO_AUTOMATED_QUANTUM_DYNAMICS_CANDIDATE'
        res={'source':a.source,'label':SOURCES[a.source],'classification':cls,'pdf_bytes':len(data),'pages':len(rd.pages),'joint_candidate_count':len(joint),'quantum_candidate_count':len(q),'passages':hs[:80],'claim_lock':'automated passages nominate manual audit only; no gate or bridge credit'}
      except Exception as e:
        res={'source':a.source,'label':SOURCES[a.source],'classification':'INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION','errors':[repr(e)]}
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(res,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in res.items() if k!='passages'},indent=2))
if __name__=='__main__': main()
