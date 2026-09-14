# ITER063 — RC008 held-out non-retuned transport / selector gate

Date frozen: 2026-09-14

Parent: ITER062B `SCIENTIFIC_PASS_RC008_RESTRICTED_COARSE_FINE_NUMERICAL_RECONSTRUCTION_SCOPED`.

## Aim

Test whether the restricted RC008 coarse↔fine crossing transports beyond the ITER062B boundary panel without any retuning of the amplitude, alpha grid, convergence thresholds, crossing predicate, integration domains or source model.

This is a held-out transport/selector test inside the same severe symmetry-restricted large-j Riemannian EPRL-FK quantum-cuboid truncation. It is not full EPRL/FK refinement, Lorentzian refinement, q-deformed reconstruction, continuum recovery or bridge derivation.

## Frozen implementation inheritance

The scientific kernel is exactly `code/iter062b/reconstruct.py` at parent implementation lineage `8039a7e8a17aa2b62baead26452425971367ae9c`, with only the prospectively declared boundary tuples and independent seeds overridden. No source factor, amplitude term, FP measure, observable, alpha value, sampling power, convergence threshold or crossing rule may be changed.

Inherited alpha panel:
`[0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80]`.

Inherited sample powers:
`2^12, 2^14, 2^16`.

Independent frozen Owen-scrambled Sobol seeds:
`[32452843, 49979687, 67867967]`.

## Frozen held-out boundary panel

Spatial permutation controls, chosen because the source kernel is symmetric under X/Y/Z relabelling while the observable singles out only the T direction:

- P1 = `(1,3,1,1)`
- P2 = `(1,1,3,1)`

Genuinely new anisotropic transport boundaries, frozen before execution:

- H1 = `(2,1,1,2)`
- H2 = `(2,3,1,1)`
- H3 = `(2,3,4,1)`
- H4 = `(1,2,3,2)`

No boundary may be dropped, replaced, rescaled or added after seeing outputs.

## Frozen convergence predicate

Identical to ITER062B on central alpha subset `[0.55,0.60,0.65,0.70]`:

- finite-weight fraction exactly `1.0`;
- median ESS fraction >= `1e-4` for coarse and fine;
- coefficient of variation across seeds <= `0.15` for coarse and fine;
- relative mean change from `2^14` to `2^16` <= `0.20` for coarse and fine.

A boundary failing convergence is NUMERICAL FAIL for that lane and is not counted as a scientific negative.

## Frozen crossing predicate

For each converged boundary, use `D(alpha)=<Delta V1>_fine-<Delta V1>_coarse` at `2^16`. A robust crossing requires an adjacent-panel sign change whose endpoint signs are each resolved relative to the across-seed standard error. Linear interpolation is report-only.

## Frozen scientific classification

Calibration inheritance must first pass unchanged.

Permutation-control requirement:
- both P1 and P2 must converge;
- each must reproduce a robust crossing;
- each crossing bracket must overlap the parent B2 bracket `[0.50,0.55]` or be directly adjacent by one frozen alpha interval. Failure is `INVALID_IMPLEMENTATION_OR_SELECTOR_SYMMETRY_FAIL`, because these lanes test a source symmetry rather than new physics.

Held-out transport requirement:
- among H1–H4, at least three must converge to permit a transport verdict;
- if at least two converged H lanes show robust crossings: `SCIENTIFIC_PASS_RC008_HELDOUT_TRANSPORT_SCOPED`;
- if at least three H lanes converge but fewer than two cross: `SCIENTIFIC_FAIL_RC008_HELDOUT_TRANSPORT_NOT_ROBUST`;
- otherwise: `NUMERICAL_FAIL_HELDOUT_PANEL_CONVERGENCE_NOT_ESTABLISHED`.

No threshold may be changed after execution.

## Adversarial / null control

Run one calibration lane using the inherited analytic calibration, which already includes malformed-area-map detection. Scientific credit is forbidden if inherited calibration fails.

## Claim locks

Even PASS yields no bridge credit and does not authorize `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`, full Riemannian EPRL/FK refinement, Lorentzian refinement, candidate equations or candidate-theory construction.

Candidate theory remains `0 / UNFORMED`; `bridge_credit=false`.
