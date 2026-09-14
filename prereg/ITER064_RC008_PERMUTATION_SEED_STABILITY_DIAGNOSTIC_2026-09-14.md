# ITER064 — RC008 permutation / seed stability diagnostic

Date frozen: 2026-09-14

Parent: ITER063 terminal `INVALID_IMPLEMENTATION_OR_SELECTOR_SYMMETRY_FAIL`.

## Purpose

Diagnose prospectively why ITER063 permutation controls P1/P2 failed to reproduce the parent B2 crossing even though the inherited local source calibration passed axis relabelling and all lanes met the frozen ITER063 convergence thresholds.

This gate is diagnostic only. It cannot upgrade RC008 bridge status or retroactively turn ITER063 into PASS.

## Frozen kernel

Reuse the exact ITER062B scientific kernel without changing any amplitude/source factor, observable, alpha panel, integration domain or endpoint treatment.

Frozen geometries:
- B2 = `(3,1,1,1)`
- P1 = `(1,3,1,1)`
- P2 = `(1,1,3,1)`

These are spatial permutations under the source-kernel symmetry assumption tested locally in calibration.

Frozen alpha panel remains `[0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80]`.

Frozen common seed panel, selected before execution:
`[32452843,49979687,67867967,86028121,104395301,122949823,141650939,160481183]`.

Frozen powers: `2^16` and `2^18` only. No result-driven denser rerun is authorized by this preregistration.

## Diagnostics

For every boundary / alpha / power report normalized coarse and fine volume fluctuation, fine-minus-coarse difference, finite fraction and ESS fraction for every seed.

At each alpha and boundary compute across-seed mean, standard error and coefficient of variation. Report crossings exactly as before, but do not use them to fit anything.

## Frozen diagnostic classification

At `2^18`, require finite fraction 1.0 for every estimate. For central alphas `[0.55,0.60,0.65,0.70]`, require median ESS fraction >= `1e-4` and across-seed CV <= `0.15` for both coarse and fine values. Also require relative change of the eight-seed mean from `2^16` to `2^18` <= `0.15`.

If these numerical conditions fail on any of B2/P1/P2: `NUMERICAL_UNRESOLVED_PERMUTATION_SEED_DIAGNOSTIC`.

If all three converge and all three show a robust crossing in the same or adjacent frozen alpha interval: `DIAGNOSTIC_PASS_PERMUTATION_CROSSING_STABLE`.

If all three converge but B2 crosses while either P1 or P2 does not: `DIAGNOSTIC_FAIL_INTEGRATED_PERMUTATION_MISMATCH`.

If all three converge and none crosses: `DIAGNOSTIC_PARENT_B2_CROSSING_NOT_SEED_STABLE`.

Other mixed cases: `DIAGNOSTIC_MIXED_SEED_TRANSPORT_UNRESOLVED`.

No outcome is a scientific PASS/FAIL for full EPRL/FK, Lorentzian refinement or any bridge.

## Locks

Candidate theory remains `0 / UNFORMED`; bridge credit remains zero. No threshold or model change after viewing results.
