# ITER132 preregistration — D=4 transfer authority for explicit R2/Gamma2 momentum vertices

Date: 2026-09-15
Gate: `ITER132_FIXED_GEODESIC_CURVATURE_D4_VERTEX_TRANSFER_AUTHORITY`

## Frozen motivation
ITER131 closed an explicit component-generator gate on a deterministic D=2 symmetric-tensor basis. The downstream fixed-geodesic curvature pole calculation is four-dimensional. Before any M/G numerator jet may consume the nonlinear vertices, the dimension-independent indexed formulas must pass an explicit D=4 transfer audit.

## Frozen predicates
A. Instantiate the canonical unreduced ITER130 R2 and Gamma2 momentum formulas in D=4 on the full 10-element symmetric graviton-leg basis.
B. Verify R2 graviton-leg Bose symmetry and Gamma2 lower-index plus leg Bose symmetries on the full D=4 component basis.
C. Verify simultaneous momentum homogeneity: degree 2 for R2 and degree 1 for Gamma2 on a deterministic spanning panel.
D. Independently reconstruct the quadratic Fourier coefficient from the metric definition `g=delta+kappa h`, inverse-metric expansion and Christoffel/Ricci contraction for deterministic two-plane-wave panels, and compare with the explicit vertex generator. The direct reconstruction must not call the R2/Gamma2 vertex routines under test.
E. Include off-diagonal polarizations and non-collinear integer momenta in the direct panel.
F. No loop denominator, pole residue, B1 target, EDT exponent, cancellation target or fitted coefficient may enter the transfer audit.

## Frozen classifications
- `PASS_SCOPED_D4_R2_GAMMA2_VERTEX_TRANSFER_CLOSED` iff A-F pass.
- `FAIL_SCOPED_D4_VERTEX_TRANSFER_MISMATCH` if any exact identity fails.
- `NUMERICAL_OR_INFRASTRUCTURE_FAIL` only for execution/tool failure before predicates are evaluated.

## Claim ceiling
A PASS authorizes the D=4 R2/Gamma2 vertices as inputs to subsequent M/G pole-relevant numerator-jet construction. It is not a loop-pole result, B1 determination, noncancellation result, EDT match, bridge, new physics or candidate theory.
