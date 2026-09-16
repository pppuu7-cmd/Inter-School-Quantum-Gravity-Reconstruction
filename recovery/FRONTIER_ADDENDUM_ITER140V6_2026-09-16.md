# ISQGR recovery frontier addendum — ITER140 v6 rank-path infrastructure repair

Date: 2026-09-16
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

This note supplements `FRONTIER_ADDENDUM_ITER140V5_ITER148V2_2026-09-15.md` and `FRONTIER_ADDENDUM_ITER148_MANUAL_CRITIC_2026-09-16.md`.

Candidate theory remains **UNFORMED / 0%**. Bridge credit remains **0**. ITER147 remains the latest terminal scientific result. ITER148 remains independently active and nonterminal until its frozen run outputs exist and are adjudicated.

## ITER140 v5 adjudication

ITER140 v5 run `35018417447` completed with workflow conclusion `cancelled`. Its family x dimension shard jobs were terminated at the configured 12-minute infrastructure cap and produced no terminal aggregate artifact. Therefore v5 is an infrastructure/numerical non-result, not a scientific FAIL and not a scientific PASS.

The v5 implementation performs the frozen exact contractions, coefficient solve, held-outs and D=4 terminal-authority comparisons, but then calls `A.rank()` on the accepted 28x28 exact design matrix when serializing/printing shard metadata. The frozen `design_panels()` routine has already executed an exact determinant test and raises if `A.det() == 0`. Consequently, for the accepted 28x28 matrix, rank 28 is already exactly certified before the v5 `A.rank()` call.

Diagnostic reproduction under SymPy 1.14 localized the timeout path to this redundant exact rank computation rather than to a changed scientific predicate. No scientific data from the cancelled v5 run is used to modify basis, dimensions, degree bounds, fit/held-out panels, D=4 authority values, or classification rules.

## ITER140 v6 repair

v6 is a pure infrastructure implementation retry of the already frozen ITER140 gate.

Changes:

- retain the same three frozen numerator families;
- retain D=3..10 exact evaluation, D=3..7 training and D=8..10 no-refit validation;
- retain the same 28-element invariant basis and selected design panels;
- retain the same exact held-out panels;
- retain the same `(d-2)^2` trace-polynomial degree <=4 predicate;
- retain the same hash-pinned D=4 terminal authority manifest from ITER138/139;
- retain the same PASS/BLOCKED/SCIENTIFIC_FAIL classification logic and claim ceiling;
- retain the same 24 `(D,family)` shard layout and 12-minute shard cap;
- remove only the redundant `Matrix.rank()` call and record rank 28 from the exact nonzero-determinant certificate already enforced by frozen `design_panels()`.

Implementation files:

- `analysis/iter140_family_dimension_shard_v6.py`;
- `analysis/iter140_aggregate_v6.py`;
- `.github/workflows/iter140_first_mg_general_d_invariant_continuation_v6_rank_repair.yml`.

The shard JSON explicitly records `scientific_predicates_changed: false`; the aggregate requires this for every shard.

## Exact next actions

1. Run ITER140 v6 without changing any frozen scientific predicate.
2. Only a terminal aggregate artifact may adjudicate ITER140.
3. If the terminal aggregate returns `PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN`, immediately feed its exact JSON into the already preregistered ITER143 implementation without changing ITER143 support/contact rules.
4. If v6 is infrastructure-only again, diagnose implementation/runtime only; do not alter the frozen scientific gate based on partial output.
5. Continue ITER148 independently; do not infer its scientific classification from green/partial CI alone.
