#!/usr/bin/env python3
from __future__ import annotations
import gzip, hashlib, io, json, re, tarfile, time, urllib.request
from pathlib import Path, PurePosixPath

OUT=Path('out_iter029'); OUT.mkdir(exist_ok=True)
ARXIV='1609.02429v2'
ARCH='3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee'
EQ='88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d'

def fetch(url, n=5):
    e=None
    for i in range(n):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'ISQGR-ITER029/1.0'})
            with urllib.request.urlopen(req,timeout=75) as r:return r.read()
        except Exception as x:e=repr(x); time.sleep(2*(i+1))
    raise RuntimeError(e)

def unpack(data):
    try:
        with tarfile.open(fileobj=io.BytesIO(data),mode='r:*') as tf:
            out={}
            for m in tf.getmembers():
                p=PurePosixPath(m.name)
                if p.is_absolute() or '..' in p.parts or not m.isfile() or p.suffix.lower() not in {'.tex','.sty','.bib'}: continue
                f=tf.extractfile(m)
                if f: out[str(p)]=f.read().decode('utf-8','replace')
            if out:return out
    except tarfile.TarError: pass
    try:return {'source.tex':gzip.decompress(data).decode('utf-8','replace')}
    except Exception:return {'source.tex':data.decode('utf-8','replace')}

def display(text,pos):
    pats=[(r'\\begin\{align\*?\}',r'\\end\{align\*?\}'),(r'\\begin\{equation\*?\}',r'\\end\{equation\*?\}')]
    ss=[]
    for a,b in pats:ss += [(m.start(),b) for m in re.finditer(a,text[:pos+1])]
    for s,b in sorted(ss,reverse=True):
        q=re.search(b,text[s:])
        if q:
            e=s+q.end()
            if s<=pos<=e:return text[s:e]
    return None

def lane(name,passed,**kw):
    return {'lane':name,'pass':bool(passed),**kw}

def main():
    try:
        raw=fetch(f'https://export.arxiv.org/e-print/{ARXIV}')
        ah=hashlib.sha256(raw).hexdigest(); files=unpack(raw)
        hits=[]
        for fn,t in files.items():
            for m in re.finditer(r'\\label\{eq:eprl-3-valent\}',t):
                d=display(t,m.start())
                if d:hits.append((fn,d))
        if ah!=ARCH or len(hits)!=1:
            out={'classification':'INFRASTRUCTURE_OR_PROVENANCE_BLOCKED','archive_sha':ah,'hits':len(hits)}
            (OUT/'aggregate.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2)); return
        fn,d=hits[0]; eh=hashlib.sha256(d.encode()).hexdigest()
        if eh!=EQ:
            out={'classification':'INFRASTRUCTURE_OR_PROVENANCE_BLOCKED','archive_sha':ah,'eq_sha':eh}
            (OUT/'aggregate.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2)); return

        b=len(re.findall(r'\\begin\{tikzpicture\}',d)); e=len(re.findall(r'\\end\{tikzpicture\}',d)); env=min(b,e)
        draw=len(re.findall(r'\\draw\b',d)); sums=len(re.findall(r'\\sum\b|\\sum_',d))
        bracket_factors=len(re.findall(r'\\left\[\s*\\sum.*?\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\s*\\right\]',d,re.S))
        A=lane('source-token-census', env==2 and b==2 and e==2 and draw==2 and sums==2,
               environments=env,begin_tokens=b,end_tokens=e,begin_end_tokens=b+e,draw_commands=draw,sums=sums,eq_sha=eh)

        p21=Path('results/ITER021_RC006_EQ27_COMPONENT_TRANSLATION_2026-09-14.md').read_text()
        p28=Path('prereg/ITER028_RC006_EQ27_TOPOLOGY_FAITHFUL_CONTRACTION_2026-09-14.md').read_text()
        r28=Path('results/ITER028_RC006_EQ27_STAGE_S_SOURCE_GRAPH_MAP_BLOCKED_2026-09-14.md').read_text()
        hist21=('two draw paths, four TikZ begin/end tokens' in p21)
        iter28_four=('four TikZ graphical blocks / source graphical factors' in p28)
        iter28_blocked=('two `tikzpicture` graphical factors' in r28 and 'four TikZ graphical blocks' in r28)
        B=lane('historical-language-audit',hist21 and iter28_four and iter28_blocked,
               iter021_two_draw_four_tokens=hist21,iter028_four_graphical_language=iter28_four,iter028_blocker_recorded=iter28_blocked)

        C=lane('structural-factorization', bracket_factors==2 and sums==2 and env==2,
               bracketed_sum_tikz_factors=bracket_factors,sums=sums,environments=env)
        wrong={'four_environments':env==4,'one_environment':env==1,'four_bracket_factors':bracket_factors==4,'hash_mismatch':eh!=EQ}
        D=lane('null-controls',not any(wrong.values()),wrong_interpretations=wrong,detected=sum(not v for v in wrong.values()),required=4)

        lanes=[A,B,C,D]
        if all(x['pass'] for x in lanes): cls='RC006_EQ27_SOURCE_SEMANTICS_RECONCILED_SCOPED'
        elif ah==ARCH and eh==EQ: cls='RC006_EQ27_SOURCE_SEMANTICS_RECONCILIATION_BLOCKED'
        else: cls='INFRASTRUCTURE_OR_PROVENANCE_BLOCKED'
        out={'classification':cls,'scientific_pass':cls.endswith('RECONCILED_SCOPED'),'archive_sha':ah,'eq_sha':eh,'source_file':fn,'lanes':lanes,
             'iter028_retrofit_authorized':False,'new_stage_s_successor_prereg_allowed':cls.endswith('RECONCILED_SCOPED')}
        for x in lanes:(OUT/f"{x['lane']}.json").write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
        (OUT/'eq27_exact.tex').write_text(d)
        (OUT/'aggregate.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
        print(json.dumps(out,indent=2,sort_keys=True))
    except Exception as e:
        out={'classification':'NUMERICAL_OR_INFRASTRUCTURE_FAIL_PRE_SCIENCE','error':repr(e),'scientific_pass':False}
        (OUT/'aggregate.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))

if __name__=='__main__':main()
