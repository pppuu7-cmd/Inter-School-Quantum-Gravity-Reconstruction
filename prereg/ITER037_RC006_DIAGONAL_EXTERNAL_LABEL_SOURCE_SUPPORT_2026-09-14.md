# ITER037 preregistration — RC006 diagonal external-label source support

Date: 2026-09-14
Status: `PREREGISTERED_NOT_EXECUTED`.

## Authorization basis

ITER036 terminalized `BLOCKED — RC006_EPRL_MAP_LABEL_INSTANTIATION_CONSISTENCY_BLOCKED` solely because the prospectively frozen distinct/nonzero within-case pair construction yielded one tested pair and no primary tested pair. ITER036 remains unchanged.

ITER037 asks a new independent source/mathematical question: whether Eq.(27)'s two external EPRL labels `l_1,l_2` are independently admissible representation labels such that the diagonal assignment `l_1=l_2=l` is within the source-defined domain. This is not inferred from numerical success and does not change ITER036's frozen panel.

## Frozen source panel

Use only the three non-trivial source-listed cases already extracted in ITER036:
- `k=6, gamma=1/3, l=3 -> (2,1)`;
- `k=10, gamma=3/5, l=5 -> (4,1)`;
- `k=12, gamma=1/3, l=3 -> (2,1)` and separately source-listed `l=6 -> (4,2)`.

For the diagonal-support gate, each source-listed nonzero `l` is tested as `(l_1,l_2)=(l,l)`; no new l or gamma is introduced. The source cases are ordered lexicographically by `(k,gamma,l)`. Even-indexed diagonal cases are primary and odd-indexed cases held-out. This split is frozen before execution.

## Four independent lanes (`fail-fast:false`)

### Lane A — external-label scope authority
Inspect the exact byte-pinned source for the definition/context of Eq.(27) and its surrounding map. PASS requires explicit source evidence that `l_1` and `l_2` are two independently labelled external/input SU(2) representations (or two instances `l_i` of the same allowed representation domain), rather than a source constraint that they must be distinct. Mere absence of `l_1 != l_2` is not sufficient: there must be positive general/indexed domain language or a formula defined for generic `l_i`.

### Lane B — diagonal admissibility from source rules
For every source-listed nonzero mapped `l`, instantiate `(l_1,l_2)=(l,l)` and apply only source-qualified finite-level representation and coupling/admissibility conditions. PASS requires the diagonal assignment itself to satisfy every applicable external representation-domain rule exactly. No Eq.(29)/Lambda and no output fitting.

### Lane C — diagonal Eq.(27) internal-j support
For every frozen diagonal case, map both external labels with the source EPRL map and compute the common integer internal-j domain required by the two Eq.(27) q-exponent couplings. PASS requires a finite non-empty internal-j panel for every tested diagonal case, plus at least one primary and one held-out case. Record exact rational exponents. This is domain/support only, not amplitude summation.

### Lane D — frozen nulls
Require 3/3 detection on the first lexicographic source case:
1. use an unmapped nonzero l not allowed by the source EPRL integrality rule;
2. use the first diagonal l above the finite-k cutoff;
3. replace one leg's mapped `(j^+,j^-)` by the swapped pair while retaining positive gamma.
Detected means exact map/domain/cutoff identity fails.

## Aggregate classes

`RC006_DIAGONAL_EXTERNAL_LABEL_SOURCE_SUPPORT_PASS`: A-D all PASS. This does not alter ITER036. It authorizes a new separately preregistered panel-construction/label-consistency gate using source-authorized diagonal cases before any Eq.(27) numerical summation.

`RC006_DIAGONAL_EXTERNAL_LABEL_SOURCE_SUPPORT_BLOCKED`: source does not positively authorize generic/indexed independent external labels or a diagonal case lacks source-domain support. This is BLOCKED, not scientific failure.

`RC006_DIAGONAL_EXTERNAL_LABEL_SOURCE_SUPPORT_FAIL`: only if source authority is valid but a frozen exact domain/null predicate fails.

Infrastructure/parser/hash failures are pre-science.

## Claim locks

Always false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.

Candidate theory remains `UNFORMED / 0%`; overall roadmap readiness remains 49%.