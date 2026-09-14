#!/usr/bin/env python3
import argparse, hashlib, json, re, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path
QUERIES={
 'lorentzian-eprl-refinement':'all:"Lorentzian EPRL" AND (all:refinement OR all:"coarse graining")',
 'lorentzian-spin-foam-map':'all:"Lorentzian spin foam" AND (all:"embedding map" OR all:"coarse graining")',
 'eprl-rg-simplicial':'all:EPRL AND all:renormalization AND (all:simplicial OR all:Pachner)',
 'eprl-refinement-map':'all:EPRL AND (all:"refinement map" OR all:"embedding map")'
}
CONSUMED={'2302.00072','1803.00835','0810.1714','1903.12624','1412.8247','1409.2407','1701.02311'}
NS={'a':'http://www.w3.org/2005/Atom'}
def fetch(q):
 params=urllib.parse.urlencode({'search_query':q,'start':0,'max_results':50,'sortBy':'relevance','sortOrder':'descending'})
 urls=['https://export.arxiv.org/api/query?'+params,'https://arxiv.org/api/query?'+params]
 last=None
 for base in urls:
  for k in range(4):
   try:
    req=urllib.request.Request(base,headers={'User-Agent':'ISQGR-discovery/1.0'})
    with urllib.request.urlopen(req,timeout=90) as r: data=r.read()
    if data:return base,data
   except Exception as e:last=repr(e);time.sleep(4*(k+1))
 raise RuntimeError(last)
def aid(x):
 m=re.search(r'arxiv.org/abs/([^v]+)',x);return m.group(1) if m else x.rsplit('/',1)[-1].split('v')[0]
def score(title,summary):
 t=(title+' '+summary).lower(); flags={
 'lorentzian_eprl':(('lorentzian' in t) and ('eprl' in t or 'engle-pereira-rovelli-livine' in t)),
 'map_transform':any(x in t for x in ['refinement','coarse grain','coarse-grain','embedding map','renormalization']),
 'simplicial_multivertex':any(x in t for x in ['simplicial','pachner','multi-vertex','multivertex','5-1','five vertex','five-vertex']),
 'boundary_amplitude_map':(('boundary' in t or 'amplitude' in t) and any(x in t for x in ['map','refin','coarse','renormal']))}
 return flags,sum(flags.values())
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--lane',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
 if a.lane=='null-provenance':
  out={'iteration':'ITER059','lane':a.lane,'pass':True,'queries_frozen':QUERIES,'consumed_sorted':sorted(CONSUMED),'metadata_only_no_authority_pass':True}
 else:
  q=QUERIES[a.lane];url,data=fetch(q);root=ET.fromstring(data);entries=[]
  for e in root.findall('a:entry',NS):
   i=aid(e.findtext('a:id','',NS));title=' '.join(e.findtext('a:title','',NS).split());summary=' '.join(e.findtext('a:summary','',NS).split());authors=[x.findtext('a:name','',NS) for x in e.findall('a:author',NS)];flags,n=score(title,summary)
   entries.append({'arxiv_id':i,'title':title,'authors':authors,'summary':summary,'published':e.findtext('a:published','',NS),'updated':e.findtext('a:updated','',NS),'already_consumed':i in CONSUMED,'inclusion_flags':flags,'inclusion_score':n,'new_metadata_candidate':(i not in CONSUMED and n>=2)})
  out={'iteration':'ITER059','lane':a.lane,'query':q,'url':url,'response_sha256':hashlib.sha256(data).hexdigest(),'retrieval_pass':True,'entry_count':len(entries),'entries':entries,'new_candidate_ids':[x['arxiv_id'] for x in entries if x['new_metadata_candidate']]}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
