# ITER098 source authority — published multivariate CDT response objects

Date: 2026-09-15
Gate: `ITER098_PUBLISHED_MULTIVARIATE_RESPONSE_OBJECT_AUTHORITY`
Preregistration: `df4e4b7926b563a4e9c1f1b2e3eca01c026321e0`

## Positive source result

The frozen CDT literature does publish genuinely multivariate covariance information.

For spatial-volume fluctuations one defines a time-indexed covariance matrix

`C_tt' = <delta n_t delta n_t'>`,

where `n_t` is the spatial three-volume (or its discrete simplex-count representative) at slice `t`.

The effective-action reconstruction uses the inverse covariance as the Hessian in this projected variable space,

`(C^{-1})_tt' = partial^2 S_eff / (partial n_t partial n_t')`

about the measured background profile, after accounting for the imposed volume-fixing contribution. Toroidal-topology studies explicitly exploit the resulting tridiagonal structure to infer kinetic/potential coefficients of the effective minisuperspace action.

The transfer-matrix programme likewise supplies multivariate/effective dynamical information in a reduced spatial-volume state basis.

## Typing audit

These objects are real cross-information, but their domains are:

- spatial-volume profile variables `n_t`, or
- reduced spatial-volume transfer-matrix states.

They are not covariances of the action-conjugate primitive basis

`A=(-N_0, N_41-6N_0, N_4)`.

The effective spatial-volume action is obtained after integrating out other microscopic degrees of freedom. Its Hessian therefore describes curvature of a projected/effective action with respect to `n_t`, not curvature of `ln Z` with respect to the bare couplings `(kappa_0,Delta,kappa_4)`.

## Missing map

No frozen source provides a Jacobian or exact reconstruction map

`J: {n_t fluctuations / effective-volume variables} -> {A_i bare-action conjugates}`

sufficient to transform the published profile covariance/Hessian into the ITER093 bare-coupling Fisher matrix.

In particular:

1. `N_0` is not determined by the spatial-volume profile alone;
2. `N_41-6N_0` is not a linear functional of the published `n_t` covariance matrix with a source-defined coefficient map;
3. total `N_4=N_41+N_32` and its constrained response require additional microscopic information;
4. integrating out microscopic variables is many-to-one and cannot be inverted from the reduced Hessian alone.

## Inverse covariance control

The fact that `C^{-1}` is a Hessian of the effective spatial-volume action does not make it the inverse or Hessian of the bare-coupling covariance matrix. The indices themselves differ: `(t,t')` versus `(kappa_0,Delta,kappa_4)`.

## Transfer-matrix control

A transfer matrix over spatial volumes or triangulation states is a dynamical/composition object. It is not the thermodynamic Fisher matrix with respect to bare couplings unless a separate source-derived parameter-response map is supplied.

## Predicate adjudication

- A explicit cross-information exists: **PASS**.
- B domain/basis explicitly identified: **PASS**.
- C source-defined map to ITER093 action-conjugate basis: **NO**.
- D no inversion of integrating-out projection: **PASS_CONTROL**.
- E no effective-Hessian/bare-Hessian swap: **PASS_CONTROL**.
- F transfer-matrix typing preserved: **PASS_CONTROL**.

## Classification

`PASS_SCOPED_MULTIVARIATE_OBJECT_EXISTS_DIFFERENT_DOMAIN`

This is a positive structural result: CDT has published multivariate covariance/Hessian objects, but they do not supply the missing bare-coupling cross-covariances required by ITER093.

Bridge credit remains `0`. Candidate theory remains `UNFORMED / 0%`.
