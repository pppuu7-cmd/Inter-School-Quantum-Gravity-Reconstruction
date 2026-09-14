#!/usr/bin/env python3
import argparse,io,json,re,time
from pathlib import Path
import requests
from pypdf import PdfReader
SOURCES={'hep-th/0105267v1':'Ambjorn-Jurkiewicz-Loll 2001 full CDT','1205.3791v1':'4D CDT transfer matrix 2012','1302.2210v1':'4D CDT transfer-matrix method 2013'}
TERMS=('transfer matrix','propagator','composition','reflection positivity','positive','hamiltonian','wick rotation','automorphism','symmetry factor','spatial triangulation','three-volume','effective transfer matrix','measure','inner product','proper time','foliation','sum over','matrix element')
def get_pdf(aid):
 errs=[]
 for u in (f'https://arxiv.org/pdf/{aid}',f'https://export.arxiv.org/pdf/{aid}'):
  for k in range(3):
   try:
    r=requests.get(u,timeout=45,headers={'User-Agent':'ISQGR-ITER067/1.0'})
    if r.status_code==200 and r.content[:4]==b'%PDF': return r.content,errs
    errs.append(f'{u}:HTTP{r.status_code}')
   except Exception as e: errs.append(f'{u}:{type(e).__name__}:{e}')
   time.sleep(2*(k+1))
 return None,errs
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source',required=True,choices=SOURCES); ap.add_argument('--out',required=True); a=ap.parse_args(); data,errs=get_pdf(a.source)
 if data is None: res={'source':a.source,'classification':'INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION','errors':errs}
 else:
  try:
   rd=PdfReader(io.BytesIO(data)); text='\n'.join((p.extract_text() or '') for p in rd.pages); low=text.lower(); ps=[]
   for t in TERMS:
    for m in re.finditer(re.escape(t),low):
     lo=max(0,m.start()-1200); hi=min(len(text),m.end()+1200); sn=re.sub(r'\s+',' ',text[lo:hi]); sl=sn.lower(); hits=[x for x in TERMS if x in sl]; ps.append({'trigger':t,'terms':hits,'snippet':sn[:2600]})
   uniq=[]; seen=set()
   for x in ps:
    k=x['snippet'][:400]
    if k not in seen: seen.add(k); uniq.append(x)
   required={'full_state':any('spatial triangulation' in x['terms'] and 'transfer matrix' in x['terms'] for x in uniq),'composition':any('composition' in x['terms'] or ('propagator' in x['terms'] and 'sum over' in x['terms']) for x in uniq),'measure':any(('automorphism' in x['terms'] or 'symmetry factor' in x['terms'] or 'measure' in x['terms']) and 'transfer matrix' in x['terms'] for x in uniq),'positivity':any(('reflection positivity' in x['terms'] or 'hamiltonian' in x['terms']) and 'transfer matrix' in x['terms'] for x in uniq),'full_effective':any('effective transfer matrix' in x['terms'] or 'three-volume' in x['terms'] for x in uniq),'time_wick':any(('proper time' in x['terms'] or 'foliation' in x['terms'] or 'wick rotation' in x['terms']) and 'transfer matrix' in x['terms'] for x in uniq)}
   res={'source':a.source,'label':SOURCES[a.source],'classification':'SOURCE_CANDIDATE_REQUIRES_MANUAL_AUDIT','pages':len(rd.pages),'pdf_bytes':len(data),'automated_predicates':required,'passages':uniq[:120],'claim_lock':'automation nominates exact passages only; manual equation-level audit controls scientific classification'}
  except Exception as e: res={'source':a.source,'classification':'INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION','errors':[repr(e)]}
 p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(res,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:v for k,v in res.items() if k!='passages'},indent=2))
if __name__=='__main__': main()
