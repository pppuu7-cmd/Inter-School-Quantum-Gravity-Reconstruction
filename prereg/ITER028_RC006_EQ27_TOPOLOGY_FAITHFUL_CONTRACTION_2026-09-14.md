# ITER028 preregistration — RC006 topology-faithful Eq.(27) component contraction

Date: 2026-09-14

Status: `PREREGISTERED_NOT_EXECUTED`.

## Authorization basis

ITER026 terminalized `PASS — RC006_DIRECT_SOURCE_QBAR_PRIMITIVE_VALIDATED`, closing the executable qbar primitive under the exact source identity.

ITER027 is terminal `INVALID_IMPLEMENTATION — RC006_EQ27_TOPOLOGY_NOT_INSTANTIATED`. Its local qbar/duality/R controls are retained, but it did not execute the frozen Eq.(27) graph object and therefore gives no Eq.(27) PASS/FAIL/BLOCKED physics verdict.

ITER028 is a new scientific object and does not repair or overwrite ITER027.

## Frozen target hypothesis

`H028`: the exact source-pinned Eq.(27) graphical object in Dittrich–Schnetter–Seth–Steinhaus, arXiv:1609.02429v2, can be compiled into a complete component network using only already source-qualified RC006 primitives, and two independently implemented contractions of that network agree with the source Appendix-E reduction on prospectively frozen bounded sectors without post-hoc sign, orientation, tensor-order, normalization or channel repair.

This gate tests a source-faithful bounded realization of Eq.(27), not Eq.(29), not the historical one-step TNR benchmark, not a continuum/GR claim, and not an inter-school bridge.

## Frozen source/provenance authority

Primary target: arXiv:1609.02429v2.

Required exact e-print SHA256:

`3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

Required Eq.(27) source object: unique display carrying `\label{eq:eprl-3-valent}`.

Historical exact-source snippet digest from the source-pinned ITER021 extraction:

`sha256:88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d`.

The fresh ITER028 extraction must reproduce both the archive hash and the Eq.(27) snippet digest before any numerical lane is scientifically admissible. A mismatch is `INFRASTRUCTURE_OR_PROVENANCE_BLOCKED`, not a physical FAIL.

## Frozen prerequisite primitive set

Only the following may enter the Eq.(27) compiler/contraction:

1. q-number, quantum dimensions and admissibility/A7 from the target convention;
2. the validated ITER019/020 q-CG solver backend;
3. target bilinear A8/A9 convention;
4. source-gauged Appendix-B cap/cup primitives;
5. ITER026 direct-source qbar primitive using the exact ordered q<->qbar magnetic-index identity, with no inverse-q independent reconstruction;
6. ITER025B source-qualified R/R^-1 crossing convention;
7. the exact source graph and Appendix-E/F normalization chain extracted from the byte-pinned target source;
8. source measure slice `alpha=0` for the bounded contraction unless the exact Eq.(27)/Appendix-E source object itself requires an explicit different fixed factor.

Forbidden:

- Eq.(29) or Lambda machinery;
- `formLambda6j` / lambda-qbinomial objects;
- historical Iter012 TNR truncation;
- Hermitian absolute-square replacement of categorical bilinear pairing;
- fitted row/column phases or signs;
- choosing R versus R^-1 after numerical inspection;
- tensor-leg permutations not dictated by the source graph;
- per-channel gauge repair after seeing a mismatch;
- changing alpha/normalization after seeing outputs.

## Stage S — immutable source graph compiler prerequisite

Stage S runs before all substantive numerical lanes. It must emit a machine-readable graph/component dictionary and immutable extraction artifacts.

The compiler must mechanically recover and represent all of the following source-pinned Eq.(27) inventory:

- exactly one `eq:eprl-3-valent` display;
- four TikZ graphical blocks / source graphical factors as historically extracted;
- the two source `\sum` structures / internal sums;
- exactly two closed `l`-loop occurrences;
- internal `j` and all explicitly present `j_i^+`, `j_i^-`, `J^+`, `J^-` channels;
- both primed `(J^+)'`, `(J^-)'` and unprimed `J^+`, `J^-` labels;
- every source-written scalar prefactor, sign, quantum-dimension factor and normalization marker adjacent to the graph;
- every external and internal tensor leg, its direction/orientation and index order;
- every contraction edge and every summed magnetic/internal index;
- no unaccounted open magnetic leg in the displayed reduced amplitude.

The graph dictionary must contain stable node IDs, edge IDs, primitive type, ordered input/output legs, representation labels, summed/free indices, orientation/bend/crossing metadata, and source locator for every entry.

No edge, loop, orientation, crossing or index order may be supplied from memory or inferred from a visually plausible graph when the exact source does not determine it.

### Stage-S PASS

PASS only if:

1. fresh archive SHA and exact Eq.(27) snippet digest match the frozen values;
2. every inventory item above is represented exactly once where source-appropriate;
3. graph dictionary -> regenerated inventory reproduces the frozen source inventory;
4. every dictionary node/edge has a source locator or an explicit algebraic identity source anchor;
5. no unresolved graph-to-index ambiguity remains.

If an exact leg order, loop attachment, crossing direction, normalization factor or source locator is unresolved, Stage S terminal classification is `RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED`; numerical contraction must not run.

## Frozen bounded sectors

Primary source sector:

- `k=12`;
- source free-spin samples `j=1,2,3` exactly where the extracted Eq.(27)/Appendix-E formula defines complete admissible samples.

If the source graph requires additional external labels to make those samples complete, Stage S must freeze them mechanically from the same source/table/formula context **before** any contraction runs. They may not be selected by numerical agreement.

Independent undeformed sentinel:

- q=1 replacement using the same graph dictionary, same leg ordering and same contraction engines, with only the q-deformed algebra replaced by its undeformed counterpart.

No additional finite-k held-out sector may be added after numerical outputs are observed. A future transport panel, if scientifically useful, requires a separate preregistration.

## Parallel execution design after Stage S

After Stage S passes, the following lanes may run concurrently with `fail-fast:false`. They consume the same immutable Stage-S graph dictionary and source artifact hashes. No lane may change another lane's criteria or graph data.

### Lane A — network/einsum contraction

Compile the full frozen Eq.(27) graph dictionary into a tensor-network/einsum style contraction.

For every frozen k=12 sample:

- instantiate every source node with only the qualified primitive set;
- sum every internal magnetic and representation channel specified by Stage S;
- include both closed l loops and all primed/unprimed channel wiring;
- preserve every source scalar/sign/dimension/normalization factor;
- return the complete bounded closed scalar for the displayed Eq.(27) object.

No generic-triple surrogate or isolated `F@D` / `R^-1 R` identity counts as Eq.(27) execution.

### Lane B — independent explicit-index reference contraction

Implement the same immutable graph dictionary as explicit nested index/channel sums without calling the Lane-A network/einsum contraction routine and without importing a cached Lane-A result.

Shared primitive tensors and immutable graph metadata are allowed; contraction-order code and summation implementation must be independently written.

For every frozen k=12 sample, Lane B returns the full closed scalar.

This lane is required to detect wiring/contraction-engine errors common to a single implementation.

### Lane C — Appendix-E source reduction comparator

Independently evaluate the exact Appendix-E reduction (E1–E4, including the E3/E4 closed-form factors actually applicable to the frozen samples) from source-qualified algebra, without numerically reusing Lane A or B's final scalar.

The comparator must retain the source outer-label delta, signs and all quantum-dimension factors and must use categorical bilinear pairing rather than Hermitian modulus-square convenience.

### Lane D — q=1 instrumentation sentinel

Using the identical Stage-S graph dictionary and both contraction implementations, replace only q-deformed q-numbers/dimensions/actions/q-CG data by the undeformed q=1 backend.

The graph, index order, normalization and channel wiring are unchanged.

Compare Lane-A and Lane-B q=1 contractions with the q=1 reduction of the same Appendix-E source expression.

This lane gives zero finite-k or bridge credit; it is a graph/compiler sentinel.

### Lane E — source-number / normalization sentinel

Mechanically recover the exact source meaning of the historical printed values and reproduce, where the Stage-S source context confirms the same definitions:

- `N13(alpha=4) = 7.41492`
- `N13(alpha=8) = 1.399277`
- `N14(alpha=4) = -1.931582`
- `N14(alpha=8) = -3.861564`

and the source-stated k=12 cancellation leading to the vanishing `l=3` contribution.

The exact definitions of N13/N14/alpha and cancellation factors must come from source context; if the source object cannot be unambiguously tied to these sentinels, classify this lane `BLOCKED_SENTINEL_IDENTITY` rather than guessing.

### Lane F — topology-breaking adversarial controls

On one smallest complete nontrivial source-defined k=12 sample, run prospectively frozen wrong graph variants independently:

1. swap one source-ordered pair of tensor legs on a non-symmetric node;
2. remove or miswire one of the two closed l loops;
3. erase the primed/unprimed distinction on one J-channel connection;
4. swap a source R crossing with R^-1 where the source graph requires that crossing;
5. replace qbar/cap-cup duality by ordinary Hermitian conjugation;
6. remove one source quantum-dimension normalization factor.

A wrong variant is detected if it violates a source identity/inventory predicate or changes the independently agreed correct closed scalar by absolute or relative `>1e-6` on the frozen sample.

The lane PASS requirement is at least 4/6 detected wrong variants **and** mandatory detection of both (2) l-loop removal/miswire and (3) primed/unprimed channel erasure. If either mandatory topology control is structurally inapplicable under the exact source dictionary, this is `INVALID_CONTROL_DESIGN`, not an automatic PASS.

## Frozen numerical tolerances

For each k=12 source-defined sample:

- Lane A vs Lane B: absolute and relative agreement `<=1e-10`;
- each of Lane A and B vs Lane C Appendix-E reduction: absolute and relative agreement `<=1e-8`;
- residual allowed channel-sign gauge changes must leave the final closed scalar invariant to `<=1e-10`;
- all scalars must be finite;
- source-number printed sentinels: absolute error `<=5e-6` where source identity is unambiguous;
- exact source cancellation sentinel: residual `<1e-10`.

No tolerance may be relaxed after substantive output is observed.

## Positive controls

Required before a scientific PASS:

1. Stage-S archive/snippet hash match and exact topology inventory match;
2. the previously validated B2/cup/qbar and R/R^-1 local identities remain within their historical qualified thresholds when loaded by ITER028;
3. Lane A and Lane B agree on a deliberately simple source-derived subgraph whose Appendix-B/E evaluation is analytically known before the full Eq.(27) sample is evaluated;
4. q=1 graph/compiler sentinel passes with the identical topology dictionary.

## Terminal scientific classes

### PASS — `RC006_EQ27_TOPOLOGY_FAITHFUL_COMPONENT_CONTRACTION_PASS_SCOPED`

Only if Stage S and all required Lanes A–F PASS and, for every frozen source-defined k=12 sample:

- the complete Eq.(27) source topology is instantiated;
- both independent contractions agree;
- both agree with the independent Appendix-E source reduction;
- all positive controls pass;
- Lane-F adversarial calibration passes;
- no source ambiguity or post-hoc repair occurs.

### FAIL — `RC006_EQ27_TOPOLOGY_FAITHFUL_COMPONENT_MISMATCH`

Only if Stage S fully source-qualifies the graph and all required objects exist, but the two independent full graph contractions and/or source Appendix-E comparator disagree beyond frozen tolerance, a required complete contraction is non-finite, or a source-defined identity fails under the exact frozen implementation.

A local primitive failure alone must identify the exact failed dependency and may require a narrower dependency FAIL/qualification; it must not be silently promoted to a family-level or school-level verdict.

### BLOCKED — `RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED`

If any exact source graph-to-index relation, loop attachment, tensor order, internal summation range, crossing, normalization or comparator identity required by the full frozen Eq.(27) object remains source-ambiguous or unavailable.

### INVALID

`INVALID_IMPLEMENTATION` if the code does not instantiate the Stage-S graph dictionary or substitutes primitive/local identities for the full graph object.

`INVALID_PROVENANCE` if source/artifact identity cannot be verified.

`INVALID_CONTROL_DESIGN` if prospectively mandatory topology controls are not meaningful for the compiled object.

Infrastructure failures before substantive evaluation are non-scientific and may receive a control-only retry with the identical frozen scientific contract.

## Interpretation ceiling

Even a full ITER028 PASS establishes only:

> a bounded, source-faithful component realization and internal validation of target Eq.(27) for the prospectively frozen reduced Euclidean RC006 sectors.

It does **not** establish Eq.(29)/Lambda, one-step TNR flow, preferred alpha, Lorentzian EPRL, continuum/GR recovery, an inter-school bridge, a universal parent principle, new physics, or a candidate theory.

Only a full ITER028 PASS may authorize consideration of a separately preregistered next-layer TNR/refinement test. It does not automatically authorize the historical ITER012 object without a fresh dependency/provenance review.

## Claim locks

Always false during ITER028:

`iter012_retry_authorized`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.

Candidate theory remains `UNFORMED`.
