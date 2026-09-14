# ITER090 terminal result — fixed-volume Einstein-Hilbert minisuperspace identifiability no-go

Date: 2026-09-15
Gate: `ITER090_FIXED_VOLUME_EH_MINISUPERSPACE_IDENTIFIABILITY_NOGO`
Preregistration: `a5b68cad14d102824777d349be904bba94c19c34`
Source authority: `f3fdf4662f0423730c95811e0b99d02a94ea77e0`
Adversarial review: `3665de31680b67e298f6f030a6652c422acb09ce`

## Terminal classification

**`PASS_SCOPED_ONE_PARAMETER_FIXED_VOLUME_IDENTIFIABILITY_NOGO`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Exact result

The source-defined fixed-volume Einstein-Hilbert minisuperspace action is

`S[v_3] = -(1/(24 pi)) [sqrt(V_4(k))/G_k] I[v_3]`.

For the self-consistent de-Sitter background,

`V_4(k) = (8 pi^2/3) * 81/(lambda_k^2 k^4)`,

while

`G_k=g_k/k^2`.

Therefore

`sqrt(V_4(k))/G_k = 6 sqrt(6) pi/(g_k lambda_k)`,

and hence

**`S[v_3] = -sqrt(6)/(4 g_k lambda_k) I[v_3]`.**

The RG scale cancels and the entire coupling dependence represented by the frozen reduced action has rank one:

**`p_k = g_k lambda_k`.**

## Identifiability consequence

Within this fixed-volume two-coupling Einstein-Hilbert minisuperspace truncation, any correlation function or higher cumulant generated solely by the same reduced action can constrain at most `p_k`.

Measuring more covariance eigenmodes, three-point functions, four-point functions, or other moments of the same normalized global scale-factor/volume distribution cannot separate `g_k` and `lambda_k` unless new coupling dependence enters from outside the frozen action.

This generalizes ITER089 from Gaussian covariance redundancy to an action-level one-parameter identifiability obstruction.

## Scope

The no-go does **not** cover:

- variable-total-volume/grand-canonical response;
- coupling-dependent measure effects not represented by the frozen effective action;
- higher-curvature or other operators beyond Einstein-Hilbert;
- local/non-minisuperspace observables;
- different FRG truncations.

Thus it is a route-selection result, not a no-go theorem for full quantum gravity.

## Consequence for ITER080

The reduced fixed-volume sector cannot by itself remove ITER080's separate-coupling underdetermination. A successful successor must cross the boundary of the fixed-volume EH minisuperspace sector.

## Highest-information successor

Audit the **variable-total-volume / cosmological susceptibility** route. CDT simulations already introduce `kappa_4` conjugate to total four-volume and sometimes relax the volume constraint with a Gaussian fixing term. The next gate should ask whether a source-qualified derivative or susceptibility with respect to the true cosmological source can be related to a renormalized cosmological direction independently of `Gamma` and `omega`, while keeping bare `kappa_4`, critical `kappa_4^c`, and FRG `lambda_k` strictly distinct.
