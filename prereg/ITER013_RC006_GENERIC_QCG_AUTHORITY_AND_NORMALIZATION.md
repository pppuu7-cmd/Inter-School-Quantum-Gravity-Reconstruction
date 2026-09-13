# Preregistration — ITER013 RC006 generic q-CG authority and cap/cup normalization

Frozen before production on 2026-09-13.

## Trigger
Iter012 run `34773202384` classified `RC006_EQ27_ONE_STEP_TNR_RECONSTRUCTION_BLOCKED_SOURCE_IMPLEMENTATION_GAP`. Lane B found that a generic source-faithful q-Clebsch–Gordan numerical implementation is absent; lane C therefore did not execute the Eq.(27) contraction. No classical-CG substitution, fitted phase, fitted normalization, or post-hoc rescaling is allowed.

## Objective
Resolve the blocker without retuning Iter012 by auditing the exact published authority chain for the generic SU(2)_k q-CG coefficients and, independently, the special cap/cup normalization identity used as a control.

Immutable versioned sources:
- Dittrich et al., arXiv:1609.02429v2.
- Dittrich, Martin-Benito, Steinhaus, arXiv:1312.0905v2.
- Steinhaus, arXiv:1506.04749v3.

The versioned arXiv source payload SHA256 values must be recorded by the workflow at execution.

## Independent lanes
A. `main-authority`: inspect 1609.02429v2 Appendix A/B for coproduct, q-CG decomposition, admissibility, completeness/orthogonality, cap/cup, q/qbar duality, modified-normalization footnote, and the exact external authority to which the standard generic q-CG coefficients are delegated.
B. `prior-1312`: inspect 1312.0905v2 for an explicit generic q-CG numerical formula/algorithm, or a precise delegation if the formula is not supplied.
C. `prior-1506`: independently inspect 1506.04749v3 for the same.
D. `cap-cup`: inspect the exact source representation of the cap and cup and the source-stated concatenation identity. In particular determine whether the diagrammatic cap is the raw modified q-CG coefficient or includes an explicit quantum-dimension factor. Do not use an Euclidean absolute-square normalization unless the source explicitly states it.

## Frozen outputs
- `RC006_GENERIC_QCG_EXPLICIT_OPEN_SOURCE_AUTHORITY_COMPLETE_SCOPED`: an exact, executable generic q-CG formula/algorithm including normalization/phase convention is present in the audited open primary sources.
- `RC006_GENERIC_QCG_EXTERNAL_BOOK_AUTHORITY_REQUIRED`: the audited open primary sources define the objects/identities but delegate the generic coefficient convention/formula to an external non-audited authority, with no source-complete executable formula found.
- `RC006_GENERIC_QCG_AUTHORITY_PARTIAL`: evidence is insufficient or internally ambiguous.
- `INFRASTRUCTURE_SOURCE_EXTRACTION_FAIL`: source fetch/unpack/parser failure only.

The cap/cup lane receives a separate sub-classification: `CAP_CUP_NORMALIZATION_IDENTITY_SOURCE_QUALIFIED`, `CAP_CUP_NORMALIZATION_AMBIGUOUS`, or `INFRASTRUCTURE_SOURCE_EXTRACTION_FAIL`.

## Scope locks
Even a complete q-CG authority result authorizes only a separate prospectively preregistered q-CG implementation/validation gate and then a fresh Iter012-style one-step contraction. It gives zero bridge credit, does not authorize Eq.(29)/Lambda, does not establish a preferred alpha, does not establish new physics, and does not authorize candidate-theory construction.
