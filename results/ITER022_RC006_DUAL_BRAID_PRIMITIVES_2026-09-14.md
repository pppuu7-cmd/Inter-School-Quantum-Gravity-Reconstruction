# ITER022 — RC006 cup/qbar-dual + R/braiding primitive qualification

Date: 2026-09-14

## Terminal classification

**`RC006_QBAR_DUAL_TRANSLATION_BLOCKED`** — BLOCKED under the frozen aggregate rule.

The exact cap/cup identities are now executable-qualified with very small residuals and the false-positive controls work. However, the graphical qbar-CG relation has not yet been translated into a uniquely source-qualified component index ordering. Therefore a bounded Eq.(27) component contraction remains unauthorized.

Separately, the automatic R/braiding lane returned PASS on its lexical/formula detector, but direct inspection of the preserved source context does not provide enough evidence to promote the R primitive as independently executable-qualified. This is treated conservatively as an **open authority item**, not as a reason to override or weaken the frozen qbar blocker.

## Authority

- preregistration commit: `576e9479f001e3b6378e36d97147cf95d8ba6415`
- implementation commit: `de09c0cf51fa9792d68e62c80be694a169881af4`
- production head: `254727a91518c72ae3c1c8a06c4c61a8cca73ddc`
- authoritative run: `34785800807`
- jobs: qbar `103800929030`; capcup `103800929150`; rbraid `103800929160`; null `103800929231`; aggregate `103800967237`
- artifacts:
  - capcup `10326731242`, digest `sha256:6c3456c2e3aa6481d853f5d494edb110b018fe3acb78762ab0b27fb3edf9aae1`
  - qbar `10326258811`, digest `sha256:ac519e431d2d22b7dc1b0c05a0f5c214d3fd4aca0e2891b936047a211f33f93f`
  - rbraid `10326183921`, digest `sha256:04992e2341f17f1356de56b2d680b8a63b6e009cfcb961770ba80e68932535ab`
  - null `10326277281`, digest `sha256:d42c639d17c2f12a7e7046f720634cd353e32bec0ccf166e2c33ec8af720c8b8`
  - aggregate `10325954640`, digest `sha256:976da49e6e98afb2d2908a94520978ba67fe07569ce687491126b2d7642a7115`

All raw artifacts and the frozen aggregate were consumed before classification. Green CI was not treated as scientific PASS.

## Lane results

### A — cap/cup executable identity: PASS

Across `k={6,10,12}` and the frozen twice-spin panel, the largest cap-cup identity residual is `2.6360122491655997e-17`, versus the frozen `1e-12` threshold. No phase/sign fit was performed.

### B — qbar-dual graphical translation: BLOCKED

The primary source digest matches the historical pin. The graphical qbar relation is recovered and the cap/cup subcontrol remains accurate (`1.115027998978557e-16`). An explicit component-equation signal exists, but the graph-to-index ordering is not yet independently qualified. The implementation therefore correctly refuses to select an ordering post hoc and returns `BLOCKED_GRAPH_TO_INDEX_ORDERING`.

### C — R/braiding: AUTOMATED DETECTOR PASS, SCIENTIFIC AUTHORITY STILL OPEN

The frozen worker reports one `R matrix` lexical hit, finds Appendix F and marks `explicit_executable_R_formula_signal=true`. However, manual consumption of the preserved source context did not reveal a sufficiently explicit source formula that can yet be mapped to an executable R operator in the target convention. Consequently this lane is not used to claim R qualification. A narrow source-location/formula authority audit remains required.

This conservative interpretation does not alter the aggregate terminal class because qbar translation independently blocks promotion.

### D — adversarial controls: PASS

Correct cap/cup residual is `2.6360122491655997e-17`. Wrong controls are strongly separated: wrong cup q exponent residual `1.6629392246050907`, wrong cup sign residual `2.0`, and ordinary Hermitian qbar-dual is rejected by the source graphical relation. Detected wrong controls: 3/3 (frozen requirement 2/3).

## Consequence

The next admissible work consists of two independent narrow authority streams that may run in parallel:

1. exact qbar graphical-to-component index-order qualification, including orientation/permutation enumeration with source-derived rejection rather than fitting;
2. exact Appendix-F R/braiding source-location and target-convention executable-authority audit.

Only after both close positively may a bounded numerical Eq.(27) component contraction be prospectively preregistered.

Still false: `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `eq29_amplitude_authorized`, `preferred_alpha_found`, `iter012_retry_authorized`. Candidate theory remains **UNFORMED / 0%**.