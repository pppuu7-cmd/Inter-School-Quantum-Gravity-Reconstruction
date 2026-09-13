# Preregistration — ITER014 RC006 q-CG constructibility and residual phase-gauge audit

Frozen before production on 2026-09-13.

## Trigger
Iter013 classified `RC006_GENERIC_QCG_EXTERNAL_BOOK_AUTHORITY_REQUIRED`: the open source panel delegates the standard generic q-CG coefficient formula/convention to an external authority. Iter012 may not be retried yet.

## Objective
Determine, without importing an external coefficient formula or fitting phases, whether the source-stated U_q(su(2)) representation data are sufficient to construct generic q-CG coefficients numerically up to a residual trivalent phase gauge, and whether the Eq.(27)-relevant graphical contractions are source-defined to be invariant under that gauge.

Immutable source panel: arXiv:1609.02429v2, arXiv:1312.0905v2, arXiv:1506.04749v3. Record source SHA256 values.

## Independent lanes
A. `rep-action`: require explicit source formulas for J_z and J_± action on |j,m>, q-number convention, finite-k representation range, and coproduct. Missing ladder-action data => BLOCKED.
B. `constructibility`: require decomposition equation plus orthogonality/completeness sufficient to define a finite-dimensional change-of-basis problem once representation matrices are known. No external closed-form q-CG formula may be imported.
C. `phase-gauge`: audit source graphical identities and Eq.(27)/Appendix-F contractions for whether each internal trivalent coefficient occurs in conjugate/dual pairings or otherwise has a source-stated phase-cancellation identity. Ambiguity => BLOCKED; do not assume cancellation.
D. `cap-cup`: audit whether cap/cup and q/qbar duality source identities constrain the residual phase/normalization beyond arbitrary Euclidean norm conventions.

## Frozen classification
- `RC006_QCG_CONSTRUCTIBLE_FROM_OPEN_SOURCE_ALGEBRA_UP_TO_PHASE_GAUGE_SCOPED` only if A+B pass and C+D establish source-qualified residual-gauge handling.
- `RC006_QCG_CONSTRUCTIBILITY_BLOCKED_MISSING_REPRESENTATION_ACTION` if the source panel lacks explicit representation-action data required for the numerical eigen/decomposition problem.
- `RC006_QCG_PHASE_GAUGE_BLOCKED_SOURCE_IDENTITY_INSUFFICIENT` if construction is otherwise possible but Eq.(27)-relevant phase cancellation is not source-qualified.
- `INFRASTRUCTURE_SOURCE_EXTRACTION_FAIL` for fetch/parser failures only.

## Scope locks
No bridge credit. No Eq.(29)/Lambda. No preferred alpha. No Iter012 retry unless this gate returns the first PASS classification, and even then a separate prospectively preregistered implementation-validation gate is required before any Eq.(27) contraction. Candidate theory remains UNFORMED.