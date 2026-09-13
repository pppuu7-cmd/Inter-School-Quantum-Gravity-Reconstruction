# ITER026 prereg — RC006 direct-source qbar identity execution

Date: 2026-09-14

Frozen before ITER026 implementation or result inspection.

## Motivation

`ITER025A` (logical alias for `prereg/ITER025_RC006_SOURCE_NORMALIZED_QBAR_SIGN_2026-09-14.md`) terminalized `RC006_QBAR_CUP_INDEPENDENT_FAIL`: its inverse-parameter/reversed-order qbar highest-weight construction passed its construction and 4-valent lanes but failed independent cup and held-out cup panels, including high/root-boundary spins.

`ITER025B` subsequently source-qualified an explicit ordered q↔qbar component identity from exact `1312.0905v2` and source-stated map order, plus exact R/R^-1 authority. Source authority does not erase the executable FAIL.

This gate asks whether using the explicit source identity **directly**, rather than solving qbar independently at inverse parameter and then normalizing its sign, yields an executable graph-dual primitive consistent with the target Appendix-B identities over the full frozen domain.

## Exact source authorities

1. Target: Dittrich et al., arXiv:1609.02429v2, exact archive SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.
   - Appendix A: q, admissibility, coproduct, A8/A9 bilinear normalization.
   - Appendix B: B2 cap, B3/B4 cup, B5 qbar bent-leg map, B7 dual composition, B8/B9 4-valent identities.
2. qbar cited source: Dittrich–Martin-Benito–Steinhaus, arXiv:1312.0905v2, exact archive SHA256 `69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0`.
   - `qg_spinnet_20140616.tex:1101`:
     `{}_q C^{j1 j2 j3}_{m1 m2 m3} = (-1)^(j1+j2-j3) {}_{bar q} C^{j1 j2 j3}_{-m1,-m2,-m3}`.
3. R authority remains inherited from ITER024A/ITER025B and is **not retested** here.

## Frozen hypothesis

`H026`:

For every frozen admissible channel, let `C_q(a,b,c;k)` be the already validated target-coproduct q-CG embedding with ordered tensor basis `V_a ⊗ V_b` and columns in `V_c`.

Define the source-direct qbar coefficient tensor by the exact cited identity:

`C_bar_src(a,b,c;k) = s(a,b,c) * J_ab * C_q(a,b,c;k) * J_c`,

where

- `s(a,b,c) = (-1)^((a+b-c)/2)` for twice-spin labels `a,b,c`;
- `J_t` reverses the magnetic basis, implementing `m -> -m`;
- `J_ab = J_a ⊗ J_b`;
- there is **no m1↔m2 index swap inside the source identity**.

The graph-oriented dual map is then frozen as

`D_src(a,b,c;k) = S_(ba->ab) * C_bar_src(b,a,c;k) / sqrt(d_c)`,

where `S_(ba->ab)` is only the explicit tensor-order permutation required to express the source bent-leg graph in the fixed map order `V_c -> V_a ⊗ V_b`; it is not a fitted orientation choice.

### Singlet q-CG source gauge

The validated q-CG solver retains the A9-allowed residual `±1` channel gauge. For singlet channels `(t,t,0)` only, target B2 supplies an exact absolute cap convention. Before applying the q↔qbar identity, define the q-CG singlet sign by the ratio at the lexicographically first nonzero B2 component and require that this ratio is real `±1` within tolerance and makes the **entire** singlet tensor agree with B2. This is a prospectively fixed source convention, not a post-hoc fit.

For non-singlet channels no coefficient-by-coefficient phase fitting or sign table is allowed. The existing solver sign is retained, and only gauge-covariant/source identities may be used for acceptance.

## Frozen realization/domain

Realization: RC-006 reduced Euclidean `SU(2)_k × SU(2)_k` EPRL/FK-type tensor/intertwiner model. This gate is not Lorentzian EPRL.

Target levels:

- primary: `k = 6, 10, 12`;
- held-out transport: `k = 7, 9, 11`.

All simple labels `0 <= twice_j <= k` are inside the target root-of-unity simple-object range. Cup panels include **every** `twice_j = 1,...,k` at all six levels. No previously failing high-spin point may be removed after execution.

Admissibility is the frozen target rule: triangle/parity plus `a+b+c <= 2k` in twice-spin notation. All tested quantum dimensions must satisfy `|d_j| >= 1e-12`; if a source-qualified tested object is outside the stated domain or has a vanishing required normalization, classify `BLOCKED_SOURCE_DOMAIN`, not FAIL.

## Independent lanes

Use a GitHub Actions matrix with `fail-fast:false`.

### Lane `domain`

No qbar numerical construction. Verify the exact frozen source hashes/locators recorded in the repository, target admissibility/range for every planned cup and channel panel, and nonzero required quantum dimensions. PASS only if the full panel is source-domain admissible. Missing/mismatched authority => `BLOCKED_SOURCE_AUTHORITY`/provenance failure, not numerical FAIL.

### Lane `algebra`

Construct `C_bar_src` directly from the frozen source identity, with no inverse-parameter highest-weight solve. On the frozen channel panels:

- verify the explicit q↔qbar component identity residual `< 2e-12` (construction/provenance check; not counted as independent support);
- verify qbar coproduct intertwining residual `< 5e-9` under the already frozen qbar representation action;
- verify the source singlet B2 gauge calibration has ratio squared error `< 2e-9`, imaginary part `< 2e-9`, and full B2 residual `< 2e-9`.

Primary channel pairs: `(1,1)`, `(2,1)`, `(4,2)` at k=6,10,12; additionally `(6,4)`, `(8,4)`, `(6,6)`, `(8,8)` where admissible. Held-out pairs: `(3,1)`, `(3,2)`, `(5,1)`, `(5,3)` at k=7,9,11.

No per-channel repair is allowed after evidence is seen.

### Lane `cup`

Independent graphical check against target B4. For each k in `(6,7,9,10,11,12)` and every `twice_j=1,...,k`, compare `D_src(t,t,0;k)` to the source B4 cup normalized exactly as in the prior frozen tests.

PASS iff global max residual `< 2e-9`.

This explicitly includes all ITER025A counterexamples, including `(k,twice_j)=(6,6),(7,7),(9,9),(10,8),(10,9),(11,9),(12,9),(12,10)`.

B4 is a source graphical consistency test, not independent evidence for the existence of a cross-school bridge.

### Lane `four`

Use the source-direct `D_src` in the frozen Appendix-B 4-valent contraction checks without changing the prior formulas. Primary panels:

- k=6,10,12: `(1,1,1,1)`, `(2,2,2,2)`, `(4,2,4,2)`;
- k=12 additionally `(6,6,6,6)`, `(8,4,8,4)`.

Held-out panels add at least one admissible non-primary external quadruple at each of k=7,9,11 selected **before** result inspection in the implementation source.

PASS iff global max residual `< 5e-8`.

### Lane `null`

At least three frozen deliberately wrong controls must be detected at residual `>1e-6` while their corresponding correct controls satisfy their lane thresholds:

1. wrong magnetic reversal: omit `J_c`;
2. wrong source sign: force `s=+1` on channels where source `s=-1`;
3. wrong tensor-order realization: omit `S_(ba->ab)` for an asymmetric pair;
4. legacy ITER025A inverse-parameter/reversed-order construction on the previously failing cup panel is retained as a diagnostic negative comparator only; it is not required to fail every point and is never used to tune `D_src`.

PASS if at least 3/3 structural wrong controls are detected. Legacy-comparator outcome is recorded but not part of PASS.

## Aggregate verdict

The aggregate is frozen before implementation.

- `INFRASTRUCTURE_FAIL` if required lane evidence is missing or transport/runtime fails before a scientific result.
- `INVALID_IMPLEMENTATION` if implementation deviates from the formulas/panels/thresholds above, silently drops a counterexample, or applies per-channel post-hoc repair.
- `BLOCKED_SOURCE_AUTHORITY` / `BLOCKED_SOURCE_DOMAIN` if a required exact source/domain statement cannot support the object being tested.
- `RC006_DIRECT_SOURCE_QBAR_ALGEBRA_FAIL` if domain passes but algebra fails.
- `RC006_DIRECT_SOURCE_QBAR_CUP_FAIL` if algebra passes but cup fails.
- `RC006_DIRECT_SOURCE_QBAR_4VALENT_FAIL` if algebra+cup pass but four fails.
- `RC006_DIRECT_SOURCE_QBAR_NULL_FAIL` if positive lanes pass but null controls are not discriminating.
- `PASS — RC006_DIRECT_SOURCE_QBAR_PRIMITIVE_VALIDATED` only if all five lanes PASS.

Only that full PASS sets `eq27_component_reconstruction_prereg_allowed=true`.

## Interpretation ceiling / locks

Even full PASS means only: an executable qbar/dual primitive is source-consistent in this bounded RC-006 realization and the separately preregistered Eq.(27) component gate becomes admissible.

It does **not** establish Eq.(27), Eq.(29), a TNR result, continuum/GR recovery, Lorentzian EPRL, bridge credit, universal composition/refinement, new physics, failure of any school, or candidate theory.

Always false in this gate unless the frozen aggregate full-PASS condition is met for the single named authorization:

- `iter012_retry_authorized=false`
- `eq29_amplitude_authorized=false`
- `one_step_tnr_authorized=false`
- `bridge_credit=false`
- `candidate_theory_authorized=false`
- `new_physics_found=false`
- candidate theory remains `UNFORMED`.
