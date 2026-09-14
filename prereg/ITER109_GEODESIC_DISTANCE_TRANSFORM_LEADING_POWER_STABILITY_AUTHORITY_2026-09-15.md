# ITER109 preregistration — geodesic-distance transform leading-power stability authority

Date: 2026-09-15
Gate: `ITER109_GEODESIC_DISTANCE_TRANSFORM_LEADING_POWER_STABILITY_AUTHORITY`

## Motivation frozen before final adjudication

ITER108 establishes a modern EDT curvature-correlator power consistent with approximately `r^-10` in a fluctuating geodesic-shell observable, while the 2026 low-energy EFT master-coordinate curvature correlator has a universal noncontact `G^2/r^8` term. ITER106–107 forbid direct exponent comparison because changing the separation observable is itself a quantum operation with additional renormalization.

ITER109 asks a narrower analytic question: **can the observable change alter the leading inverse-power exponent at the same perturbative order, or only coefficients/logarithms?**

No EDT target exponent may be used to choose counterterms or assume a cancellation.

## Frozen source/authority stack

1. arXiv:2510.11888 / Phys. Rev. D 113, 106032 (2026): master-coordinate relational curvature correlator, first noncontact term `~G^2/r^8`.
2. arXiv:1706.01891 / Class. Quantum Grav. 35, 035005 (2018): one-loop fixed-geodesic-distance matter-scalar correlator, including geodesic embedding renormalization and double logarithms.
3. ITER107 only for separation-observable typing.
4. Standard four-dimensional EFT mass-dimension/power counting may be used explicitly.

## Frozen question

At a fixed nonzero separation in four-dimensional massless low-energy quantum gravity, if the fixed-geodesic scalar-curvature correlator has a nonzero noncontact contribution at order `G^2`, is its inverse-power part forced to scale as `G^2/l^8` up to logarithms and dimensionless constants? Can a source-derived argument establish that this `O(G^2)` term is necessarily nonzero after switching from master-coordinate to fixed-geodesic separation?

## Required predicates

A. Scalar curvature has engineering mass dimension `2`; its two-point function has dimension `4`.

B. At order `G^2` in 4D, and away from contact with no additional physical mass scale, dimensional analysis must give `G^2/l^8` times dimensionless functions/logarithms.

C. The fixed-geodesic scalar-field precedent must be used only structurally: it may show new logarithms/counterterms but cannot substitute for the curvature calculation.

D. Renormalization scale `mu` may generate `log(mu l)` and finite-counterterm dependence but cannot supply a new power of `l` at fixed perturbative order without an additional dimensionful coupling/operator.

E. A full `LEADING_POWER_STABLE` result requires source/analytic authority that the `O(G^2)` fixed-geodesic curvature coefficient cannot cancel identically.

F. If such noncancellation is not established, the result must remain conditional: cancellation could postpone the first noncontact term to `O(G^3)`, where `G^3/l^10` is dimensionally allowed.

G. Higher-derivative EFT coefficients/contact terms must not be promoted into noncontact long-distance powers unless the source calculation shows this.

H. No EDT exponent may be used to infer the cancellation or select a scheme.

## Frozen classifications

- `PASS_SCOPED_FIXED_GEODESIC_LEADING_POWER_STABLE_AT_G2` if A-E all pass.
- `PASS_SCOPED_CONDITIONAL_G2_POWER_IS_MINUS8_NONCANCELLATION_OPEN` if A-D/F-H pass but E is not established.
- `FAIL_SCOPED_POWER_COUNTING_ALLOWS_DIFFERENT_G2_POWER` if the geodesic observable introduces source-qualified dimensionful structures that permit a different inverse power at the same `G^2` order.
- `BLOCKED_SOURCE_AUTHORITY` if perturbative-order typing is insufficient.

## Controls

- `CURVATURE_MATTER_SCALAR_SWAP_CONTROL`
- `RENORMALIZATION_SCALE_POWER_SWAP_CONTROL`
- `CONTACT_NONCONTACT_SWAP_CONTROL`
- `G2_CANCELLATION_ASSUMPTION_CONTROL`
- `EDT_TARGET_CANCELLATION_FIT_CONTROL`

## Claim ceiling

Even a full PASS would constrain only the long-distance perturbative fixed-geodesic exponent at leading order. It would not establish that EDT is in that regime, determine the amplitude, prove a direct conflict, establish a continuum limit, `BRIDGE_DERIVED`, new physics or a candidate theory.