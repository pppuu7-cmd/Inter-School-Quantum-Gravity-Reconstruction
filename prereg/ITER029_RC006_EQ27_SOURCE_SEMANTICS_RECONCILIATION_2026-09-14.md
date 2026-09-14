# ITER029 preregistration — RC006 Eq.(27) source-semantics reconciliation

Date: 2026-09-14

Status: `PREREGISTERED_NOT_EXECUTED`.

## Authorization basis

ITER028 Stage S terminalized `BLOCKED — RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED` because its frozen inventory required four TikZ graphical blocks while the exact byte-pinned Eq.(27) display mechanically contains two `tikzpicture` environments. ITER028 remains terminal and may not be repaired retroactively.

The durable ITER021 record, inspected only to identify the next admissible question, states a more specific historical predicate: **two draw paths, four TikZ begin/end tokens**, not four TikZ environments. This creates a source-semantics reconciliation question that is distinct from numerical Eq.(27) execution.

## Frozen hypothesis

`H029`: the historical “four” count arose from counting the two `\\begin{tikzpicture}` plus two `\\end{tikzpicture}` tokens (four begin/end tokens total), while the exact Eq.(27) object itself consists of two bracketed graphical factors / two TikZ environments. If and only if repository provenance plus the byte-pinned source support this interpretation without ambiguity, the historical inventory conflict is reconciled for a **future new gate**.

## Frozen source/provenance inputs

Required target source: arXiv `1609.02429v2`.

Required archive SHA256: `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

Required Eq.(27) display SHA256: `88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d`.

Required durable repository records:

- `results/ITER021_RC006_EQ27_COMPONENT_TRANSLATION_2026-09-14.md`;
- `prereg/ITER028_RC006_EQ27_TOPOLOGY_FAITHFUL_CONTRACTION_2026-09-14.md`;
- `results/ITER028_RC006_EQ27_STAGE_S_SOURCE_GRAPH_MAP_BLOCKED_2026-09-14.md`.

## Independent lanes

Run with `fail-fast:false`:

1. `source-token-census`: fresh byte-pinned source extraction; count TikZ environments, begin tokens, end tokens, draw commands, bracketed sum factors and internal sums.
2. `historical-language-audit`: parse ITER021/ITER028 durable wording and distinguish environment count, begin/end token count, draw-path count and “graphical factor” language.
3. `structural-factorization`: test whether the exact display is mechanically factorized into two outer bracketed `sum_j ... tikzpicture ...` factors, without assigning additional tensor semantics.
4. `null-controls`: reject deliberately false interpretations: four TikZ environments; one TikZ environment; four independent bracket factors; or a source hash mismatch.

No numerical q-CG, R, qbar or amplitude contraction is permitted in ITER029.

## PASS

`RC006_EQ27_SOURCE_SEMANTICS_RECONCILED_SCOPED` only if all four lanes establish that:

- provenance hashes match exactly;
- Eq.(27) has exactly two TikZ environments;
- it has exactly two begin tokens and two end tokens, hence four begin/end tokens total;
- ITER021 explicitly records “two draw paths, four TikZ begin/end tokens”;
- the exact display is mechanically two bracketed graphical factors carrying the two internal sums;
- the ITER028 “four graphical blocks / source graphical factors” requirement is therefore a historical inventory interpretation mismatch, not evidence of missing source bytes;
- all frozen false interpretations are rejected.

PASS does **not** convert ITER028 to PASS. It authorizes only consideration of a newly preregistered corrected Stage-S successor using the exact source semantics established here.

## BLOCKED

`RC006_EQ27_SOURCE_SEMANTICS_RECONCILIATION_BLOCKED` if durable records or exact source do not uniquely determine the count semantics.

## FAIL

`RC006_EQ27_SOURCE_SEMANTICS_RECONCILIATION_FAIL` only if exact source/provenance and durable records are unambiguous but contradict `H029`.

Infrastructure/provenance errors are non-scientific.

## Claim locks

No bridge credit; no Eq.(29)/Lambda; no one-step TNR; no preferred alpha; no candidate theory; no new physics; no retrofit of ITER028.
