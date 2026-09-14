# ITER093 terminal result — CDT bare-coupling response matrix / scaling-field authority

Date: 2026-09-15
Gate: `ITER093_BARE_COUPLING_RESPONSE_MATRIX_SCALING_FIELD_AUTHORITY`
Preregistration: `2f45f30d336ad6ca0a80eb6ff673c134ae95fdcd`
Source authority: `368d343fe769c21ea1a0a9b9eb44360f662a5474`
Adversarial review: `d25819131aefc0b1e7a3762522a86ab42a9503b0`

## Terminal classification

**`PASS_SCOPED_FORMAL_RESPONSE_MATRIX_DATA_AUTHORITY_OPEN`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Exact formal result

For the standard four-dimensional CDT Euclidean action

`S_R = -kappa_0 N_0 + kappa_4 N_4 + Delta (N_41-6N_0)`,

with `N_4=N_41+N_32`, define

`A = (-N_0, N_41-6N_0, N_4)`.

Because the action is linear in the bare couplings, the local thermodynamic/Fisher matrix is exactly

**`F_ij = Cov(A_i,A_j)`**

(up to equivalent score-sign conventions).

This is the correct CDT-internal object for resolving whether the bare coordinate axes mix near a candidate continuous transition.

## Published-data blocker

The frozen four-dimensional phase-transition literature supplies:

- scalar susceptibilities and their maxima;
- order-parameter histograms and Binder information;
- finite-size transition shifts;
- the mixed pseudocritical `K_4-Delta` trajectory of ITER092.

It does **not** expose the full matched set of off-diagonal connected covariances of the action-conjugate observables at common transition points with the metadata required to reconstruct `F`.

Separate scalar scans cannot be stitched into one matrix. Nonlinear ratio observables do not invert uniquely to the primitive count covariance without joint samples.

## Cosmological-row obstruction

The `kappa_4` row/column is especially sensitive to simulation protocol. Fixed-volume conditioning removes the total-volume response, while a Gaussian fixing potential adds external stiffness. When the restraint is imposed on `N_41` rather than total `N_4`, the correlated `N_32` response also matters.

The algebraic fixing correction is in principle tractable. The frozen published summaries simply do not expose enough matched joint information to apply it.

## What ITER093 establishes

This is not a no-go. It establishes:

1. the exact response matrix that should be measured;
2. the primitive observables required to construct it;
3. why scalar susceptibilities and transition-line slopes are insufficient;
4. how volume fixing must be accounted for;
5. the distinction between finite-volume thermodynamic directions and continuum RG eigendirections.

## Minimal reopening data product

A common Monte Carlo time series, at each selected transition point/volume, containing at least

`N_0, N_41, N_32`

plus `kappa_0,Delta,kappa_4`, volume-fixing parameters and autocorrelation metadata.

From this one can construct

`A=(-N_0,N_41-6N_0,N_41+N_32)`,

estimate the full connected covariance matrix, remove the known external fixing contribution, and study its finite-size eigenstructure without FRG input.

## Highest-information successor

Search for public supplementary/raw CDT Monte Carlo data or author repositories containing matched `N_0,N_41,N_32` time series for the B-C / bifurcation transition studies. If such data exist, preregister the exact response-matrix estimator and compute it reproducibly. If no public dataset exists, record that availability gap explicitly rather than inferring missing cross-covariances from published marginal summaries.

## Claim ceiling

No continuum RG eigenvector, no FRG stability-matrix map, no unique FRG trajectory, no shared fixed point, no bridge derivation and no candidate theory follow.
