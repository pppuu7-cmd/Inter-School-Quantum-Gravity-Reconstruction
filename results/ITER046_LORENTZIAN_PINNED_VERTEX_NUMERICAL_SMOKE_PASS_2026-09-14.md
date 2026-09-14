# ITER046 — pinned Lorentzian EPRL vertex numerical smoke

Date: 2026-09-14

## Terminal classification

**SCIENTIFIC PASS — `LORENTZIAN_PINNED_VERTEX_NUMERICAL_SMOKE_PASS`**.

This is an executable single-vertex backend validation embedded in the source-qualified 1→5 programme. It does not yet compute a five-vertex contraction, coarse↔fine equality, Pachner invariance or a refinement bridge.

## Frozen preregistration and backend

- prereg commit: `f648ceff1082b98f44b8e1715e530c529862de62`
- original workflow head: `86eac7ecd3eeb069b414c6dfd6a74edf0b5f840b`
- backend: `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`
- frozen inputs: `gamma=1.2`, ten face spins `j=1` (`two_j=[2]*10`), `Dl=0`; primary five intertwiners `i=0` (`two_i=[0]*5`), held-out five intertwiners `i=1` (`two_i=[2]*5`). Each tuple was evaluated twice.
- frozen numerical acceptance: normal execution, finite real outputs, repeat difference <= `1e-12*max(1,abs(A))`; no sign/magnitude/ratio target.

## Original control lanes

Original run `34808304690`:

- vertex-face-map job `103864431152` — PASS; artifact `10333498333`, digest `sha256:dfc5e769515fca0a036284cca9892a8fe70c80d3ef7b6d59042b4e809ed15094`
- backend-source-control job `103864431342` — PASS; artifact `10333199568`, digest `sha256:98025c30ff53a8c3c0f26e75630e8d5d8355b82bd13b45f2f22874e0ee17ac88`
- semantic-null job `103864431377` — PASS; artifact `10334041954`, digest `sha256:d3dd2c1691e52672897e798add45f0ce96f3542b56799f4089e91a91136af31c`
- aggregate job `103864534957`; artifact `10333957322`, digest `sha256:6e00d6169a54fbd7382eb6981a5fa13c59fcb5ecc31c134fe1a5fa84c7fc388f`

The original numerical job `103864431259` failed pre-science during parallel test linking. No amplitude was evaluated.

## Minimal infrastructure recoveries

1. Build-order-only repair commit `3b770691c33385cf10a6007d260db6f589d5dac0`; run/job `34808387189 / 103864666854`. It built library and tools but failed pre-science because the runtime loader could not locate `libsl2cfoam.so`.
2. Loader-path-only repair commit `e7e41d348296d49ccd565befbd20b4ab0a77778a`; authoritative numerical recovery run/job `34808487683 / 103864955774`; artifact `10333568519`, digest `sha256:aee4671294bc669d57a63d14276f5ec70187f4d4aeaa0be953d331b740e2585e`.

Neither recovery altered backend source, compiler science flags, Y-map, spins, intertwiners, shell cutoff or thresholds.

## Raw numerical evidence

Authoritative recovery artifact reports:

- primary #1: `6.68473838546e-11`
- primary #2: `6.68473838546e-11`
- held-out #1: `1.77486269381e-10`
- held-out #2: `1.77486269381e-10`
- all finite: true
- primary repeat PASS: true
- held-out repeat PASS: true
- scientific_pass: true
- classification: `NUMERICAL_SMOKE_PASS`

The values were not compared to any post-hoc target; their sign or relative magnitude carries no gate credit.

## Consequence

The exact pinned Lorentzian EPRL single-vertex object is executable and deterministic on both prospectively frozen primary and held-out intertwiner tuples. Together with ITER044 source-map qualification and ITER045 1→5 implementation readiness, this authorizes a separate prospectively preregistered multi-vertex assembly-authority gate.

It does **not** by itself authorize a full ten-bulk-face sum, claim shell convergence, prove Pachner/refinement invariance or earn bridge credit.

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory = `0 / UNFORMED`.

## Exact next allowed gate

Before a five-vertex contraction, source-qualify and mechanically map the full 5→1 vertex-renormalization amplitude formula: face/edge/vertex factors, internal spin/intertwiner summations, local vertex argument ordering and boundary/internal incidence. In parallel, a bounded backend shell-transport diagnostic may run with inputs frozen prospectively. Only after that assembly map closes may a bounded multi-vertex contraction be preregistered.
