#!/usr/bin/env python3
"""Prospective internal label/reference-chain audit for monolithic RC006 source.

The preceding independent source-structure audit established that arXiv 1609.02429
is a monolithic TeX source with a machine-readable internal label/reference graph.
This gate uses that qualified object. It does not relax failed lexical gates and
never infers edges from figure geometry.
"""
from pathlib import Path
import argparse,json,re,hashlib

ANCHOR='Before we discuss the behaviour of the EPRL model under coarse graining'
ROLES=('eq29_local_refs','recoupling_local_labels','eq29_figure_links','eq29_equation_links','recoupling_equation_links','shared_reference_component')

def line(t,p): return t.count('\n',0,p)+1

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--role',choices=ROLES,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    files=list(Path(a.source_dir).rglob('*.tex'))
    if len(files)!=1: raise SystemExit('qualified monolithic-source precondition failed')
    p=files[0]; t=p.read_text(errors='ignore')
    q=t.lower().find(ANCHOR.lower())
    if q<0: raise SystemExit('Eq29 anchor missing')
    qline=line(t,q)
    labels=[]; refs=[]; graphics=[]
    for m in re.finditer(r'\\label\s*\{([^}]+)\}',t): labels.append({'name':m.group(1),'line':line(t,m.start())})
    for m in re.finditer(r'\\(ref|eqref|autoref)\s*\{([^}]+)\}',t): refs.append({'kind':m.group(1),'name':m.group(2),'line':line(t,m.start())})
    for m in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\s*\{([^}]+)\}',t): graphics.append({'target':m.group(1),'line':line(t,m.start())})
    label_names={x['name'] for x in labels}
    # independently freeze local source windows around Eq29 and all recoupling/6j tokens
    eqwin=(qline-220,qline+220)
    rec_lines=[line(t,m.start()) for m in re.finditer(r'6j|six[- ]?j|recoupl',t,re.I)]
    def near_any(x,lines,r=180): return any(abs(x-y)<=r for y in lines)
    if a.role=='eq29_local_refs':
        xs=[r for r in refs if eqwin[0]<=r['line']<=eqwin[1] and r['name'] in label_names]
        metrics={'eq29_anchor_line':qline,'resolved_local_ref_count':len(xs),'sample':xs[:25]}; ok=len(xs)>=1
    elif a.role=='recoupling_local_labels':
        xs=[l for l in labels if near_any(l['line'],rec_lines)]
        metrics={'recoupling_token_count':len(rec_lines),'nearby_label_count':len(xs),'sample':xs[:25]}; ok=len(rec_lines)>=1 and len(xs)>=1
    elif a.role=='eq29_figure_links':
        local_graphics=[g for g in graphics if eqwin[0]<=g['line']<=eqwin[1]]
        figrefs=[r for r in refs if eqwin[0]<=r['line']<=eqwin[1] and re.search(r'fig|diagram|graph',r['name'],re.I)]
        metrics={'local_graphic_count':len(local_graphics),'local_figure_ref_count':len(figrefs),'graphics':local_graphics[:20],'figure_refs':figrefs[:20]}; ok=(len(local_graphics)+len(figrefs))>=1
    elif a.role=='eq29_equation_links':
        xs=[r for r in refs if eqwin[0]<=r['line']<=eqwin[1] and r['kind']=='eqref' and r['name'] in label_names]
        metrics={'resolved_eqrefs_near_eq29':len(xs),'sample':xs[:25]}; ok=len(xs)>=1
    elif a.role=='recoupling_equation_links':
        xs=[r for r in refs if r['kind']=='eqref' and r['name'] in label_names and near_any(r['line'],rec_lines)]
        metrics={'resolved_eqrefs_near_recoupling':len(xs),'sample':xs[:25]}; ok=len(xs)>=1
    else:
        eqnames={r['name'] for r in refs if eqwin[0]<=r['line']<=eqwin[1] and r['name'] in label_names}
        recnames={r['name'] for r in refs if r['name'] in label_names and near_any(r['line'],rec_lines)} | {l['name'] for l in labels if near_any(l['line'],rec_lines)}
        shared=sorted(eqnames & recnames)
        metrics={'eq29_reference_names':sorted(eqnames),'recoupling_reference_or_label_names':sorted(recnames),'shared_names':shared,'shared_count':len(shared)}
        ok=len(eqnames)>=1 and len(recnames)>=1 and len(shared)>=1
    out={'test':'RC006_EQ29_INTERNAL_REFERENCE_CHAIN_AUDIT','role':a.role,'source':'official arXiv 1609.02429 monolithic TeX source','metrics':metrics,'frozen_gate_pass':bool(ok),'classification_if_pass':'PASS_INTERNAL_SOURCE_REFERENCE_CHAIN_OBJECT_ONLY','claim_lock':'No relaxed lexical gate, no figure-geometry inference, no unique contraction or Eq29 amplitude, no bridge/candidate-theory claim.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()
