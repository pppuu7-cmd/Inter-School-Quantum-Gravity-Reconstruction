# ITER020 preregistration — RC006 held-out non-retuned q-CG transport

Date: 2026-09-14

## Authorization basis

ITER019 terminal classification: `RC006_QCG_SOLVER_VALIDATED_BOUNDED_K12`.

ITER020 is a robustness/transport checkpoint. It does not rerun ITER019's frozen panel and does not authorize Iter012, Eq.(29)/Lambda amplitudes, alpha selection, bridge credit, or candidate-theory construction.

## Frozen construction

Use exactly the ITER019 solver construction, without retuning:

- `q = exp(2*pi*i/(k+2))`;
- the same q-number, representation action and target coproduct;
- the same admissibility rule and bilinear normalization;
- highest-weight nullspace construction followed by target lowering recurrence;
- no external closed-form q-CG coefficient formula;
- no row/column phase fit and no per-level threshold fit.

Any numerical instability must be classified as numerical/infrastructure failure unless a source-level mathematical obstruction is demonstrated. Thresholds below are frozen before production.

## Parallel lanes

### Lane A — level transport

Run held-out low/intermediate-spin channels at `k={6,10}` that were not part of ITER019 production. Frozen channel panel (twice-spins):

- k=6: `(1,3)->2,4`, `(2,3)->1,3,5`, `(3,3)->0,2,4,6` where admissible;
- k=10: `(1,3)->2,4`, `(2,4)->2,4,6`, `(5,5)->0,2,4,6,8,10` where admissible.

PASS: every expected highest-weight nullspace dimension is 1 and maximum Jz/J+/J- intertwiner residual `< 1e-9`.

### Lane B — near-cutoff adversarial transport

At `k={6,10,12}`, test channels whose input/output labels lie on or immediately below the fusion cutoff. Build the admissible set prospectively from the source rule `t1+t2+t3 <= 2k`, with fixed pairs `(k-2,k-2)`, `(k-1,k-1)`, and `(k,k)` in twice-spin notation; retain only output labels satisfying the target admissibility rule and dimension > 0.

PASS: nullspace dimension 1 for every retained channel; maximum intertwiner residual `< 2e-8`; no zero/isotropic bilinear norm; no recurrence singularity in an admissible retained channel.

### Lane C — held-out recoupling invariants

At k=6 and k=10, construct three-body recoupling matrices from solver embeddings only for:

- `(1/2,1/2,1)->J=1`;
- `(1,1/2,1)->J=1/2`;
- `(1,1,1/2)->J=1/2`, where admissible.

No row/column sign fit. PASS if every produced F matrix is square on the allowed intermediate-channel space, final-M dependence `< 5e-8`, `F^T F-I` residual `< 5e-8`, and max imaginary part `< 5e-8`.

### Lane D — null/false-positive calibration

Deliberately perturb one frozen ingredient at a time on a small fixed panel:

1. replace the target coproduct by the undeformed tensor-product coproduct at finite k;
2. replace q-numbers by classical integers while retaining finite-k q phases;
3. flip one coproduct q-exponent sign.

The null-control lane passes only if at least two of these three wrong constructions are detected by either an intertwiner residual `>1e-6`, an A9 residual `>1e-6`, or a recoupling orthogonality residual `>1e-6`. The correct construction must remain below `1e-9` on the same control panel.

## Aggregate classification

All four lanes run independently with `fail-fast:false` and emit raw JSON evidence. Green CI is not a scientific PASS.

Terminal classes:

- `RC006_QCG_HELDOUT_TRANSPORT_PASS`
- `RC006_QCG_LEVEL_TRANSPORT_FAIL`
- `RC006_QCG_NEAR_CUTOFF_FAIL`
- `RC006_QCG_HELDOUT_RECOUPLING_FAIL`
- `RC006_QCG_NULL_CALIBRATION_FAIL`
- `RC006_QCG_HELDOUT_INFRASTRUCTURE_PARTIAL`

Only the full PASS may authorize a later source-faithful Eq.(27) component/reconstruction preregistration. Even full PASS gives zero bridge credit by itself.

## Claim locks

Always false during ITER020: `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `iter012_retry_authorized`, `eq29_amplitude_authorized`, `preferred_alpha_found`.