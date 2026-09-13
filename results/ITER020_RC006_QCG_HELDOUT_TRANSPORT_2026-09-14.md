# ITER020 — RC006 held-out non-retuned q-CG transport

Date: 2026-09-14

## Terminal classification

**`RC006_QCG_HELDOUT_TRANSPORT_PASS`** — SCIENTIFIC PASS in the preregistered robustness scope.

This is a transport/false-positive robustness result for the already validated solver. It is not bridge credit and is not a candidate-theory result.

## Authority

- preregistration commit: `35a003e743bfa47bc8577f0a19267367e149be55`
- implementation commit: `b0ce5650b111e60a8b7219a327e7129a5f72ccb8`
- production head: `b2c3948e1463060ffa5a2da6230859278a24ccd7`
- run: `34785245738`
- jobs: near-cutoff `103799413997`; heldout-recoupling `103799414066`; null-calibration `103799414145`; level-transport `103799414181`; aggregate `103799444617`
- artifacts: level `10325868751` (`sha256:6765ebdf82aca65ac640f119116df8bb023b0800847eea791a5afa73f0d93815`); near-cutoff `10325943779` (`sha256:82af9f6c6e9789a8adc6e3419a23bef4ffaf2a3be414a0c90eb7f75abe47ff26`); recoupling `10326775476` (`sha256:fd021a5404c47e1ef3a596c4d5a78034e60cede94cd623872ea0a33dac2d7687`); null `10326083376` (`sha256:f65534c38172aee74d2aee4bebe34cec263769721e31b7e4276f66da444e4146`); aggregate `10326411477` (`sha256:b67462bfedb91ca2ecff5cba655ffce92b430292b76b109e9eb4e525189ca32c`).

Every raw lane artifact and the frozen aggregate were consumed. Green CI alone was not used as a scientific predicate.

## Results

### Level transport — PASS

Held-out k=6 and k=10 channels passed without retuning. Every expected highest-weight nullspace was one-dimensional. Maximum intertwiner residual over the frozen panels was `2.905052937842534e-14`, versus the frozen `1e-9` threshold.

### Near-cutoff adversarial transport — PASS

18 retained channels across k=6,10,12 passed with no recurrence/nullspace failures. Maximum intertwiner residual was `2.139545123799759e-12`, versus `2e-8`.

### Held-out recoupling — PASS

Six panels across k=6 and k=10 passed with no row/column sign fit. Maximum final-M dependence was `7.216449660063518e-16`; maximum `F^T F-I` residual `1.352772180613162e-15`; maximum imaginary part `2.0816681711721685e-16`, all below `5e-8`.

### Null/false-positive calibration — PASS

Correct-construction residual on the frozen control channel was `2.482534153247273e-16`. All three deliberately wrong constructions were detected, exceeding the `1e-6` detection threshold by large margins:

- classical q-number substitution: `0.01846620981021134`
- coproduct exponent flip: `1.056103722013331`
- undeformed coproduct at finite k: `0.5466795137214169`

Frozen requirement was detection of at least two of three; observed 3/3.

## Consequence

The bounded solver has now passed both the original k=12 implementation gate and an independent non-retuned robustness/false-positive gate. The next authorized step is a separately prospectively preregistered source-faithful Eq.(27)/Appendix-E component reconstruction. Historical Iter012 remains historical and is not silently reclassified or simply rerun.

Still false: `bridge_credit`, `candidate_theory_authorized`, `eq29_amplitude_authorized`, `preferred_alpha_found`, `new_physics_found`. Candidate theory remains **UNFORMED**.