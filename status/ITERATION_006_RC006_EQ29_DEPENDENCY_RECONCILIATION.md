# ITERATION_006 RC006 Eq.(29) immutable dependency reconciliation — preregistration

Date: 2026-09-12  
Status: PREREGISTERED BEFORE IMPLEMENTATION

## Frozen inputs

This gate does not rerun or weaken any earlier gate. It consumes only immutable terminal summaries from two already completed prospective audits:

1. Eq.(29) source dependency audit, run `34718554940`, summary artifact `10305491683`, digest `sha256:ca82d129681a540d7b0daa618b43b831957e2001a527e1556ea0852c8387ada8`, terminal `EQ29_SOURCE_DEPENDENCIES_PARTIAL` with:
   - `SOURCE_LABEL_GEOMETRY_QUALIFIED`;
   - `SOURCE_PATH_INCIDENCE_QUALIFIED`;
   - `SOURCE_R_PLACEMENT_NOT_MACHINE_QUALIFIED`.
2. Exact arc-aware immutable-block geometry, run `34719362365`, summary artifact `10305333911`, digest `sha256:3ec0ce7ab19a34243f2309e9b75cdcff20f8ba8ad1c034fc233702bef5e8c667`, terminal `EQ29_COMPLETE_SOURCE_NO_CROSSING`.

The historical PARTIAL classification remains historically true and is not rewritten. This is a new derived dependency state for the **immutable Eq.(29) source block only**.

## Frozen interpretation

The source dependency object required three physical pieces: source-faithful label geometry, source-faithful path incidence, and a valid treatment of crossing/R semantics. R-placement may be satisfied either by a source-qualified placement when a crossing exists or by a prospective source-geometry proof that no crossing exists in the immutable block, making R/R^-1 placement not applicable to that block.

No later crossing-bearing amplitude inherits this non-applicability.

## Frozen classifications

- `EQ29_IMMUTABLE_SOURCE_DEPENDENCIES_COMPLETE_R_NOT_APPLICABLE` iff the dependency summary is valid and exactly contains qualified label geometry + qualified path incidence + unqualified R placement, while the independently frozen complete geometry is valid `EQ29_COMPLETE_SOURCE_NO_CROSSING` with zero proper crossing pairs.
- `EQ29_IMMUTABLE_SOURCE_DEPENDENCIES_PARTIAL` iff geometry/incidence remain qualified but complete geometry has a crossing or is unresolved, or the expected historical R-placement state differs without becoming independently qualified.
- `INVALID_SOURCE_OR_IMPLEMENTATION` on artifact/digest mismatch, missing required fields, invalid upstream summary, or contradictory terminal records.

## Authorization

Only `EQ29_IMMUTABLE_SOURCE_DEPENDENCIES_COMPLETE_R_NOT_APPLICABLE` authorizes **preregistration** of a literal Eq.(29) tensor reconstruction gate from the immutable source block. It does not itself authorize numerical amplitude claims, refinement/bridge credit, or candidate theory construction.

## Claim locks

Bridge credit remains zero. Candidate theory remains `UNFORMED`; no `BRIDGE_DERIVED`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.
