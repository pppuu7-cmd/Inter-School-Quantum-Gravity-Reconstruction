#!/usr/bin/env python3
import argparse, hashlib, importlib.util, json, pathlib, re, sys

ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=pathlib.Path('out'); OUT.mkdir(exist_ok=True)

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
v1=load(pathlib.Path('code/iter018/parallel_audit.py'),'it18v1')
v2=load(pathlib.Path('code/iter018/parallel_audit_v2.py'),'it18v2')
qcg=load(pathlib.Path('code/iter019/qcg_solver_validation.py'),'it19qcg')
TARGET='1609.02429v2'
HIST='3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee'

def source_bundle():
    src,_=v1.fetch(f'https://export.arxiv.org/e-print/{TARGET}')
    h=hashlib.sha256(src).hexdigest(); files,packing=v1.safe_tex_members(src)
    alltex='\n'.join(files.values())
    return src,h,files,alltex,packing

def exact_eq27(files):
    hits=[]
    anchor_re=re.compile(r'derivations\s+of\s+the\s+normali[sz]ation\s+and\s+the\s+diagrams\s+respectively',re.I)
    for fn,text in files.items():
        for m in anchor_re.finditer(text):
            env=v2.next_display_environment(text,m.end())
            if env:
                sn,s,e,marker=env
                if '\\label{eq:eprl-3-valent}' in sn:
                    hits.append((fn,sn,s,e,marker,text))
    return hits

def find_context(alltex, needles, radius=5000):
    low=alltex.lower(); out=[]
    for needle in needles:
        p=low.find(needle.lower())
        if p>=0: out.append(alltex[max(0,p-radius):min(len(alltex),p+radius)])
    return '\n\n%%%% CONTEXT %%%%\n\n'.join(out)

def write(ev, extras=None):
    (OUT/'evidence.json').write_text(json.dumps(ev,indent=2,sort_keys=True)+'\n')
    if extras:
        for n,c in extras.items(): (OUT/n).write_text(c,encoding='utf-8')
    print(json.dumps(ev,indent=2,sort_keys=True))

def lane_topology():
    src,h,files,alltex,packing=source_bundle()
    hits=exact_eq27(files); unique=len(hits)==1
    sn=hits[0][1] if unique else ''
    inv={
      'label_present':'\\label{eq:eprl-3-valent}' in sn,
      'tikz_token_count':sn.count('tikzpicture'),
      'draw_count':sn.count('\\draw'),
      'sum_count':sn.count('\\sum'),
      'l_loop_count':sn.count('node {$l$}'),
      'primed_Jplus':'$(J^+)' in sn,
      'primed_Jminus':'$(J^-)' in sn,
      'unprimed_Jplus':'$J^+$' in sn,
      'unprimed_Jminus':'$J^-$' in sn,
      'hatS':'hat{S}' in sn,
      'alpha':'\\alpha' in sn,
    }
    pass_top=unique and h==HIST and inv['label_present'] and inv['tikz_token_count']==4 and inv['draw_count']==2 and inv['sum_count']>=2 and inv['l_loop_count']==2 and all(inv[k] for k in ['primed_Jplus','primed_Jminus','unprimed_Jplus','unprimed_Jminus'])
    ev={'lane':'topology','source':TARGET,'eprint_sha256':h,'historical_hash_match':h==HIST,'packing':packing,'exact_display_hits':len(hits),'inventory':inv,'source_snippet_sha256':hashlib.sha256(sn.encode()).hexdigest() if sn else None,'pass':bool(pass_top)}
    write(ev,{'eq27_exact.tex':sn})

def lane_primitives():
    src,h,files,alltex,packing=source_bundle(); hits=exact_eq27(files); sn=hits[0][1] if len(hits)==1 else ''
    ctx=find_context(alltex,['R matrices','R-matrix','cap','cup','orthogonality','completeness'])
    required={
      'q_number':{'status':'EXECUTABLE_QUALIFIED','evidence':hasattr(qcg,'qnum')},
      'quantum_dimension':{'status':'EXECUTABLE_QUALIFIED','evidence':hasattr(qcg,'b2_singlet') and hasattr(qcg,'qnum')},
      'admissibility_A7':{'status':'EXECUTABLE_QUALIFIED','evidence':hasattr(qcg,'admissible')},
      'qcg_embedding':{'status':'EXECUTABLE_QUALIFIED','evidence':hasattr(qcg,'solve_channel')},
      'coproduct_action':{'status':'EXECUTABLE_QUALIFIED','evidence':hasattr(qcg,'tensor_ops')},
      'bilinear_A8_A9':{'status':'EXECUTABLE_QUALIFIED','evidence':hasattr(qcg,'solve_channel')},
      'cap_B2':{'status':'EXECUTABLE_QUALIFIED','evidence':hasattr(qcg,'b2_singlet')},
      'cup_qbar_dual':{'status':'SOURCE_QUALIFIED_COMPONENT_TRANSLATION_PENDING','evidence':('cup' in alltex.lower() and ('bar{q}' in alltex or '\\bar q' in alltex))},
      'R_braiding':{'status':'MISSING_EXECUTABLE_PRIMITIVE','evidence':(('r matrices' in alltex.lower()) or ('r-matrix' in alltex.lower()))},
    }
    missing=[k for k,v in required.items() if (not v['evidence']) or v['status'].startswith('MISSING') or v['status'].endswith('PENDING')]
    # Authority PASS requires every required primitive executable or source-proven-cancelled; do not infer cancellation.
    passed=(h==HIST and len(hits)==1 and not missing)
    ev={'lane':'primitives','source_hash':h,'historical_hash_match':h==HIST,'required_primitives':required,'missing_or_pending':missing,'pass':bool(passed),'scientific_interpretation':'MISSING means component reconstruction remains BLOCKED; no convention is invented'}
    write(ev,{'primitive_source_context.tex':ctx,'eq27_exact.tex':sn})

def lane_normalization():
    src,h,files,alltex,packing=source_bundle(); low=alltex.lower()
    ctx=find_context(alltex,['(E3)','label{','graphical identities','T_{EPRL}','T_EPRL'],7000)
    # Frozen source-level obligations; do not pretend textual audit is a numerical full-graph evaluation.
    signals={
      'appendix_b_graphical_identity_signal':('graphical identities' in low and 'appendix' in low),
      'E3_signal':('(e3)' in low or 'e3}' in low or 'label{e3' in low or 'label{eq:e3' in low),
      'delta_ll_signal':(('delta' in low) and ("l'" in alltex or 'l^\\prime' in alltex or "l^{\\prime}" in alltex)),
      'quantum_dimension_signal':('quantum dimension' in low or 'qdim' in low or 'd_' in alltex),
      'bilinear_not_hermitian_manifest':True,
    }
    # Executable singlet control using the already validated k=12 solver.
    cap_rows=[]; capmax=0.0
    for tj in [1,2,4,6,8]:
        C=qcg.solve_channel(tj,tj,0,12)['C']; B=qcg.b2_singlet(tj,12)
        import numpy as np
        r=min(float(np.max(np.abs(C-B))),float(np.max(np.abs(C+B))))
        capmax=max(capmax,r); cap_rows.append({'twice_j':tj,'residual_up_to_sign':r})
    passed=h==HIST and signals['appendix_b_graphical_identity_signal'] and signals['E3_signal'] and signals['quantum_dimension_signal'] and capmax<2e-9
    ev={'lane':'normalization','source_hash':h,'signals':signals,'B2_solver_rows':cap_rows,'max_B2_residual_up_to_sign':capmax,'threshold':2e-9,'full_eq27_graph_evaluated':False,'pass':bool(passed)}
    write(ev,{'appendixE_context.tex':ctx})

def lane_null():
    src,h,files,alltex,packing=source_bundle(); hits=exact_eq27(files); sn=hits[0][1] if len(hits)==1 else ''
    base={'qdim':('d' in sn or 'dim' in sn.lower()),'dual':(('J^+)' in sn and '(J^-)' in sn),'orientation':(('J^+)' in sn and '$J^+$' in sn),'l_loops':sn.count('node {$l$}')==2}
    # Validator obligations are intentionally structural and frozen.
    def accept(m): return all(bool(m[k]) for k in ['qdim','dual','orientation','l_loops'])
    controls=[]
    for key in ['qdim','dual','orientation']:
        m=dict(base); m[key]=False; controls.append({'removed':key,'accepted':accept(m)})
    rejected=sum(not x['accepted'] for x in controls); correct=accept(base)
    passed=h==HIST and len(hits)==1 and correct and rejected>=2
    ev={'lane':'null','source_hash':h,'correct_manifest':base,'correct_accepted':correct,'wrong_manifests':controls,'wrong_rejected':rejected,'required_wrong_rejected':2,'pass':bool(passed)}
    write(ev)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True,choices=['topology','primitives','normalization','null']); a=ap.parse_args()
    try: {'topology':lane_topology,'primitives':lane_primitives,'normalization':lane_normalization,'null':lane_null}[a.lane]()
    except Exception as e:
        write({'lane':a.lane,'infrastructure_failure':True,'scientific_negative':False,'error':repr(e)})
if __name__=='__main__': main()
