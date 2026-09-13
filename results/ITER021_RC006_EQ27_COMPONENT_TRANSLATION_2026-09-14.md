# ITER021 — RC006 Eq.(27) executable component-translation authority

Date: 2026-09-14

## Terminal classification

**`RC006_EQ27_COMPONENT_TRANSLATION_BLOCKED_MISSING_PRIMITIVE`** — BLOCKED.

This is not a scientific failure of the EPRL amplitude and not a bridge result. The exact target Eq.(27) topology is source-pinned and the already validated q-CG backend survives the relevant local controls, but a full executable graph-to-component translation is not yet authorized because two categorical primitives remain unresolved at implementation level: the cup/qbar-dual translation and R/braiding.

## Frozen authority and production provenance

- preregistration commit: `f1702901a01bc921b46fe567188534bc3869b14a`
- initial implementation commit: `20a7e899d40d398560228a7584689fd657838691`
- run `34785449456`: diagnostic/non-authoritative because YAML parsed unquoted `null` lane as YAML null
- YAML-only fix: `3bce5a5e167cd5e1abb7242bbc6af0b008d62686`
- run `34785469014`: infrastructure failure before science because of a common parser SyntaxError
- parser/loader-only repair: `8848762adf769c96b742102698a3bf09b42bf6ef`; frozen scientific predicates unchanged
- authoritative production run: `34785590660`
- authoritative head: `8848762adf769c96b742102698a3bf09b42bf6ef`
- jobs: null `103800367454`; topology `103800367514`; normalization `103800367527`; primitives `103800367539`; aggregate `103800408850`
- artifacts:
  - topology `10326323267`, `sha256:8dc9cca72e99468abd24e7c4ec4646e05aba1bd32883710177fc504b9fffa4fb`
  - primitives `10325984205`, `sha256:5310b237df141688f61f88f20f67365cf0b0f761bc420836bd82b7eb04276a92`
  - normalization `10326780772`, `sha256:89da21eaff93642bb0fa49287375998e21fec2b73bf4429f222a191af305846a`
  - null `10325788178`, `sha256:dd0cdcd4cd761d8eb974f1b8492c5659951185155a802eb92b862076753b298f`
  - aggregate `10326193831`, `sha256:6b33f0c0c5ecceec1468c8f7d697851d2064d0cb3924db0a301cc01807ed287e`

All four raw artifacts and the frozen aggregate were consumed. Green CI was not used as a scientific PASS predicate.

## Lane results

### A — exact Eq.(27) topology: PASS

The fresh source bytes reproduce the historically pinned e-print digest `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`. Exactly one `eq:eprl-3-valent` environment is recovered. The frozen inventory is satisfied: two draw paths, four TikZ begin/end tokens, two internal sums, two closed `l` loops, and both primed and unprimed `J^+/J^-` pairs. Exact recovered snippet digest: `sha256:88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d`.

### B — executable primitive dictionary: BLOCKED

Already executable/qualified: q-number, quantum dimension, A7 admissibility, q-CG embedding, coproduct/action, bilinear A8/A9 contraction, and B2 cap.

Not yet executable-qualified:

1. `cup_qbar_dual` — the source explicitly supplies cup/cap and qbar-dual graphical relations, but the current RC006 backend has not yet converted the whole relation into an independently tested executable primitive.
2. `R_braiding` — no source-qualified executable R/braiding primitive exists in the current backend. No cancellation was assumed and no convention was invented.

These two items are sufficient for the frozen aggregate BLOCKED classification.

### C — Appendix-E normalization audit: parser-level false negative, not promoted to a scientific FAIL

The raw lane has `pass=false` only because the frozen lexical detector expected an explicit literal `E3` token that is not present in the TeX source. The preserved source context itself contains the target `Normalisation of EPRL model` derivation, explicitly evaluates the closed graph to

- the sign `(-1)^{sum_i j_i^+ + j_i^- - 2l}`,
- `(d_{l1} d_{l2} d_{l3} d_{l4})^{-1}`,
- `d_l^{-2}`,
- `delta_{l l'}`,

and derives `c_{\{l\}} = (-1)^{...}(prod_i d_{l_i})^alpha d_l^2` after introducing the measure-family freedom. Thus the literal-E3 test is a lexical parser defect. It is not used to override the independent primitive BLOCKED result and no frozen scientific threshold is weakened.

The executable B2 subcontrol itself remains strong: maximum residual up to the preregistered overall sign gauge is `1.056171682913856e-15` versus threshold `2e-9`.

### D — adversarial translation/null controls: PASS

The intact manifest is accepted. Removing the required quantum-dimension marker, dual marker, or orientation marker is rejected in all `3/3` controls; preregistration required at least `2/3`.

## Consequence

A bounded numerical Eq.(27) graph contraction is **not yet authorized**. The next admissible gate is a narrow source-faithful executable-primitives gate for cup/qbar-dual and R/braiding, including identity/duality controls and an audit of whether Appendix-F uses an explicit R operation or only a source-proven algebraic cancellation.

Still false: `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `eq29_amplitude_authorized`, `preferred_alpha_found`, `iter012_retry_authorized`. Candidate theory remains **UNFORMED / 0%**.