# RC-003 — Asymptotic Safety / effective-average-action Einstein–Hilbert truncation

Status: `MAPPED_PARTIAL`  
Family: `F03 asymptotic safety`  
Date: 2026-09-12

## Sources

- F. Saueressig, *The Functional Renormalization Group in Quantum Gravity* (2023), https://arxiv.org/abs/2302.14152
- A. Eichhorn, *Asymptotically safe quantum gravity and its phenomenology — a review* (2026), https://arxiv.org/abs/2606.21522
- C. Laporte, A. D. Pereira, F. Saueressig, J. Wang, *Scalar-Tensor theories within Asymptotic Safety* (2021), https://arxiv.org/abs/2110.09566

Evidence class: `SOURCE_GROUNDED / TRUNCATION_SCOPED`.

## Native definition

- **Primitive ontology:** continuum quantum fields, including the metric field, treated within quantum field theory.
- **Dynamical/RG object:** the effective average action and its functional renormalization-group flow, commonly formulated through the Wetterich equation.
- **UV mechanism:** an interacting non-Gaussian/Reuter fixed point is the proposed ultraviolet completion mechanism.
- **Concrete scope of this card:** the Einstein–Hilbert truncation as the simplest nonperturbative approximation, with scalar-tensor extensions noted only as neighboring evidence.
- **State-space object:** `NOT_YET_AUDITED` at the level required by ISQGR physical-state comparison.
- **Composition/gluing:** ordinary continuum QFT composition is implicit in the effective-action framework, but the exact physical composition object comparable to RC-001/RC-002 is `NOT_YET_AUDITED`.
- **Causal/Lorentzian object:** recent work explicitly targets Lorentzian formulations; this card does not yet claim a complete same-realization Lorentzian physical observable chain.

## Scale / recovery map

- **UV -> IR:** RG trajectories from the fixed-point regime toward low-energy effective gravitational couplings are the central scale map.
- **Continuum:** fundamental description is continuum rather than a continuum limit of a lattice in this realization.
- **GR recovery:** Einstein–Hilbert operators are present in the truncation, but correct low-energy GR plus parameter identity must be checked trajectory by trajectory rather than assumed from operator content.
- **Matter/source rule:** gravity-matter systems are actively studied; the full quantum operational source rule relevant to RQIR remains `NOT_YET_AUDITED`.
- **Parameter identity:** explicit RG running exists, but comparator-grade identification of UV parameters with normalized low-energy observables is `OPEN_BLOCKED` in this card.

## Operational map

- Exact normalized RQIR Q1–Q7 observable chain: `OPEN_BLOCKED`.
- Phenomenology exists at programme level, but this card does not splice those results into the Einstein–Hilbert truncation without a same-realization map.

## Interface audit

- IF-01 ontology translation: `NOT_YET_AUDITED`
- IF-02 state space: `OPEN_BLOCKED`
- IF-03 dynamics/amplitude: `MAPPED_PARTIAL`
- IF-04 composition/gluing: `NOT_YET_AUDITED`
- IF-05 causality/locality: `NOT_YET_AUDITED`
- IF-06 gauge/relational observables: `NOT_YET_AUDITED`
- IF-07 measure/normalization/positivity: `NOT_YET_AUDITED`
- IF-08 continuum/coarse graining: `MAPPED_PARTIAL`
- IF-09 Lorentzian recovery: `OPEN_BLOCKED`
- IF-10 GR recovery/parameter identity: `OPEN_BLOCKED`
- IF-11 matter/source rule: `NOT_YET_AUDITED`
- IF-12 UV/IR identity: `MAPPED_PARTIAL`
- IF-13 observable/comparator closure: `OPEN_BLOCKED`
- IF-14 degeneracy/non-identifiability: `NOT_YET_AUDITED`
- IF-15 cross-school splice: `NOT_APPLICABLE`

## H0 test relevance

RC-003 is the strongest initial challenge to a naive discrete-composition version of H0 because its native language is continuum RG rather than microscopic discrete gluing.

For H0 to survive, ISQGR must show either:

1. the relevant FRG flow is itself a representation of a deeper composition/refinement operation on physical data; or
2. H0 must be weakened so that discrete gluing is not fundamental, only one representation of a broader scale-composition structure.

### Cheapest decisive next tests

1. Identify a precise composition/coarse-graining algebra underlying the EAA flow rather than using the word "coarse graining" analogically.
2. Compare that algebra with CDT transfer composition and EPRL refinement at the level of maps/fixed structures, not variables.
3. Test whether common fixed/stable objects survive scheme/truncation changes strongly enough to support a cross-school universality claim.

## Promotion decision

- Can contribute to recurrent motif now? **NO**.
- Reason: the correspondence between FRG scale evolution and the composition/refinement structures in RC-001/RC-002 is still only a research question.

## Claim lock

Evidence for a fixed point in a truncation or family of truncations is not promoted here to proof of a complete quantum-gravity theory, nor is truncation dependence treated as refutation.