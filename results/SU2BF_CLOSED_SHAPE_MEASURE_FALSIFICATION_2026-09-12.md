# SU(2) BF Closure-Preserving Shape-Deformation Falsification

Date: 2026-09-12  
GitHub Actions run: `34657552304`  
Status: `UNIVERSAL BH-001 CLOSURE MOTIF FALSIFIED IN SU2 BF / LOW-SPIN RETURN EFFECT ONLY`

## Stronger holdout

This campaign removes the possibility that the previous measure-corrected result was caused only by permutation/recoupling structure. Instead of permuting the regular-tetrahedron normals, the three contracted coherent boundary states use continuously different sets of equal-area unit normals with exact closure `sum_a n_a = 0`.

The source-native SU(2) BF partial-coherent vertex is retained, including the physical bulk-intertwiner edge measure through the canonical basis

`A_tilde = sqrt(D) A sqrt(D)`, `D_ii = 2 i + 1`.

The retained sector is frozen from the regular equilateral training vertex. The campaign spans

- spins `j = 1, 3/2, 2, 5/2`;
- four closure-preserving coherent shapes;
- all 12 ordered heterogeneous shape pairs;
- 96 Haar-random rank-matched controls per job;
- 48 jobs total.

Primary robust metrics are percentiles: the fraction of random sectors producing a worse leakage or discarded-sector return defect than the frozen train sector.

## Overall result

Across all 48 jobs:

- mean fraction random worse on one-step leakage: **0.00846**;
- median fraction random worse on one-step leakage: **0.00000**;
- mean fraction random worse on heterogeneous return: **0.36089**;
- median fraction random worse on heterogeneous return: **0.19792**;
- mean relative difference between the two held-out operators: **0.91036**.

Thus the train-defined sector is generically **worse**, not better, than Haar-random sectors at one-step closure, and it is not generically protected against two-step return either.

## Spin dependence

Fraction of random controls with worse heterogeneous return, averaged over all ordered shape pairs:

| spin | random worse return | random worse leakage |
|---:|---:|---:|
| `j=1` | **86.46%** | 0.00% |
| `j=3/2` | **16.49%** | 0.26% |
| `j=2` | **36.46%** | 0.26% |
| `j=5/2` | **4.95%** | 2.86% |

The previously observed strong return suppression is therefore a **low-spin phenomenon** in this realization. It does not grow toward the larger spins tested here and is already reversed at `j=3/2` and strongly absent at `j=5/2`.

## Pair dependence

No ordered continuous-shape pair remains robustly protected when averaged over all four spins. Mean fractions of random sectors worse on return range only from roughly 0.297 to 0.487 across the twelve ordered pairs. The large directional asymmetries seen in the earlier permutation campaign therefore do not generalize across continuous closure-preserving shape deformations.

## Scientific conclusion

The broad BH-001 statement

> a physically meaningful retained sector generically suppresses `P A2 Q A1 P` relative to random rank-matched sectors

is **falsified in source-native, edge-measure-corrected SU(2) BF** once the test is extended beyond special permutation holdouts and beyond the smallest spin.

A narrower observation survives:

> at very low spin and small intertwiner dimension, certain train-defined sectors can strongly suppress two-step discarded-sector return even while exhibiting large one-step leakage.

That is interesting as a possible finite-dimensional quantum-geometric effect, but it is not evidence for a universal coarse-graining law and should not be used as a design principle for a quantum-gravity model without independent support.

## Program consequence

ISQGR should **downgrade BH-001 from candidate recurrent universal motif** to `LOW-SPIN / MODEL-SPECIFIC EFFECT UNDER AUDIT`.

The decisive next discriminator is Lorentzian EPRL quantum gravity, where source-native full vertex tensors and coherent intertwiner states are now computationally available. If an analogous effect survives there across spin and boundary deformations, it can be reconsidered. If not, BH-001 should be retired as a general inter-school bridge.

## Claim lock

This result concerns SU(2) BF theory, not Lorentzian EPRL gravity. The coherent shape family enforces unit normals and closure but is not asserted to span all Regge-geometric boundary data. The conclusion falsifies only the tested universal closure interpretation; it does not falsify the existence of special protected channels in other theories or regimes.
