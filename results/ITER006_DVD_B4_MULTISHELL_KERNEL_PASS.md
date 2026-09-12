# ITERATION 006 — Lorentzian EPRL DVD B4 multi-shell kernel PASS

Date: 2026-09-12

## Scope

This result qualifies the pinned `sl2cfoam-next` B4 numerical primitive away from the previously tested `Delta l = 0` point. It does **not** establish a DVD2/DVD3 shell-sum convergence law, a coarse/fine refinement map, a continuum limit, or a bridge.

Pinned numerical source:
- repository: `qg-cpt-marseille/sl2cfoam-next`
- commit: `052e4346028870bd76f69a3034e6cae8defb8f7f`
- primitive: `sl2cfoam_b4`

Frozen grid:
- gamma = {0.5, 1.2, 2.0}
- Delta l = {0, 1, 2, 3}
- boundary j_a = 1
- uniform l_a = 1 + Delta l
- fast-vs-accurate relative-error threshold <= 1e-5

## Provenance

Initial run `34706661403` was **infrastructure-invalid for science**: all lanes stopped before the numerical gate because `make ... tests -j2` raced test linking against construction of `libsl2cfoam.so`. No physical result was produced by that run.

The workflow was repaired only at build ordering level:
- `make ... lib -j2`
- then `make ... bin/b4_test -j1`

Frozen scientific parameters and threshold were unchanged.

Authoritative repaired run: `34707794670`.
Aggregate job: `103591135360`.
Aggregate classification: `B4_MULTISHELL_NUMERICAL_KERNEL_PASS`.

## Results

| gamma | Delta l | comparisons | max relative error |
|---:|---:|---:|---:|
| 0.5 | 0 | 5 | 1.29783e-15 |
| 0.5 | 1 | 8 | 5.08148e-10 |
| 0.5 | 2 | 9 | 7.68137e-10 |
| 0.5 | 3 | 9 | 1.19358e-09 |
| 1.2 | 0 | 5 | 4.50813e-16 |
| 1.2 | 1 | 8 | 2.98677e-09 |
| 1.2 | 2 | 9 | 2.83710e-09 |
| 1.2 | 3 | 9 | 3.15916e-08 |
| 2.0 | 0 | 5 | 7.61999e-16 |
| 2.0 | 1 | 8 | 9.74849e-09 |
| 2.0 | 2 | 9 | 2.31470e-08 |
| 2.0 | 3 | 9 | 1.05909e-07 |

All 12 lanes passed the pre-registered `1e-5` threshold. The largest observed error is `1.05909e-07`, at gamma=2.0, Delta l=3.

## Decision

`B4_MULTISHELL_NUMERICAL_KERNEL_PASS = YES`.

This closes the numerical-primitive prerequisite for a prospectively frozen source-labelled DVD2/DVD3 **finite shell-sum amplitude** test. It does not authorize the terms `refinement map`, `cylindrical consistency`, `continuum`, `new physics`, or `bridge` for that next calculation.
