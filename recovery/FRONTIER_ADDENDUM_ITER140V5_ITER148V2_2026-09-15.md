# ISQGR recovery frontier addendum — ITER140 v3/v4/v5 and ITER148 v1/v2 active

Date: 2026-09-15
Repository: `pppuu7-cmd/Inter-School-Quantum-Gravity-Reconstruction`

Prefer this note over older additive recovery files for the current fixed-geodesic curvature branch. Candidate theory remains **UNFORMED / 0%**; bridge credit remains **0**.

## Latest terminal scientific result

ITER147 is terminal PASS:

`PASS_SCOPED_RATIONAL_S3_EVALUATOR_AND_M3_SLICE_REPAIR_CLOSED_FULL_INVARIANT_OPEN`.

Result commit: `f5246a44d5fccaec7f9c65333dcfa2ccaab21190`.
Run: `35016375562`; job: `104540719390`; artifact: `10415677784`; artifact SHA256: `e5c5b016340c8bdcb7d06dd99bb6a364296fc18451760dcb38c95dbe5c251000`.

The repaired exact rational S3 evaluator closes all four frozen M3 affine slices at realized degree exactly 8 with lambda=9,10 held-outs passing. ITER146's earlier FAIL is therefore localized to its integer-coercing evaluator implementation, not to a physical tensor/routing contradiction.

## ITER148 — frozen full M3 invariant/bubble gate, two implementations active

Preregistration: `f2d59b35ef3e943ee94484e479a4951a736356b1`.
Frozen target: exact 45-monomial D=4 invariant numerator, tau degree <=8 on the frozen 0,1/8,...,1 grid, no-refit tau=1/3 and 2/5 held-outs, direct rational pinned-source vs accelerated `-2*EH_GammaGamma` authority check, ITER145 routing/permutation/parity/source-weight controls, and all three exact canonical bubble maps with prefactors `tau^(3-d)/Q`, `(1-tau)^(3-d)/Q`, `-[tau(1-tau)]^(3-d)/Q`.

Single implementation:
- implementation `b7603dd0d6fbc78d266e12da52528c8169a097a6`;
- workflow head `a5f48c584e53d6af9f4ac2cdbe4c9d670eeff1c7`;
- run `35017383409`, job `104544128820`.

Parallel tau-shard implementation with identical frozen object/predicates:
- shard implementation `0d16ac9e935b4742a2b212fee9dd8fadc61826d7`;
- aggregator `687ade9bc3b8f7a494098cdf078327f853bba8a3`;
- workflow head `511591f0b8e68b23d2667b2e4bb6cd50579fc59f`;
- run `35018047575`.

The first scientifically terminal implementation may adjudicate ITER148; any later identical implementation is an independent computational confirmation, not a new scientific gate.

## ITER140 — frozen general-d Gaussian gate, implementation retries

Attempt 3 was already adjudicated `NUMERICAL_OR_INFRASTRUCTURE_FAIL` after D=3..10 direct contractions completed but postprocessing hit the 180-minute timeout. No scientific FAIL was inferred.

V3:
- implementation `03d2578c38b119e6a4b77d65a0206c101c5e99a1`;
- workflow head `3b73e61073412cc85540fedbe35ae618a3e7dab4`;
- run `35016456669`, job `104541005387`.

V4 dimension-parallel:
- dimension shard `032ff98c20c06344b9ce81c2a931a984fa564f7d`;
- aggregator `6434a0610761630c9ccbf1dabedcf1870a37dcc5`;
- workflow head `c166a8021fdb3a07764aa9ea3e7be6a283d6a2da`;
- run `35017861276`.

V5 family x dimension parallel:
- terminal D=4 authority manifest commit `6ec45b713d67cbe955241a54bc43990514982bbb`, copying exact held-out values from immutable successful ITER138/139 artifacts with their hashes;
- family-dimension shard `bb4117aa933f05ff856d661abf447aea608a3c41`;
- aggregator `f91d06c2ae923ff96fb735df2766e207f72e63ea`;
- workflow head `e93da64c6161cc6fbda6f10d6a57de0468976f2d`;
- run `35018417447`.

V5 changes no scientific predicate. It splits each D into the three frozen families and replaces expensive re-execution of ITER138/139 D=4 symbolic authority functions by exact comparison against their terminal artifact values:

- panel 1: M1 `15741/4`, M2 `-48893/8`, G1 `-4455/4`;
- panel 2: M1 `3306`, M2 `-8441`, G1 `-3030`;
- panel 3: M1 `-1341/2`, M2 `6463/4`, G1 `1215/2`.

Provenance hashes are pinned in `analysis/iter140_d4_terminal_authority_manifest.json`.

## Already-frozen immediate downstream gate

ITER143 was preregistered **before** ITER140 coefficients were inspected and its implementation already exists:

`ITER143_FIXED_GEODESIC_CURVATURE_FIRST_MG_DENOMINATOR_CANCELLATION_CONTACT_PARTITION`.

If and only if an ITER140 implementation returns

`PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN`,

immediately feed that exact JSON to the frozen ITER143 implementation. Do not alter ITER143 support/contact rules based on the observed coefficients.

## Exact next actions

1. Consume the first terminal ITER140 retry. If PASS, terminalize ITER140 and run frozen ITER143 immediately. If infrastructure-only, prefer the already queued finer implementation rather than raising a timeout again.
2. Consume the first terminal ITER148 implementation. If PASS, terminalize and preregister M3 general-d/O(epsilon) continuation of the full invariant/canonical-bubble representation. If FAIL, apply the preregistered exact failure class without basis/degree enlargement.
3. No B1, noncancellation, EDT match, bridge, new physics or candidate-theory claim is authorized until general-d numerators, denominator/contact partition, master poles, required subtraction sectors and ITER124 projected genuine-defect assembly all close.
