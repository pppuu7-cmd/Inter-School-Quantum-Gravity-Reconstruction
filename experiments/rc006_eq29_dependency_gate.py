#!/usr/bin/env python3
"""Source-faithful dependency gate for RC006 Eq.29 reconstruction.

The gate records which independently qualified ingredients are available before
we are allowed to call an implementation 'Eq29'.  It intentionally refuses to
promote a tensor unless the source graph, label geometry, recoupling map and
R-matrix/braiding factors are all explicitly pinned.
"""
import json, pathlib
required = {
  "qgroup_recoupling_kernel":"results/ITER006_RC006_QGROUP_KERNEL_QUALIFICATION.md",
  "eq29_source_semantics":"experiments/rc006_eq29_source_semantics.py",
  "eq29_label_geometry":"experiments/rc006_eq29_label_geometry.py",
  "eq29_rmatrix_factor":"experiments/rc006_eq29_rmatrix_factor.py",
  "eq29_path_incidence":"experiments/rc006_eq29_path_incidence.py",
  "appendix_b13_mapping":"experiments/rc006_b13_sixjr_source_mapping.jl"
}
present={k:pathlib.Path(v).exists() for k,v in required.items()}
all_present=all(present.values())
out={
  "test":"RC006_EQ29_SOURCE_DEPENDENCY_CLOSURE",
  "required":required,
  "present":present,
  "all_present":all_present,
  "classification":"EQ29_DEPENDENCY_GRAPH_PRESENT" if all_present else "EQ29_DEPENDENCY_GRAPH_INCOMPLETE",
  "permission_if_pass":"Proceed to a literal Eq29 tensor implementation only after each listed ingredient also has its own terminal source-faithful PASS; file presence alone is not physics validation.",
  "claim_lock":"No EPRL tensor reproduction, TNR flow, refinement or new-physics claim from this bookkeeping gate."
}
print(json.dumps(out,indent=2,sort_keys=True))
open('rc006_eq29_dependency_gate.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
raise SystemExit(0 if all_present else 2)
