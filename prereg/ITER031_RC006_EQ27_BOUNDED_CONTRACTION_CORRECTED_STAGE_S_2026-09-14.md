# ITER031 preregistration — RC006 bounded Eq.(27) component contraction under corrected Stage-S authority

Date: 2026-09-14

Status: `PREREGISTERED_NOT_EXECUTED`.

## Authorization basis

ITER030 terminalized `PASS — RC006_EQ27_CORRECTED_STAGE_S_COMPONENT_MAP_PASS` and explicitly authorized a separately preregistered bounded numerical component contraction. ITER028 remains BLOCKED and is not retrofitted. ITER031 is a new successor gate.

ITER031 deliberately reuses the already frozen ITER027 numerical kernel and thresholds rather than changing the model after observing prior outputs. The only scientific change is the authority prerequisite: the contraction is now conditioned on the corrected two-factor Stage-S result from ITER030.

## Frozen panels and conventions

Primary levels: `k={6,10,12}`.
Held-out levels: `k={7,9,11}`.
Frozen pair panel: `(1,1),(2,1),(2,2),(4,2)` in twice-spin notation, with admissible output channels generated mechanically.
`alpha=0` remains fixed prospectively.

The numerical primitives are the already validated repository implementations used by ITER027: q-CG solver, source-qualified qbar primitive, cap/cup duality and R/R^-1 maps. No phase, sign, tensor permutation, R orientation, qbar orientation, normalization or held-out parameter may be fitted to improve agreement.

Eq.(29)/Lambda and one-step TNR remain forbidden.

## Four independent lanes

All run with `fail-fast:false`.

### Lane A — authority-domain
PASS requires the ITER031 preregistration, terminal ITER030 PASS result, ITER021 translation result, ITER026 qbar result and pinned qbar/R authority file to exist; no forbidden Eq.(29)/Lambda dependency; and non-empty admissible primary and held-out panels.

### Lane B — component-translation
For every frozen primary and held-out channel, evaluate source q-CG and qbar objects and verify the already frozen source-qbar identity and qbar intertwiner residuals. Thresholds are unchanged from ITER027: source identity `<2e-12`; qbar intertwiner `<5e-9`; all expected tensor shapes must match.

### Lane C — bounded-contraction
Execute the bounded duality/R-inverse component contraction on primary and held-out panels with the same implementation and no retuning. PASS requires all finite values, maximum dual-contraction residual `<5e-8` and maximum R-inverse residual `<5e-8` across both primary and held-out levels.

This is not a full Eq.(27) amplitude/TNR claim; it is a bounded executable component-contraction gate under the corrected source dictionary.

### Lane D — frozen null controls
Use the same preregistered wrong constructions as ITER027: legacy inverse-parameter qbar, wrong magnetic ordering and R↔R^-1 substitution. At least 2/3 must be detected with residual `>1e-6` (or non-finite where structurally invalid).

## Aggregate classes

### PASS — `RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_CORRECTED_STAGE_S_PASS`
Only if A–D all PASS. This authorizes a next, separately preregistered two-factor network assembly gate. It gives zero bridge/TNR/candidate-theory credit.

### SCIENTIFIC FAIL — `RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_CORRECTED_STAGE_S_FAIL`
If all authority/prerequisite checks are valid and a frozen primary or held-out numerical identity exceeds its threshold, or required null controls are not discriminating. Thresholds may not be weakened after inspection.

### BLOCKED
Missing authoritative prerequisite or an unavailable source-qualified primitive is BLOCKED, not scientific FAIL.

### INFRASTRUCTURE FAIL
Import/runtime/artifact/transport failure before substantive evaluation is `NUMERICAL_OR_INFRASTRUCTURE_FAIL_PRE_SCIENCE`.

## Claim locks

Always false during ITER031: `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.

Candidate theory remains `UNFORMED / 0%`. Programme readiness remains 49% unless and until a roadmap rubric/gate is actually closed beyond this bounded layer.
