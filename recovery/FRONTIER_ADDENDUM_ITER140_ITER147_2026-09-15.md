# ISQGR recovery frontier addendum — ITER146 adjudicated, ITER147 + ITER140-v3 active

Date: 2026-09-15
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

This additive recovery note is newer than `recovery/FRONTIER_ADDENDUM_ITER140_ITER146_2026-09-15.md` and should be preferred over stale iteration pointers in `recovery/state.json` for the active fixed-geodesic curvature branch.

Candidate theory remains **UNFORMED / 0%**. Bridge credit remains **0**.

## ITER146 — terminal FAIL with localized implementation-domain cause

Terminal result commit: `096f2eccc4cdab6e773116a481f9ec421508fc79`.
Authoritative run: `34994417063`, job `104466939263`, artifact `10406914029`.
Artifact SHA256: `91b55142e1c01966c219953058b57a0b4fcc2cd9c84963344f15b51e5b9aa33e`.

Frozen classification:

`FAIL_SCOPED_M3_TENSOR_ALLOCATION_OR_ROUTING_MISMATCH`.

Only the affine interpolation/held-out predicate failed. Routing conservation, pinned S3 source, explicit R1/chi1/dR1 plus three de Donder maps, nominal degree-8 interpolants, S3 permutations, global momentum flip, and target blindness passed.

Post-run localization found that ITER146 reused ITER144 `source_value`, which coerces every momentum component with `sympy.Integer(x)`. ITER144 used integer momentum panels, so this did not invalidate ITER144. ITER145 routing at fractional tau produces rational p/r components, so the coercion destroys exact rational affine dependence and invalidates that helper for ITER146.

## ITER147 — active minimal repair gate

Gate: `ITER147_FIXED_GEODESIC_CURVATURE_RATIONAL_S3_EVALUATOR_M3_SLICE_REPAIR`.
Preregistration: `776db2007685a353bf3ed43dfb2d53bae88a543c`.
Implementation: `ea45e799d39ad12c9645c732c79c6798a8b7f2ab`.
Workflow head: `8645fcf8e85380470f812d2b23e136a9a55196a8`.
Active run: `35016375562`, job `104540719390`.

ITER147 changes only evaluator domain preservation (`sympify` rather than integer coercion). It freezes the same pinned source/parser, proves agreement with ITER144 on integer panels, verifies degree-two S3 homogeneity for rational/symbolic momenta, and reruns the exact ITER146 four affine slices and held-outs with the same routing/tensor predicates.

If ITER147 PASSes, the next admissible M3 step is a preregistered full invariant numerator / ITER145 bubble-reduced representation gate. If it fails scientifically, do not enlarge the degree ceiling or change panels post hoc; localize the remaining exact tensor mismatch.

## ITER140 attempt 3 — infrastructure adjudication

Attempt result commit: `9f5dffff36c667354dc6bd9d70ce7d9204ad89c7`.
Run `34991523078`, job `104457100505`.
Classification: `NUMERICAL_OR_INFRASTRUCTURE_FAIL`.

Direct exact contractions completed for every required D=3..10 and all three frozen Gaussian M/G families. The run then hit the 180-minute timeout in post-reconstruction symbolic work before any predicate classification was emitted. Therefore no scientific FAIL or PASS is inferred.

## ITER140 v3 — active implementation-only retry

Implementation commit: `03d2578c38b119e6a4b77d65a0206c101c5e99a1`.
Workflow head: `3b73e61073412cc85540fedbe35ae618a3e7dab4`.
Active run: `35016456669`, job `104541005387`.

Frozen scientific predicates are unchanged. V3 keeps the same direct indexed contractions and replaces expensive general-purpose symbolic postprocessing by exact Newton finite-difference arithmetic for the preregistered `(D-2)^2` degree<=4 trace bound plus exact rational held-out checks.

## Exact next actions

1. Adjudicate ITER147 from its authoritative output. If PASS, terminalize and immediately preregister the full M3 invariant/bubble-reduced numerator gate.
2. Independently adjudicate ITER140-v3. If PASS, terminalize general-d continuation and authorize it as input to later pole extraction. If it still fails only infrastructurally, profile the precise v3 stage without changing the scientific object.
3. Preserve strict claim locks: no pole coefficient, B1 noncancellation, EDT comparison, bridge, new physics or candidate theory until the complete projected renormalized pole system closes.
