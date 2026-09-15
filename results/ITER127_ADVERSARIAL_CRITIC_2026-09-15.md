# ITER127 adversarial critic — exact chi1/chi2 singular-strata authority

Date: 2026-09-15
Gate: `ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY`
Source authority: `sources/ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY_2026-09-15.md`
Strict source artifact: `iter127-frob-strict-source-assertions`

## Attack 1 — the -1/2 and +3/8 coefficients could be false-positive regex matches

Resolved. The strict v2 source check requires each coefficient to occur in the **same TeX equation environment** as the corresponding `chi1` or `chi2` order and preserves file/line evidence in the artifact. The earlier wider-context checker is not the final authority.

## Attack 2 — the compact schematic chi2 equation may omit tensor-index terms

The source-authority record intentionally suppresses indices only when classifying affine weights and nesting. It does not replace the exact TeX equations for future tensor algebra. The exact-source artifact remains authoritative for signs/index contractions when the actual pole numerator is constructed.

## Attack 3 — differentiating chi1 always removes the inner Green factor completely

For the bulk Green solution, differentiating with respect to the outer affine endpoint changes `(tau-sigma)` into a constant on the ordered interior, so the polynomial diagonal suppression from that kernel is removed. Endpoint-distribution terms and differentiation of local initial data are kept separately in the endpoint sector. ITER127 claims the polynomial suppression order, not the full tensor distribution.

## Attack 4 — chi1chi1 bulk-bulk should be treated on an ordered triangle rather than a square

For the product of two independently integrated first-order endpoint displacements, the natural domain is the square `[0,1]^2`; symmetry can later reduce it to ordered sectors with a combinatorial factor. The diagonal remains an unsuppressed coincidence stratum either way.

## Attack 5 — the chi2 nested dGamma1-chi1 term could have additional endpoint suppression from tensor contractions

Possible. ITER127 records only source-explicit polynomial Green-kernel suppression. Curvature/projector tensor contractions may further soften or cancel leading singularities. This is precisely why ITER128 is required and why no residue is assigned here.

## Attack 6 — the initial-tangent terms are irrelevant because they have no line parameter

Rejected during renormalization. They are endpoint-local composite pieces and can be required for gauge/subdivergence cancellation. Their absence of an affine integration only means ITER126's line subtraction algorithm is not applied to them as independent line masters.

## Attack 7 — exact source weights transfer the matter-scalar residue to curvature

Rejected. The source supplies geodesic kinematics only. Curvature carries different derivative vertices/composite mixing. No matter-scalar pole coefficient is imported.

## Critic verdict

**CONFIRMS `PASS_SCOPED_EXACT_CHI1_CHI2_WEIGHTS_SOURCE_QUALIFIED_SINGULAR_TABLE_CLOSED`.**

ITER127 closes the source-sensitive geodesic-kernel stage. The next calculation must combine the exact affine suppression with curvature/projector derivative counting before any pole coefficient is evaluated.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.