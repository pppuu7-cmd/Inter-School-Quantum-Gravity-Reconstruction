# ITERATION 005 — Lorentzian EPRL Shell-Distance Orientation Audit

Date: 2026-09-12  
GitHub Actions run: `34665851619`  
Status: `SUCCESS / FAR-SHELL STRONG SUPPORT FOR ALL GAMMA`

## Design

Pinned `sl2cfoam-next` commit:

`052e4346028870bd76f69a3034e6cae8defb8f7f`.

For each `gamma = 0.5, 1.2, 2.0`, one-vertex Lorentzian EPRL tensors were computed at `Dl=0,1,2`.

For every choice of two open intertwiner axes and all `8 x 8` fixed-boundary pairs, the retained rank-1 projector was trained only from the `Dl=0` all-zero source slice and frozen.

Shared-unitary orientation nulls then compared:

- near shell: `Dl=1 -> Dl=0`;
- farther shell: `Dl=2 -> Dl=0`.

Each transition contains `640` exhaustive cases with `128` shared-unitary null draws per case.

## Preregistered far-shell gate

Natural support:

- median case median-null/source return improvement `>1`;
- fraction cases with majority null worse `>0.5`.

Strong support:

- same median condition;
- fraction majority-null-worse `>0.6`.

## Results

| gamma | near median improvement | far median improvement | far majority-null-worse | far/near gain | far strong support |
|---:|---:|---:|---:|---:|:---:|
| 0.5 | `1.6565x` | `1.8471x` | `0.6234` | `1.1151x` | YES |
| 1.2 | `4.0703x` | `4.2378x` | `0.6969` | `1.0411x` | YES |
| 2.0 | `3.9956x` | `4.1440x` | `0.6938` | `1.0371x` | YES |

All three gamma lanes pass the preregistered strong-support gate at `Dl=2`.

The median far-shell orientation improvement over gamma is `4.14395x`, and the median far/near ratio is `1.04113x`.

## Interpretation

The Lorentzian EPRL orientation effect identified in RM-001 is not confined to the immediate `Dl=1` shell in this one-vertex realization. It persists, and in the present diagnostic slightly strengthens, at `Dl=2`.

This rules out a simple explanation in which the previous orientation result was an artifact of only the first shell correction.

## Claim lock

`Dl` shell extension is not multi-vertex spin-foam refinement, true coarse graining, a continuum limit, or GR recovery. This result strengthens the gravity-side structural evidence for RM-001 but does not supply the missing independent amplitude-level refinement test required for `BRIDGE_DERIVED`.
