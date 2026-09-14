# Preregistration — ITER041 RC006 root-unity primitive-domain source audit

Date frozen: 2026-09-14

## Inherited facts

ITER039 remains terminal SCIENTIFIC FAIL. ITER040 diagnostic complete showed:

- all exact prior ITER027 pair-scope tuples pass (24/24);
- R/R^-1 failures concentrate at the preregistered naive root-tensor boundary `a+b>k`;
- distinct dual-contraction failures also occur outside that boundary but outside the prior validated pair scope.

No ITER039 threshold/domain/convention may be changed in this audit.

## Frozen source panel

Only the exact versions already pinned by ITER025 are admissible in this iteration:

1. Dittrich et al., arXiv:1609.02429v2, archive SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`;
2. Dittrich, Martin-Benito, Steinhaus, arXiv:1312.0905v2, archive SHA256 `69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0`;
3. Dittrich, Kaminski, arXiv:1311.1798v1, historical archive SHA256 `d6804794d3f4589f77a2e11d2a143c1125a900160e0c632ed3b3e471598af3f7`.

No later source may be used to retroactively reinterpret this gate. A later source-expansion gate may be opened prospectively if this panel is insufficient.

## Question A — root-of-unity R domain

Does the frozen source panel explicitly state whether the executable R/R^-1 relation is an identity on the full naive tensor product or on a truncated/physical/fusion/quotient category at root of unity, and does it state the relevant admissibility/projection rule when `a+b>k`?

PASS requires source-locatable text/formula sufficient to distinguish these domains without numerical fitting. Lexical mention of root of unity, cutoff, fusion, or R alone is insufficient.

## Question B — dual/cap/cup identity domain

Does the frozen source panel explicitly state the representation/channel domain and trace/duality convention under which the cap/cup or dual contraction identity used in ITER031/039 holds, including any quantum-trace, negligible-object/morphism, quotient, physical-channel, or normalization restriction relevant to channels outside the earlier bounded pair scope?

PASS requires a source-locatable indexed/graphical identity together with enough domain/convention context to decide whether the ITER039 expanded channels are within its stated scope. A generic cup/cap formula without domain qualification is insufficient.

## Lanes

- A: exact provenance/hash recovery for all three frozen archives.
- B: root-of-unity R-domain evidence collection and strict predicate evaluation.
- C: dual/cap/cup domain evidence collection and strict predicate evaluation.
- D: controls: bibliography-only/lexical-only hits cannot PASS; exact prior R and qbar positive source passages must still be recoverable.

## Classification

- `RC006_ROOT_UNITY_PRIMITIVE_DOMAIN_SOURCE_AUTHORITY_PASS` only if A/B/C/D pass.
- `RC006_ROOT_UNITY_PRIMITIVE_DOMAIN_SOURCE_AUTHORITY_BLOCKED` if exact sources are recovered but B or C lacks decisive domain authority.
- `INFRASTRUCTURE FAIL` if transport/decode/hash recovery prevents source evaluation.

A PASS authorizes only a separately preregistered numerical formulation that implements the source-stated domain/quotient object. A BLOCKED result authorizes only prospective source expansion, not numerical retry.

Eq.(29), Lambda, TNR, bridge credit and candidate theory remain forbidden. Candidate theory remains 0/UNFORMED.
