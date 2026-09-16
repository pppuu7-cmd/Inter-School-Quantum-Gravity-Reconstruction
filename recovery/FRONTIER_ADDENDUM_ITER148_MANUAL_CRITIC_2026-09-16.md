# ISQGR recovery frontier addendum — ITER148 active, manual critic audit recorded

Date: 2026-09-16
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

This addendum is newer than `recovery/CURRENT_FRONT.md`, which is stale at ITER136. For the active fixed-geodesic branch, use this note together with `FRONTIER_ADDENDUM_ITER140V5_ITER148V2_2026-09-15.md` and the current GitHub Actions state.

Candidate theory remains **UNFORMED / 0%**. Bridge credit remains **0**. Overall roadmap percentage remains bookkeeping only.

## Latest terminal scientific result

ITER147 remains terminal:

`PASS_SCOPED_RATIONAL_S3_EVALUATOR_AND_M3_SLICE_REPAIR_CLOSED_FULL_INVARIANT_OPEN`.

Result commit: `f5246a44d5fccaec7f9c65333dcfa2ccaab21190`.

## ITER148 active authoritative implementation

Preregistration: `f2d59b35ef3e943ee94484e479a4951a736356b1`.
Parallel shard implementation: `4a2fc6eda9a41121e941f90561556de83306c599`.
Parallel aggregator: `a70d03bb28b4130ccc7679cd98e678808e000964`.
Workflow timeout-only repair: `108ec4fca9d9ebfa9f2321b69cab926b21d0bb4d`.
Active run: `35033354189`.

At the latest audit, all nine tau-shard jobs are still inside the frozen exact shard computation. No shard artifact is yet available. Therefore no scientific classification can be inferred from the active run.

Earlier single and parallel implementations were cancelled/time-limited before producing a terminal aggregate and remain infrastructure/numerical non-results, not scientific FAILs.

## Adversarial implementation audit

The parallel aggregator correctly computes the A/B/C denominator substitutions, but the frozen check `L_canonical_jacobian_prefactor_powers` is represented as a literal `True` rather than a machine-derived predicate. Green CI alone therefore cannot be used as evidence that prereg predicate L was executed.

Independent manual equation-level audit is durable at commit:

`1bfea2d5f9ac8baf248a173390c7b9b656c87f21`

File:

`analysis/ITER148_ADVERSARIAL_MANUAL_JACOBIAN_AUDIT_2026-09-16.md`.

Manual result:

`MANUAL_PREDICATE_L_PASS_SCOPED`.

The exact prefactors are independently derived as

- A: `tau^(3-d)/Q`;
- B: `(1-tau)^(3-d)/Q`;
- C: `-[tau(1-tau)]^(3-d)/Q`.

This closes the mathematical Jacobian/prefactor predicate for terminal manual adjudication if and only if all other frozen ITER148 predicates are supported by immutable run outputs. It does not by itself terminalize ITER148.

A second literal architectural assertion, `G_target_blind_no_denominator_integration=True`, was manually inspected against the current base/shard/aggregate implementation: the production numerator is generated only from the frozen source tensors/routing and invariant solves; no target coefficient, fitted physics input, or denominator integration enters the reconstruction. This is an implementation-architecture audit, not a numerical result.

## Exact next action

Consume run `35033354189` only after it becomes terminal. Then:

1. inspect every tau-shard artifact and exact rank/held-out status;
2. inspect aggregate artifact and pinned source hash;
3. apply frozen A–L predicates exactly;
4. combine immutable machine evidence with the manual L audit above;
5. terminalize ITER148 with the preregistered scoped class;
6. only a genuine scoped PASS may authorize prospective preregistration of the M3 general-d/O(epsilon) continuation.

Do not start master poles, subtraction, B1, EDT comparison, bridge formation, new physics, or candidate theory from a partial/green CI signal.
