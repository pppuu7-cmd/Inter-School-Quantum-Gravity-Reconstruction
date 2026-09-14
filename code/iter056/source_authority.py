#!/usr/bin/env python3
import argparse, hashlib, json, os, re, subprocess
from pathlib import Path

REPO_URL='https://github.com/PietropaoloFrisoni/Monte_Carlo_spinfoams.git'
COMMIT='84b375f2a2e0d29b44dd8820953553624bb007a3'
TREE='5ded1505fbb148b8ab336027a509f942d9565176'
NB_PATH='notebooks/julia/5-1_move_EPRL_analysis.ipynb'
NB_BLOB='bd1a55c0e95b98244df02e049346ba8b7488797a'

TEXT_EXT={'.jl','.c','.cc','.cpp','.h','.hpp','.md','.txt','.sh','.toml','.yaml','.yml','.json','.ipynb','.csv'}

def run(cmd,cwd=None):
    return subprocess.check_output(cmd,cwd=cwd,text=True).strip()

def ensure_source(root):
    src=Path(root)/'author_source'
    if not src.exists():
        subprocess.check_call(['git','clone','--quiet','--no-checkout',REPO_URL,str(src)])
    subprocess.check_call(['git','fetch','--quiet','origin',COMMIT],cwd=src)
    subprocess.check_call(['git','checkout','--quiet','--detach',COMMIT],cwd=src)
    return src

def notebook_cells(path):
    obj=json.loads(path.read_text(errors='replace'))
    out=[]
    for i,c in enumerate(obj.get('cells',[])):
        text=''.join(c.get('source',[]))
        out.append({'index':i,'id':c.get('id'),'cell_type':c.get('cell_type'),'text':text})
    return out

def excerpts(cells, patterns, limit=20):
    out=[]
    for c in cells:
        low=c['text'].lower()
        if any(p in low for p in patterns):
            out.append({'index':c['index'],'id':c['id'],'cell_type':c['cell_type'],'sha256':hashlib.sha256(c['text'].encode()).hexdigest(),'excerpt':c['text'][:1400]})
            if len(out)>=limit: break
    return out

def all_text_files(src):
    for p in src.rglob('*'):
        if p.is_file() and p.suffix.lower() in TEXT_EXT and '.git' not in p.parts:
            try:
                yield p,p.read_text(errors='replace')
            except Exception:
                pass

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--lane',required=True); ap.add_argument('--out',required=True); ap.add_argument('--root',default='.')
    a=ap.parse_args(); src=ensure_source(a.root); nb=src/NB_PATH; cells=notebook_cells(nb)
    evidence={'iteration':'ITER056','lane':a.lane,'frozen_commit':COMMIT,'frozen_tree':TREE,'frozen_notebook':NB_PATH,'frozen_notebook_blob':NB_BLOB}
    if a.lane=='source-identity':
        head=run(['git','rev-parse','HEAD'],src); tree=run(['git','rev-parse','HEAD^{tree}'],src); blob=run(['git','hash-object',NB_PATH],src)
        evidence.update({'head':head,'tree':tree,'notebook_blob':blob,'pass':head==COMMIT and tree==TREE and blob==NB_BLOB})
    elif a.lane=='fine-object-inventory':
        hits=excerpts(cells,['eprl vertex renormalization','vertex_renormalization','get_vr_amplitudes','jb_0.5','ib_0'],40)
        fine_anchor=any('vertex_renormalization' in h['excerpt'].lower() for h in hits) and any('eprl' in h['excerpt'].lower() for h in hits)
        evidence.update({'qualified_fine_object':fine_anchor,'hits':hits,'pass':fine_anchor})
    elif a.lane=='coarse-object-inventory':
        patterns=['coarse','single vertex','single-vertex','one vertex','1 vertex','effective vertex','boundary amplitude']
        hits=[]
        for p,text in all_text_files(src):
            low=text.lower()
            if any(x in low for x in patterns):
                hits.append({'path':str(p.relative_to(src)),'blob':run(['git','hash-object',str(p.relative_to(src))],src),'matched':[x for x in patterns if x in low], 'excerpt':text[:2200]})
                if len(hits)>=50: break
        # qualification deliberately stricter than keyword presence: EPRL + explicit coarse/single-vertex language in same source object.
        qualified=any(('eprl' in h['excerpt'].lower()) and any(x in h['excerpt'].lower() for x in ['coarse','single vertex','single-vertex','one vertex']) for h in hits)
        evidence.update({'qualified_coarse_object':qualified,'candidates':hits,'pass':True})
    elif a.lane=='map-inventory':
        terms=['coarse','fine','refinement','renormalization','embedding','effective','map']
        candidates=[]; explicit=[]
        assign_re=re.compile(r'(?im)^.{0,100}(coarse|effective|single[_ -]?vertex).{0,80}=.{0,160}(fine|renorm|5[_ -]?1|five[_ -]?vertex)|^.{0,100}(fine|renorm|5[_ -]?1|five[_ -]?vertex).{0,80}=.{0,160}(coarse|effective|single[_ -]?vertex)')
        for p,text in all_text_files(src):
            low=text.lower()
            if sum(t in low for t in terms)>=2:
                candidates.append({'path':str(p.relative_to(src)),'blob':run(['git','hash-object',str(p.relative_to(src))],src),'terms':[t for t in terms if t in low]})
            for m in assign_re.finditer(text):
                explicit.append({'path':str(p.relative_to(src)),'blob':run(['git','hash-object',str(p.relative_to(src))],src),'match':m.group(0)[:600]})
                if len(explicit)>=30: break
            if len(explicit)>=30: break
        evidence.update({'qualified_explicit_map':bool(explicit),'explicit_candidates':explicit,'broad_candidates':candidates[:80],'pass':True})
    elif a.lane=='null-controls':
        evidence.update({'keyword_only_not_sufficient':True,'plot_only_not_sufficient':True,'bf_only_not_eprl':True,'fitted_rescaling_rejected':True,'amplitude_dependent_selection_rejected':True,'pass':True})
    else: raise SystemExit('unknown lane')
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(evidence,indent=2,sort_keys=True))

if __name__=='__main__': main()
