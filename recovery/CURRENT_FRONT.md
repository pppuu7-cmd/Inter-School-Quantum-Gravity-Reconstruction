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

Direct DVD2↔DVD3 strict trivial extension remains excluded by run `34710895347`: `DVD23_DIRECT_TRIVIAL_EXTENSION_EXCLUDED`; scoped only to that direct pair.

The one-zero-spin B4 primitive passed in run `34711008648`. Independent asymmetric held-out run `34712687076`, aggregate job `103604345234`, artifact `10303514068`, digest `sha256:b516d16574ee47e016fc4886cf91368c9081492989fe2da2c0c60fae0725e8c6`, passed 5/5 frozen gamma lanes with worst relative error `1.74533e-06 < 1e-5`. Primitive-level zero-spin robustness is saturated unless a new failure mode appears; neither primitive result is a refinement bridge.

DED→DLD source qualification run `34712970339` found candidate context but no explicit injective V/E/F map. Source-vector incidence run `34713333741` remained `DED_DLD_FIGURE_ONLY_REQUIRES_MANUAL_INCIDENCE_AUDIT`, `machine_incidence_ready=false`.

### Terminal dual-representation topology prerequisite

Preregistered run `34715789027` covered DED/DLD × original/GS-eps2write × 300/600 dpi. All eight science lanes completed; its original aggregate failed only because `numpy` was missing. Recovery run `34716846693` reused the immutable artifacts and evaluated them with both the unchanged frozen classifier and an independent bit-count implementation. Both returned:

`TOPOLOGY_EXTRACTION_UNSTABLE`

Cross-representation EPS↔GS thresholds pass, but DPI component-count stability fails. Incidence/embedding, amplitude identity, cylindrical consistency and bridge credit are therefore not authorized.

Localization run `34716979296` narrowed the failure to DED only:
- DED / ORIGINAL_EPS: `121 → 123` components from 300→600 dpi
- DED / GS_EPS2WRITE_NORMALIZED: `121 → 123`
- DLD / ORIGINAL_EPS: `15 → 15`
- DLD / GS_EPS2WRITE_NORMALIZED: `15 → 15`

Follow-up run `34717249322`, aggregate job `103616862737`, artifact `10305175813`, digest `sha256:ddcdf805d87dbe6ab9a1c61bc5a67d44372b84e1773ad7742b8bab50723da92d`, is terminal `DED_EXTRA_600DPI_COMPONENTS_LOCALIZED`. Both original EPS and GS-normalized EPS identify the same two unmatched 600-dpi components: 44 pixels at normalized centroid `(0.189866082925573, 0.5180094786729857)` and 39 pixels at `(0.7200188857412654, 0.8872037914691943)`.

This is a reproducible DED-specific resolution sensitivity. It does **not** establish that those source features are semantically irrelevant, so deleting them or retuning threshold/connectivity/minimum area post hoc is forbidden. The frozen topology prerequisite remains failed.

### DVD23 synthetic structural audit

Run `34715884817` returned workflow label `DVD23_STRUCTURAL_REFINEMENT_MAP_ADMISSIBLE`, but code audit shows that the script constructs its own fine graph by splitting a declared coarse edge. Programme classification remains `SYNTHETIC_STRUCTURAL_SELF_CONSISTENCY_PASS_SOURCE_AUTHORITY_ABSENT`; bridge/refinement credit `0`.

## RC006 source-faithful reconstruction

The relation-aware contraction-serialization retry remains terminal scientific FAIL:
- run `34713459961`, aggregate job `103610235012`
- all 10 lanes valid; full unique = true; holdout unique = `6/8`
- minimum pairwise-order agreement `0.8698752228163993`; unordered null ambiguous = true
- classification `SCIENTIFIC_FAIL_RELATION_AWARE_CONTRACTION_SERIALIZATION_UNSTABLE`.

Per frozen stop rule, no retuned serialization retry is admissible without genuinely new independent source authority.

### Appendix-B Eq. (B13)

After correcting only the wrong pinned source path, run `34716905247` passed frozen `k=6,10,12` mapping with `bad_cases=0`:

`RC006_B13_SOURCE_MAPPING_PASS`

Scope is convention/source-formula mapping against pinned `sixjr()` only; not an EPRL tensor, RG flow, refinement, continuum, bridge or new-physics result.

### Eq. (29) source authority

Dependency closure run `34715908026` remains correctly fail-closed as `EQ29_DEPENDENCY_GRAPH_INCOMPLETE`; source-faithful Eq.(29) semantics, label geometry, R-matrix placement and path incidence must be independently qualified before any literal Eq.(29) tensor implementation.

Manual primary-source inspection of arXiv:1609.02429v2 confirmed that printed Eq.(29) is the initial 3-valent EPRL intertwiner tensor; its surrounding discussion states that `J+` and `J-` couple to `l` without the latter coupling necessarily satisfying the original simplicity constraints, and the source separately defines over/undercrossings through the quantum-group R-matrix and inverse.

Preregistered two-stream run `34717474214` then independently extracted the versioned arXiv source bundle and PDF text and returned:

`EQ29_PRIMARY_SOURCE_EXTRACTION_READY`

Pinned source-bundle SHA256: `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`; sole TeX source file: `bc-spin-nets.tex`. TeX extraction found EPRL/intertwiner/simplicity/R-matrix anchors and PDF text independently confirmed the EPRL-intertwiner section and R-matrix anchor. This is source-discovery authority only; it does not qualify graph incidence or R-matrix placement in Eq.(29).

Active run `34717600962` (`ISQGR Iter006 RC006 Eq29 Exact Source Block`) was preregistered before implementation and has two independent jobs: exact hash-pinned TeX/TikZ extraction anchored by the unique `initial 3-valent tensor` source sentence, and independent source-identity/anchor verification. Even a PASS may only authorize a later prospective geometry/incidence/R-placement audit; Eq.(29) amplitude remains blocked.

## Auto-research state

`ISQGR Автоисследование` is enabled on its hourly schedule. Its prior stale recovery snapshot was caused by the previous auto iteration finishing before run `34715789027` reached terminal state, not by a disabled automation. `recovery/state.json` and this file are now synchronized to the terminal DED/B13/source-extraction results and active run `34717600962`, so the next auto iteration should not repeat the superseded gates.

## Exact next admissible gates

1. Consume run `34717600962`. If the exact Eq.(29) source block is uniquely extracted, preregister a **source-faithful** parser/audit of label geometry, path incidence and R-matrix placement against that immutable block. Do not launch the Eq.(29) amplitude before each required dependency independently passes.
2. For DED/DLD, do not retune the failed raster topology prerequisite. A further attempt is admissible only as a prospectively defined source-semantic/vector-level identification of the two localized DED features, followed by a new independently justified topology representation if warranted.
3. Do not treat synthetic DVD23 self-consistency as a refinement map. A genuine refinement claim still requires source-derived V/E/F incidence preservation.
4. RC008 remains source-only BLOCKED; RC009 remains SCOPED BLOCKED. Do not spend compute on denser RC009 quadrature without a new mathematically justified regularization/measure/contour object.
5. Do not substitute figure complexity, internal-face count, shell depth, finite-cutoff stabilization, raster-threshold retuning or synthetic graph construction for a genuine refinement map.

Latest durable update: `results/ITER006_PARALLEL_PROGRESS_2026-09-12_2037Z.md`.

Iteration completion: **78%**. Amplitude/refinement validation: **46%**. Overall readiness: **49%**. Candidate theory: **0% / UNFORMED**.
