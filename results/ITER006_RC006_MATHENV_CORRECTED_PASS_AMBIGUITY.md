# ITERATION 006 — RC006 corrected named-anchor MathEnv / symbol-incidence audit

Date: 2026-09-12

## Provenance

Frozen-science gate originally preregistered before run `34699899382`. That first run was measurement-invalid because its parser could select the entire `document` environment and tokenize prose; see `results/ITER006_RC006_MATHENV_RUN1_IMPLEMENTATION_INVALID.md`.

Minimal parser-only fix: `508764118d551fb1e85a1eee6730d52e7e732db6`. Frozen thresholds and interpretation rules were unchanged.

Corrected authoritative run: `34699987643`  
Aggregate job: `103570011082`  
Aggregate artifact: `10299503360`  
Aggregate digest: `sha256:7171b1e3aebf00a7a0b286202328cef5b71453cd88c67d010133efdb79639f8b`

## Raw result

All nine corrected lanes passed the unchanged frozen gate: `9/9 PASS`, `all_pass=true`.

The corrected `symbol_incidence` job `103569919405`, artifact `10299842274`, digest `sha256:21f040a995c42ef1a0067c8ce3b16d72a82ced4c14bac6620214a1a5ab12ac9c`, records:

- all eight named source anchors unique;
- environments: `app:EPRL-diagram`, `app:EPRL-norm`, `app:graph` use bounded `LOCAL_BLOCK`; `eq:BC-3-int`, `eq:BC-3-valent`, `eq:eprl-map` use exact `equation`; `eq:eprl-3-valent`, `eq:recoupling-basis` use exact `align`;
- `shared_symbol_count = 16` between the Eq29/EPRL/BC group and downstream EPRL-map/recoupling group;
- `distinct_ordered_token_signatures = 8`;
- `ambiguity_preserved = true`.

The shared token set includes `J`, `T`, `j`, `l`, `m`, `n`, `sum`, `hat`, `otimes` and diagram-source operators, after prose-token contamination was removed.

## Scientific classification

`PASS_EXACT_SOURCE_MATHENV_SYMBOL_INCIDENCE_PREREQUISITE_ONLY / TENSOR_ORDERING_NOT_UNIQUE_AT_THIS_ABSTRACTION`.

This is a valid source-qualification PASS: the qualified source anchors expose stable machine-readable math/diagram objects and a nonempty shared symbol incidence. It is **not** a contraction-map PASS. The frozen ambiguity lane explicitly produces eight distinct ordered signatures, so source symbol incidence by itself does not identify one oriented/braided tensor ordering.

## Consequence

`RC006_EQ29_ORIENTED_BRAIDED_GRAPH_MAPPING_GATE` remains OPEN/BLOCKED. The minimal `k=12, gamma=1/3` numerical Eq.(29) amplitude is still forbidden.

The next allowed object is a stricter leg-order identifiability audit using decorated source indices and explicit equation/diagram-source incidence. It must report non-identifiability if multiple leg permutations preserve all extracted source constraints; it may not choose one by geometry or convention.

## Claim locks

No Eq.(29) amplitude, Appendix-C TNR flow, held-out transport, `BRIDGE_DERIVED`, continuum limit, new physics, or candidate theory follows.
