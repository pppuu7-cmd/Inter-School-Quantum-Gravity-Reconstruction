# Iteration 006 / RC006 — Eq.(29) arc-aware source geometry gate

## Authority and purpose

This gate is preregistered **before implementation/production**. It is the only dependent follow-up authorized by the terminal result of run `34718784867`, whose frozen classifier returned `EQ29_RPLACEMENT_APPLICABILITY_INCONCLUSIVE`: the immutable Eq.(29) block has no proper crossing among straight segments, contains two TikZ `arc(...)` primitives, and has an explicit source reference path to the R/R^{-1} convention. The gate does not modify or weaken the prior R-placement criterion.

Pinned source: arXiv `1609.02429v2`, source-bundle SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

Immutable Eq.(29) EPRL block SHA256: `4f505657a580216d176c1c63ec92f5614dc73e8113294722a854d5a350b67083`.

## Frozen scientific object

Reconstruct the complete geometry of the single active TikZ `\\draw ... ;` path inside the immutable Eq.(29) block, including every straight `--` segment and every TikZ circular `arc(start:end:radius)` primitive under standard TikZ arc semantics. Node-placement text is excluded from the geometric path exactly as in the predecessor gate.

For every pair of non-adjacent geometric primitives, test analytically for **proper interior intersections**:

- line–line;
- line–arc;
- arc–arc.

Shared endpoints and endpoint-only contacts are not proper crossings. Arc membership uses the directed angular sweep encoded in the source. Geometry is evaluated deterministically at 80 decimal digits; an intersection is accepted only when the candidate lies at least `1e-25` of the relevant parameter away from every primitive endpoint and satisfies both primitive equations to absolute residual `<=1e-40`. The same result must be reproduced at 120 digits. No image rasterization, OCR, hand-selected crossing, or post-result tolerance change is permitted.

A separate source-reference control rechecks, without synonym inference, that the EPRL body directly references a labeled structural object whose definition lies within 2500 source characters of an explicit `\\mathcal{R}` or `\\mathcal{R}^{-1}` definition. This control is not allowed to alter the geometry result.

## Frozen outputs and interpretation

1. `EQ29_ARC_GEOMETRY_INVALID` — source hash/path parsing/high-precision consistency fails. This is an implementation/numerical failure, not scientific evidence.
2. `EQ29_ARC_AWARE_NO_PROPER_CROSSING` — zero proper interior crossings after all line/arc pairs are included. Consequence: R/R^{-1} is **not applicable at this immutable Eq.(29)-block geometry level**; literal Eq.(29) reconstruction remains blocked for any other unresolved source dependency and receives no bridge credit.
3. `EQ29_ARC_AWARE_UNIQUE_PROPER_CROSSING_R_REF_QUALIFIED` — exactly one proper interior crossing and the independent exact-reference control is present. Consequence: the previously blocked R-placement applicability dependency is source-qualified at this block level; this only authorizes a separately preregistered literal Eq.(29) reconstruction gate. It is not an amplitude PASS and gives no bridge credit by itself.
4. `EQ29_ARC_AWARE_CROSSING_PRESENT_R_REF_BLOCKED` — one or more proper crossings but exact R-reference control absent. R-placement remains BLOCKED.
5. `EQ29_ARC_AWARE_MULTIPLE_CROSSINGS_AMBIGUOUS` — more than one proper crossing. R-placement remains BLOCKED unless a new independent source rule prospectively selects the relevant crossing; no fitted selector is allowed.
6. `EQ29_ARC_AWARE_PRECISION_DISAGREEMENT` — 80/120-digit topology differs. Numerical/geometry BLOCKED, not scientific FAIL.

## Claim locks

- `eq29_amplitude_authorized=false` for this gate itself, even in case (3).
- `bridge_credit=false` for this gate itself.
- No `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, or `ALL_KNOWN_SCHOOLS_FAIL` claim.
- No candidate action/Hamiltonian/field equations.
- No post-hoc tolerance, source-block, or geometry edits after production output is visible.
