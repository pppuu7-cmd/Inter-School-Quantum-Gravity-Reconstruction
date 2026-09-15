# ISQGR recovery frontier addendum — ITER147 terminal PASS, ITER148 + ITER140-v3 active

Date: 2026-09-15
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

Prefer this additive note over older recovery pointers for the active fixed-geodesic curvature branch. Candidate theory remains **UNFORMED / 0%**; bridge credit remains **0**.

## ITER146 — terminal scoped FAIL, cause localized

Result commit: `096f2eccc4cdab6e773116a481f9ec421508fc79`.
The failed degree-8 held-outs were caused by reuse of the ITER144 integer-only momentum coercion helper on rational ITER145 routed momenta. This did not invalidate ITER144 but required a rational evaluator repair.

## ITER147 — terminal PASS

Result commit: `f5246a44d5fccaec7f9c65333dcfa2ccaab21190`.
Run `35016375562`, job `104540719390`, artifact `10415677784`, SHA256 `e5c5b016340c8bdcb7d06dd99bb6a364296fc18451760dcb38c95dbe5c251000`.

Classification:

`PASS_SCOPED_RATIONAL_S3_EVALUATOR_AND_M3_SLICE_REPAIR_CLOSED_FULL_INVARIANT_OPEN`.

All frozen predicates passed. Exact rational S3 evaluation agrees with ITER144 on its integer domain, preserves symbolic momentum-degree-two homogeneity, and restores every frozen ITER146 M3 affine slice to exact realized degree 8 with lambda=9,10 held-outs passing without refit. Routing, all S3 leg permutations, momentum-flip parity and target blindness pass.

## ITER148 — active full M3 invariant/bubble lane

Preregistration commit: `f2d59b35ef3e943ee94484e479a4951a736356b1`.
Implementation commit: `b7603dd0d6fbc78d266e12da52528c8169a097a6`.
Workflow head: `a5f48c584e53d6af9f4ac2cdbe4c9d670eeff1c7`.
Active run: `35017383409`, job `104544128820`.

Frozen target:

- reconstruct the complete D=4 `M_R1_chi1_dR1_S3` numerator in the 45-element degree-8 / at-most-n^2 invariant basis;
- reconstruct all coefficient polynomials in tau with frozen degree <=8 and no-refit tau/q/k held-outs;
- revalidate the authorized fast `-2 * EH_GammaGamma` contraction against repaired direct rational pinned-source evaluation before production use;
- combine the full invariant numerator with the exact ITER145 partial-fraction identity;
- verify the three canonical bubble loop maps and Jacobian/prefactor powers:
  `tau^(3-d)/Q`, `(1-tau)^(3-d)/Q`, and `-[tau(1-tau)]^(3-d)/Q`.

A PASS would close the full D=4 M3 invariant numerator and canonical bubble representation, while leaving general-d/O(epsilon) continuation and all poles open.

## ITER140 — still active general-d Gaussian lane

Attempt 3 was adjudicated `NUMERICAL_OR_INFRASTRUCTURE_FAIL` after direct D=3..10 contractions completed but postprocessing hit the 180-minute timeout. Result note commit: `9f5dffff36c667354dc6bd9d70ce7d9204ad89c7`.

V3 implementation commit: `03d2578c38b119e6a4b77d65a0206c101c5e99a1`.
Workflow head: `3b73e61073412cc85540fedbe35ae618a3e7dab4`.
Active run: `35016456669`, job `104541005387`.

V3 keeps all frozen ITER140 scientific predicates and replaces only expensive symbolic continuation/postprocessing with exact Newton finite-difference/rational arithmetic.

## Exact next actions

1. Adjudicate ITER148. If PASS, next M3 gate is general-d/O(epsilon) continuation of the full invariant/canonical-bubble representation before any master pole.
2. Independently adjudicate ITER140-v3. If PASS, terminalize and authorize the three Gaussian M/G general-d numerator families for later pole integration.
3. Do not compute or claim physical B1 until general-d numerators, master poles, bulk/composite/endpoint/line-counterterm subtraction and ITER124 projected genuine-defect pole assembly are all closed.
