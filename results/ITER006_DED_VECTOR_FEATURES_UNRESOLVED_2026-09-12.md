# ITERATION_006 DED vector-feature provenance — terminal result

Date: 2026-09-12  
Preregistration: `a01b216be502d2463949bde5ccb5829a9ac8d94c`  
Implementation/launch: `0b33c2d263b27f261a1c699a6e5c70a01e95550b`  
Run: `34719398165`  
Aggregate job: `103622523348`  
Summary artifact: `10305988121`  
Summary digest: `sha256:45b7a2a25b77e8b42b315d4acfa9782bf69351016413ecbe847a5fba4253158d`

## Frozen result

The frozen classifier returns:

`DED_VECTOR_FEATURES_UNRESOLVED`

Both independent representations are internally valid and agree on the target-containment counts:

- `ORIGINAL_EPS`: target A = 1 vector path mark, target B = 0;
- `GS_EPS2WRITE_NORMALIZED`: target A = 1 vector path mark, target B = 0.

Each trace recorded 60 `stroke`/`fill`/`eofill` path-mark operations. Target A is therefore reproducibly associated with a source vector-path mark. Target B is not contained by any such path-mark bounding box in either representation.

## Scientific interpretation

This result does **not** license nearest-neighbour assignment of target B and does not imply that target B is semantically irrelevant. The preregistration deliberately excluded text-show operators, image operators, and stroke-envelope expansion beyond the current-path centreline bbox. The absence of a path-mark containment candidate therefore narrows the next admissible provenance question to those explicitly excluded source marking classes.

The terminal raster topology verdict remains `TOPOLOGY_EXTRACTION_UNSTABLE`; no threshold, connectivity or minimum-area retuning is authorized. No DED→DLD incidence embedding, refinement map, amplitude identity, cylindrical consistency or bridge credit follows.

## Admissible continuation

A separate prospectively frozen +0 provenance audit may classify target B against text/glyph/image marking operators and against the source stroke envelope derived from current line width and CTM. Such an audit must remain diagnostic and cannot retroactively turn the failed raster topology prerequisite into a PASS.

## Claim locks

Bridge credit remains zero. Candidate theory remains `UNFORMED`; no `BRIDGE_DERIVED`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.
