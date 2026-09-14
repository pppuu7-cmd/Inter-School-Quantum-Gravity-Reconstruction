# ITER032 preregistration — RC006 bounded two-factor Eq.(27) network assembly

Date: 2026-09-14

Status: `PREREGISTERED_NOT_EXECUTED`.

## Authorization basis

ITER031 terminalized `PASS — RC006_EQ27_BOUNDED_COMPONENT_CONTRACTION_CORRECTED_STAGE_S_PASS` and prospectively authorized exactly one separately preregistered two-factor network-assembly successor. ITER030 had already established the corrected source inventory of exactly two bracketed graphical factors and two source sum structures.

ITER032 is deliberately **below** a full Eq.(27) amplitude/TNR reconstruction. It asks whether the two source factors can be kept distinct, instantiated from the already validated bounded component primitives, and assembled factorwise without retuning, while preserving primary-to-held-out transport. It does not import Eq.(29), Lambda, one-step TNR, or any candidate-theory object.

## Frozen source and numerical conventions

Primary source: arXiv:1609.02429v2, exact source/archive authority already frozen by ITER030.

Primary levels: `k={6,10,12}`.
Held-out levels: `k={7,9,11}`.
Frozen base pair panel: `(1,1),(2,1),(2,2),(4,2)` in twice-spin notation, with admissible output channels generated mechanically exactly as in ITER031.
`alpha=0` remains fixed.

No phase, sign, tensor permutation, R/R^-1 orientation, qbar orientation, normalization, channel selection, pair ordering, or held-out parameter may be fitted after observing outputs.

For each level k, admissible component rows are ordered lexicographically by `(a,b,c)`. Two-factor test pairs are generated prospectively and deterministically as adjacent rows `(row_i,row_{i+1})` with cyclic wraparound. This rule is fixed before execution and applies identically to primary and held-out levels. No result-dependent pair selection is allowed.

The single-factor bounded object is the already validated duality contraction from ITER031:
`M(a,b,c;k) = F(a,b,c;k) @ D(a,b,c;k)`
with frozen target
`T(a,b,c;k) = (-1)^((a+b-c)/2) / qdim(c,k) * I_(c+1)`.

The ITER032 factorized two-factor bounded assembly is the tensor product
`N12 = M(row1;k) ⊗ M(row2;k)`
with preregistered target
`T12 = T(row1;k) ⊗ T(row2;k)`.

This tensor-product object is only a bounded factorwise assembly check justified if Lane A confirms that the byte-pinned Eq.(27) source presents the two graph factors as two distinct bracketed multiplicative factors with separate internal sums. It is not claimed to be the complete Eq.(27) amplitude.

Frozen numerical threshold for the two-factor assembly residual: `<5e-8`, reusing the ITER031 bounded threshold rather than choosing a new post-result value.

## Four independent lanes

All run with `fail-fast:false`.

### Lane A — source factorization authority
Mechanically re-read the byte-pinned Eq.(27) source using the frozen archive/display hashes from ITER030. PASS requires:
1. exactly two bracketed TikZ graphical factors;
2. exactly two source sum structures;
3. the two bracketed factors occur as distinct multiplicative factors in the Eq.(27) display rather than one nested/collapsed graph object;
4. ITER030 and ITER031 terminal PASS result notes are present;
5. no Eq.(29)/Lambda dependency is used.

If the exact source does not mechanically establish this limited factorization syntax, classification is `BLOCKED_TWO_FACTOR_SOURCE_FACTORIZATION`, not scientific FAIL.

### Lane B — independent factor reconstruction
For every deterministic two-factor pair at primary and held-out levels, construct both `M1,M2` independently from the immutable ITER031 primitives and compare each against its own `T1,T2` before any assembly.

PASS requires all finite values and max single-factor residual `<5e-8` for both factor positions across primary and held-out levels. No factor may be copied from the other factor merely to force equality.

### Lane C — factorized two-factor assembly
For every frozen adjacent-row pair at primary and held-out levels, construct `N12=kron(M1,M2)` and `T12=kron(T1,T2)` using the same implementation and no retuning.

PASS requires all finite values and maximum two-factor residual `<5e-8` across primary and held-out levels. The held-out calculation must use exactly the same rule and parameters as primary.

### Lane D — frozen adversarial/null controls
Use a fixed test pair chosen mechanically as the first adjacent pair at `k=12`. Test three wrong constructions:
1. flip the sign of the second target factor;
2. replace the second target quantum dimension by the first factor's quantum dimension whenever the two channels differ; if the first pair has equal channels, advance mechanically to the first adjacent pair with unequal output channel and record that deterministic choice;
3. collapse the second factor to an identity matrix with matching dimension instead of its source-qualified scalar target.

A wrong construction is detected when its residual is `>1e-6` or non-finite/structurally invalid. PASS requires at least 2/3 detected. This criterion is frozen before execution.

## Aggregate classes

### PASS — `RC006_EQ27_TWO_FACTOR_BOUNDED_NETWORK_ASSEMBLY_PASS`
Only if A-D all PASS. It demonstrates a source-authorized **bounded factorized two-factor composition** with non-retuned held-out transport. It still gives zero bridge/TNR/candidate-theory credit.

A PASS may authorize only a separately preregistered next gate that asks whether the remaining source scalar/summation structure can be lifted from bounded factorwise composition toward a fuller Eq.(27) amplitude object. It does not itself authorize Eq.(29)/Lambda or one-step TNR.

### SCIENTIFIC FAIL — `RC006_EQ27_TWO_FACTOR_BOUNDED_NETWORK_ASSEMBLY_FAIL`
Only if source factorization authority and all prerequisites are valid but a frozen single-factor/two-factor numerical residual exceeds threshold or the preregistered null controls fail discrimination. Thresholds and pair rules may not be weakened after inspection.

### BLOCKED
Missing source factorization authority or missing validated prerequisite is BLOCKED, not scientific FAIL.

### INFRASTRUCTURE FAIL
Import/runtime/artifact/transport/source-download failure before substantive evaluation is `NUMERICAL_OR_INFRASTRUCTURE_FAIL_PRE_SCIENCE`.

## Claim locks

Always false during ITER032: `iter012_retry_authorized`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`, `full_eq27_amplitude_derived`.

Candidate theory remains `UNFORMED / 0%`. Overall programme readiness remains 49% unless and until a roadmap rubric/gate beyond this bounded composition layer is actually closed.
