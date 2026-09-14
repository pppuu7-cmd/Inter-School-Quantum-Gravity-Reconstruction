#!/usr/bin/env python3
from __future__ import annotations
import argparse, gzip, hashlib, io, json, re, tarfile, time, urllib.request
from pathlib import Path, PurePosixPath

ARXIV='1609.02429v2'
ARCH='3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee'
EQ='88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d'

def fetch(url,n=6):
    err=None
    for i in range(n):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'ISQGR-ITER030/1.0'})
            with urllib.request.urlopen(req,timeout=75) as r:return r.read()
        except Exception as e: err=repr(e); time.sleep(2*(i+1))
    raise RuntimeError(err)

def unpack(data):
    try:
        with tarfile.open(fileobj=io.BytesIO(data),mode='r:*') as tf:
            out={}
            for m in tf.getmembers():
                p=PurePosixPath(m.name)
                if p.is_absolute() or '..' in p.parts or not m.isfile() or m.size>12_000_000 or p.suffix.lower() not in {'.tex','.sty','.bib'}: continue
                f=tf.extractfile(m)
                if f: out[str(p)]=f.read().decode('utf-8','replace')
            if out:return out
    except tarfile.TarError: pass
    try:return {'source.tex':gzip.decompress(data).decode('utf-8','replace')}
    except Exception:return {'source.tex':data.decode('utf-8','replace')}

def display(text,pos):
    pats=[(r'\\begin\{align\*?\}',r'\\end\{align\*?\}'),(r'\\begin\{equation\*?\}',r'\\end\{equation\*?\}'),(r'\\ba\b',r'\\ea\b'),(r'\\be\b',r'\\ee\b')]
    starts=[]
    for a,b in pats: starts += [(m.start(),b) for m in re.finditer(a,text[:pos+1])]
    for s,b in sorted(starts,reverse=True):
        q=re.search(b,text[s:])
        if q:
            e=s+q.end()
            if s<=pos<=e:return text[s:e],s,e
    return None

def load_source():
    raw=fetch(f'https://export.arxiv.org/e-print/{ARXIV}')
    ah=hashlib.sha256(raw).hexdigest(); files=unpack(raw); hits=[]
    for fn,t in files.items():
        for m in re.finditer(r'\\label\{eq:eprl-3-valent\}',t):
            d=display(t,m.start())
            if d:hits.append((fn,t,*d))
    if ah!=ARCH or len(hits)!=1:
        return None,{'classification':'INFRASTRUCTURE_OR_PROVENANCE_BLOCKED','archive_sha':ah,'hits':len(hits)}
    fn,text,d,s,e=hits[0]; eh=hashlib.sha256(d.encode()).hexdigest()
    if eh!=EQ:return None,{'classification':'INFRASTRUCTURE_OR_PROVENANCE_BLOCKED','archive_sha':ah,'eq_sha':eh}
    return {'archive_sha':ah,'eq_sha':eh,'file':fn,'text':text,'display':d,'start':s,'end':e},None

def blocks(d): return re.findall(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}',d,re.S)
def label_tokens(s): return sorted(set(re.findall(r"(?:j|l|J)(?:_\{[^}]+\}|_\w+|\^\{[+\-]\}|\^[+\-]|')+",s)))
def draw_commands(b): return [m.group(0) for m in re.finditer(r'\\draw(?:\[[^\]]*\])?\s*(.*?);',b,re.S)]
def node_names(b): return set(re.findall(r'\\node(?:\[[^\]]*\])?\s*\(([^)]+)\)',b,re.S))
def refs(draw): return re.findall(r'\(([^)]+)\)',draw)

def run_lane(lane):
    src,err=load_source()
    if err:return err
    d=src['display']; bs=blocks(d)
    base={'lane':lane,'archive_sha':src['archive_sha'],'eq_sha':src['eq_sha'],'source_file':src['file']}
    if lane=='A':
        begin=len(re.findall(r'\\begin\{tikzpicture\}',d)); end=len(re.findall(r'\\end\{tikzpicture\}',d)); draws=len(re.findall(r'\\draw\b',d)); sums=len(re.findall(r'\\sum\b|\\sum_',d))
        factors=len(re.findall(r'\\left\[\s*\\sum.*?\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\s*\\right\]',d,re.S))
        ok=(len(bs)==2 and begin==2 and end==2 and draws==2 and sums==2 and factors==2)
        return {**base,'pass':ok,'classification':'PASS' if ok else 'RC006_EQ27_CORRECTED_STAGE_S_SOURCE_CONTRADICTION','tikz_environments':len(bs),'begin_end_tokens':begin+end,'draw_commands':draws,'sum_structures':sums,'bracketed_factors':factors}
    if lane=='B':
        unresolved=[]; inventory=[]
        for i,b in enumerate(bs,1):
            names=node_names(b); ds=draw_commands(b); item={'factor':i,'nodes':sorted(names),'draws':ds,'labels':label_tokens(b)}
            for j,dr in enumerate(ds,1):
                sym=[x for x in refs(dr) if re.match(r'^[A-Za-z@][A-Za-z0-9_:@.-]*$',x)]
                missing=[x for x in sym if x not in names]
                if missing: unresolved.append({'factor':i,'draw':j,'kind':'unresolved_named_endpoint','refs':missing})
                if len(sym)<2 and not label_tokens(dr): unresolved.append({'factor':i,'draw':j,'kind':'endpoint_or_leg_not_component_qualified'})
            inventory.append(item)
        ok=(len(bs)==2 and not unresolved)
        return {**base,'pass':ok,'classification':'PASS' if ok else 'BLOCKED_TOPOLOGY_ENDPOINT_AUTHORITY','factor_inventory':inventory,'unresolved':unresolved}
    if lane=='C':
        unresolved=[]; edges=[]
        # Strict prereg rule: graphical geometry alone is not component/index authority.
        # A draw path must itself carry component labels or be backed by an explicit nearby algebraic index relation.
        context=src['text'][max(0,src['start']-12000):min(len(src['text']),src['end']+12000)]
        for i,b in enumerate(bs,1):
            for j,dr in enumerate(draw_commands(b),1):
                toks=label_tokens(dr)
                entry={'factor':i,'draw':j,'draw_labels':toks,'raw':dr}
                edges.append(entry)
                if not toks:
                    unresolved.append({'factor':i,'draw':j,'kind':'draw_geometry_without_explicit_component_index_order'})
        # Record but do not promote generic appendix vocabulary to a specific edge mapping.
        appendix_vocab={k:bool(re.search(p,context,re.S)) for k,p in {
            'magnetic_indices':r'magnetic|m[_^]|n[_^]',
            'primed_channels':r"J[^\n]{0,20}'",
            'qbar':r'\\bar\s*q|qbar|q\\leftrightarrow',
            'cap_cup':r'cap|cup|bending|bend',
            'R_matrix':r'R[-_ ]?matrix|\\mathcal\{R\}|R\^\{-1\}'}.items()}
        ok=(len(bs)==2 and len(unresolved)==0)
        return {**base,'pass':ok,'classification':'PASS' if ok else 'BLOCKED_INDEX_AUTHORITY','edges':edges,'unresolved':unresolved,'nearby_authority_vocabulary':appendix_vocab}
    if lane=='D':
        begin=len(re.findall(r'\\begin\{tikzpicture\}',d)); end=len(re.findall(r'\\end\{tikzpicture\}',d)); factors=len(bs)
        primed=bool(re.search(r"J[^\n]{0,30}'",d)); scalar_markers={'quantum_dimensions':len(re.findall(r'\\dim|d_',d)),'signs':len(re.findall(r'\(-1\)|\^\{[^}]*-1',d)),'fractions':len(re.findall(r'\\frac',d))}
        wrong={'four_graph_factors':factors==4,'one_graph_factor':factors==1,'four_tokens_as_four_factors':(begin+end)==factors,'accept_unlabelled_draw_as_index_authority':False,'erase_primed_unprimed':not primed}
        detected=sum(not v for v in wrong.values())
        ok=(detected==5 and primed)
        return {**base,'pass':ok,'classification':'PASS' if ok else 'BLOCKED_SCALAR_OR_NULL_CONTROL','scalar_markers':scalar_markers,'primed_channel_present':primed,'wrong_interpretations':wrong,'detected':detected,'required':5}
    raise ValueError(lane)

def aggregate(root):
    lane_data=[]
    for p in sorted(Path(root).rglob('lane_*.json')):
        try: lane_data.append(json.loads(p.read_text()))
        except Exception: pass
    by={x.get('lane'):x for x in lane_data if x.get('lane') in 'ABCD'}
    if len(by)<4:
        return {'classification':'NUMERICAL_OR_INFRASTRUCTURE_FAIL_PRE_SCIENCE','scientific_pass':False,'reason':'missing_lane_artifacts','lanes_present':sorted(by)}
    if any(x.get('classification')=='INFRASTRUCTURE_OR_PROVENANCE_BLOCKED' for x in by.values()): cls='INFRASTRUCTURE_OR_PROVENANCE_BLOCKED'
    elif not by['A'].get('pass'): cls='RC006_EQ27_CORRECTED_STAGE_S_SOURCE_CONTRADICTION'
    elif all(x.get('pass') for x in by.values()): cls='RC006_EQ27_CORRECTED_STAGE_S_COMPONENT_MAP_PASS'
    else: cls='RC006_EQ27_CORRECTED_STAGE_S_COMPONENT_MAP_BLOCKED'
    return {'classification':cls,'scientific_pass':cls.endswith('COMPONENT_MAP_PASS'),'numerical_contraction_authorized':cls.endswith('COMPONENT_MAP_PASS'),'lanes':by,'claim_locks_preserved':True}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',choices=list('ABCD')); ap.add_argument('--aggregate'); ap.add_argument('--out',required=True); a=ap.parse_args()
    out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
    try:
        obj=aggregate(a.aggregate) if a.aggregate else run_lane(a.lane)
    except Exception as e: obj={'classification':'NUMERICAL_OR_INFRASTRUCTURE_FAIL_PRE_SCIENCE','scientific_pass':False,'error':repr(e),'lane':a.lane}
    name='aggregate.json' if a.aggregate else f'lane_{a.lane}.json'; (out/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n'); print(json.dumps(obj,indent=2,sort_keys=True))
if __name__=='__main__': main()
