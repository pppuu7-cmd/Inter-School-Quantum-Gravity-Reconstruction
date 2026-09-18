# Current front — ISQGR

Date: 2026-09-19.

Overall scientific programme: **50%**. Candidate theory: **0% / UNFORMED**. Bridge credit: **0**.

## ITER177 — terminal INVALID, preserved

Authoritative execution: commit `57a62ecb0e029ed72a2dc162cb4888fd3cd04a49`, run `35399067738`.

Aggregate job/artifact: `105774674791 / 10568907833`, SHA256 `9e341c6d6ada06a2505244a35456022b82a73834f3e7d5809a6e0ac4036e44ce`.

Classification: **`INVALID_IMPLEMENTATION_OR_SELECTOR_SYMMETRY_FAIL`**. Calibration passed; all six boundary computations converged; no artifact was missing. Frozen permutation controls P1 and P2 both lacked a robust crossing, so H1-H4 cannot be promoted to a scientific held-out transport verdict. For record only, H1, H2 and H4 crossed on `[0.50,0.55]`; H3 did not.

## RC008 reconciliation against pre-existing authority

The pre-ITER177 tree already contained the prospectively frozen ITER064 permutation/seed diagnostic and the later ITER065 global-measure authority gate.

ITER064 authoritative run `34874915843` showed that the earlier P1/P2 discrepancy is seed/QMC sensitive, but its positive `alpha=0.50` crossing endpoint remained non-converged under its own ESS/CV diagnostics. Durable interpretation: **`INVALID_DIAGNOSTIC_INFERENCE_CROSSING_ENDPOINT_NONCONVERGED`**. This does not rescue ITER177 or establish a physical crossing.

ITER065 is the deeper terminal RC008 authority:
**`SCOPED_BLOCKED_NO_EXPLICIT_GLOBAL_MEASURE_AUTHORITY`**
(descriptive equivalent: `SCOPED_BLOCKED_RC008_GLOBAL_MEASURE_FACTORISATION_UNDERIVED`).

ITER065 prereg commit: `e1f97fa2ac91a48e9bb479c81074ea091c0d6d21`.
Initial run: `34877639682`; source-transport repair run: `34877767148`.

Its geometric sentinel found that the old product of local one-hypercuboid `Delta_FP` factors is not normalization-equivalent to the frozen global pullback sentinel (ratio CV `0.01783571272665122` for coarse2 and `0.9369701593382911` for fine32, both above the frozen `1e-2` threshold). Manual same-realization source audit found no explicit global glued-complex reduced measure/Jacobian equation.

Therefore:
- `restricted_coarse_fine_amplitude_reproduced=false`;
- corrected RC008 crossing is unauthorized;
- do not rerun ITER177;
- do not duplicate ITER064;
- do not run another RC008 crossing with the old local-product measure.

RC008 can reopen only with genuinely new same-realization authority for the global measure or a separately preregistered mathematical derivation of the global measure / constraint-overlap / gluing object with independent completeness checks.

## Exact next admissible front

Recalculate the broader PHASE_1 DAG outside the saturated RC008 numerical route and select only a genuinely executable unsaturated front.

Known exclusions remain:
- Lorentzian genuine coarse/fine refinement: blocked until a real model-matched map/object exists;
- RC-006 q-deformed EPRL/FK amplitude/TNR: blocked until a source-faithful executable amplitude object exists;
- BH-004B structural selector lane: saturated;
- RC-009: scoped blocked;
- distributional/R-operation branch: blocked at ITER175 prerequisites.

No new iteration should be opened merely to repeat a lexical/source search already terminalized.

## Persistent locks

`B1_total = UNAUTHORIZED`; `ALL_KNOWN_SCHOOLS_FAIL=false`; `NEW_QG_THEORY_REQUIRED=false`; `NEW_PHYSICS_FOUND=false`; `BRIDGE_DERIVED=false`; `ITER118_MATCHING_AUTHORIZED=false`. Candidate theory remains **UNFORMED / 0%**.
