# ITER088 source authority — retrospective CdS spatial-gap infrared scaling adjudication

Date: 2026-09-15
Gate: `ITER088_RETROSPECTIVE_CDS_SPATIAL_GAP_IR_SCALING_ADJUDICATION`
Protocol commit: `385f70a3c24f3f4dc39a5ba8e2380516786ad5d7`

## Source status

The decisive source is arXiv `1903.00430` / Phys. Rev. D 99, 114506 (2019), Clemente, D'Elia and Ferraro, *Running scales in causal dynamical triangulations*.

A PDF screenshot was requested during audit but the retrieval service returned a cache miss. The adjudication therefore uses the source's extracted PDF text; no claim of successful visual-page inspection is made.

## Published setup

The paper studies four-dimensional CDT with spatial topology `S^3`. In the `C_dS` phase it reports a simulation at fixed bare couplings

`kappa_0 = 0.75`, `Delta = 0.7`,

with total spatial volume fixed to

`V_S,tot = N_41/2 = 40K`

for the main sample, plus checks at additional total volumes.

The single-slice spatial volume `V_S` varies over the extended blob. Slices are binned by `V_S`, and average low-lying eigenvalues are computed within bins. The source explicitly displays results for `n=1,3,5` and states that similar behavior holds for modes up to a few tens.

The discrete spatial operator is the same unweighted four-regular dual-graph Laplacian used in the ISQGR spectral route,

`L = 4 I - A`,

with `lambda_0=0` and `lambda_1` the spectral gap.

## Published finite-size fit

The source fits the low eigenvalues to

`<lambda_n> = A_n V_S^(-2/d_eff)`.

For the `C_dS` data it reports that the fits have approximately unit chi-squared per degree of freedom and yield

**`d_eff approximately 1.6`**,

in agreement with earlier large-scale spectral effective-dimension measurements of CDT spatial slices. Similar results are stated for `n` up to a few tens.

The same source concludes that the gap closes in the thermodynamic limit in `C_dS`, with the closing governed by this measured effective dimension.

## Comparison with the round-S3 residue of ITER087

The ITER087 relative round-`S^3` hypothesis would require

`d_IR = 3`,

hence

`lambda_n propto V_S^(-2/3)`.

The published source instead gives

`d_eff approximately 1.6`,

corresponding to an exponent

`2/d_eff approximately 1.25`.

This is not a small normalization discrepancy. The exponent itself differs materially from the round-three-dimensional value `2/3`, and a multiplicative normalization cannot repair an exponent mismatch.

Therefore the accessible low-mode spatial spectrum in the published `C_dS` ensemble does **not** support the round-`S^3` infrared finite-size law.

## Predicate adjudication

- A fixed-bare-coupling `C_dS` ensemble: **PASS**.
- B explicit slice-volume binning and low-mode averages: **PASS**.
- C explicit power-law fit form: **PASS**.
- D source-reported effective dimension: **PASS**, `d_eff approximately 1.6`.
- E fit quality/mode-family authority: **PASS_SCOPED** — chi-squared per dof approximately one; modes `1,3,5` shown and similar results reported to a few tens.
- F gap closure distinguished from dimension: **PASS_CONTROL** — gap closes, but with `d_eff approximately 1.6`, not 3.
- G global de-Sitter profile kept distinct: **PASS_CONTROL**.
- H no FRG rescue: **PASS_CONTROL**.

## Structural consequence

The direct reduced CDT↔FRG minisuperspace map and the spatial Laplacian probe live in genuinely different observable sectors.

A de-Sitter-like global three-volume profile does not imply that individual spatial slices have a round-three-sphere low-mode spectrum at accessible finite regulator. This directly explains why attempts in ITER086/087 to convert the global reduced radius into a lowest-nonzero spatial-gap identity are overconstrained.

The observed `d_eff approximately 1.6` is a source-qualified property of the finite-regulator `C_dS` spatial spectrum. It is not promoted to the final CDT continuum infrared dimension.

## Source classification

**`SOURCE_REJECTS_ROUND_S3_IR_SCALING_ACCESSIBLE_CDS`**

Prospective validation credit: **0 by protocol**.
Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.
