#!/usr/bin/env python3
import json
from pathlib import Path
p=Path('iter154b_primitive_bubble_proper_subgraph_r_operation.json')
d=json.loads(p.read_text())
rows=d['records']
checks={
 'A_three_records':len(rows)==3,
 'B_whole_loop_rank_one':all(r['operator_loop_core']=={'V_eff':2,'E':2,'C':1,'b1':1,'edges':['e1','e2']} for r in rows),
 'C_each_has_two_one_edge_proper_subgraphs':all(len(r['strict_proper_nonempty_edge_subgraphs'])==2 and all(s['E']==1 and s['b1']==0 for s in r['strict_proper_nonempty_edge_subgraphs']) for r in rows),
 'D_no_nested_insertions':all(not r['same_site_self_pairing'] and not r['action_or_ghost_insertion'] for r in rows),
 'E_independent_pinch_route':all(r['method_B']['denominator_count']==2 and r['method_B']['independent_loop_momenta']==1 and r['method_B']['pinch_either_edge_breaks_closed_bubble'] and not r['method_B']['nested_loop_denominator_subset'] for r in rows),
 'F_endpoint_not_erased':d['endpoint_renormalization_still_open'] is True and all(r['frozen_endpoint_strata'] for r in rows),
 'G_zero_scope_narrow':'strict proper ordinary bulk/local-composite subdivergence' in d['derived_zero'],
 'H_no_claim_leak':'contact zero' in d['claim_ceiling'] and 'B1_total' in d['claim_ceiling']
}
cls='PASS_CRITIC_ITER154B_PRIMITIVE_BUBBLE_SUBDIVIDENCE_ZERO_SOUND' if all(checks.values()) else 'FAIL_CRITIC_ITER154B'
out={'critic':'ITER154B_PRIMITIVE_BUBBLE_CRITIC','classification':cls,'checks':checks,'conclusion':'Whole cores are one-loop bubbles, but every strict proper nonempty edge subset breaks the loop. Scoped slot-6 proper-subdivergence forest is empty; endpoint renormalization remains open.' if all(checks.values()) else 'repair required'}
Path('iter154b_adversarial_critic.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if not all(checks.values()): raise SystemExit(1)
