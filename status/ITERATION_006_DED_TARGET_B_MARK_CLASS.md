# ITERATION_006 DED target-B source marking-class audit — preregistration

Date: 2026-09-12  
Status: PREREGISTERED BEFORE IMPLEMENTATION

## Frozen prerequisite

Run `34719398165` is terminal `DED_VECTOR_FEATURES_UNRESOLVED`: target A is contained by exactly one `stroke/fill/eofill` current-path bbox in both original and eps2write-normalized representations, while target B is contained by zero such bboxes in both. The terminal raster topology verdict remains `TOPOLOGY_EXTRACTION_UNSTABLE`.

Frozen target B normalized coordinate from run `34717249322`:

`(x,y) = (0.7200188857412654, 0.8872037914691943)`.

## Source and scope

Pinned source is arXiv:1801.03771 bundle SHA256 `9fc0b3396573b4f5ec457cafbc487aa5a1681fcb48561916d1398ed5bcc35303`, file `_images/DEDconplex_plus_vg.eps`.

This is a +0 provenance-classification audit only. It must not change raster threshold, connectivity, crop rule, minimum-area rule or component matching.

## Frozen dynamic marking classes

Instrument the **original pinned EPS** before execution and record device-space bboxes for:

1. `stroke`: use a protected copy of the current path and Ghostscript/PostScript `strokepath` before the original stroke, so the bbox includes line width, line cap and line join rather than only the centerline path;
2. `fill` / `eofill`: ordinary current-path bbox;
3. text `show`: in protected graphics state, use the current font and current point to create a `charpath` for the exact string and record its path bbox; if charpath fails, record an explicit unsupported event rather than infer a bbox;
4. `glyphshow`: analogously construct the exact glyph charpath where supported and fail closed for that operator if unavailable.

The dynamic tracer must execute original marking operators unchanged after tracing. It must record a monotonically increasing mark index and marking class.

Normalize all dynamic mark bboxes with the same union-bbox convention as the preceding vector provenance gate. Target B counts only by exact closed-bbox containment; nearest-neighbour distance is diagnostic only and never a PASS criterion.

## Independent static census

Independently scan the original EPS source text, without executing it, for active PostScript marking/operator tokens from these classes:

- text: `show`, `ashow`, `widthshow`, `awidthshow`, `glyphshow`;
- raster/image: `image`, `imagemask`, `colorimage`;
- path paint: `stroke`, `fill`, `eofill`.

Report token counts and bounded source contexts. Static presence alone never establishes target-B provenance.

## Frozen classifications

- `DED_TARGET_B_STROKE_ENVELOPE_LOCALIZED`: dynamic target B is contained by exactly one `stroke`-envelope bbox and by no text/glyph bbox.
- `DED_TARGET_B_TEXT_LOCALIZED`: dynamic target B is contained by exactly one `show`/`glyphshow` bbox and by no stroke-envelope bbox.
- `DED_TARGET_B_MARK_CLASS_AMBIGUOUS`: target B is contained by multiple dynamic marks or by more than one marking class.
- `DED_TARGET_B_IMAGE_CLASS_UNRESOLVED`: no dynamic path/text containment exists, but the independent static census finds at least one image-class operator; image spatial provenance is not inferred by this gate.
- `DED_TARGET_B_SOURCE_MARK_CLASS_UNRESOLVED`: no dynamic containment exists and no image-class source operator is found.
- `INVALID_SOURCE_OR_IMPLEMENTATION`: source hash failure, no valid dynamic marks, tracer changes execution semantics, or malformed output.

A localized result identifies source marking-class provenance only; it does not make the two raster component births semantically ignorable and does not promote DED→DLD topology/refinement.

## Claim locks

Raster topology remains failed. Bridge credit remains zero. Candidate theory remains `UNFORMED`; no `BRIDGE_DERIVED`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.
