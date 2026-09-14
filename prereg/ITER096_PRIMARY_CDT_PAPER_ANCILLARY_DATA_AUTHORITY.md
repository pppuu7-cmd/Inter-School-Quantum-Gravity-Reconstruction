# ITER096 preregistration — primary 3+1 CDT paper ancillary/data authority

Date: 2026-09-15

## Motivation

ITER094 and ITER095 saturated frozen GitHub and public-archive discovery surfaces without a qualifying dataset. A distinct remaining public route is the source/ancillary payload and explicit availability language of the primary 3+1 CDT papers that generated or consumed the relevant Monte-Carlo ensembles.

## Frozen papers

1. `1704.04373` — New higher-order transition in causal dynamical triangulations.
2. `1802.10434` — The phase structure of CDT with toroidal spatial topology.
3. `2002.01051` — The higher-order phase transition in toroidal CDT.
4. `1904.05755` — Critical Phenomena in Causal Dynamical Triangulations.
5. `2510.02159` — Machine learning in phase transition analysis of lattice quantum gravity (uses numerical 4D CDT Monte-Carlo data; revised 2026).

## Frozen procedure

For each paper independently:

- download the exact current arXiv source package by ID;
- preserve the source archive SHA256;
- recursively list filenames, sizes and SHA256 digests;
- flag data-like ancillary extensions/paths (`csv`, `tsv`, `dat`, `json`, `h5`, `hdf5`, `npz`, `npy`, `txt`, `data`, `supp`, `ancillary`, `github`, `zenodo`, `figshare`);
- search TeX/bibliographic text for availability/link tokens (`data availability`, `code availability`, `supplement`, `supplementary`, `ancillary`, `github`, `zenodo`, `figshare`, `repository`, `available upon request`, `not deposited`, `N_0`, `N_41`, `N_32`).

The scan is inventory/evidence collection only. A filename hit is not a scientific PASS.

## Frozen classifications

### `SCIENTIFIC_PASS_SCOPED_PRIMARY_ANCILLARY_JOINT_COUNT_DATA_AUTHORITY`

Requires a primary-paper source/ancillary payload or explicit linked public resource satisfying the full ITER094 dataset conditions: matched 3+1 `N_0,N_41,N_32` Monte-Carlo samples, coupling metadata, volume-fixing metadata and exact provenance.

### `SCOPED_BLOCKED_PRIMARY_SOURCES_NO_QUALIFYING_PUBLIC_DATA`

Use when all frozen primary sources are successfully audited but expose no qualifying public joint-count dataset. Explicit statements that data/code are not deposited count as positive availability evidence for this BLOCKED classification, not as a scientific failure.

### `INFRASTRUCTURE_FAIL_PRIMARY_SOURCE_AUDIT_PARTIAL`

Use if one or more source archives cannot be retrieved/audited.

## Controls

Figures, TeX tables, scalar histograms, plotted points, low-dimensional examples, source-code snippets, and machine-learning feature descriptions without matched primitive Monte-Carlo counts do not qualify. No reconstruction of raw counts from raster/vector figures is authorized.

## No-retuning lock

Paper set, file-token rules, classifications and PASS conditions are frozen before Action output inspection.

## Claim ceiling

No continuum RG eigenvector, no FRG coupling bridge, no new physics and no candidate theory follow.
