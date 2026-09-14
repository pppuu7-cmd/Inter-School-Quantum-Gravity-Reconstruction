# Preregistration — ITER053 Lorentzian five-vertex phase/weight authority

Date frozen: 2026-09-14

## Inherited terminal state

ITER051 is terminal `LORENTZIAN_PINNED_BACKEND_RUNTIME_PASS`.
ITER052 is terminal `LORENTZIAN_LOCAL_VERTEX_ARGUMENT_CROSSWALK_AUTHORITY_PASS`.

No five-vertex amplitude value is authorized until the phase, face-weight and intertwiner-dimension conventions are source-qualified.

## Scientific/source question H053

Can the exact paper Eq.(11), pinned authors' executable implementation, and pinned `sl2cfoam-next` normalization be reconciled into one executable fixed-summand phase/weight convention **without amplitude fitting**, with any remaining discrepancy reduced to an explicit boundary-only phase independent of all bulk spins/intertwiners?

Prospectively frozen hypothesis:

1. the author-code face exponent `weight` is the same model deformation parameter as paper `mu`, so the standard paper amplitude is `mu=weight=1`;
2. the paper internal-edge product `prod_{e=1}^{15}(2 i_e+1)` is reproduced by half-dimension factors distributed between the five backend vertex tensors and the five recoupling Wigner-6j matrices, not by an additional manual edge-dimension multiplier;
3. multiplying author-code `df_phase`, all five recoupling phases, and all five final-contraction phases differs from the literal Eq.(11) `(-1)^chi` by exactly the boundary-only factor `(-1)^(2 j_b)`, with no dependence on `j1...j10` or `i1...i15`;
4. the reduced-Euclidean RC006 parameter `alpha` from ITER010 is a different source/model normalization parameter and must not be identified with Lorentzian paper `mu`.

No outcome may change these frozen targets.

## Frozen authorities

### Paper source object

`sources/ITER053_PHASE_WEIGHT_DATA.json`, blob `9b668b4b8ad749cb45eadd7b78434d9c1cd64bbb`, extracted from the already authoritative ITER048 raw source:

- arXiv `2302.00072`;
- exact `main.tex` SHA256 `bff93f3a7857658264a04eb23521bb935a68eccb7760b284589ff5ec4073f063`;
- raw-TeX artifact `10334723630`, digest `sha256:191262f0c2a6d5c5b3ac6f1036caacd6808735c4bc38ecc73c45da49b2c53cb9`.

Frozen paper statements:

- `A_e(i_e)=2i_e+1`;
- standard `A_f(j_f)=2j_f+1`;
- Eq.(11) includes `prod_{f=1}^{10}(2j_f+1)` and `prod_{e=1}^{15}(2i_e+1)`;
- Eq.(11) phase `(-1)^chi` with `chi=sum_{k=1}^{10}j_k + sum_{k=11}^{15}i_k`;
- deformation `A_f=(2j_f+1)^mu`, with `mu=1` explicitly the standard case.

### Pinned author code

`PietropaoloFrisoni/Monte_Carlo_spinfoams@84b375f2a2e0d29b44dd8820953553624bb007a3`:

- EPRL MC `src/vertex_renormalization_EPRL_MC.jl`, blob `6b627f7c2329724b589947195edc7e5ee7c18bb1`;
- BF exact control `src/vertex_renormalization_BF.jl`, blob `6ce6a9cb31db931bb3491932edfe1828d0852091`;
- utilities `src/utilities.jl`, blob `7dddb9e34156264c2b599f74ed38853a2799ddb0`.

### Pinned backend normalization

`qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`:

- `src/vertex.c`, blob `9581999f0d5d59155e8c912fc7f2f3c5a98b346e`;
- `src/b4.c`, blob `ccbe7d907ff5c04fd876343b6e732759064567c8`.

### Alpha firewall

`prereg/ITER010_RC006_EPRL_ALPHA_MEASURE_FAMILY_GATE.md` defines `alpha` only for the reduced Euclidean `SU(2)_k x SU(2)_k` source-normalization family through q-dimensions. It is not a Lorentzian paper parameter and must not be imported into this gate.

## Frozen phase decomposition

Using the exact ITER052 source-name crosswalk, the five author-code Wigner recoupling phase exponents are frozen as:

- up: `jb + j3 + j6 - j5`;
- left: `jb + j1 + j3 - j2`;
- bottom-left: `jb + j7 + j1 - j8`;
- bottom-right: `jb + j7 + j10 - j4`;
- right: `jb + j10 + j6 - j9`.

The five final-contraction phase exponents are frozen as:

- up: `jb + j6 + i12`;
- left: `jb + j3 + i13`;
- bottom-left: `jb + j1 + i11`;
- bottom-right: `jb + j7 + i14`;
- right: `jb + j10 + i15`.

The global author-code face phase is frozen as:

`df_phase = (-1)^(2*(j1+...+j10))`.

The gate must derive the total executable phase symbolically from these exact terms. It may not infer the relation from numerical amplitude signs.

## Frozen dimension accounting

Use the ITER052 original local vertex incidence mapping and Wigner pairs.

Backend source must independently establish:

- the 15j kernel supplies `sqrt(DIM(i1)*DIM(k2)*DIM(k3)*DIM(k4)*DIM(k5))`;
- each B4 supplies `sqrt(DIM(i)*DIM(k))`;
- hence each returned physical vertex component carries `sqrt(prod_{a=1}^{5} DIM(i_a))` in its five external physical intertwiner labels.

Each author-code recoupling matrix supplies `sqrt(DIM(i_left)*DIM(i_right))`.

The dimension lane must show that every global `i1...i15` has total exponent exactly `1` after combining the five original vertex half-dimensions with the five recoupling half-dimensions. Any extra manual `prod(2i+1)` would therefore double count.

## Independent lanes

1. `paper-authority` — verify frozen paper formulas/provenance and standard `mu=1` semantics.
2. `author-code` — verify exact `dfj`, `df_phase`, five recoupling phases/dimension square roots, five final phases, and `dfj^weight` semantics from the pinned code; BF exact code is the standard-weight control.
3. `backend-normalization` — verify exact pinned 15j/B4 dimension half-factors and establish per-vertex external `sqrt(prod DIM(i_a))` normalization.
4. `symbolic-crosswalk` — derive phase ratio and global intertwiner-dimension exponents from frozen source mappings only.
5. `null-controls` — require rejection of at least: (a) importing RC006 `alpha=mu`; (b) adding a second manual full edge-dimension product; (c) omitting `df_phase`; (d) omitting one frozen recoupling phase. The latter two must produce bulk-dependent phase mismatch on a pre-frozen admissible parity panel rather than the allowed boundary-only factor.

No lane may evaluate a Lorentzian vertex amplitude.

## Pre-frozen parity panel for null controls

Use doubled labels only for sign algebra. Test all combinations generated by:

- `2jb in {0,1,2}`;
- ten internal doubled spins independently drawn from the two deterministic patterns
  - P0: `(1,1,1,1,1,1,1,1,1,1)`;
  - P1: `(1,2,1,2,1,2,1,2,1,2)`;
- inner doubled intertwiners `(2i11,...,2i15)` from
  - Q0 `(0,0,0,0,0)`;
  - Q1 `(0,2,0,2,0)`.

Only combinations for which every frozen code phase exponent is integral are used in sign comparison. This panel is frozen before execution and is not selected by output.

## Frozen PASS criteria

`PAPER_AUTHORITY_PASS`: all paper formula identities and provenance match the frozen source record.

`AUTHOR_CODE_PASS`: every frozen code formula/sign/dimension signature is present under exact source identity; code clearly makes face exponent `weight` act on `dfj`, while BF exact control uses `dfj` to the first power.

`BACKEND_NORMALIZATION_PASS`: exact backend sources contain the frozen 15j and B4 half-dimension factors sufficient to establish external per-vertex square-root edge normalization.

`SYMBOLIC_CROSSWALK_PASS` iff:

- executable total phase minus paper `chi` simplifies exactly to `10*jb + 4*(j1+j3+j6+j7+j10)`;
- its sign simplifies for half-integer labels to the boundary-only factor `(-1)^(2jb)`;
- coefficients of every bulk `j1...j10` and `i11...i15` in the residual sign vanish modulo even integers;
- global intertwiner dimension exponent equals exactly `1` for all `i1...i15`;
- Lorentzian `weight` is identified with paper `mu`, standard production choice `mu=weight=1`.

`NULL_CONTROLS_PASS`: alpha-import and double-edge-dimension variants are structurally rejected, and omitted-phase variants fail the boundary-only-residual condition on at least one valid frozen parity-panel point.

## Terminal classifications

- `LORENTZIAN_PHASE_WEIGHT_AUTHORITY_PASS_BOUNDARY_PHASE_QUALIFIED` iff all lanes PASS and the only paper↔executable phase mismatch is exactly `(-1)^(2jb)`.
- `LORENTZIAN_PHASE_WEIGHT_BLOCKED_SOURCE_NORMALIZATION` if edge/face normalization cannot be source-mapped uniquely.
- `LORENTZIAN_PHASE_WEIGHT_BLOCKED_PHASE_CONVENTION` if a source-qualified but bulk-dependent phase mismatch remains.
- `LORENTZIAN_PHASE_WEIGHT_STRUCTURAL_FAIL` if exact source identities contradict the frozen accounting.
- `INVALID_IMPLEMENTATION` or `INVALID_PROVENANCE` as appropriate.

## Interpretation / authorized successor

A PASS does **not** erase the explicit boundary-phase difference. It authorizes a separately preregistered bounded five-vertex fixed-configuration gate only if that successor freezes one of these two equivalent reporting conventions before output:

- `AUTHOR_EXECUTABLE_CONVENTION`: use author code phases exactly;
- `PAPER_EQ11_CONVENTION`: multiply the author-executable fixed summand by the prospectively declared conversion factor `(-1)^(2jb)`.

The successor must freeze standard Lorentzian `mu=weight=1`; it may not import RC006 `alpha`.

No unbounded sum, convergence, refinement-map, bridge, or candidate-theory claim follows from this gate.

## Claim locks

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory remains `UNFORMED / 0%`.

Still unauthorized: unbounded ten-face summation, shell convergence, coarse↔fine equality, zero-face deletion, full Eq.(27), Eq.(29)/Lambda, one-step TNR, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`.