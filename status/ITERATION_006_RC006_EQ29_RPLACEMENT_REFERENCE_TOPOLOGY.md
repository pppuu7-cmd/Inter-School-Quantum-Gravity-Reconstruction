# ITERATION_006 RC006 Eq.(29) R-placement structural reference-topology audit — preregistration

Date: 2026-09-12
Phase: PHASE_1 amplitude/refinement bridge
Status: PREREGISTERED BEFORE IMPLEMENTATION

## Frozen prerequisite

Run `34718554940` is terminal `EQ29_SOURCE_DEPENDENCIES_PARTIAL`: immutable-block geometry and source-level incidence PASS, while R-placement is `SOURCE_R_PLACEMENT_NOT_MACHINE_QUALIFIED`. This result is preserved and will not be reclassified by weakening its criterion.

Earlier durable result `results/ITER006_RC006_EQ29_SOURCE_RELATION_MIXED_RESULT.md` explicitly permits a distinct prospective source-structure object based on TeX include/section/label/reference topology. The old failed lexical crossing threshold will not be rerun with easier patterns.

## Frozen source/object

- source: arXiv:1609.02429v2, `bc-spin-nets.tex`;
- source bundle SHA256: `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`;
- immutable EPRL Eq.(29) block SHA256: `4f505657a580216d176c1c63ec92f5614dc73e8113294722a854d5a350b67083`;
- no raster geometry, nearest-neighbour label fitting, manual crossing choice or new lexical synonym set is allowed.

## Scientific objective

Answer two independent questions without changing the preceding PARTIAL verdict:

1. Does the exact source-level Eq.(29) TikZ contain a proper straight-segment crossing, making crossing convention demonstrably applicable at the immutable tensor-diagram level? Arcs are reported separately and prevent a `NO_CROSSING` claim when unresolved.
2. Is there an explicit TeX structural reference path (labels/`ref`/`eqref`/section containment only) that connects the Eq.(29) EPRL subsection/block to the source-defined R/R^-1 crossing identities or their graph appendix, sufficient to determine placement without a fitted selector?

## Frozen independent lanes

### CROSSING_GEOMETRY

Parse only explicit numeric TikZ coordinates and `--` straight segments in the immutable draw command. Use exact rational arithmetic for coordinates. Count proper interior intersections of non-adjacent straight segments, excluding shared endpoints. Also record the number of `arc(...)` operators.

Outcomes:
- `EQ29_STRAIGHT_CROSSING_PRESENT` if at least one exact proper straight-segment intersection exists;
- `EQ29_NO_STRAIGHT_CROSSING_ARCS_UNRESOLVED` if none exists but one or more arcs are present;
- `EQ29_NO_SOURCE_CROSSING` only if no proper straight intersection and no arcs occur;
- `INVALID_SOURCE_OR_IMPLEMENTATION` on block/hash/parser failure.

This lane alone never determines R versus R^-1.

### REFERENCE_GRAPH

Strip TeX comments with the already frozen unescaped-`%` rule. Build a graph only from explicit structural objects:
- section/subsection/subsubsection containment;
- `\\label{...}` definitions;
- `\\ref{...}` and `\\eqref{...}` edges;
- exact containment of the immutable Eq.(29) target and exact containment of source R/R^-1 definition blocks.

No lexical synonyms are graph edges. PASS only if a directed explicit-reference path from the EPRL Eq.(29) source container to an R/R^-1 definition container or graph-appendix object exists.

Outcomes: `EQ29_R_EXPLICIT_REFERENCE_PATH_PRESENT` or `EQ29_R_EXPLICIT_REFERENCE_PATH_ABSENT`.

### APPENDIX_GRAPH_CHAIN

Independently audit the exact source statement following the R/R^-1 identities that references appendix `app:graph`, resolve that label structurally, and test whether the EPRL Eq.(29) subsection itself contains an explicit `ref`/`eqref` chain to that appendix or to an object inside it. Merely occurring later in the same file or sharing the word EPRL is insufficient.

Outcomes: `EQ29_APPENDIX_GRAPH_REFERENCE_CHAIN_PRESENT` or `EQ29_APPENDIX_GRAPH_REFERENCE_CHAIN_ABSENT`.

## Frozen aggregate interpretation

- `EQ29_RPLACEMENT_STRUCTURALLY_QUALIFIED` only if a proper straight crossing is present **and** REFERENCE_GRAPH PASSes with an explicit source reference path sufficient to tie Eq.(29) to the R convention. This still authorizes only a separately preregistered literal tensor reconstruction gate.
- `EQ29_RPLACEMENT_STILL_BLOCKED_CROSSING_PRESENT_NO_EXPLICIT_REF` if a proper straight crossing exists but no explicit reference path is found.
- `EQ29_RPLACEMENT_APPLICABILITY_INCONCLUSIVE` if straight crossings are absent but arcs remain unresolved, regardless of reference outcome.
- `EQ29_R_NOT_APPLICABLE_AT_IMMUTABLE_BLOCK_LEVEL` only if the source block has neither proper straight crossings nor arcs; this does not remove R-placement requirements from later crossing-bearing amplitudes.
- `INVALID_SOURCE_OR_IMPLEMENTATION` on any invalid lane.

No outcome changes the frozen `EQ29_SOURCE_DEPENDENCIES_PARTIAL` result. No bridge credit is awarded.

## Claim locks

No numerical Eq.(29) amplitude, RC006 bridge credit, `BRIDGE_DERIVED`, candidate theory, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized by this diagnostic.

## Administrative launch annotation

The implementation workflow was registered at commit `745ecd2f3c999dbf130d4e7ed4520a3f0f28f13a`. This annotation only triggers the already-frozen workflow and changes no scientific object, criterion, source, parameter, control or interpretation rule above.
