# ITER146 preregistration — exact interaction-dressed M3 numerator slices

Date: 2026-09-15
Gate: `ITER146_FIXED_GEODESIC_CURVATURE_M3_EXACT_NUMERATOR_SLICE_AUTHORITY`

## Frozen motivation
ITER144 authorizes the cubic graviton S3 tensor structure up to one global convention factor. ITER145 closes the exact collinear three-denominator routing and reduction to bubbles, but leaves the S3 tensor numerator open. Before attempting a full general-d invariant reduction, construct the complete D=4 tensor contraction for the interaction-dressed family `M_R1_chi1_dR1_S3` on exact one-parameter loop-momentum slices.

## Frozen object
For routing `p=-Q-(1-tau)k`, `r=Q-tau k`, contract:

1. the linear scalar-curvature vertex `A_ab(p)=p^2 delta_ab-p_a p_b`;
2. the source-qualified bulk geodesic response `chi1^mu(k) = -(1-tau) Gamma1^mu_nn(k)` at the tensor level, retaining the explicit `(1-tau)` factor outside the numerator core;
3. `partial_mu R1(r)=i r_mu A_cd(r)`;
4. three de Donder propagator numerators in D=4;
5. the pinned ITER144 S3 source tensor with its common global `I*kappa` stripped exactly as in ITER144.

The contraction is evaluated on deterministic rational D=4 data with unit tangent `n`, nonzero Euclidean `Q^2`, rational `tau`, and affine loop slices `k(lambda)=k0+lambda k1`.

## Frozen predicates
A. Use exactly the ITER145 routing and verify momentum conservation at S3.
B. Re-fetch the pinned ITER144 machine source and require the same Git blob SHA.
C. Construct R1, chi1, dR1 and all three de Donder projector contractions explicitly; no derivative-count proxy may replace them.
D. On at least four deterministic held-out slices, reconstruct the exact numerator as a polynomial in `lambda` by rational interpolation and verify against additional withheld integer lambda values.
E. Record the realized polynomial degree and require it not exceed the ITER129 interaction-dressed M ceiling `D_total<=8`.
F. Verify the numerator is invariant under the S3 leg permutation controls when the complete leg data are permuted together.
G. Verify global `Q -> -Q` relabeling with corresponding routed momenta gives the expected parity-consistent polynomial relation on frozen panels.
H. No denominator integration, pole coefficient, B1 target, EDT exponent, desired cancellation, or fitted physics coefficient may enter.

## Frozen classifications
- `PASS_SCOPED_M3_EXACT_NUMERATOR_SLICES_CLOSED_FULL_INVARIANT_POLYNOMIAL_OPEN` iff A-H pass.
- `FAIL_SCOPED_M3_TENSOR_ALLOCATION_OR_ROUTING_MISMATCH` if an exact frozen identity fails.
- `BLOCKED_PINNED_S3_SOURCE_UNAVAILABLE_OR_CHANGED` if the pinned source cannot be verified.

## Claim ceiling
A PASS establishes exact tensor allocation and loop-degree evidence for M3 on held-out D=4 slices. It is not yet the full general-d invariant numerator, a master integral, a pole residue, B1, noncancellation, EDT match, bridge, new physics, or candidate theory.
