# ITER021 preregistration — RC006 source-faithful Eq.(27) component reconstruction

Date: 2026-09-14

## Authorization basis

ITER020 terminal classification: `RC006_QCG_HELDOUT_TRANSPORT_PASS`.

ITER021 is the first checkpoint allowed to consume the validated, non-retuned q-CG backend inside the target EPRL graphical normalization. It does **not** run the historical Iter012 one-step TNR lane, does not evaluate Eq.(29)/Lambda, does not select alpha, and gives zero bridge/candidate-theory credit by construction.

## Frozen source and provenance

Primary target: Dittrich, Schnetter, Seth, Steinhaus, arXiv:1609.02429v2.

Required e-print SHA256:
`3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

The implementation must stop with an infrastructure/provenance classification if fresh source bytes do not reproduce this hash. No unversioned or silently changed source may replace it.

## Stage S — exact source extraction / graph compiler

Before numerical component reconstruction, mechanically extract from the byte-pinned TeX source:

1. the unique display `\label{eq:eprl-3-valent}` corresponding to PDF Eq.(27), including every TikZ edge/label and its adjacent normalization prose;
2. Appendix-E displays E1–E4 and the prose explaining which Appendix-B graphical identities are used;
3. Appendix-F display F1 and the immediately adjacent B15/R-matrix reduction prose;
4. the Appendix-A q-number/coproduct/admissibility/A8/A9 source environments used by the solver;
5. Appendix-B cap/cup/qbar-dual environments used to bend legs;
6. every exact source occurrence and local context of the frozen historical numerical sentinels `7.41492`, `1.399277`, `-1.931582`, `-3.861564`, and the k=12 statement/cancellation associated with the vanishing `l=3` contribution.

Extraction is source inspection, not physics credit. It must emit exact file names, labels, bounded source snippets and SHA256 provenance. No graph edge may be supplied from memory when absent from the source environment.

## Frozen reconstruction principle

After Stage S succeeds, construct the target graphical contraction using only:

- the validated ITER019/020 q-CG solver embeddings;
- the target bilinear A8/A9 convention;
- Appendix-B cap/cup and qbar-dual bending rules;
- the exact Eq.(27), Appendix-E and Appendix-F source graph environments extracted in Stage S;
- target quantum dimensions/q-numbers at `k=12`.

Forbidden:
- importing an external closed-form q-CG formula;
- replacing qbar duality by Hermitian conjugation or absolute-square convenience;
- fitting row/column signs or phases to a source answer;
- altering graph orientation, tensor ordering, edge labels, or normalization factors after seeing numerical outputs;
- inserting an alternate Eq.(29), Lambda prescription or TNR truncation.

Residual normalized channel sign gauge may be changed only where the already source-qualified A9/B2 convention permits it; any final closed scalar must be sign-gauge invariant under those allowed changes.

## Parallel numerical lanes after Stage S

### Lane A — Eq.(27)/Appendix-E component identity

At k=12, use the exact source graph to build `T_EPRL` and its source-defined dual contraction for the smallest nontrivial admissible sample sectors corresponding to source free spin labels `j=1,2,3` wherever the extracted formula defines them.

For each sample, compute the closed component contraction directly and independently compute the Appendix-E closed-form reduction extracted as E3/E4.

PASS if:
- every required channel is source-admissible;
- no source-graph factor is omitted;
- direct component contraction and E3/E4 reduction agree to absolute and relative tolerance `1e-8`;
- result is invariant under independently flipping any residual allowed channel sign gauge.

If the extracted source shows that `j=1,2,3` are not sufficient to define a complete sample without additional fixed labels, the lane must freeze those additional labels mechanically from the same source/table context before evaluation; it may not choose them to improve agreement.

### Lane B — q=1 sentinel

Using the **same graph compiler and contraction code**, replace q-deformed q-numbers/dimensions/actions by their undeformed q=1 values and use the undeformed highest-weight solver backend. No graph or normalization change is permitted.

For the same source-defined sample sectors as Lane A, compare direct component contraction with the q=1 reduction of the extracted Appendix-E expression.

PASS tolerance: absolute and relative `1e-8`.

This is an instrumentation sentinel only and gives zero finite-k or bridge credit.

### Lane C — frozen source-number normalization audit

Use exact source formulas/graph normalization, not literal string matching, to reproduce the historical frozen numerical sentinels at k=12:

- `N13(alpha=4) = 7.41492`
- `N13(alpha=8) = 1.399277`
- `N14(alpha=4) = -1.931582`
- `N14(alpha=8) = -3.861564`

and the stated source cancellation leading to `|lambda_{l=3}|=0` at k=12.

The exact meaning of `N13`, `N14`, alpha and the cancellation factors must be taken mechanically from Stage-S source context before evaluation. No symbol may be assigned by guesswork.

PASS if the four values reproduce to `5e-6` absolute error (source print precision) and the l=3 cancellation residual is `<1e-10` in the exact source expression.

### Lane D — graph/sign adversarial calibration

On one smallest nontrivial finite-k sample from Lane A, deliberately apply separately:

1. ordinary complex conjugation in place of source qbar/cap-cup duality;
2. remove one source quantum-dimension normalization factor;
3. reverse one source-identified cap/cup bend orientation where this changes the component formula.

The correct construction must satisfy Lane-A tolerance. The calibration passes only if at least two of the three wrong constructions are detected by a direct-vs-E3/E4 mismatch `>1e-6` or by a source identity violation `>1e-6`.

This lane exists only to reject false-positive graph compilers; wrong variants never receive physical interpretation.

## Dependency and execution design

Stage S is a prerequisite job. After it succeeds, Lanes A–D should run as independent GitHub Actions jobs where practical, consuming the same immutable Stage-S extraction artifact and the same solver backend commit/hash. `fail-fast:false` is required.

The aggregate must preserve per-lane failure and distinguish infrastructure/source-provenance blockage from mathematical mismatch.

## Terminal classes

- `RC006_EQ27_COMPONENT_RECONSTRUCTION_PASS`
- `RC006_EQ27_SOURCE_EXTRACTION_BLOCKED`
- `RC006_EQ27_COMPONENT_MISMATCH`
- `RC006_EQ27_Q1_SENTINEL_FAIL`
- `RC006_EQ27_SOURCE_NUMBER_REPRODUCTION_FAIL`
- `RC006_EQ27_GRAPH_CALIBRATION_FAIL`
- `RC006_EQ27_RECONSTRUCTION_INFRASTRUCTURE_PARTIAL`

Only the full PASS may authorize preregistration of the historical one-step 2x2 TNR benchmark in a later iteration. A full PASS does not itself authorize Eq.(29)/Lambda or bridge credit.

## Claim locks

Always false during ITER021:
`iter012_retry_authorized`, `eq29_amplitude_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`.

Administrative readiness values do not automatically increase on a reconstruction PASS.