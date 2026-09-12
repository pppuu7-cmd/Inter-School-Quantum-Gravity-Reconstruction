# ITER006 — Eq.(29) R-placement structural topology terminal result

Date: 2026-09-13

## Authoritative production

- Gate: `ITER006_RC006_EQ29_RPLACEMENT_REFERENCE_TOPOLOGY`
- Prereg commit: `95a176d84353a9bf358035140f4fd7423b45873e`
- Implementation commit: `745ecd2f3c999dbf130d4e7ed4520a3f0f28f13a`
- Trigger/head commit: `892c4b55f4099ced2743fbc0d34dc121e09fa070`
- Run: `34718784867`
- Aggregate job: `103620738661`
- Summary artifact: `10305042483`
- Summary digest: `sha256:482bc4998d96fd11b0ad2b742038b626d76bc6eacf950efa358cb6333212fc96`

Lane artifacts:

- `reference_graph`: job `103620663803`, artifact `10305992257`, digest `sha256:e77cb1acca0d6983fd0abaefc496872e7e54e98932085b76d321b5cf910ea98d`.
- `crossing_geometry`: job `103620663910`, artifact `10304927980`, digest `sha256:36dee43fb0e6d774a59dcce71292050ba818f69c85dbad78c94b46cf186ab698`.
- `appendix_graph_chain`: job `103620663950`, artifact `10305123431`, digest `sha256:d52ddf3612fc5dd03fee37d56f730b5b558d4c0bd67906c7c659063724fc7366`.

All four jobs completed with green CI; classification below is from the frozen scientific classifier and raw artifacts, not CI color.

## Raw frozen evidence

The immutable Eq.(29) candidate block hash remained exactly `4f505657a580216d176c1c63ec92f5614dc73e8113294722a854d5a350b67083`.

### Exact TeX reference graph

`reference_graph` returned `EQ29_R_EXPLICIT_REFERENCE_PATH_PRESENT`.

- EPRL-body refs: `eq:eprl-3-valent`, `sec:optimization`, `fig:eprl-plots`.
- Exact direct target ref: `eq:eprl-3-valent`.
- R/R^-1 source-formula offsets: `114215`, `114902`.
- The exact label near those formulas includes `eq:eprl-3-valent`.

Thus the previously missing Eq.(29)-specific structural reference route to the R convention is present under the preregistered exact-reference object.

### Straight-line crossing geometry

`crossing_geometry` returned `EQ29_NO_STRAIGHT_CROSSING_ARCS_UNRESOLVED`.

- straight segments: `15`;
- TikZ arcs: `2`;
- proper straight-segment crossing pairs: none.

The predecessor gate deliberately did not infer the geometry of the two arcs. Therefore it cannot decide whether a proper crossing exists in the full source path.

### Appendix graph chain

`appendix_graph_chain` returned `EQ29_APPENDIX_GRAPH_REFERENCE_CHAIN_ABSENT`.

The R-convention context references `app:graph`, but the EPRL body does not independently reference `app:graph`. This does not erase the direct `eq:eprl-3-valent` reference route found by the separate exact-reference lane.

## Frozen aggregate classification

**`EQ29_RPLACEMENT_APPLICABILITY_INCONCLUSIVE`**.

This is a scientifically valid terminal diagnostic, not an infrastructure/numerical failure. It is neither a PASS nor a scientific FAIL of Eq.(29) itself. The exact source-reference part is qualified, while geometric applicability of R/R^-1 remains unresolved only because the two source arcs were outside the predecessor geometry object.

Preserved locks:

- prior `EQ29_SOURCE_DEPENDENCIES_PARTIAL` verdict remains authoritative;
- `eq29_amplitude_authorized=false`;
- `bridge_credit=false`;
- no lexical/crossing selector fitting or threshold retuning is authorized;
- no `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, or `ALL_KNOWN_SCHOOLS_FAIL` claim.

## Next prospectively frozen gate

The only dependent follow-up permitted by the predecessor preregistration is an exact **arc-aware source geometry** audit of the same immutable Eq.(29) block. That gate was preregistered before implementation in commit `9c8221a066369e51367b569f7a65169ba757aa8c` and implemented in commit `286c67c9c7ab444a86bdbea12b9159b5aae36461`.

Authoritative production run: `34721521848` (`ISQGR Iter006 RC006 Eq29 Arc Aware Source Geometry`). It evaluates full line-line, line-arc and arc-arc proper intersections independently at 80 and 120 decimal digits against frozen endpoint/residual tolerances. The gate itself cannot award bridge credit and cannot authorize Eq.(29) amplitude; a qualifying result can only unlock a separately preregistered literal reconstruction gate.
