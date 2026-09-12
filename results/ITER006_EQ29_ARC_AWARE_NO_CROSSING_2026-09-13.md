# ITER006 — Eq.(29) arc-aware source geometry terminal result

Date: 2026-09-13

## Authoritative gate

- Gate: `ITER006_RC006_EQ29_ARC_AWARE_SOURCE_GEOMETRY`
- Prereg commit: `9c8221a066369e51367b569f7a65169ba757aa8c`
- Implementation/head commit: `286c67c9c7ab444a86bdbea12b9159b5aae36461`
- Run: `34721521848`
- 80-dps job: `103628188426`
- 120-dps job: `103628188654`
- Aggregate job: `103628295264`
- 80-dps artifact: `10306676425`, digest `sha256:ab7c5230fb953a0d012404468b2d34930e0981f56e8b60bc41932feab5203f13`
- 120-dps artifact: `10307075132`, digest `sha256:8868d8ef456cac1cc8cd0392b865030a89d3769958c5164119b5d59c9055a494`
- Summary artifact: `10305789489`, digest `sha256:3b0347308b27f1c9f9bd0aa122505e2dc3dd8799feece6c52366c91c60402d68`

All jobs completed successfully, but scientific classification is based on the frozen aggregate and raw geometry artifacts, not CI color.

## Frozen raw result

Both independent precision lanes reconstruct the same immutable Eq.(29) source block SHA256 `4f505657a580216d176c1c63ec92f5614dc73e8113294722a854d5a350b67083` and return identical topology:

- geometric primitives: `18`;
- straight lines: `16`;
- circular TikZ arcs: `2`;
- proper interior crossings after line-line, line-arc and arc-arc tests: `0`;
- exact R-reference control: `true`;
- direct R-near source ref: `eq:eprl-3-valent`.

The 80- and 120-digit artifacts both contain `proper_crossings: []`. Therefore the result is precision-stable under the preregistered topology comparison.

## Scientific classification

**`EQ29_ARC_AWARE_NO_PROPER_CROSSING`**.

Within the immutable final Eq.(29) drawing, no R/R^-1 crossing placement is geometrically applicable. This resolves the specific R-placement applicability blocker that survived run `34718784867`.

Scope is strict: Appendix F still states that the derivation of the final EPRL expression uses the R-matrix identity, and the literal Eq.(29) formula contains its source q-phase. The result therefore does **not** license dropping or modifying that literal q-phase; it only removes any need to invent an additional graphical R/R^-1 placement in the final planar Eq.(29) block.

## Consequences and locks

- Prior `EQ29_SOURCE_DEPENDENCIES_PARTIAL` is narrowed: label geometry and source incidence were already qualified, and final-block R applicability is now resolved as absent.
- `eq29_amplitude_authorized=false` remains true because the literal formula/derivation chain and numerical graphical evaluation still require their own prospectively frozen gates.
- `bridge_credit=false`.
- No `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`, candidate action/Hamiltonian/field equations, or candidate-theory construction.

## Next gate

A first proposed direct B14-isomorphism preregistration was explicitly superseded **before implementation** after consistency review against already existing source-incidence evidence showed that Eq.(29) is not a nine-edge B14 graph. No production run existed for that proposal.

The corrected prospective next object is the literal source derivation chain: Eq.(29) factor/q-phase + Appendix-F B15/R dependency + Appendix-B B13/B15/B16 identities. Prereg commit `98197e8fa44224fc8af547edbc47a2e65f49ba56`; implementation commit `a210a47edbc8f4510b6edd4e18e3f1dee377ed47`. Only if that source chain is machine-qualified may a numerical Eq.(29) reconstruction object be frozen.
