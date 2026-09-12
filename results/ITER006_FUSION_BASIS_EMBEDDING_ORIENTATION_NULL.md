# ITERATION 006 — Fusion-Basis Embedding-Orientation Null

Date: 2026-09-12  
GitHub Actions run: `34666545108`  
Status: `SUCCESS / STRONG NEAREST-FRAMEWORK ABSORPTION SUPPORT`

## Purpose

Test whether the generic statement

> embedding/subspace orientation carries downstream coarse-graining information beyond singular values

is already ordinary amplitude-level tensor-renormalization structure.

The control is the pinned q-deformed fusion-basis coarse-graining implementation

`ssteinhaus/Fusion-basis-coarse-graining`

at commit

`bb4d1adb1aa81e5090f3ef25a3b9fb8845f19ff4`.

This is a nearest-framework lattice-gauge/TNR control, not an EPRL quantum-gravity realization.

## Counterfactual null

For each coupling `g = 0, 0.5, 1.0`:

1. run the source SVD normally;
2. preserve the complete current first-SVD singular spectrum;
3. after the SVD has been computed, apply a norm-preserving cyclic permutation to the retained first embedding vector `U` inside each admissible block;
4. propagate this modified embedding map through the unmodified gluing/coarse-graining code for three RG steps;
5. compare later singular spectra and ribbon observables with the source-aligned baseline.

Thus the current singular values are unchanged by construction while embedding orientation is altered.

## Preregistered gate

Spectrum preservation:

`first-step first-SVD normalized block spectrum relative difference <= 1e-12`

for all three couplings.

Downstream change:

`max(final second-SVD relative difference, final ribbon relative difference) > 1e-6`.

Natural nearest-framework absorption support:

- spectrum preserved in all couplings;
- downstream changes in at least `2/3` couplings.

Strong support:

- spectrum preserved in all couplings;
- downstream changes in `3/3` couplings.

## Result

| coupling | current first-SVD spectrum difference | final second-SVD difference | final ribbon difference | downstream changed |
|---:|---:|---:|---:|:---:|
| `g=0.0` | `0.0` | `0.0`* | `1.0` | YES |
| `g=0.5` | `0.0` | `0.416628` | `0.624423` | YES |
| `g=1.0` | `0.0` | `0.391272` | `11.621804` | YES |

Natural absorption support: **YES**.  
Strong absorption support: **YES**.

`*` The `g=0` endpoint is degenerate: after the orientation perturbation the nontrivial amplitude sectors collapse and later normalized block spectra contain NaNs/zero-support behavior. The machine aggregate therefore reports the finite parsed second-SVD difference as `0`; the physically meaningful downstream diagnostic in this endpoint is the complete ribbon-observable change. The nondegenerate `g=0.5` and `g=1.0` lanes independently satisfy the intended spectrum-preserved/downstream-changed test with finite spectra.

## Interpretation

This is a **novelty-negative but scientifically positive** result.

It demonstrates in an independent amplitude-level TNR framework that singular values alone do not determine subsequent coarse-grained dynamics. The orientation of the retained SVD embedding map is indispensable information.

Therefore the abstract RM-001 statement

`orientation data matter beyond rank/spectrum`

cannot by itself be advertised as new quantum-gravity physics.

The potentially distinctive ISQGR content is now narrowed to a much more specific conjunction:

1. the transported effective orientation/envelope is **source-native physical/constraint data**, not an arbitrary optimized isometry;
2. a **source-native local physical selector** acts inside the transported envelope;
3. the transport/selector law is frozen without using the held-out closure target;
4. the law survives a genuine QG amplitude/refinement test;
5. the resulting structure is not fully reducible to standard TNR embedding-map optimization or ordinary projected effective dynamics.

This sharpening substantially reduces the risk of false novelty.

## Effect on ISQGR status

- `RM-001` remains a valid structural diagnostic;
- generic orientation-beyond-spectrum novelty: **ABSORBED BY NEAREST FRAMEWORK**;
- `BH-004B` remains a useful QG-specific bridge hypothesis only in its source-native selector/held-out-transport form;
- `BRIDGE_DERIVED = NO`;
- `NEW_PHYSICS = NOT ESTABLISHED`;
- candidate QG theory remains `UNFORMED`.
