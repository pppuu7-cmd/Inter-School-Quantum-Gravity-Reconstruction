# ITER074 source authority — CDT 4D walk-distance / diffusion normalization

Date: 2026-09-14
Gate: `ITER074_CDT_4D_WALK_DISTANCE_DIFFUSION_NORMALIZATION_AUTHORITY`
Preregistration commit: `6ed0ba6a07d28c2fa44c66bc03caff1db4da1a2e`

## Frozen stack audited

Primary/full-4D authority:

- arXiv:hep-th/0505113 — J. Ambjorn, J. Jurkiewicz, R. Loll, *Spectral Dimension of the Universe*.
- arXiv:hep-th/0505154 — J. Ambjorn, J. Jurkiewicz, R. Loll, *Reconstructing the Universe*.
- arXiv:1905.08669 — R. Loll, *Quantum Gravity from Causal Dynamical Triangulations: A Review*.
- arXiv:2007.13311 — J. Ambjorn, Z. Drogosz, A. Görlich, J. Jurkiewicz, *Properties of dynamical fractal geometries in the model of Causal Dynamical Triangulations*.
- arXiv:2604.05641 — J. Ambjørn, R. Loll, *Causal Dynamical Triangulations: New Lattice Theory of Quantum Gravity*.

Contextual consistency check only, not a frozen authority source:

- arXiv:1203.3591 — J. Ambjorn, A. Görlich, J. Jurkiewicz, R. Loll, *Nonperturbative Quantum Gravity*.

The contextual review is used only to test whether the frozen-stack interpretation contradicts a detailed CDT account. It does not upgrade any frozen predicate.

## Executive result

The frozen full-4D CDT stack does **not** establish an independent measured mean-square displacement, diffusion radius or scale-dependent walk dimension for the spacetime random walk used in the spectral-dimension measurement.

It does establish a weaker positive object:

- a concrete nearest-neighbour random walk on the dual four-simplex adjacency graph;
- standard smooth/regular diffusion semantics in which linear spread scales as `sqrt(sigma)`;
- discrete geodesic-distance observables on full 4D CDT geometries, including shortest dual-lattice paths/loops and Hausdorff-type measurements;
- explicit acknowledgement that direct/dual lattice distances and anisotropic simplex geometry are representation-dependent at finite cutoff.

This supports only a **regular-step geometry / heuristic diffusion-distance** sub-result, not comparator-grade quantum walk normalization.

## Predicate A — independent diffusion-displacement observable

**NOT ESTABLISHED.**

The 2005 spectral source defines the heat kernel, return probability and the scale-dependent spectral dimension. On infinite flat space it notes that `sqrt(sigma)` is an effective measure of the linear spread of the Gaussian. It does not define or report a separate full-4D CDT observable of the form

`R^2(sigma) = <d^2(X_sigma,X_0)>`

or an equivalent diffusion radius extracted from the same random walk.

The later 2019 and 2026 CDT reviews discuss the spacetime spectral dimension and a growing set of other geometric observables, but the frozen texts do not expose a full-4D scale-dependent walk-dimension / mean-square-displacement measurement.

## Predicate B — evaluated on four-dimensional CDT ensemble

**NOT ESTABLISHED FOR WALK DISPLACEMENT.**

The spectral return probability is measured on the full 4D ensemble. Separately, 4D CDT studies measure geodesic distances, Hausdorff dimensions, loop lengths and curvature-like observables. These are genuine independent geometric measurements, but the frozen stack does not evaluate a displacement-versus-diffusion-duration law for the same random walker.

## Predicate C — extracted `R(sigma)` or `D_w(sigma)` scaling law

**NOT ESTABLISHED.**

No comparator-grade full-4D curve `R(sigma)`, `<r^2(sigma)>`, first-passage radius or scale-dependent `D_w(sigma)` is found in the frozen authority stack.

A detailed CDT review outside the frozen stack describes the numerical spectral implementation as a nearest-neighbour random walk and says that the diffusion distance grows as `sqrt(sigma)` when interpreting the reliable lattice window. That statement is consistent with ordinary nearest-neighbour step counting, but it is not an independently measured anomalous walk law and therefore cannot promote this predicate.

## Predicate D — distance normalization and CDT geometric units

**PARTIAL POSITIVE AUTHORITY.**

The CDT sources define several discrete geometric distance notions:

- direct-lattice edge lengths with spacelike/timelike assignments in the regulated geometry;
- dual-lattice adjacency distance measured by the number of dual links / simplex-to-simplex steps;
- geodesic distances and shortest noncontractible loops in full 4D toroidal CDT.

The 2020 full-4D toroidal study explicitly defines geodesics between simplices by minimal length in the dual lattice and, for simplicity in that observable, assumes equal dual-link lengths. It also demonstrates that quantum geometry produces highly nontrivial distance distributions and shortcuts/outgrowths.

This establishes that discrete distance is a real source-defined CDT observable. It does **not** establish a universal physical conversion factor between one spectral random-walk step and the direct-lattice physical edge scale across anisotropic 4D CDT ensembles.

## Predicate E — evidential independence from `D_s`

**FAILS FOR A WALK-DIMENSION CLAIM / PASSES AS A CONTROL.**

No independent `D_w` is measured in the frozen full-4D stack. Therefore any attempt to infer `D_w` solely from the measured `D_s` and another fractal dimension would violate the preregistered independence requirement.

The independent geodesic/Hausdorff observables remain useful geometry diagnostics, but they do not by themselves measure random-walk displacement.

## Predicate F — validity of `D_s = 2 D_H / D_w` for same 4D scale-dependent geometry

**NOT ESTABLISHED.**

Generic fractal identities relating spectral, Hausdorff and walk dimensions are known in appropriate self-similar settings. The frozen full-4D CDT spacetime spectral dimension is explicitly scale dependent rather than a single self-similar exponent. The stack does not source-qualify a scale-by-scale application of such an identity to the same full spacetime ensembles.

Accordingly, ITER074 does not derive `D_w(sigma)` from `D_s(sigma)` and a Hausdorff measurement.

## Predicate G — full four-dimensional spacetime applicability

**PARTIAL POSITIVE / PROMOTION CONTROLS ACTIVE.**

The spectral measurement itself is full four-dimensional spacetime data. Full-4D geodesic/loop and thick-slice Hausdorff measurements also exist. But several nearby positive results are not the required object:

- spatial-slice Hausdorff dimensions are three-dimensional subgeometry observables;
- thick-slice and full-spacetime Hausdorff dimensions are volume-distance scalings, not random-walk displacement laws;
- toroidal geodesic-loop studies measure shortest paths/topological structure, not `<r^2(sigma)>`;
- reduced multigraph and lower-dimensional CDT models can define walk dimensions but cannot establish the full-4D spacetime law.

## Predicate H — no FRG import

**PASS_CONTROL.**

No QEG/FRG walk dimension or anomalous-diffusion law is used to infer the CDT result.

## Positive residual authority — regular-step geometry only

There is a legitimate but narrow positive sub-result.

The full-4D CDT spectral process is a discrete nearest-neighbour diffusion on the triangulation/dual adjacency structure. In smooth flat space the heat kernel gives Gaussian spread `R ~ sqrt(sigma)`, and detailed CDT accounts use the same `sqrt(sigma)` relation as an order-of-magnitude interpretation of how many lattice steps are probed once the odd/even artifact region has been excluded.

This is enough to justify an infrared/regular-step geometric heuristic. It is **not** enough to establish that the Planckian quantum walk has `D_w=2`, nor to fix an absolute physical diffusion radius in the scale-dependent quantum regime.

## Control audit

- `FLAT_GAUSSIAN_PROMOTION_CONTROL`: **triggered successfully**; smooth-flat `sqrt(sigma)` is not promoted to a Planckian full-CDT theorem.
- `SPECTRAL_WALK_IDENTITY_CONTROL`: **passes**; no `D_w` inferred from `D_s` alone.
- `HAUSDORFF_INFERENCE_CONTROL`: **passes**; no unsupported `2D_H/D_s` construction.
- `SPATIAL_SLICE_SPACETIME_CONTROL`: **passes**; spatial-slice results remain typed as subgeometry observables.
- `TOY_GRAPH_FULL_CDT_CONTROL`: **passes**; reduced/multigraph walk dimensions receive no full-4D authority.
- `GEODESIC_LOOP_DIFFUSION_CONTROL`: **passes**; 4D geodesic-loop measurements are retained as distinct geometry observables.
- `DUAL_DIRECT_DISTANCE_CONTROL`: **triggered**; dual adjacency steps are not silently identified with direct physical edge lengths.
- `FINITE_WINDOW_CONTROL`: **passes**; spectral odd/even and finite-size windows remain explicit.
- `FRG_IMPORT_CONTROL`: **passes**.

## Source-authority classification

**`PASS_SCOPED_REGULAR_STEP_GEOMETRY_ONLY`**

Mandatory negative lock:

**`INDEPENDENT_4D_WALK_DISTANCE_OBSERVABLE = NOT_ESTABLISHED`**

Consequences:

- full-4D spectral return-probability observable: qualified;
- independent full-4D geodesic distance observables: qualified;
- regular nearest-neighbour / `sqrt(sigma)` heuristic: qualified only as a regular-step interpretation;
- scale-dependent full-4D `D_w(sigma)` or `<r^2(sigma)>`: not qualified;
- absolute Planckian diffusion-radius normalization: not qualified;
- ITER073 physical-scale crosswalk: **not reopened**.

## Claim ceiling

No cross-school comparator, bridge, universal walk law, continuum theorem, new physics or candidate theory follows from ITER074.