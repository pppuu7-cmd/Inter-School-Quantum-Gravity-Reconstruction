# ITER100 preregistration — FRG nonlocal QRC composite-expectation authority

Date: 2026-09-15
Gate: `ITER100_FRG_NONLOCAL_QRC_COMPOSITE_EXPECTATION_AUTHORITY`

## Motivation frozen before source adjudication

ITER099 established that the **same finite-radius QRC metric functional** can be evaluated on the source-qualified FRG self-consistent smooth metric. It also isolated the remaining quantum blocker: CDT measures an ensemble expectation of this nonlinear nonlocal functional, while the reduced FRG result presently provides only a background evaluation.

ITER100 asks whether existing asymptotic-safety/FRG observable machinery closes that gap at source level.

## Frozen QRC target object

The required object is not merely a local Ricci scalar. It is the finite-radius functional built from:

1. geodesic distance `d_g(x,y)`;
2. geodesic spheres `S_p^delta` defined by a fixed-distance condition;
3. their induced hypersurface measures/volumes;
4. a normalized double integral of `d_g(x,x')` over two equal-radius spheres with centres separated by `delta`;
5. point/direction averaging and ultimately a quantum expectation value.

A valid FRG construction may use equivalent relational/composite notation, but all five structures must remain identifiable.

## Frozen source stack

- arXiv:1611.06522 — Pagani & Reuter, *Composite Operators in Asymptotic Safety*.
- arXiv:1810.11816 — Becker & Pagani, *Geometric operators in the asymptotic safety scenario for quantum gravity*.
- arXiv:2112.02118 — Baldazzi, Falls & Ferrero, *Relational observables in asymptotically safe gravity*.
- arXiv:1712.08847 and arXiv:2006.06263 only to type the target QRC observable.
- ITER099 only as prior claim/type authority.

## Required predicates

A. FRG composite-operator formalism admits genuinely metric-dependent geometric operators, not only action couplings.

B. Geodesic length/distance is explicitly treated or source-qualified as a composite geometric operator.

C. Geodesic ball/sphere or hypersurface-volume ingredients needed by QRC are explicitly treatable with source-defined operator semantics.

D. Fixed-geodesic-distance constraints / sphere localization are source-defined strongly enough to construct the QRC integration domains without replacing them by coordinate spheres.

E. The normalized double-sphere average of pairwise geodesic distance is explicitly constructed, or follows from a source-derived closed operator algebra with all necessary renormalization/mixing accounted for.

F. The formalism yields or defines the RG evolution toward the **quantum expectation value** of that same nonlocal object, rather than only its value on a background metric.

G. Relational-coordinate formulations do not silently replace metric geodesic spheres by coordinate spheres.

H. No CDT QRC target values, fitted sphere radii, or shape data may be used to choose FRG operator normalizations/truncations.

## Frozen classifications

- `PASS_SCOPED_EXPLICIT_QRC_COMPOSITE_EXPECTATION_AUTHORITY` if A-F all pass for an explicit QRC-equivalent operator.
- `PASS_SCOPED_QRC_INGREDIENTS_EXIST_CLOSED_CONSTRUCTION_OPEN` if A-D pass materially but E/F remain unresolved.
- `SCOPED_BLOCKED_GENERIC_COMPOSITE_FORMALISM_NO_QRC_CLOSURE` if generic/ingredient authority exists but the exact nonlocal QRC operator and expectation flow are not source-derived.
- `FAIL_SCOPED_FRG_CANNOT_REPRESENT_QRC` only if the formalism explicitly excludes the required construction.
- `INFRASTRUCTURE_FAIL` only for source-access failure.

## Controls

- `LOCAL_CURVATURE_SUBSTITUTION_CONTROL`
- `GEODESIC_COORDINATE_DISTANCE_SWAP_CONTROL`
- `BACKGROUND_EXPECTATION_SWAP_CONTROL`
- `INGREDIENTS_CLOSURE_CONTROL`
- `OPERATOR_MIXING_ERASURE_CONTROL`
- `TARGET_FIT_CONTROL`

## Claim ceiling

A PASS would authorize at most a source-defined same-observable quantum-composite route. It would not establish numerical CDT/FRG agreement, a unique trajectory, a shared fixed point, theory equivalence, `BRIDGE_DERIVED`, new physics, or a candidate theory.