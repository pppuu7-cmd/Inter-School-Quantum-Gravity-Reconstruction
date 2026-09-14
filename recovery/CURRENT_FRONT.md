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

## ITER059 — failed-only rerun attempt 5 ACTIVE

Authoritative run remains **34835772221** at frozen production head `7dd94a511d95be0512ed5bbeb76c7682a223180b`; current run attempt is **5**.

Attempt 4 materially improved the discovery front: `eprl-rg-simplicial` job `104007923037` completed scientifically and uploaded artifact `10351617556` (digest `sha256:04781968cac707778dc22880145809ded13f544956799611cb09ad77098faadd`). The only remaining missing lane, `eprl-refinement-map` job `104007922804`, again failed before scientific evaluation with HTTP 429. Its raw log terminates at metadata retrieval with `RuntimeError: <HTTPError 429: 'Unknown Error'>`; no inclusion/scoring predicate was reached.

Attempt-4 aggregate job `104009338640` uploaded artifact `10352407284`, digest `sha256:91ad884a7e45b21a37edf3ce398117620f9246ec7c68e59ece7b42781087d044`. It is correctly classified `INFRASTRUCTURE_FAIL_DISCOVERY`, with `missing=[eprl-refinement-map]`; the only candidate ID remains `1107.2633`, already source-qualified and BLOCKED by ITER060. Therefore there is no new scientific PASS/FAIL and no bridge credit.

Only the failed lane was re-run. Attempt 5 currently has **1 scientifically useful job queued / 0 in_progress**: `104025417356` (`eprl-refinement-map`). Successful lanes were not duplicated. Frozen queries, inclusion scoring, thresholds and consumed-source set remain unchanged.

Recovery state transition commit: `26958d496ec46a0df2a797634f0933facfa4431c`.

## Readiness

Current iteration/front completion: **≈70%**. Overall scientific programme: **49% (Δ0)**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

## Exact next admissible action

Consume raw terminal output from attempt-5 job `104025417356`, then the fresh aggregate if produced. If it completes scientifically and yields any genuinely new source ID, freeze that exact ID in a separate source-qualification gate before interpretation. If it completes scientifically with no new ID beyond blocked `1107.2633`, classify ITER059 as `DISCOVERY_SATURATED_SCOPED`, preserve the Lorentzian refinement-map authority blocker, and shift compute to another independent PHASE_1 branch. If HTTP 429 recurs, classify only as infrastructure failure; do not weaken or retune frozen queries/scoring/thresholds/map criterion.
