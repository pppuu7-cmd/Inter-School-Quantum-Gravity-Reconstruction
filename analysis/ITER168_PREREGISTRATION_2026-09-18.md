# ITER168 preregistration — semantic provenance / executable-source audit

Frozen prospectively after ITER167 was reclassified SCIENTIFIC_FAIL for provenance leakage, before ITER168 results.

## Frozen purpose
Determine whether the singular geometry needed downstream of the ITER163 21-term ledger is encoded in executable or structured source-expression objects, rather than being inferred from preregistration, terminal-result, recovery, navigator, or other prose.

## Allowed positive evidence
Only tracked executable/structured source objects that actually encode the denominator/phase/endpoint geometry used to generate the ITER163 ledger. Positive evidence must include exact path plus symbol/key/line-context and the mechanically extracted expression. Markdown prose, recovery files, terminal notes, preregistration text, navigator text, lexical keyword hits, and later summaries are forbidden as positive evidence.

## Lane A — executable provenance extractor
Trace each ITER163 ledger family QQ/QK/KQ backward to executable/structured source objects. Record exact object provenance, denominator/factor expressions, endpoint/orientation information, and contact/cancelled-propagator encoding. If the trace terminates in hard-coded ledger rows or prose rather than source geometry, return BLOCKED_MISSING_SOURCE_EXPRESSION.

## Lane B — adversarial negative-control critic
Search specifically for provenance leakage: hard-coded term ledgers, markdown-derived geometry, keyword-only matches, or objects that encode tensor bookkeeping but not denominator/phase singular geometry. Attempt to falsify every Lane-A positive claim. No positive credit from prose.

## Lane C — source-geometry completeness critic
Independently scan eligible executable/structured source objects for denominator zeros, endpoint/intersection sectors, phase singularities, and contact loci. Compare only after independent extraction. Missing source geometry or an untraceable sector blocks completeness.

## Frozen outcomes
- PASS_SCOPED_ITER168_EXECUTABLE_SOURCE_GEOMETRY_PROVENANCE_COMPLETE only if all three lanes establish executable/structured source provenance without prose leakage and the independent critic finds no omitted eligible locus. This only authorizes a later sector manifest/domain-scaling-pullback gate.
- BLOCKED_SCOPED_ITER168_MISSING_EXECUTABLE_SOURCE_GEOMETRY if required geometry is absent from eligible source objects.
- BLOCKED_SCOPED_ITER168_PROVENANCE_OR_COMPLETENESS_INCOMPLETE if some eligible geometry exists but the ITER163 trace or sector completeness is incomplete.
- SCIENTIFIC_FAIL_ITER168_FROZEN_SOURCE_CLAIM_CONTRADICTED only for an exact contradiction of a frozen positive source claim.
- infrastructure failure remains separate.

Green CI is not scientific PASS. Do not use ITER160 residue, inverse-28 reconstruction, ITER118 coefficients, fitted pole tensors, post-result regularization, or markdown prose as positive source evidence. No threshold/model/tensor-basis/contact change after observing results. ITER168 cannot authorize Laurent/R-operation, ITER118 matching, B1_total, bridge credit, candidate equations, or candidate theory.
