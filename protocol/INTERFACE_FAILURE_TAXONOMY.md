# ISQGR Interface-Failure Taxonomy v0.1

Status: **ACTIVE / PHASE-0**

An interface failure is a scoped obstruction in a required map between physical or mathematical layers. It is not a family-level refutation unless a separate coverage theorem establishes that conclusion.

## IF-01 — Ontology translation failure

Two mechanisms use primitives that cannot currently be embedded into a common parent object without losing essential structure.

Examples of questions:
- Can continuum fields and discrete relational data be represented in one state space?
- Is geometry fundamental or derived, and is there an explicit map between the two descriptions?

Terminal labels: `MAPPED`, `OPEN_BLOCKED`, `INTERFACE_FAILURE_SCOPED`.

## IF-02 — State-space incompatibility

A proposed synthesis lacks one common physical state space, generalized probabilistic structure, or controlled relation between the participating state descriptions.

Kill condition for a bridge: the maps preserve neither the physical quotient nor the claimed observable algebra.

## IF-03 — Dynamics/amplitude mismatch

Kinematics can be related, but the dynamical generators, amplitudes, constraints, or path-integral weights cannot be made compatible in one realization.

## IF-04 — Composition/gluing failure

Local amplitudes or subsystems exist, but there is no associative/consistent composition, gluing, refinement, or history-composition law carrying the relevant physical data.

This is a high-priority interface because a candidate parent principle should generally compose before it is trusted as a microscopic theory.

## IF-05 — Causality/locality mismatch

The frameworks assign incompatible status to causal order, locality or nonlocality, and no controlled map explains how the effective causal/local structure emerges.

A bridge must identify the operational causal object rather than only assert Lorentz invariance at the end.

## IF-06 — Gauge/relational-observable failure

A proposed common structure depends on gauge/coordinate artifacts, or the relational/gauge-invariant observable map is missing across the interface.

## IF-07 — Measure/normalization/positivity failure

The same realization lacks a finite or controlled measure, normalized amplitude/channel, physical positivity condition, or replacement principle with a recovery theorem.

Cutoffs or branch weights added solely to force normalization incur a maximal freedom tax unless derived independently.

## IF-08 — Continuum/coarse-graining failure

A microscopic construction exists, but the required continuum or macroscopic limit is not controlled, is nonunique, or does not preserve the structures used elsewhere in the argument.

## IF-09 — Lorentzian-recovery failure

A construction is Euclidean, combinatorial or otherwise non-Lorentzian in its controlled form, but the Lorentzian physical regime lacks a same-realization derivation.

## IF-10 — GR-recovery / parameter-identity failure

The candidate reaches an effective gravitational description but cannot demonstrate controlled recovery of GR (or a bounded deformation) with parameter identity maintained across scales.

## IF-11 — Matter/source-rule failure

The gravitational sector exists but the rule connecting quantum matter, stress-energy, conditional states, stochastic sources or operator-valued sources to the gravitational degrees of freedom is absent or inconsistent.

## IF-12 — UV/IR identity failure

The UV and IR descriptions use parameters or observables whose identity is assumed rather than derived through RG/coarse-graining/matching.

## IF-13 — Observable/comparator closure failure

Formal amplitudes exist, but no normalized observable can be carried through the same realization into a common comparator domain.

## IF-14 — Degeneracy / non-identifiability failure

A claimed distinctive mechanism produces an operational fingerprint degenerate with a classical, semiclassical, stochastic, hybrid or neighboring quantum model in the stated domain.

## IF-15 — Cross-school splice failure

A proposed synthesis requires results from incompatible realizations with no parent map. This is a methodological failure of the synthesis itself.

Any candidate that depends essentially on IF-15 remains `CANDIDATE_PARTIAL` or is rejected.

---

# Recurrent-motif rule

A recurrent motif is recorded only when:

1. at least two concrete realization chains exhibit the same interface class;
2. their source lineage is audited for dependence;
3. the failures are expressed at the same semantic level;
4. neither is merely `OPEN_BLOCKED` because a source object has not yet been located;
5. a candidate bridge would make a falsifiable structural difference.

Use motif labels `RM-001`, `RM-002`, ...

# Bridge-principle admission score

For ranking only, not truth probability:

`B = I + U + R + F - T - S`

where each component is scored 0–2:

- `I`: number/independence of interface tensions addressed;
- `U`: unification of independently successful mechanisms;
- `R`: rigidity / reduction of arbitrary freedom;
- `F`: falsifiability / cheap decisive tests;
- `T`: tuning/freedom tax;
- `S`: realization-splice penalty.

A bridge with `S=2` cannot be promoted until the splice is removed mathematically.

# Priority order for Phase 1

Start with interfaces most likely to constrain a parent architecture before detailed phenomenology:

1. IF-04 composition/gluing;
2. IF-02 state space;
3. IF-05 causality/locality;
4. IF-06 gauge/relational observables;
5. IF-07 normalization/positivity;
6. IF-08/09 continuum + Lorentzian recovery;
7. IF-10 GR recovery / parameter identity;
8. IF-11 matter/source rule;
9. IF-13/14 observables and degeneracy.

This ordering is a search heuristic and may not be used as evidence for any physical conclusion.