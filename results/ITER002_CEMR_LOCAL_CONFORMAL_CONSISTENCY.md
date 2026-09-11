# Iter002 Result — Local CEMR Conformal-Consistency Obstruction

Status: `DERIVED_ISQGR / DOMAIN_SCOPED`  
Date: 2026-09-12

## 1. Problem

BH-002 proposes combining:

- a causally reconstructed conformal metric class `[g]`;
- independent quantum-information geometric data, e.g. leading-order RT area data;

to reconstruct a full Lorentzian metric.

Before solving the global nonlinear inverse problem, there is a cheaper necessary local consistency test.

## 2. Setup

Work in a `D`-dimensional semiclassical Lorentzian region where causal structure determines a conformal class. Choose any representative

`g_bar`.

The physical metric, if compatible with that causal class, is

`g = Omega(x)^2 g_bar`.

Consider sufficiently small codimension-2 surface patches `Sigma_i` through a neighborhood of the same point `x`, small enough that `Omega` is approximately constant across each patch.

Their induced areas satisfy

`A_i[g] ~= Omega(x)^(D-2) A_i[g_bar]`.

For `D=4`,

`A_i[g] ~= Omega(x)^2 A_i[g_bar]`.

## 3. Entanglement-derived area channel

In a leading semiclassical RT-type domain and natural units,

`A_i^obs = 4 G_N S_i`,

where `S_i` is the appropriate entanglement entropy associated with the geometric surface data.

This identification is **domain scoped**. Generalized entropy / QES corrections are not neglected outside their controlled regime.

Each patch then independently estimates

`Omega_i(x) = ( A_i^obs / A_i[g_bar] )^(1/(D-2))`.

In `D=4`,

`Omega_i(x) = sqrt( 4 G_N S_i / A_i[g_bar] )`.

## 4. Necessary compatibility condition

If a single conformal factor completes the causally reconstructed metric, then all sufficiently local patches through `x` must agree:

`Omega_1(x) = Omega_2(x) = ...`

within theoretical/measurement uncertainty.

Equivalently define

`r_i = log(A_i^obs / A_i[g_bar])`.

Then a compatible conformal factor requires

`r_i = (D-2) log Omega(x)`

independent of patch orientation/label.

The local obstruction residual is

`delta_i = r_i - mean(r)`.

Nonzero structured residuals imply that **no single local conformal rescaling of the causally reconstructed metric can reproduce all supplied area data**.

## 5. Conformal-gauge invariance of the obstruction

The representative `g_bar` is arbitrary inside its conformal class.

Under

`g_bar -> exp(2 chi(x)) g_bar`,

local codimension-2 areas transform as

`A_i[g_bar] -> exp((D-2) chi(x)) A_i[g_bar]`.

Therefore

`r_i -> r_i - (D-2) chi(x)`.

All `r_i` receive the **same local additive shift**, so

`delta_i = r_i - mean(r)`

is unchanged.

Thus the patch-to-patch inconsistency test is independent of the arbitrary conformal representative to the accuracy of the local-patch approximation.

This is the first concrete ISQGR obstruction quantity derived from combining the two school-native reconstruction channels.

## 6. Weighted statistical version

With independent uncertainties `sigma_{r_i}`, estimate

`r_bar = sum_i w_i r_i / sum_i w_i`,

`w_i = 1/sigma_{r_i}^2`.

Then

`chi2_CEMR = sum_i (r_i-r_bar)^2 / sigma_{r_i}^2`

with nominal `dof = N-1` when the assumptions of independent approximately Gaussian errors are valid.

A large `chi2_CEMR` is an **incompatibility diagnostic**, not automatically evidence for new physics: the failure may come from RT/QES corrections, bad localization, wrong surface identification, incorrect `G_N`, or a non-overlapping applicability domain.

## 7. Error propagation

For

`A_i^obs = 4 G_N S_i`,

an approximate relative log-area uncertainty is

`sigma_r_i^2 ~= (sigma_G/G_N)^2 + (sigma_S_i/S_i)^2 + (sigma_Abar_i/Abar_i)^2`

plus any covariance/systematic terms.

Correlated errors require the covariance generalization

`chi2 = delta^T C^(-1) delta`.

The first executable implementation uses the diagonal version and fails closed when positive inputs/uncertainties are not supplied consistently.

## 8. Interpretation

### PASS_LOCAL

All patch estimates agree within the declared domain/uncertainty. This is **necessary but not sufficient** for CEMR.

### TENSION_LOCAL

Residuals are nonzero but plausibly attributable to finite-patch, QES, calibration or mapping uncertainty. Refine the model before physical interpretation.

### INCOMPATIBLE_LOCAL

No single local conformal factor fits the supplied causal-class representative and independent area data within a controlled error model.

This rejects that CEMR realization in scope; it does not refute causal sets, holography, or entanglement reconstruction as families.

## 9. Why this matters

This test converts the inter-school synthesis into a falsifiable relation:

`causal conformal class + independent area data -> one common local scale field`.

The two inputs cannot be independently fitted once the surface correspondence and calibration are fixed.

## 10. Next strengthening

1. Replace the local constant-`Omega` approximation by finite-surface integral inversion.
2. Include covariance between entropy/area channels.
3. Add generalized-entropy/QES corrections.
4. Test a synthetic geometry where `Omega(x)` is known.
5. Search for uniqueness/stability conditions for the global CEMR inverse problem.

Code: `code/cemr_local_consistency.py`.
