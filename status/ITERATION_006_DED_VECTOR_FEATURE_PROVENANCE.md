# ITERATION_006 DED vector-feature provenance — preregistration

Date: 2026-09-12  
Status: PREREGISTERED BEFORE IMPLEMENTATION

## Frozen prerequisite

The dual-representation raster topology prerequisite is terminal `TOPOLOGY_EXTRACTION_UNSTABLE` and cannot be rescued by threshold, connectivity or minimum-area retuning. Run `34717249322` localized exactly two additional 600-dpi DED components, identically in original EPS and GS-normalized EPS:

- target A normalized raster centroid `(x,y) = (0.189866082925573, 0.5180094786729857)`, 44 pixels;
- target B normalized raster centroid `(x,y) = (0.7200188857412654, 0.8872037914691943)`, 39 pixels.

The only scientifically admissible continuation is source-semantic/vector-level identification of those frozen features; this gate does not rerun or modify the failed raster classifier.

## Frozen source

- arXiv:1801.03771 source bundle SHA256 `9fc0b3396573b4f5ec457cafbc487aa5a1681fcb48561916d1398ed5bcc35303`;
- DED source EPS: `_images/DEDconplex_plus_vg.eps`;
- no source edits or path deletion are permitted.

## Frozen vector object

Instrument the original EPS execution in Ghostscript at the PostScript marking-operator level. Before executing the EPS, wrap `stroke`, `fill` and `eofill`; immediately before each original marking operator, record the current path bounding box using PostScript `pathbbox`, together with operator type and monotonically increasing mark index. The original operator must then execute unchanged. The audit does not classify text-show operators or image operators as vector path marks; if either frozen target lacks a path-mark provenance candidate, the result is unresolved rather than fitted.

For all recorded vector path marks, form the union of their source-space bounding boxes. Map each mark bbox to normalized figure coordinates using this union, with x increasing left→right and raster y increasing top→bottom. No raster threshold enters this normalization.

## Frozen target matching

For each frozen target centroid, identify vector marks whose normalized bbox contains the target point exactly under closed-bbox containment. No spatial tolerance or nearest-neighbour radius is allowed in the PASS condition. Separately report the five nearest mark bboxes by exact point-to-rectangle Euclidean distance for diagnostic use only; nearest marks are never promoted when containment is absent.

## Independent lane

A second lane must repeat the same instrumentation after Ghostscript `eps2write` normalization of the pinned original EPS. Because eps2write may merge/split marking operations, mark indices need not match. The lane is used only to test whether each target is still contained by at least one vector-path mark at the same normalized location class. It cannot substitute for source-original uniqueness.

## Frozen classifications

- `DED_VECTOR_FEATURES_UNIQUELY_LOCALIZED`: in the original source EPS each target is contained by exactly one recorded stroke/fill/eofill bbox, the two targets map to distinct marks, and the normalized eps2write lane contains each target in at least one mark bbox.
- `DED_VECTOR_FEATURES_AMBIGUOUS`: source-original path marks contain both targets but at least one target has multiple containing mark bboxes or both targets map to the same source mark.
- `DED_VECTOR_FEATURES_UNRESOLVED`: at least one target has zero source-original containing path marks; nearest-mark diagnostics may be reported but cannot promote it.
- `INVALID_SOURCE_OR_IMPLEMENTATION`: source hash/path failure, PostScript instrumentation failure, invalid bbox output, or no path marks recorded.

No outcome changes the terminal raster topology verdict. Even `UNIQUELY_LOCALIZED` only identifies vector provenance candidates for later source-semantic inspection; it does not prove DED→DLD incidence embedding or bridge/refinement consistency.

## Claim locks

Raster threshold/connectivity/minimum-area retuning remains forbidden. Bridge credit remains zero. No amplitude identity, cylindrical consistency, candidate theory, `BRIDGE_DERIVED`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.
