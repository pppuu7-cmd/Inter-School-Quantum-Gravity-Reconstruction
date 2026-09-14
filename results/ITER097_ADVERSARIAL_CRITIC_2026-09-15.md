# ITER097 adversarial critic — response-matrix PSD-bound identifiability

Date: 2026-09-15
Gate: `ITER097_RESPONSE_MATRIX_PSD_BOUND_IDENTIFIABILITY`

## Target conclusion under attack

Provisional conclusion: diagonal susceptibility information plus covariance positivity does not identify the eigenvectors of the full CDT bare-coupling response matrix.

## Rescue attempt 1 — assume weak correlations

Rejected. No frozen source bound establishes `|rho_ij| << 1`. Setting missing cross-covariances near zero would be an unsupported prior and directly violate `ZERO_COVARIANCE_CONTROL`.

## Rescue attempt 2 — use maximal-correlation bounds as approximate values

Rejected. Cauchy-Schwarz gives an allowed interval, not an estimator. Both signs are admissible absent source information, and opposite signs rotate the principal directions oppositely.

## Rescue attempt 3 — identify the pseudocritical-line normal with the leading response eigenvector

Rejected. A finite-size transition-locus tangent/normal is not source-defined as a Fisher eigenvector, and still does not determine mixing with `kappa_0` or the constrained volume direction. This would violate `TANGENT_EIGENVECTOR_SWAP_CONTROL`.

## Rescue attempt 4 — drop the `kappa_4` row and solve the remaining 2 x 2 block

Rejected as a solution to the preregistered three-coupling problem. Even the 2 x 2 block remains non-identifiable from diagonals alone because the unknown covariance controls the rotation angle and its sign.

A reduced 2 x 2 analysis can be useful only if an explicit cross-covariance or structural relation is added from an independent source.

## Rescue attempt 5 — infer off-diagonals from nonlinear ratio susceptibilities

Rejected. Variances of ratios such as `N_0/N_41` or `N_32/N_41` depend on joint moments and denominator fluctuations. Without matched joint data, inversion is non-unique.

## Rescue attempt 6 — use an FRG stability direction to select the admissible CDT matrix

Rejected as circular bridge construction. The purpose of the CDT-internal gate is to determine whether a scaling direction is independently fixed. Selecting the matrix by agreement with FRG violates `FRG_TARGET_SELECTION_CONTROL`.

## Critic verdict

The no-go survives adversarial review.

The strongest exact statement is:

> Published marginal susceptibility information and PSD constraints can bound missing covariance magnitudes once matching diagonal variances are known, but they cannot determine the sign/orientation of the CDT bare response eigendirections; the volume-fixing row adds an independent protocol ambiguity.

This is an identifiability theorem for the frozen information set, not a physical no-go for CDT or its continuum limit.
