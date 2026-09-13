# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Administrative programme readiness remains **49%**. This is roadmap bookkeeping, not a correctness probability.

## RC006 current authority

ITER018 closed the Eq.(27) graph/even-k source-convention prerequisite as `RC006_EQ27_GRAPH_AND_EVENK_CATEGORY_PINNED_IMPLEMENTATION_PREREG_ALLOWED`.

ITER019 is now terminal **SCIENTIFIC PASS** in its frozen bounded scope:

`RC006_QCG_SOLVER_VALIDATED_BOUNDED_K12`.

Authority:

- prereg `4f497a0e6413d8f4bc0408f0050552fa80d2ba98`
- implementation `4408ad9725aa1ac5bf0a80dd2619ac444c3bb91d`
- production head `d5934a5f2251c01b2d8ec2315d1c36161b45f507`
- run `34785058584`
- jobs: algebra `103798900360`; recoupling `103798900429`; projector-cap `103798900448`; classical-limit `103798900462`; aggregate `103798931295`
- aggregate artifact `10326466098`, digest `sha256:66208c6a95c1c2e7375edf21e8172680a42b36a697c7d5a6ecc921f96dc4f025`
- durable result: `results/ITER019_RC006_QCG_SOLVER_VALIDATION_2026-09-14.md`

Raw artifacts were consumed lane-by-lane. All frozen predicates pass. Maximum algebra intertwiner residual is `1.5625802476324566e-12`; maximum A9 residual `1.183923065063617e-12`; held frozen recoupling `F^T F-I` residual `1.2228665433368622e-15`; classical-projector continuity difference `8.883991123583906e-4 < 2e-3`.

This sets `implementation_validation_gate_authorized=true` only for the bounded solver implementation. It does **not** authorize historical Iter012, Eq.(29)/Lambda, alpha selection, bridge credit or candidate theory.

## Active ITER020

Prospectively preregistered gate:

`RC006_QCG_HELDOUT_NONRETUNED_TRANSPORT`.

- prereg commit `35a003e743bfa47bc8577f0a19267367e149be55`
- implementation commit `b0ce5650b111e60a8b7219a327e7129a5f72ccb8`
- production head `b2c3948e1463060ffa5a2da6230859278a24ccd7`
- authoritative run `34785245738`

Four independent lanes are frozen before result inspection:

1. held-out level transport at k=6 and k=10;
2. adversarial near-cutoff channels at k=6,10,12;
3. held-out non-retuned recoupling invariants at k=6 and k=10;
4. false-positive/null calibration using deliberately wrong coproduct/q-number choices.

No threshold, panel or convention may be changed after production results are visible. Green CI is not a scientific PASS.

## Locks

Still false:

- `iter012_retry_authorized`
- `eq29_amplitude_authorized`
- `bridge_credit`
- `candidate_theory_authorized`
- `preferred_alpha_found`
- `new_physics_found`
- `ALL_KNOWN_SCHOOLS_FAIL`
- `NEW_QG_THEORY_REQUIRED`

BH004/BH004B remains scoped-negative; genuine multi-vertex Lorentzian refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

## Exact next gate

Consume every raw ITER020 artifact and the frozen aggregate from run `34785245738`. Only a full preregistered PASS may authorize a new source-faithful Eq.(27) component/reconstruction preregistration. A failed robustness lane is preserved as a negative result and must not be repaired by post-hoc retuning.
