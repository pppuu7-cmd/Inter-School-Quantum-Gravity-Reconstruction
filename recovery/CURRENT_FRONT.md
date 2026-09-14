# Current front — ISQGR

Date: 2026-09-14.

Candidate theory: **UNFORMED / 0%**. Overall programme roadmap readiness remains **49%**; this is not a correctness probability.

## Reconciled lineage through ITER027

The historical ITER024/025 A/B collision remains resolved by `results/ITER024_025_AB_PROVENANCE_RECONCILIATION_2026-09-14.md`.

- ITER025B established exact source authority for ordered q<->qbar components and R/R^-1 crossing.
- ITER026 prospectively executed the direct-source qbar identity and terminalized `PASS — RC006_DIRECT_SOURCE_QBAR_PRIMITIVE_VALIDATED` across domain, algebra, cup, four-valent and adversarial lanes.
- This authorized only a separately preregistered bounded Eq.(27) component translation/contraction.

## ITER027 terminal INVALID_IMPLEMENTATION

Preregistration: `prereg/ITER027_RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_2026-09-14.md`, prereg commit `d07fd121f0abeb34396bb4f2bc4028070fed0e12`.

Implementation commit: `fcb17f980caa82fd7a1a1482a523084125915d53`.

Initial run `34791069641` failed before science because the workflow omitted the `mpmath` dependency required by the frozen q-CG backend. This is a pure infrastructure failure. A control-only repair added `mpmath` without changing the frozen scientific contract; repair / authoritative execution head: `b59fbc7a53ec2dda697826beb07550201052cd71`.

Corrected run `34792339154` completed. All four independent matrix lanes executed and raw artifacts were preserved.

Raw lane outcomes:

- `component-translation`: local primitive controls PASS; `max_source_identity=0.0`, `max_qbar_intertwiner=3.839616566770844e-15`.
- `bounded-contraction`: local duality/braid controls PASS; `max_dual_contraction=8.671119018262734e-16`, `max_R_inverse=7.224267142543843e-15`, held-out k=7,9,11 not retuned, `full_eq27_amplitude_claimed=false`.
- `null-controls`: PASS under frozen 2/3 rule; legacy inverse-qbar and R/R^-1-swap controls give O(1) residuals, while the chosen wrong-magnetic-order control is insensitive (`0.0`).
- `authority-domain`: raw `pass=false`, but this is an implementation false positive because the scanner searches the whole implementation file for forbidden strings that are literally present in its own blacklist definitions. `missing=[]`.

The raw aggregate therefore emitted `RC006_EQ27_COMPONENT_CONTRACTION_BLOCKED_AUTHORITY`. That raw classification is retained for provenance but is **not** the scientific terminal verdict.

### Decisive contract mismatch

ITER021 source-pinned the exact Eq.(27) topology: four graphical blocks, two internal sums, two closed `l` loops, and both primed/unprimed `J^+/J^-` channel pairs.

The ITER027 production code does not instantiate that topology. It operates on generic admissible triples and evaluates direct qbar/intertwiner identities, local dual contraction `F @ D`, local braid inverse `R^-1 @ R`, and local null controls. It does **not** encode or contract:

- the two source-defined closed `l` loops;
- the internal `j`, `j_i^+`, `j_i^-`, `J^+`, `J^-` network;
- primed/unprimed channel wiring;
- the four Eq.(27) graphical blocks and their exact component connectivity.

Therefore the code tests necessary validated primitives but not the frozen Eq.(27) contraction object.

Terminal scientific classification:

**`INVALID_IMPLEMENTATION — RC006_EQ27_TOPOLOGY_NOT_INSTANTIATED`**.

Durable report: `results/ITER027_RC006_EQ27_BOUNDED_COMPONENT_INVALID_IMPLEMENTATION_2026-09-14.md`, commit `cad509649420b79a46b4c8e08616865e35673a0f`.

Recovery state updated at commit `f02fa60670bcb8afa905bdef2535c786a81fcfe6`.

This is not a physical FAIL of RC006, not a source-authority BLOCKED result, and not bridge evidence. The local primitive PASSes remain useful controls but cannot be promoted to Eq.(27) PASS.

## Exact next admissible gate

Create a **new prospectively preregistered topology-faithful Eq.(27) successor**. Do not silently patch ITER027 after observing its outputs.

Before substantive execution the successor must freeze and encode:

1. the exact source-pinned Eq.(27) graph as a machine-readable component dictionary;
2. every external/internal tensor leg and its index order;
3. both closed `l` loops;
4. all internal `j`, `j_i^\pm`, `J^\pm`, primed/unprimed channels;
5. exact admissibility and summation ranges;
6. source-authorized placement of q-CG, cap/cup, direct-source qbar and R/R^-1 primitives;
7. alpha=0/source normalization without post-hoc rescaling;
8. primary and held-out k/spin panels;
9. an independently known positive contraction control;
10. topology-breaking negative controls: edge/channel swap, loop removal or miswire, and R/R^-1 crossing swap;
11. an explicit PASS/FAIL/BLOCKED/INVALID predicate on the Eq.(27)-topology contraction itself.

Only after this successor terminalizes may Eq.(27) be called validated or failed in bounded scope.

## Locks

Still false: `iter012_retry_authorized`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.

BH004/BH004B remains scoped-negative; genuine multivertex Lorentzian refinement remains source-blocked; RC008 and RC009 remain blocked; Lorentzian Delta4 remains saturated-negative in scope.
