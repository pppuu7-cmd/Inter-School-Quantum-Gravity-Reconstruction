# ITER027 — RC006 bounded Eq.(27) component contraction

Date: 2026-09-14

## Terminal scientific classification

**`INVALID_IMPLEMENTATION — RC006_EQ27_TOPOLOGY_NOT_INSTANTIATED`**

This classification overrides neither the preserved raw lane outputs nor the raw workflow aggregate. It is a manual scientific verdict against the prospectively frozen ITER027 contract. Green CI is not a scientific PASS predicate.

ITER027 does **not** establish a bounded Eq.(27) component-contraction PASS, does not establish Eq.(29), does not authorize one-step TNR, and earns no bridge credit.

## Frozen contract

Preregistration: `prereg/ITER027_RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_2026-09-14.md`.

Prereg commit: `d07fd121f0abeb34396bb4f2bc4028070fed0e12`.

The frozen scientific question was whether the already source-pinned Eq.(27) graph could now be translated into a bounded component-level contraction using only the previously qualified q-CG, cap/cup, direct-source qbar and R/R^-1 primitives, with exact tensor-leg ordering, internal channels, source normalization and no Eq.(29)/Lambda or post-hoc convention repair.

ITER021 had already pinned the target Eq.(27) topology and recorded the decisive inventory: the `eq:eprl-3-valent` environment contains four TikZ blocks, two internal sums, two closed `l` loops, and both primed and unprimed `J^+/J^-` pairs. Those topology objects were part of the prerequisite authority for ITER027.

## Production history

Implementation commit: `fcb17f980caa82fd7a1a1482a523084125915d53`.

Initial workflow head: `95073389c83cf45851bb44473f972c89af6d3564`.

Run `34791069641` failed before substantive computation because `mpmath` was not installed while the frozen q-CG backend imports it. No science-lane evidence was produced. This is a pre-science infrastructure failure only.

A control-only workflow repair added the missing Python dependency and changed no hypothesis, physical object, source authority, panel, threshold, PASS/FAIL/BLOCKED/INVALID criterion or interpretation ceiling.

Repair commit / authoritative execution head: `b59fbc7a53ec2dda697826beb07550201052cd71`.

Corrected run: `34792339154`, completed `success` as an execution status.

Jobs:
- authority-domain `103818770258`
- component-translation `103818770467`
- bounded-contraction `103818770439`
- null-controls `103818770400`
- aggregate `103818814261`

Artifacts / digests:
- authority-domain `10327933057`, `sha256:8e643e02e4666411eac0d38f6017d48a6595f081cec40eeaf1b2e9fe150f72f9`
- component-translation `10328319002`, `sha256:019de16e9eac75c34031476a8e97ea92f5d9f611299528f1e416161254bb19ea`
- bounded-contraction `10328109395`, `sha256:c205e5207a2dd2e55ce6f2eb42b53499a88c6574b19426c940f6bc6e56cbc9c0`
- null-controls `10328775999`, `sha256:0f2d268ded37cbf3ef2ca2ee20d1e7f66b42ecfa57c30be97e02664de676a4dd`
- aggregate `10328698059`, `sha256:fe1369502a90c617e601d7d45a3d7620010dd516b24174b3191117b013e20411`

## Raw lane results retained

### Component-translation local primitive controls

Raw lane `pass=true`.

Across primary and held-out k panels, the direct-source qbar identity remained exact at machine representation (`max_source_identity = 0.0`) and the qbar intertwiner residual remained small (`max_qbar_intertwiner = 3.839616566770844e-15` versus frozen `5e-9`). Shape checks passed.

This is useful evidence that the already validated primitive stack transports cleanly into the ITER027 runtime. It is **not** by itself Eq.(27) component translation.

### Bounded-contraction local controls

Raw lane `pass=true`.

The code reports `max_dual_contraction = 8.671119018262734e-16` and `max_R_inverse = 7.224267142543843e-15` against the frozen `5e-8` tolerance; all tested values were finite; held-out k={7,9,11} used `alpha=0` without retuning.

The output explicitly records `full_eq27_amplitude_claimed=false`.

These calculations test local dual-pairing and braid-inverse identities. They do not instantiate the source-pinned Eq.(27) graph connectivity.

### Adversarial controls

Raw lane `pass=true`: 2/3 required wrong-structure controls were detected.

- legacy inverse-parameter qbar residual: `1.6579164156537258`
- R/R^-1 swap residual: `0.6214441724142149`
- wrong magnetic-order residual: `0.0`

The zero wrong-order residual is retained as a qualification: that particular frozen null control is insensitive on the chosen tested channel, although the preregistered 2/3 null criterion was met.

### Authority-domain lane

Raw lane `pass=false`, and the workflow aggregate therefore emitted `RC006_EQ27_COMPONENT_CONTRACTION_BLOCKED_AUTHORITY`.

This raw BLOCKED classification is **not scientifically accepted**. The lane searched the entire implementation source for forbidden dependency strings while the implementation itself literally contains the blacklist strings `formLambda6j`, `eq29_amplitude`, and `lambda_qbinomial`. Consequently the scanner detects its own blacklist definitions and makes its own authority predicate false. `missing=[]`; the apparent forbidden-dependency finding is a self-referential implementation false positive, not evidence that Eq.(29)/Lambda entered the contraction.

This defect alone would require implementation repair, not scientific BLOCKED.

## Decisive implementation-contract mismatch

The more fundamental defect is independent of the self-scanner bug.

The frozen gate is an Eq.(27)-specific graph-to-component contraction. The source-pinned Eq.(27) object contains the explicit topology recorded in ITER021: two internal sums, two closed `l` loops, internal `j` and `j_i^\pm/J^\pm` channels, primed/unprimed `J^+/J^-` data, and four graphical blocks whose connectivity must determine a component dictionary and contraction order.

The ITER027 production code never instantiates those Eq.(27) topology objects. Its science lanes operate on generic admissible triples `(a,b,c)` and evaluate:

- direct q-to-qbar coefficient identity / intertwining,
- a local dual contraction `F @ D`,
- a local braid inverse product `R^-1 @ R`,
- local wrong-structure controls.

There is no executable representation of the two `l` loops, no `j_i^\pm/J^\pm` component network, no primed/unprimed channel wiring, no summation over the source-defined Eq.(27) internal channels, and no component contraction of the four source graphical blocks.

Therefore the implementation studies necessary local primitives but not the frozen Eq.(27) contraction object. The successful local residuals cannot be promoted to `RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_VALIDATED_SCOPED`.

## Adversarial conclusion

The useful positive information survives only at the primitive-control level: qbar, duality and R/R^-1 identities remain numerically consistent over the frozen primary and held-out k panels, and two strong wrong-structure controls are detected.

No evidence from ITER027 supports a full or bounded Eq.(27)-topology contraction because that topology was not executed.

This is an implementation validity result, not a physical FAIL of RC006 and not a source-authority BLOCKED result.

## Authorization consequence

ITER027 is terminal. Do **not** silently patch it after seeing its outputs and do not convert its green execution into PASS.

The next admissible gate is a **new prospectively preregistered topology-faithful successor** (suggested ITER028) that must, before execution:

1. encode the exact ITER021 Eq.(27) source topology as an explicit machine-readable graph/component dictionary;
2. name every external and internal tensor leg and source-defined index order;
3. represent both closed `l` loops and all internal `j`, `j_i^\pm`, `J^\pm`, primed/unprimed channels;
4. freeze the precise summation ranges and admissibility rules at each internal channel;
5. place q-CG, cap/cup, direct-source qbar and R/R^-1 primitives only at source-authorized graph locations;
6. preserve the source normalization / alpha=0 slice without post-hoc rescaling;
7. include a positive control whose expected component contraction is independently known;
8. include topology-breaking controls (edge swap, loop removal/channel miswire, R crossing swap), not only primitive-level controls;
9. make an explicit PASS predicate on the Eq.(27)-topology contraction itself.

Only that new gate may determine whether bounded Eq.(27) component translation/contraction passes, fails, or is source-blocked.

Still false / locked:
- `iter012_retry_authorized`
- `eq29_amplitude_authorized`
- `one_step_tnr_authorized`
- `bridge_credit`
- `candidate_theory_authorized`
- `preferred_alpha_found`
- `new_physics_found`
- `ALL_KNOWN_SCHOOLS_FAIL`
- `NEW_QG_THEORY_REQUIRED`
- `UNIVERSAL_BRIDGE_FOUND`

Candidate theory remains **UNFORMED**.
