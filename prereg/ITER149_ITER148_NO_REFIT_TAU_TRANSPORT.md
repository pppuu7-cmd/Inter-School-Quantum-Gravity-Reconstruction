# ITER149 — ITER148 no-refit tau transport gate

Date frozen: 2026-09-16

## Purpose
Independent held-out transport test of the terminal ITER148 v3 invariant numerator. This gate does **not** fit or modify any coefficient, basis element, source convention, routing, degree bound, bubble map, or threshold.

## Frozen authority
Input artifact is exactly ITER148 v3 authoritative run `35044099632`, aggregate job `104677935357`, artifact `10431996892`, SHA256 `5617edf6b6d30db3599e67a86f97b8f7c31308550e94a5bff3f859b395a2ab94`, classification `PASS_SCOPED_M3_FULL_D4_INVARIANT_AND_CANONICAL_BUBBLE_REDUCTION_CLOSED_GENERAL_D_POLES_OPEN`.

## Frozen held-out tau values
`3/10`, `5/12`, `7/13`. None belongs to the ITER148 training grid j/8 or the prior held-outs 1/3 and 2/5.

## Frozen held-out kinematic panels
1. q=(3,-2,1,2), k=(1,3,-2,1), n=(1,0,0,0)
2. q=(-1,2,4,-2), k=(2,-3,1,3), n=(0,1,0,0)
3. q=(2,3,-1,4), k=(-2,1,3,-1), n=(0,0,1,0)
4. q=(4,-1,2,1), k=(1,2,-3,2), n=(0,0,0,1)

## Frozen predicates
A. Artifact identity matches the exact authoritative run/artifact digest above.
B. Artifact scientific predicates are unchanged and basis size is 45.
C. For all 12 tau×panel combinations, substitute the frozen coefficient polynomials into the frozen invariant basis and compare exactly with `numerator_fast`; every difference must be exactly zero.
D. No refit/reconstruction is permitted in ITER149; coefficient polynomials are read-only inputs.
E. Target blindness: no denominator integration, pole extraction, endpoint subtraction, or bridge quantity is used.

## Classification
All A-E true: `PASS_SCOPED_ITER148_NO_REFIT_TAU_TRANSPORT_HELDOUTS`.
Any exact mismatch with valid artifact/input: `SCIENTIFIC_FAIL_ITER148_NO_REFIT_TAU_TRANSPORT`.
Artifact/download/hash/runtime problem: `NUMERICAL_OR_INFRASTRUCTURE_FAIL`, never scientific FAIL.

## Claim ceiling
A PASS strengthens only non-retuned tau transport of the frozen D4 numerator representation. It does not close general-D poles, endpoint subtraction, amplitude/refinement bridge, new physics, or candidate theory.
