# SU(2) BF Heterogeneous Composition — BH-001 Cross-Realization Test

Date: 2026-09-12  
GitHub Actions run: `34655775004`  
External source: `sethkasante/su2bf-TNAlgo` at commit `2460cda77b8fe27a4106e98bf39a94fa9059bc92`  
Status: `CANDIDATE RECURRENT CLOSURE/LEAKAGE MOTIF UNDER AUDIT`

## Construction

For equal-spin cases `j = 1, 3/2, 2, 5/2`, the two-valent partial-coherent SU(2) BF vertex is used as a matrix over bulk intertwiner indices.

The retained sector `P` is learned **only** from the equilateral training amplitude using the leading right-singular subspace at approximately half rank. `P` is then frozen.

Three distinct held-out boundary amplitudes are used:

- `swap_one`;
- `cycle_two`;
- `mixed_three`.

For ordered pairs `A1 != A2`, the benchmark evaluates

`Delta_21 = ||P A2 Q A1 P|| / ||P A2 A1 P||`,

and compares the train-defined retained sector against 96 Haar-random rank-matched subspaces per job.

## Holdout heterogeneity

Across 24 jobs the mean relative difference between `A1` and `A2` is **1.42978**. Therefore this is not a repeated identical-operator test.

## Result

Overall:

- random-mean / train-sector first-step leakage: **1.66278x**;
- random-mean / train-sector heterogeneous return defect: **5.70608x**;
- fraction of random sectors worse on leakage: **76.2%**;
- fraction of random sectors worse on heterogeneous return: **83.1%**.

By ordered pair:

| ordered pair | mean `A1/A2` difference | random/train leakage | random/train return | random worse return |
|---|---:|---:|---:|---:|
| `cycle_two -> mixed_three` | 1.2990 | 1.0707x | 2.8007x | 87.2% |
| `mixed_three -> cycle_two` | 1.2990 | 1.0707x | 2.8007x | 87.2% |
| `cycle_two -> swap_one` | 1.4571 | 1.0707x | 1.2651x | 67.4% |
| `mixed_three -> swap_one` | 1.5332 | 1.0707x | 1.2651x | 67.4% |
| `swap_one -> cycle_two` | 1.4571 | 2.8468x | **13.0524x** | **94.5%** |
| `swap_one -> mixed_three` | 1.5332 | 2.8468x | **13.0524x** | **94.5%** |

The strong ordering asymmetry is itself informative: discarded-sector return is sensitive to the sequence of physically different boundary amplitudes, as expected for a genuinely heterogeneous composition channel rather than a scalar goodness-of-fit statistic.

## Cross-realization significance

BH-003 causal-set experiments previously found that a physically motivated Pauli-Jordan spectral sector suppresses the BH-001-type discarded-sector return channel relative to rank-matched random sectors by about 6.70x.

The present source-native SU(2) BF realization independently exhibits the same structural preference under the stronger heterogeneous composition `P A2 Q A1 P`, with an overall random/train return ratio of about 5.71x.

This is sufficient to promote the structural observation from a single-realization curiosity to a **candidate recurrent closure/leakage motif under audit**.

## Important limitation: gluing measure

The present operator-level benchmark composes the partial-vertex matrices in the ordinary Euclidean intertwiner basis. In the full SU(2) BF state sum, bulk intertwiner contractions carry an edge amplitude/measure factor. Therefore the next decisive test is a measure-corrected gluing benchmark in a canonicalized intertwiner basis.

## Claim lock

This result is not a quantum-gravity theory and not an EPRL result. SU(2) BF is topological, the retained sector is SVD-defined rather than independently physical, and the present composition does not yet include the full source-native gluing measure. The result supports only a candidate recurrent structural motif.
