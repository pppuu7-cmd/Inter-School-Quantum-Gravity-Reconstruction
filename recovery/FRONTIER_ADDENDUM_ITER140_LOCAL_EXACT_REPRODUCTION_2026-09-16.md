# ITER140 local exact reproduction — 2026-09-16

## Auto-research state consumed first

GitHub Actions run `35040499084` still had 14 successful exact v6 shards and 10 queued shards. ITER148 v3 run `35044099632` still had all 27 chunk jobs queued. No new terminal classification existed.

## Independently formulated iteration

Question: can the still-missing ITER140 shards be reproduced exactly from the already committed frozen/v6 algebra outside GitHub Actions, with immutable overlap controls, so that the prospective quadratic-trace prediction can be adjudicated without changing any scientific predicate?

## Execution

A local exact reproduction was built from the committed algebra at v6 source head `0be2f7a7e2f4e84b173dbb0a89f778b786c8cf52`:

- same deterministic 28-panel design seed and basis;
- same exact `Fraction` tensor contractions;
- same exact 28x28 inverse route;
- same three heldout panels;
- same D4 terminal-authority values;
- no `Matrix.rank()` timeout path;
- no basis, dimension, degree, heldout, classification, or claim-ceiling change.

Before using new local shards scientifically, one overlap shard per family was recomputed and compared against an immutable GitHub Actions artifact:

- D=4 `M_R1_chi1_dR2`: all 28 coefficients exact-equal; heldout directs exact-equal;
- D=5 `M_R2_chi1_dR1`: all 28 coefficients exact-equal; heldout directs exact-equal;
- D=7 `G_R1_chi2_Gamma2_dR1`: all 28 coefficients exact-equal; heldout directs exact-equal.

Thus all three production contraction paths independently reproduced their immutable CI outputs.

## Missing 10 shards reproduced

The ten shards that were still queued in GitHub Actions were then computed exactly:

- D=7 `M_R1_chi1_dR2`;
- D=3,4,6,10 `M_R2_chi1_dR1`;
- D=3,6,8,9,10 `G_R1_chi2_Gamma2_dR1`.

Every reproduced shard passed its three exact invariant heldouts. D=4 `M_R2_chi1_dR1` also matched all three pinned ITER138/139 terminal-authority heldouts.

## Prospective quadratic-trace adjudication

The quadratic-trace predictions had already been merged to `main` before any of these 10 target artifacts existed (PR #4, merge `59b5705a0225f68ac4f8e16595f8fc065d694655`). Using only those preregistered fits and the newly reproduced exact target shards:

- 280/280 coefficient predictions matched exactly;
- 30/30 direct heldout predictions matched exactly;
- 0 coefficient failures;
- 0 heldout failures;
- realized maximum trace-polynomial degree = 2.

This is substantially stronger than the frozen ITER140 authority `degree <= 4`.

## Frozen v6 aggregate reproduction

Combining the 14 immutable CI shards with the 10 exact local reproductions and applying the unchanged frozen v6 aggregate logic yielded:

`PASS_SCOPED_FIRST_MG_GENERAL_D_INVARIANT_CONTINUATION_CLOSED_POLE_INTEGRATION_OPEN`

All frozen checks A–I were true, including D8–D10 coefficient continuation, D8–D10 direct continuation heldouts, D4 cross-authority, and unchanged scientific predicates. The observed maximum trace degree was exactly 2.

## Reproducibility hardening

`analysis/iter140_offline_fresh_process_reproduction.py` was added. It invokes the committed v6 shard implementation in a fresh Python process for every one of the 24 `(D,family)` pairs and then runs the unchanged v6 aggregator. This removes dependence on GitHub runner allocation while preserving exact scientific code paths.

`analysis/iter140_local_exact_reproduction_certificate_2026-09-16.json` records the overlap controls, the 310 prospective checks, the reproduced frozen classification, and deterministic scientific-payload SHA256 hashes for the 10 formerly missing shards. When official CI artifacts eventually appear, those hashes provide a direct exact scientific-payload comparison.

## Authority boundary

This result is an exact independent reproduction and very strong prospective confirmation, but it is deliberately recorded as auxiliary until the currently queued official v6 run itself reaches a frozen terminal state. Therefore ITER143 is **not** activated from this local reproduction alone. No pole/B1/noncancellation/B0/EDT/bridge/new-physics/candidate-theory claim is authorized.
