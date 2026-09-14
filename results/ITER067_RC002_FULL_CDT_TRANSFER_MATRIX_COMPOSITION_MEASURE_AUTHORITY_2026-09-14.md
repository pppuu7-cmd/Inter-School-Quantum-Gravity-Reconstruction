# ITER067 terminal result — RC002 full CDT transfer-matrix composition/measure authority

Date: 2026-09-14
Gate: `ITER067_RC002_FULL_CDT_TRANSFER_MATRIX_COMPOSITION_MEASURE_AUTHORITY`
Preregistration commit: `c103cb2e5b39d7dcf8fe747210dd9d7e3d0a58b9`

## Terminal classification

**`PASS_SCOPED / STRUCTURAL_MAP_ESTABLISHED_SCOPED`**

This is a source-authority PASS for a **regulated CDT composition component** only. It is not an inter-school bridge and carries zero bridge credit.

## Established source-defined object

For regulated CDT spatial triangulation states `|g>` with a spatial-volume cutoff, the frozen primary stack defines:

1. an automorphism-weighted scalar product and resolution of identity;
2. a one-step full transfer matrix between complete spatial triangulations;
3. matrix elements given by a sum over all distinct interpolating sandwich triangulations with source weight `exp(i Delta S)/C(T)`;
4. arbitrary-time propagation by powers of the transfer matrix;
5. an exact semigroup/gluing law over intermediate spatial triangulations with the required factor `C(g)`;
6. a source-defined Wick rotation to the Euclidean transfer object used for positivity/Hamiltonian analysis.

In the 2001 source, Eqs. (43)–(47) provide the core object:

- state sum with `m(T)=1/C(T)`;
- state inner product / identity with `C(g)`;
- full one-step matrix element;
- iterated propagator;
- exact semigroup composition.

## Positivity theorem — exact ceiling

In `d>2`, the source does **not** establish general positivity of the elementary one-step `T_N`.

The source explicitly corrects the stronger earlier claim and establishes the required symmetry/positivity/boundedness package for the **two-step object `T_N^2`**. Site-reflection positivity suffices for `T_N^2`; link-reflection positivity of elementary `T_N` is not established in `d=3,4`, and the paper explicitly allows that `T_N` itself may fail to be positive. The source Hamiltonian is correspondingly constructed from

`h'_N = -(1/(2a)) log(T_N^2)`

with a quotient by possible zero-eigenvectors if necessary.

Terminal lock:

`ELEMENTARY_T_POSITIVITY_D4 = NOT_ESTABLISHED`.

## Full vs effective matrix

The 2012 and 2013 four-dimensional sources independently prevent a major false correspondence.

The **full** transfer matrix acts on complete spatial triangulation states. The measured/effective transfer matrix labelled only by spatial three-volume / scale factor is a reduced object obtained from averages/probability information over the much larger full state space. The 2012 paper explicitly treats use of that volume-labelled matrix as an effective approximation and tests its adequacy numerically.

Therefore:

`T_effective_volume != T_full` as a source-authorized operator identity.

Any later bridge audit must compare the full Eq. (45)/(47) composition object unless it separately preregisters a reduced comparator.

## Preferred time and Wick dependence

The composition law is not representation-independent in the form established here.

CDT histories possess a distinguished discrete proper-time slicing. The transfer matrix is defined for one-step `Delta t=1` sandwiches; its semigroup law sums over an intermediate time slice; site/link reflections are defined relative to integer/half-integer time hypersurfaces. The source explicitly says the discrete proper-time structure is part of the invariant geometric data rather than a coordinate gauge choice.

The Lorentzian transfer amplitude and Euclidean positivity analysis are related by the source-defined Wick rotation but must not be conflated.

## Frozen controls

All six preregistered controls detect the intended scope violation:

- full/effective conflation: detected;
- automorphism/measure drop: detected;
- erased time slicing: detected;
- `T` vs `T^2` positivity strengthening: detected;
- Lorentzian/Euclidean Wick conflation: detected;
- reduced-volume observable promoted to full operator equality: detected.

## Researcher result

`STRUCTURAL_MAP_ESTABLISHED_SCOPED`.

The local structural arrow is

`g_t -> T_full -> g_(t+1)`

with exact automorphism-weighted gluing under intermediate-state summation.

## Adversarial critic result

Durable critic: `results/ITER067_ADVERSARIAL_CRITIC_2026-09-14.md`.

The critic attempted to invalidate the PASS through preferred-foliation dependence, weak positivity, regulated-vs-continuum measure, finite-volume cutoff, full/effective reduction, Wick rotation and automorphism-normalization ambiguity. None destroys the preregistered **regulated local** composition object. They instead rule out stronger promotions.

A countermodel is immediate: generic preferred-time transfer-matrix systems can satisfy semigroup composition without possessing a gravitational continuum limit or a common-parent relation. Thus the semigroup law alone cannot derive H0.

## New structural fact

ITER067 establishes a nontrivial coupled package rather than a bare algebraic semigroup:

`state quotient/normalization + automorphism-weighted measure + time-sliced amplitude + exact composition + qualified T^2 positivity`.

This package is the correct CDT interface object for future bridge work. Omitting the `C(g)`/`C(T)` weights or the preferred-time semantics changes the source object.

## What ITER067 rules out

Within the frozen primary stack it rules out the following shortcuts:

- treating the volume-labelled effective matrix as the full CDT operator;
- claiming elementary `T` positivity in four dimensions;
- dropping automorphism factors as cosmetic normalization;
- calling the regulated semigroup law foliation-independent;
- using Euclideanized positivity as if it were an unqualified Lorentzian-unitarity theorem;
- promoting a local composition law directly to a common-parent principle.

## Downstream authorization

The only newly authorized scientific successor is a separately preregistered **cross-school composition-arrow audit** that compares the exact CDT full-state composition package to another already source-qualified composition law and keeps explicit:

- domain/codomain state spaces;
- measure/normalization;
- gauge/automorphism quotient;
- causal/preferred-time structure;
- dynamics/amplitude;
- exact composition map;
- positivity/physical interpretation.

No cross-school equality or refinement map is implied in advance.

## Claim ceiling

`CANDIDATE_THEORY = UNFORMED`

`THEORY_ESTABLISHED = 0%`

`BRIDGE_CREDIT = 0`

Not established: continuum theorem, full GR recovery, foliation independence, representation-independent composition, EPRL/CDT equivalence, common-parent principle, `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, or any new quantum-gravity theory.
