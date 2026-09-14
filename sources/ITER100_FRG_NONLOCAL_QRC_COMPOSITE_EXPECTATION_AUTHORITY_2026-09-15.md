# ITER100 source authority — FRG nonlocal QRC composite expectation

Date: 2026-09-15
Gate: `ITER100_FRG_NONLOCAL_QRC_COMPOSITE_EXPECTATION_AUTHORITY`
Preregistration: `df41c4df12c485a13056ef46857a4ef8221bfce0`

## Frozen source stack

- arXiv:1611.06522 — Pagani & Reuter, *Composite Operators in Asymptotic Safety*.
- arXiv:1810.11816 — Becker & Pagani, *Geometric operators in the asymptotic safety scenario for quantum gravity*.
- arXiv:2112.02118 — Baldazzi, Falls & Ferrero, *Relational observables in asymptotically safe gravity*.
- arXiv:1712.08847 / 2006.06263 — QRC target typing only.

## A. Metric-dependent geometric composite operators

**PASS.**

The composite-operator EAA formalism introduces sources for operators not normally retained in the action truncation and derives an exact composite-operator RG equation. The authors explicitly name volumes, lengths and geodesic distances as representative geometric operators.

This is genuine observable/operator machinery, not a relabeling of gravitational couplings.

## B. Geodesic distance / length

**PASS_SCOPED.**

The frozen composite/geometric-operator literature explicitly treats geodesic length as a metric-dependent composite operator and studies its anomalous scaling. The geodesic itself depends on the metric, so the formalism already encounters an essential nonlocal ingredient of QRC.

This materially strengthens the route opened by ITER099: FRG is not restricted to local curvature insertions.

## C. Geodesic ball/sphere measure

**PASS_SCOPED.**

The geometric-operator analysis treats volumes of submanifolds and analyzes geodesic balls; its sphere discussion defines a geodesic sphere by fixed geodesic radius and obtains the corresponding small-radius hypersurface-volume behavior. Thus both the induced hypersurface measure/volume idea and geodesically defined integration domains are present in source-qualified FRG geometric-operator work.

The available treatment is perturbative/truncation-scoped and does not by itself supply the full QRC operator.

## D. Fixed-distance localization

**PASS_SCOPED_INGREDIENT.**

A geodesic sphere is explicitly characterized by fixed metric geodesic distance from a centre. Therefore source semantics exist for metric-defined rather than coordinate-defined spheres.

However, the frozen stack does not construct the full two-centre QRC geometry with two equal-radius spheres whose centres are themselves constrained to be separated by the same radius while all of these metric-dependent constraints fluctuate quantum mechanically.

`GEODESIC_COORDINATE_DISTANCE_SWAP_CONTROL`: **PASS_CONTROL** — no coordinate-sphere substitution is authorized.

## E. Normalized double-sphere pair-distance operator

**OPEN / NOT SOURCE-DERIVED.**

No frozen FRG source explicitly constructs the QRC operator

`[Vol(S_p^delta) Vol(S_p'^delta)]^(-1) int_{S_p^delta} int_{S_p'^delta} d_g(x,x')`

with `d_g(p,p')=delta`, nor an equivalent relational representation.

The existence of each ingredient separately is not sufficient to infer multiplicative renormalization or closure of their product/ratio. In particular, the metric dependence of:

- both sphere domains;
- both hypersurface measures;
- the centre-separation constraint;
- the pairwise geodesic-distance kernel;
- inverse sphere-volume normalization

creates operator mixing and nonlinear composite structure not computed in the frozen stack.

`INGREDIENTS_CLOSURE_CONTROL`: **TRIGGERS**.
`OPERATOR_MIXING_ERASURE_CONTROL`: **TRIGGERS**.

## F. Flow toward quantum expectation values

**PASS_FORMALISM / QRC-SPECIFIC OPEN.**

The 2022 relational-observable construction explicitly frames composite-operator FRG as evolving microscopic observable expressions toward their full quantum expectation values. It demonstrates the method for relational inverse metric and relational scalar curvature.

This establishes that an expectation-value route exists in principle within FRG. It does **not** establish the QRC-specific nonlocal operator or its closed truncation.

Therefore `BACKGROUND_EXPECTATION_SWAP_CONTROL` is narrowed but not removed: FRG has quantum-observable machinery beyond background evaluation, yet the same QRC expectation has not been derived.

## G. Relational coordinates

**PASS_CONTROL / NO RESCUE.**

Relational-observable sources can define physical coordinate frames using dynamical scalar fields. But replacing QRC geodesic spheres by fixed coordinate-radius spheres would change the target observable. The frozen stack does not make that substitution and ITER100 does not authorize it.

## H. Target fit

**PASS_CONTROL.**

No CDT QRC values, fitted radii, four-sphere curves or numerical target features are used to choose an FRG normalization or truncation.

## Predicate summary

- A geometric composite formalism: **PASS**
- B geodesic distance/length: **PASS_SCOPED**
- C geodesic ball/sphere measure: **PASS_SCOPED**
- D fixed-distance domain semantics: **PASS_SCOPED_INGREDIENT**
- E exact normalized double-sphere QRC operator: **NO / OPEN**
- F expectation-value RG machinery: **PASS_FORMALISM; QRC-SPECIFIC OPEN**
- G relational coordinate substitution avoided: **PASS_CONTROL**
- H target fit avoided: **PASS_CONTROL**

## Source classification

**`PASS_SCOPED_QRC_INGREDIENTS_EXIST_CLOSED_CONSTRUCTION_OPEN`**

The source stack is materially closer to QRC than ITER083B implied. FRG composite-operator work already contains the main geometric primitives and a formal expectation-value route. The missing object is precise and nontrivial: a closed renormalized construction of their QRC-specific nonlinear nonlocal composition.

This is not evidence that FRG cannot represent QRC. It is an explicit source-authority gap in the currently demonstrated truncation/operator basis.

## Highest-information successor

Before inventing a numerical cross-framework comparison, determine whether the QRC double-sphere functional admits a controlled expansion in already-renormalized geometric composite operators at small `delta`, and whether the leading nontrivial coefficient reduces to a relational Ricci-curvature insertion with source-controlled corrections.

Such a gate would connect ITER100 back to ITER083B without equating finite-radius QRC with local curvature. It must derive the expansion and its domain of validity before any CDT target values are used.

## Claim ceiling

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**. No explicit QRC expectation equality, unique RG trajectory, shared fixed point, full theory equivalence, `BRIDGE_DERIVED`, or new physics follows.