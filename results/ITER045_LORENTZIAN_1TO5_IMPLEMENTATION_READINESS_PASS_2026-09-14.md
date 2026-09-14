# ITER045 — Lorentzian EPRL 1→5 implementation readiness

Date: 2026-09-14

## Terminal classification

**SCIENTIFIC PASS — `LORENTZIAN_1TO5_IMPLEMENTATION_READINESS_PASS`**.

This gate validates topology/backend readiness only. It does not derive a coarse↔fine amplitude equality and earns no bridge credit.

## Frozen provenance

- prereg commit: `459792b5dcd3675c84eff324bbc2ae3512488472`
- original production head: `40d4b2b5b039c6d48b309b2c54bda91c6dabea02`
- original run: `34808101073`
- original jobs:
  - topology-incidence `103863841052`
  - backend-provenance `103863841282`
  - state-space `103863841319`
  - topology-null `103863841448`
  - aggregate `103863870574`

Validated original PASS artifacts:

- topology incidence `10333528151`, `sha256:b472dc9ed86ad7b798b0560bf7d0ccf107820fb2c01564c83c09a5851c10679f`
- backend provenance `10333308561`, `sha256:860e8c0bf6d4b6c4f731835f809befc1676ea2a8a8b08543ef25c4459568cf72`
- state-space `10333642689`, `sha256:740b3fddf1514bc32186af5a847dcaf774d159c8cee9b68653d9ffcf127a5a9a`

## Technical recovery

The original topology-null lane failed because the implementation used `dict.fromkeys` before evaluating the duplicate-simplex control, erasing the very duplicate that the frozen control was intended to reject. This was a test-harness defect, not a changed scientific predicate.

The original aggregate correctly computed an incomplete `INFRASTRUCTURE_FAIL` summary from only three artifacts, then artifact finalization separately failed with HTTP 403. Neither event is a scientific FAIL.

A D-only recovery changed duplicate detection only; all frozen malformed cases and validity predicates remained unchanged:

- repair commit: `0548ac3838a99351b79a40249f6c7c8f04408c60`
- recovery run/job: `34808180748 / 103864077510`
- recovery artifact: `10333697665`
- digest: `sha256:2b9feddf8681366c11468a0a9563751cccc1b0a48bf8c14b84ac574a4ad8b63b`
- classification: `NULL_PASS`

Raw recovery evidence rejects all four frozen malformed controls: remove-one, duplicate-one, replace-center, and disconnected-one.

## Scientific findings

### Algorithmic 1→5 topology — PASS

Starting only from the original five boundary vertices plus one interior vertex, the algorithm reconstructs exactly:

- 5 refined 4-simplices;
- 10 internal tetrahedra / dual internal edges;
- 10 internal triangles / dual bulk faces;
- 10 boundary triangles;
- every pair of refined 4-simplices shares exactly one internal tetrahedron.

Thus the source-stated 1→5 incidence is reproduced rather than hand-entered.

### Pinned Lorentzian EPRL backend — PASS

Official `qg-cpt-marseille/sl2cfoam-next` is pinned at `052e4346028870bd76f69a3034e6cae8defb8f7f`. The frozen repository/API confirms a Lorentzian EPRL vertex tensor/amplitude interface with ten face spins, Immirzi parameter and shell cutoff controls. No backend version was selected after seeing amplitudes.

### Ten-face raw state-space feasibility — COMPLETE

The frozen diagnostic reports raw Cartesian growth for ten bulk half-integer spins at `Jmax={1,1.5,2,2.5,3}`. This is feasibility information only; no amplitude-derived sector pruning is authorized.

### Null controls — PASS after technical recovery

All prospectively frozen malformed topologies are rejected. The correction did not modify the 1→5 target topology or acceptance criteria.

## Consequence

A separate bounded numerical Lorentzian EPRL backend/vertex validation is now authorized. Full ten-face summation, Pachner amplitude invariance, bridge derivation and zero-spin face deletion remain unauthorized.

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory = `0 / UNFORMED`.
