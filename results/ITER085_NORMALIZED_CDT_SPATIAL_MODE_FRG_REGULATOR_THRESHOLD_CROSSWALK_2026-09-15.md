# ITER085 terminal result — normalized CDT spatial mode ↔ foliated-FRG regulator threshold

Date: 2026-09-15
Gate: `ITER085_NORMALIZED_CDT_SPATIAL_MODE_FRG_REGULATOR_THRESHOLD_CROSSWALK`
Preregistration: `c5abaa46cdc5a32801b469fb195e4aa2e8d455f1`
Workflow launch: `3327a99444cf0951c9580910031cef22c0aab4b9`
Source authority: `ff5c24e32e9757fd533edd0878b11e73e4d8f67b`
Adversarial review: `f91f9b83b6b15f73bee106547e3e160288643b42`

## Terminal classification

**`PASS_SCOPED_BACKGROUND_SPATIAL_THRESHOLD_ROUTE_PRODUCTION_COVARIANT_OPEN`**

Retained production sub-result: **`PRODUCTION_COVARIANT_SUPPORT_ENVELOPE_FROM_SPATIAL_EIGENVALUE`**.

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

Combining the independently normalized CDT spatial eigenvalue from ITER084,

`z_CDT = 9 lambda_graph/a^2`,

with the source-defined background foliated-FRG spatial coarse-graining operator and Litim regulator yields the target-independent dimensionless probe variable

`x_CDT(k) = z_CDT/k^2 = 9 lambda_graph/(a^2 k^2)`.

For the background-spatial regulator route:

- `x_CDT < 1`: the mode lies inside Litim regulator support;
- `x_CDT = 1`: scheme-defined threshold;
- `x_CDT > 1`: the mode lies outside support.

Equivalently, the threshold scale for the normalized spatial mode is

**`k_thr = sqrt(z_CDT) = 3 sqrt(lambda_graph)/a`**.

This is not `k=1/a`; it is mode-dependent and regulator-scheme dependent.

## Production-flow distinction

The 2023 fluctuation calculation does not implement the background spatial regulator. Its adopted profile is covariant in the regulator argument,

`R_k(q^2)=(k^2-q^2) Theta(k^2-q^2)`,

with

`q^2 = q0^2 + vec(q)^2`.

Therefore a CDT spatial eigenvalue alone is not a complete eigenvalue of the production coarse-graining operator. External projection onto `vec(p)^2` does not remove temporal loop momentum.

Nevertheless, a normalized spatial eigenvalue gives an exact support envelope:

`q0^2 + z_CDT < k^2`.

Hence:

- for `z_CDT >= k^2`, no temporal mode associated with that spatial sector can lie in regulator support;
- for `z_CDT < k^2`, supported temporal modes obey
  `|q0| < sqrt(k^2-z_CDT)`.

This is useful production information, but it is weaker than a full spatial-mode identity.

## What changed relative to ITER080/082

ITER082's broad operator-type candidate and ITER084's local geometric normalization now combine into a genuine **regulator-probe scale relation** on the background-spatial FRG route. The FRG probe scale for a CDT spatial eigenmode is no longer arbitrary up to an unknown local multiplicative constant.

One component of the older ITER080 obstruction is therefore narrowed: a scheme-qualified `k` can now be assigned to a normalized CDT spatial mode at the regulator threshold without imposing `k=1/a`.

The other ITER080 obstruction remains untouched: this mode threshold does not determine the separate running couplings `(g_k,lambda_k,...)` or select a unique FRG trajectory.

## Residual type ceiling

ITER084 did not prove global spectral convergence/eigenfunction identity between fluctuating CDT slices and a smooth FRG background. Thus `z_CDT` is authorized here as a normalized **probe argument**, not as proof of equality of global spectral geometries.

## Claim ceiling

No unique FRG trajectory, no `k=1/a`, no production spatial-regulator identity, no shared UV fixed point, no theory equivalence, no bridge derivation and no candidate theory follow.

## Highest-information successor

The next gate should return to the ITER080 underdetermination with the new mode-probe scale held fixed prospectively. It should ask whether the already-qualified reduced CDT↔FRG map from ITER078, evaluated at an independently assigned `k_thr`, determines enough FRG coupling information for a **held-out, target-independent prediction**, or whether the map still constrains only combinations such as `g_k lambda_k` and leaves a one-parameter family of trajectories.

No CDT held-out spectral value may be used to solve for the remaining FRG coupling freedom.
