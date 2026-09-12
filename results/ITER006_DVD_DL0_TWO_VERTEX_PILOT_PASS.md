# ITER006 — Genuine two-vertex Lorentzian EPRL DVD Dl0 pilot

Date: 2026-09-12

## Scientific classification

`SCIENTIFIC_PASS_SCOPED_DVD_DL0_TWO_VERTEX_PILOT`

This is a scoped PASS for the prospectively frozen single-shell `Delta l = 0` numerical contraction only. It is **not** a full DVD2/DVD3 spin-sum reproduction, multi-shell convergence result, refinement map, continuum result, bridge derivation, or new physics claim.

## Authoritative provenance

- Source: arXiv:1801.03771, pinned source hash `27e781f9ae9b36056a57b7747dc3c58b5b9c944dd0214041149843d8434e16c1`.
- Frozen preregistration: `protocol/ITER006_DVD_DL0_TWO_VERTEX_PILOT_PREREG.json`.
- sl2cfoam-next pinned commit: `052e4346028870bd76f69a3034e6cae8defb8f7f`.
- Workflow run: `34703528413`.
- Workflow head: `cb21a8aaf938c8c893ec9ea58036522bfb382497`.
- Aggregate job: `103579476677`.
- Aggregate artifact: `10301595889`.
- Aggregate artifact digest: `sha256:ef6ed6fa672b79eb259d8d348fe4aebb4983b8aa71966809d408ce8b63abc1d9`.

## Frozen numerical result

All three gamma lanes passed the preregistered finite/reproducible Dl0 gate with zero repeat relative difference:

- `gamma=0.5`: `DVD2=5.496983896037186e-4`, `DVD3=5.496983896037186e-4`.
- `gamma=1.2`: `DVD2=1.2780379206216302e-5`, `DVD3=1.2780379206216305e-5`.
- `gamma=2.0`: `DVD2=3.7591052442651034e-7`, `DVD3=3.759105244265104e-7`.

An independent symbolic/source guard also passed:

- run `34703574873`, head `8d79350e35acc772b12c00e74db059993d262bce`, job `103579481295`, artifact `10301042008`, digest `sha256:9c7d1b5b1947d0c818de59029666f8406c2ac35276e5d59d1df5fd423c1ba276`.
- classification `DVD_DL0_SYMBOLIC_GUARD_PASS`.
- source-derived reductions checked independently: `DVD2 = 9 B4(i=1,k=1) sum_{k=0,1,2}(2k+1) B4(i=1,k)^2`; `DVD3 = 27 B4(i=1,k=1)^3` for the frozen symmetric Dl0 boundary.

## Preserved negative/source-lock result

The earlier leave-one-anchor equation-selection robustness gate remains a scientific/source-authority FAIL (`34701317882`, only 2/8 stable). This pilot does not retroactively turn that failed generic selector into a PASS. The pilot is instead tied to the later explicit source-labelled DVD2/DVD3 authority and independent symbolic reduction guard.

## Next permitted work

Independent held-out non-retuned gamma transport and source-faithful shell diagnostics are permitted. A genuine refinement/bridge promotion remains forbidden until an actual coarse/refined amplitude map and held-out transfer gate are derived and passed.
