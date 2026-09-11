# BH-003 Thinning Projector Transfer — Negative Scale-Flow Result

Date: 2026-09-12  
Corrected GitHub Actions run: `34655369681`  
Status: `NEGATIVE FOR SOURCE-EXPONENT DERIVATION / POSITIVE NATIVE FLOW`

## Question

Can the physically useful BH-003 spectral scale be derived without entropy by demanding covariance of retained spectral subspaces under Bernoulli thinning of one causal set?

For a full causal set and its induced thinned subset:

1. diagonalize `iDelta` on the full set;
2. probe fixed retained fractions `0.08, 0.12, 0.18, 0.26, 0.36`;
3. restrict each full-set retained subspace to the surviving elements;
4. QR-orthonormalize the restricted span;
5. match it to the closest nested spectral projector of the thinned `iDelta`;
6. infer

`lambda_thin/lambda_full = (N_thin/N_full)^alpha`.

The source SSEE exponent `1/2` is consulted only after inference.

## Method correction

The first campaign compared the raw restricted Gram operator `A A^†` to an orthoprojector even though restricting eigenvectors destroys orthonormality.  That run was therefore not interpreted physically.

The corrected campaign compares **orthoprojectors onto the restricted spans**, obtained through QR.  Probe fractions, thinning probabilities and the post-hoc `1/2` reference were unchanged.

## Campaign

- `N = 384, 512, 768, 1024`;
- requested thinning probabilities `p = 0.5, 0.7`;
- three seeds per `(N,p)`;
- 24 successful jobs plus aggregate.

## Result

A remarkably stable native scale flow appears, but its exponent is approximately one, not one half.

Overall job-level inferred exponent:

- median `alpha = 1.02547`;
- mean `alpha = 1.03866`;
- standard deviation `0.04034`;
- post-hoc `|median alpha - 1/2| = 0.52547`.

The two independent thinning levels agree closely:

- `p=0.5`: inferred exponent is about `1.03`;
- `p=0.7`: inferred exponent is about `1.02`.

The low retained-fraction probes are especially stable:

- probe `0.08`: median `alpha ≈ 0.981`;
- probe `0.12`: median `alpha ≈ 0.991`;
- probe `0.18`: median `alpha ≈ 1.011`.

Mean normalized projector-transfer error is about **0.417**, so the transfer is informative but not an exact RG covariance.

## Interpretation

Simple Bernoulli-thinning covariance of `iDelta` spectral subspaces naturally detects a nearly linear density scaling,

`lambda_cut ~ N^1`,

rather than the SSEE regulator scaling

`lambda_cut ~ N^(1/2)`.

Therefore the proposition

> "the source SSEE cutoff exponent 1/2 follows from spectral-projector covariance under ordinary Bernoulli thinning"

is rejected for this transfer definition.

This does **not** reject BH-003 or the source-defined regulator.  It shows that ordinary element thinning is not by itself the missing physical regulator-selection principle.  It may represent a different normalization/scale transformation of the discrete Pauli–Jordan operator.

## Required diagnostic before stronger interpretation

The next test must ask a narrower semantic question: does the **already known source-defined spectral sector** itself transfer coherently under Bernoulli thinning?

- if it transfers poorly, Bernoulli thinning is simply the wrong RG/coarse-graining map for this sector;
- if it transfers well while the raw eigenvalue exponent remains near one, the difference is likely tied to normalization/density conventions rather than failure of the retained physical subspace.

No entropy optimization is allowed in that diagnostic.
