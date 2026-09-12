# ITERATION_006 DED target-B source marking-class audit — terminal result

Date: 2026-09-12  
Preregistration: `434340ab701fe9d7c8a1f3dfe7e4a4fc551d4f35`  
Implementation/launch: `a0022c4144dcd4eb302055b774023a18a1ce3529`  
Run: `34719724688`  
Aggregate job: `103623260709`  
Summary artifact: `10305432855`  
Summary digest: `sha256:3d34838fa18d7a32d42750d925d72ad13d88088bc5f5a94006d1daabf35b63fa`

## Frozen result

The aggregate returns:

`DED_TARGET_B_SOURCE_MARK_CLASS_UNRESOLVED`

The dynamic source execution trace found no exact target-B containment in any preregistered dynamic marking class:

- stroke envelope obtained with `strokepath`: none;
- fill/eofill path marks: none;
- text `show` charpath marks: none;
- unsupported dynamic events: none.

The independent active-PostScript census found:

- image-class operators (`image`, `imagemask`, `colorimage`): `0`;
- text-class operator tokens: `2`.

Thus target B is not localized to a source path centreline, exact stroke envelope, traced text glyph bbox, or source raster/image operator under the current coordinate normalization. No nearest-neighbour mark is promoted.

## Interpretation and next admissible question

The preceding provenance gates normalize target coordinates through a vector-mark union, while the original component-birth coordinates are defined in a thresholded **cropped raster frame**. Since expanded stroke/text/image classes do not resolve B, the next admissible diagnostic is exact reconstruction of the fixed raster-pixel → EPS/device-coordinate transform used by the frozen rendering pipeline. Such a coordinate-calibration audit may reuse the same frozen threshold solely to recover the original crop origin; it may not change threshold/connectivity/minimum-area criteria.

The terminal raster topology verdict remains `TOPOLOGY_EXTRACTION_UNSTABLE` regardless of any later provenance localization.

## Claim locks

No DED→DLD refinement map, amplitude identity, cylindrical consistency or bridge credit is established. Candidate theory remains `UNFORMED`; no `BRIDGE_DERIVED`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND` claim is authorized.
