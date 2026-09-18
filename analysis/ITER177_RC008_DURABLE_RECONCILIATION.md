# ITER177 RC008 durable reconciliation with pre-existing ITER064/ITER065 authority

Date: 2026-09-19

## Purpose

ITER177 remains terminal `INVALID_IMPLEMENTATION_OR_SELECTOR_SYMMETRY_FAIL` under its frozen execution. This note does not reclassify that run. It reconciles the post-ITER177 recovery pointer against durable RC008 authorities that already existed in the repository before ITER177 execution head `57a62ecb0e029ed72a2dc162cb4888fd3cd04a49`.

## Pre-existing diagnostic authority

The pre-result tree already contained:

- `prereg/ITER064_RC008_PERMUTATION_SEED_STABILITY_DIAGNOSTIC_2026-09-14.md`;
- workflow `.github/workflows/iter064_rc008_permutation_seed_diagnostic.yml`;
- terminal manual audit `results/ITER064_RC008_CROSSING_CONVERGENCE_AND_GLOBAL_MEASURE_MANUAL_AUDIT_2026-09-14.md`.

ITER064 prereg commit: `aa2179c06bbbc3d54fbd917e1809e335839d30ed`.
Authoritative run: `34874915843`.
Aggregate artifact: `10361141304`, digest `sha256:f248f9146222a411d04b3b74359650f89ff81ce77e9fcb5083cb3a5220376bf8`.

That diagnostic used the common B2/P1/P2 panel, eight prospectively frozen Sobol seeds and powers `2^16,2^18`. Its raw workflow label was `DIAGNOSTIC_PASS_PERMUTATION_CROSSING_STABLE`, but the preserved manual audit correctly rejected scientific/diagnostic promotion because the positive crossing endpoint at `alpha=0.50` remained non-converged under the run's own ESS/CV diagnostics. The durable narrow conclusion is only that the P1/P2 discrepancy is seed/QMC sensitive, not a validated physical selector-symmetry failure.

This matches the independent ITER177 artifact inspection: P1/P2 change sign between 0.50 and 0.55, but their 0.50 signs are not resolved relative to across-seed uncertainty; at 0.55 and above the two permutations are mutually consistent.

## Deeper pre-existing RC008 blocker

The same pre-result tree already contained ITER065:

- prereg `prereg/ITER065_RC008_GLOBAL_GEOMETRIC_MEASURE_TOPOLOGY_AUTHORITY_2026-09-14.md`;
- terminal result `results/ITER065_RC008_GLOBAL_GEOMETRIC_MEASURE_TOPOLOGY_AUTHORITY_2026-09-14.md`.

Prereg commit: `e1f97fa2ac91a48e9bb479c81074ea091c0d6d21`.
Initial run: `34877639682`; source-transport repair run: `34877767148`.

Terminal classification:
`SCOPED_BLOCKED_NO_EXPLICIT_GLOBAL_MEASURE_AUTHORITY`
(descriptive equivalent: `SCOPED_BLOCKED_RC008_GLOBAL_MEASURE_FACTORISATION_UNDERIVED`).

ITER065 independently established that the old product of local one-hypercuboid `Delta_FP` factors is not equivalent up to one normalization constant to the frozen global geometric pullback sentinel: ratio CV `0.01783571272665122` for coarse2 and `0.9369701593382911` for fine32, both above the frozen `1e-2` non-constancy threshold. Manual source audit found no explicit same-realization equation for the required global glued-complex reduced measure/Jacobian.

Therefore the current RC008 numerical-crossing route is blocked at a deeper source-authority layer than the ITER177 permutation-control INVALID.

## Durable consequence

Do not rerun ITER177, do not create a duplicate permutation/seed diagnostic, and do not run another RC008 crossing with a guessed or locally factorized measure.

RC008 can reopen only if one of the following is prospectively established:

1. genuinely new same-realization source authority for the global glued-complex reduced measure/Jacobian; or
2. a separately preregistered mathematical derivation of that global measure / constraint-overlap / gluing object with independent completeness checks.

Until then:
- `restricted_coarse_fine_amplitude_reproduced=false`;
- `bridge_credit=false`;
- `BRIDGE_DERIVED=false`;
- candidate theory remains `0 / UNFORMED`;
- no fixed-point, continuum/GR, full EPRL/FK, Lorentzian-refinement or new-physics claim is authorized.

The next project action is broader PHASE_1 DAG recovery outside the saturated RC008 numerical route, using only genuinely executable unsaturated fronts.
