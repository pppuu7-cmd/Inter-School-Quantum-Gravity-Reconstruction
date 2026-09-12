# ITER006 terminal topology / B13 / Eq29 update — 2026-09-12

## 1. DED/DLD dual-representation topology prerequisite

Original run `34715789027` completed all eight science lanes, but its aggregate job failed from missing `numpy`; this was infrastructure-only and did not classify the science lanes.

Recovery run `34716846693` reused the immutable eight artifacts and evaluated them in two independent aggregate paths: (a) the unchanged frozen classifier with the missing dependency installed and (b) an independent pure-Python bit-count cross-check. Both returned the same terminal classification:

`TOPOLOGY_EXTRACTION_UNSTABLE`

All four original-vs-Ghostscript representation comparisons passed the frozen cross-representation thresholds, but DPI component-count stability failed. Therefore no incidence-graph extraction, embedding test, amplitude identity, cylindrical-consistency or bridge credit is authorized from this prerequisite.

Post-failure localization run `34716979296` then showed the instability is confined to DED:

- DED / ORIGINAL_EPS: 121 components at 300 dpi → 123 at 600 dpi (`+2`)
- DED / GS_EPS2WRITE_NORMALIZED: 121 → 123 (`+2`)
- DLD / ORIGINAL_EPS: 15 → 15
- DLD / GS_EPS2WRITE_NORMALIZED: 15 → 15

Classification: `DPI_COMPONENT_COUNT_INSTABILITY_LOCALIZED`. Thresholds and minimum-component-area rule were not changed.

A follow-up diagnostic, run `34717249322`, localizes the two 600-dpi DED component births using the same pixel threshold and minimum-area rule. It is diagnostic-only and cannot retroactively promote the frozen topology gate.

## 2. RC006 Appendix-B Eq. (B13) source mapping

The first B13 recheck failed before mathematics because the workflow addressed the pinned Fusion-basis kernel at the wrong path. The correct pinned path at commit `bb4d1adb1aa81e5090f3ef25a3b9fb8845f19ff4` is `half_int/no_torsion/qgroup_def.jl`.

After fixing only that infrastructure path, run `34716905247` completed the frozen `k = 6, 10, 12` lanes and aggregate with `bad_cases = 0` in all three lanes. Terminal classification:

`RC006_B13_SOURCE_MAPPING_PASS`

This qualifies the convention/source-formula mapping between Appendix-B Eq. (B13) and the pinned `sixjr()` implementation only where the RC006 source graph is explicitly reduced by the paper's identities. It is not an EPRL amplitude, TNR-flow, refinement, continuum, bridge or new-physics result.

## 3. RC006 Eq. (29) dependency closure and source audit

Dependency run `34715908026` correctly failed closed as `EQ29_DEPENDENCY_GRAPH_INCOMPLETE`. At launch, the q-group kernel and B13-mapping files were present, while the following source-faithful ingredients were absent:

- Eq. (29) source semantics
- Eq. (29) label geometry
- Eq. (29) R-matrix/braiding factor
- Eq. (29) path incidence

The primary source, arXiv:1609.02429v2, Sec. VII.B, Eq. (29), has now been manually re-inspected at the PDF level. It explicitly presents the initial 3-valent EPRL intertwiner tensor and its graphical label structure. The surrounding text states that the two representations `J+` and `J-` couple to `l`, and that this latter coupling need not fulfill the original simplicity constraints. Earlier in the same source the quantum-group over/undercrossing convention is related by the R-matrix and inverse R-matrix.

This manual source inspection is **new source authority for semantics**, but it is not yet a machine-qualified Eq. (29) graph/incidence reconstruction. Therefore Eq. (29) amplitude implementation remains blocked pending prospective, source-faithful qualification of graph geometry, R-factor placement and path incidence. No retuned contraction-serialization retry is authorized.

## 4. DVD2→DVD3 synthetic structural gate

Run `34715884817` returned `DVD23_STRUCTURAL_REFINEMENT_MAP_ADMISSIBLE`, but code audit shows the script constructs its own fine graph by splitting a declared coarse internal edge while preserving boundary labels. It therefore checks self-consistency of a synthetic construction rather than extracting a source-derived refinement map.

Programme classification: `SYNTHETIC_STRUCTURAL_SELF_CONSISTENCY_PASS_SOURCE_AUTHORITY_ABSENT`.

Bridge/refinement credit remains `0`; no cylindrical-consistency or amplitude permission is granted.

## Claim lock

Candidate-theory construction remains `0% / UNFORMED`. No result in this update authorizes `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`, RQIR promotion or KMQGB promotion.
