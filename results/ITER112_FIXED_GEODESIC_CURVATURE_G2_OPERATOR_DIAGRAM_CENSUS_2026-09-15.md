# ITER112 terminal result — fixed-geodesic scalar-curvature `O(G^2)` operator / diagram census

Date: 2026-09-15
Gate: `ITER112_FIXED_GEODESIC_CURVATURE_G2_OPERATOR_DIAGRAM_CENSUS`
Preregistration: `38e92177aec907b055be86c74239c2496dcd7937`
Source authority: `11c3466ae05c4fb64e1267e3f8e64e95c636078e`
Adversarial review: `3fc14634c52e7deb6e0d2374075bd3b1c4d7df75`

## Terminal classification

**`PASS_SCOPED_FINITE_G2_OPERATOR_DIAGRAM_CENSUS_CALCULATION_READY`**

Scope: anchored fixed-geodesic scalar-curvature two-point function through `O(G^2)`, **not yet** the normalized EDT distance-shell estimator.

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

The missing four-dimensional perturbative calculation is finite and structurally closed at the first potentially noncontact curvature order.

With

`R = kappa R_1 + kappa^2 R_2 + kappa^3 R_3 + ...`

and

`chi = chi_0 + kappa chi_1 + kappa^2 chi_2 + ...`,

the endpoint curvature insertion requires only

`R(chi) = kappa R_1`
` + kappa^2 (R_2 + chi_1.partial R_1)`
` + kappa^3 (R_3 + chi_1.partial R_2 + chi_2.partial R_1 + 1/2 chi_1 chi_1:partial partial R_1)`
` + ...`

for a correlator through `kappa^4 ~ G^2`.

## Closed class structure

All contributions fall into three perturbative localization sectors:

- **F — field/curvature sector:** ordinary curvature vertices, graviton/ghost loops, action interactions and bulk/local counterterms;
- **M — mixed sector:** first-order geodesic localization `chi_1` correlated with curvature/interaction corrections;
- **G — pure geodesic sector:** `chi_2`, `chi_1 chi_1` and associated second-order endpoint terms.

At this order the bulk action needs at most one quartic or two cubic interactions, with the corresponding gauge-fixing/ghost structure. No infinite tower/resummation is required.

## Renormalization split

Two sectors must be kept distinct:

1. ordinary gravitational/curvature-composite EFT renormalization;
2. observable-specific geodesic-embedding renormalization.

The 2018 fixed-geodesic precedent shows that geodesic divergences survive as a separate problem and that field/geodesic contributions can be individually gauge dependent even though the fully renormalized observable is gauge independent.

## Cancellation problem now sharply defined

A cancellation of the complete separated `G^2/l^8` coefficient, if it exists, must occur only after summing every noncontact contribution across F/M/G in one consistent gauge and renormalization convention. Pure contact structures cannot cancel a separated tail.

No EDT exponent is used to select classes or finite counterterms.

## Scope correction from adversarial review

The modern EDT observable contains additional shell-pair measure/normalization fluctuations and an improved distance-dependent connected subtraction. ITER112 does not yet include those. It solves the operator census for the **anchored fixed-geodesic two-point function**, which is the necessary first continuum calculation before a shell-estimator transform.

## Exact successor

`ITER113_FIXED_GEODESIC_CURVATURE_G2_NONLOCAL_STRUCTURE_CANCELLATION_DIAGNOSTIC`

Before evaluating all tensor integrals, classify which F/M/G terms can generate the nonanalytic momentum/position-space structures associated with a separated `G^2/l^8` tail, and test whether gauge/BRST identities or derivative counting force any nonzero linear combination. The successor must not infer cancellation/noncancellation from the EDT `P≈-10` target.

## Claim ceiling

No `O(G^2)` coefficient, no cancellation/noncancellation theorem, no direct EDT/EFT conflict, no continuum EDT, no `BRIDGE_DERIVED`, no new physics and no candidate theory follow.