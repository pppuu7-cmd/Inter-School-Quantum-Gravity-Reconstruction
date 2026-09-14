# ITER095 preregistration — public research-archive CDT joint-count data discovery

Date: 2026-09-15

## Motivation

ITER094 saturated a frozen GitHub-repository set without finding a qualifying 3+1 CDT Monte-Carlo dataset. ITER093 still has an exact estimator waiting for matched primitive counts. The next independent discovery surface is public research-data/archive metadata, not another scan of the same repositories.

## Frozen question

Do public research-data archives expose a 3+1-dimensional CDT transition dataset or supplementary record that contains, or explicitly links to, row/configuration-level joint `N_0`, `N_41`, `N_32` Monte-Carlo output together with coupling and volume-fixing metadata sufficient for ITER093?

## Frozen providers

Independent metadata lanes:

1. Zenodo REST search;
2. DataCite REST search;
3. Figshare public article search.

Provider failure is infrastructure failure for that lane, not scientific absence.

## Frozen query families

Each provider must run all of these before any result is inspected:

- exact/near-exact phrase: `causal dynamical triangulations`;
- `causal dynamical triangulations N41 N32`;
- `causal dynamical triangulations bifurcation transition`;
- `causal dynamical triangulations phase transition data`;
- author/title anchors: `Gizbert-Studnicki causal dynamical triangulations`, `Ambjorn causal dynamical triangulations data`.

Returned metadata are filtered only for records whose title/description/keywords contain CDT/causal-dynamical-triangulation context. All surviving record identifiers, URLs, dates, file/link metadata and snippets are preserved exactly.

## Frozen scientific classifications

### `SCIENTIFIC_PASS_SCOPED_PUBLIC_ARCHIVE_JOINT_COUNT_DATA_AUTHORITY`

Requires at least one public 3+1 CDT data product satisfying all ITER094 PASS conditions:

1. matched row/configuration-level `N_0`, `N_41`, `N_32` values or exact reconstructibility for common samples;
2. actual Monte-Carlo/ensemble output, not software-only, toy fixtures, plots, or formulas;
3. `kappa_0`, `Delta`, `kappa_4` (or exact source-defined equivalent) metadata;
4. explicit volume-fixing/ensemble prescription;
5. exact archive record + file/link provenance.

PASS only authorizes a separate preregistered response-matrix computation.

### `SCOPED_BLOCKED_ARCHIVE_RECORDS_INSUFFICIENT`

Use if relevant 3+1 CDT records exist but exposed files/metadata do not meet the joint-count requirements.

### `DISCOVERY_SATURATED_NO_PUBLIC_ARCHIVE_DATA_IN_FROZEN_PROVIDERS`

Use only if all three frozen provider queries complete and no plausible qualifying archive data product survives manual artifact audit.

### `INFRASTRUCTURE_FAIL_DISCOVERY_PARTIAL`

Use if one or more provider lanes cannot complete sufficiently to support saturation.

## Controls / non-credit

No PASS credit for software-only archives, 1+1/2+1 CDT, article PDFs without raw data, machine-learning derived feature tables that omit primitive counts, volume profiles alone, scalar susceptibilities/histograms, or mirrors of already-consumed ITER094 fixtures.

## No-retuning lock

Providers, query families, scientific classifications and PASS conditions are frozen before Action output inspection. New providers require a new iteration.

## Claim ceiling

No bridge credit, no FRG map, no RG eigenvector, no new physics and no candidate theory follow from this discovery gate.
