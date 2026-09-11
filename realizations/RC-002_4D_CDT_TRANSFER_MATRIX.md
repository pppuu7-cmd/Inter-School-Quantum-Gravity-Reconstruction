# RC-002 — 4D Causal Dynamical Triangulations / transfer-matrix chain

Status: `MAPPED_PARTIAL`  
Family: `F05 causal dynamical triangulations`  
Date: 2026-09-12

## Sources

- J. Ambjørn, R. Loll, *Causal Dynamical Triangulations: Gateway to Nonperturbative Quantum Gravity* (2024), https://arxiv.org/abs/2401.09399
- R. Loll, *Quantum Gravity from Causal Dynamical Triangulations: A Review* (2019), https://arxiv.org/abs/1905.08669
- J. Ambjørn et al., *The transfer matrix in four-dimensional CDT* (2012), https://arxiv.org/abs/1205.3791
- J. Ambjørn et al., *The transfer matrix method in four-dimensional causal dynamical triangulations* (2013), https://arxiv.org/abs/1302.2210

Evidence class: `SOURCE_GROUNDED / REALIZATION_PARTIAL`.

## Native definition

- **Primitive ontology:** Lorentzian simplicial spacetime histories built from dynamical triangulations with a discrete proper-time structure.
- **State object:** spatial triangulated geometries on discrete-time slices.
- **Dynamics/amplitude:** a nonperturbative gravitational path integral over allowed triangulated spacetime configurations; a transfer matrix relates spatial geometries at adjacent lattice times and, in the cited 4D formulation, uniquely determines the theory.
- **Causal object:** the construction imposes a Lorentzian/causal triangulation structure and discrete proper time before Wick rotation used for simulations.
- **Composition:** transfer-matrix multiplication supplies an explicit adjacent-time composition law at the regulated level.
- **Measure/normalization:** a regulated statistical/path-integral ensemble is defined; full continuum physical normalization/positivity is `NOT_YET_AUDITED` in this card.

## Scale / recovery map

- **Microscopic -> macroscopic:** numerical simulations exhibit a phase with a de Sitter-like semiclassical geometry and an effective transfer matrix for the spatial volume.
- **Continuum:** second/higher-order transition structure is investigated as a possible route to a continuum limit; a complete continuum theorem is not asserted here.
- **Lorentzian:** Lorentzian causal structure is part of the regulated construction, although simulations use a configuration-wise Wick rotation.
- **GR recovery:** `PARTIAL`; the de Sitter-like semiclassical phase and effective minisuperspace behavior are positive recovery evidence, not a proof of full GR in all observables.
- **Matter/source rule:** `NOT_YET_AUDITED`.
- **Parameter identity across scales:** `OPEN_BLOCKED` for the full UV-to-IR physical map.

## Operational map

- Diffeomorphism-invariant observables are studied numerically in CDT.
- Exact frozen-RQIR Q1–Q7 mapping: `NOT_YET_AUDITED`.
- Same-realization normalized comparator observable suitable for KMQGB: `OPEN_BLOCKED` in this card.

## Interface audit

- IF-01 ontology translation: `NOT_YET_AUDITED`
- IF-02 state space: `MAPPED_PARTIAL`
- IF-03 dynamics/amplitude: `MAPPED_PARTIAL`
- IF-04 composition/gluing: `MAPPED_PARTIAL`
- IF-05 causality/locality: `MAPPED_PARTIAL`
- IF-06 gauge/relational observables: `NOT_YET_AUDITED`
- IF-07 measure/normalization/positivity: `NOT_YET_AUDITED`
- IF-08 continuum/coarse graining: `OPEN_BLOCKED`
- IF-09 Lorentzian recovery: `MAPPED_PARTIAL`
- IF-10 GR recovery/parameter identity: `OPEN_BLOCKED`
- IF-11 matter/source rule: `NOT_YET_AUDITED`
- IF-12 UV/IR identity: `OPEN_BLOCKED`
- IF-13 observable/comparator closure: `OPEN_BLOCKED`
- IF-14 degeneracy/non-identifiability: `NOT_YET_AUDITED`
- IF-15 cross-school splice: `NOT_APPLICABLE`

## H0 test relevance

CDT is a strong stress test for H0 because it possesses a concrete regulated composition object — the transfer matrix — while continuum geometry is intended to emerge from the ensemble rather than being inserted as a fixed background metric.

### Cheapest decisive next tests

1. Extract the exact algebraic properties required of the full CDT transfer matrix before volume reduction.
2. Separate properties that depend on the preferred foliation/discrete proper time from representation-independent composition properties.
3. Test whether the composition law and phase/continuum structure can be expressed in the same abstract language as an EPRL/spinfoam gluing map without erasing essential causal information.

## Promotion decision

- Can contribute to recurrent motif now? **NO**.
- Reason: comparison with another independently audited composition law has not yet been performed.

## Claim lock

This card does not state that CDT fails or that its foliation is unphysical. It records the precise structures needed for an inter-school comparison.