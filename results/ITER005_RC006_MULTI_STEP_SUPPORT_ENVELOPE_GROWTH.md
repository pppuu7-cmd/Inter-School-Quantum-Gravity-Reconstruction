# ITERATION 005 — RC-006 Multi-Step Support-Envelope Growth

Date: 2026-09-12  
GitHub Actions run: `34665997309`  
Status: `SUCCESS / ENVELOPE GROWTH CONFIRMED / SUPPORT-LEVEL ONLY`

## Question

If the source EPRL/FK support is coarse-recoupled repeatedly without reapplying the local simplicity condition, does the admissible support remain close to the source image or expand into a larger envelope?

## Result

Starting from the exact source support and iterating the finite `SU(2)_k` support recoupling three times:

| case | raw support sizes, steps 0→3 | source-simple fraction, steps 0→3 |
|---|---|---|
| `k=6, gamma=1/3` | `2 → 4 → 8 → 8` | `1.000 → 0.500 → 0.250 → 0.250` |
| `k=10, gamma=3/5` | `2 → 4 → 9 → 12` | `1.000 → 0.500 → 0.222 → 0.167` |
| `k=12, gamma=1/3` | `3 → 45 → 119 → 119` | `1.000 → 0.0667 → 0.0252 → 0.0252` |

For all three source cases:

- extra support appears immediately after the first raw recoupling step;
- all source simplicity targets remain represented at every step;
- the frozen source-native simplicity selector restores the exact original source support at every evaluated step.

## Interpretation

The support-level obstruction is not a one-step accident. Repeated raw recoupling can rapidly populate an overcomplete envelope while preserving the original physical support as a small embedded subset.

The `k=12, gamma=1/3` case is the clearest example: the raw support grows from `3` source states to `119`, while only about `2.5%` of the saturated envelope obeys the original simplicity map.

This supports a structural separation between:

1. coarse transport/composition, which naturally enlarges effective support;
2. a local/source-native physical selector, which imposes the physical constraint inside that support.

## Claim lock

This remains finite support combinatorics. No q-deformed amplitudes, tensor weights, singular spectra, or TNR truncation dynamics are computed here.
