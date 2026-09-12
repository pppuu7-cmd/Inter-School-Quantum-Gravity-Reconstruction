#!/usr/bin/env python3
"""Independent prospective TeX source-structure audit for RC006 Eq.(29).

This is deliberately a different object from the failed lexical Appendix-F /
crossing audit. It parses source-file include topology and structural TeX objects
(labels, refs, headings, graphics) without weakening or rerunning the failed
lexical thresholds. PASS only means that the requested structural object is
machine-readable and source-connected; it does not assert a unique Eq.(29)
contraction or authorize amplitudes.
"""
from pathlib import Path
import argparse, hashlib, json, re

ANCHOR='Before we discuss the behaviour of the EPRL model under coarse graining'
ROLES=('include_graph','heading_graph','label_ref_graph','graphic_graph','eq29_component','recoupling_component')

def norm_target(raw):
    raw=raw.strip().replace('\\','/')
    return raw if raw.endswith('.tex') else raw+'.tex'

def h(s): return hashlib.sha256(s.encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',required=True); ap.add_argument('--role',choices=ROLES,required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
    root=Path(a.source_dir)
    tex={str(p.relative_to(root)).replace('\\','/'):p.read_text(errors='ignore') for p in root.rglob('*.tex')}
    includes=[]; headings=[]; labels=[]; refs=[]; graphics=[]
    eq29_files=[]; rec_files=[]
    for f,t in tex.items():
        if ANCHOR.lower() in t.lower(): eq29_files.append(f)
        if re.search(r'6j|six[- ]?j|recoupl',t,re.I): rec_files.append(f)
        for m in re.finditer(r'\\(?:input|include)\s*\{([^}]+)\}',t): includes.append((f,norm_target(m.group(1))))
        for m in re.finditer(r'\\(?:part|chapter|section|subsection|subsubsection)\*?\s*\{([^}]*)\}',t): headings.append((f,' '.join(m.group(1).split())))
        for m in re.finditer(r'\\label\s*\{([^}]+)\}',t): labels.append((f,m.group(1)))
        for m in re.finditer(r'\\(?:ref|eqref|autoref)\s*\{([^}]+)\}',t): refs.append((f,m.group(1)))
        for m in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\s*\{([^}]+)\}',t): graphics.append((f,m.group(1)))
    label_names={x[1] for x in labels}; resolved_refs=[r for r in refs if r[1] in label_names]
    include_sources={x[0] for x in includes}; include_targets={x[1] for x in includes}
    if a.role=='include_graph':
        metrics={'node_count':len(tex),'edge_count':len(includes),'source_count':len(include_sources),'target_count':len(include_targets)}
        ok=len(tex)>0 and len(includes)>0
    elif a.role=='heading_graph':
        metrics={'heading_count':len(headings),'files_with_headings':len({x[0] for x in headings})}
        ok=len(headings)>=3
    elif a.role=='label_ref_graph':
        metrics={'label_count':len(labels),'ref_count':len(refs),'resolved_ref_count':len(resolved_refs),'resolved_fraction':len(resolved_refs)/max(1,len(refs))}
        ok=len(labels)>0 and len(refs)>0 and len(resolved_refs)>0
    elif a.role=='graphic_graph':
        metrics={'graphic_count':len(graphics),'files_with_graphics':len({x[0] for x in graphics})}
        ok=len(graphics)>0
    elif a.role=='eq29_component':
        related_refs=[r for r in refs if r[0] in eq29_files and r[1] in label_names]
        metrics={'eq29_file_count':len(eq29_files),'eq29_files':eq29_files,'resolved_refs_from_eq29_files':len(related_refs)}
        ok=len(eq29_files)>=1 and len(related_refs)>=1
    else:
        rec_labels=[l for l in labels if l[0] in rec_files]; rec_refs=[r for r in refs if r[0] in rec_files and r[1] in label_names]
        metrics={'recoupling_file_count':len(rec_files),'recoupling_files':rec_files,'labels_in_recoupling_files':len(rec_labels),'resolved_refs_in_recoupling_files':len(rec_refs)}
        ok=len(rec_files)>=1 and (len(rec_labels)+len(rec_refs))>=1
    out={'test':'RC006_TEX_SOURCE_STRUCTURE_AUDIT','role':a.role,'source':'official arXiv 1609.02429 source archive','tex_file_count':len(tex),'metrics':metrics,'frozen_gate_pass':bool(ok),'classification_if_pass':'PASS_MACHINE_READABLE_SOURCE_STRUCTURE_OBJECT_ONLY','claim_lock':'Independent structural diagnostic; does not relax failed lexical gate, infer picture geometry, establish unique Eq29 contraction, compute amplitude, or derive bridge.'}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not ok: raise SystemExit(2)
if __name__=='__main__': main()
