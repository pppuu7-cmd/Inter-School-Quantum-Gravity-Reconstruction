# ITER006 — Lorentzian B4 one-zero-spin primitive gate

Authoritative GitHub Actions run: `34711008648` (commit `b60cc12ac2927404d9d76a50be1fdd3f533c36a3`).

Frozen matrix: gamma = 0.5, 1.2, 2.0; four one-zero-spin configurations per gamma.

Terminal aggregate: `B4_ZERO_SPIN_PRIMITIVE_AGGREGATE_PASS`.

- gamma 0.5: 4 comparisons, max relative error `2.03838e-16`.
- gamma 1.2: 4 comparisons, max relative error `1.93487e-16`.
- gamma 2.0: 4 comparisons, max relative error `1.65249e-16`.

Interpretation: the pinned `sl2cfoam-next` B4 numerical primitive is capable of evaluating the required one-zero-spin sectors at machine-precision consistency. This removes the zero-spin *kernel capability* blocker for a future strict foam-embedding test.

Claim lock: this does **not** establish a trivial-extension amplitude identity, cylindrical consistency, a refinement bridge, continuum physics, or new physics. The next Lorentzian step must first pin a source-faithful coarse→fine foam incidence/label map, then compare amplitudes under that exact embedding.
