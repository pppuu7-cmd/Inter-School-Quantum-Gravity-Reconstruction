# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## Persistent locks

RC006 numerical retry remains unauthorized. RC009 remains SCOPED BLOCKED. Lorentzian Delta4 negative results remain preserved. No full Eq.(27), Eq.(29), Lambda, one-step TNR, bridge derivation or candidate-theory construction is authorized.

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `0 / UNFORMED`.

Forbidden claims remain `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.

## Lorentzian frontier summary

ITER054 and ITER055 remain scoped SCIENTIFIC PASS results for bounded five-vertex fixed summands and four low-spin recoupling transport classes without retuning. They do not establish a full sum or refinement invariance.

ITER056, ITER057 and ITER058 remain source/refinement-transfer blockers: no exact source-qualified Lorentzian simplicial EPRL 5→1 coarse↔fine map has been established.

ITER060 remains **SCOPED BLOCKED — `SCOPED_BLOCKED_NO_EXPLICIT_REFINEMENT_MAP`** for arXiv:1107.2633. Durable result commit `d089cc48717fa0b0f893f71af9859ea10fe12780`; authoritative run `34835559911`; aggregate artifact `10344285407`, digest `sha256:e5b88e4fc9b0bdab73c0fa4a371acd800be5ac18f1b88b0a5887275193ff3244`.

## ITER059 — failed-only rerun attempt 4 ACTIVE

Authoritative run remains **34835772221** at frozen production head `7dd94a511d95be0512ed5bbeb76c7682a223180b`; current run attempt is **4**.

Attempt 3 is classified **INFRASTRUCTURE FAIL DISCOVERY PARTIAL**, not a scientific negative. The two remaining discovery lanes both failed before scientific evaluation with HTTP 429: `eprl-rg-simplicial` job `103983244933` and `eprl-refinement-map` job `103983246550`. Their logs terminate at the metadata fetch with `RuntimeError: <HTTPError 429: 'Unknown Error'>`; no inclusion/scoring predicate was reached.

The successful lanes remain valid and are not being reinterpreted as new science. The previously discovered ID `1107.2633` remains already source-qualified and BLOCKED by ITER060. Frozen queries, inclusion scoring, thresholds and consumed-source set remain unchanged.

Because the authoritative run was terminal, only the failed jobs were re-run. Attempt 4 currently has **2 scientifically useful jobs queued / 0 in_progress**: `104007922804` (`eprl-refinement-map`) and `104007923037` (`eprl-rg-simplicial`). Successful jobs were not duplicated.

Recovery state commit for this transition: `aa9837219028eb71d08d5974d1c1fd0824eecfde`.

## Readiness

Current iteration/front completion: **≈60%**. Overall scientific programme: **49% (Δ0)**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

## Exact next admissible action

Consume raw terminal outputs from attempt-4 jobs `104007922804` and `104007923037`, then consume the fresh aggregate. If they complete scientifically and yield any genuinely new source IDs, freeze each exact ID in a separate source-qualification gate before interpretation. If all completed discovery lanes yield no new IDs beyond blocked `1107.2633`, preserve the Lorentzian refinement-map authority blocker and shift compute to another independent PHASE_1 branch. If HTTP 429 recurs, classify it only as infrastructure failure; do not weaken or retune frozen queries/scoring/thresholds/map criterion.
