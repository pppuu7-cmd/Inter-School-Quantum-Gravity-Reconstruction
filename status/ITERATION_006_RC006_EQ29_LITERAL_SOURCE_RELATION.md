# ITERATION_006 RC006 Eq.(29) literal source-reference relation — preregistration

Date: 2026-09-12  
Status: PREREGISTERED BEFORE IMPLEMENTATION

## Frozen prerequisite

Run `34719456729` is terminal `EQ29_IMMUTABLE_SOURCE_DEPENDENCIES_COMPLETE_R_NOT_APPLICABLE` and explicitly authorizes preregistration of a literal Eq.(29) tensor reconstruction gate. It does not authorize a remembered/fitted formula or numerical amplitude by itself.

## Frozen source

- arXiv:1609.02429v2;
- source bundle SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`;
- source file `bc-spin-nets.tex`;
- immutable Eq.(29) align-block SHA256 `4f505657a580216d176c1c63ec92f5614dc73e8113294722a854d5a350b67083`;
- Eq.(29) target sentence in the unique active `EPRL intertwiner model` subsection explicitly contains `\\eqref{eq:eprl-3-valent}`.

No external derivation, remembered EPRL formula, fitted contraction order or unreferenced code is admitted in this gate.

## Scientific objective

Resolve the source object denoted by the explicit Eq.(29)-context reference `eq:eprl-3-valent`, extract its exact containing source environment and determine whether it supplies an independent literal source relation usable to constrain a later evaluator of Eq.(29).

## Frozen extraction rule

After stripping only unescaped-`%` TeX comments:

1. require exactly one `\\label{eq:eprl-3-valent}` in the active document;
2. identify the smallest complete enclosing `equation`, `equation*`, `align`, `align*`, `gather`, `gather*`, or `multline` environment containing that label; if none exists, identify the smallest complete enclosing `tikzpicture` together with its immediately containing display-math environment; unsupported/ambiguous containment is fail-closed;
3. independently re-extract the immutable Eq.(29) EPRL subsection and require exactly one explicit `\\eqref{eq:eprl-3-valent}` there;
4. record SHA256 of the referenced source environment, its literal TeX, all `\\label`, `\\ref`, `\\eqref`, `\\sum`, `\\sqrt`, dimension-factor tokens `d_...`, q-power tokens, TikZ draw commands, and node-label strings without semantic rewriting;
5. record the nearest active section/subsection/subsubsection header containing the referenced label.

## Independent lanes

### ENVIRONMENT_EXTRACTOR

Use character-offset balanced-environment matching to select the unique smallest allowed enclosing source environment and emit the literal block plus structural token inventory.

### LINE_STRUCTURAL_VERIFY

Independently locate the unique label line, determine the enclosing allowed environment by linewise begin/end nesting, and verify the Eq.(29) EPRL subsection contains exactly one direct `eqref` to that label. It does not reuse the first lane's offsets or environment selection.

## Frozen classifications

- `EQ29_LITERAL_SOURCE_RELATION_EXTRACTED`: both lanes are valid and agree on a unique source label, a unique enclosing allowed environment type, identical environment SHA256, and exactly one direct Eq.(29)-subsection `eqref` to `eq:eprl-3-valent`.
- `EQ29_LITERAL_SOURCE_RELATION_AMBIGUOUS`: source is valid but label/reference/environment uniqueness fails or lanes disagree on containment/hash.
- `EQ29_LITERAL_SOURCE_RELATION_UNSUPPORTED`: the unique source label exists but is not contained in an allowed extractable display object.
- `INVALID_SOURCE_OR_IMPLEMENTATION`: source hash/block mismatch or parser/runtime failure.

A PASS establishes an immutable source-reference relation only. It authorizes preregistration of a source-to-algebra/tensor evaluator gate using the extracted literal object plus already qualified Eq.(29) geometry/incidence. It does **not** itself authorize numerical Eq.(29) amplitudes.

## Claim locks

Bridge credit remains zero. Candidate theory remains `UNFORMED`; no `BRIDGE_DERIVED`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.
