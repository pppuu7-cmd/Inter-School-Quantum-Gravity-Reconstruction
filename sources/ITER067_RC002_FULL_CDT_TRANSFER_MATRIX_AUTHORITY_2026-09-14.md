# ITER067 — RC002 full CDT transfer-matrix source authority

Date: 2026-09-14
Gate: `ITER067_RC002_FULL_CDT_TRANSFER_MATRIX_COMPOSITION_MEASURE_AUTHORITY`
Preregistration: `prereg/ITER067_RC002_FULL_CDT_TRANSFER_MATRIX_COMPOSITION_MEASURE_AUTHORITY_2026-09-14.md`

## Frozen primary sources

1. Ambjørn, Jurkiewicz, Loll, **Dynamically Triangulating Lorentzian Quantum Gravity**, arXiv `hep-th/0105267v1`, Nucl. Phys. B610 (2001) 347–382, DOI `10.1016/S0550-3213(01)00297-8`.
2. Ambjørn, Gizbert-Studnicki, Görlich, Jurkiewicz, **The transfer matrix in four-dimensional CDT**, arXiv `1205.3791v1`, JHEP 1209 (2012) 017, DOI `10.1007/JHEP09(2012)017`.
3. Ambjørn, Gizbert-Studnicki, Görlich, Jurkiewicz, Loll, **The transfer matrix method in four-dimensional causal dynamical triangulations**, arXiv `1302.2210v1`, DOI `10.1063/1.4791727`.

All three version histories were checked before the substantive audit; each frozen arXiv object has only the cited `v1` in the gate.

## A — FULL_STATE_SPACE: PASS

The 2001 primary source defines boundary data as unlabelled spatial triangulations `g` of fixed topology at integer proper times. Eq. (44) gives the scalar product and resolution of identity:

`<g1|g2> = delta(g1,g2)/C(g1)`

and

`sum_g C(g) |g><g| = 1`.

For a spatial-volume cutoff `N`, the finite-dimensional regulated Hilbert space `H^(N)` is explicitly the span of spatial triangulation states with allowed volume bounded by `N`.

The 2013 same-realization source independently restates the Hilbert-space basis as 3D triangulations of `S^3` and the automorphism-weighted inner product.

**Decision:** `FULL_STATE_SPACE_QUALIFIED_REGULATED = true`.

## B — FULL_MATRIX_ELEMENT + regulated measure: PASS

The 2001 source first fixes the full regulated state sum, Eq. (43):

`Z = sum_T [1/C(T)] exp(i S(T))`,

where the sum is over inequivalent Lorentzian triangulations and `C(T)` is the order of the automorphism group. The source explicitly identifies

`m(T) = 1/C(T)`

as the dynamical-triangulation measure factor.

Eq. (45) then defines the full one-step transfer-matrix element

`<g2|T_N(alpha)|g1> = G_alpha(g1,g2;1)`

as a sum over **all distinct interpolating d-dimensional sandwich triangulations** `T: g1 -> g2`, each carrying `1/C(T)` and the source action phase `exp(i Delta S_alpha(T))`.

This is the full triangulation-state object, not the later volume-only effective matrix.

**Decision:** `FULL_MATRIX_ELEMENT_AND_REGULATED_MEASURE_QUALIFIED = true`.

## C — COMPOSITION: PASS

Eq. (46) defines arbitrary integer-time propagation by iteration:

`G_N(g1,g2;t) = <g2|T_N^t|g1>`.

Eq. (47) gives the exact semigroup/gluing law

`G_N(g1,g2;t1+t2) = sum_g C(g) G_N(g1,g;t1) G_N(g,g2;t2)`.

The primary source explains why the intermediate factor `C(g)` is required: it compensates the boundary/sandwich automorphism structure so each glued geometry appears with the correct symmetry factor inherited from Eq. (45).

This is precisely the preregistered regulated composition arrow. Dropping the symmetry factor changes the source-defined gluing law.

**Decision:** `FULL_COMPOSITION_LAW_QUALIFIED_REGULATED = true`.

## D — POSITIVITY / HAMILTONIAN: PASS WITH MANDATORY LIMITATION

The positivity result must not be strengthened.

The source Wick-rotates to the Euclidean transfer matrix for the statistical/Hamiltonian analysis. In `d>2` it explicitly corrects an earlier stronger claim and states that the required symmetry/positivity/boundedness properties are established for the **two-step transfer matrix `T_N^2`**, not generally for the elementary one-step `T_N`.

The detailed statements are:

- `T_N` is symmetric under exchange of in/out states.
- Site-reflection positivity is proven and is sufficient to imply positivity of `T_N^2`.
- Link-reflection positivity, which would imply positivity of elementary `T_N`, is straightforward in `d=2` but is not established in higher dimensions; the authors explicitly allow that `T_N` itself may fail to be positive for `d=3,4`.
- A Hamiltonian is constructed from the two-step object as

  `h'_N = -(1/(2a)) log(T_N^2)`.

- Possible accidental zero-eigenvectors are handled by the quotient

  `H_ph^(N) = H^(N) / N^(N)`.

- At finite spatial-volume cutoff, boundedness follows from finite-dimensionality and finite matrix elements built as finite sums of `exp(-S)/C(T)`.

**Decision:** `T2_POSITIVITY_HAMILTONIAN_QUALIFIED_REGULATED = true`; `ELEMENTARY_T_POSITIVITY_D4 = NOT_ESTABLISHED`.

This limitation is scientifically material and is carried into the terminal label/claim ceiling.

## E — FULL_VS_EFFECTIVE: PASS

The 2012 four-dimensional primary source explicitly distinguishes two objects.

First, the CDT transfer matrix relates complete spatial triangulations at adjacent discrete times and is defined on the much larger space spanned by triangulation states. It gives the slab amplitude by summing over compatible 4D triangulations and uses the automorphism-weighted scalar product.

Second, the paper introduces an **effective** transfer matrix labelled only by spatial three-volume / scale factor. It is built from averages over the full matrix elements associated with all triangulations of a given volume. The authors explicitly warn that it is misleading to identify the volume label with a single normalized full-state vector; the correct reduced description is related to a uniform distribution/density operator over the full states. They then state that use of the reduced object as an effective transfer matrix is an approximation whose quality depends on the dispersion of the underlying full-matrix elements and is checked numerically.

The 2013 source independently states that the theory has a transfer matrix on spatial geometries while the measured scale factor is described by an effective matrix labelled only by that scale factor.

**Decision:** `FULL_EFFECTIVE_SEPARATION_QUALIFIED = true`; `EFFECTIVE_EQUALS_FULL = false`.

## F — TIME / WICK DEPENDENCE: PASS, dependency is essential

The 2001 source defines CDT histories as globally hyperbolic simplicial manifolds with a sliced structure and says the discrete proper-time label is part of the invariant geometric data rather than a coordinate gauge choice. The transfer matrix is then defined per `Delta t = 1` sandwich.

The 2012 source states directly that the time foliation present in CDT provides the transfer matrix. The 2013 source likewise formulates the regulated path integral with discrete proper time and a global time foliation.

The 2001 source separately defines the Lorentzian transfer matrix `T_N(alpha)` and then performs the positivity/Hamiltonian analysis on the Wick-rotated Euclidean matrix `T_N(-1)`. The source therefore supplies a relation between the Lorentzian regulated amplitude and the Euclidean statistical transfer object, but it does **not** authorize erasing the foliation or treating Euclidean positivity as a representation-independent Lorentzian composition theorem.

**Decision:** `PREFERRED_DISCRETE_TIME_DEPENDENCE = ESSENTIAL_IN_SOURCE_CONSTRUCTION`; `WICK_RELATION_SOURCE_DEFINED = true`.

## Frozen controls

1. **Full/effective null:** DETECTED. The 2012 paper explicitly defines the volume-labelled effective object as a reduced/averaged approximation, not the full operator.
2. **Measure-drop null:** DETECTED. Eqs. (43)–(47) require the automorphism factors; the intermediate `C(g)` is explicitly justified by composition.
3. **Time-structure null:** DETECTED. One-step sandwiches, semigroup time composition and reflection planes use distinguished discrete proper time.
4. **Positivity-strength null:** DETECTED. In `d=3,4`, source authority reaches `T^2`; elementary-`T` positivity is not proven and may fail.
5. **Wick null:** DETECTED. Lorentzian `T_N(alpha)` and Wick-rotated Euclidean `T_N(-1)` have distinct roles.
6. **Reduced-observable null:** DETECTED. Scale-factor/volume agreement is evidence for the effective matrix, not equality with the full transfer operator.

## Object table

| coordinate | source-defined CDT object | status in ITER067 |
|---|---|---|
| S | spatial triangulation states, automorphism-weighted inner product | PASS_REGULATED |
| D | one-step transfer amplitude over sandwich triangulations | PASS_REGULATED |
| M | `1/C(T)` combinatorial state-sum measure; `C(g)` state normalization | PASS_REGULATED |
| C | exact semigroup/gluing Eq. (47) | PASS_REGULATED |
| G | inequivalent triangulations / automorphism quotient semantics | PASS_REGULATED |
| K | globally hyperbolic sliced causal construction | PASS_REGULATED |
| positivity | site reflection -> `T^2` positivity in d>2 | PASS_WITH_LIMITATION |
| full/effective | full triangulation matrix vs volume-reduced effective matrix | EXPLICITLY_DISTINGUISHED |
| R | continuum/refinement/RG map | NOT_ESTABLISHED_BY_THIS_GATE |
| X/E | continuum and full GR recovery | OUTSIDE_GATE / NOT_ESTABLISHED |

## Source-authority conclusion

All preregistered mandatory A–F source objects are present with the exact positivity limitation preserved.

**Source verdict:** `PASS_SCOPED / STRUCTURAL_MAP_ESTABLISHED_SCOPED`.

The established map is a **regulated CDT composition component**:

`g_t  --T_full-->  g_(t+1)`

with exact source-defined automorphism-weighted gluing over an intermediate spatial triangulation.

It is not yet an inter-school bridge. In particular, the construction depends on CDT's distinguished discrete proper time, its state space of spatial triangulations, its automorphism measure, and the Wick-rotated positivity analysis. Those are candidate mismatch coordinates, not details to erase.

## Claim ceiling

No continuum theorem, foliation independence, scale-refinement law, EPRL equivalence, representation-independent composition law, common-parent principle, bridge, candidate theory or new physics follows from this source-authority PASS.