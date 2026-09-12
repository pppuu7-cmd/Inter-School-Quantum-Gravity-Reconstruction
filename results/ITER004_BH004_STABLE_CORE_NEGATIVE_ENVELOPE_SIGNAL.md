# ITERATION 004 — BH-004 Stable-Core Negative Result and Transport-Envelope Signal

Date: 2026-09-12  
GitHub Actions run: `34664913496`  
Status: `SUCCESSFUL EXECUTION / PREREGISTERED STABLE-CORE GATE FAILED / TRANSPORT-ENVELOPE SIGNAL`

## Question

Can the weak principal-direction tail observed in the first BH-004 three-level holdout be removed by a single source-geometric singular-value threshold learned on disjoint training seeds, then frozen and tested at a fourth nested scale?

## Design

Nested levels:

`p0=1`, `p1=0.75`, `p2=0.5625`, `p3=0.421875`.

Training used only:

- sizes `N=512,768,1024`;
- seeds `401,402,403,404`;
- transitions `p0->p1` and `p1->p2`;
- source-subspace geometry only;
- no closure target and no held-out `p3` information.

For a grid `tau=0.50..0.975`, the parent source sector was canonically restricted to the child subset, SVD-decomposed, and directions with `s/s_max >= tau` retained. One global threshold was frozen by minimizing median normalized projector distance to training child source sectors.

The training-only choice was

`tau = 0.525`.

Testing used completely disjoint seeds `501,502,503,504` at the unseen fourth level `p3`, again for all three sizes. There were `12` held-out jobs.

## Preregistered gates

Natural support required all of:

- median mean principal cosine `>0.92`;
- median minimum principal cosine `>0.25`;
- retained rank fraction `>=0.50` of source rank;
- median stable-core / unpruned projector-distance ratio `<0.95`;
- median leakage and sequential closure gains over rank-matched random `>1`;
- at least `2/3` jobs improve both closure metrics.

Strong support required stricter analogues, including distance ratio `<0.80`.

## Aggregate result

| quantity | held-out result |
|---|---:|
| frozen training-only threshold | `0.525` |
| held-out jobs | `12` |
| median mean principal cosine | `0.98773` |
| median minimum principal cosine | `0.86758` |
| median retained-rank / source-rank | `1.15` |
| median stable/unpruned projector-distance ratio | `1.000` |
| median random/stable leakage improvement | `3.08199x` |
| median random/stable sequential-defect improvement | `6.22814x` |
| jobs improving both closure metrics | `12/12` |
| preregistered natural support | **NO** |
| preregistered strong support | **NO** |

The preregistered gate fails specifically because the learned threshold does not improve normalized projector distance relative to the unpruned canonical restriction. The median ratio is exactly `1.0`.

## Why this is not a generic failure of BH-004

The held-out geometry and closure quantities are in fact substantially stronger than in the previous three-level rank-matched transport test:

- mean principal cosine is near `0.988`;
- minimum principal cosine is near `0.868` rather than near `0.081`;
- every held-out job beats rank-matched random controls on both closure metrics;
- median closure gains are about `3.08x` and `6.23x`.

The key difference is that the fourth-level transported restriction is **not forced to match the child source rank**. It retains a median dimension about `15%` larger than the source sector.

Thus the negative result falsifies the simple hypothesis

> an unstable directional tail should be identified and removed by a universal restriction-singular-value threshold.

It does **not** falsify projector-aware transport.

## Transport-envelope interpretation

The data support a different structural possibility:

> the canonically transported parent physical sector may define a slightly overcomplete **transport envelope** at the child scale, inside which the child source-defined physical sector lies with high principal-angle fidelity.

The envelope can preserve closure better than a prematurely rank-matched transported projector even though it contains extra directions.

This explains the apparent tension between the two BH-004 campaigns:

1. **three-level rank-predicted transport:** correct approximate rank, useful closure, but low minimum principal cosine;
2. **four-level unpruned/envelope transport:** overcomplete rank, much stronger all-direction alignment and closure.

The difference suggests that rank reduction and orientation transport should not be collapsed into one operation.

## Revised structural decomposition

A more defensible bridge architecture is now

`P_parent --canonical transport--> E_child --local physical selector--> P_child`,

where

- `E_child` is an overcomplete transported envelope;
- the local selector is determined by child-scale source-native measure/constraint data, not by held-out closure optimization.

This is compatible with the earlier BH-004 separation between projector orientation and `mu_s` scale/measure flow, but is more precise: `mu_s` or another source-native child datum may select the physical subspace **inside** a transported orientation envelope.

## Critical caution

High mean/minimum principal cosines when the envelope dimension exceeds the source rank show that the child source sector is well contained in the envelope; they do not prove that the extra envelope directions are physically harmless.

The next gate must therefore test whether a source-native child-scale selector can remove the extra directions without seeing the closure target and without reproducing the source projector by construction.

## Decision

- `STABLE_CORE_UNIVERSAL_SINGULAR_THRESHOLD`: **REJECTED in current form**.
- `BH-004_PROJECTOR_AWARE_TRANSPORT`: **remains supported at natural level**.
- `TRANSPORT_ENVELOPE + LOCAL_SELECTOR`: **admitted as the next falsifiable refinement, not yet accepted**.
- `NEW_PHYSICS`: **NOT ESTABLISHED**.
- `CANDIDATE_QG_THEORY`: **UNFORMED**.
