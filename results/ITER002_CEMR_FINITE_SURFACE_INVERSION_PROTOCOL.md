# ITER002 — CEMR finite-surface inversion protocol

Status: **PRE-REGISTERED / COMPUTATION PENDING**

Bridge: `BH-002_CAUSAL_ENTANGLEMENT_METRIC_RECONSTRUCTION`

## Purpose

This is the first finite-surface inverse-problem test of the CEMR branch. It deliberately starts one level below the full RT/QES problem: codimension-two surfaces are held fixed in the reference conformal geometry. Therefore it can test **conformal-scale identifiability, obstruction and nuisance separation**, but it cannot yet establish full extremal-surface metric reconstruction.

For four-dimensional spacetime,

\[
A_i[\Omega] = \int_{\Sigma_i}\Omega(x,y)^2\,dA_{\bar g}.
\]

The synthetic conformal field is parameterized as

\[
\log\Omega(x,y)=\theta_0+\theta_1x+\theta_2y+\theta_3xy.
\]

No result is permitted to change this parameterization after looking at the output of the registered campaign.

## Registered scenarios

### C1 — clean calibrated reconstruction

Redundant finite surfaces are generated from a known `theta_true`. A calibrated log-area likelihood fits the four conformal parameters.

Required result for scoped support:
- full Jacobian rank;
- reduced chi-square <= 4;
- max absolute parameter error < 0.02 in the unit test realization.

A failure is a failure of this Stage-I implementation/domain, not a failure of CEMR in general.

### C2 — unknown global scale

An additional global log-area calibration parameter `beta` is fitted.

Because a constant shift of `theta0` changes every D=4 log area by `2 theta0`, while `beta` also shifts every log area uniformly, the two are expected to be exactly non-identifiable. The registered interpretation is:

`BLOCKED_NONIDENTIFIABLE`, **not physical failure**.

This directly operationalizes BH-002 blocker B4: an independent scale / `G_N` calibration is required before an absolute conformal scale can be reconstructed.

### C3 — unmodelled channel anisotropy

Every geometric surface is measured twice with channel labels +/-1. Synthetic observations receive an opposite log-area distortion `+/- epsilon`, while the fitted model contains only the scalar conformal field.

Because the duplicated surfaces have identical geometry, no scalar `Omega(x,y)` can make their areas differ. Registered scoped incompatibility criterion:

- full-rank geometric fit;
- reduced chi-square > 9.

This is a falsification control against absorbing arbitrary non-geometric structure into the conformal field.

### C4 — profiled channel nuisance

The same distorted data are fitted with an explicit channel nuisance `alpha`.

If the nuisance signature is independently identifiable, it should remove the false geometric tension. This tests the DSIR-style nuisance-quotient principle inside CEMR rather than declaring any residual disagreement to be new geometry.

## Campaign grid

Seeds: `101, 211, 307`.

Scenarios:
- `clean_calibrated`
- `global_scale_nuisance`
- `channel_anisotropy`
- `channel_profiled`

Default registered injection:
- `epsilon = 0.05`
- `sigma_log_area = 0.003`

This is 12 independent synthetic fits plus unit tests.

## Outputs

Every job must report:
- fitted parameters;
- nuisance estimate when applicable;
- chi-square and reduced chi-square;
- numerical Jacobian rank;
- singular values / condition number;
- maximum conformal-parameter error;
- fail-closed classification.

## Claim lock

Even a complete PASS of C1/C3/C4 plus the expected C2 rank obstruction would establish only:

1. finite fixed-surface conformal inversion is executable in this controlled model;
2. absolute conformal scale is structurally non-identifiable without independent calibration;
3. a duplicated-surface anisotropic inconsistency cannot be hidden inside a scalar conformal field;
4. a separately parameterized nuisance can be profiled when its signature is identifiable.

It would **not** establish:
- full RT/QES inversion;
- causal-order + entanglement sufficiency for a Lorentzian metric;
- uniqueness in continuum quantum gravity;
- a new quantum-gravity theory;
- new physics.

The next level, if this protocol survives, is metric-dependent extremal surfaces followed by QES/generalized-entropy nuisance structure and a wrong-conformal-class challenge.
