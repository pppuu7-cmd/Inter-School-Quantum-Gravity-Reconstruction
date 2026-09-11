# Iter003 Result — MC-001 Independence / Semantic-Level Audit

Status: `SOURCE_GROUNDED / NON_PROMOTION_RESULT`  
Date: 2026-09-12

## Question

Can asymptotic-safety functional RG provide the second independent realization needed to promote

`MC-001 — PHYSICAL/CONSTRAINT SECTOR NOT AUTOMATICALLY CLOSED UNDER SCALE FLOW`

to a recurrent motif `RM-001`?

## Sources

- F. Saueressig, *The Functional Renormalization Group in Quantum Gravity* (2023), arXiv:2302.14152.
- J. Dietz, *Functional truncations in asymptotic safety for quantum gravity* (2016), arXiv:1605.09354.
- N. Ohta, *Background Scale Independence in Quantum Gravity* (2017), arXiv:1701.01506.

## What is source-grounded

The effective-average-action/FRG programme defines a flow on a theory space of gravitational functionals. Explicit calculations require controlled approximations/truncations; the Einstein–Hilbert truncation is a basic finite approximation, while functional truncations enlarge the retained operator content.

The literature also shows that approximation choices such as the single-field approximation can generate qualitatively misleading behavior and that split/background Ward identities contain independent consistency information relevant to restoring background/split symmetry.

Therefore the statement

> a chosen finite ansatz is not automatically an invariant/complete representation of the exact RG flow

is well motivated at the methodology level.

## Why this does NOT yet promote MC-001

RC-006 concerns source-defined *simplicity/constraint data* in a reduced EPRL/FK-like spin-foam model changing under tensor-network coarse graining.

FRG truncation error concerns *operator/function-space closure* of an approximate effective action and consistency with Ward identities.

These are related structurally but not yet the same semantic object:

- one is a constraint-defined microscopic sector;
- the other is a truncation subspace in theory space.

Calling them the same recurrent QG failure now would be an analogy-driven promotion, forbidden by the ISQGR constitution.

## Useful broader candidate motif

A broader, weaker candidate can be recorded:

`MC-002 — SCALE EVOLUTION GENERICALLY REQUIRES CLOSURE DATA BEYOND A CHOSEN REDUCED DESCRIPTION`.

This wording can encompass both RC-006 and FRG truncation phenomena, but by itself it risks becoming a generic renormalization statement rather than new QG physics.

For MC-002 to become scientifically useful, ISQGR must identify a **shared physically constrained closure datum**, such as a common boundary/memory/constraint-restoration object, not merely the fact that truncations are imperfect.

## Relation to BH-001A

The exact abstract identity

`Delta_seq = D o Phi2 o (I-E o D) o Phi1 o E`

suggests one way of asking the question: what data live in the discarded sector `(I-EoD)` and can later feed back into retained observables?

But no source-defined map from gravitational FRG theory-space truncation to this finite-channel identity is asserted here. That mapping remains a target.

## Promotion verdict

- `MC-001 -> RM-001`: **NOT AUTHORIZED**.
- `MC-002`: **TENSION_CANDIDATE / TOO_GENERIC_FOR_PROMOTION**.

## Next decisive test

Construct realization-native closure maps on both sides:

1. for one spin-foam coarse-graining step, identify retained tensor/constraint coordinates and generated discarded coordinates;
2. for one FRG truncation, identify a projection from enlarged theory space to the reduced ansatz and the leading generated orthogonal operators / Ward-identity defect;
3. compare whether both defects obey a nontrivial common closure law after normalization by their native physical scales.

Only then revisit recurrence.

## Claim lock

The existence of truncation artifacts in FRG is not evidence against asymptotic safety. This audit is specifically designed to prevent a false positive in inter-school synthesis.