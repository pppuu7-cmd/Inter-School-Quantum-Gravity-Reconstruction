# ITER006 — DED/DLD vector canonicalization terminal result

Date: 2026-09-13

## Authority
- Prereg commit: `c1384a675a53e3aaf3bde61808b280bcc6cdbb5b`
- Implementation/head: `27b8127a8be154051662515c2953d4b7a17b6030`
- Run: `34722257762`
- DED normalized job `103630162171`, artifact `10306447752`, digest `sha256:95db3f1d161d5e7fe8bf57aa47da46726b6b5b0f6a64235def2c0412dbb86a12`
- DLD original job `103630162179`, artifact `10306238363`, digest `sha256:9cc7b6c2d8094d42f67f86a34b33f2d9a8cb754ad4e6028a72ca894376342bc9`
- DLD normalized job `103630162213`, artifact `10306358137`, digest `sha256:e3996d01cae9967ec0b017393ff784d7674b3bcf70ed02a1b17e6bd7fd789c0e`
- DED original job `103630162280`, artifact `10306193358`, digest `sha256:370214bf6b95b8e5e79edf6f820c6b5889562c62e6676aabd6e0a7383663757b`
- aggregate job `103630201105`, artifact `10306487662`, digest `sha256:7011e93d7c2bdb29f6860d197319875c14968429baf5532757f46e714f9f3975`

## Frozen result
All four vector lanes are valid. Aggregate classification:

**`DED_DLD_VECTOR_CANONICALIZATION_UNSTABLE`**

Frozen exact-vector stability is false for both `DED` and `DLD`: after non-raster Ghostscript `pdfwrite` → Poppler SVG canonicalization, the original EPS and Ghostscript `eps2write`-normalized EPS do not have identical frozen body-path multiset/count/command/use/viewBox metadata.

This is a valid scoped negative result for the strict exact-vector canonicalization object, not an infrastructure failure. The preregistration expressly forbids post-result coordinate rounding, tolerance fitting, manual SVG editing, or choosing a subset of matching paths.

## Consequence
The DED/DLD route now has three independent blockers:
1. raster topology: `TOPOLOGY_EXTRACTION_UNSTABLE`;
2. active source prose: `DED_DLD_SOURCE_CONTEXT_ONLY`, with no frozen both-figure relation/map evidence;
3. strict resolution-free vector canonicalization: `DED_DLD_VECTOR_CANONICALIZATION_UNSTABLE`.

Therefore no source-derived injective V/E/F refinement map is authorized, no parent/refined amplitude identity may be launched from this route, and bridge credit remains zero.

A new attempt would require a genuinely new mathematically justified source/vector object defined prospectively; merely adding coordinate tolerances or alternate render settings is prohibited.

Candidate theory remains `0/UNFORMED`.
