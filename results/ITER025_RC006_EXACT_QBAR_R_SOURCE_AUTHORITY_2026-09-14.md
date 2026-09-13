# ITER025 terminal — RC006 exact qbar/R source authority

Date: 2026-09-14

## Terminal classification

`PASS — RC006_EXACT_QBAR_R_SOURCE_AUTHORITY_COMPLETE`

This is a source/convention PASS only. It is not an Eq.(27) contraction PASS, not bridge evidence, and not candidate-theory evidence.

## Prospective gate

Preregistration: `prereg/ITER025_RC006_EXACT_QBAR_R_SOURCE_AUTHORITY_2026-09-14.md`

Prereg commit: `db2e00079e61258e69c1c8d68c587674e921be9e`.

Frozen hypothesis: the exact cited source chain uniquely fixes both (a) qbar dual-map graph-to-index ordering under the frozen target q-CG normalization and (b) R/R^-1 crossing convention, without fitting or convention repair.

## Execution and provenance

- evidence collector: `code/iter025/exact_authority_audit.py`
- implementation commit: `8294e02f2e0ab9e08f44b124d608efbc44a05072`
- workflow/production head: `cdf8142df05b61ea17b116571326e4e2721dbde0`
- GitHub Actions run: `34788769863`
- job: `103808982965`
- run conclusion: `success` (used only as execution status)
- artifact: `10326669550` (`iter025-exact-authority-evidence`)
- artifact digest: `sha256:cb1e40dc31495eb1b21d38315fb28dcc70b35f6d0505f7cd81091c0ecd4afba5`

The automation itself emitted `EVIDENCE_COLLECTED_REQUIRES_MANUAL_VERDICT` and `scientific_pass_emitted_by_automation=false`, so scientific classification was not delegated to regex booleans.

Exact source archive hashes:

- `1609.02429v2`: `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee` — matches frozen historical control.
- `1312.0905v2`: `69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0` — matches frozen historical control.
- `1311.1798v1`: `d6804794d3f4589f77a2e11d2a143c1125a900160e0c632ed3b3e471598af3f7` — newly recorded exact archive hash.

## qbar verdict

PASS under the frozen rule.

Decisive evidence:

1. Target `bc-spin-nets.tex:1432-1464` defines the inverse/complex-conjugate qbar coefficient by the bent-leg cup/cap graph, writes the ordered coefficient `{}_{\bar q} C^{j_1 j_2 j_3}_{m_1 m_2 m_3}`, labels the graph legs, and explicitly interprets the map as `V_{j_3} -> V_{j_1} \otimes V_{j_2}`.
2. Cited `qg_spinnet_20140616.tex:1101` gives the explicit indexed identity
   `{}_q C^{j_1 j_2 j_3}_{m_1 m_2 m_3}=(-1)^{j_1+j_2-j_3}{}_{\bar q} C^{j_1 j_2 j_3}_{-m_1,-m_2,-m_3}`.
3. The cited source also repeats the qbar bent-leg construction at lines 451-465.

Together these statements determine the qbar input/output component order with no `m_1/m_2` swap, no representation permutation, and no fitted sign/phase/orientation.

## R/R^-1 verdict

PASS under the frozen rule.

Decisive evidence:

1. Target `bc-spin-nets.tex:956-987` explicitly assigns one crossing to `\mathcal R` with channel factor `q^{-Delta/2}` and the opposite crossing to `\mathcal R^{-1}` with `q^{+Delta/2}`, where `Delta=j_1(j_1+1)+j_2(j_2+1)-j(j+1)`.
2. Cited `arxiv20131107.tex:1668-1682` states that the crossing exchanges tensor-product factors and defines that crossing as `R` with the same negative exponent sign.
3. The same cited source at lines 1707-1718 explicitly defines the inverse anti-crossing as `R^{-1}` with the positive exponent sign and labels the two strands.

This supplies an executable channel weight and source-unique R versus R^-1 crossing assignment. No post-hoc crossing/orientation choice is required.

## Controls

Positive control recovered exact indexed cap/cup/coproduct evidence from the target source with source-file/line context. Bibliography-only and lexical-only evidence were not allowed to qualify authority. No source-version/hash mismatch was found.

## Adversarial check

No convention conflict was found inside the frozen source set:

- target and q-spinnet sources use the same ordered qbar coefficient and the cited source adds the explicit magnetic-index relation;
- target and `1311.1798v1` agree on R versus R^-1 crossing assignment and on the sign of the channel exponent.

This is not a claim of universal quantum-group convention outside the frozen realization/source set.

## New structural fact

The ITER023 blockers were not intrinsic source absence. They were recoverable from the exact source chain once the source packages were inspected at component/diagram level rather than through the earlier restricted authority parser. In particular, the target source itself contains a full R/R^-1 crossing formula, while the cited q-spinnet source supplies the explicit q↔qbar magnetic-index identity.

## Authorization consequence

Set:

`eq27_component_reconstruction_prereg_allowed=true`.

The next admissible scientific step is a **new, separately preregistered bounded Eq.(27) component translation/contraction** using only these now-frozen qbar and R conventions plus previously validated q-CG/cap/cup data.

Still false / unauthorized:

- `iter012_retry_authorized`
- `eq29_amplitude_authorized`
- `bridge_credit`
- `candidate_theory_authorized`
- `preferred_alpha_found`
- `new_physics_found`
- all-schools failure / new-theory-required / universal-bridge claims.

Candidate theory remains `UNFORMED`.
