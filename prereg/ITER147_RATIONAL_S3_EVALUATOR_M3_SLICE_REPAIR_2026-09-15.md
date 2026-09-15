# ITER147 preregistration — rational-momentum S3 evaluator authority and M3 slice repair

Date: 2026-09-15
Gate: `ITER147_FIXED_GEODESIC_CURVATURE_RATIONAL_S3_EVALUATOR_M3_SLICE_REPAIR`

## Frozen motivation

ITER146 failed only because its held-out affine interpolation did not close. Post-run inspection localized a minimal implementation-domain mismatch: the ITER144 helper `source_value` coerces momentum components through `sympy.Integer`, whereas the exact ITER145 routing at fractional `tau` produces rational momenta. ITER144 itself remains authoritative on its frozen integer-momentum panels.

This gate repairs only the evaluator domain. It does not change the pinned S3 source, parser, tensor object, routing, de Donder projectors, affine panels, degree ceiling, or physics acceptance criteria.

## Frozen object

Define an exact source evaluator from the already parsed ITER144 terms with momentum components preserved by `sympy.sympify` rather than converted to `sympy.Integer`. Coefficients, metric contractions, index-momentum factors and momentum dot products are otherwise identical to ITER144.

Use this evaluator in the already frozen ITER146 contraction

`R1 x chi1.dR1 x S3`

with exact ITER145 routing

`p=-Q-(1-tau)k`, `r=Q-tau k`.

## Frozen predicates

A. Re-fetch the exact ITER144 pinned source and require the same Git blob SHA and fixed parser grammar.
B. The rational evaluator must agree exactly with the original ITER144 integer evaluator on deterministic integer momentum component panels, including the existing leg-permutation domain.
C. On deterministic rational momentum panels, every parsed S3 source component must remain homogeneous of total momentum degree two under a symbolic common rescaling `p_i -> z p_i`.
D. Rerun the four ITER146 affine loop slices with the same Q, n, tau, k0, k1 panels. Interpolate lambda=0..8 and require exact reproduction at withheld lambda=9,10 without refitting.
E. The resulting exact affine polynomials must have realized degree <=8 on all four panels.
F. Preserve exact ITER145 momentum conservation, all S3 leg permutations and global `(Q,k)->(-Q,-k)` parity controls.
G. No denominator integration, loop pole, B1 target, EDT exponent, desired cancellation or fitted physics coefficient may enter.

## Frozen classifications

- `PASS_SCOPED_RATIONAL_S3_EVALUATOR_AND_M3_SLICE_REPAIR_CLOSED_FULL_INVARIANT_OPEN` iff A-G pass.
- `SCIENTIFIC_FAIL_M3_NUMERATOR_DEGREE_OR_TENSOR_ALLOCATION` if the exact rational evaluator still fails the frozen degree/held-out/tensor predicates.
- `BLOCKED_PINNED_S3_SOURCE_OR_PARSER_CHANGED` if source integrity no longer matches ITER144.

## Claim ceiling

A PASS repairs the exact rational S3 evaluation domain and closes the D=4 M3 numerator slice authority. It does not yet establish a full invariant numerator, bubble-reduced invariant representation, master integral, pole residue, B1, noncancellation, EDT match, bridge, new physics or candidate theory.
