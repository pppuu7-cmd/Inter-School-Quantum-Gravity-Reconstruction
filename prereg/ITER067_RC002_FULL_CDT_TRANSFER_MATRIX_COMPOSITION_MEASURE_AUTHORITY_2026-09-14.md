# ITER067 — RC002 full CDT transfer-matrix composition/measure authority gate

Date frozen: 2026-09-14

## GATE_ID

`ITER067_RC002_FULL_CDT_TRANSFER_MATRIX_COMPOSITION_MEASURE_AUTHORITY`

## SCIENTIFIC_QUESTION

In the source-grounded 4D CDT realization, does the **full regulated transfer matrix on spatial triangulation states** — not merely the effective matrix reduced to spatial three-volume / scale factor — supply a mathematically explicit composition object together with source-defined path-integral measure/normalization and positivity/Hamiltonian structure sufficient to qualify a local `D/C/M` structural-map component for later inter-school comparison? Which parts of that structure depend essentially on CDT's preferred discrete proper-time slicing and Wick rotation?

This gate does not ask whether CDT is correct, whether a continuum limit exists, or whether its transfer matrix is equivalent to an EPRL/spinfoam gluing law.

## SOURCE_OBJECTS

Frozen primary-source stack:

1. J. Ambjørn, J. Jurkiewicz, R. Loll, **Dynamically Triangulating Lorentzian Quantum Gravity**, arXiv `hep-th/0105267v1`, Nucl. Phys. B610 (2001) 347–382, DOI `10.1016/S0550-3213(01)00297-8`.
   - authoritative target for the full regulated state sum, full transfer matrix, Hilbert/state space, measure factor, Wick rotation, positivity and Hamiltonian claims in d=3,4.
2. J. Ambjørn, J. Gizbert-Studnicki, A. T. Görlich, J. Jurkiewicz, **The transfer matrix in four-dimensional CDT**, arXiv `1205.3791v1`, JHEP 1209 (2012) 017, DOI `10.1007/JHEP09(2012)017`.
   - authoritative target for the relationship between the underlying full transfer matrix and the measured/effective transfer matrix labelled by spatial volume.
3. J. Ambjørn, J. Gizbert-Studnicki, A. T. Görlich, J. Jurkiewicz, R. Loll, **The transfer matrix method in four-dimensional causal dynamical triangulations**, arXiv `1302.2210v1`, DOI `10.1063/1.4791727`.
   - independent same-realization cross-check of full-vs-effective semantics and discrete-time transfer-matrix interpretation.

Reviews already listed in `realizations/RC-002_4D_CDT_TRANSFER_MATRIX.md` may be used only for navigation and interpretation checks, never to replace missing primary-source authority.

## SOURCE_VERSIONS

The three arXiv versions above are frozen exactly as `v1`. No later paper or revised source may be added after observing the gate result. A newly discovered source object requires a new gate/version and cannot retroactively alter ITER067.

## DOMAIN

- 3+1-dimensional / d=4 CDT regulated Lorentzian triangulations with the model's discrete proper-time slicing and fixed spatial topology as specified by the source.
- Boundary/state objects are spatial triangulations/equivalence classes used by the full transfer matrix.
- Euclideanized transfer-matrix statements are admitted only with their source-defined Wick-rotation relation to the Lorentzian regulated model explicitly recorded.
- Effective matrices labelled only by total spatial three-volume are treated as reduced/projection objects and may not be silently substituted for the full matrix.

## MAP_OR_OBSERVABLE

Target structural map:

`T_full : H_slice -> H_slice`

and its source-defined matrix elements / propagators between spatial triangulations, together with the exact composition/gluing relation over an intermediate slice.

The gate must identify, from primary equations/definitions:

A. `FULL_STATE_SPACE`: the states and inner product / basis-equivalence convention on which `T_full` acts.

B. `FULL_MATRIX_ELEMENT`: the full transfer-matrix element as a regulated sum/amplitude over one-step interpolating triangulations, including its combinatorial/measure weight.

C. `COMPOSITION`: the exact multi-step composition/gluing rule (matrix multiplication / sum over intermediate spatial states with the correct measure or symmetry factors).

D. `POSITIVITY_HAMILTONIAN`: the strongest positivity/reflection-positivity/self-adjoint-Hamiltonian statement actually proven for the source-defined transfer matrix, including whether it applies to `T`, `T^2`, link reflection, site reflection, a dimension-restricted sector, or another qualified object.

E. `FULL_VS_EFFECTIVE`: the exact logical relation between `T_full` and the spatial-volume effective matrix used in 4D measurements. Projection/coarse observable agreement must not be promoted to operator equality unless the source proves it.

F. `TIME_WICK_DEPENDENCE`: which parts of A–E rely on the preferred discrete proper-time foliation and/or configuration-wise Wick rotation.

## NORMALIZATION

Freeze only source-defined normalization/symmetry factors in the discrete state sum and transfer-matrix inner product. No post-hoc rescaling of matrix elements is allowed to manufacture stochasticity, unitarity, reflection positivity, or cross-school agreement.

Continuum physical normalization is outside this gate unless explicitly proven by the frozen primary sources.

## MEASURE

The relevant measure is the regulated CDT state-sum/combinatorial measure stated in the frozen sources, including automorphism/symmetry factors where present.

A merely fitted effective minisuperspace action is not a substitute for the full path-integral/transfer-matrix measure.

## GAUGE_QUOTIENT

Record exactly how labelled triangulations, unlabelled triangulations / equivalence classes, diffeomorphism-equivalent discrete geometries, and automorphism factors enter the state space and matrix elements. No extra gauge averaging may be introduced by ISQGR.

## COMPOSITION_OR_REFINEMENT

This is a **composition** authority gate, not a continuum-refinement theorem.

Mandatory structural arrow:

`boundary triangulation at t` -> `one-step full CDT amplitude` -> `boundary triangulation at t+1`,

with source-defined multi-step gluing through a sum over intermediate states.

A PASS does not imply scale refinement, RG naturality, or representation-independent composition.

## CONTROLS

1. **Full/effective null control:** replace the full triangulation-state matrix by the volume-labelled effective matrix. The audit must detect the scope reduction rather than treating them as identical.
2. **Measure-drop null control:** remove the source symmetry/automorphism weight. The candidate must then fail source fidelity.
3. **Time-structure null control:** erase the preferred discrete time slicing. Any composition law whose definition requires that slicing must be flagged as changed/undefined, not called representation-independent.
4. **Positivity-strength control:** distinguish positivity/reflection positivity of `T`, `T^2`, or another qualified object. No strengthening is allowed.
5. **Wick-rotation control:** Lorentzian and Euclidean transfer objects must not be conflated without the source-defined analytic continuation.
6. **Reduced-observable control:** agreement of volume distributions/effective action cannot establish equality of the full operator or measure.

## PASS

`PASS_SCOPED / STRUCTURAL_MAP_ESTABLISHED_SCOPED` only if primary-source authority establishes all of the following without imported assumptions:

- A, B and C exactly for the full regulated transfer matrix;
- a source-defined regulated measure/normalization sufficient to interpret B and C;
- D with its exact limitation preserved;
- E explicitly separating the full operator from the effective volume-reduced object;
- F explicitly recording preferred-time/Wick-rotation dependence;
- all controls correctly detect their intended scope violations.

A PASS authorizes only a local CDT composition-map component for a later separately preregistered cross-school comparison.

## FAIL

`FAIL_SCOPED` only if a frozen source explicitly contradicts a preregistered required property that it purported to establish, after domain/version checks, rather than merely omitting it.

## BLOCKED

`BLOCKED_SOURCE_AUTHORITY / BLOCKED_MISSING_REQUIRED_OBJECT` if any of A–C or the regulated measure relation needed to interpret them is not explicitly source-defined, or if the primary sources only establish the effective volume-reduced matrix while the full object remains insufficiently specified for this gate.

A weaker positivity theorem does not by itself force BLOCKED if its exact scope is sufficient to define the regulated composition object and is preserved in the terminal label; it does cap downstream claims.

## INVALID

`INVALID_IMPLEMENTATION` or `INVALID_PROVENANCE` if the audit uses a wrong source/version, conflates full and effective matrices, silently changes the measure/normalization, misreads the Wick-rotated object as the Lorentzian one, or lacks exact primary-source equation/object provenance.

## CLAIM_CEILING

Even `PASS_SCOPED` does **not** establish:

- a continuum limit theorem;
- full GR recovery;
- foliation independence;
- representation-independent composition;
- equivalence to EPRL/spinfoam/GFT composition;
- a common parent principle;
- `BRIDGE_DERIVED`;
- `NEW_PHYSICS_FOUND`;
- a candidate quantum-gravity theory.

`CANDIDATE_THEORY=UNFORMED`, `THEORY_ESTABLISHED=0%`, `BRIDGE_CREDIT=0` remain locked.

## DOWNSTREAM_AUTHORIZATION

If `PASS_SCOPED`, the only newly authorized successor is a separately preregistered **cross-school composition-arrow audit** comparing exact CDT `T_full` composition with another already source-qualified composition law while preserving state-space, measure, gauge and causal-time mismatches.

If BLOCKED/FAIL/INVALID, do not fabricate a transfer/refinement surrogate; use the exact missing/failed object to reschedule the Phase-1 frontier.
