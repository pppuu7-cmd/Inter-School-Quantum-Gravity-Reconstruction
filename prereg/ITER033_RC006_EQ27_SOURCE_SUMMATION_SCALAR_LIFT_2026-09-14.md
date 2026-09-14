# ITER033 preregistration — RC006 Eq.(27) source summation/scalar lift

Date: 2026-09-14
Status: `PREREGISTERED_NOT_EXECUTED`.

## Authorization basis

ITER032 terminalized `PASS — RC006_EQ27_TWO_FACTOR_BOUNDED_NETWORK_ASSEMBLY_PASS` and authorizes one separately preregistered gate toward the remaining explicit Eq.(27) source summation/scalar structure. ITER033 remains strictly below Eq.(29)/Lambda and one-step TNR.

## Frozen source

The source is the exact arXiv:1609.02429v2 Eq.(27) display already byte-pinned by ITER030/ITER032:
- archive SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`
- Eq.(27) display SHA256 `88d2f7be9489980a763dd66b5c4900473c79900ccf72790095ae1675e9733b2d`.

No formula from Eq.(29), Lambda, or a later fitted convention may be imported.

## Scientific question

Can Eq.(27), using its exact source text, be mechanically segmented into (i) the already-qualified two multiplicative bracketed graph factors, (ii) the two internal summation binders belonging one-to-one to those factors, and (iii) any remaining scalar/prefactor text outside the graph brackets, without ambiguity or post-result interpretation?

A PASS is a source-structure authorization only. It does not claim the scalar/summations have yet been numerically evaluated as a full amplitude.

## Frozen lanes (`fail-fast:false`)

### Lane A — exact display segmentation
PASS requires exact source hashes, exactly two non-overlapping bracketed graph factors, exactly two sum tokens, and an explicit multiplicative separator between the two factors. The display must be segmented deterministically into `prefix`, `factor1`, `separator`, `factor2`, `suffix` by source positions only.

### Lane B — summation binding
For each bracketed factor, PASS requires exactly one `\\sum` token inside that factor and zero sum tokens in the inter-factor separator. Each sum must have a syntactically non-empty binder/range immediately following `\\sum` before the factor's TikZ graph begins. The two binders are recorded verbatim; no meaning is inferred if syntax is absent.

### Lane C — external scalar/prefactor inventory
Remove the two factor spans from the exact display while retaining prefix/separator/suffix. PASS requires that all remaining non-layout mathematical source outside the factors can be recorded verbatim and that no TikZ environment or additional `\\sum` remains outside the two qualified factors. This lane is an inventory/uniqueness gate; it does not require a guessed numerical scalar formula.

### Lane D — frozen syntax nulls
Apply three predetermined text mutations to a copy of the exact display and require the same parser to reject at least 3/3:
1. replace the source `\\times` separator between factors with `+`;
2. delete the first factor's `\\sum` token;
3. append a third duplicate bracketed factor after factor2.
A null is detected when Lane-A/B structural predicates no longer all hold. All three must be detected because these are purely syntactic controls.

## Aggregate classes

### PASS — `RC006_EQ27_SOURCE_SUMMATION_SCALAR_STRUCTURE_PASS`
Only if A-D all PASS. This authorizes a separately preregistered bounded numerical lift of the *explicitly source-qualified* scalar/summation structure around the ITER032 factorized bounded object. It does not authorize Eq.(29)/Lambda or TNR.

### BLOCKED — `RC006_EQ27_SOURCE_SUMMATION_SCALAR_STRUCTURE_BLOCKED`
If the exact source cannot uniquely bind the two sums or isolate remaining scalar/prefactor text under these frozen syntactic rules. Do not infer missing structure by numerical fitting.

### INFRASTRUCTURE FAIL
Source fetch/hash/parser/runtime/artifact failure before substantive predicates is `NUMERICAL_OR_INFRASTRUCTURE_FAIL_PRE_SCIENCE`.

## Claim locks

Always false throughout ITER033: `full_eq27_amplitude_derived`, `eq29_amplitude_authorized`, `one_step_tnr_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `UNIVERSAL_BRIDGE_FOUND`.

Candidate theory remains `UNFORMED / 0%`; overall roadmap readiness remains 49% unless a separate roadmap rubric is actually closed.
