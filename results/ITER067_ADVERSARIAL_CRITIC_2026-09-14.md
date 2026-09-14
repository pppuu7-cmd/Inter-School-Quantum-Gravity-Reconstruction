# ITER067 adversarial critic — RC002 full CDT transfer matrix

Date: 2026-09-14
Target provisional conclusion: `PASS_SCOPED / STRUCTURAL_MAP_ESTABLISHED_SCOPED`

The critic attempts to destroy the positive source-authority result under the frozen preregistration.

## Attack 1 — The semigroup law may be only a bookkeeping identity, not a physical composition law

Eq. (47) is matrix multiplication over an intermediate slice. Could this be a trivial consequence of introducing a preferred time slicing, with no physical content?

**Result:** the objection limits scope but does not destroy the gate. The preregistered target is explicitly a **regulated CDT composition component**, not a representation-independent/common-parent law. Eq. (47) is source-defined at the physical regulated state-sum level, with nontrivial automorphism factors fixed so glued histories have the correct weights. It is therefore a real composition law inside this realization, although it remains dependent on CDT's preferred discrete proper time.

Critic classification: `SURVIVES_WITH_ESSENTIAL_TIME_STRUCTURE`.

## Attack 2 — Positivity is overclaimed because elementary `T` is not proven positive in 3+1D

The 2001 source explicitly says that in `d>2` the proven statement is weaker than positivity of the one-step transfer matrix. Site-reflection positivity gives positivity of `T_N^2`; link-reflection positivity, which would imply positivity of elementary `T_N`, is not established in higher dimensions and `T_N` itself may fail to be positive.

**Result:** this would invalidate any claim `ELEMENTARY_T_POSITIVE_D4` or an unqualified Hamiltonian `h=-a^-1 log T`. It does not invalidate the preregistered PASS because the prereg explicitly allowed the exact weaker theorem provided its limitation is preserved. The qualified Hamiltonian is constructed from `T_N^2` with possible zero modes quotiented.

Critic classification: `POSITIVE_RESULT_NARROWED_TO_T2_POSITIVITY`.

## Attack 3 — `1/C(T)` is merely combinatorial and cannot count as measure authority

The source labels `m(T)=1/C(T)` as the standard dynamical-triangulation measure factor and builds both matrix elements and the exact composition law with it. This is enough to define the **regulated** state-sum object tested by ITER067.

It is not enough to claim a continuum physical measure, universality of the measure prescription, or equality to another school's measure.

**Result:** gate survives; claim ceiling tightened to regulated measure only.

Critic classification: `REGULATED_MEASURE_ONLY`.

## Attack 4 — The finite-volume cutoff means the full transfer matrix is not really full

The positivity/boundedness proof is formulated on finite-dimensional `H^(N)` with a spatial-volume cutoff `N`. The word “full” could therefore be misleading if interpreted as continuum/infinite-volume.

**Result:** the prereg uses “full” only in the contrast **full triangulation-state operator vs volume-reduced effective operator**, and explicitly scopes the gate to a regulated object. It does not claim the continuum/infinite-volume operator. No invalidation if this distinction is preserved.

Critic classification: `FULL_STATE_NOT_CONTINUUM_FULL`.

## Attack 5 — The effective volume matrix may secretly be equivalent to the full matrix on the observables used

The 2012 paper defines an effective volume-labelled object from averages over full matrix elements and explicitly treats its use as an approximation whose quality is checked through dispersion/data consistency. It warns against identifying the volume label with a single normalized state in the full Hilbert space.

**Result:** no source authority for operator equality. Any later cross-school gate must use the full Eq. (45)/(47) object or explicitly declare a reduced comparator; it cannot use the effective matrix as if it were the full CDT composition law.

Critic classification: `FULL_EFFECTIVE_CONFLATION_REJECTED`.

## Attack 6 — Wick rotation could break the claimed Lorentzian physical interpretation

Eq. (45) is first defined with Lorentzian phase weights `exp(i Delta S_alpha)`. The positivity/Hamiltonian analysis is then performed after the source-defined Wick rotation to the Euclidean transfer matrix. Therefore positivity is not an independent direct proof about the raw Lorentzian one-step matrix.

**Result:** this is a genuine structural caveat, but it does not erase the regulated Lorentzian amplitude or its source-defined Wick relation. The PASS must carry separate fields for Lorentzian composition and Euclideanized positivity.

Critic classification: `WICK_DEPENDENCE_MANDATORY`.

## Attack 7 — Preferred foliation blocks a representation-independent common-parent claim

The source says the discrete proper time is part of the invariant geometric data of each history, and the transfer matrix exists because of this sliced structure. Removing the foliation destroys the source-defined one-step sandwiches and reflection planes.

**Result:** this is the strongest downstream obstruction. ITER067 establishes a local composition component but simultaneously proves that the currently source-qualified version is **not representation-independent as stated**. A future bridge must either preserve/translate this causal-time structure explicitly or derive why it is inessential in a controlled quotient/limit. Simply erasing it would fail source fidelity.

Critic classification: `COMMON_PARENT_PROMOTION_NOT_AUTHORIZED`.

## Attack 8 — Gauge/automorphism factors may be arbitrary normalization conventions

Eq. (44) and Eq. (47) show that `C(g)` is tied simultaneously to the scalar product, identity resolution and gluing. The 2001 source explains the subgroup relation between sandwich and boundary automorphism groups and why the intermediate `C(g)` produces the correct symmetry weight after gluing.

**Result:** the factors cannot be dropped or freely rescaled without changing the source-defined composition object. They are part of the bridge interface, not cosmetic normalization.

Critic classification: `AUTOMORPHISM_WEIGHT_STRUCTURAL`.

## Countermodel / nonuniqueness attempt

The positive result does not assert a unique common principle, so a countermodel need only test whether the observed composition law could arise without the stronger desired conclusions.

It can: any regulated transfer-matrix statistical system with a preferred discrete time can satisfy a semigroup law while having no gravitational continuum limit, no foliation independence and no relation to spin-foam gluing. Therefore the CDT semigroup property alone cannot derive H0 or a common parent.

This countermodel defeats any promotion from

`LOCAL_CDT_COMPOSITION_COMPONENT`

to

`REPRESENTATION_INDEPENDENT_COMPOSITION_PRINCIPLE`.

It does **not** defeat the local source-authority PASS.

## Critic verdict

The positive result survives only in the exact narrow form preregistered:

**`PASS_SCOPED / STRUCTURAL_MAP_ESTABLISHED_SCOPED`**

with mandatory qualifiers:

- full triangulation-state regulated transfer matrix, not continuum-full;
- `1/C(T)` regulated combinatorial measure;
- exact semigroup/gluing law with `C(g)` intermediate weighting;
- source-defined preferred discrete proper time is essential to the current construction;
- higher-dimensional positivity/Hamiltonian authority is carried by `T^2`, not generally elementary `T`;
- volume-labelled effective transfer matrix is a reduced approximate description, not the full operator;
- no representation-independent bridge or common parent is derived.

The critic therefore narrows but does not overturn the provisional PASS.