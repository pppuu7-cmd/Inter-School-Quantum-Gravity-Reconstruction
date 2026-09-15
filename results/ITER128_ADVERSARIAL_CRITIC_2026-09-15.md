# ITER128 adversarial critic — projected local singular-degree / Taylor-jet census

Date: 2026-09-15
Gate: `ITER128_FIXED_GEODESIC_CURVATURE_PROJECTED_LOCAL_SINGULAR_DEGREE_CENSUS`
Source authority: `sources/ITER128_FIXED_GEODESIC_CURVATURE_PROJECTED_LOCAL_SINGULAR_DEGREE_CENSUS_2026-09-15.md`

## Attack 1 — a jet-order ceiling of seven proves a seventh derivative is needed numerically

Rejected. `k=7` is a superficial local Taylor ceiling for the strongest canonical residual single-propagator defect kernel. Lower Taylor coefficients or tensor contractions may eliminate the logarithmic pole before that order. The calculation should expand only as far as power counting and symmetry require for the specific projected graph.

## Attack 2 — raw interaction graphs can be more singular than the stated global ceiling

Correct, and the source record explicitly scopes the ceiling **after bulk subdivergence subtraction and projection onto the finite residual defect basis**. Raw F/M/G integrands can have stronger coincident powers that cancel or are removed by bulk/local counterterms. Treating the post-subtraction ceiling as a raw-integrand bound would be invalid.

## Attack 3 — all two-propagator products can be assigned the same jet order from G0 squared

Rejected. The base power is fixed (`m=4+N`), but the derivative numerator assignment `N` is graph-specific. Curvature derivatives, action vertices and geodesic derivatives can distribute differently across the two lines. ITER128 correctly leaves those rows for an explicit graph numerator census.

## Attack 4 — Green suppression always lowers the pole order by one

Only where the source weight actually vanishes linearly at the same singular stratum. For example `(1-tau)` helps `tau->1` but not `tau->0`; `(tau-sigma)` helps the ordered diagonal but not unrelated endpoints. ITER128 applies suppression stratum by stratum.

## Attack 5 — derivative distributions produce contact terms that invalidate the simple power rule

They require careful distributional subtraction, but the superficial degree remains the correct local Taylor-jet budgeting tool. Contact delta derivatives are retained through ITER124 renormalization and removed from the final separated coefficient only after subtraction. The power rule is not used to discard them prematurely.

## Attack 6 — the canonical R1-to-BoxPerpR bound is itself a B1 pole

Rejected. It is the strongest allowed local derivative structure of the genuine defect counterterm basis. Its actual coefficient can vanish, be redundant in a particular projection, or cancel in the full RG system.

## Critic verdict

**CONFIRMS `PASS_SCOPED_CANONICAL_JET_BOUNDS_CLOSED_INTERACTION_SPECIFIC_ROWS_OPEN`.**

The next safe reduction is graph-specific derivative allocation, not pole evaluation from superficial degree alone.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.