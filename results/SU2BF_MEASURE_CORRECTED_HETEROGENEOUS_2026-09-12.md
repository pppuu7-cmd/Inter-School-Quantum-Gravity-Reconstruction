# SU(2) BF Measure-Corrected Heterogeneous Composition

Date: 2026-09-12  
GitHub Actions run: `34657173927`  
Status: `UNIVERSAL CLOSURE MOTIF FAILS UNDER EDGE MEASURE / DIRECTIONAL SUBCHANNEL SURVIVES`

## Stronger construction

The earlier operator-level heterogeneous benchmark used ordinary matrix products of two-valent partial-coherent vertices. The full spin-foam state sum carries the bulk-intertwiner edge amplitude

`D_ii = d_i = 2 i + 1`.

To test the physically weighted composition in an ordinary Euclidean numerical basis, each source-native partial vertex is canonicalized as

`A_tilde = sqrt(D) A sqrt(D)`.

Then

`A2_tilde A1_tilde = sqrt(D) A2 D A1 sqrt(D)`,

so the internal contraction contains exactly the physical edge weight. The retained sector is learned from the weighted equilateral train vertex and frozen before holdout evaluation.

The benchmark spans spins `j = 1, 3/2, 2, 5/2` and all six ordered pairs of the three permutation holdouts, with 96 Haar-random rank-matched controls per job.

## Robust result

The arithmetic mean of random/train defect ratios is **not** a reliable summary here because several weighted train-sector defects become numerically near zero and create enormous ratios. The primary robust statistic is therefore the fraction of random sectors with a worse defect.

Across all 24 jobs:

- mean fraction random worse on heterogeneous return: **0.5321**;
- mean fraction random worse on first-step leakage: **0.4054**;
- mean weighted/unweighted train-sector overlap: **0.9262**.

Thus the physically weighted retained sector is **not generically superior** to Haar-random sectors across the full holdout campaign.

## Strong directional asymmetry

By ordered pair, fraction of random sectors worse on heterogeneous return:

| ordered pair | random worse return |
|---|---:|
| `swap_one -> cycle_two` | **95.83%** |
| `swap_one -> mixed_three` | **95.83%** |
| `cycle_two -> mixed_three` | 50.26% |
| `mixed_three -> cycle_two` | 50.26% |
| `cycle_two -> swap_one` | **13.54%** |
| `mixed_three -> swap_one` | **13.54%** |

The edge measure therefore converts the previous broad operator-level preference into a highly directional channel effect.

## Spin dependence

Mean fraction random worse on return:

- `j=1`: **81.25%**;
- `j=3/2`: **49.31%**;
- `j=2`: **45.14%**;
- `j=5/2`: **37.15%**.

The effect does not strengthen toward the larger spins covered by this campaign.

## Scientific consequence

The universal form of the provisional statement

`physical retained sectors generically suppress P A2 Q A1 P`

is **not supported** by the stronger source-measure-corrected SU(2) BF test.

What survives is narrower:

> certain physically weighted transition directions can possess an exceptionally protected retained sector, while the reverse direction can preferentially use discarded degrees of freedom.

This suggests a possible **directed interface / transition-channel motif**, not a universal closure principle.

## Next falsification

Permutation holdouts may contain special recoupling or symmetry structure. The next SU(2) BF campaign therefore replaces permutations by continuously deformed, closure-preserving coherent boundary normal configurations. If the directional effect disappears there, it will be classified as a permutation/recoupling artifact. If it survives, the directed-interface interpretation becomes more plausible.

## Claim lock

This is SU(2) BF, not EPRL quantum gravity. No quantum-gravity theory claim is licensed by this result. The earlier unweighted cross-realization observation remains historically valid, but its universal interpretation is explicitly superseded by this stronger measure-corrected test.
