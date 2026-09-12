# ITERATION_006 RC006 Eq.(29) exact arc-aware source geometry — preregistration

Date: 2026-09-12  
Status: PREREGISTERED BEFORE IMPLEMENTATION

## Frozen prerequisite

Run `34718784867` is terminal `EQ29_RPLACEMENT_APPLICABILITY_INCONCLUSIVE`. Its crossing lane found 15 explicit straight segments, zero proper straight/straight crossings, and exactly two unresolved `arc(...)` operators. The explicit structural R-reference path is present, while the appendix graph chain is absent. The preceding `EQ29_SOURCE_DEPENDENCIES_PARTIAL` verdict remains frozen.

## Frozen source object

- arXiv:1609.02429v2, source bundle SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`;
- source file `bc-spin-nets.tex`;
- unique active subsection `EPRL intertwiner model`;
- immutable Eq.(29) align block SHA256 `4f505657a580216d176c1c63ec92f5614dc73e8113294722a854d5a350b67083`;
- the single source `\\draw` path inside that block is the only geometry object admissible to this gate.

No rasterization, nearest-neighbour fitting, manual crossing selection, lexical synonym expansion, or desired R/R^-1 choice may enter the classifier.

## Frozen geometry grammar

The parser must consume the draw path in source order and support only source-explicit numeric geometry:

1. Cartesian points `(x,y)` with signed integer or decimal numeric coordinates;
2. straight connector `--`;
3. TikZ arc syntax `arc (start-angle:end-angle:radius)` with signed integer/decimal angles and radius, optional whitespace, and an optional common unit suffix on radius;
4. if the source uses an unsupported arc syntax, x/y radii, transforms that cannot be reduced from explicit source numbers, Bézier controls, or an unparsed geometry operator, the scientific result is `EQ29_ARC_GEOMETRY_UNRESOLVED_UNSUPPORTED_SYNTAX`, never an inferred crossing/no-crossing.

For an accepted circular arc beginning at current point `P` with start angle `a`, end angle `b`, radius `r`, its center is defined by TikZ path semantics as `C = P - r(cos a, sin a)`, and its terminal point is `C + r(cos b, sin b)`. Angles are interpreted in degrees and traversal follows the explicit signed start→end angular interval as encoded by the source.

## Frozen intersection object

Enumerate the complete source path as straight segments and circular arcs. Test all non-adjacent primitive pairs:

- straight/straight;
- straight/arc;
- arc/arc.

Shared endpoints and intersections occurring only at adjacent path joins are not proper crossings. Tangencies are reported separately and do not count as proper crossings. Intersections must lie in the strict interior of both source primitives. Geometry arithmetic must use at least 80 decimal digits for transcendental evaluation; a candidate crossing is accepted only if its intersection parameters are separated from each primitive endpoint by at least `1e-30` and the residual equations are below `1e-50`. Cases failing those numerical-certification margins are `UNRESOLVED`, not PASS/FAIL.

## Independent lanes

### ANALYTIC_PATH

Directly parse the immutable source draw path under the frozen grammar and compute all primitive intersections.

### REVERSED_ENUMERATION

Independently reconstruct the same primitive list, enumerate pair order in reverse, and recompute the full intersection set using the same frozen geometry definitions but separate code. The canonical set of proper crossing primitive-index pairs and intersection coordinates rounded only for serialization to 40 decimal digits must agree between lanes.

## Frozen classifications

- `EQ29_COMPLETE_SOURCE_CROSSING_PRESENT`: both lanes are valid, agree, and contain at least one proper interior crossing involving any straight/arc or arc/arc primitive (straight/straight was already frozen zero but is recomputed).
- `EQ29_COMPLETE_SOURCE_NO_CROSSING`: both lanes are valid, agree, every source geometry primitive is parsed, and zero proper crossings exist.
- `EQ29_ARC_GEOMETRY_UNRESOLVED_UNSUPPORTED_SYNTAX`: source is valid but the frozen grammar cannot consume all relevant primitives or certification margins are not met.
- `INVALID_SOURCE_OR_IMPLEMENTATION`: pinned source/block mismatch, malformed parser output, or lane disagreement.

A crossing PASS establishes **applicability of a crossing convention only**. It does not determine R versus R^-1, does not overwrite the earlier R-placement PARTIAL verdict, and does not authorize an Eq.(29) numerical tensor. A NO_CROSSING result only proves that R is not geometrically required inside this immutable Eq.(29) drawing; it says nothing about later crossing-bearing amplitudes.

## Claim locks

Eq.(29) amplitude authorization remains false. Bridge credit remains zero. Candidate theory remains `UNFORMED`; no `BRIDGE_DERIVED`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.
