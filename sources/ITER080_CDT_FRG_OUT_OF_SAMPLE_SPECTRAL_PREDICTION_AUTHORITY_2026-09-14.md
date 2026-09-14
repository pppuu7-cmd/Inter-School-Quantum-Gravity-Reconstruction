# ITER080 source authority — out-of-sample CDT/FRG spectral prediction from the reduced map

Date: 2026-09-14
Gate: `ITER080_CDT_FRG_OUT_OF_SAMPLE_SPECTRAL_PREDICTION_FROM_REDUCED_MAP`
Preregistration commit: `090fedfb53138cca11eed27321f8304c30860b5f`

## Frozen source stack

Direct reduced CDT↔FRG map:
- arXiv:2408.07808 — J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, D. Németh, *Is Lattice Quantum Gravity Asymptotically Safe? Making contact between Causal Dynamical Triangulations and the Functional Renormalization Group*.
- arXiv:2411.02330 — same authors, *IR and UV limits of CDT and their relations to FRG*.

QEG/FRG spectral machinery:
- arXiv:1110.5224 — M. Reuter, F. Saueressig, *Fractal space-times under the microscope: A Renormalization Group view on Monte Carlo data*.
- arXiv:hep-th/0508202 — O. Lauscher, M. Reuter, *Fractal Spacetime Structure in Asymptotically Safe Gravity*.

Held-out 4D CDT spectral authority:
- arXiv:hep-th/0505113 — J. Ambjørn, J. Jurkiewicz, R. Loll, *Spectral Dimension of the Universe*.
- arXiv:1411.7712 — D. N. Coumbe, J. Jurkiewicz, *Evidence for Asymptotic Safety from Dimensional Reduction in Causal Dynamical Triangulations*.

## Executive result

The ITER078 reduced map does **not** determine enough independent FRG data to generate a finite-scale four-dimensional spectral-dimension prediction without using the target spectral curve itself.

The FRG spectral observable depends on the separate theory-space coordinates `(g_k, lambda_k)`, their beta functions and the chosen RG trajectory. ITER078 fixes a reduced combination proportional to `lambda_k g_k` and reduced geometric/action data, while ITER079 leaves the operational `k` normalization open.

The QEG fixed-point value `D_s = d/2 = 2` in four dimensions is a genuine trajectory-independent asymptotic prediction. However, the frozen sources do not independently establish that the finite-cutoff CDT short-distance data lie in the QEG fixed-point regime. Counting the CDT extrapolation toward a value near two as validation would therefore assume the shared UV regime that the prediction is meant to test.

Source-authority classification:

**`SCOPED_BLOCKED_UNDERDETERMINED_FRG_TRAJECTORY_FROM_REDUCED_MAP`**

Retained positive residual:

**`QEG_ASYMPTOTIC_SPECTRAL_VALUES_SOURCE_QUALIFIED_BUT_NOT_OUT_OF_SAMPLE_MAP_VALIDATION`**.

Bridge credit remains zero.

## A — FRG spectral dependence

**PASS; dependency structure explicitly exposes the blocker.**

The 2011 QEG source defines a local scaling exponent

`delta(k) = k d_k ln(Lambda_bar_k)`

and, as a function on Einstein-Hilbert theory space,

`delta(g,lambda) = 2 + beta_lambda(g,lambda)/lambda`.

The spectral dimension is therefore

`D_s(g,lambda) = 2 d / [4 + beta_lambda(g,lambda)/lambda]`

in the source's scale-dependent approximation.

Thus finite-scale `D_s` is **not** a function of the product `lambda*g` alone. It depends on the separate point `(g,lambda)` and the FRG beta function.

For a complete scale-dependent curve the source solves the coupled flow equations

`k d_k g = beta_g(g,lambda)`,

`k d_k lambda = beta_lambda(g,lambda)`

for specified initial conditions, then inserts the resulting trajectory into the return probability / spectral-dimension calculation.

## B — does ITER078 determine the required FRG state?

**NO.**

ITER078 establishes the reduced relation

`omega^2 Gamma/(omega_0^2 sqrt(N_4)) ~= 1.63 lambda_k g_k`

and maps reduced volume/action data to `V_4(k)` and `G_k` under the source's minisuperspace assumptions.

It does not provide, independently of scale-setting choices:

- a unique decomposition of the dimensionless product into separate `g_k` and `lambda_k` at the spectral evaluation scale;
- a unique Einstein-Hilbert RG trajectory through theory space;
- independently fixed initial conditions for that trajectory;
- the operational `k` corresponding to a held-out CDT diffusion scale.

Therefore the reduced map underdetermines the FRG spectral input.

## C — trajectory / beta-function requirements

**BLOCKING REQUIREMENTS REMAIN.**

The finite-scale spectral curve depends on trajectory data. The 2011 source demonstrates this directly: different initial conditions produce different trajectories and change the extent/location of the classical, semiclassical and fixed-point plateaus.

In the published direct QEG↔CDT spectral comparison the QEG initial conditions are selected by fitting the target Monte-Carlo spectral curve. The source explicitly tabulates the best-fit initial conditions for each triangulation size and notes that they lie on different RG trajectories.

That procedure is valid as a fit, but it is forbidden as out-of-sample prediction by ITER080.

## D — universal fixed-point spectral value

**SOURCE-QUALIFIED ASYMPTOTIC THEORY RESULT; NOT QUALIFIED AS HELD-OUT CDT REGIME.**

The older QEG source derives, in the non-Gaussian fixed-point regime,

`D_s(d) = d/2`,

so in four dimensions

`D_s = 2`.

This value is trajectory-independent within the fixed-point regime.

However, the 2011 source explicitly emphasizes that the finite-cutoff CDT simulations available in its discussion probe scales appreciably away from the continuum/fixed-point limit. It introduces a distinct semiclassical regime precisely to explain dimensional reduction before the UV fixed point is reached.

The held-out CDT sources likewise measure finite lattices and obtain short-distance values by extrapolation/fits outside the strongest lattice-artifact window. The 2005 value `1.80 +/- 0.25` is compatible with two, while the broader 2014 study finds values near `1.5` at several finer-lattice bare-coupling points.

Without an independent demonstration that a given CDT window realizes the QEG NGFP regime, applying `D_s=2` as a validation would violate the fixed-point circularity control.

## E — crossover-scale prediction

**NOT AUTHORIZED.**

Predicting a crossover location requires both:

- a specific FRG trajectory / theory-space point as a function of `k`;
- a physical mapping from FRG `k` (or heat-kernel scale) to the CDT diffusion/lattice scale.

ITER079 leaves the operational `xi_CDT <-> k` relation unresolved, and ITER073 previously left the pointwise spectral physical-scale normalization blocked. No frozen non-spectral source closes this gap.

Horizontal curve shifting or using the target crossover itself to define the scale is forbidden.

## F — target held out

**PASS_CONTROL IN THIS AUDIT.**

No QEG initial conditions, trajectory, `k` normalization or regulator are selected by minimizing disagreement with the held-out four-dimensional CDT spectral curves.

As a consequence, the audit exposes underdetermination rather than manufacturing a fit.

## G — published 3D direct spectral fit

**QUALIFIED AS REPRESENTATIONAL FLEXIBILITY, NOT PREDICTION.**

The 2011 source performs an excellent direct comparison to three-dimensional CDT data. But the QEG trajectory is fitted to the target data through its initial conditions.

This demonstrates that the QEG spectral machinery can represent the observed running `D_s`; it does not validate the ITER078 map out of sample and it cannot be promoted to four dimensions.

## H — held-out 4D CDT data

**QUALIFIED WITH FINITE-LATTICE WINDOWS.**

The four-dimensional CDT sources provide genuine held-out data:

- long-distance spectral dimension consistent with four;
- scale-dependent running toward lower values at short diffusion times;
- later measurements over multiple bare couplings, volumes and relative lattice spacings;
- explicit exclusion/control of strong short-walk odd/even artifacts and finite-size effects.

The data are sufficient to falsify a source-fixed prediction **if one existed**. The blocker is that the frozen reduced map does not uniquely produce one.

## I — asymptotic vs finite-scale/truncation distinction

**PASS_CONTROL.**

The fixed-point `D_s=2` result is retained as an asymptotic QEG statement. Finite-scale spectral curves depend on the Einstein-Hilbert RG trajectory, beta functions and regulator/truncation assumptions.

No asymptotic value is silently treated as a finite-cutoff curve prediction.

## J — validation ceiling

**PASS_CONTROL.**

Because no independent prediction is obtained, ITER080 provides no validation credit to the reduced map. Even a future held-out success would validate only the reduced correspondence in its stated truncation and scale regime.

## Mandatory-control audit

- `TARGET_TRAJECTORY_FIT_CONTROL`: **passes**; no target fitting used.
- `PRODUCT_TO_INDIVIDUAL_COUPLINGS_CONTROL`: **triggers**; `lambda*g` does not determine `(g,lambda)`.
- `MISSING_K_NORMALIZATION_CONTROL`: **triggers**; operational scale normalization remains unresolved.
- `FIXED_POINT_ASSUMPTION_CIRCULARITY_CONTROL`: **triggers**; `D_s=2` cannot validate a shared UV regime unless that regime is independently established.
- `3D_TO_4D_PROMOTION_CONTROL`: **passes**; 3D fit gets no 4D prediction credit.
- `ASYMPTOTIC_FINITE_WINDOW_CONTROL`: **triggers** where applicable; asymptotic and finite-cutoff data remain distinct.
- `REGULATOR_ERASURE_CONTROL`: **passes**.
- `SPECTRAL_SCALE_CIRCULARITY_CONTROL`: **passes**; crossover data do not set their own scale.
- `REDUCED_FULL_VALIDATION_CONTROL`: **passes**.

## Why this is underdetermined-trajectory BLOCKED

The dominant missing object appears before the remaining scale-normalization problem: from the ITER078 source-derived product `lambda_k g_k`, one cannot compute the finite-scale spectral function `D_s(g_k,lambda_k)` or integrate a unique RG trajectory.

Thus even with a hypothetical perfect horizontal scale calibration, the frozen reduced map would still not specify a unique finite-scale spectral prediction.

The preregistered classification is therefore:

**`SCOPED_BLOCKED_UNDERDETERMINED_FRG_TRAJECTORY_FROM_REDUCED_MAP`**.

## Claim ceiling

ITER080 does not refute the ITER078 reduced map; it shows that the map is not yet predictive for a held-out spectral observable. No full-theory equivalence, shared UV fixed point, bridge credit, universal common parent, new physics or candidate theory follows.