# ITER080 adversarial critic — out-of-sample spectral prediction from the reduced CDT/FRG map

Date: 2026-09-14
Preregistration: `090fedfb53138cca11eed27321f8304c30860b5f`
Source-authority audit: `b06804cf5f1d9582bfb8f99a2728f349e9528bd9`

## Target

Attempt to falsify or strengthen:

`SCOPED_BLOCKED_UNDERDETERMINED_FRG_TRAJECTORY_FROM_REDUCED_MAP`.

## Attack 1 — the mapped product lambda*g should be enough because Ds is dimensionless

Dimensionlessness does not imply dependence only on dimensionless products. In the frozen QEG machinery

`D_s(g,lambda) = 2d/[4 + beta_lambda(g,lambda)/lambda]`.

The Einstein-Hilbert beta function contains separate nonlinear dependence on `g` and `lambda`, including threshold functions evaluated at arguments involving `lambda`. Two theory-space points with the same product `g lambda` can therefore yield different `beta_lambda/lambda` and different finite-scale spectral dimensions.

**Verdict: `PRODUCT_TO_INDIVIDUAL_COUPLINGS_CONTROL` is decisive.**

## Attack 2 — ITER078 also maps V4(k) and Gk, so solve for Lambda_k, then recover gk and lambda_k

At the reduced de-Sitter level, `V_4(k)` can constrain the dimensionful cosmological scale and the action map gives `G_k`, subject to the lattice-spacing/geometric normalization assumptions. But the dimensionless coordinates remain

`g_k = k^2 G_k`,

`lambda_k = Lambda_k/k^2`.

Without the operational `k` fixed independently, the same dimensionful `(G_k,Lambda_k)` corresponds to different dimensionless points as `k` changes, while the product `g_k lambda_k = G_k Lambda_k` remains invariant.

ITER079 is exactly the authority that leaves this operational `k` unresolved.

**Verdict: no unique theory-space point; blocker survives.**

## Attack 3 — use the universal QEG fixed-point value Ds=2 as an out-of-sample prediction

`D_s=2` in four dimensions is a genuine source-derived asymptotic QEG result and is independent of the particular trajectory once the NGFP regime is reached.

But the held-out CDT measurements are finite-cutoff data. The QEG spectral source explicitly warns that the available CDT scales need not be in the NGFP regime; indeed the paper introduces a semiclassical plateau precisely to explain strong dimensional reduction before fixed-point scaling is reached.

The 2005 CDT extrapolation `D_s(0)=1.80 +/- 0.25` is compatible with two, but the broader 2014 study finds short-distance extrapolations around `1.5` at several finer bare-coupling points. Selecting whichever finite-lattice window looks closest to two and declaring it the NGFP regime would assume the cross-theory UV identification being tested.

**Verdict: asymptotic theory value retained, no out-of-sample validation credit.**

## Attack 4 — the three QEG plateaus 4, 4/3, 2 predict the qualitative CDT curve

The QEG spectral machinery indeed has classical, semiclassical and NGFP scaling regimes whose plateau values are source-derived in the Einstein-Hilbert analysis. But the **location and extent** of the plateaus depend on the RG trajectory. Without independent trajectory/scale selection, observing a running CDT curve between roughly four and lower values does not identify which QEG regime corresponds to which diffusion window.

Moreover, the held-out CDT data do not display a unique clean sequence of all three asymptotic plateaus inside one controlled continuum scale range.

**Verdict: useful qualitative mechanism, not a falsifiable out-of-sample prediction from ITER078.**

## Attack 5 — the later CDT value near 1.5 is close to the QEG semiclassical value 4/3

Numerical proximity alone does not supply regime identity. The QEG semiclassical plateau occurs in a specific region of its RG trajectory. Assigning the CDT short-distance extrapolation to that region because the numbers are close is post-hoc regime selection.

The same frozen QEG source used a target-fitted 3D trajectory to demonstrate this kind of correspondence; ITER080 prospectively forbids using the 4D target data to select the analogous trajectory/regime.

**Verdict: no prediction credit.**

## Attack 6 — use the classical IR value Ds=4 as a successful held-out prediction

Both QEG and 4D CDT approach spectral dimension near four on sufficiently long scales. This is a genuine consistency check of macroscopic dimensionality, but it does not test the new ITER078 reduced map: `D_s=4` is the generic classical four-dimensional limit and does not require the mapped parameter combination.

ITER080 is specifically a validation test of the reduced crosswalk. A result independent of that crosswalk cannot validate it.

**Verdict: positive background consistency only, not gate PASS.**

## Attack 7 — pick a representative point on the hyperbola g lambda = const and propagate an error band

This would insert an unregistered prior over the missing theory-space direction. Unless a frozen non-spectral source bounds that direction, the resulting spectral band is researcher-chosen rather than source-predicted.

The 2011 source demonstrates that varying initial conditions changes the trajectories and spectral plateaus. A broad arbitrary family that is guaranteed to contain the data has no falsification value.

**Verdict: forbidden under trajectory-fit/product controls.**

## Attack 8 — the published 3D percent-level fit calibrates the missing trajectory rule once and can then be transferred to 4D

The 3D QEG trajectory was selected by fitting the 3D target spectral data, and the best-fit initial conditions change with triangulation size. No source-derived dimension-independent rule maps ITER078 CDT parameters to those fitted initial conditions.

Transferring a target-fitted 3D prescription to 4D would additionally violate the dimensional-scope control.

**Verdict: no 4D out-of-sample authority.**

## Attack 9 — classify as `PASS_SCOPED_ASYMPTOTIC_SPECTRAL_PREDICTION_ONLY`

That classification requires not only a universal QEG asymptotic value but source-qualified applicability to the held-out CDT regime independent of assuming the shared fixed point. This second condition is not satisfied.

The asymptotic values are source-qualified **QEG predictions**, but they are not predictions of the ITER078 CDT↔FRG map until the map independently places the CDT ensemble in the corresponding QEG regime.

**Verdict: no asymptotic gate PASS.**

## Attack 10 — classify as FAIL because the finer CDT short-distance values are not 2

Too strong. There is no source-fixed finite-scale prediction to falsify. The finer CDT values could correspond to a semiclassical/crossover regime rather than the NGFP, and the frozen map does not determine the regime.

A mismatch against an inapplicable asymptotic value cannot reject the reduced map.

**Verdict: BLOCKED, not FAIL.**

## Critic verdict

**CONFIRMS `SCOPED_BLOCKED_UNDERDETERMINED_FRG_TRAJECTORY_FROM_REDUCED_MAP`.**

Durable factorization:

- `COMMON_SPECTRAL_OBSERVABLE_DEFINITION = qualified`
- `ITER078_REDUCED_PARAMETER_PRODUCT_MAP = qualified_scoped`
- `QEG_DS_REQUIRES_SEPARATE_G_LAMBDA_AND_BETA_FUNCTION = true`
- `UNIQUE_FRG_TRAJECTORY_FROM_REDUCED_MAP = absent`
- `OPERATIONAL_K_NORMALIZATION = absent`
- `QEG_UV_DS_EQUALS_2 = source_qualified_asymptotic`
- `QEG_SEMICLASSICAL_DS_EQUALS_4_OVER_3 = source_qualified_regime`
- `APPLICABILITY_OF_EITHER_TO_HELD_OUT_4D_CDT_WINDOW = not_independently_established`
- `OUT_OF_SAMPLE_4D_SPECTRAL_VALIDATION = blocked`
- `BRIDGE_CREDIT = 0`

## Successor decision

ITER080 shows that the next missing object is not another spectral curve but a **second independent reduced observable capable of resolving the one-dimensional degeneracy left by the mapped product `lambda_k g_k` and/or fixing `k`**.

A high-information successor should ask whether the same CDT ensembles contain an independent dimensionless observable that the frozen FRG Einstein-Hilbert sector predicts as a function of the ratio or separate values of `g_k` and `lambda_k`, without reusing the scale-factor action itself.

Potential candidates must be source-audited prospectively; curvature cannot be assumed because ITER077 rejected QRC/background-curvature identity.

Recommended next gate:

`PREREGISTER_ITER081_CDT_FRG_SECOND_INDEPENDENT_REDUCED_OBSERVABLE_FOR_THEORY_SPACE_POINT`.

The first task of ITER081 should be source discovery/authority: identify whether such an observable exists at all before any numerical fitting.