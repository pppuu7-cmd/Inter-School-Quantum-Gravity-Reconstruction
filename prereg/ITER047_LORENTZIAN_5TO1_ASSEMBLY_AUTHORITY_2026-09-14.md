# Preregistration — ITER047 Lorentzian EPRL 5→1 assembly authority

Date frozen: 2026-09-14

## Inherited state

ITER044 source-qualified the 1→5 Pachner / 5→1 vertex-renormalization route. ITER045 validated algorithmic 1→5 topology and pinned-backend readiness. ITER046 closed `LORENTZIAN_PINNED_VERTEX_NUMERICAL_SMOKE_PASS` on the exact backend `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

No five-vertex contraction, ten-face bulk sum, shell convergence, refinement invariance or bridge has yet been derived.

## Frozen source panel

1. arXiv:`2302.00072` — 5-1 Pachner / vertex-renormalization amplitude and Monte-Carlo bulk-sum implementation.
2. arXiv:`1803.00835` — 1-5 Pachner interpretation and EPRL-FK infrared-divergence amplitude structure.
3. Exact backend commit `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

No source substitution after results are seen.

## Frozen scientific questions

A. Is the full source formula for the 5→1/vertex-renormalization object explicit enough to identify boundary data, ten internal face spins, internal edge/intertwiner sums, face/edge/vertex factors and the five local vertex amplitudes without convention fitting?

B. Can the global 1→5 incidence be mapped mechanically to the backend's local 10-face/5-intertwiner vertex argument slots, with a deterministic ordering frozen independently of numerical amplitudes?

C. Does the exact pinned backend remain finite/executable when the already-frozen ITER046 primary and held-out single-vertex tuples are transported from `Dl=0` to `Dl=1`, without retuning? This is a shell-transport diagnostic only, not a convergence claim.

D. Do semantic/null controls reject product-of-five-vertices as a full amplitude unless the source-required internal sums and weights are included, and reject shell transport as refinement evidence?

## Independent lanes (`fail-fast:false`)

- `formula-2302`: extract exact equation neighborhoods and preserve pages for vertex-renormalization/5-1 amplitude, bulk spins, intertwiners, face/edge/vertex amplitudes and sums.
- `formula-1803`: independently extract 1-5 topology/amplitude structure and compare required internal labels/weights.
- `backend-map-shell`: clone exact pinned backend; mechanically inventory vertex input ordering/API; build with the same infrastructure recipe as ITER046 and evaluate the frozen primary/held-out tuples at `Dl=1` twice each. Inputs stay `gamma=1.2`, ten `j=1`, primary `i=0`, held-out `i=1`.
- `assembly-null`: reject (i) bare product of five vertices as full amplitude absent source weights/sums, (ii) cutoff/profile as refinement map, (iii) `Dl=0`/`Dl=1` finiteness as shell convergence, (iv) numerical agreement as authority for an unsourced ordering.

## Frozen PASS predicates

`ASSEMBLY_FORMULA_SOURCE_PASS` requires preserved source evidence sufficient to identify the five-vertex product structure **and every source-required internal summation/weight class** needed to write a bounded fixed-cutoff implementation. Missing normalization or edge/face factor remains BLOCKED.

`BACKEND_GLOBAL_LOCAL_MAP_PASS` requires a deterministic combinatorial global→local face/tetrahedron ordering plus exact backend API provenance; ordering may not be chosen from amplitude agreement.

`DL1_TRANSPORT_PASS` requires primary and held-out `Dl=1` evaluations to terminate, be finite real doubles and repeat within `1e-12*max(1,abs(A))`. No magnitude/sign/ratio condition exists and no comparison with `Dl=0` is a PASS predicate.

`ASSEMBLY_NULL_PASS` requires all four frozen false claims to remain rejected.

## Terminal outcomes

- `LORENTZIAN_5TO1_ASSEMBLY_AUTHORITY_PASS` iff source-formula authority, backend map, Dl1 transport and null controls all PASS.
- `LORENTZIAN_5TO1_ASSEMBLY_AUTHORITY_BLOCKED` if source transport succeeds but a required formula/normalization/order object is missing or ambiguous.
- `SCIENTIFIC_FAIL` only for an executed frozen numerical predicate failure.
- `INFRASTRUCTURE_FAIL` only for transport/build/tool failure before frozen predicates are evaluable.

PASS authorizes only a separately preregistered **bounded fixed-cutoff multi-vertex contraction**. It does not authorize an unbounded ten-face sum or bridge credit.

## Locks

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `0 / UNFORMED`; no `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`; zero-face deletion remains BLOCKED.