# ITER059 attempt 6 — Lorentzian refinement open-authority discovery

Date: 2026-09-14

## Terminal classification

`INFRASTRUCTURE_FAIL_DISCOVERY — TARGET_LANE_HTTP_429_PRE_SCIENCE`

This is not a scientific NULL, not a negative result for Lorentzian EPRL refinement, and not evidence that an exact coarse↔fine refinement map does not exist.

## Authoritative execution

- workflow: `ISQGR ITER059 Lorentzian refinement open authority discovery`
- run: `34835772221`
- run attempt: `6`
- production head: `7dd94a511d95be0512ed5bbeb76c7682a223180b`
- terminal workflow status: `completed / failure`
- target job `discovery (eprl-refinement-map)`: `104048033247`, `completed / failure`
- aggregate job: `104049232944`, `completed / success`

Other discovery lanes completed successfully, but the prospectively required target lane did not.

## Decisive failure mode

The target command

`python3 code/iter059/discovery.py --lane 'eprl-refinement-map' --out out/evidence.json`

failed inside the transport fetch before source predicates were applied or an evidence artifact was produced:

`RuntimeError: <HTTPError 429: 'Unknown Error'>`

Therefore the target lane supplies no scientific discovery/null evidence. Its artifact upload was skipped.

## Aggregate provenance

Because the target attempt-6 artifact is missing, the aggregate records:

- classification: `INFRASTRUCTURE_FAIL_DISCOVERY`
- missing lane: `eprl-refinement-map`
- metadata-only candidate IDs from surviving evidence: `1107.2633`
- `refinement_map_derived=false`
- `bridge_credit=false`
- candidate theory: `UNFORMED / 0%`

Fresh attempt-6 aggregate artifact:

- artifact id: `10357280571`
- digest: `sha256:9ab1f4be8109f0ccc1554e15ca7ece46693b22b2a43e4a19fab4d36b228eb78c`

The ID `1107.2633` is not new scientific authority: it was already separately source-qualified in ITER060 and terminally classified `SCOPED_BLOCKED_NO_EXPLICIT_REFINEMENT_MAP`.

## Scientific interpretation

ITER059 has now incurred repeated transport/provider failures. Re-running the same discovery transport again without a new retrieval route has low expected information gain and is not selected as the next scientific gate.

This practical saturation of the transport route must not be promoted to a scientific saturation claim. The exact Lorentzian coarse↔fine refinement-map authority remains unresolved.

## Locks

Still false / unauthorized:

- `refinement_map_derived`
- `bridge_credit`
- `candidate_theory_authorized`
- `NEW_PHYSICS_FOUND`
- `NEW_QG_THEORY_REQUIRED`
- `ALL_KNOWN_SCHOOLS_FAIL`
- `UNIVERSAL_BRIDGE_FOUND`

Candidate theory remains `UNFORMED`.

## Next-gate consequence

Close active compute for ITER059 and reassess an independent PHASE_1 realization. Do not issue another identical transport rerun unless a genuinely different source/transport route is prospectively frozen.
