# ITER018 - RC006 exact Eq.(27), even-k and provenance parallel qualification

Date: 2026-09-14  
Preregistration: `809c9a76b43c6bf05ac7c56cfb5d8d1fb260e2eb`

## Terminal classification

**`RC006_EQ27_GRAPH_AND_EVENK_CATEGORY_PINNED_IMPLEMENTATION_PREREG_ALLOWED`**

This closes the convention/source gate that remained after ITER017. It authorizes only preregistration of a bounded q-CG implementation-validation checkpoint. It does **not** authorize Iter012, Eq.(29)/Lambda amplitude work, alpha selection, bridge credit, candidate-theory construction, RQIR/KMQGB promotion, or a new-physics claim.

The final production audit was GitHub Actions run `34784718497` at head `ff5dca3f3488100c52434b127a1ca288ff0325c2`, using three matrix lanes concurrently. The aggregate machine result was `RC006_MECHANICAL_GATES_PASS_SOURCE_GRAPH_REVIEW_REQUIRED`; the source-graph review required by that machine class was then completed against the exact TeX environment and exact rendered PDF pages. No source contradiction was found, so the preregistered promotion criterion is satisfied.

## 1. Lane A - exact Eq.(27) graph recovery: PASS

Frozen target: Dittrich, Schnetter, Seth and Steinhaus, arXiv:1609.02429v2.

Fresh e-print SHA256 exactly equals the historical frozen value:

`3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

The exact source contains one unique prose anchor:

> `See appendices ... for derivations of the normalisation and the diagrams respectively:`

The immediately following display is uniquely recovered as

`\begin{align} \label{eq:eprl-3-valent}`

and matches PDF Eq.(27). Its source structure contains two bracketed internal-j sums, two closed graphical evaluations carrying the `l` loop, a primed `(J^+)',(J^-)'` pair in the first graph and an unprimed `J^+,J^-` pair in the second, and no open magnetic-index legs in the displayed reduced amplitude. The source graph is therefore not reconstructed from memory: the edge paths and labels come directly from the frozen TeX.

The exact PDF bytes in the production lane have SHA256

`accc590fb97d8e07ec0d7b836dbb03fb92052c98c9322512b428ca294a1be475`.

Pages 22, 37 and 38 were rendered from those bytes. Page 22 visually confirms Eq.(27) and the adjacent statement that its normalization is computed by contracting `T_EPRL` with itself. Page 37 (Appendix E) explicitly evaluates `T_EPRL o T_EPRL`: the paper states that the last closed diagram is computed with the graphical identities of Appendix B and reduces it to (E3), including the source signs, quantum-dimension factors and `delta_{l l'}`. Page 38 (Appendix F) continues the derivation of the EPRL graph; together with the text at the bottom of page 37 it uses (B15) and then the R-matrix identity to reach (F1)/the final graph form.

This establishes the needed provenance chain:

`target q-CG convention -> Appendix-B cup/cap/dual graphical calculus -> EPRL graph reductions -> Eq.(27) / Appendix-E normalization`.

It does not replace the categorical contraction by an ordinary Hilbert-space absolute square.

Final v3 Eq27 lane evidence:
- exact prose-anchor hits: 1;
- exact source environment: `eq:eprl-3-valent`;
- two internal-j sums;
- two closed l loops;
- primed and unprimed J pairs present;
- pages 22/37/38 rendered: all true;
- Appendix-B to E3 textual chain: true;
- B15/F1/R-matrix derivation chain: true;
- `mechanical_recovery_pass=true`.

Artifact `iter018-v3-eq27-graph`, ID `10326142705`, ZIP digest `sha256:150e6b0d8ddc1db2fb69d36acab8b6c189c3919d76724d71f0a96c60f8f80eed`.

## 2. Lane B - independent even-k category qualification: PASS in scope

Independent cross-check: Zache, Gonzalez-Cuadra and Zoller, arXiv:2304.02527v2, supplemental section on `SU(2)_k`.

Fresh e-print SHA256:

`9d725a2226ca2108fb68e070d4f52d954d11dcd86e0ee797ea0b60a2f9e998a5`.

The source satisfies every preregistered category/fusion predicate:
- `q = exp(2*pi*i/(k+2))` with `k` a positive integer;
- finite labels through `k/2`;
- q-number formula, including the equivalent sine form with `k+2`;
- fusion cutoff including `j1+j2+j3 <= k`;
- q-deformed 6j/F-matrix convention;
- F-matrix orthogonality and reality statement;
- no odd-k restriction detected in the stated `SU(2)_k` domain.

Hence even `k`, specifically `k=12`, is within the declared domain of this independent category-level source. This removes the independent-category gap caused by Fairbairn-Meusburger's odd-r restriction.

Scope remains important: arXiv:2304.02527v2 is **not** promoted to an independent q-CG component-phase authority. The component convention still comes from the target's own normalized graphical calculus and the already qualified representation-action/convention dictionary.

Artifact `iter018-v3-evenk-category`, ID `10326555531`, ZIP digest `sha256:87bd12114cbc70adcfff80efd3f90dce325fdc5c9e957ab972995642ed6fbca9`.

## 3. Lane C - byte provenance: PASS

Fresh production downloads reproduce all three historical ITER014 e-print hashes exactly:

- `1609.02429v2` -> `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`;
- `1312.0905v2` -> `69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0`;
- `1506.04749v3` -> `758e05bf73390015fb02f374c69892ad155c8edacb40a97876c12aa7f64c1e14`.

This independently confirms that the target/source panel used in the earlier frozen audit has stable byte provenance. Artifact `iter018-v3-provenance`, ID `10325618162`, ZIP digest `sha256:6a58d13395e9bc30538baf0f9eaef56a7030e46113023dbc7a029602215dee64`.

Aggregate artifact ID `10325982983`, ZIP digest `sha256:001bfbad3413976983779214b83b498442c296de07ca821c39e560a3fe09dc0f`.

## 4. Parser-correction discipline

The first production run `34784469592` produced two tooling mistakes, neither of which is scientific negative evidence:

1. its even-k q-number predicate looked for lexical phrases such as `q-number`, although the frozen source gives the formula directly; this produced a false negative;
2. its Eq.(27) source selector used a generic normalization anchor and selected the earlier EPRL tensor equation (24), even though the exact PDF page recovery was successful.

Run `34784658623` corrected both broad issues and located the unique correct Eq.(27) `align`, but two remaining syntactic counters were still overly narrow: a long TikZ path was counted as one `\draw` command, and the B15 prose is at the bottom of page 37 while F1/R-matrix text is on page 38.

Final run `34784718497` replaced these lexical counters with the preregistered structural/source predicates. Historical runs and classifications are preserved; no failed parser boolean was silently treated as physics.

## 5. Scientific consequence

The RC006 blocker has narrowed enough to admit an implementation-validation experiment without importing an external closed-form q-CG formula. The preferred next test is to construct low-spin q-CG/intertwiner data directly from:

1. the already source-qualified Uq(su2) representation action;
2. the target coproduct (A5);
3. the target root `q=exp(2*pi*i/(k+2))` and admissibility (A7);
4. the target bilinear completeness/orthogonality (A8)-(A9);
5. Appendix-B cap/cup and qbar-dual identities;
6. closed, convention-invariant checks, including the even-k case `k=12`.

A bounded implementation checkpoint should keep residual sign gauge explicit and should test invariant/paired quantities rather than fit phases to the expected answer. A solver-derived q-CG construction is preferable to importing a formula from an inaccessible book because it tests the already pinned algebraic convention directly.

## 6. Locks after ITER018

`implementation_validation_prereg_allowed=true`.

Still false until a separately preregistered implementation checkpoint succeeds:

`implementation_validation_gate_authorized=false`, `iter012_retry_authorized=false`, `eq29_amplitude_authorized=false`, `bridge_credit=false`, `candidate_theory_authorized=false`.

Candidate theory remains **UNFORMED**. Administrative readiness percentages are unchanged by this source/convention qualification.