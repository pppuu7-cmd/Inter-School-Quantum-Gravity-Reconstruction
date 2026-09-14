# ITER068 preregistration — CDT / HaPPY composition-type discrimination

Date: 2026-09-14
Gate: `ITER068_CDT_HAPPY_COMPOSITION_TYPE_DISCRIMINATION`
Status at commit: `PREREGISTERED / NOT YET ADJUDICATED`

## SCIENTIFIC_QUESTION

Does the exact regulated full-state CDT composition package qualified in ITER067 and the exact HaPPY perfect-tensor/QEC composition package instantiate one **physically meaningful typed composition principle** under explicit maps that preserve the mandatory physical coordinates, or does the shared Interface-Atlas coordinate `C` split into inequivalent operation types once dynamics, normalization/isometry, causal/time semantics and observables are kept explicit?

This is a mechanism/type-discrimination gate. It is not a test that HaPPY is a complete quantum-gravity realization.

## SOURCE_OBJECTS

### CDT / RC002

Frozen source authority is the already-terminal ITER067 package, ultimately pinned to:

1. J. Ambjørn, J. Jurkiewicz, R. Loll, *Dynamically Triangulating Lorentzian Quantum Gravity*, arXiv `hep-th/0105267v1`, especially Eqs. (43)–(47) and the associated transfer-matrix/positivity discussion.
2. J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, J. Jurkiewicz, *The transfer matrix in four-dimensional CDT*, arXiv `1205.3791v1`.
3. J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, J. Jurkiewicz, R. Loll, *The transfer matrix method in four-dimensional causal dynamical triangulations*, arXiv `1302.2210v1`.

Qualified object:

`G_N(g1,g2;t1+t2) = sum_g C(g) G_N(g1,g;t1) G_N(g,g2;t2)`

with full spatial-triangulation states, automorphism-weighted identity resolution, one-step sandwich amplitudes, preferred discrete proper time, and only `T_N^2` positivity/Hamiltonian authority in d>2.

### HaPPY / RC005

Frozen primary source:

F. Pastawski, B. Yoshida, D. Harlow, J. Preskill, *Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence*, arXiv `1503.06237v2`, JHEP 06 (2015) 149, DOI `10.1007/JHEP06(2015)149`.

Frozen exact objects:

- Definition 1 / Eqs. (1)–(2): isometry `T: H_A -> H_B` with `T^\dagger T = I_A`;
- Definition 2: a perfect tensor is proportional to an isometry for every bipartition with `|A| <= |A^c|`;
- Section 3 construction: internal tensor legs are contracted; open bulk legs are logical inputs, open boundary legs are physical degrees of freedom;
- Theorem 1: the pentagon-tiling network is an isometry from the bulk Hilbert space to the boundary Hilbert space, proved by composing layer-wise isometries.

## SOURCE_VERSIONS

CDT versions are inherited unchanged from ITER067. HaPPY is frozen to arXiv `1503.06237v2` (submitted v1 2015-03-20; v2 2015-07-22, minor corrections/bibliographic amendments).

No review article may substitute for these source objects.

## SOURCE_SCHOOL / SOURCE_SCOPE

### CDT

`SOURCE_SCHOOL = causal dynamical triangulations`

`SOURCE_OBJECT = regulated transfer matrix / state-sum semigroup composition`

`SOURCE_SCOPE = finite-cutoff spatial-triangulation state space with preferred discrete proper time; Wick-rotated positivity package qualified only as in ITER067`

### HaPPY

`SOURCE_SCHOOL = holographic quantum-information / tensor-network toy model`

`SOURCE_OBJECT = perfect-tensor contraction and bulk-to-boundary isometric encoding`

`SOURCE_SCOPE = static exact toy code; not a full gravitational dynamics or Lorentzian causal theory`

## DOMAIN

The comparison is restricted to the source-defined local composition mechanisms themselves.

No continuum limit, GR recovery, generic AdS/CFT, generic tensor networks, full holography, or complete QG theory is in scope.

## MAP_OR_OBSERVABLE

The candidate common object is a typed composition schema `P` with embeddings

`F_CDT : C_CDT -> P`

`F_HAPPY : C_HAPPY -> P`

where a positive result requires more than forgetting semantics until both become generic matrix multiplication.

Mandatory preservation table:

| coordinate | CDT | HaPPY | required for strong common-type PASS |
|---|---|---|---|
| DOMAIN/CODOMAIN | spatial triangulation states across proper-time slices | bulk/logical factors to boundary/physical factors | explicit typed correspondence |
| COMPOSITION | temporal semigroup / gluing over intermediate geometry | tensor-leg contraction / layer-wise isometry composition | explicit composition-preserving map |
| NORMALIZATION/MEASURE | `C(g)`, `1/C(T)` automorphism weights | Hilbert inner product and isometric normalization (`T^dagger T=I`, up to stated perfect-tensor proportionality) | preservation/derivation, not omission |
| DYNAMICS | transfer amplitudes from state-sum action | static encoding map; no gravitational time-evolution law in frozen source | explicit dynamics relation required |
| CAUSAL/TIME SEMANTICS | distinguished discrete proper-time succession | no source-defined fundamental Lorentzian temporal succession in the static code | explicit relation required |
| OBSERVABLE SEMANTICS | regulated boundary-transition amplitudes / triangulation-state propagation; reduced volume matrix explicitly distinct | encoded logical operators, boundary reconstruction, entanglement/QEC observables | explicit observable correspondence required |

## NORMALIZATION

A strong common-type claim must preserve or derive both:

1. CDT automorphism-weighted gluing/identity structure; and
2. HaPPY isometric inner-product structure.

Erasing these to plain index contraction is an admissible **weak algebraic forgetful map**, but does not satisfy the strong physical hypothesis.

## MEASURE

CDT: explicit combinatorial path-sum measure `1/C(T)` and intermediate state factor `C(g)`.

HaPPY: no analogous sum-over-histories measure is assumed. The relevant exact structure is Hilbert-space normalization/isometry of the encoder.

A proposed common principle may not manufacture a HaPPY history measure or silently reinterpret its isometry as CDT measure data.

## GAUGE_QUOTIENT

CDT automorphism quotients/symmetry factors are retained.

HaPPY tensor-leg/basis freedoms may be acknowledged only when source-defined; no identification with CDT automorphism equivalence is assumed.

## COMPOSITION_OR_REFINEMENT

Primary candidate relation: `COMPOSITION` only.

No `REFINEMENT` equivalence is assumed. A radial/layer interpretation of HaPPY is not automatically CDT temporal refinement, and a CDT time step is not automatically a tensor-network renormalization layer.

## IMPORTED_ASSUMPTIONS FIREWALL

Any identification of

- CDT discrete proper time with HaPPY radial/layer depth,
- CDT transfer dynamics with HaPPY encoding,
- CDT automorphism measure with HaPPY isometric normalization,
- CDT spatial geometry with HaPPY logical/boundary subsystem factorization,

must be labelled `NEW_BRIDGE_ASSUMPTION` unless explicitly derived from the frozen sources.

## CONTROLS

C1 `FORGETFUL_LINEARIZATION_CONTROL` — map both mechanisms only to generic finite-dimensional linear-map composition. Expected to show a weak algebraic commonality; it is a null against overclaiming physical equivalence.

C2 `TIME_RADIAL_SWAP_CONTROL` — replace CDT proper-time succession by HaPPY layer/radial ordering without a source-defined derivation. Must be rejected as imported semantics.

C3 `NORMALIZATION_DROP_CONTROL` — drop `C(g)/1/C(T)` on CDT or `T^dagger T=I` on HaPPY. Must be detected as structure loss.

C4 `FULL_EFFECTIVE_COLLAPSE_CONTROL` — substitute CDT's reduced volume effective matrix for the full transfer operator. Must be rejected by inherited ITER067 authority.

C5 `DYNAMICS_ENCODING_SWAP_CONTROL` — treat HaPPY encoder as a gravitational time-evolution operator or treat CDT transfer propagation as QEC encoding. Must be rejected unless the source defines the identification.

C6 `OBSERVABLE_ERASURE_CONTROL` — claim a common physical operation while omitting the mismatch between transition-amplitude observables and logical/QEC reconstruction observables. Must be rejected.

C7 `TOY_MODEL_PROMOTION_CONTROL` — promote HaPPY to a full QG realization. Must be rejected.

## PASS

`PASS_SCOPED / LOCAL_COMMON_COMPOSITION_TYPE_CANDIDATE` only if explicit typed maps can be constructed from frozen source-defined structures such that:

1. composition is preserved on both sides;
2. normalization/measure structures have an explicit common image or derivation;
3. the dynamics-versus-encoding distinction is resolved by a source-defined relation, not erased;
4. causal/time semantics have an explicit relation, not a label substitution;
5. at least one nontrivial observable class is transported consistently;
6. all controls C1–C7 behave as intended.

Even PASS gives no bridge credit; it would authorize only a further full-realization/common-parent falsification gate.

## FAIL

`FAIL_SCOPED / PHYSICAL_COMPOSITION_TYPE_EQUIVALENCE_REJECTED` if the only common map is a forgetful algebraic map (e.g. generic linear-map/tensor contraction) and at least one mandatory physical coordinate — dynamics, normalization/measure, causal/time semantics, or observables — cannot be preserved or derived without a `NEW_BRIDGE_ASSUMPTION`.

A FAIL may coexist with a positive weak statement `COMMON_ALGEBRAIC_KERNEL_ONLY`.

## BLOCKED

`BLOCKED_SOURCE_AUTHORITY` or `BLOCKED_MISSING_REQUIRED_OBJECT` if a mandatory source object needed to decide the above is not present or cannot be source-qualified.

## INVALID

`INVALID_PROVENANCE` for version/source mismatch or missing immutable authority.

`INVALID_IMPLEMENTATION` for comparator logic that fails to apply the frozen mandatory table/controls.

## ADVERSARIAL CRITIC

After the researcher classification, an independent critic must attempt to defeat it by:

- constructing a stronger common typed map using only frozen objects;
- checking whether categorical composition in Hilbert spaces already suffices physically rather than merely algebraically;
- checking basis/gauge and automorphism semantics;
- checking whether HaPPY layer ordering carries any source-defined causal/dynamical content strong enough to meet the CDT side;
- checking whether the CDT transfer operator has an isometric/QEC interpretation in the frozen source;
- checking whether observable classes can be transported rather than erased;
- checking toy-model/full-QG scope leakage.

If the critic exhibits a source-faithful strong map satisfying all mandatory coordinates, a researcher FAIL is overturned. If the critic shows a missing source object prevents adjudication, classification becomes BLOCKED rather than FAIL.

## CLAIM_CEILING

Forbidden from this gate:

- `BRIDGE_DERIVED`;
- `UNIVERSAL_COMMON_PARENT_FOUND`;
- HaPPY as full quantum gravity;
- CDT/HaPPY equivalence;
- continuum/GR recovery;
- foliation independence;
- new physics;
- candidate-theory formation.

`CANDIDATE_THEORY = UNFORMED`

`THEORY_ESTABLISHED = 0%`

`BRIDGE_CREDIT = 0`

## DOWNSTREAM_AUTHORIZATION

PASS: authorize only a new prospective falsification gate for the typed common-composition candidate against at least one additional full-QG realization and a countermodel search.

FAIL: split atlas coordinate `C` into at least `C_seq` (temporal/state-sum sequential composition) and `C_tensor` (subsystem/tensor-contraction encoding composition) for bridge work; prioritize a comparator that shares one of these typed semantics rather than the generic word `composition`.

BLOCKED/INVALID: repair only the exact missing authority/provenance/implementation defect; no scientific rerun with changed predicates.