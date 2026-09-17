# ITER157 preregistration — fixed-geodesic endpoint tensor pole equation source derivation

Date: 2026-09-17

## Frozen scientific object

Freeze the ITER118 endpoint basis exactly as `R,S,DR,DS,BoxR,D2R,BoxS,D2S` and freeze the three first-M/G endpoint strata already identified by ITER155/156. ITER156 rank=0/nullity=8 is input evidence, not a target to be repaired by assumption.

## Prospective question

Does the repository contain an explicit, source-faithful tensor-resolved pole equation or a complete derivation chain that maps a divergent first-M/G endpoint residue into at least one frozen ITER118 basis direction with an explicit coefficient?

## Admissible evidence

Only pre-existing repository files (excluding ITER157 implementation/output and recovery summaries) count. A hit must contain an explicit pole/residue/divergent coefficient relation AND identify an endpoint/geodesic stratum or endpoint tensor projection AND resolve at least one frozen basis direction. Mere mentions of a basis, generic counterterms, rank/nullity summaries, or statements that a derivation is needed do not count.

## Frozen classification

* `PASS_SCOPED_ITER157_SOURCE_FAITHFUL_ENDPOINT_TENSOR_POLE_EQUATION_FOUND` only if at least one admissible explicit equation/complete derivation chain is found with exact path/line provenance.
* `BLOCKED_SCOPED_ITER157_NO_SOURCE_FAITHFUL_ENDPOINT_TENSOR_POLE_EQUATION_FOUND` if exhaustive repository audit finds none.
* infrastructure/parser failure is not scientific FAIL/BLOCKED.

No missing equation may be interpreted as coefficient zero. No basis change, no post-result threshold change, no `B1_total`, no bridge/new-physics/candidate-theory promotion. A scoped PASS does not close slot 7 unless subsequent frozen rank/coefficient gates justify closure.