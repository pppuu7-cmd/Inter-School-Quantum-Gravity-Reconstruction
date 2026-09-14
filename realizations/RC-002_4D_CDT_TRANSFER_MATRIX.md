# RC-002 — 4D CDT transfer matrix and effective volume dynamics

Status: `COMPOSITION_MEASURE_AUTHORITY_PASS_SCOPED / CONTINUUM_OPEN`  
Family: `F05 CDT`  
Date: 2026-09-14

## Sources

Primary authority now pinned by ITER067:

- J. Ambjørn, J. Jurkiewicz, R. Loll, *Dynamically Triangulating Lorentzian Quantum Gravity* (2001), arXiv:hep-th/0105267v1, Nucl. Phys. B610 347–382, DOI 10.1016/S0550-3213(01)00297-8.
- J. Ambjørn, J. Gizbert-Studnicki, A. T. Görlich, J. Jurkiewicz, *The transfer matrix in four-dimensional CDT* (2012), arXiv:1205.3791v1, JHEP 1209 (2012) 017, DOI 10.1007/JHEP09(2012)017.
- J. Ambjørn, J. Gizbert-Studnicki, A. T. Görlich, J. Jurkiewicz, R. Loll, *The transfer matrix method in four-dimensional causal dynamical triangulations* (2013), arXiv:1302.2210v1, DOI 10.1063/1.4791727.

Navigation/context sources retained:

- R. Loll, *Quantum Gravity from Causal Dynamical Triangulations: A Review* (2019), arXiv:1905.08669.
- recent CDT review context: arXiv:2401.09399.

Evidence class: `SOURCE_GROUNDED / FULL_REGULATED_COMPOSITION_AUTHORITY_SCOPED`.

## Native definition

- **Primitive ontology:** Lorentzian simplicial manifolds with a preferred discrete proper-time slicing and fixed spatial topology.
- **Boundary/state object:** unlabelled spatial triangulations `g` at integer proper times. Distinct spatial triangulations are physical basis states of the regulated Hilbert space.
- **State normalization / gauge quotient:** Eq. (44) of hep-th/0105267v1 fixes `<g1|g2>=delta(g1,g2)/C(g1)` and `sum_g C(g)|g><g|=1`, where `C(g)` is the automorphism-group order.
- **Dynamics/amplitude:** Eq. (45) defines the one-step full transfer matrix between complete spatial triangulations as a sum over all distinct interpolating sandwich triangulations, weighted by `exp(i Delta S)/C(T)`.
- **Composition/gluing:** Eq. (47) gives an exact semigroup law over intermediate spatial triangulations with the required intermediate factor `C(g)`.
- **Measure:** the regulated state sum uses `m(T)=1/C(T)`. This is source-defined combinatorial/path-integral measure authority at the regulated level, not a continuum physical-measure theorem.
- **Causal/time structure:** the preferred discrete proper time is part of the invariant geometric data in the source construction and is essential to the one-step sandwich/transfer-matrix formulation.
- **Wick relation:** the Lorentzian transfer amplitude is source-defined; positivity/Hamiltonian analysis is performed on the source-related Wick-rotated Euclidean transfer object.

## Positivity / Hamiltonian firewall

ITER067 corrected an important possible overclaim.

In `d>2`, source authority establishes the required positivity package for **`T_N^2`**, not generally for elementary one-step `T_N`:

- site-reflection positivity is proven;
- elementary link-reflection positivity in `d=3,4` is not established;
- the authors explicitly allow that elementary `T_N` may fail to be positive;
- the regulated Hamiltonian is constructed from `T_N^2`, with possible zero modes quotiented.

Therefore:

`ELEMENTARY_T_POSITIVITY_D4 = NOT_ESTABLISHED`.

No later bridge argument may silently strengthen this.

## Full vs effective transfer matrix

The full matrix acts on complete spatial triangulations. The 2012/2013 volume-labelled transfer matrix is an **effective reduced object** built from averages/probability information over the much larger full state space.

The 2012 primary source explicitly treats its use as an approximation whose adequacy is checked numerically and warns against interpreting a volume label as a single full Hilbert-space state.

Therefore:

`T_effective_volume != T_full`

as a source-authorized operator identity.

The effective volume matrix remains useful for semiclassical/effective dynamics but cannot substitute for the full composition object in inter-school bridge tests.

## Scale / recovery map

- **Regulated temporal composition:** `MAPPED / SOURCE_QUALIFIED`.
- **Microscopic -> effective volume dynamics:** `MAPPED_PARTIAL`; reduced effective matrix is empirically supported in the studied phase/observables.
- **Continuum limit:** `OPEN_BLOCKED` for a complete source-qualified chain from the regulated transfer operator and measure to a continuum physical Hilbert space/operator.
- **Lorentzian recovery:** source-defined Wick relation exists, but Euclidean positivity results must not be promoted to an unqualified Lorentzian-unitarity theorem.
- **GR recovery:** `PARTIAL`; semiclassical/de Sitter evidence is not a full Einstein-limit theorem.
- **Matter/source rule:** `NOT_YET_AUDITED`.

## Interface audit after ITER067

- IF-01 ontology translation: `MAPPED_PARTIAL`
- IF-02 state space: `MAPPED / REGULATED`
- IF-03 dynamics/amplitude: `MAPPED / REGULATED`
- IF-04 composition/gluing: **`MAPPED / SOURCE_QUALIFIED_REGULATED`**
- IF-05 causality/locality: `MAPPED_PARTIAL / PREFERRED_TIME_ESSENTIAL`
- IF-06 gauge/relational observables: `MAPPED_PARTIAL`
- IF-07 measure/normalization/positivity: **`MAPPED_PARTIAL / REGULATED_MEASURE_AND_T2_POSITIVITY_QUALIFIED`**
- IF-08 continuum/coarse graining: `OPEN_BLOCKED`
- IF-09 Lorentzian recovery: `MAPPED_PARTIAL`
- IF-10 GR recovery/parameter identity: `OPEN_BLOCKED`
- IF-11 matter/source rule: `NOT_YET_AUDITED`
- IF-12 UV/IR identity: `OPEN_BLOCKED`
- IF-13 observable/comparator closure: `MAPPED_PARTIAL`
- IF-14 degeneracy/non-identifiability: `NOT_YET_AUDITED`
- IF-15 cross-school splice: `AUTHORIZED_ONLY_AS_SEPARATE_PREREGISTERED_COMPOSITION_AUDIT`

## ITER067 terminal record

Preregistration: `prereg/ITER067_RC002_FULL_CDT_TRANSFER_MATRIX_COMPOSITION_MEASURE_AUTHORITY_2026-09-14.md`.

Source audit: `sources/ITER067_RC002_FULL_CDT_TRANSFER_MATRIX_AUTHORITY_2026-09-14.md`.

Adversarial critic: `results/ITER067_ADVERSARIAL_CRITIC_2026-09-14.md`.

Terminal result: `results/ITER067_RC002_FULL_CDT_TRANSFER_MATRIX_COMPOSITION_MEASURE_AUTHORITY_2026-09-14.md`.

Terminal classification: **`PASS_SCOPED / STRUCTURAL_MAP_ESTABLISHED_SCOPED`**.

## H0 test relevance

The source-qualified object is not just a bare semigroup. Its package is:

`state quotient/normalization + automorphism-weighted measure + time-sliced amplitude + exact intermediate-state composition + qualified T^2 positivity`.

This makes RC002 a stronger H0 stress test than comparing abstract words like “composition” or reduced volume dynamics. Any common-parent candidate must account for the package or explicitly derive a controlled quotient in which some elements become inessential.

The preferred-time dependence is especially discriminating: erasing it by analogy is forbidden.

## Next cheapest decisive test

Use a separately preregistered cross-school composition-arrow audit against another **source-qualified** composition mechanism. The test must preserve both sides' exact state spaces, measures, quotient structures, dynamics and causal/time semantics before asking whether a common map exists.

A particularly informative route is to contrast CDT's sequential proper-time semigroup with an exact tensor-network/subsystem composition mechanism, because this can falsify the weak hypothesis that all objects called `composition` instantiate the same physical operation.

## Promotion decision

- Can contribute to recurrent composition motif now? **YES, as a source-qualified regulated CDT component.**
- Can establish a cross-school bridge now? **NO.**
- Bridge credit: **0**.

## Claim lock

ITER067 does not establish a continuum CDT theory, foliation independence, elementary-transfer positivity in 4D, EPRL equivalence, a common-parent principle, a bridge, new physics or a candidate QG theory.
