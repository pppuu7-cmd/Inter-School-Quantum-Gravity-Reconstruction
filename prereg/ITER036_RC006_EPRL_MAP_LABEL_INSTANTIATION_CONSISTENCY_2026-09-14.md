# ITER036 preregistration — RC006 bounded EPRL-map label instantiation/consistency

Date: 2026-09-14
Status: `PREREGISTERED_NOT_EXECUTED`.

## Authorization basis

ITER035 terminalized `PASS — RC006_INDEXED_SIMPLICITY_MAP_SOURCE_AUTHORITY_PASS`. The exact source explicitly supplies the EPRL map `(j^+,j^-)=((1+gamma)l/2,(1-gamma)l/2)`, declares indexed inheritance `l_i -> (j_i^+,j_i^-)`, and supplies finite-level cutoff/admissibility authority.

ITER036 is a bounded source-consistency gate. It does **not** evaluate the complete Eq.(27) sums and does not import Eq.(29)/Lambda.

## Frozen source-selection rule

No gamma is chosen by numerical performance. The only admissible non-trivial `(k,gamma)` values are those explicitly listed by the byte-pinned arXiv:1609.02429v2 source in the finite-q EPRL-map discussion. The implementation must mechanically extract that source list. If it cannot unambiguously extract the list, the gate is BLOCKED rather than repaired by manually inserting preferred values after viewing output.

For every extracted `(k,gamma)` case, admissible `l` values are generated mechanically from the source rules:
- integer representations only (as stated for this work);
- `0 <= l <= j_max`, with `j_max=k/2` for even k and the source odd-k integer cutoff where applicable;
- `j^+=(1+gamma)l/2` and `j^-=(1-gamma)l/2` must be non-negative integers and each `<=j_max`.

The resulting cases are sorted lexicographically by `(k,gamma,l)`. For transport, even-indexed entries in that sorted source-derived list are the primary panel and odd-indexed entries are held out. This split is frozen before execution and cannot be changed based on residuals.

## Four independent lanes (`fail-fast:false`)

### Lane A — source-list extraction
PASS requires exact archive hash, explicit EPRL-map equation/context, and at least two non-trivial source-listed `(k,gamma)` cases mechanically extracted outside Eq.(29)/Lambda. Record source contexts and rational gamma exactly. Ambiguous/unparseable list => BLOCKED_SOURCE_CASE_LIST.

### Lane B — mapped-label integrality/cutoff consistency
For every mechanically generated primary and held-out `(k,gamma,l)` entry, compute `j^+,j^-` exactly as rationals. PASS requires both to be integers in the source-allowed finite range and exact inverse consistency `j^+ + j^- = l` and `(j^+ - j^-)/(j^+ + j^-)=gamma` for nonzero `l`. No floating fit/tolerance is used for these algebraic identities.

### Lane C — indexed Eq.(27) exponent instantiation
Deterministically pair consecutive mapped entries **within the same `(k,gamma)` case**. For each pair `(l_1,l_2)`, instantiate the indexed labels `j_1^±,j_2^±` in the two source q-exponent expressions from ITER033. Enumerate internal integer `j` over the source-admissible SU(2)_k range that satisfies both relevant triangle/root-of-unity coupling rules for the two coupled pairs. PASS requires every tested source-derived pair to yield a finite, non-empty admissible internal-j panel and exact rational exponents. Cases with fewer than two mapped nonzero l values are recorded as structurally insufficient and do not count as tested; PASS requires at least one primary and one held-out tested pair. If the source list cannot provide that prospectively, classify BLOCKED_PANEL_SUPPORT rather than manufacture cases.

### Lane D — frozen null controls
On the first lexicographically available tested case, require detection of all 3/3 predetermined wrong maps:
1. swap the `+` and `-` formulas while retaining positive gamma;
2. use `j^+=(1+gamma)l` and `j^-=(1-gamma)l` (missing factor 1/2);
3. admit a mapped label above the source cutoff by extending `l` to the first value producing `j^+>j_max`.
A null is detected by failure of exact map identity, gamma identity, integrality, or cutoff. All 3/3 are required because these are algebraic/source controls.

## Aggregate classification

### PASS — `RC006_EPRL_MAP_LABEL_INSTANTIATION_CONSISTENCY_PASS`
A-D all PASS. This authorizes only a separately preregistered bounded numerical Eq.(27) scalar/summation-lift gate using the exact source-listed `(k,gamma)` panel, the frozen primary/held-out split, and already validated component primitives.

### BLOCKED
Source-list extraction ambiguity, insufficient source-derived primary/held-out pair support, or missing admissible internal-j panels is BLOCKED, not scientific FAIL.

### SCIENTIFIC FAIL
Only if source authority and panels are valid but a frozen exact map/domain identity or frozen null criterion fails.

### INFRASTRUCTURE FAIL
Source/hash/parser/runtime/artifact failure before substantive evaluation.

## Claim locks

Always false: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.

Candidate theory remains `UNFORMED / 0%`; overall roadmap readiness remains 49%.