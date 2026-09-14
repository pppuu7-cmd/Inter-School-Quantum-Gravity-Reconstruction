# ITER083B source authority — CDT QRC ↔ FRG relational scalar typed map

Date: 2026-09-15
Gate: `ITER083B_CDT_QRC_FRG_RELATIONAL_SCALAR_TYPED_MAP_AUTHORITY`
Preregistration: `35265caa1c73fc0510152562578fc15fcbdb277d`
Production head: `03cd537a1a97349a0d5c68abbc7b7a9c8b6dabf9`
Authoritative run: `34901885759`
Aggregate artifact: `10370918460`, digest `sha256:889231d3fdbb1515f07274c6d76ec8d63233809671a69c048d40ebe714040b0b`

Frozen exact-PDF artifacts:
- `2006.06263`: artifact `10371471258`, digest `sha256:ea694353d3c2d2023e7db987233b38bcbecccaf8b0c84399e1ac96ffb900eed4`.
- `2112.02118`: artifact `10370966781`, digest `sha256:b7fd3fdccd621972720bdde50a8d9e5fc34054b97db189f638c8718b5c31fda8`.
- `2203.08003`: artifact `10371097422`, digest `sha256:d73549d8e57ae64beb50e767fcb0b07bd20446b4cd6aee3bfa1f41ead531fb4c`.
- `2604.05641`: artifact `10370997741`, digest `sha256:b6b2c06d4677f2dfc60115e16309dff3bdcebddf70ff107eff969414fb45f228`.

## Equation-level findings

### 1. CDT quantum Ricci curvature is a finite-radius, metric-space observable

`2006.06263` defines the average distance between two geodesic spheres of equal radius `delta`, whose centres are also separated by `delta`, and then defines quantum Ricci curvature through

`dbar(S_delta(p),S_delta(p')) / delta = c_q [1 - K_q(p,p')]`.

For CDT the continuum double integral is replaced by a double sum over vertices or dual vertices. Measurements are then averaged over point pairs and triangulations. After directional averaging, `K_q(delta)` is interpreted as an average scalar curvature at length scale `delta`.

The source explicitly stresses that `c_q` is nonuniversal on piecewise-flat spaces and that lattice anisotropy/discretization can shift it. The finite-radius observable is therefore not numerically identical to a local Ricci scalar without an additional limit/normalization statement.

### 2. FRG relational scalar curvature is a local composite operator tied to physical coordinates

`2112.02118` constructs four scalar physical coordinates `X^mu_hat` from dynamical fields and maps diffeomorphism-variant composite operators into relational observables. For the Ricci scalar the source gives the relational operator

`R_hat(x_hat) = R(X(x_hat))`,

with an equivalent delta-function integral representation. The observable is therefore local in the relational coordinate system and its RG flow is treated using the composite-operator formalism. The paper computes scaling dimensions at asymptotically safe fixed points; it does not define the observable by a finite geodesic-sphere average.

### 3. There is a genuine classical/local semantic relation, but not a frozen cross-framework map

The QRC source explicitly motivates `K_q(p,p')` as a generalization of continuum `Ric(v,v)` and describes its directionally averaged version as an average scalar curvature at scale `delta`. This is sufficient to retain a **local-limit candidate relation** to scalar curvature.

However, the frozen stack does not derive a map from CDT's finite-radius sphere-distance observable to the FRG relational scalar operator at specified physical coordinates. In particular it does not identify:

- the CDT sphere-centre sampling with the FRG scalar reference-field coordinates;
- the CDT directional/ensemble average with the FRG composite-operator expectation value;
- the nonuniversal QRC constant `c_q` with a relational-operator normalization;
- dual-link radius `delta` with an FRG cutoff scale, composite-operator resolution, or relational-coordinate distance;
- a finite-radius QRC value with a running FRG relational-curvature value.

`2203.08003` supplies scale-dependent self-consistent metrics and spectral-flow machinery, but this is a mean-field/background spectral construction, not the missing QRC↔relational-composite map. `2604.05641` confirms the continued importance of nonlocal, lattice-compatible CDT observables and does not supply the missing relational-coordinate identification.

## Predicate adjudication

- Exact QRC finite-radius definition: **PASS**.
- Exact FRG relational scalar composite-operator definition: **PASS**.
- Source-defined classical/local semantic relation to Ricci/scalar curvature: **PASS_SCOPED_CANDIDATE**.
- Finite-radius QRC ↔ local relational scalar conversion: **NOT ESTABLISHED**.
- Matching normalization: **OPEN** (`c_q` is nonuniversal on the CDT side).
- Matching averaging semantics: **OPEN / TYPE MISMATCH RETAINED**.
- Explicit scale relation `delta ↔ k` or equivalent: **NOT ESTABLISHED**.
- Separate FRG running/truncation dependence retained: **PASS_CONTROL**.
- Background-curvature substitution: **FORBIDDEN / NOT USED**.
- Target fitting: **FORBIDDEN / NOT USED**.

## Controls

- `FINITE_RADIUS_LOCAL_SCALAR_CONTROL`: passed. QRC is not silently replaced by `R(x)`.
- `ENSEMBLE_RELATIONAL_EXPECTATION_CONTROL`: passed. CDT ensemble averaging is kept distinct from FRG relational-coordinate/composite-operator semantics.
- `DE_SITTER_SHAPE_CONTROL`: passed. Agreement with a round four-sphere is not used to identify the operators.
- `SCALING_DIMENSION_VALUE_MAP_CONTROL`: passed. FRG scaling dimensions do not create a cross-framework value map.
- `DELTA_K_CONTROL`: passed. QRC radius and FRG regulator scale remain distinct.

## Source classification

**`PASS_SCOPED_LOCAL_LIMIT_CANDIDATE_NORMALIZATION_OPEN`**

The frozen stack contains a nontrivial common curvature target: QRC has a source-qualified continuum/local curvature interpretation, while FRG contains an exact relational scalar-curvature composite operator. But the finite-radius/local-composite conversion, reference-frame identification, averaging rule and scale normalization are not derived.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.
