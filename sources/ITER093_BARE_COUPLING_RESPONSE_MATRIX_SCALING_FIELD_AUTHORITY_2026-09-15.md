# ITER093 source authority — CDT bare-coupling response matrix / scaling-field authority

Date: 2026-09-15
Gate: `ITER093_BARE_COUPLING_RESPONSE_MATRIX_SCALING_FIELD_AUTHORITY`
Preregistration: `2f45f30d336ad6ca0a80eb6ff673c134ae95fdcd`

## 1. Formal response matrix is exact

The standard four-dimensional Euclidean CDT Regge action can be written

`S_R = -kappa_0 N_0 + kappa_4 N_4 + Delta (N_41 - 6 N_0)`,

with `N_4=N_41+N_32`.

For bare coordinates

`theta=(kappa_0,Delta,kappa_4)`,

the action derivatives are

`A=(-N_0, N_41-6N_0, N_4)`.

Because the action is linear in `theta`,

`partial_i partial_j ln Z = <A_i A_j>-<A_i><A_j>`

(up to the equivalent score-sign convention).

Thus the complete local thermodynamic/Fisher response matrix is source-defined as the connected covariance matrix of the three action-conjugate observables.

This is the correct object for asking whether a finite-volume transition displacement mixes bare coupling coordinates.

## 2. Published CDT transition studies measure diagonal susceptibilities, not the full action-observable covariance matrix

The phase-transition literature defines scalar susceptibilities

`chi_O = <O^2>-<O>^2`

for selected order parameters and locates pseudocritical couplings by their maxima. Examples include `N_0`, the quantity conjugate to `Delta` such as `N_41-6N_0`, and nonlinear ratios/order parameters such as `N_0/N_41` and `N_32/N_41`.

The toroidal critical-phenomena sources publish:

- separate susceptibility maxima;
- order-parameter histograms;
- Binder cumulants;
- finite-size shifts of transition coordinates;
- approximate linear correlation of the pseudocritical `K_4` and `Delta` locations.

They do not publish the matched off-diagonal connected covariances

`Cov(N_0, N_41-6N_0)`,

`Cov(N_0,N_4)`,

`Cov(N_41-6N_0,N_4)`

at common transition points with the precision needed to reconstruct and diagonalize the full three-coupling response matrix.

The available thesis/full-source search likewise exposes covariance matrices for spatial-volume profile reconstruction and geometric profile correlations, but not a bare-action coupling susceptibility matrix.

## 3. Convenient order parameters cannot substitute for the missing matrix

The commonly used phase order parameters are chosen for transition visibility and need not be linear action-conjugate observables. Separate variances of nonlinear ratios do not determine the cross-covariances of the action derivatives.

Therefore scalar susceptibility peaks and Binder cumulants cannot be stitched into `F_ij` without raw matched joint time series or explicit published cross-moments.

## 4. The cosmological row is especially delicate because of volume fixing

Modern simulations often add

`S_fix = epsilon (N_41-Nbar_41)^2`

or an analogous total-volume restraint and tune `kappa_4` to a pseudocritical value.

This has two consequences:

1. conditioning/fixing suppresses the physical total-volume response that would populate the `kappa_4` row and column;
2. a Gaussian restraint adds external curvature in the restrained volume direction, so the measured variance/cross-response is not the unconstrained grand-canonical Fisher entry until the fixing contribution is removed.

If the fixing is on `N_41`, the relation to total `N_4=N_41+N_32` additionally requires the correlated `N_32` response.

The frozen published transition sources do not provide a deconvolved full `(kappa_0,Delta,kappa_4)` response matrix.

## 5. What can be inferred without the missing data

The approximately linear `K_4^crit` versus `Delta^crit` relation from ITER092 is qualitative evidence of bare-coordinate mixing. It supplies a tangent to a finite-size pseudocritical trajectory in a two-coordinate projection.

It is not enough to determine the eigenvectors of the thermodynamic response matrix, because:

- the normal response direction is not fixed by the tangent alone;
- `kappa_0` mixing is not determined by that two-dimensional plot;
- a transition-locus tangent is not automatically an RG stability eigenvector;
- finite-volume hysteresis and fixing conventions remain part of the measurement.

## Predicate adjudication

- A source-explicit bare action/conjugate observables: **PASS**.
- B source-measured diagonal susceptibilities: **PASS**.
- C source-published off-diagonal action-observable covariances: **NO / DATA AUTHORITY OPEN**.
- D common-point matched matrix authority: **NO**.
- E unconstrained/deconvolved `kappa_4` row: **NO** in the frozen published stack.
- F `N_41` fixing versus total `N_4` distinction: **PASS_CONTROL**.
- G finite-volume Fisher eigenvectors not promoted to continuum RG eigenvectors: **PASS_CONTROL**.
- H no FRG target basis selection: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_FORMAL_RESPONSE_MATRIX_DATA_AUTHORITY_OPEN`**

The response-matrix formalism is exact and identifies precisely which data would resolve the bare mixing problem. The published frozen CDT stack does not expose the necessary joint cross-covariances/deconvolution to reconstruct that matrix.

This is an actionable data-authority blocker, not a physical no-go.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.

## Minimal data product that would reopen the gate

For each selected volume and bare transition point, publish or recover a common Monte Carlo time series containing at least

`N_0`, `N_41`, `N_32`

plus the applied volume-fixing parameters. From these one can construct

`A=(-N_0,N_41-6N_0,N_41+N_32)`,

remove the known fixing contribution, estimate the full connected covariance matrix with autocorrelation-aware errors, and study its eigenvectors/eigenvalues under finite-size scaling.

No FRG input is needed for this CDT-internal reconstruction.
