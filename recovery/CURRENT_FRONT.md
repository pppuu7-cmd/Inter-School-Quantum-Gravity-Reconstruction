# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## RC006 remains source-BLOCKED

ITER039 remains SCIENTIFIC FAIL. ITER041 remains source-BLOCKED on expanded-domain dual/cap/cup normalization. ITER042 is authoritatively **`DELEGATED_AUTHORITY_SOURCE_EXPANSION_BLOCKED`**, run `34806737112`, result commit `70a8ccd7f88c9ff98a4d0b5c7cfb8996039f71f6`. The later conflicting reinterpretation was voided in commit `269e63e5e41a7f811eee4a11d3ae5aeee967014d`.

ITER043 has **no scientific effect**: run `34807715146` was `INFRASTRUCTURE_FAIL PRE-SCIENCE` and the gate premise was superseded by the pre-existing ITER042 durable result. Result commit `55cb2f9d8b6f08cddee62c4056210d0aa7222ca5`. No RC006 numerical retry is authorized.

## ITER044 — substantive source-scoped PASS

Terminal classification: **`LORENTZIAN_MULTIVERTEX_REFINEMENT_MAP_SOURCE_QUALIFIED_SCOPED`**.

- prereg `6c26b2b87e7fa21cfc040ef17a8eb2a0cbc88937`
- production `7d1c024fd52d5cb792c3d8e3bc839f9bcce69768`
- authoritative run `34807867688`
- jobs: semantic-null `103863161250`; Monte-Carlo/source `103863161435`; radiative `103863161537`; dipole `103863161561`; aggregate `103863249258`
- artifacts: semantic-null `10333752084` (`sha256:337ba7fd350ff0563b277074552dff10bf85be13414d669659e0715ca9ec637d`); Monte-Carlo `10334200311` (`sha256:32e7104c9e4d9d34227d60d7bcfc5a03d2f489a1018b0962a17c24df4439acd1`); radiative `10333742127` (`sha256:14b36dcc9a9ed07759e6883c98e662c898fe49c473b6749160eccbd8d4ad4f48`); dipole `10334065586` (`sha256:23b2a8ec9e92a3250c1237ab145789fa9c7540c7604b8b66c8341fbd68b543bc`); aggregate `10333686368` (`sha256:b3ca0235374f579423505815ba1477d9604fcc87563c0105bfff0453531d621e`)
- durable result commit `1cb98a15d356dc1ec69f1cae42984ac3bd069a82`

The frozen source panel source-qualifies genuine connected multi-vertex Lorentzian EPRL amplitudes and, critically, an explicit 4D **1→5 Pachner refinement**: a 4-simplex expanded into five 4-simplices. The corresponding 5→1 vertex-renormalization object is explicitly treated with five vertices and internal bulk sums. This satisfies the preregistered source-map predicate; it is stronger than merely observing two vertices, a cutoff profile, or a divergence.

The historical **zero-spin face-collapse shortcut remains BLOCKED**. No source-explicit amplitude-preserving zero-face deletion identity was found, and it is not inferred from the new Pachner route.

Set `source_refinement_map_qualified=true`, but keep **`refinement_map_derived=false`** until source-faithful implementation/validation closes. No bridge credit is earned by ITER044 alone.

## Active ITER045 — 1→5 implementation readiness

The next gate was frozen before implementation. Official backend is pinned to `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

ITER045 independently checks:

1. algorithmic 1→5 incidence/topology (expected 5 refined 4-simplices, 10 internal tetrahedra/dual edges, 10 internal triangles/dual faces, 10 boundary triangles);
2. pinned backend provenance/API for Lorentzian EPRL vertex tensors with ten spins plus Immirzi/shell controls;
3. raw ten-bulk-face state-space growth at frozen half-integer cutoffs without amplitude-derived pruning;
4. malformed/disconnected topology null controls.

- prereg commit `459792b5dcd3675c84eff324bbc2ae3512488472`
- production head `40d4b2b5b039c6d48b309b2c54bda91c6dabea02`
- authoritative run `34808101073`
- jobs: topology `103863841052`; backend `103863841282`; state-space `103863841319`; topology-null `103863841448`
- latest snapshot: **4 in_progress / 0 queued**, avoidable idle false.

A PASS authorizes only a separately preregistered bounded Lorentzian vertex/contraction validation. It does not authorize a full ten-face sum, coarse↔fine equality, bridge derivation, or zero-face deletion.

## Exact next action

Consume all ITER045 raw artifacts and aggregate against the frozen predicates. If readiness passes, preregister a bounded numerical Lorentzian EPRL successor using the exact pinned backend and source topology. Any backend or topology failure must remain BLOCKED/INFRASTRUCTURE as appropriate; do not alter the 1→5 topology or choose cutoffs after seeing amplitude values.

## Persistent locks

Eq.(29)/Lambda, one-step TNR, full Eq.(27) amplitude and candidate-theory construction remain unauthorized. BH004/BH004B remains scoped-negative; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.

Still false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `BRIDGE_DERIVED`.
