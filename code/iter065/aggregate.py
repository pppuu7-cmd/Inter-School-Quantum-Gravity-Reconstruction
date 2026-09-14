#!/usr/bin/env python3
import json
from pathlib import Path

files=sorted(Path('artifacts').rglob('*.json'))
rows=[json.loads(p.read_text()) for p in files]
by_mode={}
for r in rows:
    by_mode.setdefault(r.get('mode','unknown'),[]).append(r)
geom=[]
for m in ('coarse2','fine32'):
    geom.extend(by_mode.get(m,[]))
sources=by_mode.get('source_authority',[])
sentinel=by_mode.get('sentinel',[])
source_ids={r.get('arxiv_id') for r in sources}
frozen={'1508.07961','1605.07649','1701.02311','1804.00023'}
source_complete=(source_ids==frozen and all(r.get('classification')!='INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION' for r in sources))
candidates=[r for r in sources if r.get('classification')=='SOURCE_AUTHORITY_CANDIDATE_PRESENT']
geom_pass=(len(geom)==2 and all(r.get('pass') is True for r in geom))
if not source_complete:
    source_class='INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION'
elif candidates:
    source_class='SOURCE_AUTHORITY_CANDIDATE_PRESENT_REQUIRES_MANUAL_EQUATION_AUDIT'
else:
    source_class='SCOPED_BLOCKED_NO_EXPLICIT_GLOBAL_MEASURE_AUTHORITY'
if not geom_pass:
    overall='NUMERICAL_OR_IMPLEMENTATION_FAIL'
elif source_class.startswith('INFRASTRUCTURE'):
    overall='INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION'
elif source_class.startswith('SOURCE_AUTHORITY_CANDIDATE'):
    overall='MANUAL_SOURCE_EQUATION_AUDIT_REQUIRED'
else:
    overall='SCOPED_BLOCKED_NO_EXPLICIT_GLOBAL_MEASURE_AUTHORITY'
out={
 'iteration':'ITER065',
 'classification':overall,
 'source_classification':source_class,
 'geometric_pullback_diagnostic_pass':geom_pass,
 'source_ids_seen':sorted(x for x in source_ids if x),
 'candidate_source_ids':sorted(r['arxiv_id'] for r in candidates),
 'sentinel_classifications':[r.get('classification') for r in sentinel],
 'gate_credit':False,
 'bridge_credit':False,
 'candidate_theory_authorized':False,
 'claim_lock':'green CI is not scientific PASS; corrected amplitude crossing remains unauthorized until manual source equation audit qualifies a global measure object'
}
Path('aggregate').mkdir(exist_ok=True)
Path('aggregate/summary.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2))
