# ITER097 terminal — CDT response-matrix PSD-bound identifiability

Date: 2026-09-15
Gate: `ITER097_RESPONSE_MATRIX_PSD_BOUND_IDENTIFIABILITY`
Preregistration: `3e929beb98139ae99a5c47e3f9941a7af408b3ec`
Source/mathematical authority: `57436f185ef2120f5ee06a254a8eb9dcf9cad5d6`
Adversarial review: `cc0bc9e6ba4fa36a88bc1986b8696a13f52bfa04`

## Terminal classification

**`NO_GO_SCOPED_MARGINALS_DO_NOT_IDENTIFY_RESPONSE_EIGENDIRECTIONS`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Exact result

For `F=Cov(A)` with `A=(-N_0,N_41-6N_0,N_4)`, covariance positivity gives

`|F_ij| <= sqrt(F_ii F_jj)`

and nonnegative principal minors. These restrictions do not identify the missing cross-covariances.

Already for a principal block

`M=[[d1,c],[c,d2]]`,

the eigendirection satisfies

`tan(2 theta)=2c/(d1-d2)`.

Thus the same diagonal susceptibilities permit:

- `c=0`: coordinate-axis eigendirections;
- `c>0`: rotation in one orientation;
- `c<0`: rotation in the opposite orientation;
- near-saturated `|c|`: large mixed rotations when the diagonals are comparable.

Therefore even exact diagonal susceptibilities do not determine the sign or orientation of the response eigendirections.

## Why published transition slopes do not rescue identifiability

The ITER092 pseudocritical `K_4-Delta` tangent is a transition-locus observable, not a source-defined eigenvector of the thermodynamic/Fisher matrix. Promoting it to one would insert an extra assumption. It also leaves `kappa_0` mixing and the constrained volume direction unresolved.

## Why the three-coupling problem is strictly harder

The full matrix contains three unpublished cross-covariances, while the `kappa_4`/volume row is additionally modified by volume fixing. PSD constraints reduce the allowed family but do not collapse it to a common eigenspace or robust eigenvalue ordering.

## Adversarial outcome

All tested rescue routes fail without new independent information:

- zero-covariance prior;
- maximal-correlation-as-estimator;
- transition-tangent/eigenvector identification;
- dropping the volume row;
- inversion from nonlinear ratio susceptibilities;
- FRG-guided selection of a CDT matrix.

## Scientific consequence

ITER094-ITER096 show that the needed public matched raw data are absent on the frozen discovery surfaces. ITER097 now shows that published marginals cannot mathematically substitute for those data.

The response-matrix branch is therefore saturated under the present public information set unless one obtains either:

1. matched primitive cross-moments/time series; or
2. an independent source-derived structural identity fixing at least one relevant cross-covariance/eigendirection.

No broader physical no-go follows.

## Next high-information route

Shift from the unavailable full covariance matrix to observables that are already source-published as genuinely multivariate or basis-independent quantities. A productive next gate should test whether CDT critical studies publish a Hessian/second derivative, principal-component direction, joint histogram, reweighting Jacobian, or other explicit mixed-response object that contains cross-information without reconstructing raw samples.

If no such object exists, the direct CDT bare-scaling-field route should be marked saturated and research effort reallocated to another cross-school comparator.
