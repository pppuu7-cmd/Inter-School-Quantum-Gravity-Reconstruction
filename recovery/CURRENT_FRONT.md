# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**; this is not a correctness probability.

## Reconciled lineage through ITER027

ITER025B established exact source authority for ordered q<->qbar components and R/R^-1 crossing. ITER026 prospectively executed the direct-source qbar identity and terminalized `PASS — RC006_DIRECT_SOURCE_QBAR_PRIMITIVE_VALIDATED`.

ITER027 then attempted the separately preregistered bounded Eq.(27) gate. Its first run `34791069641` failed before science because the workflow omitted `mpmath`; an exact control-only dependency repair produced corrected run `34792339154`.

The corrected run executed four independent matrix lanes. Local primitive controls were strong: qbar/intertwiner, dual-pairing and R/R^-1 identities passed on primary and held-out panels, and two strong wrong-structure controls were detected. However, the authority-domain lane contained a self-referential blacklist false positive, and more importantly the implementation never instantiated the source-pinned Eq.(27) topology itself. It did not encode/contract the two closed l loops, internal j/j_i^+/j_i^-/J^+/J^- network, primed/unprimed channel wiring, or the four source graphical blocks.

Therefore ITER027 is terminal:

**`INVALID_IMPLEMENTATION — RC006_EQ27_TOPOLOGY_NOT_INSTANTIATED`**.

Durable report: `results/ITER027_RC006_EQ27_BOUNDED_COMPONENT_INVALID_IMPLEMENTATION_2026-09-14.md`, commit `cad509649420b79a46b4c8e08616865e35673a0f`.

This is not a physical FAIL of RC006 and not a source-authority BLOCKED result. Its local primitive PASSes remain controls only.

## ITER028 prospectively frozen — NOT EXECUTED

A new successor has now been preregistered before any substantive ITER028 implementation or numerical result:

`prereg/ITER028_RC006_EQ27_TOPOLOGY_FAITHFUL_CONTRACTION_2026-09-14.md`

Prereg commit:

`73246639c6710ab3e7228c3e5f0f11ae654f32b7`

Status: **`PREREGISTERED_NOT_EXECUTED`**.

### Exact frozen source object

Primary target: arXiv:1609.02429v2.

Required source archive SHA256:

`3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

Required historical exact Eq.(27) source-snippet SHA256 from ITER021:

`88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d`.

The source topology inventory remains the ITER021 inventory: the unique `eq:eprl-3-valent` display, four graphical blocks, two internal sums, two closed `l` loops, internal `j`/`j_i^+`/`j_i^-`/`J^+`/`J^-` channels and both primed/unprimed J pairs, together with every source scalar/sign/dimension/normalization factor and exact tensor-leg/index order.

### Required Stage S

ITER028 begins with an immutable source graph compiler. It must emit a machine-readable component dictionary with stable node/edge IDs, ordered legs, summed/free indices, representation labels, orientation/bend/crossing metadata and source locator for every entry.

If any exact leg order, loop attachment, crossing, summation range, normalization or graph-to-index relation remains unresolved, Stage S must terminalize `RC006_EQ27_SOURCE_GRAPH_COMPONENT_MAP_BLOCKED`; no numerical graph contraction may run.

### Parallel lanes after Stage S

Only after Stage S passes may six independent lanes run concurrently with `fail-fast:false`, all consuming the same immutable graph dictionary:

1. full tensor-network/einsum Eq.(27) contraction;
2. independently written explicit nested-index/channel-sum contraction;
3. independent Appendix-E E1–E4/E3–E4 source reduction comparator;
4. q=1 graph/compiler sentinel using the identical topology;
5. historical source-number/normalization sentinel where exact source identity is unambiguous;
6. topology-breaking adversarial controls.

The two full contraction engines may share source-qualified primitive tensors and frozen graph metadata, but may not share contraction-order code or a cached final scalar.

### Frozen primary scope

Primary target is k=12 with source-defined free-spin samples `j=1,2,3` only where Stage S can mechanically complete all additional labels from the same exact source context before numerical execution.

No post-result finite-k panel expansion is allowed inside ITER028.

### Frozen adversarial topology controls

At minimum test: non-symmetric leg swap, removal/miswire of one l loop, primed/unprimed J-channel erasure, R/R^-1 swap where source-required, Hermitian replacement of qbar/cap-cup duality, and removal of one source quantum-dimension factor.

At least 4/6 must be detected, with l-loop removal/miswire and primed/unprimed erasure mandatory. If a mandatory control is structurally inapplicable, verdict is `INVALID_CONTROL_DESIGN`, not automatic PASS.

### Frozen scientific PASS ceiling

Only full Stage-S + all-lane PASS may establish:

`RC006_EQ27_TOPOLOGY_FAITHFUL_COMPONENT_CONTRACTION_PASS_SCOPED`.

That would mean only a bounded, source-faithful component realization/internal validation of target Eq.(27) in the frozen reduced Euclidean RC006 sectors. It would not establish Eq.(29), TNR flow, preferred alpha, Lorentzian EPRL, GR recovery, a bridge, a parent principle, new physics or a candidate theory.

## Exact next action

Implement the already-frozen ITER028 Stage S **without changing its scientific contract**. If Stage S passes, launch the six post-Stage-S lanes in parallel through GitHub Actions and assemble exactly one aggregate scientific verdict after all required lanes are terminal.

Do not create a competing Eq.(27) gate. Do not reuse ITER027 local identities as a substitute for topology execution. Do not alter thresholds, source topology, k/spin scope or controls after seeing results.

Recovery state registering ITER028 preregistration: commit `75d0beaddf8a987a3066e2c7268102d8706109bb`.

## Locks

Still false: `iter012_retry_authorized`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.

BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.
