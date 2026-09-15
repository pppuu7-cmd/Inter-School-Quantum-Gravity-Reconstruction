# ITER144 preregistration — cubic graviton S3 source-structure authority

Date: 2026-09-15
Gate: `ITER144_CUBIC_GRAVITON_S3_SOURCE_STRUCTURE_AUTHORITY`
Status: **FROZEN BEFORE PRODUCTION SOURCE DOWNLOAD / PANEL COMPARISON**

## Motivation

The interaction-dressed M row `M_R1_chi1_dR1_S3` remains on the conservative ITER139 global `N1<=5` bound because this repository has no source-qualified cubic graviton action vertex `S3`. Reconstructing S3 from memory is forbidden. This gate establishes a pinned external machine source and independently checks its three-graviton tensor structure before any M3 numerator is attempted.

This gate is independent of ITER140/143 and may run in parallel.

## Frozen external authority stack

Primary machine source:

- repository: `BorisNLatosh/FeynGrav`;
- pinned commit/tree head observed for this gate: `91f697a1ca62fd051cbb297827cb1a491b393538`;
- file: `Libs/GravitonVertex_1`;
- pinned Git blob SHA: `98297aac3b640a93ac80c2cc72a8275280819954`.

Published convention/source context:

- David Prinz, *Gravity-Matter Feynman Rules for any Valence*, arXiv:2004.09543: metric split `g_{mu nu}=eta_{mu nu}+kappa h_{mu nu}` and linearized de Donder gauge fixing;
- David Prinz, *Transversality in the Coupling of Gravity to Gauge Theories*, arXiv:2208.14166: explicit propagators/three-valent vertices and de Donder transversality identities.

FeynGrav package documentation at the pinned tree states that `GaugeFixingEpsilon` controls the graviton propagator and does not enter `GravitonVertex`. Therefore this gate treats `GravitonVertex_1` as a cubic pure-gravity vertex source, not as evidence for the propagator normalization used by ISQGR.

## Frozen source-integrity checks

The workflow must download the raw file from the pinned commit and verify its Git blob SHA by the exact Git blob rule (`sha1("blob <len>\0" + bytes)`). No moving `main` content is accepted as authority.

The parser may consume only the syntax actually expected in the pinned library:

- rational/integer coefficients;
- products/sums;
- `I`, `\[Kappa]`;
- `Pair[LorentzIndex[... , D],LorentzIndex[... , D]]`;
- `Pair[LorentzIndex[... , D],Momentum[p_i,D]]` and reversed order;
- `Pair[Momentum[p_i,D],Momentum[p_j,D]]`.

Unexpected syntax is a block, not permission to silently drop a term.

## Frozen structural predicates

After stripping the common `I*kappa` factor, the source vertex must:

1. involve exactly three symmetric graviton legs `(m1,n1,p1)`, `(m2,n2,p2)`, `(m3,n3,p3)`;
2. be homogeneous of total momentum degree 2;
3. be exactly symmetric under all six permutations of the three graviton legs on deterministic held-out component/momentum panels satisfying `p1+p2+p3=0`;
4. remain symmetric under `m_i<->n_i` for each leg;
5. contain no target quantity, geodesic weight, EDT datum or desired cancellation.

## Frozen independent Einstein-Hilbert comparison

Independently construct the cubic coefficient of the pure Einstein-Hilbert action from the Gamma-Gamma representation of `sqrt(g) R`, using

`g = eta + kappa h`,

with three plane-wave perturbations `u A exp(i p1.x) + v B exp(i p2.x) + w C exp(i p3.x)` and `p1+p2+p3=0`.

The independent implementation must not call or algebraically rewrite the FeynGrav source expression. It expands:

- `sqrt(det g)` and `g^{-1}` to the order needed;
- `Gamma1` and `Gamma2` from the metric expansion;
- the Gamma-Gamma Einstein-Hilbert density through the cubic `u v w` coefficient.

Comparison panels are restricted to purely spatial momenta and spatial polarization indices embedded in D=4. Every contraction then contains an even total number of Minkowski metric pairings, so the component comparison is insensitive to mostly-plus versus mostly-minus spatial metric sign. Momentum-conservation also removes total-derivative ambiguity between R and Gamma-Gamma action forms.

The source Feynman vertex and the independently derived cubic action tensor may differ by one **single panel-independent global normalization/phase factor** due to action/Feynman-rule and Euclidean/Lorentz conventions. This gate does not infer that factor from one panel and then call the sign physical. Instead:

- determine the exact ratio on the first nonzero panel;
- require the same nonzero ratio on every other nonzero held-out panel;
- require the ratio to be independent of leg permutation;
- record the ratio explicitly;
- do not use it for a physical B1 sign until a later convention gate fixes Euclidean action/propagator normalization jointly.

## Frozen classifications

- Source hash, parser, degree, leg/index symmetries and all independent EH panel ratios pass with one constant nonzero global factor:
  `PASS_SCOPED_CUBIC_GRAVITON_S3_TENSOR_STRUCTURE_SOURCE_AUTHORITY_GLOBAL_PHASE_OPEN`.
- Source integrity/parser syntax fails before tensor evaluation:
  `BLOCKED_CUBIC_GRAVITON_SOURCE_INTEGRITY_OR_SYNTAX`.
- Tensor symmetry or independent EH ratio is not constant:
  `SCIENTIFIC_FAIL_CUBIC_GRAVITON_S3_SOURCE_STRUCTURE_MISMATCH`.
- Infrastructure failure before predicates are evaluated:
  `NUMERICAL_OR_INFRASTRUCTURE_FAIL`.

## Claim ceiling

A PASS authorizes the cubic-graviton **tensor structure** as an S3 input for derivative allocation and later convention work. It does not yet authorize the absolute Euclidean phase/sign/normalization for a physical pole coefficient, and it is not a loop residue, B1, noncancellation result, EDT comparison, bridge, new physics or candidate theory. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
