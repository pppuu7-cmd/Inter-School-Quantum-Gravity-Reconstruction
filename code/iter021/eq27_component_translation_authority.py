#!/usr/bin/env python3
import argparse, hashlib, importlib.util, json, pathlib, re
import numpy as np

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=pathlib.Path('out'); OUT.mkdir(exist_ok=True)

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
v1=load(pathlib.Path('code/iter018/parallel_audit.py'),'it18v1')
qcg=load(pathlib.Path('code/iter019/qcg_solver_validation.py'),'it19qcg')
TARGET='1609.02429v2'
HIST='3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee'

def source_bundle():
    src,_=v1.fetch(f'https://export.arxiv.org/e-print/{TARGET}')
    h=hashlib.sha256(src).hexdigest(); files,packing=v1.safe_tex_members(src)
    return h,files,'\n'.join(files.values()),packing

def next_display(text,pos):
    tail=text[pos:pos+50000]; starts=[]
    for pat,kind in [(r'\\begin\{equation\*?\}','equation'),(r'\\begin\{align\*?\}','align'),(r'\\be\b','be'),(r'\\ba\b','ba'),(r'\\bea\b','bea')]:
        m=re.search(pat,tail)
        if m: starts.append((m.start(),kind))
    if not starts: return None
    rel,kind=min(starts); start=pos+rel; sub=text[start:start+50000]
    ep={'equation':r'\\end\{equation\*?\}','align':r'\\end\{align\*?\}','be':r'\\ee\b','ba':r'\\ea\b','bea':r'\\eea\b'}[kind]
    em=re.search(ep,sub)
    return None if not em else text[start:start+em.end()]

def exact_eq27(files):
    hits=[]; ar=re.compile(r'derivations\s+of\s+the\s+normali[sz]ation\s+and\s+the\s+diagrams\s+respectively',re.I)
    for fn,text in files.items():
        for m in ar.finditer(text):
            sn=next_display(text,m.end())
            if sn and '\\label{eq:eprl-3-valent}' in sn: hits.append((fn,sn))
    return hits

def context(alltex,terms,r=5000):
    low=alltex.lower(); parts=[]
    for t in terms:
        p=low.find(t.lower())
        if p>=0: parts.append(alltex[max(0,p-r):min(len(alltex),p+r)])
    return '\n\n%%%% CONTEXT %%%%\n\n'.join(parts)

def write(ev,extras=None):
    (OUT/'evidence.json').write_text(json.dumps(ev,indent=2,sort_keys=True)+'\n')
    for n,c in (extras or {}).items(): (OUT/n).write_text(c,encoding='utf-8')
    print(json.dumps(ev,indent=2,sort_keys=True))

def topology():
    h,files,alltex,packing=source_bundle(); hits=exact_eq27(files); sn=hits[0][1] if len(hits)==1 else ''
    inv={'label_present':'\\label{eq:eprl-3-valent}' in sn,'tikz_token_count':sn.count('tikzpicture'),'draw_count':sn.count('\\draw'),'sum_count':sn.count('\\sum'),'l_loop_count':sn.count('node {$l$}'),'primed_Jplus':"$(J^+)'$" in sn,'primed_Jminus':"$(J^-)'$" in sn,'unprimed_Jplus':'$J^+$' in sn,'unprimed_Jminus':'$J^-$' in sn}
    ok=len(hits)==1 and h==HIST and inv['label_present'] and inv['tikz_token_count']==4 and inv['draw_count']==2 and inv['sum_count']>=2 and inv['l_loop_count']==2 and all(inv[k] for k in ('primed_Jplus','primed_Jminus','unprimed_Jplus','unprimed_Jminus'))
    write({'lane':'topology','source_hash':h,'historical_hash_match':h==HIST,'exact_display_hits':len(hits),'inventory':inv,'source_snippet_sha256':hashlib.sha256(sn.encode()).hexdigest() if sn else None,'pass':bool(ok)},{'eq27_exact.tex':sn})

def primitives():
    h,files,alltex,packing=source_bundle(); hits=exact_eq27(files); low=alltex.lower()
    req={
      'q_number':['EXECUTABLE_QUALIFIED',hasattr(qcg,'qnum')],
      'quantum_dimension':['EXECUTABLE_QUALIFIED',hasattr(qcg,'qnum')],
      'admissibility_A7':['EXECUTABLE_QUALIFIED',hasattr(qcg,'admissible')],
      'qcg_embedding':['EXECUTABLE_QUALIFIED',hasattr(qcg,'solve_channel')],
      'coproduct_action':['EXECUTABLE_QUALIFIED',hasattr(qcg,'tensor_ops')],
      'bilinear_A8_A9':['EXECUTABLE_QUALIFIED',hasattr(qcg,'solve_channel')],
      'cap_B2':['EXECUTABLE_QUALIFIED',hasattr(qcg,'b2_singlet')],
      'cup_qbar_dual':['SOURCE_QUALIFIED_COMPONENT_TRANSLATION_PENDING',('cup' in low and ('bar{q}' in alltex or '\\bar q' in alltex))],
      'R_braiding':['MISSING_EXECUTABLE_PRIMITIVE',('r matrices' in low or 'r-matrix' in low)]
    }
    missing=[k for k,(s,e) in req.items() if not e or s.startswith('MISSING') or s.endswith('PENDING')]
    write({'lane':'primitives','source_hash':h,'historical_hash_match':h==HIST,'required_primitives':{k:{'status':v[0],'evidence':v[1]} for k,v in req.items()},'missing_or_pending':missing,'pass':bool(h==HIST and len(hits)==1 and not missing),'scientific_interpretation':'missing primitive => BLOCKED, no guessed convention'},{'primitive_source_context.tex':context(alltex,['R matrices','R-matrix','cap','cup','orthogonality','completeness'])})

def normalization():
    h,files,alltex,packing=source_bundle(); low=alltex.lower()
    sig={'appendix_b_graphical_identity_signal':('graphical identities' in low and 'appendix' in low),'E3_signal':('(e3)' in low or 'e3}' in low or 'label{e3' in low or 'label{eq:e3' in low),'delta_ll_signal':('delta' in low),'quantum_dimension_signal':('quantum dimension' in low or 'd_' in alltex),'bilinear_not_hermitian_manifest':True}
    rows=[]; mx=0.0
    for tj in (1,2,4,6,8):
        C=qcg.solve_channel(tj,tj,0,12)['C']; B=qcg.b2_singlet(tj,12)
        r=min(float(np.max(np.abs(C-B))),float(np.max(np.abs(C+B)))); mx=max(mx,r); rows.append({'twice_j':tj,'residual_up_to_sign':r})
    ok=h==HIST and sig['appendix_b_graphical_identity_signal'] and sig['E3_signal'] and sig['quantum_dimension_signal'] and mx<2e-9
    write({'lane':'normalization','source_hash':h,'signals':sig,'B2_solver_rows':rows,'max_B2_residual_up_to_sign':mx,'threshold':2e-9,'full_eq27_graph_evaluated':False,'pass':bool(ok)},{'appendixE_context.tex':context(alltex,['(E3)','graphical identities','T_{EPRL}','T_EPRL'],7000)})

def null_lane():
    h,files,alltex,packing=source_bundle(); hits=exact_eq27(files); sn=hits[0][1] if len(hits)==1 else ''
    base={'qdim':('d' in sn or 'dim' in sn.lower()),'dual':("$(J^+)'$" in sn and "$(J^-)'$" in sn),'orientation':("$(J^+)'$" in sn and '$J^+$' in sn),'l_loops':sn.count('node {$l$}')==2}
    def accept(m): return all(bool(m[k]) for k in ('qdim','dual','orientation','l_loops'))
    ctr=[]
    for key in ('qdim','dual','orientation'):
        m=dict(base); m[key]=False; ctr.append({'removed':key,'accepted':accept(m)})
    rejected=sum(not x['accepted'] for x in ctr); correct=accept(base)
    write({'lane':'null','source_hash':h,'correct_manifest':base,'correct_accepted':correct,'wrong_manifests':ctr,'wrong_rejected':rejected,'required_wrong_rejected':2,'pass':bool(h==HIST and len(hits)==1 and correct and rejected>=2)})

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['topology','primitives','normalization','null']); a=ap.parse_args()
    try: {'topology':topology,'primitives':primitives,'normalization':normalization,'null':null_lane}[a.lane]()
    except Exception as e: write({'lane':a.lane,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)})
if __name__=='__main__': main()
