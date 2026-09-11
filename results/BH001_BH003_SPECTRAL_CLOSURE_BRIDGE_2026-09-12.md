# BH-001 × BH-003 Spectral-Closure Bridge — Campaign Result

Date: 2026-09-12  
GitHub Actions run: `34654366893`  
Status: `COMPLETED / POSITIVE WITH CLAIM LOCK`

## Question

Does the BH-003 Pauli–Jordan spectral projector select a retained sector that is more nearly closed under the native causal-set retarded propagator than a rank-matched generic subspace?

For the massless 1+1D causal-set realization, use `G_R = C/2` and the frozen BH-003 threshold

`lambda_min_tilde = sqrt(N)/(4*pi)`.

For retained projector `P`, define

`leakage = ||(I-P) G_R P||_F / ||G_R P||_F`

and the BH-001-type two-step return defect

`Delta_seq = ||P G_R (I-P) G_R P||_F / ||P G_R G_R P||_F`.

The control ensemble consists of complex Haar-random rank-matched projectors.

## Campaign

- `N = 256, 512, 768, 1024`;
- four independent sprinkling seeds per size;
- 16 causal-set realizations total;
- 16 random projectors per realization;
- no entropy observable enters the closure metric.

## Result

Across all 16 realizations, the Pauli–Jordan spectral sector was better than every rank-matched random control for both metrics.

Overall:

- random-mean / spectral leakage ratio: **3.1991**;
- random-mean / spectral sequential-defect ratio: **6.7038**;
- spectral leakage percentile-better fraction: **1.000**;
- spectral sequential-defect percentile-better fraction: **1.000**.

By size:

| N | retained fraction | spectral leakage | random leakage | improvement | spectral seq. defect | random seq. defect | improvement |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 256 | 0.2363 | 0.2785 | 0.8735 | 3.14x | 0.1205 | 0.7716 | 6.42x |
| 512 | 0.1699 | 0.2855 | 0.9117 | 3.19x | 0.1244 | 0.8306 | 6.68x |
| 768 | 0.1393 | 0.2869 | 0.9292 | 3.24x | 0.1251 | 0.8644 | 6.92x |
| 1024 | 0.1235 | 0.2904 | 0.9371 | 3.23x | 0.1299 | 0.8813 | 6.79x |

The effect is stable while the retained fraction falls from about 24% to 12%.

## Interpretation

This is evidence for a concrete connection between the abstract BH-001 leakage obstruction and BH-003 spectral coarse graining:

- the entropy-relevant spectral truncation is not merely a random dimensionality reduction;
- it selects a sector with substantially suppressed one-step leakage under `G_R`;
- more importantly for BH-001, the discarded sector contributes much less to two-step return into the retained sector.

Thus the exact BH-001 obstruction structure

`P G_R (I-P) G_R P`

is numerically suppressed by the same spectral sector used in BH-003.

## What this does NOT establish

- It does not prove that the source cutoff is dynamically selected.
- It does not prove continuum quantum gravity.
- It does not establish a recurrent cross-school motif, because only one realization has passed the test.
- It does not show exact closure: leakage and return defect remain nonzero.

## Promotion gate

Promote this structure toward a recurrent motif only if an independent realization exhibits the same nontrivial pattern:

1. a physically motivated retained sector;
2. suppressed `Q Phi P` leakage relative to rank-matched controls;
3. suppressed `P Phi Q Phi P` return defect;
4. stability under scale/refinement change;
5. no construction of the retained sector using the target closure metric itself.

Until then: `CROSS_HYPOTHESIS_BRIDGE_EVIDENCE`, not `RM-001`.
