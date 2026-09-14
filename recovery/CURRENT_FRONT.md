# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**. Bridge credit remains zero.

## RC006 unchanged

ITER039 remains SCIENTIFIC FAIL; ITER041/042 remain source-BLOCKED. Authoritative ITER042 is `DELEGATED_AUTHORITY_SOURCE_EXPANSION_BLOCKED`, run `34806737112`, durable commit `70a8ccd7f88c9ff98a4d0b5c7cfb8996039f71f6`. No RC006 numerical retry is authorized.

## Lorentzian multi-vertex front

ITER044 is terminal source-scoped SCIENTIFIC PASS — `LORENTZIAN_MULTIVERTEX_REFINEMENT_MAP_SOURCE_QUALIFIED_SCOPED`, run `34807867688`, result commit `1cb98a15d356dc1ec69f1cae42984ac3bd069a82`. The frozen panel source-qualifies the 4D 1→5 Pachner / 5→1 vertex-renormalization route. Zero-spin face-collapse remains separately BLOCKED. `refinement_map_derived=false`.

ITER045 is terminal SCIENTIFIC PASS — `LORENTZIAN_1TO5_IMPLEMENTATION_READINESS_PASS`, original run `34808101073`, null-control recovery run `34808180748`, result commit `d35026e641a87e602d270d4ff227a4f82d1ca617`.

## Active ITER046 — pinned numerical vertex smoke, infrastructure recovery only

Frozen backend: `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.
Frozen inputs: `gamma=1.2`; ten `j=1`; `Dl=0`; primary five `i=0`; held-out five `i=1`; each evaluated twice. N1–N5 test execution, finite real output and deterministic repeatability only; no amplitude target exists.

The original run `34808304690` produced three terminal control PASS artifacts:
- semantic null `10334041954`, `sha256:d3dd2c1691e52672897e798add45f0ce96f3542b56799f4089e91a91136af31c`
- vertex-face map `10333498333`, `sha256:dfc5e769515fca0a036284cca9892a8fe70c80d3ef7b6d59042b4e809ed15094`
- backend-source control `10333199568`, `sha256:98025c30ff53a8c3c0f26e75630e8d5d8355b82bd13b45f2f22874e0ee17ac88`

Its numerical lane failed **pre-science** during parallel test linking, before any amplitude evaluation. Build-order-only repair commit `3b770691c33385cf10a6007d260db6f589d5dac0`, recovery run/job `34808387189 / 103864666854`, successfully built the pinned library and CLI but then failed **pre-science** because the runtime loader could not locate `libsl2cfoam.so`.

No scientific predicate has failed. The second technical repair changes only runtime `LD_LIBRARY_PATH`:
- loader repair commit `e7e41d348296d49ccd565befbd20b4ab0a77778a`
- authoritative recovery run `34808487683`
- job `103864955774`
- latest snapshot: **1 scientifically useful job in_progress / 0 queued**; avoidable idle false.

## Exact next action

Consume terminal run `34808487683`. If the exact pinned executable reaches the four frozen calls, classify N1–N5 from raw values without sign/magnitude/ratio fitting. If it still fails before amplitude evaluation, only a minimal transport/runtime repair is allowed. Only terminal `LORENTZIAN_PINNED_VERTEX_NUMERICAL_SMOKE_PASS` authorizes a separately preregistered bounded multi-vertex assembly/contraction gate.

## Persistent locks

Full ten-face summation, coarse↔fine amplitude equality, Eq.(29)/Lambda, one-step TNR, full Eq.(27), bridge derivation and candidate-theory construction remain unauthorized. Still false: `refinement_map_derived`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `BRIDGE_DERIVED`.
