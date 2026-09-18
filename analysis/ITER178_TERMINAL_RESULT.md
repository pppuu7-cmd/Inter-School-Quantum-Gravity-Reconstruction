# ITER178 terminal result — RC007/BH003 mass-deformation spectral-stability selector

Date: 2026-09-19

## Frozen provenance

Preregistration:
`prereg/ITER178_RC007_MASS_DEFORMATION_SPECTRAL_STABILITY_SELECTOR_2026-09-19.md`

Preregistration commit:
`15fcbb8f2b484c840e4d4f1687144637a276f2b0`

Execution head:
`9069bfe88b36248f320ac71f5b7699376071bd2f`

Authoritative GitHub Actions run:
`35404339951`

Aggregate job:
`105791050343`

Aggregate artifact:
`10571429101` (`iter178-aggregate`)

Aggregate artifact digest:
`sha256:69bd30eb7d27e2508f6e5f3f86fcf7342dff3e70ff6f2d792cb23a98d07207ce`

All 16 Researcher jobs, all 16 independent Critic jobs, and the aggregate completed successfully. Green CI is not the scientific classification.

## Frozen scientific question

Could controlled massive deformation of the same 1+1D causal-set free-field Pauli-Jordan object identify a stable spectral break without entropy and without using the source SSEE cutoff during selector construction?

The frozen selector used masses `m=[0,2,5]`, parent sizes `N=[384,512,768,1024]`, new seeds `[211,223,227,229]`, and retained-fraction grid

`[0.04,0.06,0.09,0.13,0.18,0.25,0.35,0.48,0.65,0.82]`.

For each retained fraction the Researcher measured

`I(f)=mean_m[1-||U_0(f)^* U_m(f)||_F^2/r]`.

The independent Critic reconstructed the same quantity through the equivalent principal-angle / orthoprojector-distance identity.

A job-level dynamic break required a prospectively frozen positive slope in `I(f)` versus `log f`, interior to the grid and at least 1.25 times the next-largest positive slope.

## Independent implementation check

`IMPLEMENTATION_VALID = true`.

Researcher and Critic produced all 16/16 expected cases each.

No cases were missing or extra.

The maximum Researcher/Critic disagreement on the instability curve recorded by the aggregate was approximately

`2.31e-15`,

well inside the frozen `1e-9` agreement tolerance.

The two implementations also agreed on break interval and resolved/unresolved classification for every case.

Therefore this is not an implementation or provenance failure.

## Frozen result

`RESOLVED_BREAK_COUNT = 0 / 16`.

`BREAK_INTERVAL_COUNTS = {}`.

`BEST_ADJACENT_CLUSTER_COUNT = 0`.

`SELECTOR_STABLE = false`.

The failure is structurally clear in the raw curves: mass-deformation instability decreases as larger spectral fractions are retained rather than showing the prospectively requested positive-slope onset.

Representative seed 211 curves:

- N=384:
  `0.081106, 0.055182, 0.041297, 0.025556, 0.018419, 0.012785, 0.009120, 0.006922, 0.003936, 0.001521`
- N=512:
  `0.064445, 0.039956, 0.025702, 0.018623, 0.013062, 0.011132, 0.007441, 0.006954, 0.004274, 0.001529`
- N=768:
  `0.040156, 0.026134, 0.017568, 0.011766, 0.009191, 0.006139, 0.005654, 0.003338, 0.001994, 0.000805`
- N=1024:
  `0.030011, 0.019343, 0.013016, 0.008941, 0.006662, 0.004916, 0.004846, 0.002628, 0.001711, 0.000825`

Every adjacent slope in these representative curves is negative.

The adversarial point-label-permutation control is far more disruptive than the physical mass deformation, so the small native deformation signal is not a trivial inability of the metric to detect subspace change. The physical mass deformation simply does not produce the frozen kind of interior instability onset.

## Terminal classification

**`BLOCKED_SCOPED_ITER178_DYNAMIC_BREAK_NOT_STABLY_IDENTIFIED`**

This classification follows the preregistered taxonomy exactly.

It is not `SCIENTIFIC_FAIL_SCOPED_ITER178_MASS_DEFORMATION_DYNAMIC_BREAK_SOURCE_INCOMPATIBLE`, because that class required a stable dynamic break first.

## Source-compatibility stage

`SOURCE_COMPATIBILITY_GATE = NOT_REACHED`.

`POST_SELECTION_POWER_FIT = null`.

`POST_SELECTION_MEDIAN_SELECTED_TO_SOURCE_RATIO = null`.

No claim is made about whether a dynamically selected break would or would not scale as the known source SSEE cutoff `sqrt(N)/(4*pi)`, because ITER178 did not select such a break.

The sign or break definition must not be reversed post hoc to manufacture a breakpoint from the observed monotone decrease. Any alternative dynamical selector would require independent motivation and a new prospective preregistration.

## Scientific consequence

ITER178 closes one additional endogenous-regulator mechanism in the RC007/BH003 same-realization programme:

- simple visible spectral knee: negative;
- closure/compression L-curve: negative;
- Bernoulli-thinning eigenvalue exponent derivation: negative;
- transfer-optimal rank derivation of square-root flow: negative;
- mass-deformation positive-onset spectral-break selector: no stable break.

At the same time, prior positive results remain intact: the externally source-defined spectral sector has strong geometry transfer, suppressed leakage/return defect versus rank-matched random controls, and substantial subspace stability under thinning. ITER178 does not erase those scoped results.

## Claim ceiling

Overall programme remains **50%**.

Candidate theory remains **0 / UNFORMED**.

`bridge_credit=0`.

`BRIDGE_DERIVED=false`.

`NEW_PHYSICS_FOUND=false`.

`NEW_QG_THEORY_REQUIRED=false`.

`ALL_KNOWN_SCHOOLS_FAIL=false`.

`ITER118_MATCHING_AUTHORIZED=false`.

`B1_total=UNAUTHORIZED`.
