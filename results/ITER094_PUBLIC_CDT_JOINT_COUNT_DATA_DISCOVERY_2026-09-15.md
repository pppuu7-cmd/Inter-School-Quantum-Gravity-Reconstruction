# ITER094 terminal result — public CDT joint-count data discovery

Date: 2026-09-15
Gate: `ITER094_PUBLIC_CDT_JOINT_COUNT_DATA_DISCOVERY`
Preregistration: `c6c9d1b71a033306b0ec19cb6027b19a2d6b8492`
Production head: `35c812381b33f22eac3f45dbb9ab9f9d13c2f2e1`
Authoritative run: `34906684974`
Aggregate job: `104184934584`
Aggregate artifact: `10373135110`
Aggregate digest: `sha256:94ff118b234c8d31a9b4f4ee1369d0415d7be8de8dcefc92a8fd1ba2dedc040c`

## Terminal classification

**`DISCOVERY_SATURATED_NO_PUBLIC_DATA_IN_FROZEN_SET`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Artifact audit

All four frozen repository inventories completed successfully; green CI was not used as scientific PASS.

- `acgetchell/CDT-plusplus` at `b8e35a6c1accb0837a6d8cfa13eb3beb739c906a`: the sole plausible file, `reference/raw/v1/end-to-end.txt`, is an explicit **2+1-dimensional** one-pass reference/test run. It is excluded by the preregistered dimensionality and production-data controls.
- `raylee/CDT` and `tryggth/CDT` both resolve to commit `f6ecdfcc23c20b19473054089cbd68333a52d409`; their sole plausible file is `2p1-fixed-boundaries/data_analysis_scripts/testing_file.txt`, a four-line text fixture with no CDT observables or ensemble metadata. The duplicate tree is counted once scientifically.
- `sedadenboer/CDT` at `e9d8ab71df6e463269b4f9e95a8273b3d7d2afaa`: no plausible data candidate survived the frozen inventory.

No frozen repository provides a 3+1 Monte-Carlo trajectory/table with matched `N_0,N_41,N_32`, `kappa_0,Delta,kappa_4`, and volume-fixing metadata. Therefore ITER093's response-matrix estimator cannot be run from this frozen public-GitHub set.

## Scientific meaning

This is a scoped discovery saturation result, not evidence that the data do not exist anywhere and not a physical failure of CDT. It closes only the frozen repository set. Expansion to public archive/supplement repositories requires a new preregistered discovery gate.

## Claim ceiling

No FRG map, RG eigenvector, bridge derivation, new physics, or candidate theory follows.

## Next admissible route

Search independent public research-data archives/supplement indexes for exact 3+1 CDT transition datasets with joint primitive counts. Any newly found dataset must then pass the original ITER094 PASS conditions before numerical response-matrix estimation is authorized.
