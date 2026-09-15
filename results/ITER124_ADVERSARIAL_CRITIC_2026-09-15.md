# ITER124 adversarial critic — projected RG/pole calculation specification

Date: 2026-09-15
Gate: `ITER124_FIXED_GEODESIC_CURVATURE_PROJECTED_RG_POLE_CALCULATION_SPEC`
Source authority: `sources/ITER124_FIXED_GEODESIC_CURVATURE_PROJECTED_RG_POLE_CALCULATION_SPEC_2026-09-15.md`

## Attack 1 — a validated manifest proves the physics calculation is complete

Rejected as an overclaim. CI only verifies that the frozen contract contains the previously authorized sectors/checks in the required order. Scientific completeness rests on ITER112–123 plus future detection of any evanescent or newly generated operator mixing. The manifest is a reproducibility guard, not a physics theorem.

## Attack 2 — de-Donder gauge alone is sufficient because the observable is gauge invariant

Rejected. Gauge invariance is an expected property of the complete relational observable, not permission to skip a check. ITER124 correctly treats de Donder as the primary reduction gauge and requires either an independent gauge-parameter cancellation or an equivalent BRST identity before accepting `B1_total` physically.

## Attack 3 — field-redefinition-redundant line directions may be dropped before renormalization

Rejected. They are not independent physical matching data after the ITER120 quotient, but their intermediate poles/counterterms can be necessary to verify closure and field-coordinate invariance. ITER124 retains them through the renormalization stage and quotients only after the consistency check.

## Attack 4 — only double poles matter for B1

Rejected by the strategy correction after ITER117–120. Direct `H^(2)`-type structures may contribute, but beta functions of genuine line couplings arise from the properly subtracted pole mixing and can feed the physical log coefficient. `B1_total` must combine direct and defect-running pieces.

## Attack 5 — the split B1_direct + B1_defect is separately physical

Not necessarily. The decomposition can depend on renormalization/operator basis conventions. The acceptance target is the complete `B1_total` of the fixed observable together with gauge and field-redefinition invariance. The split is bookkeeping needed to audit RG consistency.

## Attack 6 — the two-point kinematic projector can be applied to every raw pole immediately

Rejected. Other bulk/contact/redundant/possibly evanescent structures may be present before subtraction/basis reduction. The ITER123 projector only reconstructs coefficients once the relevant divergence is in the genuine two-shape defect span.

## Attack 7 — evanescent operators make the entire two-shape projector invalid

Too strong. Evanescent directions can be required as intermediate `d`-dimensional renormalization data and can feed poles/finite terms. After the complete renormalized amplitude is projected onto the physical genuine-defect sector, ITER123's general-`d` projector remains valid for that sector. The correct response is to enlarge intermediate bookkeeping if an evanescent structure appears, not to discard the physical basis.

## Attack 8 — B1_total != 0 is insufficient because B0 could cancel it

Rejected as an identity-in-separation claim. `B0+B1 log(mu^2 l^2)` with `B1!=0` cannot vanish for every nonzero `l`; at most it has isolated zeros. Therefore nonzero `B1_total` proves noncancellation of the whole `O(G^2)` separated function, though it does not determine its sign or fit any lattice data.

## Critic verdict

**CONFIRMS `PASS_SCOPED_PROJECTED_RG_POLE_CALCULATION_SPEC_CLOSED`.**

The next useful step is the topology/master-integral census. No coefficient should be computed or interpreted until the subtraction/projector contract is obeyed.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.