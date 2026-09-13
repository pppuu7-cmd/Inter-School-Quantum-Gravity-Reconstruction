# ITER010 — RC006 EPRL alpha measure-family gate

Date: 2026-09-13

## Frozen authority
- preregistration commit: `83159579a483ecc9801f858cb2f610c39f641d6d`
- implementation commit: `c8fbe7be0086a5cbbd2361704c01da7b1fb64a10`
- production head: `084d3ef667d6bded4b8130bfed1c361617246c3c`
- workflow run: `34767152769`
- jobs: A `103750049785`, B `103750049747`, C `103750049869`, D `103750049813`, aggregate `103750075740`
- artifacts: A `10320538483`, B `10320628648`, C `10320937900`, D `10320417582`, summary `10320433718`
- summary digest: `sha256:4937cbd7ac929c38060cb30a55c50ff49152fa3ebfb5e84a2b058a2e8fb303c3`

## Raw-artifact results
All raw lane artifacts and the frozen aggregate were consumed.

- A PASS: tested phase exponents are integral; q-dimensions are positive; alpha=1 recovers the frozen Eq.(68) normalization member; omission of the internal `d_l^2` factor is rejected.
- B PASS: support is unchanged across source-motivated alpha values `-1, 0.35, 2`, while nontrivial normalized magnitude ratios change strongly. Example second ratio: `0.00245179 -> 8.19749 -> 166353.91`.
- C PASS: endpoint q-dimension-one configurations are alpha-insensitive, mixed configurations are alpha-sensitive, and replacing q-dimensions by classical dimensions is rejected (`qprod≈20.19567` versus classical product `637`).
- D PASS: external-leg permutations preserve the quantum-dimension product; held-out alpha values `-0.5,0,0.5,1.5` reproduce the analytic log-slope `4.015970175364951` to the frozen tolerance; wrong-sign slope control is rejected.
- Aggregate: `pass=true`, lane_count=4.

## Scientific classification
`RC006_EPRL_ALPHA_MEASURE_FAMILY_SOURCE_RECONSTRUCTED_SCOPED`

The source-derived normalization ambiguity is now pinned to the explicit one-parameter alpha family used in arXiv:1609.02429v2 rather than an arbitrary nonzero normalization function. Alpha is a model-family/measure parameter and materially reweights nontrivial representation sectors, but no preferred alpha is selected.

This result gives ZERO amplitude/refinement bridge credit. It does not reproduce a full one-step EPRL TNR flow, does not authorize Eq.(29)/general `formlamb6j`, does not supply missing q-CG/recoupling amplitudes, and does not authorize candidate-theory construction.

## Next admissible gate
Source-audit the complete numerical 3-valent EPRL tensor/amplitude formula used for the triangular coarse-graining step (main-text Eq.(27) and Appendix F), and determine prospectively whether all q-CG/recoupling ingredients and conventions are explicitly reconstructible without importing the independently blocked Eq.(29)/Lambda convention. If any required convention lacks a primary-source authority chain, classify that path BLOCKED rather than fitting it.
