# ITER006 — DVD Δl=0 held-out gamma transport

Date: 2026-09-12

## Frozen gate

Five held-out, non-retuned Immirzi-parameter points `gamma = {0.3, 0.8, 1.6, 2.5, 3.0}` were evaluated with exactly the same pinned `sl2cfoam-next` realization and source-labelled DVD2/DVD3 `Δl=0` contraction used by the preregistered pilot. Each lane was executed twice. The prospective acceptance rule required all five lanes to satisfy the existing lane gate; no monotonicity or scaling law was fitted.

## Authoritative provenance

- workflow run: `34703682106`
- workflow/head commit: `958514e1342b451511c40188b776e19e76d2a1d0`
- aggregate job: `103579890972`
- aggregate artifact: `10301416544` (`dvd-dl0-heldout-gamma-summary`)
- aggregate artifact digest: `sha256:590b11ec27f3d41ae5265b0c41091eb77303fd6e4a28db3914a838e59b38a425`

Lane artifacts consumed by the aggregate:

- gamma 0.3: artifact `10301645973`, digest `sha256:e058eaf7acd23dc8417d8195e8a60032921ae039b896079095728eed5dbb7d82`
- gamma 0.8: artifact `10301466389`, digest `sha256:2e85d9b7388efcdb154fa42bd2bd20e9eaaa1848f348ac633656ec28fa8c5a12`
- gamma 1.6: artifact `10300691982`, digest `sha256:46fdcb5fbcbac2f1e968e9c2f7d72e89db17190ebbe43211b7dda3cb26e365c4`
- gamma 2.5: artifact `10301236801`, digest `sha256:26a9e366f273856ca3ecd7cb37db6564c76edf00569b2efb6002df9ae22601b2`
- gamma 3.0: artifact `10300806694`, digest `sha256:a2580173a87883f22ed7e5fb7a4b32354c93a85ee6b1dcb0b60c2fc62a3d7151`

## Raw aggregate result

All `5/5` lanes passed. The two repeated evaluations were bitwise/numerically identical at the recorded precision (`repeat_max_relative_difference = 0.0`) in every lane.

| gamma | DVD2 Δl=0 | DVD3 Δl=0 | repeat max rel. diff |
|---:|---:|---:|---:|
| 0.3 | 1.3370736856606288e-3 | 1.3370736856606288e-3 | 0 |
| 0.8 | 1.0909544347890166e-4 | 1.0909544347890166e-4 | 0 |
| 1.6 | 1.922261779345611e-6 | 1.9222617793456108e-6 | 0 |
| 2.5 | 6.617261720924785e-8 | 6.617261720924782e-8 | 0 |
| 3.0 | 1.5100198765908135e-8 | 1.5100198765908138e-8 | 0 |

## Scientific classification

`DVD_DL0_HELDOUT_GAMMA_PASS`

This closes only the held-out/non-retuned transport and reproducibility test for the same source-labelled `Δl=0` contraction. It does **not** establish a full spin sum, multi-shell convergence, coarse/refined amplitude map, continuum limit, bridge derivation, or novelty.

## Next permitted gate

Prospectively test the source-relevant Lorentzian EPRL B4 multi-shell kernel for `Δl > 0` using pinned `sl2cfoam-next`, without treating a kernel diagnostic as a DVD2/DVD3 multi-shell amplitude or a refinement map. Only after the multi-shell numerical primitive is validated may a separately preregistered full labelled contraction/shell-sum be implemented.
