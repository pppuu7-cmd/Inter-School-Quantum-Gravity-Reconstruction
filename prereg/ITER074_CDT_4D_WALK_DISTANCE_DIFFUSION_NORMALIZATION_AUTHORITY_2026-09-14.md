# ITER074 preregistration — CDT 4D walk-distance / diffusion-normalization authority

Date: 2026-09-14
Gate: `ITER074_CDT_4D_WALK_DISTANCE_DIFFUSION_NORMALIZATION_AUTHORITY`

## Motivation

ITER073 ended at `BLOCKED_INDEPENDENT_PHYSICAL_SCALE_NORMALIZATION`. The blocker factorized into an incomplete absolute CDT diffusion-step normalization, lack of a comparator-grade 4D CDT walk-distance object, and absence of an independently normalized 4D QEG trajectory for the sampled CDT ensemble.

ITER074 isolates the CDT part only. No QEG/FRG object may be used to define or infer the CDT walk law.

## Frozen question

Does the full four-dimensional CDT source stack define and measure, on the full dynamical triangulation ensemble or a source-equivalent ensemble, an independent diffusion-displacement observable such as

`<r^2(sigma)>`, a diffusion radius, first-passage radius, or scale-dependent walk dimension `D_w(sigma)`,

with enough geometric normalization to determine how physical displacement grows with the integer random-walk duration used in the spectral-dimension measurement?

Can this object close the absolute diffusion normalization independently of the return-probability observable `D_s(sigma)`?

## Frozen sources

Primary/full-4D authority:

- arXiv:hep-th/0505113 — J. Ambjorn, J. Jurkiewicz, R. Loll, *Spectral Dimension of the Universe*.
- arXiv:hep-th/0505154 — J. Ambjorn, J. Jurkiewicz, R. Loll, *Reconstructing the Universe*.
- arXiv:1905.08669 — R. Loll, *Quantum Gravity from Causal Dynamical Triangulations: A Review*.
- arXiv:2007.13311 — J. Ambjorn, Z. Drogosz, A. Görlich, J. Jurkiewicz, *Properties of dynamical fractal geometries in the model of Causal Dynamical Triangulations*.
- arXiv:2604.05641 — J. Ambjørn, R. Loll, *Causal Dynamical Triangulations: New Lattice Theory of Quantum Gravity*.

Negative-control literature may be consulted for definitions but cannot establish full-4D authority:

- lower-dimensional CDT;
- radially reduced/multigraph models inspired by CDT;
- regular-complex superposition models;
- QEG/FRG walk-dimension calculations.

## Required predicates

A. A full-4D CDT source explicitly defines a diffusion-displacement observable distinct from return probability, for example `R^2(sigma)=<d^2(X_sigma,X_0)>` using a source-defined graph/geodesic distance.

B. The observable is actually measured or otherwise evaluated on four-dimensional CDT ensembles, not merely described as a standard random-walk expectation.

C. A scaling law `R(sigma)` or `D_w(sigma)` is extracted over a stated reliable diffusion window, with short-walk lattice artifacts and long-walk finite-size effects retained.

D. The distance entering the walk observable has a source-defined relation to CDT geometric lattice units, including the distinction between direct-lattice edge length, dual-simplex adjacency distance and spacelike/timelike anisotropy where relevant.

E. The walk observable is independent of `D_s(sigma)` in the evidential sense: it is measured from displacement/distance data, not obtained solely by inserting a separately measured Hausdorff dimension into a general fractal identity such as `D_s = 2 D_H / D_w`.

F. If a relation among `D_s`, `D_H` and `D_w` is used, the frozen full-4D CDT source must establish its applicability to the same scale-dependent quantum geometry and regime. A generic fractal identity or toy-model relation is insufficient.

G. The result must apply to the full four-dimensional CDT quantum geometry relevant to the spacetime spectral-dimension measurement. Spatial-slice-only dimensions, toroidal geodesic-loop observables, lower-dimensional CDT and reduced multigraph ensembles cannot be silently promoted.

H. No QEG/FRG scale law, anomalous walk result or desired cross-school correspondence may be imported into A-G.

## Frozen classifications

- `PASS_SCOPED_4D_WALK_DISTANCE_NORMALIZATION_QUALIFIED` if A-G pass and a comparator-grade independent 4D walk-distance law is established.
- `PASS_SCOPED_REGULAR_STEP_GEOMETRY_ONLY` if the sources establish only the discrete step geometry / ordinary `sqrt(sigma)` heuristic in a regular or large-scale regime, without an independently measured scale-dependent 4D walk law.
- `BLOCKED_NO_4D_WALK_DISTANCE_AUTHORITY` if no full-4D comparator-grade displacement/walk observable is source-qualified.
- `FAIL_SCOPED_WALK_NORMALIZATION_REJECTED` only if a proposed full-4D walk normalization is explicitly contradicted by the frozen sources.
- `BLOCKED_SOURCE_AUTHORITY` only if source access prevents adjudication.

## Frozen controls

- `FLAT_GAUSSIAN_PROMOTION_CONTROL`: the smooth-flat result `R ~ sqrt(sigma)` cannot be promoted to Planckian CDT without full-4D source authority.
- `SPECTRAL_WALK_IDENTITY_CONTROL`: `D_w` cannot be inferred from `D_s` alone.
- `HAUSDORFF_INFERENCE_CONTROL`: `D_w = 2D_H/D_s` cannot be used unless applicability of the fractal identity to the same full-4D scale regime is source-qualified.
- `SPATIAL_SLICE_SPACETIME_CONTROL`: dimensions of three-dimensional spatial slices cannot be promoted to the four-dimensional spacetime walk.
- `TOY_GRAPH_FULL_CDT_CONTROL`: multigraph/radially reduced CDT models cannot establish a full-CDT walk law.
- `GEODESIC_LOOP_DIFFUSION_CONTROL`: geodesic-loop or quantum-Ricci distance measurements are not automatically random-walk displacement observables.
- `DUAL_DIRECT_DISTANCE_CONTROL`: dual adjacency steps and direct-lattice edge lengths cannot be equated without a source-defined geometric factor.
- `FINITE_WINDOW_CONTROL`: lattice and finite-size windows remain explicit.
- `FRG_IMPORT_CONTROL`: no QEG/FRG walk dimension or scale map may rescue missing CDT authority.

## Claim ceiling

A scoped PASS could only establish a CDT-internal independent diffusion-distance normalization. It would reopen, not resolve, the cross-school ITER073 scale crosswalk. It would not establish FRG/CDT equivalence, universal dimensional flow, a common UV fixed point, `BRIDGE_DERIVED`, `UNIVERSAL_COMMON_PARENT_FOUND`, new physics, or a candidate theory.

Predicates, classifications and controls are frozen before terminal adjudication.