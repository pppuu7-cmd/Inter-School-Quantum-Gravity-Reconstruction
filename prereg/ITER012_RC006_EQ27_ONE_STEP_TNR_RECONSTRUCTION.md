# Iter012 — RC006 smallest source-faithful Eq.(27)/Appendix-F one-step TNR reconstruction

Date: 2026-09-13

## Scope
Prospective gate opened only after Iter011 terminal authority-chain PASS. This gate tests the smallest numerically explicit reduced Euclidean SU(2)_k x SU(2)_k EPRL/FK one-step reconstruction that can be implemented from the source-defined Eq.(27)+Appendices A/B/F conventions. It is implementation/transport validation only: no bridge credit, no preferred measure claim, no Lorentzian refinement claim.

## Frozen inputs
- Primary source: arXiv:1609.02429v2.
- k panel: k = 6, 10, 12.
- measure exponent: alpha = 0, fixed prospectively before production. This is a test point, not a preferred value.
- EPRL map and admissibility are exactly those qualified in Iter008/Iter010/Iter011.
- Eq.(29), Lambda/formLambda6j and any fitted normalization are forbidden.

## Independent lanes
A. Finite-k source support/weight lane: enumerate admissible reduced EPRL labels, source q-dimensions and alpha=0 measure weights; require finite values, exact support consistency and permutation invariance.

B. q-CG numerical-convention lane: instantiate only Appendix-A/B source-authorized q-CG/duality conventions and validate orthogonality/normalization on the frozen low-spin panel. If the repository implementation cannot instantiate an explicitly source-authorized ingredient, return BLOCKED rather than substitute a classical CG, fitted phase, or guessed convention.

C. One-step contraction lane: construct the smallest nontrivial Eq.(27)/Appendix-F tensor block permitted by B and perform one contraction/coarse-graining update without truncation tuning. Require finite output, deterministic repeatability, and agreement under two algebraically equivalent contraction orders to <= 1e-11 relative error. If B is unavailable, classify BLOCKED.

D. Held-out/negative-controls lane: k=10 held-out permutation/order checks; intentionally replace q-dimension by classical 2j+1 and/or q↔qbar orientation where applicable. Controls must be detected as non-equivalent whenever the qualified source formula predicts a distinction. No retuning after viewing outputs.

## Frozen aggregate interpretation
- SCIENTIFIC PASS only if A/B/C/D all satisfy their frozen predicates: `RC006_EQ27_ONE_STEP_TNR_RECONSTRUCTION_VALIDATED_SCOPED`.
- BLOCKED if a required source-faithful numerical ingredient cannot be instantiated without an unauthorized convention: `RC006_EQ27_ONE_STEP_TNR_RECONSTRUCTION_BLOCKED_SOURCE_IMPLEMENTATION_GAP`.
- SCIENTIFIC FAIL if all required ingredients are instantiated but a frozen scientific predicate fails.
- INFRASTRUCTURE/NUMERICAL FAIL only for execution/environment failures before scientific predicates can be evaluated.

## Claim locks
Even PASS gives zero bridge credit by itself. It does not authorize Eq.(29)/Lambda, a preferred alpha, genuine multivertex Lorentzian refinement, BRIDGE_DERIVED, NEW_PHYSICS_FOUND, NEW_QG_THEORY_REQUIRED, candidate action/Hamiltonian/field equations, or candidate-theory construction.
