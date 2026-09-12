# ITER006 — DVD multi-shell inherited held-out gamma: STRONG SUPPORT

Date: 2026-09-12

## Provenance

- preregistration: `protocol/ITER006_DVD_MULTISHELL_HELDOUT_GAMMA_PREREG.json`
- authoritative run: `34708554742`
- aggregate job: `103593421078`
- aggregate artifact: `10302661928`
- artifact digest: `sha256:a9279bd804a1768330edf4c86a5fc560b3485e38ee323943bc941da2950efbdb`
- classification: `DVD_MULTISHELL_HELDOUT_STRONG_SUPPORT`

The held-out gamma set `{0.3,0.8,1.6,2.5,3.0}` was inherited from the earlier Dl0-only held-out run `34703682106`; it was fixed before any D1/D2 held-out response existed.

## Frozen hypothesis

For each held-out gamma, both source-labelled amplitudes must satisfy

`relative_increment(D1 -> D2) < relative_increment(D0 -> D1)`.

Strong support required 5/5 lanes; natural support required at least 4/5.

## Result

All five numerical lanes passed reproducibility and Dl0 regression. Repeat max relative difference was exactly `0.0` in all lanes. All five lanes also passed the preregistered stabilization-pattern test.

| gamma | DVD2 increment D0→D1 | DVD2 D1→D2 | DVD3 D0→D1 | DVD3 D1→D2 | pattern |
|---:|---:|---:|---:|---:|---|
| 0.3 | 0.5301593 | 0.3632207 | 0.3779853 | 0.1486969 | PASS |
| 0.8 | 0.5185440 | 0.2900831 | 0.3855253 | 0.1251279 | PASS |
| 1.6 | 0.4981539 | 0.1979633 | 0.3963155 | 0.1035678 | PASS |
| 2.5 | 0.4828117 | 0.1626209 | 0.4024413 | 0.0989116 | PASS |
| 3.0 | 0.4770166 | 0.1579994 | 0.4043159 | 0.0985548 | PASS |

Together with the three calibration gammas `{0.5,1.2,2.0}`, the same qualitative finite-cutoff pattern is observed at 8/8 tested gamma values.

## Claim lock

This is strong evidence that the **finite-cutoff stabilization pattern transports across the inherited gamma grid**. It is not a proof of mathematical or physical convergence, not a coarse/fine refinement map, not cylindrical consistency, not a continuum limit, not a bridge derivation, and not evidence of new physics by itself.
