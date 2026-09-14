# ITER096 terminal — primary 3+1 CDT paper ancillary/data authority

Date: 2026-09-15
Gate: `ITER096_PRIMARY_CDT_PAPER_ANCILLARY_DATA_AUTHORITY`

## Frozen classification

`SCOPED_BLOCKED_PRIMARY_SOURCES_NO_QUALIFYING_PUBLIC_DATA`

## Authoritative run

- production head: `d219bd3683e613ce1154eca79c3782b292eb0224`
- workflow run: `34907499223`
- conclusion: `success` (infrastructure only; green CI is not scientific PASS)
- aggregate artifact: `10372978377`
- aggregate digest: `sha256:5b76452991b5a6633b4339b7904f18d8c546bcd258f2b4c47d08ba3fe5b248a9`

## Manual adjudication against preregistration

All five frozen arXiv source packages were retrieved and inventoried without source-transport errors:

| arXiv | files | data-like files | manual disposition |
|---|---:|---:|---|
| `1704.04373` | 26 | 0 | paper/source material only; no matched primitive-count dataset |
| `1802.10434` | 60 | 0 | paper/source material only; no matched primitive-count dataset |
| `2002.01051` | 25 | 0 | paper/source material only; no matched primitive-count dataset |
| `1904.05755` | 101 | 0 | paper/source material only; no matched primitive-count dataset |
| `2510.02159` | 27 | 1 | sole data-like hit is `00README.json`; remaining payload consists of TeX/Bib/PDF figure/table assets, not matched raw MC counts |

The source text confirms use/definition of the global CDT quantities such as `N_0`, `N_41` and `N_32`, but mentioning or plotting these observables is not equivalent to publishing matched configuration-level samples.

No frozen source package exposes a public payload satisfying the ITER094/ITER096 PASS requirements simultaneously:

1. matched 3+1 configuration-level `N_0,N_41,N_32` samples;
2. coupling metadata for the same samples;
3. volume-fixing metadata;
4. exact provenance sufficient to evaluate the ITER093 covariance/response matrix.

## Controls

- `FIGURE_AS_DATA_CONTROL`: passed. PDF plots/histograms are not reconstructed into raw samples.
- `SCALAR_SUMMARY_AS_JOINT_SAMPLE_CONTROL`: passed. Published marginal/scalar summaries are not promoted to matched joint counts.
- `SOURCE_CODE_AS_DATA_CONTROL`: passed. TeX/source snippets defining observables are not treated as MC records.
- `ML_FEATURE_DESCRIPTION_CONTROL`: passed. A paper using `N_0`, `N_41`, `N_32` as features does not itself supply the required matched primitive dataset.
- `GREEN_CI_SCIENTIFIC_PASS_CONTROL`: passed. Successful Action execution is only infrastructure success.

## Consequence for ITER093

The exact CDT-internal response object remains

`F_ij = Cov(A_i,A_j)`, with `A=(-N_0, N_41-6N_0, N_4)` and `N_4=N_41+N_32`.

ITER096 does not supply the off-diagonal connected covariances needed to evaluate this matrix. Therefore no ITER093 response-matrix computation is authorized from the frozen primary-paper ancillary route.

## Discovery saturation

Together, ITER094 (public GitHub discovery), ITER095 (Zenodo/DataCite/Figshare discovery), and ITER096 (primary arXiv source/ancillary payload audit) exhaust the currently frozen public-data surfaces for this specific matched-count object. Repeating broad discovery without a new provider or explicit new dataset would be low-information retesting.

## Claim ceiling

Bridge credit remains `0`. Candidate theory remains `UNFORMED / 0%`. No continuum RG eigendirection, FRG coupling bridge, new physics, or common-parent claim follows.

## Next admissible route

Do not repeat public raw-data discovery. The next high-information route is to ask whether source-published marginal variances/susceptibilities and exact linear identities can place rigorous positive-semidefinite/Cauchy-Schwarz bounds on the missing ITER093 response matrix strongly enough to exclude or constrain candidate renormalized eigendirections without reconstructing unavailable joint samples.
