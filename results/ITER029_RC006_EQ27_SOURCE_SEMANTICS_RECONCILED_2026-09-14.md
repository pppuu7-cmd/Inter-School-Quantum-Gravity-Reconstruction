# ITER029 result — RC006 Eq.(27) source-semantics reconciliation

Date: 2026-09-14

Scientific classification: **PASS — `RC006_EQ27_SOURCE_SEMANTICS_RECONCILED_SCOPED`**.

This is a semantics/provenance result only. It does not retrofit ITER028, does not execute Eq.(27), and gives zero bridge credit.

## Authoritative provenance

- preregistration commit: `fd3db7bc95a17dd3265e0ec7431a452df0503935`
- implementation commit: `ab42e0adf64ef47878c8f410542c8e4d7769583c`
- production head: `fab8522ca1e0b5ac36bff8255e04252f295b91c9`
- Actions run/job: `34794237347 / 103824140071`
- artifact: `10328987132`
- artifact digest: `sha256:b6114041c61b2bfe3c21403a24afe641882af042aeba6ed05ca64cc7367ef721`
- source archive SHA256: `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`
- exact Eq.(27) display SHA256: `88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d`

## Frozen-lane results

1. `source-token-census`: PASS. Exact display contains 2 `tikzpicture` environments, 2 draw commands, 2 sums, and 4 begin/end TikZ tokens (2 begin + 2 end).
2. `historical-language-audit`: PASS. ITER021 recorded “two draw paths, four TikZ begin/end tokens”; ITER028 later froze a different “four graphical blocks” interpretation and therefore remains independently BLOCKED.
3. `structural-factorization`: PASS. Exact Eq.(27) has 2 bracketed sum/TikZ factors, 2 environments and 2 sums.
4. `null-controls`: PASS. Four prospectively specified false interpretations were rejected: four bracket factors, four environments, one environment, and source-hash mismatch.

## Interpretation

The historical count discrepancy is resolved without changing any previous threshold: the number four referred to begin/end syntax tokens, not four independent graphical factors. ITER028 remains terminal `RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED` because its frozen Stage-S requirement cannot be changed after observing the source extraction.

The only authorization gained here is to preregister a **new** corrected Stage-S successor whose source inventory starts from exactly two Eq.(27) TikZ graphical factors/environments. That successor must still independently prove a complete graph-to-component/index map. If exact tensor-leg order, loop attachment, crossing, summation range, normalization, source locator, or index authority remains unresolved, it must classify BLOCKED rather than infer from visual geometry or numerical fit.

## Claim locks

Still false: `iter012_retry_authorized`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.

Candidate theory remains `UNFORMED / 0%`; overall programme roadmap readiness remains 49%.
