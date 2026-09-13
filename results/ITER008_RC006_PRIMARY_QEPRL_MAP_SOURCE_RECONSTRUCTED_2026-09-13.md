# ITER008 RC006 PRIMARY q-EPRL MAP — TERMINAL RESULT

Date: 2026-09-13

Classification: **RC006_PRIMARY_QEPRL_MAP_SOURCE_RECONSTRUCTED_SCOPED**

## Frozen authority chain
- preregistration: `2629980547ef2a263f5ddc3fd9e95c13c03a55a4`
- implementation: `48056fa668596da7b5414db44f6f72d8907f1b33`
- production head: `758dcb3244d90df10855f51c86f427bde54abe6d`
- run: `34758409423`
- jobs: A `103726740071`, B `103726740079`, C `103726739955`, D `103726740114`, aggregate `103726775902`
- artifacts: A `10317148912`, B `10318360651`, C `10318166407`, D `10318535336`, summary `10317543609`
- summary digest: `sha256:d7cf0f724edafb4976d2e87ce10637932b969c6cc58101f9bfd81987f67bfe11`

## Scientific result
All four prospectively frozen streams pass.

A: complex-q and sine q-number conventions agree to max absolute error `2.4197926948559723e-15`; root-of-unity zero and positivity controls pass.

B: the printed source controls reproduce exactly: `k=6,gamma=1/3,l=3 -> (2,1)`; `k=10,gamma=3/5,l=5 -> (4,1)`; `k=12,gamma=1/3,l=3 -> (2,1)` and `l=6 -> (4,2)`.

C: all frozen perturbed-gamma endpoint controls fail admissibility as required; deliberately wrong q convention mismatch fraction is `1.0`.

D: independent 50-digit evaluation agrees with the double-precision expression to max relative discrepancy `1.3322676295501878e-15`; q-number reflection symmetry max error is `2.220446049250313e-15`.

## Scope
This establishes only a source-faithful reconstruction of the reduced Euclidean `SU(2)_k x SU(2)_k` q-EPRL representation map and q-number/quantum-dimension convention used by the audited source. It carries **zero bridge credit by itself**.

It does **not** resolve the separate Lambda/q-binomial provenance blocker, does not authorize Eq.(29)/general `formlamb6j`, does not establish a Lorentzian amplitude, genuine multivertex refinement map, or `BRIDGE_DERIVED`, and does not authorize candidate-theory construction.

## Next admissible gate
A further RC006 computation is admissible only after pinning a source-explicit amplitude/TNR object that uses this reconstructed q-EPRL map without importing the blocked Lambda convention. Once such an object is pinned prospectively, its normalization, contraction/refinement rule, controls, and interpretation must be frozen before implementation. Until then, denser map tests are saturated and should not be repeated.
