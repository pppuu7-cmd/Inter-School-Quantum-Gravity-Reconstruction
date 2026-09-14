# Preregistration — ITER055 Lorentzian recoupling minipanel transport

Date frozen: 2026-09-14

## Inherited terminal state

ITER054 is terminal **SCIENTIFIC PASS — `LORENTZIAN_BOUNDED_FIVE_VERTEX_FIXED_SUMMAND_VALIDATED_SCOPED`**, run `34821111285`, production head `1fd40c077cc25dd12573f683fb457b7180f63e46`.

This successor does not change `gamma`, `Dl`, face weight, backend, source mapping, phase convention, thresholds, or normalization.

## Scientific question

Do the same source-faithful bounded five-vertex construction and exact pinned runtime transport without retuning to the two remaining elementary recoupling classes not numerically exercised in ITER054: every pair `1->0` and every pair `1->1`?

The objective is held-out transport across the complete 2x2 low-spin recoupling basis classes. ITER054 already exercised `0->0` and `0->1`; those sectors are not recomputed here.

## Frozen machine object

`sources/ITER055_LORENTZIAN_RECOUPLING_MINIPANEL_CALL_MAP.json`, git blob `370d21534b1d6529f189a55073bd0bbd481a4784`, created before any ITER055 amplitude output.

It freezes two new sectors:

- `R10`: `ib=0`; each recoupling pair `(i1->i2),...,(i9->i10)` is `1->0`; `i11...i15=0`; every local backend `two_i` call is `[0,0,0,0,2]`; exact Wigner recoupling factor at each of five pairs is `-sqrt(3)/2`; final signs are all `-1`.
- `R11`: `ib=1`; all `i1...i15=1`; every local backend `two_i` call is `[2,2,2,2,2]`; exact Wigner recoupling factor at each pair is `-1/2`; final signs are all `+1`.

Common frozen inputs: all ten internal/boundary local spins remain physical `1/2`, `gamma=1.2`, `Dl=0`, `mu=weight=1`, author executable convention, `A_paper=-A_author`, `df_phase=+1`, face factor `1024`.

## Frozen runtime

Reuse exactly ITER051 runtime artifact from run `34818301950`, artifact `10336669907`. Required hashes are unchanged from ITER054:

- vertex binary `b4f8f536645b3fe6bc55830040f624140eefca02a3b960b9940b2564a7876e26`;
- library `a539c968afde2a7ec397b2fa7184f9dd036042b82ff2ec5d8026c2b6881b71fc`;
- `.3j` table `73d9170de4f04b776923106c5c6ea1bbb70cf2e62a14d24b83cda31194567e6e`;
- `.6j` table `de1a29d0252c3c1ebf51b96d7fdebe7f21587ee65dcbc3864070774c14704b72`.

No rebuild or alternative runtime is authorized inside substantive lanes.

## Independent lanes

Run with `fail-fast:false`:

1. `map-and-symbolic-controls`: verify immutable map blob, derive the two local call tuples from frozen global mappings, and independently reproduce exact Wigner factors `-sqrt(3)/2` and `-1/2` plus frozen final signs.
2. `runtime-identity`: transport ITER051 artifact and verify all exact hashes.
3. `R10-A` and 4. `R10-B`: independent fresh-process replicas; each executes the five pinned local backend calls and computes the exact author/paper fixed summand.
5. `R11-A` and 6. `R11-B`: same for R11.
7. `null-controls`: reject `two_i=1` for physical `i=1`, any reuse of ITER054 amplitudes instead of executing new calls, any changed `gamma/Dl/weight`, second manual edge-dimension product, or output-dependent sign/normalization.

## Frozen formula

For both sectors:

`A_author = prod(V_v) * prod(W_r) * prod(S_v) * 1 * 1024`.

`A_paper = -A_author`.

No other factor is permitted.

## Frozen numerical predicates

Each substantive replica must:

- execute all five backend calls with return code zero;
- produce five finite parseable doubles;
- use exactly the machine-object `two_i` calls;
- compute finite `A_author` and `A_paper`;
- preserve runtime hashes and all science inputs.

Replica reproducibility, unchanged from ITER054:

For each local vertex:

`|x_A-x_B| <= 1e-15 + 1e-10*max(|x_A|,|x_B|)`.

For each author/paper summand:

`|A_A-A_B| <= 1e-60 + 1e-10*max(|A_A|,|A_B|)`.

No sign, ratio, magnitude, R10-vs-R11 relation, or relation to ITER054 values is a PASS target.

## Classification

**SCIENTIFIC PASS — `LORENTZIAN_RECOUPLING_MINIPANEL_TRANSPORT_PASS_SCOPED`** iff all control/runtime/substantive lanes PASS and both A/B reproducibility predicates PASS.

**SCIENTIFIC FAIL — `LORENTZIAN_RECOUPLING_MINIPANEL_REPRODUCIBILITY_FAIL`** only if the exact frozen objects execute but an A/B reproducibility predicate fails.

`BLOCKED_RUNTIME_TRANSPORT` if the exact ITER051 artifact cannot be transported.

`BLOCKED_SOURCE_OBJECT` if an exact source/map prerequisite cannot be established without changing the frozen contract.

`INVALID_IMPLEMENTATION` if a lane changes inputs, substitutes prior output, omits a required call, changes a convention, or adds forbidden normalization.

Infrastructure failure before scientific evaluation is nonphysical.

## Interpretation ceiling

PASS completes only a four-class low-spin fixed-summand transport panel when combined with ITER054. It still does not establish the full internal sum, shell convergence, coarse↔fine equality, zero-face deletion, refinement invariance, a derived refinement map, bridge credit, continuum/GR recovery, or candidate theory.

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory remains `UNFORMED / 0%`.

Claim locks remain unchanged.