# ITER011 — RC006 Eq.(27)/Appendix-F q-CG authority gate

Date: 2026-09-13

## Frozen objective
Determine whether arXiv:1609.02429v2 contains a complete, internally consistent authority chain for the numerical 3-valent EPRL tensor used by the triangular TNR algorithm, without importing the independently blocked Eq.(29)/Lambda convention and without fitting missing conventions.

## Primary source scope
Only source-explicit ingredients from arXiv:1609.02429v2 are admissible: Appendix A q-number/q-dimension/admissibility rules; Appendix B graphical/q-CG conventions and B15 splitting identities; Eq.(22) EPRL map; Eq.(27) 3-valent tensor; Appendix E normalization/alpha family; Appendix F derivation of the 3-valent diagrams from the 4-valent object; Appendix C coarse-graining/SVD map. Eq.(29)/general formLambda6j is excluded from authority.

## Frozen independent lanes
A — Eq.(27) ingredient inventory: require every explicit scalar ingredient in Eq.(27) to be source-defined (phase exponent, q-dimensions, sum over intermediate j, admissibility/support, EPRL j± map, external/intermediate labels). Missing source definition => FAIL/BLOCKED.

B — q-CG convention authority: require Appendix A/B to define q-CG normalization, cap/cup duality, q vs qbar orientation, orthogonality/completeness, recoupling [6j] convention and B15 splitting. A convention may delegate only to an explicit cited primary reference named by the paper; an unnamed convention is not allowed.

C — Appendix-F derivation closure: require Appendix F to derive the 3-valent diagrams from the 4-valent EPRL object using source-stated B15 identities with no new amplitude convention. If Appendix F is merely schematic but all needed numerical conventions are already fixed in A/B, this lane may PASS; if a numerical phase/normalization remains undefined, classify BLOCKED.

D — independence/negative controls: Eq.(29), Lambda/formlamb6j and any fitted normalization are forbidden inputs. Deliberately removing the modified-qCG normalization factor or swapping q/qbar dual convention must be detected as non-authoritative controls.

## Frozen interpretation
All four lanes PASS => `RC006_EQ27_APPENDIXF_NUMERICAL_AUTHORITY_CHAIN_COMPLETE_SCOPED`; this authorizes only the smallest source-faithful one-step numerical reconstruction with alpha declared prospectively. It gives zero bridge credit by itself.

Any source-essential convention missing => `RC006_EQ27_APPENDIXF_NUMERICAL_AUTHORITY_CHAIN_BLOCKED`.

Technical/parsing failure => `ITER011_INFRASTRUCTURE_OR_PARSER_FAIL`, not scientific FAIL.

No post-hoc threshold/model/convention changes. Candidate theory remains 0/UNFORMED. Claim locks remain unchanged.