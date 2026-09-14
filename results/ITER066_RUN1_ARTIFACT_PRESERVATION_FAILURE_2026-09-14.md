# ITER066 run1 — artifact preservation failure

Date: 2026-09-14
Gate: `ITER066_BH004_CAUSAL_SET_AMPLITUDE_REFINEMENT_SOURCE_AUTHORITY`
Preregistration: `prereg/ITER066_BH004_CAUSAL_SET_AMPLITUDE_REFINEMENT_SOURCE_AUTHORITY_2026-09-14.md`

## Frozen scientific contract

The scientific question, frozen source set, extractor, term selectors, aggregate classifier, claim ceiling, and manual-audit requirement remain those of the preregistration. No scientific predicate is changed by this record.

Frozen sources:

- `1903.11544`
- `2007.13192`
- `gr-qc/0212064`

Frozen extractor: `code/iter066/source_gate.py`.
Frozen workflow at run head: `.github/workflows/iter066_bh004_causal_set_source_authority.yml`.

## Authoritative run1 provenance

GitHub Actions run: `34878725306`
Run head SHA: `915255cfae8d13a10b37f95742fe61cfd9f6e6ad`
Workflow conclusion: `failure`.

Job-level audit:

- source `1903.11544`, job `104092328699`: source audit succeeded; artifact upload succeeded.
- source `2007.13192`, job `104092328921`: source audit succeeded; artifact upload succeeded.
- source `gr-qc/0212064`, job `104092328998`: **Frozen exact-PDF source audit succeeded; the job failed only at `actions/upload-artifact@v4`**.
- aggregate job `104094041545`: executed and uploaded an aggregate artifact, but necessarily classified an incomplete frozen set because the Rideout lane artifact was not preserved.

Preserved artifacts from run1:

- `iter066-1903.11544`: artifact id `10362616120`, digest `sha256:1f197aeac9ec7fadead349430d83d762d15f752fb60cbd89a907abcdc674a65c`.
- `iter066-2007.13192`: artifact id `10361683827`, digest `sha256:cc72d1964cdc9dbc67a739aae3867296736828d52e9d58a6aaaf3a6422b627ed`.
- `iter066-aggregate`: artifact id `10362486113`, digest `sha256:6b0404d0eee46bc1d1429852f86ccba935287369b42d9bb7451e6f544783df73`.
- no preserved `gr-qc/0212064` lane artifact.

## Classification

`ARTIFACT_PRESERVATION_FAILURE_AFTER_SOURCE_AUDIT`

This is not a scientific FAIL, not a source-audit failure, and not evidence that a required causal-set object is absent. The substantive Rideout extraction step completed, but its exact JSON datum was not preserved as an immutable lane artifact.

The workflow used the raw source id in the artifact name (`iter066-${{ matrix.source }}`); for `gr-qc/0212064` this introduces `/` into the artifact name. The defect is therefore downstream of frozen source extraction and upstream of complete aggregate preservation.

## Provenance firewall

The exact missing Rideout JSON is **not reconstructed by inference or memory**. Run1 cannot receive a terminal scientific PASS/FAIL/BLOCKED verdict from the incomplete aggregate.

A retry is admissible only as a transport/provenance repair if all of the following remain unchanged:

- frozen sources;
- `code/iter066/source_gate.py`;
- QTERMS, STERMS, ATERMS and their matching logic;
- aggregate classifier;
- scientific question;
- selectors and thresholds;
- manual equation-level audit requirement;
- claim ceiling.

The only admissible workflow change is to give the Rideout artifact a filesystem/GitHub-safe transport label while still passing the original source id `gr-qc/0212064` to the frozen extractor.

## Scientific status after run1

`UNRESOLVED_PENDING_PROVENANCE_PRESERVING_TRANSPORT_RETRY`

No BH004 numerical amplitude/refinement bridge computation is authorized by run1. `bridge_credit=false`. `CANDIDATE_THEORY=UNFORMED`.