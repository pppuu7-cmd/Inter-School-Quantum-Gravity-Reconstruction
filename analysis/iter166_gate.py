#!/usr/bin/env python3
import json, pathlib, re
ROOT=pathlib.Path('.')
texts=[]
for p in list(ROOT.glob('analysis/**/*'))+list(ROOT.glob('sources/**/*')):
    if p.is_file() and p.suffix in {'.md','.txt','.json','.py'} and 'ITER166' not in p.name.upper():
        try: texts.append((str(p),p.read_text(errors='ignore')))
        except: pass
patterns={
 'test_function_domain':r'(test[- ]function|Schwartz|compact(?:ly)? supported|C_c\^?infty)',
 'scaling_degree':r'(scaling degree|singular order)',
 'pullback_condition':r'(wavefront|pullback condition|transversality)',
 'local_ambiguity':r'(normal derivative|delta derivative|local ambiguity)'}
hits={k:[p for p,t in texts if re.search(rx,t,re.I)] for k,rx in patterns.items()}
# Presence is authority/navigation only: source-qualified completeness requires an explicit
# sector manifest tying all four objects to the frozen ITER163 ledger.
manifest=[]
for p,t in texts:
    if 'ITER163' in t and all(re.search(patterns[k],t,re.I) for k in patterns): manifest.append(p)
A={'lane':'A_domain_scaling_pullback','authority_hits':{k:len(v) for k,v in hits.items()},'source_qualified_sector_manifest':manifest,'verdict':'PASS_SCOPED' if manifest else 'BLOCKED'}
B={'lane':'B_local_ambiguity','enumeration_authorized':bool(manifest),'reason':'derivative ceiling requires source-qualified sector singular orders','verdict':'PASS_SCOPED' if manifest else 'BLOCKED'}
C={'lane':'C_completeness_falsifier','blocking_witnesses':[] if manifest else ['no single explicit source-qualified ITER163 sector manifest jointly supplies domain, scaling degree, pullback conditions, and local ambiguity ceiling'],'verdict':'PASS_SCOPED' if manifest else 'BLOCKED'}
if manifest: cls='PASS_SCOPED_ITER166_DOMAIN_SCALING_PULLBACK_AND_AMBIGUITY_COMPLETE'
else: cls='BLOCKED_SCOPED_ITER166_DOMAIN_OR_PULLBACK_INCOMPLETE'
out={'iteration':'ITER166','lane_A':A,'lane_B':B,'lane_C':C,'scientific_classification':cls,'bridge_credit':False,'candidate_theory':'UNFORMED'}
pathlib.Path('artifacts').mkdir(exist_ok=True); pathlib.Path('artifacts/iter166_gate.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
