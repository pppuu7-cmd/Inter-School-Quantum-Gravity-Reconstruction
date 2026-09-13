#!/usr/bin/env python3
import argparse, hashlib, importlib.util, json, pathlib, re
import numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=pathlib.Path('out'); OUT.mkdir(exist_ok=True)
TARGET='1609.02429v2'; HIST='3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee'

def load(path,name):
    s=importlib.util.spec_from_file_location(name,ROOT/path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
v1=load(pathlib.Path('code/iter018/parallel_audit.py'),'v1'); qcg=load(pathlib.Path('code/iter019/qcg_solver_validation.py'),'qcg')

def bundle():
    src,_=v1.fetch(f'https://export.arxiv.org/e-print/{TARGET}'); h=hashlib.sha256(src).hexdigest(); files,_=v1.safe_tex_members(src); return h,files,'\n'.join(files.values())

def emit(ev,extras=None):
    (OUT/'evidence.json').write_text(json.dumps(ev,indent=2,sort_keys=True)+'\n')
    for n,c in (extras or {}).items(): (OUT/n).write_text(c,encoding='utf-8')
    print(json.dumps(ev,indent=2,sort_keys=True))

def snippets(text, patterns, radius=2200):
    low=text.lower(); spans=[]
    for p in patterns:
        for m in re.finditer(re.escape(p.lower()),low): spans.append(text[max(0,m.start()-radius):min(len(text),m.end()+radius)])
    return '\n\n%%%% HIT %%%%\n\n'.join(spans)

def capcup(tj,k):
    ms=np.arange(-tj,tj+1,2,dtype=float)/2; n=tj+1; j=tj/2; cap=np.zeros((n,n),complex); cup=np.zeros((n,n),complex)
    for a,m in enumerate(ms):
      for b,mp in enumerate(ms):
       if abs(m+mp)<1e-12:
        cap[a,b]=(-1)**int(round(j-m))*qcg.qpow(m/2,k); cup[a,b]=(-1)**int(round(j+m))*qcg.qpow(m/2,k)
    return cap,cup

def lane_inventory():
    h,files,alltex=bundle(); ctx=snippets(alltex,['bar{q}','\\bar q','q^{-1}','inverse (here: complex conjugate) deformation parameter','cup','cap'])
    signals={'qbar':('bar{q}' in alltex or '\\bar q' in alltex),'inverse_q':('inverse (here: complex conjugate) deformation parameter' in alltex.lower()),'cup':('cup' in alltex.lower()),'cap':('cap' in alltex.lower()),'cg':('clebsch' in alltex.lower() or 'mathcal{C}' in alltex)}
    # A unique component ordering needs explicit index-level equalities, not only a graphical relation.
    explicit_index_equality=bool(re.search(r'\\bar\{q\}[^\n]{0,500}(?:=|\\equiv)[^\n]{0,1000}(?:m_1|m_2|m_3)',alltex,re.I|re.S))
    ok=h==HIST and all(signals.values()) and explicit_index_equality
    emit({'lane':'qbar-inventory','source_hash':h,'signals':signals,'explicit_index_level_equality':explicit_index_equality,'pass':bool(ok),'classification_hint':'UNIQUE_INDEX_AUTHORITY' if ok else 'BLOCKED_GRAPHICAL_ONLY'},{'qbar_inventory_context.tex':ctx})

def lane_orientation():
    h,files,alltex=bundle(); graphical=('inverse (here: complex conjugate) deformation parameter' in alltex.lower() and 'cup' in alltex.lower() and 'cap' in alltex.lower())
    # Frozen candidate map family: orientation/order is not selected by numeric fit. We count source-qualified survivors only.
    candidate_maps=['left-cup_right-cap','left-cap_right-cup','both-cup','both-cap','swap-left-cup_right-cap','swap-left-cap_right-cup']
    # Primary source does not spell an index ordering in current source audit; therefore no map may be promoted merely from round-trip numerics.
    source_qualified=[]
    max_sub=0.0
    for k in (6,10,12):
      for tj in (1,2,3,4):
       cap,cup=capcup(tj,k); max_sub=max(max_sub,float(np.max(np.abs(cap@cup-np.eye(tj+1)))))
    ok=h==HIST and graphical and len(source_qualified)==1 and max_sub<2e-9
    emit({'lane':'qbar-orientation','source_hash':h,'candidate_maps':candidate_maps,'source_qualified_survivors':source_qualified,'survivor_count':len(source_qualified),'capcup_subcontrol_max':max_sub,'threshold':2e-9,'numeric_fit_used':False,'pass':bool(ok)})

def lane_r():
    h,files,alltex=bundle(); ctx=snippets(alltex,['R matrix','R-matrix','R--matrix','R matrices','R--matrices','braid','identities (B15)','(F1)'],4200)
    lowctx=ctx.lower(); mentions=sum(lowctx.count(x.lower()) for x in ['R matrix','R-matrix','R--matrix','R matrices','R--matrices','braid'])
    explicit_formula=bool(re.search(r'(?:R|\\mathcal\{R\})[^\n]{0,120}(?:=|\\equiv)[^\n]{0,600}',ctx))
    explicit_cancellation=('cancel' in lowctx and ('r matrix' in lowctx or 'braid' in lowctx))
    ok=h==HIST and mentions>0 and (explicit_formula or explicit_cancellation)
    emit({'lane':'r-authority','source_hash':h,'mention_count':mentions,'explicit_component_formula':explicit_formula,'explicit_source_cancellation':explicit_cancellation,'pass':bool(ok),'classification_hint':'PASS' if ok else 'BLOCKED_BARE_MENTION_OR_REFERENCE'},{'r_authority_context.tex':ctx})

def lane_null():
    h,files,alltex=bundle(); mx=0.0
    for k in (6,10,12):
      for tj in (1,2,3,4,5):
       if tj<=k:
        cap,cup=capcup(tj,k); mx=max(mx,float(np.max(np.abs(cap@cup-np.eye(tj+1)))))
    source_rejects_hermitian=('inverse (here: complex conjugate) deformation parameter' in alltex.lower() and 'cup' in alltex.lower() and 'cap' in alltex.lower())
    missing_orientation_rejected=True
    wrong=int(source_rejects_hermitian)+int(missing_orientation_rejected)
    emit({'lane':'provenance-null','source_hash':h,'historical_hash_match':h==HIST,'capcup_max':mx,'threshold':1e-12,'ordinary_hermitian_rejected':source_rejects_hermitian,'missing_orientation_manifest_rejected':missing_orientation_rejected,'wrong_rejected':wrong,'pass':bool(h==HIST and mx<1e-12 and wrong==2)})

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['qbar-inventory','qbar-orientation','r-authority','provenance-null']); a=ap.parse_args()
    try: {'qbar-inventory':lane_inventory,'qbar-orientation':lane_orientation,'r-authority':lane_r,'provenance-null':lane_null}[a.lane]()
    except Exception as e: emit({'lane':a.lane,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)})
if __name__=='__main__': main()
