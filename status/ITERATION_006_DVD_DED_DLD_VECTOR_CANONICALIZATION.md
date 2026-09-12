# Iteration 006 — DED/DLD resolution-free vector canonicalization prerequisite

## Preregistration
Frozen before implementation/production. This is the permitted vector-level follow-up after terminal `DED_DLD_SOURCE_CONTEXT_ONLY` and the previously failed raster topology prerequisite. It does not retune raster thresholds and does not assert a DED→DLD embedding.

Pinned source: arXiv `1801.03771`, source tarball SHA256 `9fc0b3396573b4f5ec457cafbc487aa5a1681fcb48561916d1398ed5bcc35303`.
Assets: `_images/DEDconplex_plus_vg.eps`, `_images/DLDandVertex.eps`.

## Frozen object
For each asset and each of two source representations — exact original EPS and Ghostscript `eps2write` normalized EPS — convert without rasterization through Ghostscript `pdfwrite` and Poppler `pdftocairo -svg`. From the resulting SVG remove the `<defs>...</defs>` block (glyph definitions) and extract the multiset of geometric `<path d="...">` strings in the rendered body. Normalize XML whitespace only; do not round or alter numeric coordinates. Sort the exact path strings and hash the multiset. Also record body path count, `<use>` count, SVG width/height/viewBox and body-path command histogram (`M/m,L/l,C/c,Q/q,A/a,H/h,V/v,Z/z`).

Matrix: `asset ∈ {DED,DLD}` × `representation ∈ {ORIGINAL_EPS,GS_EPS2WRITE_NORMALIZED}`, `fail-fast:false`.

## Frozen validity and classifier
A lane is valid only if source hash matches, selected EPS exists, PDF and SVG conversions succeed, SVG body contains at least one geometric path, and metadata is parseable.

For each asset, original and normalized representations are **exact-vector stable** iff all of the following match exactly: sorted body-path multiset SHA256, body path count, command histogram, `<use>` count, and normalized SVG viewBox/width/height strings.

Aggregate classifications:
- `DED_DLD_VECTOR_CANONICALIZATION_REPRESENTATION_STABLE`: both DED and DLD are exact-vector stable. This authorizes only a separately preregistered vector incidence/topology extraction gate; no refinement/bridge credit.
- `DED_VECTOR_CANONICALIZATION_UNSTABLE_DLD_STABLE`: DLD stable, DED unstable. Vector route remains BLOCKED for DED; no selector or coordinate tolerance may be fitted post hoc.
- `DLD_VECTOR_CANONICALIZATION_UNSTABLE_DED_STABLE`: symmetric case.
- `DED_DLD_VECTOR_CANONICALIZATION_UNSTABLE`: both unstable.
- `INVALID_SOURCE_OR_INFRASTRUCTURE`: conversion/source/parse failure; technical only.

## Locks
No raster comparison, no DPI, no coordinate tolerance, no post-result rounding, no manual SVG edit, no DED→DLD embedding claim, no amplitude identity/cylindrical consistency, `bridge_credit=false`, candidate theory `0/UNFORMED`, and no bridge/new-physics/new-theory claims.
