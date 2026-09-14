# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness: **50%**. Bridge credit remains zero.

## Persistent locks

RC006 numerical retry remains unauthorized. RC009 remains scoped blocked on its tested reduced isotemporal route. Lorentzian Delta4 negative results remain preserved. No full EPRL/FK refinement, Lorentzian refinement, q-deformed bridge derivation or candidate-theory construction is authorized.

Forbidden claims remain `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.

## RC008 source stack that remains valid

ITER061 remains **SCIENTIFIC PASS** for companion refinement-complex/gluing source authority.

ITER062A remains **SCIENTIFIC PASS — `RC008_RESTRICTED_AMPLITUDE_KERNEL_SOURCE_CLOSED`**. The exact restricted Riemannian EPRL-FK quantum-cuboid source chain, large-j dressed hypercuboid kernel, observable, geometricity constraints, one-hypercuboid Fadeev-Popov factor and coarse/fine dimensional reduction remain valid source evidence.

These source-level PASS results are not revoked by the later numerical audit.

## ITER062B — historical workflow PASS superseded by manual audit

Authoritative run `34874113741`; aggregate artifact `10359819990`, digest `sha256:fd62c82a618b6ded0e4ab0013610f00a33a70551e9d3f76ab1188d1c2f44493b`.

The historical workflow/report classified the gate `SCIENTIFIC_PASS_RC008_RESTRICTED_COARSE_FINE_NUMERICAL_RECONSTRUCTION_SCOPED`.

That scientific credit is now **superseded** by the terminal manual audit in `results/ITER064_RC008_CROSSING_CONVERGENCE_AND_GLOBAL_MEASURE_MANUAL_AUDIT_2026-09-14.md`, commit `5f1cc5f980d1d8b49d7755148ab82ee1ebef5d10`.

Reasons:

1. The primary B0 crossing `[0.50,0.55]` uses `alpha=0.50`, where the authoritative aggregate records `fine_ess=false` and `fine_level=false`. The prereg checked convergence only on `[0.55,0.60,0.65,0.70]` but searched crossings on the full panel. Therefore the claimed primary crossing was allowed to use a non-converged endpoint.
2. `code/iter062b/reconstruct.py` inserts the one-hypercuboid `Delta_FP=J/cos(theta)` into every local amplitude and therefore multiplies it twice in the coarse pair and 32 times in the fine complex. The exact source derives the factor for one hypercuboid but the global glued-complex pullback measure after shared-face and area-sum constraints was never machine-derived. That mapping is an unresolved source/implementation object, not something that may be supplied by analogy.
3. As an a-posteriori source-fidelity sentinel only, the published crossings for the same boundaries are approximately `0.628, 0.662, 0.614, 0.607`, whereas ITER062B reported approximately `0.535, 0.567, 0.528`, and no B3 crossing. These numbers were not fit targets, so the mismatch is not a frozen physical FAIL; it reinforces that the executable integral is not yet validated as the published object.

Current ITER062B status: **`INVALID_SCIENTIFIC_INFERENCE_SOURCE_MEASURE_MAPPING_UNRESOLVED`**. This is not a scientific FAIL of RC008.

`restricted_coarse_fine_amplitude_reproduced=false`.

## ITER063 — terminal INVALID retained

Authoritative run `34874671586`; aggregate artifact `10360430809`, digest `sha256:a59a92d11b4d439b25eb17a380c03298dfe606186fa7fbd5187c4483c8ef3d00`.

Frozen verdict remains **`INVALID_IMPLEMENTATION_OR_SELECTOR_SYMMETRY_FAIL`**. P1/P2 failed the preregistered spatial-permutation selector, so positive H1/H2/H4 observations receive no gate credit.

## ITER064 — terminal manual audit

Prereg commit `aa2179c06bbbc3d54fbd917e1809e335839d30ed`; production head `be911ba4e7a847049f4882fbe615d0f25774b3ad`; authoritative run `34874915843`; aggregate job `104079838227`; aggregate artifact `10361141304`, digest `sha256:f248f9146222a411d04b3b74359650f89ff81ce77e9fcb5083cb3a5220376bf8`.

The workflow mechanically classified `DIAGNOSTIC_PASS_PERMUTATION_CROSSING_STABLE`, because B2, P1 and P2 all reported `[0.50,0.55]` crossings under the frozen logical predicates.

Manual audit does **not** accept that crossing claim as numerically converged. At `2^18`, the positive endpoint `alpha=0.50` fails both fine ESS and fine CV checks for all three geometries:

- B2: `D=+1.7352397178352406`, stderr `0.7108412841131606`, `fine_ess=false`, `fine_cv=false`;
- P1: `D=+0.8688160701971994`, stderr `0.6941321335609576`, `fine_ess=false`, `fine_cv=false`;
- P2: `D=+1.3278633647616047`, stderr `0.633022249103691`, `fine_ess=false`, `fine_cv=false`.

At `alpha=0.55`, all three are converged and stably negative. Thus ITER064 supports only the narrower structural observation that the earlier ITER063 spatial-permutation discrepancy was **seed/QMC sensitive**. It does not validate the parent crossing.

Terminal manual classification: **`INVALID_DIAGNOSTIC_INFERENCE_CROSSING_ENDPOINT_NONCONVERGED`**. No scientific gate credit.

## New structural fact

A sign-resolved Monte-Carlo difference is not sufficient evidence for a crossing if one of the sign endpoints is outside the numerically converged regime. Convergence must be attached to every endpoint used in the crossing predicate, not to a disjoint central subset.

Separately, a local one-cell measure factor is not automatically a valid global measure for a glued constrained complex. The unique shared spin variables, embedding constraints and global pullback metric must define the reduced measure before local factorization may be asserted.

## Exact next scientific gate

**`RC008_GLOBAL_GEOMETRIC_MEASURE_TOPOLOGY_AUTHORITY`**.

This is now the highest-information upstream blocker. Before another amplitude-crossing computation, prospectively freeze and derive:

- immutable coarse and fine incidence dictionaries for unique face spins and shared faces;
- all embedding/area-sum and geometricity constraints;
- the 1D coarse and 6D fine reduced coordinate maps;
- the global pullback metric/Jacobian from the unique spin variables;
- an independent symbolic/automatic-differentiation determinant implementation;
- a two-hypercuboid analytic measure sentinel;
- the old product-of-local-`Delta_FP` prescription only as an adversarial comparator.

No corrected amplitude crossing or fixed-point claim is authorized until that measure gate is terminal. Any later crossing gate must require the numerical convergence criteria at **both endpoints of every asserted crossing**. Published fixed-point values may be used only as held-out source sentinels after implementation freeze, never as fitting targets.

## Current compute / readiness

No authoritative scientific Actions are queued or in progress at the reconciled front.

Overall programme readiness: **50%**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.
