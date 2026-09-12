# ISQGR CURRENT FRONT

Date: 2026-09-12  
Active iteration: `ITERATION_006`  
Iteration completion: **78%**  
Amplitude/refinement cross-realization validation: **46%**  
Overall scientific programme readiness: **49%**  
Candidate-theory construction: **0% — UNFORMED / constitutionally locked**

## Preserved blockers and claim locks

RC008 remains source-only BLOCKED. RC009 remains `SCOPED BLOCKED`. Lorentzian Delta4 finite-cutoff/profile/scaling remains `SATURATED NEGATIVE/SCOPED` with no bridge credit. Generic projector/orientation/envelope structure remains absorbed by standard amplitude-level TNR.

`ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, candidate action/Hamiltonian/field equations and RQIR/KMQGB promotion remain forbidden.

## Lorentzian zero-spin/refinement chain

Pinned DVD source: arXiv:1801.03771. Pinned numerical kernel: `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

Direct DVD2↔DVD3 strict trivial extension remains excluded by run `34710895347`: `DVD23_DIRECT_TRIVIAL_EXTENSION_EXCLUDED`; this is scoped only to that direct pair.

The one-zero-spin B4 primitive passed in run `34711008648`. Independent asymmetric held-out run `34712687076`, aggregate job `103604345234`, artifact `10303514068`, digest `sha256:b516d16574ee47e016fc4886cf91368c9081492989fe2da2c0c60fae0725e8c6`, passed 5/5 frozen gamma lanes with worst relative error `1.74533e-06 < 1e-5`. Classification `B4_ZERO_SPIN_ASYMMETRIC_HELDOUT_PASS`. Primitive-level zero-spin robustness is saturated unless a new failure mode appears; neither primitive result is a refinement bridge.

DED→DLD source qualification run `34712970339` found candidate source context but no explicit injective V/E/F map. Source-vector incidence audit run `34713333741` was terminal `DED_DLD_FIGURE_ONLY_REQUIRES_MANUAL_INCIDENCE_AUDIT`, `machine_incidence_ready=false`; no strict refinement promotion or amplitude identity was authorized.

### Terminal dual-representation topology prerequisite

The preregistered dual-representation EPS topology experiment used DED/DLD × original/GS-eps2write × 300/600 dpi, with prereg commit `b2c34a7f5516ee61c77b5447a3b7edff168b5857`, launch commit `c82fa1c8e3101fa0a917c1a34e37cf27c36bc558`, run `34715789027`.

All eight science lanes completed. The original aggregate failed only because `numpy` was missing. Recovery run `34716846693` reused those immutable artifacts and evaluated them via both the unchanged frozen classifier and an independent pure-Python bit-count cross-check. Both returned:

`TOPOLOGY_EXTRACTION_UNSTABLE`

All four original-vs-Ghostscript comparisons pass the frozen representation thresholds, but DPI component-count stability fails. Therefore the preregistered condition required to proceed to incidence/embedding did **not** pass. No incidence extraction, amplitude identity, cylindrical consistency or bridge credit is authorized from this gate.

Localization run `34716979296` is terminal `DPI_COMPONENT_COUNT_INSTABILITY_LOCALIZED`:
- DED / ORIGINAL_EPS: `121 → 123` components from 300→600 dpi
- DED / GS_EPS2WRITE_NORMALIZED: `121 → 123`
- DLD / ORIGINAL_EPS: `15 → 15`
- DLD / GS_EPS2WRITE_NORMALIZED: `15 → 15`

Thus the instability is DED-specific and representation-independent. No threshold or minimum-area retuning is admissible as a way to convert the failed frozen gate into a PASS.

Follow-up run `34717249322` is active to localize the two 600-dpi DED component births under the unchanged extraction rule. It is diagnostic-only and cannot grant bridge credit or retroactively promote the topology prerequisite.

### DVD23 synthetic structural audit

Run `34715884817` returned `DVD23_STRUCTURAL_REFINEMENT_MAP_ADMISSIBLE`, but code audit shows the test itself constructs the fine graph by splitting the declared coarse edge `int01 → int0m,intm1` while preserving the boundary. It is therefore a synthetic self-consistency test, not a source-derived DVD2→DVD3 refinement map.

Programme classification: `SYNTHETIC_STRUCTURAL_SELF_CONSISTENCY_PASS_SOURCE_AUTHORITY_ABSENT`; bridge/refinement credit `0`; no cylindrical-consistency/amplitude permission.

## RC006 source-faithful reconstruction

The relation-aware contraction-serialization retry remains terminal scientific FAIL:
- run `34713459961`, aggregate job `103610235012`
- all 10 lanes valid; full unique = true; holdout unique = `6/8`
- minimum pairwise-order agreement `0.8698752228163993`; unordered null ambiguous = true
- classification `SCIENTIFIC_FAIL_RELATION_AWARE_CONTRACTION_SERIALIZATION_UNSTABLE`.

Per frozen stop rule, the minimal Eq.(29) amplitude remains BLOCKED absent genuinely new independent source authority. No immediate retuned serialization retry is admissible.

### Appendix-B Eq. (B13) source mapping

The first B13 recheck failed before mathematics because the pinned kernel path was wrong. Only that infrastructure path was corrected to `half_int/no_torsion/qgroup_def.jl` at pinned Fusion-basis commit `bb4d1adb1aa81e5090f3ef25a3b9fb8845f19ff4`.

Run `34716905247` then passed all frozen `k=6,10,12` lanes and aggregate with `bad_cases=0`, terminal classification:

`RC006_B13_SOURCE_MAPPING_PASS`

This qualifies only the convention/source-formula mapping between Appendix-B Eq. (B13) and pinned `sixjr()` where the RC006 source graph is explicitly reduced by the source identities. It is not an EPRL tensor, RG-flow, refinement, continuum, bridge or new-physics result.

### Eq. (29) dependency and source authority

Dependency closure run `34715908026` correctly failed closed as `EQ29_DEPENDENCY_GRAPH_INCOMPLETE`. The q-group kernel and B13 mapping exist; source-faithful Eq.(29) semantics, label geometry, R-matrix-factor placement and path incidence still require independent qualification before any literal Eq.(29) tensor implementation.

A new manual primary-source inspection of arXiv:1609.02429v2, Sec. VII.B, Eq. (29), confirms source semantics: the equation is the initial 3-valent EPRL intertwiner tensor; its diagram couples `J+` and `J-` to `l`, and the surrounding text explicitly notes that this latter coupling need not satisfy the original simplicity constraints. The same source earlier defines over/undercrossing through the quantum-group R-matrix and its inverse. This is genuinely useful source authority for semantics, but **not yet** a machine-qualified graph/incidence reconstruction.

## Exact next admissible gates

1. Consume run `34717249322` and identify the two DED components responsible for the DPI birth. Treat it as failure localization only; do not retune the frozen topology gate.
2. RC006: use the newly inspected primary source to prospectively qualify Eq.(29) source semantics, label geometry, R-factor placement and path incidence as separate claim-locked objects. Do not launch the Eq.(29) amplitude until all required source-faithful dependencies have their own terminal PASS.
3. Do not treat the synthetic DVD23 self-consistency gate as a refinement map. A true refinement claim still requires source-derived V/E/F incidence preservation.
4. RC008 remains source-only BLOCKED; RC009 remains SCOPED BLOCKED. Do not spend compute on denser RC009 quadrature without a new mathematically justified regularization/measure/contour object.
5. Do not substitute figure complexity, internal-face count, shell depth, finite-cutoff stabilization, raster threshold retuning, or synthetic graph construction for a genuine refinement map.

Authoritative update: `results/ITER006_TERMINAL_TOPOLOGY_B13_EQ29_UPDATE_2026-09-12.md`.

Iteration completion: **78%**. Amplitude/refinement validation: **46%**. Overall readiness: **49%**. Candidate theory: **0% / UNFORMED**.
