# ITER039 — RC006 Eq.(27) bounded central component closure

Date: 2026-09-14

## Terminal classification

**SCIENTIFIC FAIL — `RC006_EQ27_BOUNDED_CENTRAL_COMPONENT_CLOSURE_FAIL`**.

This is a failure of the prospectively frozen ITER039 component-closure gate, not an infrastructure failure and not a claim that RC006 or a QG school is globally false. Frozen thresholds, domains, conventions and held-out handling are unchanged after seeing the result.

## Provenance

- preregistration: `b40ff1765bd5c5c73f578a943dca72ea031f08e4`
- implementation: `d05819e58f86994e08043708d67b465a343a48c1`
- production/workflow head: `bb21fda2081ca81a691bf58cac2073645201b17f`
- authoritative run: `34806079470`
- jobs: C `103858118898`; B `103858118927`; D `103858118961`; A `103858119040`; aggregate `103858164412`
- artifacts:
  - A `10333335305`, `sha256:2632c0ea533c5cfd8ff49afe4a62a64b90c997458356a2c547bfa2c458aa0d8a`
  - B `10332773120`, `sha256:e623d7becf09b9457285cf82fdd1ede3c5d148800976f7569c2fbe614e6a740d`
  - C `10332763097`, `sha256:9edf37d3af5865f4d5e070d4b183b888cc7701eda87ac28a35754ee525cadf82`
  - D `10333315434`, `sha256:e1fb173d7786e0c4152d35a2d111567ea0ae5f2cc13dd1a6aa0eff1dc98ea12a`
  - aggregate `10333415213`, `sha256:abc8db20556142a54f467311268f061cb21eb5dbf857994788f5ed74f2974807`

## Raw frozen-gate outcome

Lane A PASS: source/provenance/domain panel is complete, with 2 primary and 2 held-out cases and finite central-domain sizes 17, 37 (primary) and 19, 77 (held-out).

Lane D PASS: all 3/3 preregistered invalid constructions are detected. On the frozen nontrivial tuple `(k=6,J+=1,J-=2,l=1)`, legacy-qbar difference is `1.1892071150027208`, R versus R^-1 difference is `2.613125929752755`, and the first outside-domain central label is rejected.

Lane B FAIL: 54 primary central tuples were evaluated without retuning; 7 fail at least one frozen numerical predicate. Representative exact failure: `(k=6,J+=2,J-=2,l=0)` has R/R^-1 residual `16.48528137423864` against the frozen `5e-8` threshold while qbar identity/intertwiner and dual residual remain small. Other primary failures at `k=12` include large dual-contraction residuals up to `0.7137917357844189`.

Lane C FAIL: 96 held-out central tuples were evaluated with the identical code and thresholds; 23 fail. The maximum held-out R/R^-1 residual is `2349.968022439629`; maximum dual-contraction residual is `0.7137917357844189`. The direct-source qbar identity remains zero in the recorded rows and the qbar-intertwiner residual remains below its frozen `5e-9` threshold.

Therefore the failure is not a simple qbar-identity failure and cannot be repaired by threshold relaxation, phase fitting, normalization fitting, tuple pruning, or held-out retuning.

## Scientific interpretation lock

ITER039 demonstrates that the previously validated local primitives do **not** extend unchanged over the entire newly authorized ITER038 central `(J+,J-,l)` domain under the frozen closure predicates. In particular, both the full-space R/R^-1 inverse check and, for some k=12 channels, the dual-contraction identity fail on the expanded central panel.

This may reflect a restricted prior validation domain, root-of-unity trace-zero/quotient structure, or another source/convention boundary; ITER039 itself does not choose among those explanations. No failed tuple is removed post hoc.

A next diagnostic may only map the failure to already published/validated domain assumptions and quotient/trace-zero structure. It may not redefine ITER039 or weaken its thresholds.

## Claims/readiness

Programme readiness remains **49%**. Candidate theory remains **0% / UNFORMED**. Bridge credit remains zero.

Still false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `BRIDGE_DERIVED`.
