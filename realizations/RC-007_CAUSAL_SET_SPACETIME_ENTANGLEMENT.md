# RC-007 — Causal-set spacetime entanglement / Sorkin–Johnston spectral construction

Status: `MAPPED_PARTIAL / SAME_REALIZATION_BRIDGE_LAB`  
Family: `F06 causal set theory` with direct relevance to quantum-information observables  
Date: 2026-09-12

## Sources

- R. D. Sorkin, Y. K. Yazdi, *Entanglement Entropy in Causal Set Theory* (2016), arXiv:1611.10281.
- S. Surya, N. X, Y. K. Yazdi, *Entanglement Entropy of Causal Set de Sitter Horizons* (2020), arXiv:2008.07697.
- A. Mathur, S. Surya, N. X, *Spacetime Entanglement Entropy: Covariance and Discreteness* (2022), arXiv:2207.01080.
- C. F. Duffy, J. Y. L. Jones, Y. K. Yazdi, *Entanglement Entropy of Disjoint Spacetime Intervals in Causal Set Theory* (2021), arXiv:2110.07627.

Evidence class: `SOURCE_GROUNDED / FIELD_ON_MANIFOLDLIKE_CAUSAL_SET`.

## Why this card matters for ISQGR

Earlier Corridor B treated causal structure and holographic entanglement as two different school-native channels with a difficult same-regime overlap problem.

RC-007 supplies a cleaner intermediate laboratory: causal order/discreteness and a covariant entanglement observable coexist in one causal-set/QFT construction.

This does not solve quantum gravity, but it lets ISQGR test causal × quantum-information compatibility without cross-realization splicing at the first step.

## Native construction

- **Geometry substrate:** manifold-like causal set / locally finite causal order.
- **Quantum field:** Gaussian/free scalar-field constructions using causal-set propagator/correlation data.
- **Entanglement observable:** Sorkin spacetime entanglement entropy (SSEE), formulated from the Wightman function and Pauli–Jordan operator on spacetime regions rather than canonical hypersurface data.
- **Covariance motivation:** the construction is spacetime/covariant in character and adapted to causal-set structure.

## Source-grounded scaling tension

The cited causal-set calculations exhibit a nontrivial UV issue:

- causal-set discreteness supplies a natural covariant spacetime cutoff;
- nevertheless, untruncated causal-set SSEE in studied manifold-like examples can show a **volume law** rather than the expected continuum/horizon area law;
- an additional spectral UV truncation of the Pauli–Jordan/correlation spectrum recovers area-law behavior in the studied examples;
- the 2022 review explicitly notes that this extra cutoff is applied in the spectral scaling regime mimicking continuum behavior and discusses the possibility that the volume law reflects fundamental causal-set nonlocality / UV physics.

This is not a family-level failure. It is a source-defined interface tension between discreteness, nonlocal correlation spectrum and continuum entanglement scaling.

## Interface audit

- IF-01 ontology translation: `MAPPED_PARTIAL`
- IF-02 state space: `MAPPED_PARTIAL` for Gaussian field sector
- IF-04 composition/gluing: `NOT_YET_AUDITED`
- IF-05 causality/locality: `MAPPED_PARTIAL`
- IF-07 normalization/positivity: `MAPPED_PARTIAL / FIELD_SECTOR`
- IF-08 continuum/coarse graining: `TENSION_CANDIDATE`
- IF-09 Lorentzian recovery: `MAPPED_PARTIAL`
- IF-10 GR recovery: `NOT_APPLICABLE_TO_THIS_FIELD_OBSERVABLE_CARD`
- IF-13 observable closure: `MAPPED_PARTIAL`
- IF-14 degeneracy/non-identifiability: `NOT_YET_AUDITED`

## New same-realization question

The key ISQGR question becomes:

> Is the spectral cutoff needed for area-law SSEE an independently derivable physical coarse-graining scale fixed by causal-set density/dynamics, or an external continuum-matching prescription?

If it is derivable, causal structure/discreteness and quantum-information scaling may be linked by a native bridge principle.

If it must be selected by demanding the target area law, it cannot serve as evidence for that bridge without circularity control.

## Relation to BH-002

RC-007 does **not** implement RT/HRT CEMR. Instead it supplies a same-realization test of whether causal discreteness contains enough information to regulate/organize entanglement geometry without importing a holographic dictionary.

It therefore attacks BH-002's `DOMAIN_OVERLAP` blocker from a different direction.

## Promotion decision

- Same-realization causal × entanglement laboratory: **YES**.
- New physics: **NO**.
- Recurrent motif contribution: `TENSION_CANDIDATE` only.

## Claim lock

Volume-law SSEE without the additional spectral truncation may reflect nonlocal UV structure, regulator structure, or limitations of the studied setup. It is not treated here as a refutation of causal set theory.