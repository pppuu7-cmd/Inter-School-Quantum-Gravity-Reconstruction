# ITER044 — genuine multi-vertex Lorentzian EPRL refinement source-map audit

Date: 2026-09-14

## Terminal classification

**SCIENTIFIC PASS (source-scoped) — `LORENTZIAN_MULTIVERTEX_REFINEMENT_MAP_SOURCE_QUALIFIED_SCOPED`**.

This is a source-map qualification only. It establishes a source-explicit Lorentzian EPRL multi-vertex/refinement object worth implementing; it does **not** derive a refinement bridge, validate a numerical coarse↔fine amplitude relation, or earn bridge credit.

## Frozen provenance

- prereg commit: `6c26b2b87e7fa21cfc040ef17a8eb2a0cbc88937`
- workflow/production head: `7d1c024fd52d5cb792c3d8e3bc839f9bcce69768`
- authoritative run: `34807867688`
- jobs:
  - semantic-null `103863161250`
  - Monte-Carlo/internal-sum `103863161435`
  - radiative two-vertex `103863161537`
  - dipole two-vertex `103863161561`
  - aggregate `103863249258`
- validated artifacts:
  - semantic-null `10333752084`, `sha256:337ba7fd350ff0563b277074552dff10bf85be13414d669659e0715ca9ec637d`
  - montecarlo `10334200311`, `sha256:32e7104c9e4d9d34227d60d7bcfc5a03d2f489a1018b0962a17c24df4439acd1`
  - radiative `10333742127`, `sha256:14b36dcc9a9ed07759e6883c98e662c898fe49c473b6749160eccbd8d4ad4f48`
  - dipole `10334065586`, `sha256:23b2a8ec9e92a3250c1237ab145789fa9c7540c7604b8b66c8341fbd68b543bc`
  - aggregate `10333686368`, `sha256:b3ca0235374f579423505815ba1477d9604fcc87563c0105bfff0453531d621e`

Aggregate raw status: `MULTIVERTEX_SOURCE_EVIDENCE_COLLECTED_REQUIRES_SCIENTIFIC_CLASSIFICATION`, `lane_count=4`, `transport_complete=true`, `refinement_map_derived=false`, `bridge_credit=false`, `candidate_theory_authorized=false`.

## Frozen scientific findings

### 1. Genuine connected multi-vertex Lorentzian EPRL amplitude — PASS

The frozen panel contains explicit connected multi-vertex Lorentzian EPRL amplitudes with boundary and internal data, not merely products of disconnected one-vertex amplitudes.

- arXiv `1801.03771` explicitly studies Lorentzian EPRL transition amplitudes with up to two non-simplicial vertices; source excerpts include internal-face sums/correlations and explicit two-vertex amplitudes.
- arXiv `2206.14755` gives radiative/two-vertex EPRL diagrams with bulk/internal sums and boundary spins.
- arXiv `2302.00072` gives explicit bulk-spin sums and Monte-Carlo treatment for multi-vertex diagrams.

Therefore `MULTIVERTEX_AMPLITUDE_OBJECT_SOURCE_PASS=true`.

### 2. True refinement/coarse-fine map — PASS, scoped to source topology

The preregistered predicate required a source to explicitly map a coarse complex/boundary object to a refined one or compare amplitudes under a stated refinement/coarse-graining transformation; mere two-vertex existence, cutoff scaling, divergence, or finiteness was insufficient.

The frozen auxiliary arXiv `1803.00835` supplies exactly such a topological refinement statement: the 4D ball diagram is described as a 4-simplex expanded by a **1-5 Pachner move into five 4-simplices**, with the resulting five-vertex/two-complex structure and internal faces/edges explicitly discussed. arXiv `2302.00072` independently identifies the corresponding **vertex-renormalization / 5-1 Pachner-move amplitude**, with five vertices and explicit internal/boundary combinatorics and ten internal-face sums.

This satisfies the prospectively frozen source-map predicate. It does **not** yet prove amplitude invariance or a derived renormalization/refinement bridge in Lorentzian EPRL; it qualifies the source-defined refinement topology and amplitude object for a later implementation gate.

Set `source_refinement_map_qualified=true`; keep `refinement_map_derived=false`.

### 3. Zero-spin face-collapse rule — remains BLOCKED

The frozen extraction did not produce a source-explicit amplitude-preserving identity/rule for deleting or collapsing zero-spin faces/strands. The semantic null control explicitly rejects unsourced zero-face deletion.

Therefore the historical zero-face-collapse ambiguity is **not repaired** and must remain separately BLOCKED. The source-qualified 1-5/5-1 Pachner route is a distinct refinement route; it does not retroactively justify zero-face deletion.

### 4. Executable multi-vertex object — PASS, scoped

The source panel gives source-defined finite-cutoff/internal bulk sums and Monte-Carlo formulations for the multi-vertex/vertex-renormalization diagrams, sufficient to justify a separate bounded implementation/validation gate. This does not authorize an unbounded 10-face production run or bridge claim.

## Null controls

All frozen semantic controls remain enforced:

- two vertices alone != refinement map;
- cutoff/profile/scaling != refinement map;
- numerical finiteness/divergence != refinement map;
- unsourced zero-face deletion != amplitude-preserving collapse.

No threshold, amplitude convention, topology, or source panel was changed after seeing the result.

## Scientific consequence

The previous broad status `BLOCKED_SOURCE_ALGEBRAIC_ZERO_FACE_COLLAPSE_AMBIGUOUS` can now be split:

- **source-explicit 1-5/5-1 Pachner multi-vertex Lorentzian EPRL route: SOURCE-QUALIFIED SCOPED**;
- **zero-face-collapse shortcut: still BLOCKED**.

This is substantive progress but does not yet raise bridge credit. Overall programme readiness remains conservatively **49%** until a source-faithful bounded implementation/validation gate closes.

## Exact next allowed gate

Prospectively preregister a bounded implementation-readiness/validation gate for the frozen 1-5/5-1 Lorentzian EPRL vertex-renormalization object. Pin the official `qg-cpt-marseille/sl2cfoam-next` implementation to an exact commit before computation; separately validate topology/incidence, backend provenance/smoke amplitude, and null/disconnected controls. Do not claim coarse↔fine amplitude equality unless explicitly computed under a later preregistered gate.

## Persistent locks

Candidate theory = **0 / UNFORMED**. `bridge_credit=false`; `BRIDGE_DERIVED=false`; `NEW_PHYSICS_FOUND=false`; `NEW_QG_THEORY_REQUIRED=false`; `ALL_KNOWN_SCHOOLS_FAIL=false`. Eq.(29)/Lambda/TNR remain unauthorized.