# ITER080 terminal result — out-of-sample spectral prediction from the reduced CDT/FRG map

Date: 2026-09-14
Gate: `ITER080_CDT_FRG_OUT_OF_SAMPLE_SPECTRAL_PREDICTION_FROM_REDUCED_MAP`
Preregistration commit: `090fedfb53138cca11eed27321f8304c30860b5f`
Source-authority commit: `b06804cf5f1d9582bfb8f99a2728f349e9528bd9`
Adversarial-critic commit: `6fa3b295f716738b962444cbaedf101fd826c88e`

## Terminal classification

**`SCOPED_BLOCKED_UNDERDETERMINED_FRG_TRAJECTORY_FROM_REDUCED_MAP`**

Retained positive residual:

**`QEG_ASYMPTOTIC_SPECTRAL_VALUES_SOURCE_QUALIFIED_BUT_NOT_OUT_OF_SAMPLE_MAP_VALIDATION`**

Bridge credit: **0**.

## Question adjudicated

Does the source-qualified ITER078 reduced CDT↔FRG map determine enough FRG theory-space information to predict a held-out four-dimensional CDT spectral-dimension feature without fitting the target spectral data?

## Result

No.

The blocker is stronger than the already-known missing horizontal scale normalization: the reduced map does not determine a unique FRG theory-space point or trajectory needed for the finite-scale spectral calculation.

## Exact mathematical blocker

The frozen QEG spectral machinery defines

`delta(g,lambda) = 2 + beta_lambda(g,lambda)/lambda`

and

`D_s(g,lambda) = 2d/[4 + beta_lambda(g,lambda)/lambda]`.

Therefore finite-scale spectral dimension depends on the separate coordinates `(g,lambda)` and the beta function, not merely on the product `g lambda`.

A full running curve requires solving

`k d_k g = beta_g(g,lambda)`,

`k d_k lambda = beta_lambda(g,lambda)`

for a specified RG trajectory / initial conditions.

ITER078 source-qualifies the reduced combination

`omega^2 Gamma/(omega_0^2 sqrt(N_4)) ~= 1.63 lambda_k g_k`,

but it does not, independently of the unresolved scale choice, determine the separate dimensionless coordinates or a unique trajectory.

## Why V4 and Gk do not remove the degeneracy

The direct reduced map also supplies dimensionful `V_4(k)` and `G_k` under its minisuperspace assumptions. In principle the de-Sitter volume constrains a dimensionful cosmological scale. But the dimensionless coordinates remain

`g_k = k^2 G_k`,

`lambda_k = Lambda_k/k^2`.

Without an independently operational `k`, the same dimensionful reduced data do not select a unique point `(g_k,lambda_k)` even though their product remains fixed.

ITER079 explicitly leaves this operational scale map open.

## Universal QEG spectral values

The QEG sources contain genuine parameter-independent asymptotic/regime results, including in four dimensions:

- classical regime: `D_s = 4`;
- semiclassical Einstein-Hilbert scaling regime: `D_s = 4/3`;
- non-Gaussian fixed-point regime: `D_s = 2`.

These remain valuable source-qualified predictions of the QEG spectral mechanism.

They do **not** become out-of-sample validation of ITER078 because the frozen non-spectral map does not independently assign the held-out CDT finite-lattice windows to those QEG regimes.

## Held-out 4D CDT data

The frozen CDT sources provide genuine held-out spectral data:

- long-distance values compatible with four;
- running dimension at shorter diffusion scales;
- the original short-distance extrapolation `D_s(0)=1.80 +/- 0.25`;
- later multi-coupling measurements with short-distance extrapolations near `1.5` for several finer-lattice points;
- explicit short-walk artifact and finite-size controls.

These data could falsify a source-fixed prediction. ITER080's problem is that the reduced map does not uniquely generate one.

## Why the fixed-point value 2 is not counted as PASS

The QEG fixed-point result `D_s=2` is trajectory-independent **conditional on being in the NGFP regime**.

The frozen spectral source explicitly warns that finite-cutoff CDT data need not yet probe that regime and introduces a semiclassical scaling regime to explain dimensional reduction before the fixed point is reached.

Declaring the CDT short-distance window to be the NGFP regime because its extrapolated dimension happens to approach two would assume the shared UV identification being tested.

The 2014 CDT measurements also demonstrate why such a promotion would be unsafe: finer-lattice bare-coupling points yield extrapolations closer to `1.5` than to two.

## Published 3D fit

The 2011 QEG paper obtains excellent agreement with three-dimensional CDT data by fitting the QEG trajectory's initial conditions to the target spectral curve. It explicitly tabulates these best-fit initial conditions and observes that different triangulation sizes select different RG trajectories.

This is strong representational evidence but not out-of-sample validation and cannot be promoted to four dimensions.

## Frozen predicate results

- A — explicit FRG spectral dependence: **PASS**.
- B — ITER078 uniquely determines required FRG inputs: **NO**.
- C — separate couplings / trajectory / `k` independently fixed: **NO**.
- D — asymptotic fixed-point value applicable to held-out CDT window independently: **NO**.
- E — crossover-scale prediction independently normalized: **NO**.
- F — target held out: **PASS_CONTROL**.
- G — 3D target-fit kept separate: **PASS_CONTROL**.
- H — 4D held-out data qualified: **PASS**.
- I — asymptotic/finite-scale and regulator distinction retained: **PASS_CONTROL**.
- J — validation ceiling retained: **PASS_CONTROL**.

This predicate pattern maps to:

**`SCOPED_BLOCKED_UNDERDETERMINED_FRG_TRAJECTORY_FROM_REDUCED_MAP`**.

## Adversarial critic

The critic attempted to rescue prediction by:

- treating the mapped product `g lambda` as sufficient;
- solving for dimensionful `G,Lambda` and pretending that this fixes dimensionless `(g,lambda)` without `k`;
- using the universal `D_s=2` fixed-point value;
- treating the three QEG plateaus as a qualitative prediction;
- post-hoc identifying the CDT values near `1.5` with the QEG `4/3` semiclassical plateau;
- using the classical `D_s=4` limit as map validation;
- selecting an arbitrary point on the mapped hyperbola;
- transferring the target-fitted 3D rule to four dimensions.

None creates an independent finite-scale prediction.

The critic also rejected a FAIL classification because there is no unique source-fixed prediction to falsify.

Critic verdict: **CONFIRMS terminal classification**.

## Structural consequence

The direct reduced crosswalk has now passed one important test and failed another in a precise sense:

- it is a source-defined equation-level reduced action/parameter map;
- it is not yet sufficiently determined to predict an independent spectral observable.

The missing degrees of freedom are:

1. separation of the mapped product `lambda_k g_k` into the individual FRG theory-space coordinates needed for `D_s`;
2. selection of a unique RG trajectory;
3. independent operational normalization of `k` relative to the CDT scale.

## Next admissible gate

The next gate should first determine whether a **second independent reduced observable** exists that can constrain the missing theory-space direction without reusing the scale-factor action or spectral target.

Recommended successor:

**`PREREGISTER_ITER081_CDT_FRG_SECOND_INDEPENDENT_REDUCED_OBSERVABLE_FOR_THEORY_SPACE_POINT`**

This should begin as source-authority/discovery, not as numerical fitting. Curvature cannot be assumed to supply the observable because ITER077 rejected the frozen QRC/background-curvature identity.

## Claim locks

- `ITER078_REDUCED_CROSSWALK = true_scoped`
- `OUT_OF_SAMPLE_4D_SPECTRAL_PREDICTION = false`
- `UNIQUE_FRG_TRAJECTORY_FROM_REDUCED_MAP = false`
- `OPERATIONAL_K_NORMALIZATION = false`
- `QEG_ASYMPTOTIC_DS_VALUES = source_qualified`
- `FULL_THEORY_EQUIVALENCE = false`
- `SHARED_UV_FIXED_POINT_ESTABLISHED = false`
- `BRIDGE_DERIVED = false`
- candidate theory = `UNFORMED / 0%`
- bridge credit = `0`