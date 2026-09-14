# ITER038 preregistration — RC006 Eq.(27) central coupling/domain authority

Date: 2026-09-14
Status: `PREREGISTERED_NOT_EXECUTED`.

ITER037 terminalized `PASS — RC006_DIAGONAL_EXTERNAL_LABEL_SOURCE_SUPPORT_PASS`. Before any numerical Eq.(27) summation, the remaining central labels must be source-qualified: `j_1^+,j_2^+ -> J^+`, `j_1^-,j_2^- -> J^-`, then `J^+,J^- -> l`. The exact source explicitly notes that the simplicity constraints are not explicitly imposed on the latter coupling, so no EPRL map may be invented for central `l`.

## Frozen diagonal source panel
Use exactly the four ITER037 diagonal cases and split, unchanged:
- primary `(k=6,gamma=1/3,l_1=l_2=3)`;
- held-out `(k=10,gamma=3/5,l_1=l_2=5)`;
- primary `(k=12,gamma=1/3,l_1=l_2=3)`;
- held-out `(k=12,gamma=1/3,l_1=l_2=6)`.
No new gamma/l and no panel reshuffling.

## Lanes (`fail-fast:false`)
A — source topology authority. PASS requires exact source text outside Eq.(29)/Lambda positively stating indexed `j_i^±` couple to `J^±`, and `J^±` then couple to central `l`, together with the explicit statement that simplicity constraints are not explicitly implemented in the latter coupling.

B — finite-k coupling-domain authority. PASS requires exact source authority for SU(2)_k admissibility sufficient to enumerate `J^+`, `J^-`, and central `l`: finite representation cutoff, triangle/admissibility and root-of-unity sum condition. Lexical label occurrence alone is insufficient.

C — bounded central-domain enumeration. For each frozen diagonal case, mechanically enumerate all integer `J^+` admissible in `(j_1^+,j_2^+)`, all integer `J^-` admissible in `(j_1^-,j_2^-)`, and all central integer `l` admissible in `(J^+,J^-)`, using only source-qualified q-SU(2) rules. PASS requires non-empty finite domains for all four cases and at least one primary and held-out case. No simplicity-map condition is imposed on central `l`.

D — frozen nulls. On the first primary case require 3/3 rejection of: (1) `J^+` above its source-admissible coupling maximum; (2) `J^-` above its source-admissible coupling maximum; (3) central `l` violating the `(J^+,J^-)` q-SU(2) admissibility rule. Detection is exact domain failure.

## Classes
`RC006_EQ27_CENTRAL_COUPLING_DOMAIN_AUTHORITY_PASS`: A-D PASS. Authorizes only a separately preregistered label-complete bounded panel gate before numerical Eq.(27) summation.

`RC006_EQ27_CENTRAL_COUPLING_DOMAIN_AUTHORITY_BLOCKED`: source topology/domain authority insufficient or a frozen source-derived panel is empty. Not scientific failure.

`RC006_EQ27_CENTRAL_COUPLING_DOMAIN_AUTHORITY_FAIL`: only valid source authority plus failure of frozen exact domain/null predicates.

Infrastructure/parser/hash/artifact failure before substantive evaluation is pre-science.

Claim locks remain false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.
Candidate theory `UNFORMED / 0%`; roadmap readiness 49%.