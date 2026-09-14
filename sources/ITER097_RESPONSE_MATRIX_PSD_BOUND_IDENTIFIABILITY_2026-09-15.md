# ITER097 source/mathematical authority — response-matrix PSD-bound identifiability

Date: 2026-09-15
Gate: `ITER097_RESPONSE_MATRIX_PSD_BOUND_IDENTIFIABILITY`
Preregistration: `3e929beb98139ae99a5c47e3f9941a7af408b3ec`

## Exact setup

From ITER093,

`F = Cov(A)`, `A=(-N_0, N_41-6N_0, N_4)`.

Therefore `F` is a real symmetric positive-semidefinite `3 x 3` matrix.

Write

`F = [[d1,c12,c13],[c12,d2,c23],[c13,c23,d3]]`,

where the diagonals are variances of the action-conjugate observables and the cross terms are the unpublished connected covariances.

PSD implies the pairwise bounds

`|c_ij| <= sqrt(d_i d_j)`

plus the full determinant inequality. These are necessary covariance constraints, not estimates of the missing entries.

## Two-dimensional subproblem already proves non-identifiability

Consider any principal `2 x 2` block

`M(c)=[[d1,c],[c,d2]]`, `|c|<=sqrt(d1 d2)`.

Its eigenvalues are

`lambda_pm = (d1+d2 +/- sqrt((d1-d2)^2 + 4 c^2))/2`,

and, when `d1 != d2`, the eigenvector rotation obeys

`tan(2 theta)=2c/(d1-d2)`.

Consequences:

1. `c=0` is PSD and yields the coordinate axes as eigenvectors.
2. Positive and negative admissible `c` rotate the principal axes in opposite directions.
3. As `|c|` approaches its Cauchy-Schwarz boundary, the rotation can be large; if `d1` and `d2` are comparable, it approaches an approximately 45-degree mixed direction.
4. If `d1=d2`, `c=0` is degenerate and any basis diagonalizes the block, while nonzero `c` selects the plus/minus 45-degree combinations. Thus exact equal diagonals make identifiability worse, not better.

Hence diagonal variances alone cannot determine even the sign of the mixing angle, much less a unique scaling direction.

## Extension to the full three-coupling matrix

The third row/column introduces `c13`, `c23` and `d3`. ITER093 establishes that the cosmological/volume direction is additionally contaminated by the fixing protocol. Published fixed-volume information therefore does not supply a clean unconstrained `d3`, `c13`, or `c23`.

The admissible full family contains matrices with materially different eigenvectors and eigenvalue orderings while preserving the same available diagonal information. Full-determinant PSD restricts combinations but does not collapse the family to a common eigenspace.

## Pseudocritical tangent does not close the family

ITER092 supplies a mixed finite-size `K_4^crit-Delta^crit` trajectory/tangent. No frozen source identity equates that tangent or its normal with an eigenvector of `F`.

Using the tangent to solve for a covariance angle would therefore violate `TANGENT_EIGENVECTOR_SWAP_CONTROL`. It is independent qualitative evidence of coordinate mixing, not a missing matrix element.

## Volume fixing prevents a stronger hidden inference

A Gaussian or conditional volume-fixing prescription can suppress or externally stiffen the volume direction. Therefore an apparently small measured volume variance cannot be interpreted as a small eigenvalue of the unconstrained thermodynamic response matrix without deconvolution.

No PSD argument removes this protocol dependence.

## Predicate adjudication

- A PSD/Cauchy-Schwarz intervals: **PASS**.
- B common forced eigensector across admissible matrices: **FAIL**.
- C pseudocritical tangent reduces family without extra identification: **FAIL / no source-defined relation**.
- D volume-fixing ambiguity retained: **PASS_CONTROL**.
- E no FRG target selection: **PASS_CONTROL**.

## Classification

`NO_GO_SCOPED_MARGINALS_DO_NOT_IDENTIFY_RESPONSE_EIGENDIRECTIONS`

This no-go is stronger than a numerical-data shortage: even exact knowledge of the diagonal variances would not determine the eigenvectors unless additional cross-covariances or an independently justified structural relation are supplied.

What exact diagonal values could improve are quantitative bounds on eigenvalues/correlation magnitudes. They cannot by themselves resolve the sign and orientation of bare-coordinate mixing.

Bridge credit remains `0`; candidate theory remains `UNFORMED / 0%`.
