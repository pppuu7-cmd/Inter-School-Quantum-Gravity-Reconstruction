# ISQGR recovery frontier addendum — ITER148 v2 terminal infrastructure cancellation; v3 chunk repair

Date: 2026-09-16
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

This note supersedes the earlier statement that ITER148 run `35033354189` was active. It is now terminal **cancelled** and produced no artifacts. This is an infrastructure/numerical non-result, not a scientific FAIL.

## Auto-research state consumed first

ITER140 v6 run `35040499084` is progressing: multiple family x dimension shards have completed successfully and uploaded exact artifacts, confirming that its rank-path infrastructure repair removed the prior systematic timeout. Do not infer the terminal ITER140 scientific class until all required shards and the exact aggregate complete.

ITER148 v2 run `35033354189` completed `cancelled`. All nine tau-shard jobs were cancelled inside `Exact frozen tau shard`, artifact upload was skipped for every shard, aggregate was skipped, and run artifacts are empty.

## ITER148 v2 diagnosis

The v2 shard computes one entire frozen tau solve in one long-lived SymPy process:

1. construct the frozen 45-row design;
2. invert the exact 45x45 design matrix;
3. evaluate all 45 exact M3 design numerators sequentially;
4. evaluate three exact training held-outs;
5. call generic `A.rank()` repeatedly before writing the artifact.

Two infrastructure pathologies were isolated without changing any scientific object:

- `base.design_panels()` already builds 45 rows by exact rational incremental-pivot elimination, so acceptance of all 45 rows for 45 columns is itself an exact rank-45 certificate. Generic `Matrix.rank()` is redundant here and follows the same pathological SymPy path already observed in ITER140.
- exact M3 numerator panels are individually tractable, but a long sequence in one SymPy process accumulates state and degrades sharply. A local SymPy 1.14 probe using the committed algebra showed the frozen `tau=1/8` first 15 design panels finishing in about 20 seconds, while long sequential runs degrade later. Therefore fresh-process chunking is preferable to another timeout increase.

## v3 infrastructure-only implementation

v3 preserves exactly:

- the frozen 45-element invariant basis;
- the deterministic `design_panels()` sample and exact row values;
- tau training grid `0,1/8,...,1`;
- all three training held-outs at every tau;
- degree <= 8 interpolation predicate;
- no-refit tau `1/3` and `2/5` held-outs;
- repaired direct-source vs `-2*EH_GammaGamma` authority;
- routing, S3 permutation, parity and source-weight controls;
- ITER145 triangle identity and canonical A/B/C bubble maps;
- the same PASS/FAIL classes and claim ceiling.

Only execution granularity changes:

- 9 frozen tau values x 3 disjoint chunks of 15 design panels = 27 production jobs;
- chunk 0 also records the same three training held-out direct values;
- no generic `Matrix.rank()` is called; rank 45 is certified by the frozen exact incremental-pivot design construction;
- the final aggregate restores all 45 values in their original order, performs the same exact solve, and then applies the same frozen checks.

Every chunk and the aggregate record `scientific_predicates_changed: false`.

Manual ITER148 Jacobian predicate-L audit remains commit `1bfea2d5f9ac8baf248a173390c7b9b656c87f21`, classification `MANUAL_PREDICATE_L_PASS_SCOPED`. A machine PASS from v3 is terminally admissible only when combined with this immutable manual audit and the already-recorded target-blind architecture audit.

## Exact next action

Launch v3. Consume only terminal artifacts. If the aggregate returns the frozen scoped PASS, terminalize ITER148 using the machine artifact plus the immutable manual L audit, then preregister the prospective M3 general-d/O(epsilon) continuation. If a scientific frozen predicate fails, apply the corresponding preregistered failure class without basis or degree enlargement. If infrastructure fails again, diagnose only the failing execution stage; do not reinterpret it as physics.
