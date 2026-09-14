# ITER070 audit — FRG / CDT scale-time type discrimination

Date: 2026-09-14
Gate: `ITER070_FRG_CDT_SCALE_TIME_TYPE_DISCRIMINATION`
Preregistration commit: `13dc381f81cb7f2f14e3dac7a099448d4d576ae2`

## Frozen objects compared

- FRG `C_scale_flow`, terminally qualified by ITER069.
- CDT `C_seq`, terminally qualified by ITER067.

No reduced CDT transfer object and no newly invented finite FRG transport are substituted for the frozen objects.

## Candidate invariant audit

### 1. Parameter-ordered evolution

**Retained weak commonality.**

Both packages are indexed by an ordered parameter: FRG by cutoff/RG scale and CDT by discrete proper-time slices. This gives an abstract ordered-family/evolution schema.

It is not non-forgetful. The parameter semantics differ: the FRG parameter controls regulated coarse graining in theory space, while the CDT parameter is part of the source-defined temporal slicing of the triangulated history. The frozen stack supplies no typed map between them.

Classification: `COMMON_ORDERED_PARAMETER_KERNEL_ONLY`.

### 2. Composable finite transport

**FAIL as a common invariant.**

CDT source authority includes an exact regulated finite semigroup/gluing law for full spatial-triangulation states. ITER069 explicitly records that the frozen FRG stack does not establish an exact finite source-defined physical `k1 -> k2` composition law of the required type.

Constructing a mathematical finite flow from the differential RG equation would be a new derived object and would still act in theory space rather than on CDT states.

Classification: `ASYMMETRIC_AUTHORITY / NO_TYPED_COMMON_FINITE_TRANSPORT`.

### 3. Elimination/coarse-graining of degrees of freedom

**FAIL as a non-forgetful physical invariant.**

FRG coarse graining is implemented through a regulator and scale-dependent functional integration/effective action. CDT semigroup composition sums over intermediate spatial triangulation states when gluing temporal slabs. The latter is state-sum composition, not source-qualified momentum/mode coarse graining.

Treating both as generic `sum/integrate over internal degrees of freedom` retains only a forgetful algebraic kernel and drops the physical role of the summed/integrated variables.

Classification: `FORGETFUL_SUM_INTEGRATE_KERNEL_ONLY`.

### 4. Generator relation

**FAIL.**

FRG's local generator is the functional beta/Wetterich flow on effective actions/couplings with regulator dependence. CDT's qualified Hamiltonian package is derived from the two-step transfer object `T_N^2` in the regulated state-space construction. Their domains, parameter meanings and physical interpretations differ.

No frozen source defines a typed map carrying the Wetterich generator to the CDT transfer/Hamiltonian generator while preserving semantics.

Classification: `NO_TYPED_GENERATOR_INTERTWINER`.

### 5. Observable/state transport

**FAIL.**

CDT `C_seq` transports amplitudes between full spatial triangulation states and composes through intermediate states. `C_scale_flow` transports/evolves effective actions and couplings with scale; ITER069 deliberately did not promote this to physical spacetime-state transport.

Classification: `DOMAIN_CODOMAIN_MISMATCH`.

### 6. Normalization/measure compatibility

**FAIL.**

CDT requires automorphism factors `C(g)`/`C(T)` and action-weighted state sums. FRG requires a regulator kernel `R_k` plus background/gauge/ghost structure. The frozen authority stack contains no map identifying these structures or deriving one from the other.

Classification: `MEASURE_REGULATOR_TYPE_MISMATCH`.

## Control outcomes

- `RG_TIME_PROPER_TIME_SWAP_CONTROL`: **triggered correctly**; identification is unsupported.
- `REGULATOR_ERASURE_CONTROL`: **triggered correctly**; commonality obtained by dropping `R_k` is forgetful.
- `FULL_REDUCED_STATE_SWAP_CONTROL`: **triggered correctly**; reduced CDT volume dynamics is not substituted for `T_full`.
- `FIXED_POINT_REFINEMENT_SWAP_CONTROL`: **triggered correctly**; FRG fixed points are not CDT refinement objects.
- `OBSERVABLE_ERASURE_CONTROL`: **triggered correctly**; abstract map/evolution language loses physical semantics.
- `MEASURE_REGULATOR_SWAP_CONTROL`: **triggered correctly**; `weight` is not a typed equivalence.
- `DIFFERENTIAL_FINITE_SWAP_CONTROL`: **triggered correctly**; FRG differential flow is not promoted to CDT's exact finite semigroup law.

## Researcher classification

The strong PASS criterion is not met.

**`FAIL_SCOPED / FRG_CDT_TYPE_EQUIVALENCE_REJECTED`**

Retained positive sub-result:

**`COMMON_ORDERED_EVOLUTION_KERNEL_ONLY`**.

The common kernel is exact but too weak for bridge credit: each object belongs to an ordered family and admits a notion of change with its parameter. Once domain/codomain, parameter meaning, dynamics, measure/regulator structure, gauge/quotient data and observables are restored, the apparent equivalence splits.

## Consequence for H0

A single universal `evolution/composition` operation is not supported by this pair. The typed multi-operation H0 survives only as a search for explicit morphisms between distinct operation classes, not as identification of their parameters or generators.

No bridge credit is awarded.