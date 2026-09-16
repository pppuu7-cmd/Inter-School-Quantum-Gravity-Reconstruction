# ISQGR recovery frontier addendum — quadratic trace conjecture for all remaining ITER140 v6 shards

Date: 2026-09-16
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

## Auto-research state first

At the start of this iteration both active Actions workflows were still queued rather than executing. ITER140 v6 run `35040499084` already had 14 immutable successful shard artifacts, while 10 shards remained absent. ITER148 v3 run `35044099632` also remained queued. This queue state was treated only as infrastructure state.

The 10 absent ITER140 v6 shards at the last artifact audit were exactly:

- `M_R1_chi1_dR2`: D=7
- `M_R2_chi1_dR1`: D=3,4,6,10
- `G_R1_chi2_Gamma2_dR1`: D=3,6,8,9,10

No result from those missing shards is used below.

## Frozen dimension variable

The authoritative ITER140 aggregate does not interpolate raw coefficients in `(D-2)^2`. It defines

`trace_j(D) = (D-2)^2 * c_j(D)`

and interpolates `trace_j` as an exact polynomial in D, with preregistered degree bound <=4.

An auxiliary attempt to fit raw coefficients as cubics in `(D-2)^2` was explicitly rejected after 33 failures among 84 M_R1 validation coefficient checks. That failed model is not used.

## Stronger auxiliary conjecture

Available exact data suggest the stronger prospective conjecture:

> For all three frozen first-M/G families and all 28 invariant coefficients, `trace_j(d)` has polynomial degree <=2.

This is a stronger auxiliary hypothesis, not a modification of the frozen degree<=4 gate.

### M_R1_chi1_dR2

Fit only D=3,4,5,6.

- observed maximum trace degree: 2
- untouched coefficient validation: D=8,9,10
- validation equalities: 28 x 3 = 84
- failures: 0

The already separately preregistered D=7 prediction is therefore retained as a genuine blind target.

### M_R2_chi1_dR1

Fit only D=5,7,8.

- observed maximum trace degree: 2
- untouched coefficient validation: D=9
- validation equalities: 28
- failures: 0

As an additional independent check, the model predicts the D=4 direct held-outs

- `15741/4`
- `3306`
- `-1341/2`

which exactly equal the immutable ITER138/139 D4 terminal-authority values already pinned for ITER140. The D=4 coefficient vector itself remains unobserved in v6 and is still a prospective prediction.

Prospective M_R2 targets are D=3,4,6,10.

### G_R1_chi2_Gamma2_dR1

A stronger linear trace model was tested first using only D=4,5 and then checked at D=7.

- 26 of 28 coefficients agree with the linear prediction;
- exactly coefficient indices 11 and 22 fail;
- therefore the available G data require trace degree at least 2.

The minimum-degree exact model through D=4,5,7 has maximum trace degree 2. It has no independent coefficient validation yet, so its remaining-D predictions are explicitly prospective and weaker than the already validated M_R1/M_R2 evidence.

Prospective G targets are D=3,6,8,9,10.

## Frozen predictions before the missing shards

The compact exact formulas and direct held-out predictions for all 10 missing shards are committed in:

`analysis/iter140_quadratic_trace_conjecture_all_remaining.json`

The generic future checker is:

`analysis/check_iter140_quadratic_trace_prediction.py`

For a completed target shard, auxiliary PASS requires:

1. exact target D/family identity;
2. basis size 28, design rank 28, unchanged scientific predicates, and shard held-outs OK;
3. exact equality of all 28 coefficients to the preregistered quadratic-trace prediction;
4. exact equality of all three direct held-outs;
5. all three observed invariant reconstructions equal their direct values.

The prediction record was created only after verifying that none of the 10 target artifacts existed in run `35040499084`.

## Scientific status and continuation rule

This prospective program does not terminalize ITER140. The original frozen v6 aggregate remains authoritative and still requires all 24 shards, D=3..7 frozen training, D=8..10 validation, D4 authority, rank, held-outs and unchanged-predicate checks.

If future target shards match the quadratic conjecture, record those matches as auxiliary blind confirmations and then let the frozen aggregate adjudicate ITER140 normally. If one or more target shards reject the quadratic conjecture but still satisfy the frozen degree<=4 gate, the auxiliary conjecture fails while ITER140 can still pass. No post-hoc degree/basis changes are authorized.

No loop-pole, B1, EDT, bridge, new-physics or candidate-theory claim follows from this addendum.
