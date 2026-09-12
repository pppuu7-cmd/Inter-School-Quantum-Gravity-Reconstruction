# ITER006 — Lorentzian EPRL DVD symmetric D3 extension: STRONG SUPPORT

Date: 2026-09-12

## Frozen question

After the source-labelled DVD2/DVD3 finite-shell calculation had shown a decreasing relative shell-change from D0→D1 to D1→D2 across eight already fixed Immirzi-parameter values, test one additional shell **without changing the gamma grid or the gate after seeing D3**.

Frozen gamma grid: `{0.3,0.5,0.8,1.2,1.6,2.0,2.5,3.0}`.

For both DVD2 and DVD3 the preregistered D3 pattern was

`relative_change(D2→D3) < relative_change(D1→D2)`.

Strong support required 8/8 lanes; natural support required at least 7/8. D0–D2 had to regress exactly to the already terminal values and each D0–D3 computation was repeated twice.

## Authoritative run

- workflow run: `34708941068`
- aggregate job: `103594246242`
- aggregate artifact: `10302319200`
- artifact digest: `sha256:8672e8509a11d5f61d0cc5ed37c49b41b341bcb0afe1bb3bd762d67ac764e949`
- classification: `DVD_D3_EXTENSION_STRONG_SUPPORT`
- numerical lanes: `8/8 PASS`
- pattern lanes: `8/8 PASS`
- D0–D2 regression maximum relative error: `0.0` in all lanes
- repeat maximum relative difference: `0.0` in all lanes

Representative relative-change magnitudes:

| gamma | DVD2 D1→D2 | DVD2 D2→D3 | DVD3 D1→D2 | DVD3 D2→D3 |
|---:|---:|---:|---:|---:|
| 0.3 | 0.3632207 | 0.2498522 | 0.1486969 | 0.0687661 |
| 0.5 | 0.3370471 | 0.2013506 | 0.1397030 | 0.0574839 |
| 0.8 | 0.2900831 | 0.1115650 | 0.1251279 | 0.0413513 |
| 1.2 | 0.2350662 | 0.0045950 | 0.1109324 | 0.0295135 |
| 1.6 | 0.1979633 | 0.0525713 | 0.1035678 | 0.0261766 |
| 2.0 | 0.1760640 | 0.0619079 | 0.1003338 | 0.0262556 |
| 2.5 | 0.1626209 | 0.0381540 | 0.0989116 | 0.0273409 |
| 3.0 | 0.1579994 | 0.0022811 | 0.0985548 | 0.0280307 |

For several higher-gamma lanes the DVD2 value itself changes direction between D2 and D3; therefore the result is deliberately stated as **decreasing change magnitude / finite-cutoff stabilization**, not monotonic convergence.

## Interpretation lock

This is strong evidence that the already observed source-labelled finite-shell stabilization persists for one additional shell across the complete frozen eight-gamma grid. It is **not** a proof of convergence, continuum limit, cylindrical consistency, a coarse↔fine refinement map, a bridge derivation, novelty, or new physics. Auxiliary booster/spin shell depth `D` must not be renamed “refinement”.
