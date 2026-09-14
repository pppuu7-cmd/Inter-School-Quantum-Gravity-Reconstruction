# ITER113 source authority — fixed-geodesic curvature `O(G^2)` nonlocal-structure diagnostic

Date: 2026-09-15
Gate: `ITER113_FIXED_GEODESIC_CURVATURE_G2_NONLOCAL_STRUCTURE_CANCELLATION_DIAGNOSTIC`
Preregistration: `53143c5a9d1faea102b97834bb329ff03ec1871f`

## 1. Separated `l^-8` tail ↔ nonanalytic `q^4 log q^2` structure

In four Euclidean dimensions, after distributional renormalization, the Fourier transform of a separated `1/l^8` behavior is represented by

`q^4 log(q^2/mu^2)`

up to scheme-dependent local polynomials in `q^2`. Conversely, a pure polynomial in external momentum Fourier transforms only to delta functions and derivatives at coincidence.

Therefore the coefficient relevant to the long-distance `G^2/l^8` tail can be isolated from the nonanalytic part of the renormalized momentum-space correlator.

Predicate A: **PASS**.

## 2. Contact pruning is valid for proven local analytic structures

The 2026 relational curvature calculation explicitly separates analytic momentum-space terms from the universal noncontact piece: the former become contact distributions after Fourier transformation, while the latter produces the separated power law.

Accordingly, ordinary local EFT counterterms whose contribution is polynomial in the external momentum can be removed from the **separated-tail coefficient** after they have been included consistently in renormalization. They remain necessary for finiteness and scheme bookkeeping but cannot cancel `q^4 log q^2` by themselves.

This pruning does **not** apply automatically to the geodesic renormalization sector, whose counterterms/embedding renormalization belong to a nonlocal observable and can generate separated logarithms.

Predicate B: **PASS_SCOPED**.
`LOCAL_CT_GEODESIC_CT_SWAP_CONTROL`: **PASS_CONTROL**.

## 3. Scaleless tadpoles can be removed in the frozen regularization

The 2018 fixed-geodesic calculation uses dimensional regularization and states that massless tadpoles vanish. The same standard pruning is available for genuinely scaleless tadpole subgraphs in the flat-background massless calculation.

Predicate C: **PASS_SCOPED**.

## 4. F-sector has an explicit mandatory nonanalytic mechanism

The master-coordinate one-loop scalar-curvature calculation produces a nonzero separated `G^2/r^8` result. In momentum language this requires a nonanalytic massless-loop structure of `q^4 log(q^2/mu^2)` type after all field and coordinate-correction pieces are combined.

Within the anchored fixed-geodesic census, the ordinary curvature/field sector contains the same local curvature vertices and massless graviton/ghost propagating degrees of freedom. Standard one-loop bubble/self-energy and multi-curvature contractions therefore possess the required massless threshold integral structure.

A canonical scalar master integral is

`I(q) = ∫ d^d p / [p^2 (p+q)^2]`,

whose renormalized nonlocal part is proportional to `log(q^2/mu^2)`. Curvature derivatives supply the external momentum factors needed for the `q^4 log q^2` tensor-reduced structure.

Predicate D: **PASS**.

## 5. Mixed geodesic sector M cannot be pruned as contact-only

The first-order geodesic displacement `chi_1` is a line integral of the graviton field and its derivatives along the background geodesic. In momentum space a line integration produces form factors of the schematic type

`∫_0^1 dτ exp(i τ p.l)`
`= [exp(i p.l)-1]/(i p.l)`,

with appropriate tensor numerators.

These are manifestly non-polynomial in momentum. When correlated with massless propagators/curvature insertions, they generate separated-point functions and logarithmic structures rather than pure contact distributions.

This is not merely dimensional reasoning: the 2018 fixed-geodesic calculation explicitly finds mixed geodesic/field contributions surviving at separated points and participating in gauge-parameter cancellation.

Predicate E for M: **PASS_NONLOCAL / CANNOT PRUNE**.
`LINE_INTEGRAL_CONTACT_ASSUMPTION_CONTROL`: **TRIGGERS**.

## 6. Pure second-order geodesic sector G also remains in the nonlocal basis

The `chi_2` and `chi_1 chi_1` terms contain one or two integrations along the geodesic. Their momentum-space kernels contain one-dimensional parameter integrals and products of the same non-polynomial line form factors.

The 2018 source explicitly computes pure second-order geodesic contributions and finds that they survive away from coincidence. They are required, together with mixed terms, for renormalization/gauge cancellation.

Therefore G cannot be discarded from the nonanalytic tail a priori.

Predicate E for G: **PASS_NONLOCAL / CANNOT PRUNE**.

## 7. Gauge/BRST invariance does not protect a nonzero coefficient classwise

Both relevant source calculations show the same structural lesson:

- ordinary field pieces can be gauge dependent;
- localization corrections are necessary to restore gauge invariance of the complete relational observable.

Gauge/BRST identities therefore constrain the **sum** of F/M/G tensor structures and gauge-parameter dependence. They do not imply that the gauge-independent nonlocal scalar coefficient is nonzero. A gauge-invariant observable may have a vanishing coefficient through cancellation without violating the identity.

No frozen Ward identity, positivity theorem or anomaly fixes the fixed-geodesic `RR` `q^4 log q^2` coefficient.

Predicate F: **NOT ESTABLISHED / CANCELLATION OPEN**.
`GAUGE_INVARIANCE_NONZERO_COEFFICIENT_CONTROL`: **PASS_CONTROL**.

## 8. Reduced mandatory nonlocal basis

Contact/scaleless pruning substantially reduces bookkeeping, but it does **not** reduce the problem to the master-coordinate F sector alone.

The minimal separated-tail calculation must retain three coefficient groups:

`C_nonlocal(q,l) = C_F(q,l) + C_M(q,l) + C_G(q,l)`

where:

- `C_F` contains the nonanalytic parts of ordinary curvature/field one-loop and composite insertions;
- `C_M` contains all first-order line-localization contributions whose line form factors survive at separated points;
- `C_G` contains all second-order line-localization contributions and finite geodesic-renormalization pieces relevant away from coincidence.

Within each group, tensor algebra and parameter integration can be reduced to a finite family of:

1. massless bubble-type loop integrals;
2. one-geodesic-parameter integrals multiplying those loops;
3. two-geodesic-parameter integrals / products generated by `chi_1 chi_1` and `chi_2`;
4. local polynomial terms retained only long enough to cancel UV poles and then separated from the noncontact coefficient.

No fourth source-required nonlocal class appears at `O(G^2)` in the frozen setup.

Predicate G: **PASS_REDUCED_BASIS**.

## 9. Target independence

No modern EDT exponent is used to assign signs, neglect M/G, choose renormalization constants or infer a zero/nonzero sum.

Predicate H: **PASS_CONTROL**.
`EDT_TARGET_PRUNING_CONTROL`: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_CONTACT_PRUNING_VALID_NONLOCAL_FMG_BASIS_REMAINS_CANCELLATION_OPEN`**

ITER113 reduces the missing coefficient calculation to a finite nonlocal basis and proves that neither mixed nor pure geodesic sectors may be discarded before evaluation. Gauge invariance constrains their sum but does not protect noncancellation.

## Highest-information successor

The cheapest remaining analytic reduction is **tensor/form-factor projection**: project the complete F/M/G integrands onto the unique rotational scalar nonanalytic structure contributing to the curvature-curvature correlator, discarding gauge-longitudinal pieces that cancel by the complete observable. Determine whether the coefficient can be expressed in terms of a small set of scalar master integrals and geodesic parameter moments before evaluating them.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No `O(G^2)` coefficient or cancellation/noncancellation theorem, no direct EDT/EFT conflict, no continuum EDT, no `BRIDGE_DERIVED`, or new physics follows.