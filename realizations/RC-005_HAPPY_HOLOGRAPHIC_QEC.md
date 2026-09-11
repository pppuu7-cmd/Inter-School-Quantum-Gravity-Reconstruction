# RC-005 — HaPPY holographic quantum-error-correcting tensor network

Status: `MECHANISM_MAPPED / TOY_MODEL`  
Family: `F09 quantum-information / tensor-network emergent geometry` with relevance to `F07 holography`  
Date: 2026-09-12

## Sources

- F. Pastawski, B. Yoshida, D. Harlow, J. Preskill, *Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence* (2015), https://arxiv.org/abs/1503.06237
- S. Ryu, T. Takayanagi, *Holographic Derivation of Entanglement Entropy from AdS/CFT* (2006), https://arxiv.org/abs/hep-th/0603001
- T. Takayanagi, *Emergent Holographic Spacetime from Quantum Information* (2025), https://arxiv.org/abs/2506.06595

Evidence class: `SOURCE_GROUNDED / EXACT_TOY_MODEL`.

## Scope firewall

HaPPY is **not** a complete model of quantum gravity. It is used here only as a concrete exactly soluble mechanism showing how quantum-information structure, tensor-network composition and geometric/entropic relations can coexist.

No conclusion from this card may be promoted directly to generic AdS/CFT, realistic gravity or cosmology.

## Native definition

- **Primitive state structure:** bulk and boundary Hilbert spaces connected by an isometric encoding map.
- **Building blocks:** perfect tensors with maximal entanglement properties across bipartitions.
- **Composition:** tensor contraction assembles the network; the full network acts as an encoder from bulk logical degrees of freedom to boundary physical degrees of freedom.
- **Entanglement/geometry link:** the model reproduces key holographic entanglement features and, in many cases, the Ryu–Takayanagi relation exactly within the toy construction.
- **Redundancy/QEC structure:** bulk logical operators admit multiple boundary representations in appropriate regions, modelling quantum-error-correcting aspects of bulk reconstruction.
- **Causal object:** a fundamental Lorentzian causal order is **not** supplied by the basic static HaPPY construction.
- **Dynamics:** `NOT_APPLICABLE / TOY_STATIC_ENCODING` for a full gravitational time-evolution law.

## Scale / recovery map

- **Geometry emergence:** network connectivity/entanglement structure supports an emergent hyperbolic geometric interpretation.
- **Continuum:** `OPEN_BLOCKED` for a controlled continuum gravitational theory.
- **Lorentzian recovery:** `OPEN_BLOCKED`.
- **GR dynamics:** `NOT_ESTABLISHED`.
- **Matter/source rule:** `NOT_APPLICABLE` at the level of this mechanism card.

## Operational map

- The model has exact Hilbert-space, isometry and quantum-channel/QEC language.
- It is therefore unusually strong for physical-state positivity/normalization at the toy-model level.
- Direct RQIR Q1–Q7 gravity mapping: `NOT_AUTHORIZED` because full gravitational dynamics are absent.

## Interface audit

- IF-01 ontology translation: `MAPPED_PARTIAL`
- IF-02 state space: `MAPPED`
- IF-03 dynamics/amplitude: `NOT_APPLICABLE / TOY_STATIC_ENCODING`
- IF-04 composition/gluing: `MAPPED`
- IF-05 causality/locality: `OPEN_BLOCKED` for Lorentzian causality
- IF-06 gauge/relational observables: `NOT_YET_AUDITED`
- IF-07 measure/normalization/positivity: `MAPPED_PARTIAL` at code/isometry level
- IF-08 continuum/coarse graining: `OPEN_BLOCKED`
- IF-09 Lorentzian recovery: `OPEN_BLOCKED`
- IF-10 GR recovery/parameter identity: `NOT_ESTABLISHED`
- IF-11 matter/source rule: `NOT_APPLICABLE`
- IF-12 UV/IR identity: `NOT_YET_AUDITED`
- IF-13 observable/comparator closure: `MAPPED_PARTIAL` only for quantum-information observables
- IF-14 degeneracy/non-identifiability: `NOT_YET_AUDITED`
- IF-15 cross-school splice: `NOT_APPLICABLE`

## BH-001 test relevance

RC-005 exposes a second kind of composition very clearly: **parallel/subsystem composition and encoding by tensor contraction**, rather than causal succession.

This does not match RC-004 causal order semantically. Treating both as one undifferentiated `star` would create a false synthesis.

### Cheapest decisive next tests

1. Split BH-001 into sequential/causal composition and parallel/subsystem composition.
2. Ask whether one scale/refinement map can preserve both structures and their compatibility relation.
3. Test whether entanglement-generated geometric data can coexist with an independently defined causal-order sector without adding a target metric by hand.

## Promotion decision

- Can contribute to a recurrent motif? **YES AS MECHANISM EVIDENCE ONLY**, not as a full QG realization.
- Candidate motif must be phrased at the level of compositional structure, not gravity completeness.

## Claim lock

Exact success of HaPPY as a tensor-network/QEC toy model is not evidence that real spacetime literally is a HaPPY network.