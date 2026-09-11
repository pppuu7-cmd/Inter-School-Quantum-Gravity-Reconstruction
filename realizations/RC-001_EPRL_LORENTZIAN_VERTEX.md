# RC-001 — Lorentzian EPRL spinfoam vertex / amplitude chain

Status: `MAPPED_PARTIAL`  
Family: `F04 canonical LQG / spinfoams`  
Date: 2026-09-12

## Sources

- E. R. Livine, *Spinfoam Models for Quantum Gravity: Overview* (2024), https://arxiv.org/abs/2403.09364
- J. Engle, S. Speziale, *Spinfoams: Foundations* (2023), https://arxiv.org/abs/2310.20147
- P. Dona, M. Fanizza, G. Sarno, S. Speziale, *Numerical study of the Lorentzian EPRL spin foam amplitude* (2019), https://arxiv.org/abs/1903.12624
- J. Engle, *A proposed proper EPRL vertex amplitude* (2011), https://arxiv.org/abs/1111.2865

Evidence class: `SOURCE_GROUNDED / REALIZATION_PARTIAL`.

## Native definition

- **Primitive ontology:** quantized discrete geometric data organized on spin-network / spinfoam structures.
- **Boundary state object:** standard SU(2) spin-network data are used in the EPRL construction; the Lorentzian amplitude involves unitary infinite-dimensional SL(2,C) representation data related to SU(2) data.
- **Dynamics/amplitude:** the Lorentzian EPRL vertex amplitude is a multidimensional noncompact integral of oscillatory functions. Numerical evaluation and saddle-point asymptotics display power-law decay and oscillations related to the Regge action.
- **Constraint/gauge structure:** simplicity constraints are central to the EPRL construction. The proper-vertex literature explicitly addresses sector/orientation contamination in the semiclassical asymptotics.
- **Composition/gluing:** spinfoams are formulated as state sums / path-integral-like sums over discrete quantum geometries, but exact refinement-independence and a controlled continuum composition law are **not established by this card**.
- **Causal object:** `NOT_YET_AUDITED`.
- **Measure/normalization:** a vertex amplitude is specified, but a full normalized physical measure/channel through arbitrary refinement is `OPEN_BLOCKED` in this card.

## Scale / recovery map

- **Microscopic -> semiclassical:** EPRL asymptotics have a controlled relation to Regge-type gravitational action for suitable boundary data.
- **Continuum:** `OPEN_BLOCKED` for a same-realization theorem carrying the amplitude through arbitrary refinement/coarse graining to continuum GR.
- **Lorentzian:** Lorentzian EPRL vertex amplitudes are explicitly defined and numerically studied.
- **GR recovery:** `PARTIAL`; local/semiclassical Regge behavior is evidence, not a full continuum Einstein limit.
- **Matter/source rule:** `NOT_YET_AUDITED`.
- **Parameter identity across scales:** `OPEN_BLOCKED`.

## Operational map

- Exact RQIR Q1–Q7 observable mapping: `NOT_YET_AUDITED`.
- Normalized same-realization comparator observable: `OPEN_BLOCKED`.

## Interface audit

- IF-01 ontology translation: `NOT_YET_AUDITED`
- IF-02 state space: `MAPPED_PARTIAL`
- IF-03 dynamics/amplitude: `MAPPED_PARTIAL`
- IF-04 composition/gluing: `OPEN_BLOCKED`
- IF-05 causality/locality: `NOT_YET_AUDITED`
- IF-06 gauge/relational observables: `MAPPED_PARTIAL`
- IF-07 measure/normalization/positivity: `OPEN_BLOCKED`
- IF-08 continuum/coarse graining: `OPEN_BLOCKED`
- IF-09 Lorentzian recovery: `MAPPED_PARTIAL`
- IF-10 GR recovery/parameter identity: `OPEN_BLOCKED`
- IF-11 matter/source rule: `NOT_YET_AUDITED`
- IF-12 UV/IR identity: `OPEN_BLOCKED`
- IF-13 observable/comparator closure: `OPEN_BLOCKED`
- IF-14 degeneracy/non-identifiability: `NOT_YET_AUDITED`
- IF-15 cross-school splice: `NOT_APPLICABLE`

## H0 test relevance

H0 proposes that a sufficiently fundamental composition/refinement law may be more primary than continuum geometry.

EPRL is useful because it already provides nontrivial microscopic amplitude/composition ingredients, while the controlled all-scale refinement -> continuum -> normalized-observable chain is exactly where the hypothesis must become more specific.

### Cheapest decisive next tests

1. Identify the strongest source-grounded EPRL refinement/coarse-graining map that preserves the physical constraint content.
2. Determine whether its composition data can be expressed without assuming the target continuum metric.
3. Check whether normalization/positivity can be transported under that refinement rather than imposed at the final observable stage.

## Promotion decision

- Can contribute to recurrent motif now? **NO**.
- Reason: the key composition/refinement and normalized continuum chain is still `OPEN_BLOCKED` in this record.

## Claim lock

This card does not state that EPRL or LQG fails. It isolates the current evidence boundary relevant to ISQGR.