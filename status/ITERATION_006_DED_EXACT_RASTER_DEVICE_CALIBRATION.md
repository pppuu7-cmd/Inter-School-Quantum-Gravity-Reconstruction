# ITERATION_006 DED exact raster→device coordinate calibration — preregistration

Date: 2026-09-12  
Status: PREREGISTERED BEFORE IMPLEMENTATION

## Frozen motivation

The terminal DED topology prerequisite is `TOPOLOGY_EXTRACTION_UNSTABLE`. Two 600-dpi component births were localized in run `34717249322`. Subsequent vector provenance run `34719398165` localized A but not B using vector-union normalized coordinates, and source marking-class run `34719724688` still left B unresolved. Those latter audits use a vector-mark-union normalization, whereas the frozen raster pipeline defines component coordinates **after cropping to thresholded foreground**. This gate tests only that coordinate-frame mismatch.

## Frozen source/render pipeline

Pinned source: arXiv:1801.03771 SHA256 `9fc0b3396573b4f5ec457cafbc487aa5a1681fcb48561916d1398ed5bcc35303`, DED `_images/DEDconplex_plus_vg.eps`.

Reproduce exactly the frozen original-EPS render:

`gs -q -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pnggray -r600 -sOutputFile=... DEDconplex_plus_vg.eps`

and the frozen image rule `gray < 200`, foreground crop `[ys.min():ys.max()+1, xs.min():xs.max()+1]`, 8-connected component labeling and minimum kept area fraction `1e-5`. No rendering or image threshold may change.

Frozen component checks from run `34717249322` for ORIGINAL_EPS at 600 dpi:

- kept component count `123`;
- A: normalized centroid `(x,y)=(0.189866082925573,0.5180094786729857)`, crop-relative bbox `[542,400,552,406]` (y0,x0,y1,x1), 44 pixels;
- B: normalized centroid `(x,y)=(0.7200188857412654,0.8872037914691943)`, crop-relative bbox `[934,1521,939,1530]`, 39 pixels.

A reproduced component is identified by exact crop-relative bbox + pixel count; no nearest-neighbour component substitution is allowed.

## Exact raster→device mapping

Let full rendered PNG dimensions be `(H,W)` pixels and the frozen foreground crop origin be `(crop_y0,crop_x0)`. For a reproduced component with crop-relative pixel centroid `(cy,cx)`, its absolute raster pixel-center coordinate is:

`px = crop_x0 + cx + 0.5`, `py_top = crop_y0 + cy + 0.5`.

Ghostscript device coordinates use bottom-left y orientation for the default page device; therefore the preregistered device point is:

`device_x = px`, `device_y = H - py_top`.

No fitted scale, rotation, translation or landmark adjustment is allowed.

## Source mark trace under the same 600-dpi page device

In a separate Ghostscript execution using `pnggray -r600`, wrap source `stroke/fill/eofill` exactly as in the previous provenance work, but record both current-path device bbox and `strokepath` device bbox through `transform` **under the same page device**. Execute original marks unchanged. Text may be traced by `charpath` for diagnostics, but A/B classification uses source path/fill/stroke-envelope marks only.

## Positive control and classifications

- First, A must be contained by exactly one source mark under the exact device-coordinate mapping. If not, classification is `DED_RASTER_DEVICE_CALIBRATION_INVALID`; B is not interpreted.
- `DED_TARGET_B_EXACT_DEVICE_LOCALIZED`: A positive control passes and B is contained by exactly one source path/fill/stroke-envelope mark.
- `DED_TARGET_B_EXACT_DEVICE_AMBIGUOUS`: A passes but B is contained by more than one such mark.
- `DED_TARGET_B_EXACT_DEVICE_UNRESOLVED`: A passes but B is contained by zero such marks.
- `INVALID_SOURCE_OR_IMPLEMENTATION`: source hash, frozen component reproduction, device trace, or render output fails.

For containment, a point on a closed bbox boundary counts as contained. Nearest-mark distances are diagnostic only.

## Independent representation cross-check

A second lane repeats the render/trace after Ghostscript `eps2write` normalization at 600 dpi, using its own reproduced crop and components. It is a robustness cross-check only and cannot rescue failure of ORIGINAL_EPS positive control.

## Claim lock

No outcome changes `TOPOLOGY_EXTRACTION_UNSTABLE`, retunes raster rules, or proves DED→DLD refinement. Bridge credit remains zero; candidate theory remains `UNFORMED`.
