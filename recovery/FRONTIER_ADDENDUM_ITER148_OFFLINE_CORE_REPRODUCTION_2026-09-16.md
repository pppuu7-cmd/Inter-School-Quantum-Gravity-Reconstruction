# ITER148 offline exact core reproduction — 2026-09-16

## Auto-research state consumed first

Before this iteration, the authoritative automated fronts were rechecked.

- ITER140 v6 run `35040499084` remained `queued`; its independent exact offline reproduction had already returned the frozen PASS classification, but official CI terminal authority remained open.
- ITER148 v3 run `35044099632` remained `queued`, with all 27 tau x design-chunk jobs still awaiting runner allocation.

No scientific conclusion was inferred from queue state.

## Independently formulated iteration

The next question was chosen without inspecting any future v3 chunk output:

> Can the frozen ITER148 v3 M3 computation be reproduced independently of GitHub Actions, using the same 45-element basis, deterministic design, tau grid, heldouts, routing/permutation/parity controls and ITER145 bubble maps, while preserving the frozen authority boundary for the pinned-source predicate B?

## Execution-path diagnosis and accelerator

The committed SymPy `-2*EH_GammaGamma` evaluator is exact but expensive. For the frozen M3 tensor allocation, the three cubic inputs have a fixed phase pattern:

- `X = P R1` is real;
- `Y = P chi1` is purely imaginary;
- `Z = P dR1` is purely imaginary.

The common phases can therefore be stripped analytically and the same Gamma-Gamma contraction evaluated entirely with exact `fractions.Fraction` arithmetic. This changes execution only, not the scientific object.

Exact controls before production:

- 4 independent numerator panels/tau values: Fraction evaluator = committed SymPy evaluator exactly, 4/4;
- per-numerator observed speedup: about 21.5x–25.0x;
- full `tau=1/8, chunk=0`: all 15 design values and all 3 training-heldout directs equal the SymPy v3 chunk exactly;
- chunk wall time improved from 28.13 s to 4.18 s in the local environment.

## Full v3 production reproduction

All 27 frozen `(tau_index, chunk_index)` outputs were generated exactly.

- 27/27 chunks completed;
- 0 chunk failures;
- 45-element basis retained;
- exact design rank certificate remains 45;
- deterministic scientific-payload SHA256 values for all 27 chunks are recorded in `analysis/iter148_offline_core_reproduction_certificate_2026-09-16.json`.

## Frozen core adjudication

Using the same nine training taus `0,1/8,...,1`, the exact 45 coefficient vectors were reconstructed and interpolated with the frozen degree ceiling.

Observed result:

- 42/45 invariant coefficient functions are nonzero;
- maximum realized tau degree is exactly 8;
- all training-tau invariant heldouts pass;
- all six no-refit heldouts at tau `1/3` and `2/5` pass exactly;
- routing, all leg permutations, parity and source-weight-at-tau=1 pass;
- ITER145 triangle identity passes;
- canonical bubble maps A/B/C pass.

Thus frozen checks A and C-K are independently reproduced as `true`.

The six no-refit direct values are:

- tau=1/3: `6676277/1458`, `10511216/2187`, `-1394939/243`;
- tau=2/5: `2627217609/1562500`, `369863706/390625`, `-4972126131/781250`.

## Independent pinned-source authority cross-check

The authoritative ITER147 artifact `10415677784`, artifact SHA256
`e5c5b016340c8bdcb7d06dd99bb6a364296fc18451760dcb38c95dbe5c251000`, was downloaded and used as an external authority lane.

Its pinned FeynGrav blob is `98297aac3b640a93ac80c2cc72a8275280819954`.

The Fraction M3 fast path agrees exactly with:

- all 44 values of the four frozen ITER147 affine-slice polynomials for lambda=0..10;
- all 8 genuinely withheld direct-source values at lambda=9,10.

ITER144 terminal authority independently established exact
`FeynGrav_source / independent_GammaGamma_cubic = -2` at commit
`5ee9043e36af2705ddea5553c6015d4552f94a32`.

This is strong auxiliary evidence for ITER148 predicate B, but it is **not substituted** for the three specific direct-source panels hard-coded in the frozen ITER148 aggregator.

## Predicate L

The separate immutable manual audit at
`1bfea2d5f9ac8baf248a173390c7b9b656c87f21` remains
`MANUAL_PREDICATE_L_PASS_SCOPED` and proves the A/B/C Jacobian powers and C sign. It does not by itself terminalize ITER148.

## Classification boundary

This iteration is recorded as:

`EXACT_CORE_PASS_B_SPECIFIC_THREE_PANEL_SOURCE_AUTHORITY_OPEN`

It deliberately does **not** assign
`PASS_SCOPED_M3_FULL_D4_INVARIANT_AND_CANONICAL_BUBBLE_REDUCTION_CLOSED_GENERAL_D_POLES_OPEN`.

Reason: the offline environment cannot retrieve the one-line pinned FeynGrav source blob directly, so the three exact direct-source panels of frozen predicate B were not rerun. The official v3 aggregate remains authoritative for that machine predicate; alternatively a later exact reproduction may close those same three panels using the pinned source.

No basis, tau grid, heldout, degree limit, bubble map, predicate, classifier or claim ceiling was changed after seeing results.

## Durable files

- `analysis/iter148_fraction_s3_accelerator.py`
- `analysis/iter148_offline_core_reproduction.py`
- `analysis/iter148_offline_core_reproduction_certificate_2026-09-16.json`
- `analysis/iter148_external_iter147_authority_certificate_2026-09-16.json`

## Claim ceiling

Full D=4 M3 invariant core and canonical bubble-map structure are independently reproduced. The three frozen direct-source B panels, official ITER148 terminal result, general-d/O(epsilon) continuation, master poles, endpoint subtraction, B1, EDT, bridge, new physics and candidate theory remain open.
