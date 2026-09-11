# ISQGR Inter-School Interface Atlas v0.1

Status: **SEED / FAMILY_LEVEL_NOT_EVIDENCE**  
Date: 2026-09-12

This document is a navigation layer. No row below is benchmark evidence until grounded in a concrete realization and source record.

## 1. Common atlas coordinates

Each realization will be mapped onto the same coordinates:

`P` primitive ontology  
`S` state structure  
`D` dynamics/amplitude  
`C` composition/gluing  
`K` causal object  
`L` locality status  
`G` gauge/relational structure  
`M` measure/normalization/positivity  
`R` renormalization/coarse graining  
`X` continuum/Lorentzian map  
`E` Einstein/GR recovery  
`Q` quantum-matter/source rule  
`O` normalized observables / RQIR Q1–Q7 mapping

A school family is represented as a partial path through these coordinates, never as a single yes/no score.

## 2. Family navigation matrix

| ID | Family | Characteristic starting point | Main atlas coordinates to inspect first | Status |
|---|---|---|---|---|
| F01 | GR + quantum-gravity EFT | continuum Lorentzian metric + QFT/EFT | E,Q,O,R | FAMILY_LEVEL_NOT_EVIDENCE |
| F02 | semiclassical / stochastic gravity | classical metric coupled to quantum expectation/fluctuation structures | Q,M,O,K | FAMILY_LEVEL_NOT_EVIDENCE |
| F03 | asymptotic safety | quantum field theory + nontrivial UV RG behavior | R,E,X,Q | FAMILY_LEVEL_NOT_EVIDENCE |
| F04 | canonical LQG / spinfoams | quantum geometry / constrained amplitudes | P,S,D,C,G,X,E | FAMILY_LEVEL_NOT_EVIDENCE |
| F05 | causal dynamical triangulations | Lorentzian lattice path integral with dynamical triangulations | D,C,K,R,X,E | FAMILY_LEVEL_NOT_EVIDENCE |
| F06 | causal set theory | locally finite causal order | P,K,L,D,X,E | FAMILY_LEVEL_NOT_EVIDENCE |
| F07 | string/M-theory + holography | extended quantum degrees / duality / boundary quantum system | S,D,C,R,E,O | FAMILY_LEVEL_NOT_EVIDENCE |
| F08 | group field theory / tensor models | combinatorial/group-theoretic many-body building blocks | P,S,D,C,R,X | FAMILY_LEVEL_NOT_EVIDENCE |
| F09 | quantum-information / tensor-network emergent geometry | entanglement/circuit/information structure | P,S,C,L,X,O | FAMILY_LEVEL_NOT_EVIDENCE |
| F10 | thermodynamic / induced / emergent gravity | macroscopic/collective gravitational dynamics | P,R,E,Q,O | FAMILY_LEVEL_NOT_EVIDENCE |

## 3. Search principle

ISQGR does not ask which whole family is correct. It searches for **cross-family structural corridors** where:

- two or more approaches preserve a successful mechanism;
- they disagree on what is fundamental;
- the disagreement can be represented as a missing map between atlas coordinates;
- a common parent principle could reduce assumptions rather than add tunable freedom.

The first three corridors are deliberately chosen to be conceptually distinct.

---

# Corridor A — Composition / refinement / continuum

**Families initially sampled:** F04 spinfoams/LQG, F05 CDT, F08 GFT/tensor models, with F03 asymptotic safety as a continuum-RG comparator.

### Shared target

Explain how microscopic quantum gravitational building blocks compose and how a controlled macroscopic gravitational regime emerges.

### Tension candidate

Different programmes place the fundamental weight on different objects — constrained transition amplitudes, triangulated histories, many-body/group-field quanta, or continuum RG flow — yet all ultimately require a stable notion of composition plus scale change.

### Atlas path

`S/D -> C -> R -> X -> E`

### Primary interface classes

- IF-04 composition/gluing
- IF-08 continuum/coarse graining
- IF-09 Lorentzian recovery
- IF-10 GR recovery / parameter identity
- IF-12 UV/IR identity

### First bridge question

> Is there a representation-independent composition/refinement law whose fixed or stable structures generate both a continuum RG description and discrete gravitational amplitudes as different representations?

### Kill condition

If candidate composition laws that reproduce one side necessarily destroy gauge/constraint structure, positivity, or same-realization continuum recovery on the other side, the corridor does not support a common bridge.

Status: `TENSION_CANDIDATE / NOT_YET_SOURCE_AUDITED`

---

# Corridor B — Causal order / entanglement / emergent geometry

**Families initially sampled:** F06 causal sets, F07 holography, F09 quantum-information/emergent-geometry programmes, with RQIR Q4/Q6 as downstream operational comparators.

### Shared target

Explain which non-geometric structure is sufficient to reconstruct effective spacetime relations.

### Tension candidate

Causal-set approaches elevate causal order and local finiteness, while holographic/information approaches often extract geometry from entanglement or other quantum-information structures. The candidate intersection is not "causality + entanglement" by addition; it is whether both descend from a more primitive compositional relation.

### Atlas path

`P/S -> C/K -> L -> X -> O`

### Primary interface classes

- IF-01 ontology translation
- IF-02 state-space incompatibility
- IF-04 composition/gluing
- IF-05 causality/locality mismatch
- IF-13 observable closure

### First bridge question

> Can causal accessibility and entanglement connectivity be two quotients of one operational composition structure, with metric locality emerging only in an appropriate phase/limit?

### Kill condition

If the proposed parent structure cannot recover Lorentzian causal consistency and quantum positivity simultaneously without hand-selected graph/branch rules, reject the bridge.

Status: `TENSION_CANDIDATE / NOT_YET_SOURCE_AUDITED`

---

# Corridor C — Quantum scale symmetry / discrete universality / GR recovery

**Families initially sampled:** F03 asymptotic safety, F05 CDT, F08 tensor/GFT approaches, with F01 low-energy EFT as the IR comparator.

### Shared target

Explain why microscopically different descriptions can flow toward a small set of macroscopic gravitational couplings and observables.

### Tension candidate

A continuum functional-RG fixed-point picture and discrete statistical/gravitational ensembles may encode the same universality information in different coordinates — or they may not.

### Atlas path

`D/C -> R -> X -> E -> O`

### Primary interface classes

- IF-03 dynamics mismatch
- IF-08 continuum/coarse graining
- IF-10 GR recovery
- IF-12 UV/IR identity
- IF-13 comparator closure

### First bridge question

> Is the physically essential UV object a theory-specific microscopic ontology, or a universality class defined by composition plus quantum scale symmetry whose realizations can be discrete or continuum?

### Kill condition

If purported cross-framework fixed-point data cannot be mapped to the same physical observables/couplings with controlled scheme and parameter identity, the apparent universality is only analogy.

Status: `TENSION_CANDIDATE / NOT_YET_SOURCE_AUDITED`

---

## 4. First candidate parent object — deliberately weak form

No physical ansatz is authorized. The only admissible Phase-0 meta-hypothesis is:

`H0: the missing common structure, if it exists, should be formulated primarily as a composition/refinement law on physical relational data, with geometry and locality permitted to be derived phase-dependent structures.`

Evidence class: `CONJECTURED`.

H0 is chosen because all three corridors touch composition/refinement while differing on ontology. It is **not** yet an ISQGR model and must be actively falsified.

## 5. H0 falsification programme

H0 is weakened or rejected if any of the following occurs:

1. two independently source-grounded successful mechanisms require incompatible composition laws with no common embedding;
2. a common composition law exists only after inserting geometry/locality by hand;
3. physical positivity/normalization cannot descend through refinement;
4. causal order cannot be recovered without extra branch selection;
5. the GR/low-energy parameter map is not preserved under the same refinement chain;
6. H0 produces no stricter statement than "different theories coarse-grain".

## 6. Immediate next records

Create source-grounded realization cards for at least:

- one EPRL/spinfoam realization;
- one 4D CDT realization;
- one asymptotic-safety truncation with explicit Lorentzian/observable scope;
- one causal-set dynamics realization;
- one holographic entanglement/geometry realization;
- one GFT/tensor-model continuum realization.

Only after these records exist may the first recurrent motif `RM-001` be accepted.