# RC-004 — Causal Set / Benincasa–Dowker(-Glaser) action chain

Status: `MAPPED_PARTIAL`  
Family: `F06 causal set theory`  
Date: 2026-09-12

## Sources

- S. Surya, *The causal set approach to quantum gravity* (2019), https://arxiv.org/abs/1903.11544
- Living Reviews version, https://doi.org/10.1007/s41114-019-0023-1
- L. Machet, J. Wang, *On the continuum limit of Benincasa-Dowker-Glaser causal set action* (2020), https://arxiv.org/abs/2007.13192
- D. Rideout, *Dynamics of Causal Sets* (2002), https://arxiv.org/abs/gr-qc/0212064

Evidence class: `SOURCE_GROUNDED / REALIZATION_PARTIAL`.

## Native definition

- **Primitive ontology:** a locally finite partially ordered set `C`.
- **Causal object:** the partial order is fundamental proto-causality; local finiteness encodes spacetime discreteness.
- **Locality status:** continuum Lorentz invariance can coexist with a characteristic fundamental nonlocality; nearest-neighbour intuition is not simply lattice-local.
- **State/history object:** finite or locally finite causal sets as candidate spacetime histories.
- **Dynamics/action object:** the Benincasa–Dowker(-Glaser) construction gives a combinatorial causal-set analogue of the Einstein–Hilbert action.

For the dimensionless 4D causal-set action, the Living Reviews derivation gives a form

`S^(4)(C) = (4/sqrt(6)) [ n - N0 + 9 N1 - 16 N2 + 8 N3 ]`,

where the `Nk` count specified order intervals.

- **Quantum dynamics:** a sum-over-histories / quantum-measure dynamics is a natural programme, but a unique complete physical quantum dynamics is **not established by this card**.
- **Sequential growth:** classical stochastic growth models provide a concrete compositional/growth laboratory, but may not be promoted as the final quantum dynamics.

## Scale / recovery map

- **Discrete -> continuum:** for causal sets obtained by appropriate sprinkling into continuum spacetimes, the expectation/continuum limit of the BD/BDG action recovers Einstein–Hilbert bulk behavior under stated conditions, with boundary subtleties.
- **Lorentzian recovery:** Lorentzian causal order is fundamental rather than reconstructed from a Euclidean regulator.
- **GR recovery:** `MAPPED_PARTIAL`; action-level continuum recovery is significant but does not by itself supply the full quantum physical-state/observable chain.
- **Matter/source rule:** `NOT_YET_AUDITED`.
- **Parameter identity:** `OPEN_BLOCKED` for a full quantum UV-to-IR realization.

## Operational map

- Exact normalized RQIR Q1–Q7 mapping: `NOT_YET_AUDITED`.
- Full physical inner product/quantum measure and comparator observable: `OPEN_BLOCKED`.

## Interface audit

- IF-01 ontology translation: `MAPPED_PARTIAL`
- IF-02 state space: `OPEN_BLOCKED`
- IF-03 dynamics/amplitude: `OPEN_BLOCKED`
- IF-04 composition/gluing: `MAPPED_PARTIAL` at growth/history level, not yet final quantum dynamics
- IF-05 causality/locality: `MAPPED_PARTIAL`
- IF-06 gauge/relational observables: `NOT_YET_AUDITED`
- IF-07 measure/normalization/positivity: `OPEN_BLOCKED`
- IF-08 continuum/coarse graining: `MAPPED_PARTIAL`
- IF-09 Lorentzian recovery: `MAPPED_PARTIAL`
- IF-10 GR recovery/parameter identity: `MAPPED_PARTIAL`
- IF-11 matter/source rule: `NOT_YET_AUDITED`
- IF-12 UV/IR identity: `OPEN_BLOCKED`
- IF-13 observable/comparator closure: `OPEN_BLOCKED`
- IF-14 degeneracy/non-identifiability: `NOT_YET_AUDITED`
- IF-15 cross-school splice: `NOT_APPLICABLE`

## BH-001 test relevance

Causal sets provide a sharp case where **sequential/causal order is itself primitive**. This makes RC-004 useful for checking whether BH-001's single generic composition law is semantically too coarse.

A map that treats causal succession as interchangeable with ordinary tensor-product/subsystem composition would erase the defining structure of this realization and is therefore not an acceptable bridge.

### Cheapest decisive next tests

1. Separate causal/sequential composition from parallel/subsystem composition in the BH-001 formalism.
2. Determine whether causal-set growth/path composition obeys a scale-compatible law under coarse graining without destroying order information.
3. Determine whether a quantum measure/physical positivity structure can coexist with that coarse graining.

## Promotion decision

- Can contribute to recurrent motif now? **NO**.
- It does, however, force a semantic refinement of BH-001: not all composition operations may be collapsed into one `star`.

## Claim lock

The absence of a complete quantum dynamics in this card is `OPEN_BLOCKED`, not evidence that causal set theory is false.