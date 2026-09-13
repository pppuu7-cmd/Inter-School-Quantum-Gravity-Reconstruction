#!/usr/bin/env python3
import argparse, json, pathlib, re, tarfile, io, urllib.request, time
OUT=pathlib.Path('out'); OUT.mkdir(exist_ok=True)
TARGET='https://export.arxiv.org/e-print/1609.02429v2'
KEYS=['q-spinnet','biedenharn','wojtek']
UA={'User-Agent':'ISQGR-source-audit/1.0'}

def fetch(url,tries=3):
    err=None
    for i in range(tries):
        try:
            req=urllib.request.Request(url,headers=UA)
            with urllib.request.urlopen(req,timeout=45) as r:return r.read()
        except Exception as e: err=e; time.sleep(2*(i+1))
    raise err

def source_text():
    b=fetch(TARGET); tf=tarfile.open(fileobj=io.BytesIO(b),mode='r:*'); files={}
    for m in tf.getmembers():
        if m.isfile() and m.size<5_000_000 and (m.name.endswith('.tex') or m.name.endswith('.bib') or m.name.endswith('.bbl')):
            f=tf.extractfile(m); files[m.name]=f.read().decode('utf-8','replace') if f else ''
    return files

def bib_entries(text,key):
    pats=[rf'@\w+\s*\{{\s*{re.escape(key)}\s*,(.*?)(?=\n@|\Z)',rf'\\bibitem\{{{re.escape(key)}\}}(.*?)(?=\\bibitem|\Z)']
    out=[]
    for p in pats: out += re.findall(p,text,re.I|re.S)
    return out

def emit(ev,extras=None):
    (OUT/'evidence.json').write_text(json.dumps(ev,indent=2,sort_keys=True)+'\n')
    for n,c in (extras or {}).items():(OUT/n).write_text(c,encoding='utf-8')
    print(json.dumps(ev,indent=2,sort_keys=True))

def resolve():
    files=source_text(); alltxt='\n'.join(files.values()); found={k:bib_entries(alltxt,k) for k in KEYS}
    refs={k:[re.sub(r'\s+',' ',x)[:4000] for x in v] for k,v in found.items()}
    ok=all(len(v)>0 for v in refs.values())
    emit({'lane':'bib-resolve','keys':KEYS,'resolved':{k:bool(v) for k,v in refs.items()},'pass':ok}, {'resolved_refs.json':json.dumps(refs,indent=2,sort_keys=True)})

def qbar():
    files=source_text(); txt='\n'.join(files.values()); entries=bib_entries(txt,'q-spinnet'); body='\n'.join(entries)
    arx=re.findall(r'(?:arxiv|eprint)\s*[=:{{ ]+([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)',body,re.I)
    explicit=bool(re.search(r'(?:bar\{q\}|q\^-?1|dual).{0,500}(?:m_1|m_2|m_3).{0,500}=',txt,re.I|re.S))
    emit({'lane':'qbar-authority','qspinnet_bib_found':bool(entries),'qspinnet_arxiv_ids':arx,'explicit_index_equality_in_primary_package':explicit,'pass':bool(entries and explicit),'classification_hint':'PASS' if entries and explicit else 'BLOCKED_NEEDS_REFERENCED_SOURCE'})

def rlane():
    files=source_text(); txt='\n'.join(files.values()); refs={k:bib_entries(txt,k) for k in ['biedenharn','wojtek']}
    r_formula=bool(re.search(r'\\mathcal\{R\}\s*=.*?q\^',txt,re.S))
    emit({'lane':'r-authority','biedenharn_found':bool(refs['biedenharn']),'wojtek_found':bool(refs['wojtek']),'primary_graphical_R_formula':r_formula,'pass':bool(r_formula and refs['biedenharn'] and refs['wojtek']),'classification_hint':'SOURCE_CHAIN_PARTIAL' if r_formula else 'BLOCKED'})

def null():
    files=source_text(); txt='\n'.join(files.values()); lexical=('R matrix' in txt or 'R--matrix' in txt or 'mathcal{R}' in txt); fake=bool(re.search(r'@\w+\s*\{\s*definitely-not-a-real-key',txt,re.I));
    emit({'lane':'provenance-null','lexical_R_present':lexical,'fake_key_rejected':not fake,'pass':bool(lexical and not fake)})

def main():
    a=argparse.ArgumentParser(); a.add_argument('--lane',required=True,choices=['bib-resolve','qbar-authority','r-authority','provenance-null']); x=a.parse_args()
    try:{'bib-resolve':resolve,'qbar-authority':qbar,'r-authority':rlane,'provenance-null':null}[x.lane]()
    except Exception as e:emit({'lane':x.lane,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)})
if __name__=='__main__':main()
