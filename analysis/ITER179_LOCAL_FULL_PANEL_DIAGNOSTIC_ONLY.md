# ITER179 local full-panel diagnostic — NON-AUTHORITY

Date: 2026-09-19

Status: **DIAGNOSTIC_ONLY / NON_AUTHORITY / DOES NOT TERMINALIZE ITER179**

The authoritative frozen GitHub Actions run remains `35407412179`, head
`9e08f8f18f7cd20f2167ac292ad7dbda3e5ab3ea`.

At the time of this diagnostic all 16 Researcher/Critic matrix jobs in that run were still queued. The calculations below were executed locally only to obtain early information while preserving the frozen preregistration and workflow unchanged.

No successor iteration is authorized from this file.

## Frozen panel diagnostic

The same frozen Researcher equations were evaluated for all eight
`(N, core_seed)` jobs:

| N | core seed | resolved | j* | DeltaBIC | j*/median source rank | lambda*/lambda_source |
|---:|---:|:---:|---:|---:|---:|---:|
| 384 | 311 | yes | 41 | 174.3027 | 1.07895 | 0.93074 |
| 384 | 337 | yes | 41 | 116.1805 | 1.09333 | 0.92435 |
| 512 | 311 | yes | 49 | 239.8686 | 1.11364 | 0.89429 |
| 512 | 337 | yes | 51 | 165.4031 | 1.15909 | 0.85738 |
| 768 | 311 | yes | 49 | 374.2405 | 0.90741 | 1.11846 |
| 768 | 337 | yes | 67 | 365.0839 | 1.24074 | 0.79997 |
| 1024 | 311 | yes | 71 | 533.8831 | 1.12698 | 0.89244 |
| 1024 | 337 | yes | 74 | 503.4970 | 1.18400 | 0.84860 |

All eight local jobs satisfied the frozen line-to-plateau basic selector and the 12-way leave-one-completion-out stability condition.

The leave-one-out break sets were:

- N384/s311: `[41,39,38,42,42,39,41,38,41,38,40,38]`;
- N384/s337: `[42,41,41,39,39,37,38,39,42,41,41,41]`;
- N512/s311: `[50,46,50,49,38,38,48,46,46,50,49,48]`;
- N512/s337: `[51,50,53,50,49,50,52,51,51,51,51,50]`;
- N768/s311: `[58,49,57,53,53,53,49,53,58,53,49,49]`;
- N768/s337: `[68,67,67,70,70,67,67,67,69,73,67,67]`;
- N1024/s311: `[71,72,70,74,71,71,71,69,71,70,71,71]`;
- N1024/s337: `[74,77,73,74,73,75,74,73,73,73,74,74]`.

## Diagnostic campaign aggregate

`RESOLVED_COUNT = 8/8`.

At least one resolved job exists at every frozen N.

For resolved jobs:

`CV(j_star / sqrt(N)) = 0.08397595168`

against the frozen campaign ceiling `0.35`.

Post-selection only:

`median(j_star / median(j_source)) = 1.12031024531`

and

`median(lambda_star / lambda_source) = 0.89336674155`.

Both are within the frozen source-compatibility interval `[0.5, 2.0]`.

Thus, **if and only if** the immutable Actions Researcher and independent Critic reproduce these results and satisfy the preregistered agreement/provenance requirements, the frozen taxonomy would map to

`PASS_SCOPED_ITER179_EIGENVECTOR_FLUCTUATION_TRANSITION_SOURCE_COMPATIBLE`.

This sentence is conditional and is not a terminal classification.

## Scientific signal

Unlike the previously falsified eigenvalue-only two-line knee, the source-derived shared-core eigenvector persistence observable produces a robust decreasing-to-plateau transition in every local frozen job examined here.

The selected transition is close to the independently known source SSEE scale despite the fact that neither the source cutoff nor entropy enters transition construction.

This is precisely the high-information feature that the authoritative Actions run must now attempt to reproduce independently.

## Locks

No change:

`BRIDGE_DERIVED=false`

`NEW_PHYSICS_FOUND=false`

`NEW_QG_THEORY_REQUIRED=false`

`ALL_KNOWN_SCHOOLS_FAIL=false`

`ITER118_MATCHING_AUTHORIZED=false`

`B1_total=UNAUTHORIZED`

candidate theory `UNFORMED / 0%`.
