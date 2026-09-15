# ITER119 source authority — line-defect observable projection rank

Date: 2026-09-15
Gate: `ITER119_FIXED_GEODESIC_CURVATURE_LINE_DEFECT_OBSERVABLE_PROJECTION_RANK`
Preregistration: `85244391af7565af8bffdb1d77d5fa3c12da47c8`

## 1. Internal defect space remains four-dimensional

ITER118 leaves four independent line-interior curvature sectors at the frozen derivative order:

`I_1=int ds R`,
`I_2=int ds R_nn`,
`I_3=int ds Box_perp R`,
`I_4=int ds Box_perp R_nn`.

Their renormalization/mixing coefficients are not identified with one another by the scalar nature of the final correlator. The internal counterterm problem can therefore remain a nontrivial matrix problem.

Predicate A: **PASS_CONTROL**.

## 2. Separated scalar output space is only two-dimensional

Corrected ITER114 proves that at nonzero separation the complete one-loop result has the form

`C(l;mu)=G^2 l^-8 [B_0(mu)+B_1(mu)L]`,

`L=log(mu^2 l^2)`,

under the frozen massless one-scale assumptions.

Any renormalized contribution of any allowed line operator to this same observable must therefore lie in

`span{f_0,f_1}`,

where

`f_0=G^2 l^-8`,
`f_1=G^2 l^-8 L`.

Thus the linear map from the four line-sector renormalization directions to the separated scalar observable has

**`rank <= 2`**

independently of the rank of the internal four-coupling mixing matrix.

Predicates B,D: **PASS**.
`INTERNAL_MIXING_OBSERVABLE_RANK_SWAP_CONTROL`: **PASS_CONTROL**.

## 3. Finite and running information feed different radial coefficients

At a fixed reference scale, finite renormalized defect couplings can alter the constant separated coefficient `B_0` whenever their renormalized line insertion projects nontrivially onto the scalar correlator.

Their pole residues / beta functions determine the explicit scale compensation and can feed the logarithmic coefficient `B_1`. Corrected ITER116 gives the physical RG hierarchy

`mu dB_1/dmu=0`,
`mu dB_0/dmu=-2B_1`.

Therefore the minimal observable information from the line sector can be organized into two projected scalar combinations:

- `C_fin`: the net finite projection into `B_0`;
- `C_run`: the net pole/running projection controlling the line-sector contribution to `B_1`.

This does not mean individual finite couplings and beta functions are interchangeable.

Predicate C: **PASS_SCOPED**.
`FINITE_RUNNING_COEFFICIENT_SWAP_CONTROL`: **PASS_CONTROL**.

## 4. No source/analytic proof reduces the observable rank to one

A rank-one result would require proving, for the curvature-decorated line observable, either:

1. all line-counterterm beta/pole projections vanish so the line sector cannot feed `B_1`; or
2. all finite separated projections vanish so it cannot feed `B_0`; or
3. a fixed source identity locks the two projections into one universal combination.

None of these is established in the frozen stack.

The matter-scalar fixed-geodesic precedent in fact contains both a running finite geodesic parameter and a logarithmic separated structure, showing that both finite and running defect information can be physically relevant in this class of observables. Its numerical coefficients cannot be imported to curvature, but it prevents assuming a one-dimensional output a priori.

Predicate E: **NO FURTHER REDUCTION AUTHORIZED**.

## 5. Minimum data product for the curvature calculation

To predict the separated scalar correlator one does **not** need every entry of the internal 4x4 mixing matrix as an observable output. It is sufficient to determine the two contractions that project onto the radial basis:

`C_fin -> Delta B_0`,
`C_run -> Delta B_1`.

The full internal matrix may still be required as an intermediate renormalization calculation to derive these contractions consistently and to demonstrate closure/gauge independence.

Thus the practical calculation target is two scalar projected combinations, not four independent physical radial functions.

Predicate F: **PASS_REDUCTION**.

## 6. Target independence

No EDT exponent/amplitude enters the rank argument.

Predicate G: **PASS_CONTROL**.
`EDT_RANK_SELECTION_CONTROL`: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_LINE_DEFECT_OBSERVABLE_PROJECTION_RANK_TWO_MAXIMAL`**

Here `TWO_MAXIMAL` means `rank <= 2` is proven and no source-authorized reduction to rank one is available. It does not assert that both projected directions are numerically nonzero.

## Highest-information successor

Compute the two projected line-sector quantities directly rather than the entire finite mixing matrix if possible:

1. the net pole/running projection `C_run` into `B_1`;
2. only if necessary, the finite projection `C_fin` into `B_0`.

Because `B_1 != 0` would already prove noncancellation, the pole/running projection remains the first target, but it must include the finite counterterm basis established by ITER118.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No projected coefficient is computed, no noncancellation theorem, no EDT fit, no direct EDT/EFT conflict, `BRIDGE_DERIVED`, or new physics follows.