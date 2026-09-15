# ITER121 terminal result — fixed-geodesic curvature genuine-defect B1 projection authority

Date: 2026-09-15
Gate: `ITER121_FIXED_GEODESIC_CURVATURE_GENUINE_DEFECT_B1_PROJECTION_AUTHORITY`
Preregistration: `6ccfce0ae9eaa5ee9aefed6a92e148126cae5b26`
Source authority: `179fe528b71b2659a2b15d975b77cc0f1eae8d2e`
Adversarial review: `2933251bed06e84341f165a1d5577001b9ea09a7`

## Terminal classification

**`PASS_SCOPED_GENUINE_DEFECT_B1_OUTPUT_ONE_DIMENSION_TWO_INPUT_WEIGHTS_OPEN`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

After the ITER120 field-redefinition quotient, the genuinely new line-defect sector is two-dimensional:

`J_R = int ds Box_perp R`,
`J_S = int ds Box_perp R_nn`.

The separated one-loop logarithmic observable sector is one-dimensional:

`G^2 l^-8 B_1 log(mu^2 l^2)`.

Therefore the most general defect contribution is one projected combination

`Delta B_1 = w_R rho_R + w_S rho_S`,

where `rho_R,rho_S` are the two genuine defect pole/mixing data and `w_R,w_S` are the corresponding scalar projection weights.

## Why symmetry does not reduce the two inputs to one

Using

`R_nn = R/4 + S_nn`

only changes basis. The traceless projection `S_nn` survives because the fixed geodesic supplies a physical tangent `n^mu`; the observable does not average over all tangent directions.

Contracted Bianchi identities constrain divergences of Ricci but do not identify `Box_perp R` with `Box_perp R_nn` on a generic off-shell fluctuating metric. Line reversal preserves both sectors because they are even under `n -> -n`.

No source-qualified symmetry therefore fixes `w_R/w_S` or removes either genuine defect input.

## Minimum explicit calculation

The remaining UV task can be organized in either of two equivalent ways:

1. compute the two genuine defect pole projections separately and combine them; or
2. construct a directly projected scalar UV integrand that contains both tensor structures and yields the single combined `B_1` residue.

The second route is computationally preferable, but it is still a real loop/pole calculation.

The field-redefinition-redundant `int R` and `int R_nn` sectors remain useful as invariance checks but are not independent physical inputs.

## Exact successor

`ITER122_LINEARIZED_CURVATURE_GENUINE_DEFECT_KERNEL_REDUCTION`

Derive in general dimension the exact de-Donder-gauge linearized kernels for the anchor scalar curvature against `R`, `R_nn`, their traceless combination, and the two genuine `Box_perp` defect representatives. Reduce them to the smallest angular polynomial basis in `u=(q.n)^2/q^2` and verify the formulas reproducibly in GitHub Actions. These kernels are projection inputs only; they are not the one-loop pole residues themselves.

## Claim ceiling

No `B_1` value, no noncancellation theorem, no EDT fit or direct EDT/EFT conflict, no bridge, new physics or candidate theory follows.