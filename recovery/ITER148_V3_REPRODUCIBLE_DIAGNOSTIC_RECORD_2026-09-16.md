# ITER148 v3 reproducible diagnostic record

Date: 2026-09-16
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

This record captures the completed research iteration that followed terminal infrastructure cancellation of ITER148 v2. It is diagnostic/infrastructure evidence only; it does not itself assign a scientific PASS/FAIL to ITER148.

## Auto-research state inspected first

- ITER148 v2 run `35033354189` is terminal `cancelled`.
- All nine tau jobs were cancelled inside `Exact frozen tau shard` at the 90-minute job cap.
- Artifact upload was skipped for every tau job; aggregate was skipped; run artifact count is zero.
- Therefore v2 is `NUMERICAL_OR_INFRASTRUCTURE_FAIL` in research bookkeeping, not a scientific failure of the frozen ITER148 object.
- ITER140 v6 run `35040499084` has already produced multiple successful exact shard artifacts, but its remaining jobs and aggregate were still queued at the final audit of this iteration. No terminal ITER140 scientific classification is inferred here.

## Independently formulated iteration question

> Does ITER148 reproduce the pathological generic SymPy `Matrix.rank()` execution path seen in ITER140, and, after removing that redundant path, is the remaining timeout caused by long-lived SymPy state across the 45 exact frozen design panels? If so, preserve the frozen scientific object exactly and change only execution granularity until an exact chunk is reproducibly bounded well below the CI timeout.

## Exact rank diagnosis

Frozen ITER148 `design_panels()` does not choose rows heuristically after the fact. It builds the design by exact rational incremental-pivot elimination (`add_rank_row`) and accepts a row only when it creates a new pivot. It terminates only after 45 accepted rows for the 45-column frozen basis.

Therefore successful construction of the frozen design is already an exact rank-45 certificate. Calling generic SymPy `Matrix.rank()` afterward is redundant. ITER148 v2 called `A.rank()` three times per tau shard (JSON field, stdout summary, and exit predicate), after the expensive exact work.

A local SymPy 1.14.0 reproduction of the committed design algebra gave:

- basis size: 45;
- accepted design rows: 45;
- exact pivots: 45;
- design construction: about `0.42 s`;
- exact `A.inv(method='DM')`: about `0.13 s`;
- generic `A.rank()` did not complete inside an 8-second diagnostic cutoff on the same already-certified matrix.

The cutoff is a diagnostic bound, not a measured rank runtime; the mathematical rank certificate comes from the exact incremental-pivot construction itself.

## Exact numerator process-state diagnosis

Using the committed D=4 M3 algebra (`A_R1`, projector, `chi_tensor`, `dR_tensor`, `eh_gamma_gamma_cubic`, and frozen `numerator_fast`) with SymPy 1.14.0:

- isolated frozen design panels are individually tractable (typically roughly sub-second to low-single-second in the probe);
- a single long-lived process evaluating the full 45-panel sequence degrades sharply later in the sequence;
- evaluating the same later panels in fresh processes returns to the short per-panel runtime;
- explicit SymPy cache clearing/GC reduces retained state but does not make a 45-panel monolithic process as robust as fresh-process chunking.

This isolates the second bottleneck as execution-state accumulation rather than a change in the frozen physics object or a uniquely pathological frozen design point.

## Chunk-size reproduction

For frozen `tau = 1/8`, a fresh SymPy 1.14.0 process evaluated frozen design panels 0..14 (15 exact panels) in approximately `19.9 s` total in the diagnostic reproduction.

The CI chunk timeout chosen for v3 is 20 minutes, leaving a large infrastructure margin while keeping each job below the process length at which degradation was observed. Chunk 0 additionally evaluates the same three frozen training heldouts, so its process contains 18 exact numerator evaluations, still below the degraded long-sequence region observed in the diagnostic probe.

## Implemented v3

Merged PR #2 at merge SHA:

`1b85eec35af8f157e2982040013a70836a49334f`

New implementation files only (no edits to preregistration or frozen v2/base implementation):

- `analysis/iter148_tau_chunk_v3.py`
- `analysis/iter148_aggregate_v3.py`
- `.github/workflows/iter148_m3_full_invariant_chunked_v3.yml`
- `recovery/FRONTIER_ADDENDUM_ITER148V3_CHUNK_REPAIR_2026-09-16.md`

Execution geometry is 9 frozen tau values x 3 disjoint 15-panel chunks = 27 exact production jobs. The aggregate restores all 45 values in original frozen order and applies the same basis, tau-degree, no-refit heldouts, direct-source authority, routing/permutation/parity/source-weight, ITER145 map, classification and claim-ceiling logic. New artifacts explicitly record `scientific_predicates_changed: false`.

Manual predicate-L audit remains immutable at commit `1bfea2d5f9ac8baf248a173390c7b9b656c87f21`, classification `MANUAL_PREDICATE_L_PASS_SCOPED`.

## Launched run and final state of this iteration

ITER148 v3 run: `35044099632`.

At the final audit of this iteration, all 27 production jobs are `queued` and artifact count is zero. Repository-level Actions reports zero `in_progress` runs and exactly two queued runs: ITER140 v6 and ITER148 v3. Thus v3 had not yet been allocated a runner; the absence of artifacts is not evidence about the v3 computation or any scientific predicate.

## Authorized continuation

1. Consume v3 only after runners actually start and immutable chunk artifacts appear.
2. A chunk success is infrastructure evidence only; do not infer ITER148 PASS from partial chunks.
3. Only the terminal exact aggregate, combined with the immutable manual predicate-L audit, may adjudicate ITER148.
4. If the frozen scoped PASS is terminal, prospectively preregister M3 general-d/O(epsilon) continuation before inspecting its outputs.
5. Do not begin master-pole, subtraction, B1, EDT, bridge, new-physics, or candidate-theory claims from queued/partial CI state.
