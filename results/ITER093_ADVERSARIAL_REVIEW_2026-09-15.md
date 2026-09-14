# ITER093 adversarial review — bare-coupling response matrix / scaling-field authority

Date: 2026-09-15
Preregistration: `2f45f30d336ad6ca0a80eb6ff673c134ae95fdcd`
Source authority: `368d343fe769c21ea1a0a9b9eb44360f662a5474`

## Attack 1 — reconstruct off-diagonal entries from published diagonal susceptibilities

In principle,

`Cov(X,Y) = 1/2 [Var(X+Y)-Var(X)-Var(Y)]`.

This can recover a cross-covariance if the three variances are measured at the **same ensemble point** with compatible normalization and errors. The frozen CDT publications do not provide the required matched variance of enough independent linear combinations of the action-conjugate observables. Separate scalar susceptibilities and nonlinear order-parameter variances therefore do not determine the missing matrix entries.

## Attack 2 — use the slope of `K_4^crit` versus `Delta^crit` as the response eigenvector

Rejected as an eigenvector identity. ITER092 supplies an approximately linear tangent to a finite-size pseudocritical trajectory in the `(Delta,K_4)` projection. A tangent to a transition locus is not the same object as an eigenvector of the local connected response/Fisher matrix. The normal direction and possible `kappa_0` mixing are not fixed by that slope.

The slope remains useful qualitative evidence that coordinate axes are mixed, but it cannot replace the missing cross-covariances.

## Attack 3 — ignore the cosmological row and diagonalize a `2x2` `(kappa_0,Delta)` matrix

This could be scientifically useful for a separate two-coupling phase-transition study, but the successor to ITER091/092 specifically asks whether the cosmological response can be disentangled. Projecting out `kappa_4` would not solve that problem.

Moreover, the frozen published studies still do not supply a matched source-qualified `Cov(N_0,N_41-6N_0)` matrix entry at the required transition point in a form sufficient for an eigenvector reconstruction.

## Attack 4 — derive action-observable cross-covariances from nonlinear order parameters such as ratios

Nonlinear order parameters may be related to the primitive simplex counts through a Jacobian, but their covariance transformation still requires a common joint covariance matrix (or raw matched samples). Published separate variances/histograms of ratios do not invert uniquely to the covariance of `(N_0,N_41,N_32)`.

No post-hoc linearization at different scan points can supply the missing common-point matrix without additional data.

## Attack 5 — analytically subtract the Gaussian volume-fixing Hessian from the measured response

In principle this is a promising route. The external fixing potential is known, so its Hessian contribution in the restrained volume direction can be modeled/subtracted if the full matched covariance or inverse susceptibility matrix is available and if the restrained variable (`N_41` versus total `N_4`) is treated exactly.

The blocker is data authority, not algebra: the published summary observables do not expose the required common time series/cross-moments to perform that correction. Thus this attack motivates a raw-data search rather than upgrading ITER093.

## Attack 6 — absence of a published matrix proves there is no mixed scaling direction

Rejected. ITER093 is explicitly not a physics no-go. The formal response matrix exists exactly, and ITER092 already indicates coordinate mixing. The missing item is the source-accessible numerical joint distribution needed to estimate its eigenvectors.

A public raw Monte Carlo dataset containing `N_0,N_41,N_32` and fixing metadata could immediately reopen this gate.

## Attack 7 — finite-volume Fisher eigenvectors are already continuum RG eigendirections

Rejected by scope. Even after the response matrix is reconstructed, its finite-volume eigenvectors are thermodynamic response directions in bare-coordinate space. Continuum RG eigendirections require finite-size scaling, approach to a continuous critical point, and a source-defined relation to the RG stability matrix.

## Verdict

The strongest defensible classification remains

**`PASS_SCOPED_FORMAL_RESPONSE_MATRIX_DATA_AUTHORITY_OPEN`**.

The result is constructive: the exact missing data product is known, and no FRG assumptions are needed to build it. The gate should be reopened only if matched raw/supplementary CDT data or published cross-covariances become available.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.
