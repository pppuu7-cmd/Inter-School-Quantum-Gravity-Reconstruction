# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## RC006 unchanged

ITER039 remains SCIENTIFIC FAIL; ITER041/042 remain source-BLOCKED. Authoritative ITER042 is `DELEGATED_AUTHORITY_SOURCE_EXPANSION_BLOCKED`, run `34806737112`, durable commit `70a8ccd7f88c9ff98a4d0b5c7cfb8996039f71f6`. No RC006 numerical retry is authorized.

## Lorentzian multi-vertex front

ITER044: source-scoped SCIENTIFIC PASS — `LORENTZIAN_MULTIVERTEX_REFINEMENT_MAP_SOURCE_QUALIFIED_SCOPED`, run `34807867688`, result commit `1cb98a15d356dc1ec69f1cae42984ac3bd069a82`. The source panel explicitly qualifies the 4D 1→5 Pachner / 5→1 vertex-renormalization route. Zero-spin face-collapse remains separately BLOCKED.

ITER045: SCIENTIFIC PASS — `LORENTZIAN_1TO5_IMPLEMENTATION_READINESS_PASS`, original run `34808101073`, technical null-control recovery `34808180748`, result commit `d35026e641a87e602d270d4ff227a4f82d1ca617`.

ITER046: SCIENTIFIC PASS — `LORENTZIAN_PINNED_VERTEX_NUMERICAL_SMOKE_PASS`. Exact backend `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f` executed the prospectively frozen primary and held-out tuples. Authoritative recovery run/job `34808487683 / 103864955774`; artifact `10333568519`, digest `sha256:aee4671294bc669d57a63d14276f5ec70187f4d4aeaa0be953d331b740e2585e`. Primary amplitude repeated as `6.68473838546e-11`; held-out repeated as `1.77486269381e-10`; both finite and within frozen repeat tolerance. Result commit `81b354c578e9bbbe27776baefeed79f70a6a3eaf`.

This validates the executable local Lorentzian EPRL vertex only. `refinement_map_derived=false`; bridge credit remains zero.

## Active ITER047 — 5→1 assembly authority

Before attempting a five-vertex contraction, ITER047 prospectively freezes the missing assembly layer: exact source formula/weights/sums, global→local backend argument map, and independent shell transport.

Frozen source panel: arXiv `2302.00072`, arXiv `1803.00835`, and exact backend SHA above. A bare product of five local vertices is explicitly rejected as the full amplitude unless all source-required face/edge factors and internal sums are present.

Parallel lanes:
- `formula-2302`: exact 5→1/vertex-renormalization formula authority;
- `formula-1803`: independent 1→5 amplitude/topology authority;
- `backend-map-shell`: deterministic global→local face/tetrahedron map plus non-retuned `Dl=1` primary/held-out transport;
- `assembly-null`: frozen false-claim controls.

Provenance:
- prereg commit `87ca4ffc54ac061288c1d9ad5db6e1559a273b5b`
- production head `2adacb08693365cf6eba0fdf4605e772d5f38b70`
- authoritative run `34808646324`
- jobs: backend-map-shell `103865407445`; formula-2302 `103865407524`; formula-1803 `103865407527`; assembly-null `103865407568`.
- latest snapshot: assembly-null terminal PASS; **3 scientifically useful jobs in_progress / 0 queued**, avoidable idle false.

## Exact next action

Consume the three remaining raw ITER047 artifacts plus aggregate. Source evidence must identify all required internal summation/weight classes and normalization needed for a bounded fixed-cutoff five-vertex implementation; missing/ambiguous factors remain BLOCKED. `Dl=1` transport is judged only by execution/finiteness/repeatability and cannot be promoted to shell convergence or refinement evidence.

Only terminal `LORENTZIAN_5TO1_ASSEMBLY_AUTHORITY_PASS` authorizes a separately preregistered bounded fixed-cutoff multi-vertex contraction.

## Persistent locks

Full ten-face unbounded summation, coarse↔fine amplitude equality, Eq.(29)/Lambda, one-step TNR, full Eq.(27), bridge derivation and candidate-theory construction remain unauthorized. Still false: `refinement_map_derived`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `BRIDGE_DERIVED`.
