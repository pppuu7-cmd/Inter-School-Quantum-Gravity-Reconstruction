# ITER147 terminal result — rational-momentum S3 evaluator authority and M3 slice repair

Date: 2026-09-15
Gate: `ITER147_FIXED_GEODESIC_CURVATURE_RATIONAL_S3_EVALUATOR_M3_SLICE_REPAIR`
Preregistration: `776db2007685a353bf3ed43dfb2d53bae88a543c`
Implementation: `ea45e799d39ad12c9645c732c79c6798a8b7f2ab`
Workflow head: `8645fcf8e85380470f812d2b23e136a9a55196a8`
Authoritative run: `35016375562`
Job: `104540719390`
Artifact: `10415677784` (`iter147-rational-s3-m3-slice-repair`)
Artifact SHA256: `e5c5b016340c8bdcb7d06dd99bb6a364296fc18451760dcb38c95dbe5c251000`

## Scientific classification

`PASS_SCOPED_RATIONAL_S3_EVALUATOR_AND_M3_SLICE_REPAIR_CLOSED_FULL_INVARIANT_OPEN`

All preregistered predicates A-G pass.

## What was repaired

The only implementation change relative to the failed ITER146 calculation is preservation of exact rational/symbolic momentum components in the already pinned ITER144 S3 term evaluator. The source blob, fixed parser, tensor object, ITER145 routing, D=4 de Donder projectors, affine panels, degree ceiling and held-out values remained frozen.

The repaired evaluator agrees exactly with the original ITER144 evaluator on deterministic integer-momentum panels and all tested leg permutations, so ITER144 authority is preserved rather than replaced.

## Exact rational source authority

The pinned source blob remains

`98297aac3b640a93ac80c2cc72a8275280819954`.

On a deterministic rational three-leg panel, the exact parsed S3 component is homogeneous under common momentum scaling with total degree two, exactly as required by the 231-term ITER144 source structure.

## Repaired interaction-dressed M3 slices

The original four frozen ITER146 affine loop slices were rerun without changing their Q, n, tau, k0 or k1 data.

For every panel:

- the lambda=0..8 exact values reconstruct a polynomial of realized degree exactly 8;
- withheld lambda=9 and lambda=10 agree exactly without refitting;
- ITER145 momentum conservation holds;
- all S3 leg permutations agree;
- global `(Q,k)->(-Q,-k)` even-parity control agrees;
- no denominator integration or target coefficient enters.

Thus the expected ITER129 interaction-dressed M3 derivative ceiling is saturated but not exceeded on all four exact held-out slices.

## Consequence

The D=4 interaction-dressed family `M_R1_chi1_dR1_S3` now has authorized exact tensor allocation on rational routed momenta. The next admissible step is a preregistered **full invariant numerator / ITER145 bubble-reduced representation** suitable for subsequent dimensional continuation and pole extraction.

## Claim ceiling

This PASS is not yet a full invariant numerator, bubble pole, renormalized `1/epsilon`, B1 result, noncancellation result, B0, EDT comparison, bridge, new physics or candidate theory. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
