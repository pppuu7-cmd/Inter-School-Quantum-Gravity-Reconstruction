# ITERATION_006 RC006 Eq.(29) R-placement reference-topology result — 2026-09-12

Frozen preregistration: `95a176d84353a9bf358035140f4fd7423b45873e`  
Implementation: `745ecd2f3c999dbf130d4e7ed4520a3f0f28f13a`  
Trigger/head: `892c4b55f4099ced2743fbc0d34dc121e09fa070`  
Run: `34718784867`  
Aggregate job: `103620738661`  
Summary artifact: `10305042483`  
Summary digest: `sha256:482bc4998d96fd11b0ad2b742038b626d76bc6eacf950efa358cb6333212fc96`

## Frozen result

All three independent source-structure lanes completed successfully. The aggregate is valid and returns:

`EQ29_RPLACEMENT_APPLICABILITY_INCONCLUSIVE`

Lane results:

- crossing geometry: `EQ29_NO_STRAIGHT_CROSSING_ARCS_UNRESOLVED` — 15 explicit straight segments, zero proper straight/straight interior crossings, and exactly 2 source `arc(...)` operators;
- structural reference graph: `EQ29_R_EXPLICIT_REFERENCE_PATH_PRESENT`;
- appendix graph chain: `EQ29_APPENDIX_GRAPH_REFERENCE_CHAIN_ABSENT`.

The frozen `EQ29_SOURCE_DEPENDENCIES_PARTIAL` verdict from run `34718554940` is preserved. In particular, the existence of a source-level reference path to the R/R^-1 convention does not by itself determine whether the immutable Eq.(29) drawing actually contains a crossing carried by one of the unresolved arc primitives, nor does it determine an over/under choice.

## Admissible continuation

The preregistration explicitly permits a **separately preregistered exact arc-aware source-geometry object** when straight crossings are absent but arcs remain unresolved. Such a follow-up may parse the two immutable source arc primitives and all straight primitives and determine complete source-path intersection topology without rasterization or manual crossing selection. It must not alter the prior lexical/source dependency threshold and must not use a desired R placement as a selector.

## Claim lock

Eq.(29) numerical amplitude remains unauthorized. RC006 bridge credit remains zero. No `BRIDGE_DERIVED`, candidate theory, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim follows from this diagnostic.
