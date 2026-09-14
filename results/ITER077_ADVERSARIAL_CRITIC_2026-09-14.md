# ITER077 adversarial critic — FRG/CDT curvature-observable identity

Date: 2026-09-14
Preregistration: `f15c7e53d241533d371416b3c748fbf5d3748d7e`
Source-authority audit: `38b58bc9a430b3c9fde0c5c2280f5493ebbb6dfd`

## Target

Attempt to invalidate or strengthen:

`FAIL_SCOPED_CURVATURE_OBSERVABLE_IDENTITY_REJECTED`

with positive residual

`COMMON_CONSTANT_CURVATURE_STRUCTURE_ONLY`.

## Attack 1 — QRC reduces to Ricci curvature on smooth manifolds, so it is the FRG Ricci-curvature object

Too strong.

The smooth small-probe expansion motivates the name quantum Ricci curvature and relates the average-sphere-distance construction to classical Ricci information. But the measured CDT quantity is a finite-`delta`, direction/ensemble-averaged metric-space observable with a non-universal lattice normalization. The FRG 2018 object is background Ricci curvature entering/evaluating a curvature-dependent effective action.

A shared classical limiting tensor does not make their finite-regulator quantum evaluation procedures identical.

**Verdict: no promotion.**

## Attack 2 — both sides fit positive constant curvature / de Sitter, therefore observable equality is empirically established

Rejected by the frozen four-sphere control.

Many distinct observables on the same approximately constant-curvature geometry can be compatible with the same four-sphere radius/sign. The fit constrains geometry; it does not map the CDT geodesic-sphere estimator to the FRG EAA curvature variable.

**Verdict: retain `COMMON_CONSTANT_CURVATURE_STRUCTURE_ONLY`.**

## Attack 3 — set the QRC radius `delta` equal to the FRG resolving scale `1/k`

No frozen source derives this. `delta` is a geodesic separation/radius measured in the CDT geometry. `k` labels coarse graining in the EAA. The 2022 FRG source supplies spacetime distances/spectra inside each effective metric while retaining `k` as a separate scale label.

**Verdict: `GEODESIC_SCALE_RG_SCALE_SWAP_CONTROL` rejects the rescue.**

## Attack 4 — ensemble average and self-consistent mean geometry are both expectations, so the measure distinction is cosmetic

Rejected.

CDT QRC is computed configuration-wise from metric distances and then averaged over directions/configurations. The FRG mean background is defined by a tadpole/self-consistency condition in a regulated functional formalism. Nonlinearity of curvature and of the QRC construction means `curvature(mean geometry)` and `mean(curvature observable)` cannot be silently identified.

**Verdict: `ENSEMBLE_BACKGROUND_SWAP_CONTROL` is essential.**

## Attack 5 — the 2018 FRG action includes Ricci tensor invariants, which is closer to QRC than scalar-only truncations

True but insufficient. Including Ricci-tensor dependence enriches the FRG truncation and reduces a superficial scalar/tensor mismatch. It still does not define the CDT average-sphere-distance measurement or a map of its probe radius, normalization and ensemble expectation to the EAA/background variables.

**Verdict: richer truncation does not establish observable identity.**

## Attack 6 — classify only as BLOCKED because a future map could exist

A future map may indeed exist. But the frozen scientific claim is whether the **frozen objects already constitute the same source-defined observable under a non-forgetful typed map**. Both constructions are sufficiently explicit to answer that question: no such map is present, and the evaluation procedures are typed differently.

`BLOCKED` would be appropriate if one side's definition were unavailable or too incomplete to decide. Here the strong identity claim is adjudicable and rejected in scope.

**Verdict: FAIL rather than BLOCKED.**

## Attack 7 — a later relational scalar-curvature observable in FRG may close the gap

Potentially high-information, but procedurally irrelevant to ITER077 because it is outside the frozen source stack. If it is closer operationally to CDT QRC, that is a reason for a new prospective gate, not a retroactive upgrade.

**Verdict: reserve for successor research.**

## Attack 8 — use ITER075 de-Sitter action similarity as independent support

Rejected prospectively. The same de-Sitter geometry appearing in a reduced effective-action comparison and in a curvature comparison is not statistically or logically independent evidence for a map. ITER077 must stand on its own frozen curvature sources.

**Verdict: `TARGET_FIT_CONTROL` / predicate G succeed.**

## Critic verdict

**CONFIRMS `FAIL_SCOPED_CURVATURE_OBSERVABLE_IDENTITY_REJECTED`.**

Retained positive residual:

**`COMMON_CONSTANT_CURVATURE_STRUCTURE_ONLY`**.

Durable factorization:

- `CDT_QRC_OPERATIONAL_OBSERVABLE = qualified`
- `FRG_BACKGROUND_CURVATURE_EAA_OBJECT = qualified`
- `FRG_SCALE_DEPENDENT_DE_SITTER_MEAN_GEOMETRY = qualified`
- `COMMON_POSITIVE_CONSTANT_CURVATURE_STRUCTURE = qualified_scoped`
- `SOURCE_DEFINED_QRC_TO_FRG_CURVATURE_MAP = false`
- `DELTA_TO_K_SCALE_MAP = false`
- `ENSEMBLE_TO_MEAN_BACKGROUND_MAP = false`
- `QUANTUM_OBSERVABLE_IDENTITY = rejected_scoped`
- `BRIDGE_CREDIT = 0`

## Successor decision

Two successor routes are now scientifically distinct:

1. freeze a genuinely **relational FRG curvature observable** and compare it prospectively with CDT QRC; or
2. freeze the post-ITER075/076 direct CDT↔FRG comparison literature (arXiv:2408.07808 and 2411.02330), which contains explicit reduced-action/parameter mapping machinery unavailable to the older frozen stacks.

The second route is currently higher-information because it directly targets the exact missing parameter/action crosswalk already exposed by ITER075-076.

Recommended successor:

`PREREGISTER_ITER078_DIRECT_CDT_FRG_REDUCED_ACTION_PARAMETER_CROSSWALK_AUTHORITY`.