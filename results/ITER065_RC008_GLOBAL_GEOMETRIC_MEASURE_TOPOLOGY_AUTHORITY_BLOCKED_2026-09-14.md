# ITER065 — RC008 global geometric measure / topology authority

Date: 2026-09-14

## Terminal classification

**SCOPED BLOCKED — `SCOPED_BLOCKED_NO_EXPLICIT_GLOBAL_MEASURE_AUTHORITY`**

This is not a scientific FAIL of RC008, EPRL-FK, or spin-foam refinement. It closes the current RC008 numerical route at the source-authority layer: the same-realization source stack does not provide an explicit global reduced geometric measure/Jacobian for the glued coarse/fine quantum-cuboid complexes required by the frozen gate.

`candidate_theory = UNFORMED / 0%`; `bridge_credit = false`; `restricted_coarse_fine_amplitude_reproduced = false`.

## Frozen gate and provenance

Preregistration commit: `e1f97fa2ac91a48e9bb479c81074ea091c0d6d21`.

Initial production head: `3609580257c5ff35bbf292d7d04754031bf3523f`.

Initial Actions run: `34877639682`.

Run 1 source lanes failed only at extraction infrastructure; the geometric lanes completed. Aggregate artifact `10361358105`, digest `sha256:f70e984bcfa109ca8b3f07aefdc196289bad4308608d1312abb325a5acb11e36`, correctly classified the run `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION` and gave no gate credit.

A minimal dependency/transport-only repair was then committed at `d6a5e018d2029b3d629142d3b9bc144c09b9fe53`. No scientific source set, topology, criterion, threshold, realization scope, or claim ceiling changed.

Repair run: `34877767148`, completed success. Source aggregate artifact `10362035885`, digest `sha256:c152167507d988f392548bc8577fa59802bd564aa120aacbf943abc029d20b8c`, nominated all four frozen sources for manual equation-level audit and explicitly gave no gate credit.

## Geometric pullback diagnostics

These diagnostics test the frozen reduced geometric embeddings only; they do not define the physical spin-foam measure.

### Coarse two-hypercuboid embedding

Artifact `10360359283`, digest `sha256:1c0de992800e1f858278c3c778a81183df8468e28bc6afdc8ec57a546779fde3`.

Across five frozen split fixtures:
- reduced coordinate dimension = 1;
- Jacobian rank = 1 at every fixture;
- Gram log determinant is finite and constant, `2.377692565480851`;
- analytic vs central-finite-difference Jacobian maximum relative discrepancy is at most `1.5628153092627092e-10`.

Classification: `DIAGNOSTIC_PASS_GEOMETRIC_PULLBACK`.

### Fine 2x2x2x4 embedding

Artifact `10360279585`, digest `sha256:0e325725eada5aaced645a7a82fd1dd55221bddad29531da2327a9b2af115f8b`.

Across five frozen six-coordinate fixtures:
- reduced coordinate dimension = 6;
- Jacobian rank = 6 at every fixture;
- Gram log determinant is finite at every fixture;
- analytic vs finite-difference Jacobian maximum relative discrepancy is at most `1.5000919527268305e-10`.

Classification: `DIAGNOSTIC_PASS_GEOMETRIC_PULLBACK`.

### Adversarial old-local-product sentinel

Artifact `10361348303`, digest `sha256:6581c435770871baaff0d2b576c81cf40e4b195a9d36e8fe657ed954c51c72bf`.

For the ratio `product(local Delta_FP) / sqrt(det(J^T J))`:
- coarse2 coefficient of variation = `0.01783571272665122`;
- fine32 coefficient of variation = `0.9369701593382911`.

Both exceed the frozen `1e-2` non-constancy threshold. Thus the old product of one-cell `Delta_FP` factors is not equivalent up to a global normalization to the frozen geometric pullback sentinel. This is an adversarial structural fact only; it does not determine the correct quantum measure.

## Manual equation-level source audit

Frozen source set:
- arXiv:1508.07961;
- arXiv:1605.07649;
- arXiv:1701.02311;
- arXiv:1804.00023.

Repair artifacts and digests:
- `1508.07961`: artifact `10361751291`, `sha256:067efa63f1ae2e50e7ba14f1435fa1179ed6cfab567ad179055c27afad2dc37e`;
- `1605.07649`: artifact `10361303858`, `sha256:a7200d0b1f90950c0bf935510e90821db8d873edefab113a046c1ce45807798d`;
- `1701.02311`: artifact `10361542560`, `sha256:b65d6e8b6f033000180792944ad196b4bf72a4839b8308e8c388e0f2d6d68b77`;
- `1804.00023`: artifact `10361691343`, `sha256:4883b220bc3ed605d3c1d4374b65184affeb5fbd10d27a3eed0eeb25982f420f`.

### arXiv:1508.07961

Provides the quantum-cuboid baseline, geometricity constraints, non-geometricity diagnostics and asymptotic amplitude structure. The nominated passages do not provide a global glued-complex reduced measure/Jacobian.

### arXiv:1605.07649

Explicitly interprets the coarse-graining integral as ranging over decompositions of a fixed coarse hypercuboid into fine hypercuboids and discusses the path-integral measure. It does not provide an explicit global pullback/Jacobian formula for the glued coarse/fine quantum-cuboid complex.

### arXiv:1701.02311

This is the closest same-realization authority. Appendix B explicitly defines the geometric-sector measure by pullback of `ds^2 = sum_f dj_f^2` to the geometricity-constraint surface and derives the Faddeev-Popov-type factor for **one 4D hypercuboid**. It then states that the general case can be inferred. Elsewhere the paper states that the geometric reduction leaves one integration variable on the coarse lattice and six on the fine lattice, and warns that a nontrivial Faddeev-Popov determinant must be included.

However, it does not write the required global incidence-aware pullback/Jacobian for the specific glued two-hypercuboid and 2x2x2x4 complexes. The phrase that the general case can be inferred is not an explicit source-defined object and cannot authorize a unique implementation under the project source-authority rules.

### arXiv:1804.00023

This paper does contain explicit coarse/fine Jacobian machinery: a change of variables with a Jacobian, delta constraints fixing the coarse/fine temporal structure, and reduced partition functions. But it is the **hyperfrustum curvature truncation**, with different variables and amplitudes. It is not the RC008 quantum-cuboid/hypercuboid realization frozen by ITER065. Importing its Jacobian as the missing RC008 measure would be a cross-realization assumption and therefore requires a separate preregistered derivation/bridge gate; it cannot close the present same-realization authority gate.

## Verdict

All four frozen PDFs were successfully recovered after the control-only repair. No same-realization source supplies the explicit global glued-complex reduced measure required by ITER065.

Therefore the frozen source-authority outcome is:

**`SCOPED_BLOCKED_NO_EXPLICIT_GLOBAL_MEASURE_AUTHORITY`**.

The geometric diagnostic lanes remain useful evidence about the topology of a candidate pullback construction, and the old local-product prescription is positively disfavored as a mere normalization-equivalent representation. But neither fact supplies missing physical/source authority.

## Claim ceiling

No corrected RC008 amplitude crossing is authorized. No fixed point is reproduced. No full Riemannian EPRL/FK refinement, Lorentzian refinement, continuum/GR recovery, cross-school bridge, new physics, or candidate theory follows.

## Next admissible strategy

Do not perform another RC008 crossing calculation unless a genuinely new same-realization source or a separately preregistered derivation establishes the global glued-complex measure object. Repeating local-product numerics or fitting to published fixed-point values is unauthorized.

The programme should now compare independent PHASE_1 fronts and select the highest-information exact blocker/test outside this saturated RC008 source route.