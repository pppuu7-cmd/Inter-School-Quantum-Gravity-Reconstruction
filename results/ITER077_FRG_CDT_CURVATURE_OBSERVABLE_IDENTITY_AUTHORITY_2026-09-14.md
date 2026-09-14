# ITER077 terminal result — FRG/CDT curvature-observable identity authority

Date: 2026-09-14
Gate: `ITER077_FRG_CDT_CURVATURE_OBSERVABLE_IDENTITY_AUTHORITY`
Preregistration commit: `f15c7e53d241533d371416b3c748fbf5d3748d7e`
Workflow launch: `1cc2ed8342083c4d969ae16bc0305b9ac006ff83`
Authoritative extraction run: `34896247267`
Source-authority commit: `38b58bc9a430b3c9fde0c5c2280f5493ebbb6dfd`
Adversarial-critic commit: `cc65ae82a9f4a0376ee3ef5462d4b662bb2153dd`

## Terminal classification

**`FAIL_SCOPED_CURVATURE_OBSERVABLE_IDENTITY_REJECTED`**

Retained positive residual:

**`COMMON_CONSTANT_CURVATURE_STRUCTURE_ONLY`**

Bridge credit: **0**.

## Question adjudicated

Do the frozen full-4D CDT quantum-Ricci-curvature observable and FRG/QEG curvature/effective-background objects constitute the same source-defined observable under a non-forgetful typed map?

## Result

No, in the frozen scope.

Both sides have real, source-defined curvature structures, but their domains, evaluation procedures, scale semantics and averaging/measure semantics are different and no frozen source supplies the required map.

## CDT object

The 4D CDT source defines quantum Ricci curvature through a quasi-local metric-space measurement:

- choose two geodesic spheres of radius `delta` with centers separated by `delta`;
- compute the normalized average distance between pairs of sphere points;
- use the scale dependence of that dimensionless average-sphere-distance ratio as the quantum-Ricci curvature/profile;
- evaluate the observable on full four-dimensional CDT configurations and average over directions/configurations/ensemble.

The probe variable `delta` is a geodesic radius in the regulated quantum geometry. Finite-`delta` normalization and lattice effects are part of the observable.

## FRG/QEG objects

The 2018 frozen source studies EAA truncations that depend on the Ricci scalar, Ricci tensor and their invariants. It derives RG flows and a fixed-point effective action as a function of **background Ricci curvature**.

The 2022 frozen source studies a family of `k`-dependent self-consistent de-Sitter effective/mean geometries and their scale-dependent spectral geometry.

These are legitimate curvature structures, but they are generated/evaluated through the regulator-dependent EAA/background formalism, not through the CDT average-geodesic-sphere-distance measurement.

## Exact type mismatch

The frozen stack does not define

`(CDT geometry ensemble, sphere pair, delta) -> QRC expectation`

as the same object as

`(FRG EAA trajectory, background/mean metric, k) -> curvature invariant/effective geometry`.

Missing source-defined structures include:

1. domain/codomain map;
2. `delta <-> k` scale map;
3. Monte-Carlo ensemble / geodesic averaging <-> EAA expectation/mean-background map;
4. finite-`delta` quantum-Ricci normalization <-> local/background Ricci-scalar/tensor normalization;
5. regulator/lattice translation.

## Frozen predicate adjudication

- A — CDT operational quantum curvature: **PASS**.
- B — FRG curvature/effective-background object: **PASS**.
- C — source-defined observable identity map: **FAIL / NOT PRESENT**.
- D — geodesic probe scale vs RG scale preserved/mapped: **NO MAP; CONTROL TRIGGERS**.
- E — ensemble/background measure semantics preserved/mapped: **NO MAP; CONTROL TRIGGERS**.
- F — common four-sphere/de-Sitter structure: **PASS AS STRUCTURAL RESIDUAL ONLY**.
- G — no reuse of spectral fit or ITER075 action similarity: **PASS_CONTROL**.

The preregistered strong identity is therefore rejected in scope.

## Why the positive residual survives

The CDT QRC data are compatible, over the qualified non-artifact window, with positive constant-curvature/four-sphere behavior. The FRG frozen stack contains positive-curvature de-Sitter effective backgrounds and curvature-dependent effective actions.

Thus a recurring constant-curvature/de-Sitter structure is source-grounded. It is not sufficient to identify the quantum curvature observables.

## Why FAIL rather than source-BLOCKED

The source definitions on both sides are sufficiently explicit to test the frozen identity claim. They show different operational constructions and no source-defined map. The strong identity claim is therefore adjudicable and rejected, rather than merely unanswerable.

This does **not** say that no future map can be derived.

## Adversarial critic

The critic attempted to rescue the identity by:

- using the smooth small-`delta` Ricci limit;
- treating four-sphere fit agreement as observable equality;
- setting `delta proportional_to 1/k`;
- equating ensemble-averaged QRC with curvature of a self-consistent mean background;
- using richer Ricci-tensor FRG truncations as a substitute for an operational map;
- importing a later relational-curvature source outside the frozen stack.

All rescue routes either violate a frozen control or require new post-prereg authority.

Critic verdict: **CONFIRMS FAIL_SCOPED**.

## Structural consequence

The observable-first route now separates two cases:

- spectral dimension: a genuinely common observable **definition** exists, but independent physical-scale matching remains blocked;
- curvature: the frozen quantum curvature objects themselves are **not the same operational observable**, even though they share a constant-curvature/de-Sitter structural limit.

This reinforces the rule that shared classical geometry is weaker evidence than shared operational observable construction.

## Next high-information gate

A materially stronger direct CDT/FRG comparison source was deliberately excluded from ITER075-076 because it was identified after those source stacks were frozen.

The next gate should freeze it prospectively:

**`PREREGISTER_ITER078_DIRECT_CDT_FRG_REDUCED_ACTION_PARAMETER_CROSSWALK_AUTHORITY`**

Recommended frozen core:

- arXiv:2408.07808 — direct CDT/FRG comparison with explicit minisuperspace parameter mapping machinery;
- arXiv:2411.02330 — follow-up on CDT IR/UV limits and their relation to FRG;
- source-native CDT reduced-action authority and FRG coupling definitions as supporting references fixed before adjudication.

The gate should test whether the direct literature establishes a typed **reduced-action/parameter crosswalk** while keeping conformal-sign rotation, anisotropy/deformation, finite-size scaling and the unresolved CDT correlation-length ↔ FRG `k` relation explicit.

Even a PASS would remain reduced/scoped and carry zero bridge credit absent a later constitutional promotion.

## Claim locks

- `BRIDGE_DERIVED = false`
- `UNIVERSAL_COMMON_PARENT_FOUND = false`
- `NEW_PHYSICS_FOUND = false`
- `NEW_QG_THEORY_REQUIRED = false`
- `ALL_KNOWN_SCHOOLS_FAIL = false`
- candidate theory = `UNFORMED / 0%`
- bridge credit = `0`