#!/usr/bin/env python3
"""Validate ITER129 graph derivative ceilings."""
from __future__ import annotations
import json
from pathlib import Path

p=Path('analysis/iter129_graph_derivative_ceiling_table.json')
d=json.loads(p.read_text())
rows=d['rows']
assert rows
for r in rows:
    assert r['two_prop_m_raw_ceiling']==4+r['D_total'], r['id']
    if r['affine']:
        assert r['N1_max']==r['D_line_max']+r['D_partner_max'], r['id']
        assert 2+r['N1_max'] >= 3
    else:
        assert r['N1_max'] is None
by={r['id']:r for r in rows}
assert by['M_R2_chi1_dR1']['D_total']==6
assert by['M_R1_chi1_dR1_S3']['D_total']==8
assert by['G_R1_chi2_Gamma1_dchi1_dR1']['line_line_N_max']==2
assert by['G_R1_chi2_dGamma1_chi1_dR1']['line_line_N_max']==3
assert by['G_R1_chi1chi1_d2R1']['N1_max']==5
out=Path('artifacts/iter129'); out.mkdir(parents=True,exist_ok=True)
summary={
 'status':'PASS_GRAPH_DERIVATIVE_CEILING_ARITHMETIC',
 'family_count':len(rows),
 'sector_counts':{s:sum(1 for r in rows if r['sector']==s) for s in ['F','M','G']},
 'max_D_total':max(r['D_total'] for r in rows),
 'max_affine_N1':max(r['N1_max'] or 0 for r in rows),
 'max_two_prop_m_raw_ceiling':max(r['two_prop_m_raw_ceiling'] for r in rows),
 'claim_lock':d['claim_lock'],
}
(out/'validation.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
