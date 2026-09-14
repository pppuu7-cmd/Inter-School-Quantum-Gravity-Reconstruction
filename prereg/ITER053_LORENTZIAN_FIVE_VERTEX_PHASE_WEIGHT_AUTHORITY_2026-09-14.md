# ITER053 preregistration — Lorentzian five-vertex phase/weight authority

Date: 2026-09-14

## Scientific question

Before any repaired bounded five-vertex Lorentzian contraction, determine whether the exact paper/source and the pinned authors' executable implementation uniquely fix the total sign/phase and face-weight convention required for the fixed-summand 5→1 amplitude.

This is an authority/translation gate only. No Lorentzian amplitude value may be computed, fitted, inspected, or used to choose a convention.

## Frozen upstream authority

- exact arXiv source: `arXiv:2302.00072`, exact `main.tex` SHA256 `bff93f3a7857658264a04eb23521bb935a68eccb7760b284589ff5ec4073f063`;
- pinned authors' code: `PietropaoloFrisoni/Monte_Carlo_spinfoams@84b375f2a2e0d29b44dd8820953553624bb007a3`, file `src/vertex_renormalization_EPRL_MC.jl`;
- ITER051 runtime PASS remains runtime-only;
- ITER052 local-vertex argument crosswalk PASS is authoritative for local argument ordering;
- ITER048 remains BLOCKED and is not retrofitted; ITER049 remains PASS only in its routing-reconciliation scope.

## Frozen lanes

Run independently with `fail-fast:false`.

1. `tex-phase-weight`
   - obtain exact arXiv source and verify the frozen `main.tex` SHA256;
   - locate Eq.(11)'s global `(-1)^chi` factor, internal-face factors, intertwiner-dimension factors, and the source's explicit reduction/definition of `chi` if present;
   - record exact source tokens only; no inferred repair.

2. `author-code-phase`
   - verify the pinned author-code commit/file;
   - qualify `dfj`, `df_phase`, the five local sign factors multiplying the five pre-contracted vertices, and the final multiplication by `dfj^(weight) * df_phase`;
   - require exactly five local phase factors in the final contraction path and one global `df_phase` multiplication.

3. `weight-parameter-semantics`
   - determine from pinned source/code whether the executable `weight` exponent has an explicit source-level identification with the paper's face-weight parameter;
   - separately test whether the project's historical `alpha` notation is source-qualified as identical to that parameter. No equality may be asserted from naming similarity or previous project convention alone.
   - If paper↔code weight semantics are exact but project-`alpha`↔source parameter identity is not source-qualified, classify that subquestion BLOCKED while preserving the source-qualified paper/code convention. A future numerical gate must then use the source/code parameter name/value directly and must not relabel it `alpha`.

4. `null-controls`
   - parser/authority controls must reject at least: removed global `df_phase`; changed final exponent from `dfj^(weight)` to `dfj^(1)`; one removed local phase factor; and a fake project-`alpha` source identity.

## Frozen classification

`PASS — LORENTZIAN_FIVE_VERTEX_PHASE_WEIGHT_AUTHORITY_PASS` only if:

- exact source provenance/hash is valid;
- source Eq.(11) phase/weight objects are found without inference;
- author-code `dfj`, `df_phase`, five local sign factors and face-weight exponent semantics are structurally qualified;
- source/code conventions can be translated without amplitude fitting;
- all null controls are distinguished.

The project historical `alpha` alias is **not required** for PASS if no source authority identifies it; in that case the aggregate must explicitly set `historical_alpha_alias_authorized=false`, and subsequent numerical work must use the source/code weight parameter directly.

`SCOPED BLOCKED — LORENTZIAN_FIVE_VERTEX_PHASE_WEIGHT_AUTHORITY_BLOCKED_SOURCE_SEMANTICS` if exact source/code objects are present but their relation is not uniquely source-qualified.

`SCIENTIFIC FAIL — LORENTZIAN_FIVE_VERTEX_PHASE_WEIGHT_STRUCTURAL_FAIL` only if exact qualified source/code conventions are mutually inconsistent under the frozen translation test.

`INFRASTRUCTURE/INVALID_PROVENANCE` if required source retrieval/hash/pin fails before scientific predicates are evaluable.

## Locks

No threshold or convention may be changed after result inspection. No five-vertex amplitude is authorized by workflow green status alone.

Until terminal PASS: no repaired bounded five-vertex numerical gate; no unbounded ten-face sum; no shell convergence; no coarse↔fine equality; no zero-face deletion; no Eq.(27)/Eq.(29)/Lambda/TNR; no bridge credit; no candidate-theory construction.

Claim locks remain: `refinement_map_derived=false`, `bridge_credit=false`, candidate theory `UNFORMED / 0%`; do not claim `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, or `BRIDGE_DERIVED`.