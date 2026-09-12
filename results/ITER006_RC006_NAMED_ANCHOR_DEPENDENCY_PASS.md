# ITERATION 006 — RC006 named-anchor dependency audit

Date: 2026-09-12

## Provenance

Prospective script commit: `06b550cbd6e18b5b83c4bed7fdc82a3646884496`  
Workflow/head: `b55fb9e340094df4c2608b0cae6351d680521859`  
Authoritative run: `34699750791`  
Aggregate job: `103569310624`  
Aggregate artifact: `10299468120`  
Aggregate digest: `sha256:4c53da18b01ecd10c60d8bfbca74bce99961ef7c0f065ded597bce70e9628fe4`

This gate used only exact internal TeX labels already qualified by the previous 6/6 reference-chain gate. It did not relax the failed lexical gate, use picture geometry, or infer an amplitude from rendered diagrams.

## Raw result

All seven prospectively frozen lanes passed:

- `app:EPRL-diagram`;
- `app:EPRL-norm`;
- `app:graph`;
- `eq:BC-3-int`;
- `eq:BC-3-valent`;
- `eq:eprl-3-valent`;
- `dependency_connectivity`.

Aggregate: `7/7 PASS`, `all_pass=true`.

The source label/reference dependency graph contains `52` labelled nodes and `69` resolved structural edges. Starting from the six shared Eq.(29)/EPRL/BC anchors, five preregistered downstream targets are reachable:

- `eq:SVD`;
- `eq:eprl-map`;
- `eq:recoupling-basis`;
- `eq:svd`;
- `fig:recoupling`.

The preregistered target `6j-def` is **not** reachable under this specific nearest-preceding-label structural graph. That negative is preserved; the gate passed because connectivity required at least one downstream recoupling/EPRL-map target, not all targets.

Connectivity artifact: `10300315926`, digest `sha256:ccc7e9b938d7674b4c0c8a9cabdd0f1cd5a1330536f65d21c807f6f9e1104734`.

## Scientific classification

`PASS_NAMED_SOURCE_ANCHOR_DEPENDENCY_PREREQUISITE_ONLY`.

This materially narrows the remaining Eq.(29) mapping problem. The named source anchors are unique source objects with nonempty contexts, and the internal source dependency graph explicitly connects the Eq.(29)/EPRL/BC component to EPRL-map, recoupling and SVD structures.

It still does **not** prove a unique oriented/braided tensor contraction. Structural reachability is weaker than exact tensor-index ordering, and the non-reachability of `6j-def` means a direct 6j-definition authority cannot be silently imported from this graph.

## Next allowed gate

Freeze an exact math-environment / symbol-incidence / tensor-ordering audit for the qualified named anchors. It must distinguish explicit source ordering from mere co-occurrence and must report ambiguity rather than choose an ordering. Only a source-unique contraction-ready mapping may unlock the minimal `k=12, gamma=1/3` Eq.(29) amplitude.

## Claim locks

No Eq.(29) numerical amplitude, Appendix-C TNR flow, refinement bridge, continuum limit, `BRIDGE_DERIVED`, new physics, or candidate theory follows from this prerequisite PASS.
