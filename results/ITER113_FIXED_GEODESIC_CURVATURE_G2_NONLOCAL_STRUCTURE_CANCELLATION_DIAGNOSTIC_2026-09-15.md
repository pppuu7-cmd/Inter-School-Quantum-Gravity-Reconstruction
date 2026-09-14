# ITER113 terminal result — fixed-geodesic curvature `O(G^2)` nonlocal-structure / cancellation diagnostic

Date: 2026-09-15
Gate: `ITER113_FIXED_GEODESIC_CURVATURE_G2_NONLOCAL_STRUCTURE_CANCELLATION_DIAGNOSTIC`
Preregistration: `53143c5a9d1faea102b97834bb329ff03ec1871f`
Source authority: `fa267ec33645614818c3dc12c2335709d22fc971`
Adversarial review: `6cc14085ac29453eb475f9125a2ed6d58dc51e91`

## Terminal classification

**`PASS_SCOPED_CONTACT_PRUNING_VALID_NONLOCAL_FMG_BASIS_REMAINS_CANCELLATION_OPEN`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main reduction

For the separated fixed-geodesic scalar-curvature correlator, the long-distance `G^2/l^8` information is carried by the nonanalytic part of the momentum-space answer, schematically `q^4 log(q^2/mu^2)` up to local polynomials/contact terms.

This permits safe pruning of:

- momentum-polynomial pieces after renormalization when they are proven to remain local/contact;
- genuinely scaleless tadpoles in dimensional regularization.

It does **not** permit removal of the geodesic localization sectors.

## Mandatory nonlocal basis

The minimum coefficient problem remains

`C_nonlocal = C_F + C_M + C_G`,

where:

- `C_F` = ordinary curvature/field one-loop nonanalytic pieces;
- `C_M` = first-order geodesic/curvature mixed line-integral pieces;
- `C_G` = pure second-order geodesic pieces plus nonlocal finite geodesic-renormalization contributions.

The M/G line integrations generate non-polynomial form factors such as `(exp(i p.l)-1)/(p.l)` and explicitly survive at separated points in the source precedent. They therefore cannot be treated as contact corrections.

## What symmetry does and does not do

Gauge/BRST identities constrain the complete F/M/G sum and supply a strong calculation check. They do **not** protect a nonzero physical coefficient. A complete cancellation of the `O(G^2)` separated tail remains logically/source-wise open until the reduced nonlocal basis is explicitly evaluated.

## Calculation compression achieved

The surviving problem can be organized into a finite family of:

1. massless bubble-type scalar loop integrals;
2. one-geodesic-parameter integrals dressing those loops;
3. two-geodesic-parameter integrals/products from second-order endpoint motion;
4. local polynomial pieces retained only for UV-pole/gauge bookkeeping and then separated from the tail.

No additional source-required nonlocal class appears at this order.

## Exact successor

`ITER114_FIXED_GEODESIC_CURVATURE_G2_TENSOR_FORM_FACTOR_MASTER_BASIS`

Construct a gauge-respecting tensor/form-factor reduction of F/M/G onto the minimal scalar master-integral basis. The gate should determine whether the unknown `G^2/l^8` coefficient can be expressed as a finite linear combination of a small number of bubble and geodesic-parameter master integrals before evaluating them. Longitudinal pieces must be retained until complete gauge cancellation is verified.

## Claim ceiling

No coefficient, cancellation/noncancellation theorem, direct EDT/EFT conflict, continuum EDT, `BRIDGE_DERIVED`, new physics or candidate theory follows.