# ITER070 preregistration — FRG / CDT scale-time type discrimination

Date: 2026-09-14
Gate: `ITER070_FRG_CDT_SCALE_TIME_TYPE_DISCRIMINATION`

## Frozen question

Can the source-qualified FRG operation `C_scale_flow` and the source-qualified CDT operation `C_seq` be related by a non-forgetful typed invariant or explicit embedding that preserves or derives their mandatory physical structure, rather than identifying RG scale evolution with temporal composition by analogy?

## Frozen source/authority stack

### FRG / RC003

- arXiv:2302.14152 — Saueressig, FRG in quantum gravity.
- arXiv:2606.21522 — Eichhorn, asymptotically safe quantum gravity review.
- arXiv:2110.09566 — Laporte et al., scalar-tensor asymptotic safety.
- `sources/ITER069_RC003_FRG_SCALE_OPERATION_AUTHORITY_2026-09-14.md`.
- `results/ITER069_RC003_FRG_SCALE_COMPOSITION_AUTHORITY_2026-09-14.md`.

### CDT / RC002

- the frozen primary CDT authority stack used by ITER067;
- `sources/ITER067_RC002_FULL_CDT_TRANSFER_MATRIX_AUTHORITY_2026-09-14.md`;
- `results/ITER067_RC002_FULL_CDT_TRANSFER_MATRIX_COMPOSITION_MEASURE_AUTHORITY_2026-09-14.md`.

No new source may be used to rescue a failing predicate after inspection without a new preregistration.

## Frozen typed objects

### `C_scale_flow`

Domain/codomain: scale-indexed effective actions/functionals/couplings in theory space.

Mandatory structure:

- Wetterich differential flow;
- regulator `R_k` / coarse-graining kernel;
- background/gauge/ghost structure in gravity;
- trajectory/fixed-point semantics in theory space;
- no source-qualified identification of RG time with physical proper time;
- no exact finite source-defined physical composition law established by ITER069.

### `C_seq`

Domain/codomain: regulated CDT spatial-triangulation states on discrete proper-time slices.

Mandatory structure:

- full transfer amplitude / matrix;
- action-weighted sum over sandwich triangulations;
- automorphism weights and intermediate-state factor;
- exact regulated temporal semigroup/gluing;
- preferred discrete proper-time semantics;
- qualified `T_N^2` positivity/Hamiltonian package in the established scope.

## Candidate invariants to test prospectively

A candidate common structure may count only if it is non-forgetful with respect to the mandatory structure above.

1. **Parameter-ordered evolution:** both objects form ordered families indexed by a parameter.
2. **Composable finite transport:** existence of source-qualified finite maps with an associative/semigroup law.
3. **Elimination/coarse-graining of degrees of freedom:** preservation of an explicit meaning of what is integrated/summed out.
4. **Generator relation:** whether the differential FRG generator and the CDT transfer/Hamiltonian object can be placed under one typed generator/evolution schema without changing semantics.
5. **Observable transport:** whether observables/states are transported under a source-defined map in both realizations with compatible typing.
6. **Normalization/measure compatibility:** whether regulator structure and state-sum automorphism measure are related by an explicit map rather than merely both being auxiliary weights.

## Strong PASS criterion

`PASS_SCOPED_TYPED_COMMON_INVARIANT` requires at least one candidate invariant for which the frozen stack supplies explicit typed maps preserving or deriving:

- domain/codomain;
- parameter meaning;
- dynamics/generator meaning;
- measure/regulator structure;
- gauge/quotient structure;
- observable semantics;
- physical time/scale semantics.

Abstract embedding into sets, vector spaces, categories, ordered flows or generic semigroups does not count if mandatory physical structure is forgotten.

## FAIL criterion

`FAIL_SCOPED_FRG_CDT_TYPE_EQUIVALENCE_REJECTED` if all apparent common structures require at least one forbidden substitution/erasure below and only a forgetful algebraic/order-theoretic kernel survives.

## BLOCKED criterion

`BLOCKED_SOURCE_AUTHORITY` only if the already-qualified ITER067/ITER069 objects are insufficient to adjudicate the frozen candidate invariants. A negative answer is not a source block if the mismatch itself is source-qualified.

## Frozen failure controls

- `RG_TIME_PROPER_TIME_SWAP_CONTROL`: identifying `ln(k/k0)` or cutoff scale with CDT proper time must fail unless explicitly derived.
- `REGULATOR_ERASURE_CONTROL`: removing `R_k`/scheme/background dependence to force commonality must fail.
- `FULL_REDUCED_STATE_SWAP_CONTROL`: replacing the full CDT triangulation-state transfer object by its reduced volume effective object must fail.
- `FIXED_POINT_REFINEMENT_SWAP_CONTROL`: an FRG fixed point cannot be treated as a CDT refinement/fixed geometry without a typed derivation.
- `OBSERVABLE_ERASURE_CONTROL`: a comparison that drops observable meaning cannot pass.
- `MEASURE_REGULATOR_SWAP_CONTROL`: CDT automorphism/state-sum weights and FRG regulator kernels cannot be identified by the generic word `weight`.
- `DIFFERENTIAL_FINITE_SWAP_CONTROL`: differential FRG flow cannot be promoted to the exact finite CDT semigroup law without source authority.

## Claim ceiling

Even a PASS may establish only a typed common-structure candidate. It cannot establish `BRIDGE_DERIVED`, physical equivalence of FRG and CDT, a universal common parent, a complete QG theory, or new physics.

A FAIL constrains this route only; it is not a no-go theorem for all deeper common parents.

Thresholds, candidate invariants and controls are frozen before the comparison audit.