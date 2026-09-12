# ITER002 — CEMR finite-surface inversion result

Status: **AUDITED / DOMAIN_SCOPED**

Registered grid: 4 scenarios × 3 seeds; `epsilon=0.05`, `sigma_log_area=0.003`.

| Scenario | Seed | Class | rank/npar | red. chi2 | max |theta-theta_true| | nuisance | condition |
|---|---:|---|---:|---:|---:|---:|---:|
| clean_calibrated | 101 | PASS_SCOPED | 4/4 | 1.02329 | 0.00151085 | — | 5.30354 |
| clean_calibrated | 211 | PASS_SCOPED | 4/4 | 1.00879 | 0.00139851 | — | 5.30385 |
| clean_calibrated | 307 | PASS_SCOPED | 4/4 | 1.28335 | 0.00308185 | — | 5.30395 |
| global_scale_nuisance | 101 | BLOCKED_NONIDENTIFIABLE | 4/5 | 1.02329 | 2.49737 | -4.99479 | rank-deficient |
| global_scale_nuisance | 211 | BLOCKED_NONIDENTIFIABLE | 4/5 | 1.00879 | 0.136876 | 0.273946 | rank-deficient |
| global_scale_nuisance | 307 | BLOCKED_NONIDENTIFIABLE | 4/5 | 1.28335 | 1.71606 | 3.43268 | rank-deficient |
| channel_anisotropy | 101 | INCOMPATIBLE_SCALAR_CONFORMAL_SCOPED | 4/4 | 338.344 | 0.00151085 | — | 5.30354 |
| channel_anisotropy | 211 | INCOMPATIBLE_SCALAR_CONFORMAL_SCOPED | 4/4 | 337.881 | 0.00139851 | — | 5.30385 |
| channel_anisotropy | 307 | INCOMPATIBLE_SCALAR_CONFORMAL_SCOPED | 4/4 | 338.466 | 0.00308185 | — | 5.30395 |
| channel_profiled | 101 | PASS_SCOPED | 5/5 | 1.0646 | 0.00151085 | 0.050299 | 5.30354 |
| channel_profiled | 211 | PASS_SCOPED | 5/5 | 1.052 | 0.00139851 | 0.0502654 | 5.30385 |
| channel_profiled | 307 | PASS_SCOPED | 5/5 | 1.33919 | 0.00308185 | 0.0502887 | 5.30395 |

## Registered interpretation

- `clean_calibrated`: finite fixed-surface conformal parameters are recoverable in this controlled model.
- `global_scale_nuisance`: absolute conformal scale is structurally non-identifiable without an independent scale/calibration anchor; this is `BLOCKED_NONIDENTIFIABLE`, not a failure of CEMR.
- `channel_anisotropy`: duplicated identical geometric surfaces with opposite non-geometric distortions cannot be absorbed by a scalar conformal field in the registered test.
- `channel_profiled`: when the nuisance signature is explicitly parameterized and identifiable, the false geometric tension can be profiled out.

## Claim lock

These results do **not** establish full RT/QES inversion, causal+entanglement sufficiency for a Lorentzian metric, uniqueness, a quantum-gravity theory, or new physics.

The next authorized CEMR level is a preregistered metric-dependent/extremal-surface inverse problem with wrong-class and QES-like nuisance challenges.
