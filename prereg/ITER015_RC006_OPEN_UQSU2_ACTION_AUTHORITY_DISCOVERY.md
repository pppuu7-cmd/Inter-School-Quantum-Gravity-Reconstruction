# Iter015 preregistration — open Uq(su2) representation-action authority discovery

Frozen before implementation/production.

## Goal
Resolve the Iter014 source-authority blocker without fitting or importing an unqualified formula: discover openly accessible primary/standard-reference candidates that explicitly state finite-dimensional `U_q(su(2))` basis actions for `J_z` and `J_±`, with q-number normalization and enough phase/convention context to reproduce generic q-CG coefficients.

## Independent lanes
Four search lanes use distinct query families: `uqsu2-action`, `quantum-clebsch`, `root-unity-representation`, `qangular-momentum`.

## Frozen candidate requirements
A candidate is only `AUTHORITY_CANDIDATE` if its accessible source text contains all of:
1. explicit `U_q(su(2))`/q-deformed su(2) representation context;
2. explicit basis-state action for both diagonal `J_z` (or K/q^Jz equivalent) and raising/lowering generator(s);
3. q-number / q-factorial normalization definition;
4. identifiable publication metadata / arXiv id and stable source retrieval;
5. no formula inferred from numerical fitting.

This discovery gate does **not** by itself authorize implementation. If candidates are found, a separate prospectively frozen authority-qualification gate must compare conventions against the already qualified coproduct, orthogonality, cap/cup and qbar-duality structure.

## Interpretation
- candidate(s) meeting all textual predicates -> `RC006_OPEN_UQSU2_ACTION_AUTHORITY_CANDIDATES_FOUND_SCOPED`;
- no candidate meeting all predicates -> `RC006_OPEN_UQSU2_ACTION_AUTHORITY_NOT_FOUND_BLOCKED`;
- network/parser failure before search predicates -> `INFRASTRUCTURE_SOURCE_DISCOVERY_FAIL`.

Always: bridge credit=false, Iter012 retry=false, Eq.(29) unauthorized, candidate theory unauthorized.
