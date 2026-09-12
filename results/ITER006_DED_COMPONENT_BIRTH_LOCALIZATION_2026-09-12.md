# ITER006 DED component-birth localization — 2026-09-12

Authoritative run: `34717249322`  
Aggregate job: `103616862737`  
Aggregate artifact: `10305175813`  
Aggregate artifact digest: `sha256:ddcdf805d87dbe6ab9a1c61bc5a67d44372b84e1773ad7742b8bab50723da92d`

## Frozen diagnostic scope

This run did not change the topology threshold (`gray < 200`) or the minimum kept-component area fraction (`1e-5`). It was launched only after the terminal preregistered topology classification `TOPOLOGY_EXTRACTION_UNSTABLE` to localize the observed DED 300→600 dpi component-count increase. It cannot retroactively promote the failed prerequisite and grants no incidence, embedding, amplitude, cylindrical-consistency or bridge credit.

## Result

All four DED extraction lanes completed successfully. The matching aggregate returned:

`DED_EXTRA_600DPI_COMPONENTS_LOCALIZED`

Both representations reproduce the same count change:

- `ORIGINAL_EPS`: 121 kept components at 300 dpi → 123 at 600 dpi;
- `GS_EPS2WRITE_NORMALIZED`: 121 → 123.

In both representations the two 600-dpi components left unmatched by the frozen 300↔600 component matching are numerically identical:

1. label 66: `44` pixels at 600 dpi, area fraction `1.966336322164543e-05`, normalized centroid `(x,y)=(0.189866082925573, 0.5180094786729857)`, bbox `[542,400,552,406]`;
2. label 117: `39` pixels at 600 dpi, area fraction `1.7428890128276632e-05`, normalized centroid `(x,y)=(0.7200188857412654, 0.8872037914691943)`, bbox `[934,1521,939,1530]`.

The exact agreement across original EPS and Ghostscript-normalized EPS strongly localizes the failure mode to two tiny DED raster components that cross the frozen extraction criterion only at higher raster resolution. It does **not** establish that they are semantically irrelevant features of the source figure; therefore deleting them, changing connectivity, changing threshold, or raising the minimum-area rule post hoc is forbidden as a route to a topology PASS.

## Scientific interpretation

The original dual-representation topology prerequisite remains terminal:

`TOPOLOGY_EXTRACTION_UNSTABLE`

This diagnostic converts a broad representation/DPI ambiguity into a sharply localized DED-specific resolution sensitivity. The next scientifically admissible topology step, if pursued, must be source-semantic/vector-level identification of these two features under a prospectively defined audit—not threshold retuning.

## Claim lock

No `BRIDGE_DERIVED`, no source-derived DED→DLD refinement map, no amplitude identity, no cylindrical consistency, no `NEW_PHYSICS_FOUND`, and no candidate-theory promotion follows from this diagnostic.
