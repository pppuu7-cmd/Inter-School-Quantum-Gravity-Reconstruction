# ITER035 preregistration — RC006 indexed simplicity-map source authority

Date: 2026-09-14
Status: `PREREGISTERED_NOT_EXECUTED`.

## Authorization basis

ITER034 terminalized `BLOCKED — RC006_EQ27_SOURCE_LABEL_DOMAIN_BLOCKED`. The blocker is narrow: `j^+_2,j^-_1,j^+_1,j^-_2` occur explicitly in Eq.(27), but the current validated RC006 authority set does not yet contain an accepted explicit domain/map sufficient to instantiate them without inference.

ITER035 is a source-internal authority discovery gate. It searches the exact byte-pinned arXiv:1609.02429v2 source outside Eq.(29)/Lambda for a definition of the EPRL/q-deformed simplicity map and the allowed representation domains of the indexed plus/minus labels. It does not evaluate Eq.(27), does not fit labels to output, and does not import Eq.(29)/Lambda.

## Frozen source and exclusions

Exact archive SHA256 must remain `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.
The source file containing Eq.(27) is mechanically identified by the existing ITER030 provenance loader. All searches use that exact source archive.

Excluded from positive authority:
- the Eq.(29) display and any definition whose only support is Eq.(29)/Lambda;
- repository-derived fitted numerical relations;
- lexical co-occurrence of `j^+`,`j^-`,`l` without an explicit equality/map/admissibility/domain statement;
- post-result selection among competing map conventions.

## Four independent lanes (`fail-fast:false`)

### Lane A — simplicity-map definition inventory
Search the exact source text for explicit statements/equations relating an undeformed/EPRL label (`l`, `j`, or the paper's source label for the incoming representation) to a pair `(j^+,j^-)`, including gamma/k dependence if present. Record every matching source context and its equation/section neighborhood. PASS requires at least one explicit source relation or map outside Eq.(29)/Lambda; otherwise BLOCKED.

### Lane B — indexed-label inheritance
Determine syntactically whether indexed labels `j_i^+`,`j_i^-` used in/around Eq.(27) are explicitly declared as instances of the same simplicity-map representation labels identified in Lane A (e.g. by a general indexed definition, edge/leg statement, or repeated mapped pair notation). PASS requires explicit source text/equation support; notation similarity alone is insufficient.

### Lane C — representation/admissibility domain
Search exact source material for the allowed finite-level representation range/admissibility relevant to the plus/minus labels and internal coupled `j`, sufficient to enumerate a bounded sum domain at a given k without post-hoc truncation. PASS requires an explicit finite-level/domain/admissibility rule in the source or an already source-pinned appendix definition contained in the same exact archive.

### Lane D — provenance/null controls
Require exact archive hash and reject 3/3 predetermined false authorities: (1) lexical-only `j^+,j^-` occurrence; (2) a fabricated `j^+=j^-` equality; (3) an Eq.(29)/Lambda-only relation. PASS requires all 3 rejected.

## Aggregate classes

`RC006_INDEXED_SIMPLICITY_MAP_SOURCE_AUTHORITY_PASS`: A-D all PASS. This authorizes only a separately preregistered bounded source-label instantiation/consistency gate before numerical Eq.(27) summation.

`RC006_INDEXED_SIMPLICITY_MAP_SOURCE_AUTHORITY_BLOCKED`: any substantive authority lane A-C lacks explicit source support while provenance is valid. This preserves ITER031-033 PASS results and ITER034 BLOCKED; it does not count as scientific failure of RC006.

`NUMERICAL_OR_INFRASTRUCTURE_FAIL_PRE_SCIENCE`: source transport/hash/parser/artifact failure.

## Claim locks

Always false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.

Candidate theory remains `UNFORMED / 0%`; overall roadmap readiness remains 49%.