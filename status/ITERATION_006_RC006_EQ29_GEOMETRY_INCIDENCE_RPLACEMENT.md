# ITERATION_006 RC006 Eq.(29) geometry / incidence / R-placement audit — preregistration

Date: 2026-09-12
Phase: PHASE_1 amplitude/refinement bridge
Status: PREREGISTERED BEFORE IMPLEMENTATION

## Frozen prerequisite

Run 34717945469 must be terminal and independently verify a unique target inside the active-TeX subsection `EPRL intertwiner model`, with exact extracted align-block SHA256 `4f505657a580216d176c1c63ec92f5614dc73e8113294722a854d5a350b67083` and target anchor line 1090. This gate gives source-block authority only and does not authorize an Eq.(29) amplitude.

## Frozen source

- arXiv:1609.02429v2 source bundle SHA256: `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`
- TeX file: `bc-spin-nets.tex`
- Exact EPRL subsection title: `EPRL intertwiner model`
- Exact candidate align-block SHA256 above.

## Scientific objective

Test, independently and without fitting to a desired conclusion, whether the pinned primary source contains enough machine-verifiable information to qualify the three still-missing Eq.(29) dependencies:

1. label geometry;
2. path/incidence structure of the depicted 3-valent EPRL tensor;
3. R-matrix / inverse-R placement semantics tied to the relevant EPRL construction.

This is a source-authority gate, not an amplitude calculation and not a bridge derivation.

## Frozen parallel lanes

Run three independent lanes with fail-fast disabled.

### GEOMETRY lane

Re-extract the unique active EPRL subsection and exact candidate align block. Parse all TikZ node labels and draw commands. PASS only if:
- the candidate block hash exactly matches the frozen hash;
- at least one TikZ picture and one draw command are present;
- the source labels contain the structural set `{J^-, J^+, l, j^-_1, j^+_1, j^-_2, j^+_2, l_1, l_2}` modulo TeX whitespace/bracing normalization.

Otherwise FAIL_CLOSED.

### INCIDENCE lane

On the same exact block, tokenize TikZ path segments and endpoints without rasterization. Record the path graph verbatim and a normalized edge/segment multiset. PASS only if a nonempty finite path graph is machine-extractable and every required structural label can be associated with a source-level node/path occurrence. Do not infer missing edges from visual proximity and do not use raster connected components.

Otherwise classify `SOURCE_PATH_INCIDENCE_NOT_MACHINE_QUALIFIED`.

### RPLACEMENT lane

Search only the active EPRL subsection plus its immediately preceding source-defined crossing convention context in the same pinned TeX source. Record exact source snippets/offsets for R-matrix and inverse-R definitions and for over/undercrossing language. PASS only if both R and inverse-R semantics are explicitly source-defined and the EPRL subsection contains an explicit source-level reference or symbol that determines which crossing convention is used in the Eq.(29) construction. Generic R-matrix definitions elsewhere without a deterministic link to Eq.(29) do not pass.

Otherwise classify `SOURCE_R_PLACEMENT_NOT_MACHINE_QUALIFIED`.

## Frozen aggregate classifier

- `EQ29_SOURCE_DEPENDENCIES_COMPLETE` only if GEOMETRY, INCIDENCE and RPLACEMENT all PASS.
- `EQ29_SOURCE_DEPENDENCIES_PARTIAL` if at least one lane PASSes and at least one scientific dependency remains unqualified.
- `EQ29_SOURCE_DEPENDENCIES_BLOCKED` if none of the three dependencies can be qualified from the pinned source.
- `INVALID_SOURCE_OR_IMPLEMENTATION` only for source hash mismatch, malformed extraction, missing artifact, or implementation failure.

Green CI alone is never scientific PASS.

## Claim locks

Even `EQ29_SOURCE_DEPENDENCIES_COMPLETE` authorizes only a separately preregistered literal Eq.(29) tensor reconstruction gate. It does **not** authorize Eq.(29) amplitude correctness, RC006 bridge credit, BRIDGE_DERIVED, candidate theory construction, or any claim that known schools fail.

No thresholds, labels, source scope, or interpretation rule may be changed after production results are inspected.

## Administrative launch annotation

Implementation workflow was registered at commit `be3615fb36f4c1863b221b86fcf80d7cf4f11125`. This annotation exists only to trigger the already-frozen workflow after registration and changes no scientific object, parameter, threshold, source scope, control, or interpretation rule above.
