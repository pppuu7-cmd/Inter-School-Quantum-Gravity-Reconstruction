# ITER010 — RC006 source-derived EPRL normalization/measure family gate

Date: 2026-09-13

## Frozen purpose
Test the source-derived normalization family of the already-qualified reduced Euclidean `SU(2)_k x SU(2)_k` EPRL spin-net object without using Eq.(29), general `formlamb6j`, fitted q-CG data, or any post-hoc measure choice.

Primary source frozen before implementation: Dittrich, Schnetter, Seth, Steinhaus, arXiv:1609.02429v2 / Phys. Rev. D 94, 124050 (2016), main EPRL construction plus Appendix E Eq.(65)-Eq.(68). Appendix E derives the projector normalization and then explicitly introduces a one-parameter power `alpha` in the product of external quantum dimensions. The source also reports EPRL-intertwiner flows for `k=12, gamma=1/3` at alpha values including `-1`, `0.35`, and `2`.

## Frozen mathematical object
For admissible EPRL labels use source q-dimension
`d_j = sin(pi*(2j+1)/(k+2))/sin(pi/(k+2))`.
For a four-leg external tuple and internal recoupling label `l`, define only the source normalization factor
`c_alpha = (-1)^N * (prod_i d_{l_i})^alpha * d_l^2`,
where `N = sum_i(j_i^+ + j_i^-) - 2l` must be integral for each tested admissible configuration. No claim is made about the remaining q-CG/recoupling amplitude.

## Frozen streams
A — Eq.(68) reconstruction: for exact rational admissible labels at `k=12, gamma=1/3`, verify integrality of the phase exponent on the tested recoupling-support configurations, positivity/reality of q-dimensions, and exact recovery of the projector-family member at `alpha=1` relative to the Eq.(68) form. Wrong omission of `d_l^2` is a negative control.

B — alpha sensitivity: on prospectively fixed nontrivial external tuples drawn from source-allowed `l in {0,3/2,3,9/2,6}`, compare normalized magnitude ratios for `alpha=-1, 0.35, 2`. Require support to remain identical while at least one nontrivial ratio changes across alpha. No alpha is selected as physically preferred.

C — endpoint/null calibration: configurations using only q-dimension-one endpoint labels must be alpha-insensitive; mixed/non-endpoint configurations must show alpha dependence when their external q-dimension product differs from 1. Deliberately replacing q-dimensions with classical dimensions is a false-source control and must disagree for at least one nontrivial configuration.

D — held-out transport of the normalization law: evaluate frozen held-out alpha values `{-0.5,0,0.5,1.5}` and leg permutations. Require permutation invariance of `prod_i d_{l_i}` and consistent analytic log-slope `d log|c_alpha|/d alpha = log(prod_i d_{l_i})` to numerical tolerance `1e-12`. Wrong-sign slope is a negative control.

## Frozen classification
PASS only if A-D all pass their frozen predicates. Terminal label:
`RC006_EPRL_ALPHA_MEASURE_FAMILY_SOURCE_RECONSTRUCTED_SCOPED`.

A PASS authorizes only later source-faithful amplitude/TNR work that treats alpha prospectively as a declared model-family parameter. It gives ZERO bridge credit, does not choose a preferred alpha, does not reproduce a full one-step TNR flow, does not authorize Eq.(29)/general `formlamb6j`, and does not authorize candidate-theory construction.

Scientific predicate failure is SCIENTIFIC FAIL. Technical execution failure is INFRASTRUCTURE/NUMERICAL FAIL and may be minimally repaired without changing this preregistration.
