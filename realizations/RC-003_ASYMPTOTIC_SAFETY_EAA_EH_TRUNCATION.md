# RC-003 — Asymptotic Safety / effective-average-action Einstein–Hilbert truncation

Status: `SCALE_OPERATION_AUTHORITY_PASS_SCOPED / MAPPED_PARTIAL`  
Family: `F03 asymptotic safety`  
Date: 2026-09-14

## Sources

- F. Saueressig, *The Functional Renormalization Group in Quantum Gravity* (2023), https://arxiv.org/abs/2302.14152
- A. Eichhorn, *Asymptotically safe quantum gravity and its phenomenology — a review* (2026), https://arxiv.org/abs/2606.21522
- C. Laporte, A. D. Pereira, F. Saueressig, J. Wang, *Scalar-Tensor theories within Asymptotic Safety* (2021), https://arxiv.org/abs/2110.09566

Evidence class: `SOURCE_GROUNDED / TRUNCATION_SCOPED`.

## Native definition

- **Primitive ontology:** continuum quantum fields, including the metric field, treated within quantum field theory.
- **Dynamical/RG object:** the effective average action and its functional renormalization-group flow through the Wetterich equation.
- **UV mechanism:** an interacting non-Gaussian/Reuter fixed point is the proposed ultraviolet completion mechanism.
- **Concrete scope of this card:** Einstein–Hilbert truncation as the simplest nonperturbative approximation, with scalar-tensor extensions as neighboring evidence.
- **State-space object:** `OPEN_BLOCKED` at the level required for physical-state comparison. ITER069 establishes a theory-space effective-action flow, not a physical spacetime-state Hilbert-space transport.
- **Composition/gluing:** `C_scale_flow` is now source-qualified as regulator-dependent continuum coarse graining / theory-space EAA flow. A finite source-defined physical composition/semigroup law comparable to CDT gluing is `NOT_ESTABLISHED_IN_FROZEN_STACK`.
- **Causal/Lorentzian object:** recent work targets Lorentzian formulations, but this card does not claim a complete same-realization Lorentzian physical observable chain.

## ITER069 authority update

ITER069 prospectively preregistered and manually audited the FRG scale/composition object after exact-PDF extraction from the frozen source stack.

Terminal result:

**`PASS_SCOPED / FRG_SCALE_OPERATION_QUALIFIED`**

Mandatory qualifier:

**`FINITE_SOURCE_DEFINED_COMPOSITION_LAW = NOT_ESTABLISHED_IN_FROZEN_STACK`**

Source-qualified predicates:

- exact EAA/Wetterich flow object: **PASS**;
- domain/codomain as effective actions/functionals/couplings in theory space: **PASS**;
- regulator insertion/dependence: **PASS**;
- gravitational background/gauge/ghost structure: **PASS**;
- exact finite `k1 -> k2` source-defined composition law: **SCOPED ABSENCE**;
- separation of RG fixed points/trajectories from physical refinement maps: **PASS**;
- cross-school identification by analogy: **FORBIDDEN / NEGATIVE LOCK**.

Durable records:

- preregistration: `prereg/ITER069_RC003_FRG_SCALE_COMPOSITION_AUTHORITY_2026-09-14.md`;
- source authority: `sources/ITER069_RC003_FRG_SCALE_OPERATION_AUTHORITY_2026-09-14.md`;
- adversarial critic: `results/ITER069_ADVERSARIAL_CRITIC_2026-09-14.md`;
- terminal result: `results/ITER069_RC003_FRG_SCALE_COMPOSITION_AUTHORITY_2026-09-14.md`.

## Scale / recovery map

- **UV -> IR:** RG trajectories from the fixed-point regime toward low-energy effective gravitational couplings are the central scale map.
- **Continuum:** the realization is continuum from the outset rather than a lattice continuum-limit construction.
- **GR recovery:** Einstein–Hilbert operators are present in the truncation, but correct low-energy GR plus parameter identity must be checked trajectory by trajectory rather than assumed from operator content.
- **Matter/source rule:** gravity-matter systems are actively studied; the full quantum operational source rule relevant to RQIR remains `NOT_YET_AUDITED`.
- **Parameter identity:** explicit RG running exists, but comparator-grade identification of UV parameters with normalized low-energy observables remains `OPEN_BLOCKED`.

## Operational map

- Exact normalized RQIR Q1–Q7 observable chain: `OPEN_BLOCKED`.
- Phenomenology exists at programme level, but this card does not splice those results into the Einstein–Hilbert truncation without a same-realization map.

## Interface audit

- IF-01 ontology translation: `NOT_YET_AUDITED`
- IF-02 state space: `OPEN_BLOCKED`
- IF-03 dynamics/amplitude: `MAPPED_PARTIAL`
- IF-04 composition/gluing: `MAPPED_SCOPED_DISTINCT_TYPE_C_SCALE_FLOW`
- IF-05 causality/locality: `NOT_YET_AUDITED`
- IF-06 gauge/relational observables: `MAPPED_PARTIAL_BACKGROUND_GAUGE_STRUCTURE`
- IF-07 measure/normalization/positivity: `MAPPED_PARTIAL_REGULATOR_STRUCTURE`
- IF-08 continuum/coarse graining: `SOURCE_QUALIFIED_SCOPED`
- IF-09 Lorentzian recovery: `OPEN_BLOCKED`
- IF-10 GR recovery/parameter identity: `OPEN_BLOCKED`
- IF-11 matter/source rule: `NOT_YET_AUDITED`
- IF-12 UV/IR identity: `MAPPED_PARTIAL`
- IF-13 observable/comparator closure: `OPEN_BLOCKED`
- IF-14 degeneracy/non-identifiability: `NOT_YET_AUDITED`
- IF-15 cross-school splice: `NEGATIVE_LOCK_NO_TYPED_EQUIVALENCE`

## H0 test relevance

ITER069 falsifies the naive form of H0 in which `composition/refinement` is one undifferentiated operation across schools.

The current source-qualified atlas contains at least three distinct operation types:

1. `C_seq` — CDT sequential temporal/state-sum composition;
2. `C_tensor` — HaPPY subsystem/tensor contraction and isometric encoding;
3. `C_scale_flow` — FRG regulator-dependent EAA/theory-space flow.

A surviving H0 must therefore be typed and multi-operation. Any common parent must derive explicit embeddings preserving domain/codomain, regulator or measure, gauge/quotient structure, dynamics, causal/time semantics and observables.

### Cheapest decisive next test

Prospectively compare `C_scale_flow` with the strongest source-qualified dynamical comparator, CDT `C_seq`, while freezing controls against `RG time = proper time`, regulator erasure, full/reduced-state substitution and fixed-point/refinement substitution.

Recommended gate: `PREREGISTER_ITER070_FRG_CDT_SCALE_TIME_TYPE_DISCRIMINATION`.

## Promotion decision

- Can contribute to recurrent motif now? **YES, only as a distinct typed operation `C_scale_flow`.**
- Can contribute bridge credit now? **NO**.
- Can be identified with CDT/HaPPY/EPRL/causal-set composition or refinement? **NO, not from the frozen authority stack.**

## Claim lock

Evidence for a fixed point in a truncation or family of truncations is not promoted to proof of a complete quantum-gravity theory. RG scale is not promoted to physical proper time. Truncation/regulator/background dependence may not be erased to manufacture a cross-school equivalence. `BRIDGE_CREDIT = 0`.