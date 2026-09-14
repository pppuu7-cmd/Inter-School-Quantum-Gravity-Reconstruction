# ITER065 — RC008 global geometric measure / topology authority — terminal result

Date: 2026-09-14

## Terminal classification

**SCOPED BLOCKED — `SCOPED_BLOCKED_NO_EXPLICIT_GLOBAL_MEASURE_AUTHORITY`**

Descriptive equivalent: `SCOPED_BLOCKED_RC008_GLOBAL_MEASURE_FACTORISATION_UNDERIVED`.

This is not a physical scientific FAIL of RC008, EPRL-FK, or spin-foam refinement. It blocks the current RC008 numerical crossing route because the global quantum-measure mapping for the glued coarse/fine quantum-cuboid complexes remains source-unqualified.

## Frozen gate

Preregistration commit: `e1f97fa2ac91a48e9bb479c81074ea091c0d6d21`.

Implementation commits:
- `f25ccba64d81de1daa4d3c6205a7425d22b93e3e` — geometric/source gate;
- `031cfefd7a0d6f2b62bfce79a12f9a55c544fb98` — aggregate classifier.

Initial production head: `3609580257c5ff35bbf292d7d04754031bf3523f`.
Initial authoritative run: `34877639682`, attempt 1.

Frozen source set: arXiv `1508.07961`, `1605.07649`, `1701.02311`, `1804.00023`.

## Initial run — infrastructure failure only in source lanes

The geometric lanes completed successfully. All four source-authority lanes failed before scientific evaluation because the source jobs omitted a Python runtime dependency required by `gate.py`.

Latest-attempt job IDs from Actions:
- `sentinel`: `104088681482` — success;
- source `1605.07649`: `104088681505` — pre-science failure;
- `coarse2`: `104088681562` — success;
- source `1701.02311`: `104088681655` — pre-science failure;
- source `1804.00023`: `104088681692` — pre-science failure;
- `fine32`: `104088681704` — success;
- source `1508.07961`: `104088681718` — pre-science failure;
- aggregate: `104088788574` — success, classification `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION`.

Initial aggregate artifact `10361358105`, digest `sha256:f70e984bcfa109ca8b3f07aefdc196289bad4308608d1312abb325a5acb11e36`.

These source failures are **INFRASTRUCTURE FAIL PRE-SCIENCE**, not scientific FAIL.

## Minimal source-transport repair

Only the missing runtime dependency was repaired. Frozen sources, terms, source-candidate logic, topology, numerical predicates and interpretation ceiling did not change.

Repair head: `d6a5e018d2029b3d629142d3b9bc144c09b9fe53`.
Repair run: `34877767148`.

Latest-attempt jobs:
- source `1701.02311`: `104089109862` — success;
- source `1804.00023`: `104089109981` — success;
- source `1508.07961`: `104089110145` — success;
- source `1605.07649`: `104089110155` — success;
- source aggregate: `104089211009` — success.

Repair artifacts:
- `1508.07961`: `10361751291`, digest `sha256:067efa63f1ae2e50e7ba14f1435fa1179ed6cfab567ad179055c27afad2dc37e`;
- `1605.07649`: `10361303858`, digest `sha256:a7200d0b1f90950c0bf935510e90821db8d873edefab113a046c1ce45807798d`;
- `1701.02311`: `10361542560`, digest `sha256:b65d6e8b6f033000180792944ad196b4bf72a4839b8308e8c388e0f2d6d68b77`;
- `1804.00023`: `10361691343`, digest `sha256:4883b220bc3ed605d3c1d4374b65184affeb5fbd10d27a3eed0eeb25982f420f`;
- source aggregate: `10362035885`, digest `sha256:c152167507d988f392548bc8577fa59802bd564aa120aacbf943abc029d20b8c`.

The repair aggregate classified `SOURCE_AUTHORITY_CANDIDATE_PRESENT_REQUIRES_MANUAL_EQUATION_AUDIT`; by preregistration this carries no gate credit.

## Geometry diagnostics

These establish internal correctness of the frozen reduced geometric embedding/pullback implementation only. They do not identify the physical spin-foam measure.

### coarse2

Artifact `10360359283`, digest `sha256:1c0de992800e1f858278c3c778a81183df8468e28bc6afdc8ec57a546779fde3`.

Across all five frozen points:
- reduced dimension = 1;
- Jacobian rank = 1;
- Gram log determinant = `2.377692565480851`, finite with positive sign;
- analytic-vs-central-FD maximum relative Jacobian discrepancy <= `1.5628153092627092e-10`.

Classification: `DIAGNOSTIC_PASS_GEOMETRIC_PULLBACK`.

### fine32

Artifact `10360279585`, digest `sha256:0e325725eada5aaced645a7a82fd1dd55221bddad29531da2327a9b2af115f8b`.

Across all five frozen points:
- concatenated local-area outputs = 192;
- reduced dimension = 6;
- Jacobian rank = 6;
- Gram determinant finite with positive sign;
- analytic-vs-central-FD maximum relative Jacobian discrepancy <= `1.5000919527268305e-10`.

Classification: `DIAGNOSTIC_PASS_GEOMETRIC_PULLBACK`.

## Adversarial old-local-product sentinel

Artifact `10361348303`, digest `sha256:6581c435770871baaff0d2b576c81cf40e4b195a9d36e8fe657ed954c51c72bf`.

For `product(local one-hypercuboid Delta_FP) / sqrt(det(J^T J))`, the immutable artifact records:
- `coarse2`: `ratio_cv = 0.01783571272665122`;
- `fine32`: `ratio_cv = 0.9369701593382911`.

Both exceed the frozen `1e-2` non-constancy threshold. Narrow conclusion only: the old product of local one-cell `Delta_FP` factors is not identical up to a single normalization constant to this independent geometric embedding-pullback sentinel. This does **not** determine the correct physical measure.

## Manual equation-level source audit

### arXiv:1508.07961

Provides the foundational quantum-cuboid restricted-state-sum/geometricity setting. The audited passages contain no explicit global glued-complex reduced Faddeev-Popov/Jacobian object for the present coarse/fine construction.

### arXiv:1605.07649

Explicitly discusses coarse/fine hypercuboid decompositions and the path-integral measure. The audited source does not derive the required global incidence-aware pullback/Jacobian for the present glued complex.

### arXiv:1701.02311

Strongest same-realization authority. Appendix B defines the geometric-sector measure as the pullback of `ds^2 = sum_f dj_f^2` to the geometricity-constraint surface and explicitly derives the Faddeev-Popov-type factor for **one 4D hypercuboid**. The source states that the general case can be inferred. Elsewhere it states that the geometric reduction leaves one integration variable on the coarse lattice and six on the fine lattice and warns that a nontrivial determinant must be included.

However, it does not provide the explicit incidence-aware global reduced measure for the glued two-hypercuboid / `2x2x2x4` complex, nor an equation establishing the naive product of one-cell `Delta_FP` factors. Under the frozen source-authority rules, “the general case can be inferred” is insufficient to uniquely authorize that implementation.

### arXiv:1804.00023

Contains explicit coarse/fine Jacobians, variable changes and delta constraints in a symmetry-restricted **hyperfrustum curvature** model. This is useful structural evidence, but it is a different restricted realization/object. Importing its Jacobian into RC008 quantum cuboids would require a separate prospectively frozen derivation/bridge gate and cannot close ITER065.

## Terminal verdict

All four frozen sources were successfully extracted after the control-only repair. Manual audit finds no explicit same-realization source equation for the required global glued-complex reduced measure.

Therefore:

**`SCOPED_BLOCKED_NO_EXPLICIT_GLOBAL_MEASURE_AUTHORITY`**.

ITER065 scientific/gate credit: **0**.

## Claim locks

- corrected RC008 crossing authorized: **false**;
- restricted coarse/fine amplitude reproduction: **false**;
- full Riemannian EPRL/FK refinement: **false**;
- Lorentzian refinement: **false**;
- bridge credit: **0**;
- candidate theory: **0% / UNFORMED**;
- overall programme readiness: **50%**, unchanged.

No `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`, fixed-point, continuum/GR-recovery or candidate-theory claim is authorized.

## Next admissible action

Do not rerun the RC008 crossing with another guessed measure. A later RC008 amplitude/refinement gate requires either a genuinely new same-realization authority or a separately preregistered mathematical derivation of the global measure / constraint-overlap / gluing object.

Compute should move to an independent PHASE_1 front unless such an object is independently established.

## Provenance correction note

This terminal note corrects only provenance/numerical transcription from its first durable version: immutable Actions artifacts give the job IDs and sentinel CV values listed above. The scientific classification and claim ceiling are unchanged.