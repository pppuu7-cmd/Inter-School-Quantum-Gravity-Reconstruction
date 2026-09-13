# ITER009 — RC006 Eq.(24)/Eq.(15) source-explicit q-EPRL tensor/TNR object authority gate

Date: 2026-09-13

## Frozen purpose
Determine whether the already-qualified reduced Euclidean SU(2)_k x SU(2)_k q-EPRL representation map can be embedded into an explicitly source-defined initial tensor/coarse-graining object without using the independently blocked Lambda/q-binomial Eq.(29) convention.

Primary source frozen before implementation: Dittrich, Schnetter, Seth, Steinhaus, arXiv:1609.02429v2 / Phys. Rev. D 94, 124050 (2016). The source explicitly states the tensor-network partition-function/coarse-graining form, recoupling/block tensor Eq.(15), and the EPRL spin-net initial tensor Eq.(24), with j_i^±=(1±gamma)l_i/2 and normalization c_{l}. Eq.(29) is OUT OF SCOPE and may not be used.

## Frozen streams
A — source-object structure: verify that the reconstructed object uses four-valent EPRL spin-net tensor Eq.(24), paired q-EPRL labels j_i^±, Haar/projector contraction structure, and block/recoupling representation Eq.(15). Reject any object requiring Eq.(29)/formlamb6j.

B — exact representation-support census for the published finite-k examples k=6,gamma=1/3; k=10,gamma=3/5; k=12,gamma=1/3. Enumerate all l in [0,k/2] on the half-integer lattice for which j^± are admissible half-integers in [0,k/2]. Frozen controls: reproduce source-highlighted nonzero maps l=3 -> (2,1) at k=6; l=5 -> (4,1) at k=10; l=3 -> (2,1) and l=6 -> (4,2) at k=12. Perturbed wrong maps must reject.

C — source-defined TNR contraction topology: construct an abstract four-leg tensor support object and verify that pairwise tensor contraction followed by regrouping is permutation-consistent at the support/block-label level, with no use of numerical q-CG amplitudes or blocked q-binomial conventions. This is topology/support only, not an amplitude value.

D — normalization-family audit: keep c_{l} symbolic. Determine which support/topology statements are invariant under arbitrary nonzero c_{l} and explicitly mark amplitude magnitudes/flows as NOT uniquely reconstructible until a source-fixed normalization choice (or prospectively declared member of the source-allowed family) is selected. Negative control: setting c_l by post-hoc fitting is forbidden.

## Frozen classification
PASS only if A-D all satisfy their frozen predicates. Terminal label:
`RC006_EQ24_TNR_OBJECT_SOURCE_PINNED_NORMALIZATION_FAMILY_OPEN_SCOPED`.

This PASS gives source-object authority and authorizes only a subsequent prospectively preregistered normalization-family / one-step support-level transport audit. It gives ZERO amplitude/refinement bridge credit, does NOT establish a numerical EPRL/FK amplitude, does NOT authorize Eq.(29), does NOT derive a genuine multivertex refinement map, and does NOT authorize candidate-theory construction.

If Eq.(24)/Eq.(15) cannot be represented without importing Eq.(29), classify SCIENTIFIC FAIL. If source leaves c_l free, that is an expected scoped blocker for unique amplitude magnitude, not a failure of source-object pinning. Technical execution failures are INFRASTRUCTURE/NUMERICAL FAIL and may be minimally repaired without changing these criteria.
