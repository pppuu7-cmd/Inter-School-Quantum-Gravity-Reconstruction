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

## ITER059 — transport-repaired discovery ACTIVE RETRY

Authoritative run remains **34835772221** at frozen production head `7dd94a511d95be0512ed5bbeb76c7682a223180b`.

The latest completed attempt was **INFRASTRUCTURE FAIL DISCOVERY PARTIAL**, not a scientific negative. Raw logs show `eprl-rg-simplicial` job `103949121291` and `eprl-refinement-map` job `103949121524` failed before scientific evaluation with HTTP 429. Successful lanes remained valid. Aggregate job `103950107579` / artifact `10344805518` (`sha256:828ea5babbb64013c2f16492a776773d0f4c05a979156db73305a4aa02ecf6fa`) reported missing lanes `[eprl-rg-simplicial, eprl-refinement-map]` and only one metadata candidate, `1107.2633`, which is already source-qualified and BLOCKED by ITER060.

Frozen queries, inclusion scoring, thresholds and consumed-source set remain unchanged. No scientific predicate was weakened or retuned.

A retry of the failed discovery work was started. Current scientifically useful workload at the last check: **0 queued / 1 in_progress** — job `103964393982` (`eprl-rg-simplicial`) in progress. The recreated `eprl-refinement-map` job `103964395296` has already failed again pre-science; it must not be interpreted as a scientific negative and may be retried only after the active run is no longer executing. Successful lanes are not to be reinterpreted as new science.

Recovery state commit: `b7eb6cad1facccd679a6a96ac635ce8aeb0d8ca6`.

## Readiness

Current iteration/front completion: **≈60%**. Overall scientific programme: **49% (Δ0)**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

## Exact next admissible action

Consume terminal output from job `103964393982`. Once the run is no longer active, retry only the still-failed `eprl-refinement-map` lane if it remains an infrastructure failure. Do not change frozen queries, scoring, thresholds, source set or map criterion. If all discovery lanes eventually complete with no genuinely new source ID beyond blocked `1107.2633`, preserve the Lorentzian refinement-map authority blocker and shift compute to another independent PHASE_1 branch rather than weakening the explicit-map requirement.
