# Independent SU(2) BF Holdout Closure — Cross-Realization Evidence

Date: 2026-09-12  
Source-native GitHub Actions run: `34655296947`  
External source: `sethkasante/su2bf-TNAlgo` at commit `2460cda77b8fe27a4106e98bf39a94fa9059bc92`  
Status: `POSITIVE CROSS-REALIZATION EVIDENCE / NOT RM PROMOTION`

## Construction

The external implementation's `partial_cohn_vertex2` returns a two-valent partial coherent vertex as a matrix over bulk intertwiner labels.  We use this matrix as an independent spin-foam/BF operator.

For each equal-spin case `j = 1, 3/2, 2, 5/2`:

1. construct the equilateral train vertex `A_train` from the source boundary normals;
2. define a retained subspace from the top right-singular vectors of `A_train`, with rank approximately half of the intertwiner space;
3. **freeze this subspace**;
4. construct holdout vertices from nontrivial permutations of tetrahedral boundary normals;
5. evaluate holdout leakage and return defect using the train-defined subspace;
6. compare with 64 Haar-random rank-matched subspaces.

Metrics:

`leakage = ||Q A_test P|| / ||A_test P||`,

`Delta_seq = ||P A_test Q A_test P|| / ||P A_test A_test P||`.

The target metrics never enter the SVD-sector construction.

## Holdout validity

The holdout matrices are not numerically identical to the training vertex.

Mean relative train/test differences:

- `cycle_two`: **0.8905**;
- `swap_one`: **1.2861**;
- `mixed_three`: **1.3222**;
- overall: **1.1663**.

Thus the result cannot be dismissed as a trivial identical-operator symmetry test.

## Result

Across 12 source-native holdout jobs:

- random-mean / train-sector leakage: **1.6774x**;
- random-mean / train-sector sequential return defect: **2.8323x**;
- fraction of random sectors worse on leakage: **0.7357**;
- fraction of random sectors worse on return defect: **0.8984**.

By holdout family:

| holdout | random/spectral leakage | random/spectral seq. defect | random worse leakage | random worse seq. |
|---|---:|---:|---:|---:|
| `swap_one` | 2.8910x | 2.8323x | 94.1% | 89.8% |
| `cycle_two` | 1.0705x | 2.8323x | 63.3% | 89.8% |
| `mixed_three` | 1.0705x | 2.8323x | 63.3% | 89.8% |

The strongest and most stable signal is the BH-001-type discarded-sector **return defect**, not one-step leakage.

## Cross-realization significance

Causal-set BH-003 previously showed that its physically motivated Pauli–Jordan spectral sector suppresses

`P G_R Q G_R P`

relative to rank-matched random sectors by about **6.70x**.

This independent SU(2) BF realization now shows the same structural preference in a source-native partial-vertex operator: a nonrandom retained sector learned from one physical boundary realization suppresses discarded-sector return on held-out boundary data.

This is the first non-causal-set realization in ISQGR to pass a quantitative leakage/return benchmark.

## Claim lock

This is **not yet RM-001** because:

1. SU(2) BF is topological and is not EPRL quantum gravity;
2. the retained sector here is learned by SVD from the train amplitude rather than fixed by an independently sourced physical coarse-graining prescription;
3. the current sequential test uses the same holdout operator twice, `P A Q A P`, rather than heterogeneous composition `P A2 Q A1 P`;
4. leakage superiority is weaker for two holdout families even though return-defect superiority remains strong.

## Promotion gate

The next decisive independent test is heterogeneous held-out composition:

`Delta_12 = ||P A2 Q A1 P|| / ||P A2 A1 P||`,

where `P` is frozen from the equilateral train vertex and `A1 != A2` are two distinct holdout boundary amplitudes.  A robust advantage over Haar controls across spin and holdout orderings would justify labeling the structure a **candidate recurrent closure/leakage motif under audit**, while still not constituting a quantum-gravity theory.
