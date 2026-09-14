# ITER043 — pre-science terminal record

Date: 2026-09-14

## Classification

**`INFRASTRUCTURE_FAIL PRE-SCIENCE`**, additionally **VOID FOR SCIENTIFIC INFERENCE** because the preregistration inherited an ITER042 interpretation that conflicts with the already-existing durable source-of-truth result commit `70a8ccd7f88c9ff98a4d0b5c7cfb8996039f71f6` (`DELEGATED_AUTHORITY_SOURCE_EXPANSION_BLOCKED`).

No scientific predicate from ITER043 may update the RC006 frontier.

## Provenance

- prereg commit: `d1aca4c37fe855ca00e7f9a92bceea241f82e700`
- workflow/production head: `a1102cbe88c3f99110710ea56fe90015d64f66db`
- run: `34807715146`
- jobs: null `103862737182`; delegated-preview `103862737295`; Coman `103862737300`; Dowdall `103862737304`; aggregate `103862770361`
- aggregate artifact: `10333332986`, digest `sha256:9b394312494e422f4cd67ed0008d7b5f60109c53363b322d36c166a4442effb1`
- other completed artifacts: null `10334175257` (`sha256:68f48d5d7ea81b1b8482fdde286c426e639680a33ec3c86a6c947e70c01f6d24`); delegated preview `10334160195` (`sha256:5e88ab64673984503d7beb2ad7cfbb2d01185d774533b7a301984c4bbf31f714`); Coman `10333931463` (`sha256:bfb11d827b498d1a11ae6acd3a9048602476404d4ecc45dffeb7e407bddee193`).

Raw aggregate: `INFRASTRUCTURE_FAIL`, `lane_count=3`, `transport_complete=false`, `ITER039_remains_scientific_fail=true`, `numerical_retry_authorized=false`, `bridge_credit=false`, `candidate_theory_authorized=false`.

## Causal technical failure

Dowdall lane failed before evidence extraction: the frozen Nottingham PDF URL returned HTTP 404 (`curl` exit 22). Therefore four-lane evidence collection was incomplete. This is not a scientific FAIL.

## Why no repair/re-run

A transport-only repair would normally be admissible. It is intentionally **not** performed here because the latest-commit audit found that ITER042 had already been authoritatively classified BLOCKED before ITER043 was created. ITER043 therefore does not represent an authorized successor gate from the durable frontier. Re-running it would waste compute on a gate with a superseded premise.

## Scientific state unchanged

ITER039 remains SCIENTIFIC FAIL. ITER041 and ITER042 remain source-BLOCKED. RC006 numerical retry remains unauthorized. Candidate theory = `0 / UNFORMED`; bridge credit = 0; Eq.(29)/Lambda/TNR unauthorized.

The next useful work must come from an independent, nonduplicating PHASE_1 priority rather than an RC006 retry.