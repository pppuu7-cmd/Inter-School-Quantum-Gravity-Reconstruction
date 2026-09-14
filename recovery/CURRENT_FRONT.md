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

## ITER059 — failed-only rerun attempt 6 ACTIVE

Authoritative run remains **34835772221** at frozen production head `7dd94a511d95be0512ed5bbeb76c7682a223180b`; current run attempt is **6**.

Attempt 5 target job `104025417356` (`eprl-refinement-map`) completed as **INFRASTRUCTURE FAIL PRE-SCIENCE**. Raw logs terminate in `code/iter059/discovery.py::fetch` with `RuntimeError: <HTTPError 429: 'Unknown Error'>` before any inclusion/scoring predicate was evaluated. Therefore this is not a scientific FAIL and does not change bridge credit or readiness.

Attempt-5 aggregate job `104026737223` uploaded artifact **`10353877344`**, digest `sha256:27ac1f026e19295ada6fc28123e0b26ae7b5b6709a95c239d5cfedf7c9f8b209`. The aggregate classification is `INFRASTRUCTURE_FAIL_DISCOVERY`, with `missing=[eprl-refinement-map]`; the only candidate ID remains `1107.2633`, already source-qualified and BLOCKED by ITER060. No new source authority was established.

Durable attempt-5 result note commit: `8a812bd9236cf12e049a5079ec351868626330fa`.

A failed-only rerun has been requested without changing frozen science. GitHub created workflow attempt 6; latest verified workflow state is **queued**. Queries, inclusion/scoring predicates, thresholds, consumed-source set, and explicit-map criterion remain unchanged.

Latest `recovery/state.json` commit: `7ac9122b056b5173a284ac286ad7c973a96b8643`.

## Readiness

Current iteration/front completion: **≈70%**. Overall scientific programme: **49% (Δ0)**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

Scientifically useful compute at the latest verified check: **1 queued / 0 in_progress**. This satisfies anti-idle while the single unresolved frozen discovery lane is retried; no duplicate heavy computation is being credited as new science.

## Exact next admissible action

Consume the terminal attempt-6 `eprl-refinement-map` raw output and fresh aggregate. If it completes scientifically and yields a genuinely new source ID, freeze that exact ID in a separate source-qualification gate before interpretation. If it completes scientifically with no new ID beyond blocked `1107.2633`, classify ITER059 as `DISCOVERY_SATURATED_SCOPED`, preserve the Lorentzian refinement-map authority blocker, and shift compute to another independent PHASE_1 branch. If HTTP 429 recurs, classify only as infrastructure failure; do not weaken or retune frozen queries/scoring/thresholds/map criterion.
