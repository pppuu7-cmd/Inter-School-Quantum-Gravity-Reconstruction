# ITER086 terminal result — canonical spectral-gap scale ↔ reduced-map FRG theory-space point

Date: 2026-09-15
Gate: `ITER086_CANONICAL_SPECTRAL_GAP_SCALE_THEORY_SPACE_POINT_TEST`
Preregistration: `f54bb3238eb1a52923230537256e973936d82ec2`
Source authority: `16447e30a109dbe8aaa109cd39584de7e8a3273f`
Adversarial review: `b600057277043eb3d915ccb60060640df0eeaf12`

## Terminal classification

**`FAIL_SCOPED_CANONICAL_GAP_SCALE_INCOMPATIBLE`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Frozen hypothesis rejected

ITER086 prospectively froze the bridge hypothesis

`H_gap: k^2 = z_1 = 9 ell_1/a^2`,

where `ell_1` is the lowest strictly positive CDT spatial graph-Laplacian eigenvalue. No higher mode or target-fitted threshold was allowed.

Conditional on this hypothesis, ITER078+ITER084+ITER085 algebra would indeed close the dimensionless FRG coordinates:

`g_1 = (3/(8 pi)) ell_1 Gamma (omega/omega_0)^(4/3)`,

`lambda_1^FRG = [8 pi/(3*1.63)] (omega/omega_0)^(2/3)/(ell_1 sqrt(N_4))`.

The algebra is not the failure.

## Decisive held-out consistency failure

The direct CDT↔FRG source itself defines the self-consistent Euclidean de-Sitter background by

`R_k = 3/(sqrt(lambda_k) k)`.

On its equatorial round `S^3`, the first nonzero scalar Laplace-Beltrami eigenvalue is

`z_1 = 3/R_k^2 = (lambda_k/3) k^2`.

The frozen threshold equality `z_1=k^2` therefore implies

**`lambda_k=3`**

in the exact radius convention written by the direct source.

This is not a fit: round/de-Sitter spectral geometry was explicitly frozen as a held-out consistency check before data extraction.

The direct source treats the Gaussian regime with `lambda_k << 1` and warns that most Einstein-Hilbert FRG beta functions become singular at `lambda=1/2`. The frozen foliated fluctuation authority likewise has a `lambda=1/2` singular locus delimiting the connected physically interesting region. Thus the canonical gap-at-cutoff hypothesis forces the reduced self-consistent geometry onto the wrong branch/domain.

Even replacing the source's stated radius convention by the standard Einstein relation `R^2=3/Lambda` would only weaken the forced value from `lambda=3` to `lambda=1`; it would not rescue the hypothesis into the `lambda<=1/2` connected flow region.

## Why matched numerical data were not consumed

The preregistration allowed an analytic held-out consistency test. Once `H_gap` failed that test, consuming CDT target tuples to search for an exceptional mode/ensemble would amount to rescue-after-failure and would violate the mode/domain controls.

Matched `(ell_1,Gamma,omega,N_4)` data remain useful for a new hypothesis, but not for repairing ITER086.

## What survives

- ITER084: `z_CDT=9 lambda_graph/a^2` remains qualified at finite regulator.
- ITER085: `z_CDT/k^2` remains a valid background-spatial regulator-probe variable.
- The production covariant support envelope remains valid.
- A relation between the first spatial gap and the FRG scale is not ruled out in general.

What is ruled out is the **universal equality** `z_1=k^2` for the canonical lowest nonzero spatial mode of the reduced self-consistent de-Sitter sector.

## Structural lesson

The source-defined semiclassical geometry suggests the correct variable is not a standalone threshold equality but a curvature-dependent ratio:

`z_1/k^2 = F(lambda_k)`,

with the round self-consistent source convention giving

`F(lambda_k)=lambda_k/3`.

This converts the ITER086 failure into a sharper next prediction route rather than reopening mode selection.

## Claim ceiling

No shared RG trajectory, no held-out spectral validation, no shared fixed point, no bridge derivation and no candidate theory follow.

## Highest-information successor

Prospectively test the **self-consistent curvature-gap relation** rather than the cutoff-threshold relation. Combine:

1. the ITER078 self-consistent de-Sitter radius/coupling map,
2. the ITER084 normalized CDT spatial eigenvalue,
3. the measured deformation `omega/omega_0`,
4. the same-ensemble lowest spatial gap,

while keeping the spatial spectral datum held out until the formula is frozen.

The successor should first derive the dimensionless no-`k` consistency relation implied by the reduced map and only then search for matched numerical data.
