# ITER119 adversarial critic — line-defect observable projection rank

Date: 2026-09-15
Gate: `ITER119_FIXED_GEODESIC_CURVATURE_LINE_DEFECT_OBSERVABLE_PROJECTION_RANK`
Preregistration: `85244391af7565af8bffdb1d77d5fa3c12da47c8`
Source authority: `89f32f60c266c31ed86a0cde99186937f6034522`

## Attack 1 — two radial functions imply only two counterterms are needed internally

Rejected. Observable-output rank and renormalization-matrix rank are different. Four independent line operators may mix among themselves and be required to cancel divergences even if only two scalar combinations survive in the final RR correlator.

## Attack 2 — the line sector can only shift B0, because finite counterterms are constants

Too strong. Pole residues and running of line-defect couplings can compensate explicit logarithmic scale dependence and therefore project into `B_1`. The fixed-geodesic scalar precedent explicitly exhibits this finite/running interplay.

## Attack 3 — every running coupling generates an independent logarithm, so output rank can exceed two

Rejected under the corrected radial-basis theorem. Multiple running couplings can only contribute to the same single-log radial function `l^-8 L`; they combine into one projected `B_1` coefficient. Their internal beta functions may be independent, but the measured scalar radial shape does not distinguish them at this order.

## Attack 4 — finite and running projections must be linearly independent, proving rank exactly two

Not established. One or both projected combinations could vanish by symmetry or cancellation in the curvature case. ITER119 proves only the upper bound and the absence of a source theorem reducing it further.

## Attack 5 — gauge dependence invalidates the projection argument

No. The complete physical `B_0,B_1` are gauge independent, while individual operator/mixing coefficients can be gauge/scheme dependent. The projection must be performed on the complete renormalized observable. Gauge dependence affects how internal directions combine, not the two-dimensional radial output space.

## Attack 6 — the finite projection is unphysical because finite defect counterterms are arbitrary

Observable-specific renormalization conditions can indeed shift finite constants. That is precisely why `C_fin` must be separated from the leading-log/running information. The existence of scheme dependence does not increase the number of radial functions.

## Critic verdict

**CONFIRMS `PASS_SCOPED_LINE_DEFECT_OBSERVABLE_PROJECTION_RANK_TWO_MAXIMAL`.**

The next calculation should target the projected running/pole combination feeding `B_1` first; if nonzero, full finite mixing data are unnecessary for the noncancellation question.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.