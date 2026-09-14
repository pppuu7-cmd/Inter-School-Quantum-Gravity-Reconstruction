# ITER101 preregistration — QRC small-delta ↔ relational-curvature operator expansion authority

Date: 2026-09-15
Gate: `ITER101_QRC_SMALL_DELTA_RELATIONAL_CURVATURE_OPERATOR_EXPANSION_AUTHORITY`

## Motivation frozen before coefficient adjudication

ITER100 established FRG source authority for the main geometric ingredients of QRC but not a closed finite-radius QRC composite operator. A controlled alternative is to ask whether the QRC functional has a smooth small-radius expansion whose first curvature-dependent term is a local curvature composite already represented in FRG relational-observable machinery.

This gate is an **asymptotic operator-typing test**, not a finite-radius CDT fit.

## Frozen sources

- arXiv:1712.08847 — smooth-manifold QRC construction and expansions.
- arXiv:1802.10524 — *Implementing quantum Ricci curvature*; dimension-dependent smooth expansion authority.
- arXiv:2112.02118 — FRG relational scalar-curvature composite operator.
- ITER083B, ITER099 and ITER100 only as prior type/claim authority.

## Frozen question

In `D=4`, does the smooth QRC/normalized-average-sphere-distance expansion at `delta -> 0`, after the same directional averaging used to define the scalar QRC profile, reduce at leading nontrivial order to a source-defined coefficient times the local scalar curvature `R`, so that this coefficient can be typed against the FRG relational scalar-curvature composite operator?

## Required predicates

A. The `D=4` expansion of `dbar/delta` must be source-explicit through the first curvature-dependent order.

B. `Ric(v,v)` and `R` contributions must remain distinct until directional averaging is performed.

C. Directional averaging must be mathematically/source justified; for an isotropic average over unit directions, `<Ric(v,v)>_v = R/D` may be used.

D. The resulting leading scalar-curvature coefficient must be fixed independently of CDT numerical target data.

E. The FRG relational scalar-curvature object must be source-defined as a quantum composite observable, with its truncation/reference-field semantics retained.

F. The relation must be stated only as `delta -> 0` / smooth-manifold asymptotics. Higher-order curvature/derivative terms remain explicit remainder authority.

G. Lattice artefacts and the fact that accessible CDT QRC measurements require `delta` above the cutoff-dominated regime must prevent direct finite-radius promotion.

H. No `delta <-> 1/k` relation may be inferred from dimensionality alone.

## Frozen classifications

- `PASS_SCOPED_SMALL_DELTA_QRC_TO_RELATIONAL_SCALAR_OPERATOR_MAP` if A-F pass, with G-H retained as ceilings.
- `PASS_SCOPED_DIRECTIONAL_CURVATURE_ONLY` if the leading term remains direction-dependent and does not reduce to scalar curvature under the frozen averaging.
- `BLOCKED_SOURCE_AUTHORITY` if coefficients/averaging cannot be established.
- `FAIL_SCOPED_LOCAL_EXPANSION_INCOMPATIBLE` if the QRC expansion does not contain the required local curvature structure.

## Controls

- `FINITE_RADIUS_PROMOTION_CONTROL`
- `DIRECTIONAL_SCALAR_SWAP_CONTROL`
- `HIGHER_ORDER_REMAINDER_ERASURE_CONTROL`
- `LATTICE_SMALL_DELTA_CONTROL`
- `DELTA_K_SWAP_CONTROL`
- `TARGET_FIT_CONTROL`

## Claim ceiling

A PASS may establish a local asymptotic operator crosswalk only. It cannot establish equality of finite-radius QRC profiles, `delta=1/k`, numerical CDT/FRG agreement, a shared trajectory/fixed point, full theory equivalence, `BRIDGE_DERIVED`, new physics, or a candidate theory.