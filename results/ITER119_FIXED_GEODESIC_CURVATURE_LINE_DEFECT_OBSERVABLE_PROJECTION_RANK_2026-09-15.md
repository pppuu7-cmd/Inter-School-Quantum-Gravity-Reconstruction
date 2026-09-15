# ITER119 terminal result — fixed-geodesic curvature line-defect observable projection rank

Date: 2026-09-15
Gate: `ITER119_FIXED_GEODESIC_CURVATURE_LINE_DEFECT_OBSERVABLE_PROJECTION_RANK`
Preregistration: `85244391af7565af8bffdb1d77d5fa3c12da47c8`
Source authority: `89f32f60c266c31ed86a0cde99186937f6034522`
Adversarial review: `96abda1f2f21f3df06a9cbe3936a0c064c6fb1ff`

## Terminal classification

**`PASS_SCOPED_LINE_DEFECT_OBSERVABLE_PROJECTION_RANK_TWO_MAXIMAL`**

Here `TWO_MAXIMAL` means the separated scalar observable rank is proven `<=2`, while no source-authorized reduction to rank one is available.

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

The internal curvature-decorated line-defect renormalization space may remain four-dimensional,

`(int R, int R_nn, int Box_perp R, int Box_perp R_nn)`,

but corrected ITER114 restricts the complete separated one-loop scalar correlator to

`C(l;mu)=G^2 l^-8[B_0(mu)+B_1(mu) log(mu^2 l^2)]`.

Therefore the map from all allowed line-defect directions into the physical radial output has rank at most two.

## Practical reduction

For the scalar RR observable, all finite/mixing information ultimately enters only two projected combinations:

- `C_fin -> Delta B_0`;
- `C_run -> Delta B_1`.

The full internal mixing matrix may still be required to renormalize the line operator consistently, but it is not the final physical data product.

No theorem currently proves that either projection vanishes, so rank one is not authorized.

## Consequence for calculation order

Because `B_1 != 0` alone would prove a nonzero `O(G^2)` separated tail, the optimal sequence is:

1. compute the projected pole/running combination `C_run`;
2. stop if it gives `B_1 != 0` and the only question is noncancellation;
3. compute the finite projection `C_fin` / `B_0` only if `B_1=0` or if the full function/amplitude is needed.

## Exact successor

`ITER120_FIXED_GEODESIC_CURVATURE_LINE_DEFECT_FIELD_REDEFINITION_AND_LEADING_LOG_AUTHORITY`

Before computing the pole matrix, test whether the four allowed line counterterms are equivalent, at linear curvature order, to local metric field redefinitions evaluated on the geodesic. If so, determine whether this makes the finite projection scheme/observable dependent while leaving the leading-log `B_1` controlled by one-loop pole residues. This can clarify what part of the two-dimensional output is universal within a fixed geodesic observable.

## Claim ceiling

No projected coefficient, no noncancellation theorem, no EDT fit or direct EDT/EFT conflict, no continuum EDT, `BRIDGE_DERIVED`, new physics or candidate theory follows.