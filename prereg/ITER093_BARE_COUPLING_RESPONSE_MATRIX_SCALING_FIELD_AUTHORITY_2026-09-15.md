# ITER093 preregistration — CDT bare-coupling response matrix / scaling-field authority

Date: 2026-09-15
Gate: `ITER093_BARE_COUPLING_RESPONSE_MATRIX_SCALING_FIELD_AUTHORITY`

## Motivation

ITER091 established an independent bare total-volume source but no renormalized cosmological map. ITER092 showed that the finite-size shifts of `K_4^crit` and `Delta^crit` co-scale and are approximately linearly correlated, so a bare coordinate axis cannot be assumed to be a pure RG eigendirection.

The natural local object for resolving coupling mixing is the connected thermodynamic response matrix of the observables conjugate to the bare CDT action couplings.

## Exact formal object frozen before detailed source audit

Using the standard four-dimensional Euclidean CDT action convention

`S_R = -kappa_0 N_0 + kappa_4 N_4 + Delta (N_41 - 6 N_0)`,

with `N_4=N_41+N_32`, define the action-derivative observables

`A_kappa0 = -N_0`,

`A_Delta = N_41 - 6 N_0`,

`A_kappa4 = N_4`.

Because the action is linear in the bare couplings, the Hessian of `ln Z` is the connected covariance matrix

`F_ij = partial_i partial_j ln Z = Cov(A_i,A_j)`

(up to equivalent score-sign conventions).

This matrix is the Fisher/thermodynamic susceptibility matrix of the bare exponential family. Its eigenvectors are candidate local response directions in the chosen bare coordinates; they are not automatically continuum RG eigenvectors.

## Frozen question

Do the four-dimensional CDT source/data stack expose the **full joint connected covariance matrix**, or an equivalent set of cross-responses, near a candidate continuous transition with enough control of volume fixing to identify mixed scaling-field directions rather than only scalar susceptibilities?

## Required predicates

A. The bare action and conjugate observables are source-explicit.

B. Diagonal susceptibilities for the relevant transition are source-measured.

C. Off-diagonal connected covariances between the conjugate observables are source-published or recoverable from public matched raw time series.

D. The matrix is measured at common bare couplings, volume and phase-transition prescription; separate scans cannot be assembled as if simultaneous without source authority.

E. The `kappa_4`/`N_4` row and column are either measured in a genuinely variable-volume ensemble or corrected for the exact volume-fixing potential. A hard/fixed `N_4` ensemble has zero physical information in that projected direction.

F. If the fixing is on `N_41` rather than total `N_4`, the induced response mixing with `N_32` is retained.

G. Eigenvectors of the finite-volume thermodynamic matrix are called **candidate bare scaling directions** only. A continuum RG eigenvector requires finite-size scaling and source-defined approach to a continuous critical point.

H. No numerical agreement with FRG critical exponents/eigenvectors may be used to choose a basis, sign, normalization or missing cross-covariance.

## Frozen controls

- `DIAGONAL_ONLY_MATRIX_CONTROL`: separate susceptibilities do not define a response-matrix eigenvector.
- `SEPARATE_SCAN_STITCHING_CONTROL`: measurements at different coupling points cannot be combined into one covariance matrix.
- `FIXED_VOLUME_KAPPA4_ROW_CONTROL`: conditioning on volume projects out/distorts the cosmological response direction.
- `GAUSSIAN_FIXING_HESSIAN_CONTROL`: external quadratic fixing contributes to the measured Hessian and must be removed for physical response.
- `ORDER_PARAMETER_ACTION_OBSERVABLE_CONTROL`: convenient nonlinear order parameters are not automatically the linear action-conjugate observables.
- `THERMODYNAMIC_RG_EIGENVECTOR_CONTROL`: finite-volume Fisher eigenvectors are candidates, not continuum RG eigenvectors by themselves.

## Frozen classifications

- `PASS_SCOPED_FULL_RESPONSE_MATRIX_SCALING_DIRECTION_CANDIDATE` if A-F pass and at least one nontrivial mixed bare response eigenvector is source-qualified.
- `PASS_SCOPED_FORMAL_RESPONSE_MATRIX_DATA_AUTHORITY_OPEN` if A/B pass and the exact formal matrix is defined, but C/D/E prevent source-level eigenvector reconstruction.
- `SCOPED_BLOCKED_VOLUME_FIXING_PROJECTS_COSMOLOGICAL_DIRECTION` if cross-data exist only under a constraint that removes the needed `kappa_4` response and no correction is source-available.
- `BLOCKED_SOURCE_AUTHORITY` if even the action-conjugate response structure cannot be established.

## Claim ceiling

A PASS identifies at most a candidate mixed bare scaling direction for a later finite-size/RG test. It cannot establish a continuum critical eigendirection, map it to FRG, create bridge credit or authorize candidate-theory construction.
