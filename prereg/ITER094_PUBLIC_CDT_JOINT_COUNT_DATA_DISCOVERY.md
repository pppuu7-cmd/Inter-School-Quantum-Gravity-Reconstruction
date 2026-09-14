# ITER094 preregistration — public CDT joint-count data discovery

Date: 2026-09-15

## Motivation

ITER093 established the exact CDT-internal response object

`F_ij = Cov(A_i,A_j)`, with `A=(-N_0, N_41-6N_0, N_4)` and `N_4=N_41+N_32`,

but found that the frozen published summaries do not expose matched off-diagonal connected covariances. The highest-information reopening route is therefore a search for public raw/supplementary Monte Carlo data containing jointly sampled primitive counts.

## Frozen question

Does a public repository in the frozen candidate set contain a scientifically reusable 3+1-dimensional CDT trajectory or matched table with joint per-sample/per-configuration values sufficient to construct the ITER093 primitive vector, together with enough coupling/ensemble metadata to interpret the samples?

## Frozen candidate repositories

1. `tryggth/CDT` — public CDT tools/code with explicit `3p1` implementation.
2. `acgetchell/CDT-plusplus` — public CDT implementation; retained as an implementation/data-output candidate, not presumed to contain production 4D transition data.
3. `sedadenboer/CDT` — public repository returned by exact GitHub repository search for causal dynamical triangulations.
4. `raylee/CDT` — public repository returned by the same search; treated independently only if its tree/content is non-identical to another candidate.

Low-dimensional repositories are excluded from PASS credit even if they expose analogous observables.

## Frozen discovery procedure

For each candidate repository, recursively inventory the default-branch tree and flag files whose path or textual content contains any of:

- `N0`, `N_0`, `vertices`;
- `N41`, `N_41`, `(4,1)`, `41-simplex`;
- `N32`, `N_32`, `(3,2)`, `32-simplex`;
- `kappa0`, `kappa_0`, `kappa4`, `kappa_4`, `delta`, `Delta`;
- `volume fixing`, `volume-fixing`, `target volume`, `timeseries`, `trajectory`, `measurements`, `output`, `data`.

Binary files are inventoried by path/size only. Text files are scanned without modifying upstream content.

## Frozen scientific classifications

### `SCIENTIFIC_PASS_SCOPED_PUBLIC_JOINT_COUNT_DATA_AUTHORITY`

Requires at least one public 3+1 CDT data product satisfying all of:

1. joint row/configuration-level values from which `N_0`, `N_41`, and `N_32` are directly available or exactly reconstructible for the same samples;
2. samples are actual Monte Carlo/ensemble output, not only code variables, formulas, toy fixtures, or initial configurations;
3. coupling metadata identify at least `kappa_0`, `Delta`, and `kappa_4` (or an exact source-defined equivalent) for the dataset;
4. volume-fixing/ensemble prescription is explicit enough to determine whether the cosmological row is constrained and how;
5. provenance is exact: repository, commit/tree object, path, and file digest.

PASS only authorizes preregistration of the ITER093 response-matrix estimator on that dataset. It gives no FRG bridge credit.

### `SCOPED_BLOCKED_PUBLIC_DATA_INSUFFICIENT`

Use if public candidates contain 3+1 code and/or marginal/derived outputs but no dataset meeting all PASS requirements.

### `DISCOVERY_SATURATED_NO_PUBLIC_DATA_IN_FROZEN_SET`

Use if the complete frozen repository trees contain no plausible production 3+1 raw/supplementary data product after path/content inventory.

### `INFRASTRUCTURE_FAIL_DISCOVERY_PARTIAL`

Use only when repository/API/network failures prevent complete inventory. A green job is not by itself scientific PASS.

## Controls / non-credit cases

The following do not satisfy PASS:

- source code merely defining `N0/N41/N32` counters;
- synthetic/test data;
- 1+1 or 2+1 CDT trajectories;
- a volume profile alone;
- scalar susceptibilities/histograms without matched primitive counts;
- separate files measured at unmatched Markov-chain points unless an exact shared sample identifier permits deterministic joining;
- forks/mirrors duplicating an already-consumed dataset;
- inferred `N32` from a relation not valid sample-by-sample under the source ensemble.

## No-retuning lock

Candidate repositories, inclusion criteria, and classification thresholds are frozen before Action results are inspected. If the frozen set is negative, later expansion to new repositories requires a new preregistered discovery iteration rather than reinterpretation of ITER094.

## Claim ceiling

No continuum RG eigenvector, no FRG coupling map, no bridge derivation, no new physics, and no candidate theory follow from this discovery gate alone.
