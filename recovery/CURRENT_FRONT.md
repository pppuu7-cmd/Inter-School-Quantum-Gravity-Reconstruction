# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Administrative programme readiness remains **49%**. This is roadmap readiness, not a correctness probability.

## RC006 — current terminal frontier

ITER018 closed the exact Eq.(27) graph/even-k source-convention prerequisite. ITER019 then validated the source-derived q-CG solver at even `k=12` as `RC006_QCG_SOLVER_VALIDATED_BOUNDED_K12`.

ITER020 is now terminal **SCIENTIFIC PASS**:

`RC006_QCG_HELDOUT_TRANSPORT_PASS`.

Authority:

- prereg `35a003e743bfa47bc8577f0a19267367e149be55`
- implementation `b0ce5650b111e60a8b7219a327e7129a5f72ccb8`
- production head `b2c3948e1463060ffa5a2da6230859278a24ccd7`
- run `34785245738`
- jobs: near-cutoff `103799413997`; heldout-recoupling `103799414066`; null-calibration `103799414145`; level-transport `103799414181`; aggregate `103799444617`
- aggregate artifact `10326411477`, digest `sha256:b67462bfedb91ca2ecff5cba655ffce92b430292b76b109e9eb4e525189ca32c`
- durable result `results/ITER020_RC006_QCG_HELDOUT_TRANSPORT_2026-09-14.md`

All raw lane artifacts and the aggregate were consumed. Results: held-out level-transport residual `2.905052937842534e-14`; near-cutoff maximum residual `2.139545123799759e-12` across 18 retained channels with no recurrence/nullspace failure; held-out recoupling max `F^T F-I` residual `1.352772180613162e-15`; false-positive calibration detected all 3/3 deliberately wrong constructions while the correct construction residual remained `2.482534153247273e-16`.

Thus the bounded solver has now passed both the original k=12 gate and a non-retuned transport/adversarial/null-calibration gate.

## What this authorizes

`implementation_validation_gate_authorized=true`.

`eq27_component_reconstruction_prereg_allowed=true`.

Historical Iter012 is **not** silently rerun or reclassified. The next computation must be a new prospectively frozen source-faithful Eq.(27)/Appendix-E component translation/reconstruction checkpoint using the validated solver as backend.

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

BH004/BH004B remains scoped-negative. Genuine multi-vertex Lorentzian EPRL refinement remains source-blocked. RC008 and RC009 remain blocked. Lorentzian Delta4 remains saturated-negative in its tested scope.

## Exact next gate

Prospectively freeze a source-faithful Eq.(27) component-translation/reconstruction gate before implementation. It must preserve the exact target graphical/bilinear normalization, Appendix-B cup/cap/dual structure and Appendix-E normalization chain; use the validated q-CG solver without coefficient fitting; include held-out orientation/permutation and wrong-q/classical/normalization controls; and classify any missing unambiguous graph-to-component ingredient as BLOCKED rather than inventing a convention.
