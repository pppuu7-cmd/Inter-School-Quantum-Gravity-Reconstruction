#!/usr/bin/env python3
import argparse, hashlib, importlib.util, json, pathlib, re
import numpy as np

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=pathlib.Path('out'); OUT.mkdir(exist_ok=True)
TARGET='1609.02429v2'
HIST='3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee'

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
v1=load(pathlib.Path('code/iter018/parallel_audit.py'),'it18v1')
qcg=load(pathlib.Path('code/iter019/qcg_solver_validation.py'),'it19qcg')

def bundle():
    src,_=v1.fetch(f'https://export.arxiv.org/e-print/{TARGET}')
    h=hashlib.sha256(src).hexdigest(); files,packing=v1.safe_tex_members(src)
    return h,files,'\n'.join(files.values())

def emit(ev,extras=None):
    (OUT/'evidence.json').write_text(json.dumps(ev,indent=2,sort_keys=True)+'\n')
    for n,c in (extras or {}).items(): (OUT/n).write_text(c,encoding='utf-8')
    print(json.dumps(ev,indent=2,sort_keys=True))

def magnetic(tj): return np.arange(-tj,tj+1,2,dtype=float)/2

def capcup(tj,k,wrong=None):
    ms=magnetic(tj); n=len(ms); cap=np.zeros((n,n),complex); cup=np.zeros((n,n),complex)
    j=tj/2
    for a,m in enumerate(ms):
        for b,mp in enumerate(ms):
            if abs(mp+m)>1e-12: continue
            cap[a,b]=(-1)**int(round(j-m))*qcg.qpow(m/2,k)
            exponent=m/2
            signexp=j+m
            if wrong=='cup-q-exponent': exponent=-m/2
            if wrong=='cup-sign': signexp=j-m
            cup[a,b]=(-1)**int(round(signexp))*qcg.qpow(exponent,k)
    return cap,cup

def lane_capcup():
    rows=[]; mx=0.0
    for k in (6,10,12):
        for tj in (1,2,3,4,5):
            if tj>k: continue
            cap,cup=capcup(tj,k); r=float(np.max(np.abs(cap@cup-np.eye(tj+1))))
            mx=max(mx,r); rows.append({'k':k,'twice_j':tj,'identity_residual':r})
    emit({'lane':'capcup','rows':rows,'max_identity_residual':mx,'threshold':1e-12,'phase_or_sign_fit':False,'pass':bool(mx<1e-12)})

def source_context(alltex,terms,r=6500):
    low=alltex.lower(); parts=[]
    for term in terms:
        p=low.find(term.lower())
        if p>=0: parts.append(alltex[max(0,p-r):min(len(alltex),p+r)])
    return '\n\n%%%% CONTEXT %%%%\n\n'.join(parts)

def lane_qbar():
    h,files,alltex=bundle(); low=alltex.lower()
    # Frozen criterion requires source statement + uniquely executable index ordering.
    relation=('inverse (here: complex conjugate) deformation parameter' in low and 'cup' in low and 'cap' in low)
    ctx=source_context(alltex,['inverse (here: complex conjugate) deformation parameter','dual to','cup'])
    # The primary source states the relation graphically. Until a separately validated
    # graph-to-index ordering is encoded, do not choose an orientation post hoc.
    explicit_component_equation=bool(re.search(r'\{\}_\{\\bar\{q\}\}\s*\\mathcal\{C\}.*=',alltex,re.S))
    graph_to_index_ordering_qualified=False
    # Local cap/cup round trip is nevertheless checked as a necessary subcontrol.
    mx=0.0
    for k in (6,10,12):
        for tj in (1,2,3,4):
            cap,cup=capcup(tj,k); mx=max(mx,float(np.max(np.abs(cap@cup-np.eye(tj+1)))))
    passed=h==HIST and relation and explicit_component_equation and graph_to_index_ordering_qualified and mx<2e-9
    emit({'lane':'qbar','source_hash':h,'historical_hash_match':h==HIST,'graphical_qbar_relation_found':relation,'explicit_component_equation_signal':explicit_component_equation,'graph_to_index_ordering_qualified':graph_to_index_ordering_qualified,'capcup_subcontrol_max_residual':mx,'threshold':2e-9,'classification_hint':'PASS' if passed else 'BLOCKED_GRAPH_TO_INDEX_ORDERING','pass':bool(passed)},{'qbar_source_context.tex':ctx})

def lane_rbraid():
    h,files,alltex=bundle(); low=alltex.lower()
    pats=['r matrix','r-matrix','r--matrix','r matrices','r--matrices','braid']
    hits={p:low.count(p) for p in pats}; total=sum(hits.values())
    ctx=source_context(alltex,pats+['identities (b15)','derivation of eprl amplitude'],8000)
    appendix_f=('derivation of eprl amplitude' in low)
    explicit_formula=bool(re.search(r'R[^\n]{0,80}:?=|R[^\n]{0,80}\\equiv',alltex))
    external_ref=('q-spinnet' in ctx.lower() or 'biedenharn' in ctx.lower())
    # No source-proven cancellation is inferred merely from a diagram.
    source_proven_cancelled=False
    passed=h==HIST and appendix_f and total>0 and (explicit_formula or source_proven_cancelled)
    hint='PASS' if passed else ('BLOCKED_EXTERNAL_R_AUTHORITY' if total>0 and not explicit_formula else 'BLOCKED_R_SOURCE_RECOVERY')
    emit({'lane':'rbraid','source_hash':h,'historical_hash_match':h==HIST,'lexical_hits':hits,'appendixF_found':appendix_f,'explicit_executable_R_formula_signal':explicit_formula,'source_proven_cancelled':source_proven_cancelled,'external_reference_signal':external_ref,'classification_hint':hint,'pass':bool(passed)},{'rbraid_source_context.tex':ctx})

def lane_null():
    rows=[]; correct_max=0.0; wrong={'cup-q-exponent':0.0,'cup-sign':0.0}
    for k in (6,10,12):
        for tj in (1,2,3,4,5):
            if tj>k: continue
            cap,cup=capcup(tj,k); correct_max=max(correct_max,float(np.max(np.abs(cap@cup-np.eye(tj+1)))))
            for mode in wrong:
                _,cw=capcup(tj,k,mode); wrong[mode]=max(wrong[mode],float(np.max(np.abs(cap@cw-np.eye(tj+1)))))
    # Third wrong control: ordinary Hermitian dual is source-structurally rejected because
    # source explicitly inserts cups/caps for qbar duality.
    h,files,alltex=bundle(); low=alltex.lower(); hermitian_wrong_detected=('inverse (here: complex conjugate) deformation parameter' in low and 'cup' in low and 'cap' in low)
    detections=sum(v>1e-6 for v in wrong.values()) + int(hermitian_wrong_detected)
    passed=h==HIST and correct_max<1e-12 and detections>=2
    emit({'lane':'null','correct_max_residual':correct_max,'wrong_numeric_residuals':wrong,'ordinary_hermitian_dual_source_rejected':hermitian_wrong_detected,'detected_wrong_controls':detections,'required_detected':2,'pass':bool(passed)})

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['capcup','qbar','rbraid','null']); a=ap.parse_args()
    try: {'capcup':lane_capcup,'qbar':lane_qbar,'rbraid':lane_rbraid,'null':lane_null}[a.lane]()
    except Exception as e: emit({'lane':a.lane,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)})
if __name__=='__main__': main()
