# Preregistration — ITER050 Lorentzian bounded fixed-configuration five-vertex contraction

Date frozen: 2026-09-14

## Inherited terminal state

ITER049 is terminal SCIENTIFIC PASS — `LORENTZIAN_AUTHOR_CODE_ROUTING_RECONCILIATION_PASS`, authoritative run `34811866640`, durable result commit `5d3d480196c0525701996b56a799034a7f498778`.

The route is now source-qualified structurally: the executable author code uses `rbl/rbr` for the fourth 6j and `rCDl/rCDr` for the fifth. Under the exact source comment crosswalk this selects `COMMENT_REPAIR`, i.e. the fifth 6j uses `i9`, not duplicated `i8`.

ITER048 remains historically SCOPED BLOCKED. No result in ITER050 may retrofit ITER048.

## Frozen scientific question

Can the source-qualified five-vertex Lorentzian EPRL assembly be evaluated as a **bounded fixed-configuration summand** on the two sectors frozen in ITER048, with no retuning and no unbounded internal-face summation?

This is a local summand/executability gate. PASS does not establish a refinement map, convergence, coarse↔fine equality, or bridge derivation.

## Frozen authority panel

1. exact arXiv `2302.00072` source, `main.tex` SHA256 `bff93f3a7857658264a04eb23521bb935a68eccb7760b284589ff5ec4073f063`;
2. author code `PietropaoloFrisoni/Monte_Carlo_spinfoams@84b375f2a2e0d29b44dd8820953553624bb007a3`;
3. Lorentzian EPRL backend `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`;
4. ITER049 route: `COMMENT_REPAIR` only. `TEX_LITERAL` is a frozen null control and may not be substituted after results.

## Frozen sectors

Exactly inherited from ITER048:

- boundary `jb=1/2`;
- Immirzi `gamma=1.2`;
- shell `Dl=0`;
- primary: `j1..j10=1/2`, `ib=0`, `i1..i15=0`;
- held-out: `j1..j10=1/2`, `ib=1`, `i1..i15=(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0)` in order `i1...i15`.

No spin, intertwiner, shell, gamma, phase convention, normalization, or route may be changed after output is observed.

## Frozen computation object

For each sector:

1. evaluate the five source-defined Lorentzian EPRL vertex tensors/amplitudes at `Dl=0` using the pinned backend and source-defined ten-spin/five-intertwiner argument lists;
2. evaluate the five SU(2) recoupling 6j factors with the ITER049-reconciled route;
3. evaluate the source-prescribed phase and finite face/intertwiner dimension weights for that one fixed configuration;
4. contract/multiply only that fixed configuration into one bounded five-vertex summand.

No sum over the ten internal spins is allowed. No shell sweep is allowed.

## Independent lanes (`fail-fast:false`)

1. `authority-freeze`: mechanically verify pinned SHAs, exact sector constants, and the ITER049 route before any numerical result is used.
2. `primary-summand`: evaluate the primary fixed configuration only.
3. `heldout-summand`: independently evaluate the held-out fixed configuration using identical implementation and no retuning.
4. `null-controls`: evaluate structural nulls only: reject `TEX_LITERAL` duplicated-i8 routing, reject any changed gamma/Dl/sector, and verify that no amplitude-based selector is called.

An optional backend-build/setup failure before the vertex values are evaluable is `INFRASTRUCTURE_FAIL`, not scientific FAIL.

## Frozen PASS predicates

`AUTHORITY_FREEZE_PASS`: exact source/code/backend SHAs and exact inherited sectors match preregistration; `COMMENT_REPAIR` is the only production route.

`PRIMARY_SUMMAND_PASS`: all five Lorentzian vertex evaluations required by the primary fixed configuration return finite values/tensor entries and the recoupling/phase/weight factors are finite, yielding a finite bounded summand. Zero is allowed.

`HELDOUT_SUMMAND_PASS`: same predicate on the held-out sector, with no code/parameter retuning. Zero is allowed.

`NULL_CONTROLS_PASS`: duplicated-i8/TEX_LITERAL is not used in the production contraction; no route is chosen by magnitude/sign/agreement; no forbidden sector or parameter mutation occurs.

## Terminal outcomes

- `LORENTZIAN_BOUNDED_FIXED_CONFIGURATION_CONTRACTION_PASS` iff all four predicates PASS.
- `LORENTZIAN_BOUNDED_FIXED_CONFIGURATION_CONTRACTION_SCIENTIFIC_FAIL` if the frozen, successfully executed contraction is non-finite or violates a frozen scientific predicate.
- `LORENTZIAN_BOUNDED_FIXED_CONFIGURATION_CONTRACTION_BLOCKED` if a source-required contraction object cannot be mapped unambiguously despite successful transport.
- `NUMERICAL_FAIL` for reproducible numerical breakdown after the source-qualified object is instantiated.
- `INFRASTRUCTURE_FAIL` for dependency/build/transport failure before scientific predicates are evaluable.

## Consequence of PASS

PASS authorizes only a separately preregistered bounded mini-panel over additional **pre-frozen** fixed configurations or a source-faithful refinement-map test if a genuine map object is available. It does **not** authorize unbounded ten-face summation, shell-convergence claims, zero-face deletion, coarse↔fine equality, or bridge credit.

## Claim locks

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `0 / UNFORMED`.

Do not assert `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, or `BRIDGE_DERIVED`.