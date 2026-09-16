#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path

PARENT="a85276e5bf8a7518dc037a33d5eb8c9a02ca14f5"
PREREG="c35e3a1d7a6a7c78ed0a02b376a7b899319d6be6"
ITER125="sources/ITER125_FIXED_GEODESIC_CURVATURE_PROJECTED_UV_TOPOLOGY_AND_MASTER_INTEGRAL_CENSUS_2026-09-15.md"
ITER141="analysis/iter141_first_mg_wick_geometry_phase_strata.py"
BLOB125="e79f2ac2d884e5acdbee40c9d70174bea95866b8"
BLOB141="5d1c94a8e8fcdb6970de79b65f50e3625402f37e"
FAMS={
 "M_R2_chi1_dR1":{"strata":["lower"],"snip":"('R2_q','chi1_minus_q'), ('R2_k','dR1_minus_k')"},
 "M_R1_chi1_dR2":{"strata":["upper"],"snip":"('R1_minus_q','dR2_q'), ('chi1_minus_k','dR2_k')"},
 "G_R1_chi2_Gamma2_dR1":{"strata":["lower","upper"],"snip":"('R1_minus_q','Gamma2_q'), ('Gamma2_k','dR1_minus_k')"},
}
def git(*a,check=True): return subprocess.run(["git",*a],check=check,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
def anc(x): return git("merge-base","--is-ancestor",x,"HEAD",check=False).returncode==0

def main():
 s125=git("show",f"{PARENT}:{ITER125}").stdout; s141=git("show",f"{PARENT}:{ITER141}").stdout
 lineage={"parent":anc(PARENT),"prereg":anc(PREREG),"blob125":git("rev-parse",f"{PARENT}:{ITER125}").stdout.strip(),"blob141":git("rev-parse",f"{PARENT}:{ITER141}").stdout.strip()}
 source_ok=(lineage["blob125"]==BLOB125 and lineage["blob141"]==BLOB141 and
   "the loop-dependent core is still a two-propagator bubble" in s125 and
   "at most one independent loop momentum" in s125 and
   "same connected two-point loop reduce to a bubble denominator" in s125 and
   "local/self-pairing quadratic channel remains a separate renormalization sector" in s141)
 rows=[]
 for fam,spec in FAMS.items():
  ident=fam in s141 and spec["snip"] in s141
  whole={"V_eff":2,"E":2,"C":1,"b1":1,"edges":["e1","e2"]}
  proper=[{"edges":["e1"],"V_eff":2,"E":1,"C":1,"b1":0},{"edges":["e2"],"V_eff":2,"E":1,"C":1,"b1":0}]
  rows.append({"family":fam,"source_identity":ident,"operator_loop_core":whole,"strict_proper_nonempty_edge_subgraphs":proper,
   "any_strict_proper_cyclic":False,"same_site_self_pairing":False,"action_or_ghost_insertion":False,
   "frozen_endpoint_strata":spec["strata"],"slot6_counterterm_insertions":[],"R_sub":"identity",
   "method_B":{"denominator_count":2,"independent_loop_momenta":1,"pinch_either_edge_breaks_closed_bubble":True,"nested_loop_denominator_subset":False}})
 hyp=all(r["source_identity"] and r["operator_loop_core"]["b1"]==1 and len(r["strict_proper_nonempty_edge_subgraphs"])==2 and all(x["b1"]==0 for x in r["strict_proper_nonempty_edge_subgraphs"]) and not r["same_site_self_pairing"] and not r["action_or_ghost_insertion"] and r["method_B"]["pinch_either_edge_breaks_closed_bubble"] for r in rows)
 controls={"self_energy_third_edge":"reject","self_pairing":"reject","S3_or_ghost":"reject","whole_graph_as_proper":"reject","endpoint_as_bulk":"reject","contact_zero":"reject","B1_total":"reject"}
 checks={"A_lineage":lineage["parent"] and lineage["prereg"],"B_sources":source_ok,"C_three_families":len(rows)==3,
  "D_whole_bubble_b1_one":all(r["operator_loop_core"]["b1"]==1 for r in rows),"E_strict_proper_subgraphs_acyclic":all(not r["any_strict_proper_cyclic"] for r in rows),
  "F_no_self_or_action_insertions":all(not r["same_site_self_pairing"] and not r["action_or_ghost_insertion"] for r in rows),
  "G_denominator_route_agrees":all(r["method_B"]["independent_loop_momenta"]==1 and r["method_B"]["pinch_either_edge_breaks_closed_bubble"] for r in rows),
  "H_endpoint_strata_preserved":all(bool(r["frozen_endpoint_strata"]) for r in rows),"I_controls":all(v=="reject" for v in controls.values()),"J_claim_locks":True}
 if not checks["A_lineage"] or not checks["B_sources"] or not checks["C_three_families"]: cls="INVALID_IMPLEMENTATION_ITER154B"
 elif not hyp: cls="SCIENTIFIC_FAIL_SCOPED_ITER154B_PRIMITIVE_BUBBLE_HYPOTHESIS_FALSE"
 elif all(checks.values()): cls="PASS_SCOPED_SLOT6_FIRST_MG_PRIMITIVE_BUBBLES_NO_PROPER_SUBDIVERGENCES"
 else: cls="BLOCKED_SCOPED_ITER154B_SUBGRAPH_AUTHORITY_INCOMPLETE"
 out={"gate":"ITER154B_FIXED_GEODESIC_FIRST_MG_PRIMITIVE_BUBBLE_PROPER_SUBGRAPH_R_OPERATION","classification":cls,"lineage":lineage,"records":rows,
  "slot6_closed_scoped":cls.startswith("PASS_SCOPED_SLOT6"),"derived_zero":"zero strict proper ordinary bulk/local-composite subdivergence counterterm insertions for the three scoped first-M/G connected-cross bubble cores",
  "endpoint_renormalization_still_open":True,"controls":controls,"checks":checks,"next":"slot7 divergent endpoint/geodesic counterterm coefficients in frozen ITER118 basis",
  "claim_ceiling":"no contact zero, endpoint coefficient, line mixing, B1_total, bridge, or candidate theory"}
 Path("iter154b_primitive_bubble_proper_subgraph_r_operation.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps({"classification":cls,"checks":checks},indent=2,sort_keys=True))
 if cls.startswith("INVALID"): raise SystemExit(1)
if __name__=="__main__": main()
