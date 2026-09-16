# ISQGR recovery frontier addendum — ITER140 M_R1 blind D=7 prediction

Date: 2026-09-16
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

## Auto-research state inspected first

At the start of this iteration both active workflow runs were still queued rather than executing:

- ITER140 v6 run `35040499084` remained `queued` with a mixture of already completed exact shards and remaining queued shards.
- ITER148 v3 run `35044099632` remained `queued`; no v3 chunk artifact had yet been created.

This external Actions queue was treated as infrastructure state, not scientific evidence.

## Independently formulated iteration question

Use immutable exact ITER140 v6 shard artifacts already produced before the queue stall to ask whether the `M_R1_chi1_dR2` family obeys a dimension dependence stronger than the frozen degree-4 authority. Fit only D=3,4,5,6, reserve D=8,9,10 as untouched validation, and if exact validation succeeds preregister a blind D=7 prediction before the queued D=7 M_R1 shard exists.

The frozen ITER140 aggregator defines the trace polynomial as

`trace_j(D) = (D-2)^2 * c_j(D)`

and interpolates it as an exact polynomial in `D`. The first attempted auxiliary model used the wrong variable and was rejected: fitting the raw coefficients as cubics in `(D-2)^2` produced 33 failures among the 84 D=8,9,10 coefficient checks. No result from that failed auxiliary model is used below.

## Exact stronger result in the frozen variable

Using only the exact D=3,4,5,6 `M_R1_chi1_dR2` artifacts and the same trace transform as frozen ITER140:

- all 28 independently fitted trace polynomials have degree <= 2;
- frozen authority allows degree <= 4;
- D=8,9,10 are not used in the fit;
- all 28 coefficients match exactly at all three validation dimensions;
- validation count = 84 exact coefficient equalities;
- validation failures = 0.

Thus this family shows a substantially lower realized dimension degree than the preregistered maximum, without changing the frozen gate.

## Blind D=7 prediction fixed before its M_R1 shard

The full predicted D=7 coefficient vector is committed in:

`analysis/iter140_mr1_d7_blind_prediction.json`

and is therefore immutable before the queued D=7 M_R1 artifact appears.

The three frozen held-out direct values predicted from that coefficient vector are:

- panel 0: `-17563/10`
- panel 1: `9338/5`
- panel 2: `12823/10`

The D=7 held-out q/k and `basis_values_full(q,k)` used to evaluate those invariant predictions were taken from the already immutable D=7 `M_R2_chi1_dR1` shard artifact. This is legitimate because `iter140_family_dimension_shard_v6.py` constructs held-out q/k and basis values before applying the family-specific direct numerator; the basis values are family-independent. No M_R1 D=7 direct value was available or used.

A standalone verifier is committed at:

`analysis/check_iter140_mr1_d7_blind_prediction.py`

When the queued D=7 M_R1 shard becomes available, run the checker on its JSON. Its auxiliary PASS requires exact equality of all 28 coefficients and all three direct held-out values, plus the normal shard rank/integrity predicates.

## Scientific status

This auxiliary result does **not** terminalize ITER140. The frozen aggregator remains authoritative and still requires all three families at D=3..10, frozen D=3..7 training, D=8..10 validation, held-outs, D4 authority, and unchanged scientific predicates.

A future match at D=7 would provide a genuinely blind confirmation of the M_R1 dimension continuation and of the observed lower realized degree. A mismatch would falsify this auxiliary stronger model but would not by itself falsify the original frozen degree<=4 ITER140 gate.

No pole integration, B1, EDT, bridge, new-physics, or candidate-theory claim is authorized by this addendum.
