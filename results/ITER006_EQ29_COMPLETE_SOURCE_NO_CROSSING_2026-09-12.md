# ITERATION_006 RC006 Eq.(29) exact arc-aware geometry — terminal result

Date: 2026-09-12  
Preregistration: `27abf689dda00283425f576bb5ed8188fc4b0d29`  
Implementation/launch: `9e483af5ff3a1822afc8622c51a973ca028db46f`  
Run: `34719362365`  
Aggregate job: `103622271283`  
Summary artifact: `10305333911`  
Summary digest: `sha256:3ec0ce7ab19a34243f2309e9b75cdcff20f8ba8ad1c034fc233702bef5e8c667`

## Frozen result

Both independently implemented source-path lanes completed successfully and agree exactly on the frozen classifier:

`EQ29_COMPLETE_SOURCE_NO_CROSSING`

Both reconstruct:

- total geometry primitives: `18`;
- straight segments: `16`;
- circular arcs: `2`;
- proper interior crossing pairs: `[]`.

The earlier straight-only audit counted 15 straight segments because it intentionally stopped continuity at unresolved arc operators. The exact arc-aware reconstruction resolves the two semicircular source arcs and restores the straight connector following the first arc; both independent implementations agree on the complete count of 16 straight segments. This is not threshold retuning; it is the preregistered completion of the previously unresolved source geometry object.

## Scientific scope

For the immutable Eq.(29) EPRL source drawing, the quantum-group crossing convention is **not geometrically applicable at this block level** because the complete source path has no proper crossing. Therefore an Eq.(29)-specific R/R^-1 placement is not required to represent this immutable diagram. This conclusion does not remove R-matrix requirements from any later amplitude or graph that actually contains a crossing.

The historical run `34718554940` remains, as executed, `EQ29_SOURCE_DEPENDENCIES_PARTIAL`; it is not rewritten. A new prospective reconciliation gate may combine its already qualified label geometry and path incidence with this independently established Eq.(29)-block R non-applicability. Only such a new gate may decide whether the immutable Eq.(29) source dependencies are now complete enough to authorize a separately preregistered literal tensor reconstruction.

## Claim locks

This source-geometry result alone does not authorize the numerical Eq.(29) tensor, bridge credit, cylindrical consistency, candidate theory, `BRIDGE_DERIVED`, `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, or `NEW_PHYSICS_FOUND`.
