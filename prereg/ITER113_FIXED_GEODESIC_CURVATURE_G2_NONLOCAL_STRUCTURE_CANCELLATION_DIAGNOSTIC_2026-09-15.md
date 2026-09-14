# ITER113 preregistration — fixed-geodesic curvature `O(G^2)` nonlocal-structure / cancellation diagnostic

Date: 2026-09-15
Gate: `ITER113_FIXED_GEODESIC_CURVATURE_G2_NONLOCAL_STRUCTURE_CANCELLATION_DIAGNOSTIC`

## Motivation frozen before pruning

ITER112 established a finite `O(G^2)` census for the anchored fixed-geodesic scalar-curvature correlator: ordinary field/curvature sector F, mixed first-order geodesic sector M, and pure second-order geodesic sector G. A brute-force evaluation is therefore possible, but may be unnecessarily large.

ITER113 asks which terms can contribute to the separated long-distance tail and whether source-independent identities protect a nonzero combination before complete tensor integration.

## Frozen source / analytic authority

1. arXiv:2510.11888 — one-loop relational curvature correlator and its contact/noncontact separation.
2. arXiv:1706.01891 — fixed-geodesic mixed/pure corrections, gauge cancellation and geodesic renormalization.
3. Standard dimensional-regularization Fourier/distribution identity: in 4D a separated `1/l^8` tail corresponds to a nonlocal momentum-space structure of `q^4 log(q^2/mu^2)` up to local polynomials/contact terms.
4. ITER109–ITER112 only as prior order/census authority.

## Frozen question

Can the F/M/G census be pruned to a smaller **mandatory nonlocal basis** at `O(G^2)`? In particular:

- which structures are guaranteed contact/scaleless and may be removed from the separated coefficient;
- which F/M/G classes can generate `q^4 log q^2` or equivalent fixed-length nonlocal structures;
- whether Ward/BRST/gauge identities force the sum of those nonlocal coefficients to be nonzero.

## Required predicates

A. Separate polynomial/analytic momentum dependence (contact after Fourier transform) from logarithmic/nonanalytic dependence.

B. Local counterterms may be pruned from the separated tail only after showing they remain polynomial/contact for the defined observable.

C. Scaleless tadpoles that vanish in dimensional regularization may be pruned.

D. At least one explicit F-sector mechanism for `q^4 log q^2` must be identified.

E. Test whether M and G line-integral/localization sectors can also produce separated nonanalytic terms; they may not be pruned solely because they arise from endpoint motion.

F. A full `NONCANCELLATION_PROTECTED` PASS requires a source/identity fixing a nonzero gauge-invariant coefficient after summing F/M/G.

G. If no such identity exists, derive the smallest remaining integral/coefficient basis whose explicit evaluation is necessary.

H. No EDT exponent may be used to declare a class negligible or to infer coefficient cancellation.

## Frozen classifications

- `PASS_SCOPED_G2_NONCANCELLATION_PROTECTED_REDUCED_BASIS` if A-H pass and F is established.
- `PASS_SCOPED_CONTACT_PRUNING_VALID_NONLOCAL_FMG_BASIS_REMAINS_CANCELLATION_OPEN` if contact/scaleless pruning succeeds but M/G remain nonlocal and no protected coefficient exists.
- `BLOCKED_SOURCE_AUTHORITY` if contact/noncontact classification cannot be made.
- `FAIL_SCOPED_PRUNING_INVALID` if apparently local sectors generate uncontrolled nonlocal tails at the same order.

## Controls

- `POLYNOMIAL_NONANALYTIC_SWAP_CONTROL`
- `LOCAL_CT_GEODESIC_CT_SWAP_CONTROL`
- `LINE_INTEGRAL_CONTACT_ASSUMPTION_CONTROL`
- `GAUGE_INVARIANCE_NONZERO_COEFFICIENT_CONTROL`
- `EDT_TARGET_PRUNING_CONTROL`

## Claim ceiling

A PASS may reduce the calculation but cannot substitute for an uncomputed coefficient unless noncancellation is genuinely protected. No direct EDT/EFT conflict, continuum EDT, `BRIDGE_DERIVED`, new physics or candidate theory follows.