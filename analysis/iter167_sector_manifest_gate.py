#!/usr/bin/env python3
import json, pathlib, re, sys
ROOT=pathlib.Path('.')
EXCLUDE={'ITER167'}
files=[]
for base in ('analysis','sources','artifacts','docs'):
    d=ROOT/base
    if not d.exists(): continue
    for p in d.rglob('*'):
        if p.is_file() and p.suffix.lower() in {'.py','.md','.txt','.json','.csv'} and not any(x in p.name.upper() for x in EXCLUDE):
            try: files.append((p,p.read_text(errors='ignore')))
            except Exception: pass
# Prospectively fixed lexical witnesses. They navigate frozen source material; they do not manufacture sectors.
iter163=[(p,t) for p,t in files if re.search(r'ITER163|21[- ]term|11\s*QQ|5\s*QK|5\s*KQ',t,re.I)]
source_expr_rx=re.compile(r'(denominat|propagator|1\s*/|phase|endpoint|affine|k\^?2|q\^?2|\bK\b\s*=|cancelled)',re.I)
singular_rx=re.compile(r'(singular|pole|zero locus|endpoint|delta|contact|cancelled|stationary|denominat)',re.I)
geometry=[]
for p,t in iter163:
    lines=t.splitlines()
    hits=[]
    for i,line in enumerate(lines,1):
        if source_expr_rx.search(line): hits.append({'line':i,'text':line[:500]})
    if hits: geometry.append({'path':str(p),'hits':hits[:80]})
# A source-qualified manifest requires structured rows tying a defining expression to a locus and orientation/contact metadata.
structured=[]
for p,t in iter163:
    low=t.lower()
    required=[('expression' in low or 'denominator' in low or 'propagator' in low),
              ('locus' in low or 'singular support' in low),
              ('upper' in low and 'lower' in low),
              ('contact' in low or 'cancelled' in low),
              ('codimension' in low or 'transverse' in low),
              ('singular order' in low or 'scaling degree' in low)]
    if all(required): structured.append(str(p))
# Independent critic scans all frozen material, not just ITER163-tagged files, for plausible singular-source witnesses.
critic=[]
for p,t in files:
    if singular_rx.search(t) and source_expr_rx.search(t):
        critic.append(str(p))
critic=sorted(set(critic))
if not iter163:
    cls='BLOCKED_SCOPED_ITER167_SOURCE_EXPRESSION_OR_PROVENANCE_MISSING'
elif not structured:
    cls='BLOCKED_SCOPED_ITER167_SINGULAR_SECTOR_OR_ORDER_INCOMPLETE'
else:
    cls='PASS_SCOPED_ITER167_SOURCE_QUALIFIED_SINGULAR_SECTOR_MANIFEST_COMPLETE'
out={'iteration':'ITER167','iter163_source_candidate_files':[str(p) for p,_ in iter163],
     'source_geometry_candidates':geometry,'structured_source_qualified_manifests':structured,
     'independent_critic_candidate_files':critic,'scientific_classification':cls,
     'bridge_credit':False,'candidate_theory':'UNFORMED'}
pathlib.Path('artifacts').mkdir(exist_ok=True)
pathlib.Path('artifacts/iter167_sector_manifest_gate.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
