# ITER009 — RC006 Eq.(24)/Eq.(15) TNR object authority gate

Date: 2026-09-13

## Frozen authority
- preregistration commit: `c25d7bdb1d03363c197e0897d2f7ed650ee68948`
- implementation commit: `37b5ab307cc717f6de2e346033f1cf9cd46314a6`
- production head: `481d58b12a2bbfb46c94facbc898075a09fde2f4`
- workflow run: `34764164219`
- jobs: A `103742061070`, B `103742061168`, C `103742061116`, D `103742060943`, aggregate `103742124048`
- artifacts: A `10319549182`, B `10319514343`, C `10319288687`, D `10319209220`, summary `10319414674`
- summary digest: `sha256:5893d3b30722386900f91ffa3b7ecddeda325d100e32c25cd7c1b740d8ec8317`

## Raw-artifact classification
All four raw lane artifacts and the aggregate were consumed, not inferred from green CI.

- A PASS: source object contains Eq.(24) four-valent EPRL spin-net tensor, paired `j^±`, Haar/projector structure and Eq.(15) block/recoupling structure; `uses_eq29=false`, `uses_formlamb6j=false`.
- B PASS: exact finite-k support census reproduced all four frozen source-highlighted maps for `(k,gamma)=(6,1/3),(10,3/5),(12,1/3)`.
- C PASS: source-defined support/block contraction topology remained consistent under the frozen relabelling test; `support_size=5`, `contracted_pairs=5`, `permuted_pairs=5`. Scope is topology/support only.
- D PASS: nonzero normalization choices preserve support while changing amplitude magnitudes; post-hoc fitting remains forbidden.
- Aggregate: `pass=true`, lane_count=4.

## Scientific classification
`RC006_EQ24_TNR_OBJECT_SOURCE_PINNED_NORMALIZATION_FAMILY_OPEN_SCOPED`

This closes source-object authority for the reduced Euclidean `SU(2)_k x SU(2)_k` EPRL spin-net/TNR object only. It gives zero amplitude/refinement bridge credit, does not establish numerical EPRL/FK amplitudes, does not authorize Eq.(29)/general `formlamb6j`, does not derive genuine multivertex Lorentzian refinement, and does not authorize candidate-theory construction.

## New source-backed refinement of the blocker
A subsequent primary-source audit of arXiv:1609.02429v2 shows that the normalization ambiguity is more structured than an arbitrary nonzero `c_l`: Appendix E Eq.(68) derives

`c_{ {l} } = (-1)^(sum_i(j_i^+ + j_i^-) - 2l) * d_{l1} d_{l2} d_{l3} d_{l4} d_l^2`

from the projector condition, and the authors explicitly generalize the external-dimension product to a one-parameter power `alpha`, keeping the sign and `d_l^2` factor. The main text states that this measure parameter can materially affect coarse-graining flow. This source structure authorizes a separate prospective normalization-family gate; it does not by itself provide bridge credit.
