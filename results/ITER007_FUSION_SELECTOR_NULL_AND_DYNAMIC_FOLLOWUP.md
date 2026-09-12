# Iteration 007 — Fusion selector null result and dynamic follow-up

## Frozen result from prior run

Authoritative GitHub Actions run `34674371871` completed successfully with six coupling lanes (`g = 0, 0.25, 0.5, 0.75, 1.0, 1.15`) plus aggregate.

The source-native ribbon-support selector did **not** predict subsequent SVD support better than rank-matched random sector labels. Aggregate values were effectively unity for both SVD channels:

- median SVD1 Jaccard gain over random: ~1.0
- median SVD2 Jaccard gain over random: ~1.0
- fraction of couplings with both mean gains > 1: 0
- `natural_support = false`
- `strong_support = false`

This falsifies the simple BH-004B implementation in which a binary ribbon-observable support mask itself supplies the missing local selector.

## Scope lock

The result is a nearest-framework control in the pinned q-deformed lattice-gauge/TNR implementation. It does **not** falsify all possible source-native selectors, quantum gravity, or BH-004B in a more general dynamical form.

## Follow-up discriminator

The next calculation removes the information-destroying binary-support reduction and tests two stronger questions in parallel:

1. **Continuous amplitude predictivity** — do the full normalized ribbon-sector amplitudes/rankings predict the two SVD spectra beyond sector-label permutation nulls?
2. **Cross-lag incremental predictivity** — does the combined SVD transport spectrum improve prediction of the next RG-step ribbon observable beyond persistence alone and permuted-SVD controls?

No fit coefficient is introduced in the cross-lag test: the SVD augmentation weight is frozen at 1/2 before evaluation.

The new workflow is `ISQGR Fusion Dynamic Predictivity Audit`, with 12 lanes (2 tests × 6 couplings). Claim scope remains restricted to selector/transport architecture inside this nearest-framework control.
