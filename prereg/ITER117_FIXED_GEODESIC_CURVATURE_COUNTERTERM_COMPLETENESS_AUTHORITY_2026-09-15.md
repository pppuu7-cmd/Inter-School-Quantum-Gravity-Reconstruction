# ITER117 preregistration — fixed-geodesic curvature counterterm-completeness authority

Date: 2026-09-15
Gate: `ITER117_FIXED_GEODESIC_CURVATURE_COUNTERTERM_COMPLETENESS_AUTHORITY`

## Motivation frozen before residue calculation

ITER116 identified the separated single-log coefficient `B_1` as a potentially cheap noncancellation diagnostic controlled by the highest UV-pole / `H^(2)`-type structure. Before computing that residue, the renormalization basis must be complete.

The fixed-geodesic matter-scalar precedent uses a wave-function-type renormalization of the geodesic embedding coordinates `Z_chi`. For scalar curvature, however, the lower-order separated `RR` correlator vanishes: it is purely contact. Therefore it is not automatic that the same geodesic counterterm basis can renormalize curvature-specific separated divergences.

## Frozen authority

1. arXiv:1706.01891 / CQG 35, 035005 (2018), especially the geodesic embedding counterterm acting on derivatives of the lower-order matter propagator.
2. arXiv:2510.11888 / PRD 113, 106032 (2026), especially the result that the leading curvature correlator is analytic in momentum / contact in position space and vanishes away from coincidence.
3. ITER112-116 for the fixed-geodesic F/M/G census and corrected radial/RG basis.

## Frozen question

Is ordinary local gravitational/curvature-composite renormalization plus the scalar-precedent geodesic embedding renormalization `Z_chi` sufficient to renormalize the anchored fixed-geodesic scalar-curvature correlator through `O(G^2)` at nonzero separation? Or can curvature-specific endpoint/line composite counterterms be required before a physical `B_1` residue is defined?

## Required predicates

A. Write the `Z_chi` counterterm contribution to a generic fixed-geodesic two-point observable as the endpoint-coordinate variation of its lower-order correlator.

B. Apply A to `RR` and retain the source fact that the lower-order separated curvature correlator is contact-only.

C. Determine whether `Z_chi` can contribute to/cancel a separated nonlocal curvature divergence at `O(G^2)`.

D. Keep ordinary local curvature/action counterterms separate and determine whether their lower-order insertions can cancel a nonlocal separated geodesic divergence.

E. Test whether renormalization of the **composite product** `R(chi) R(x)` can require new endpoint/line-supported operator mixing beyond independent renormalization of `R` and `chi`.

F. A full `STANDARD_BASIS_SUFFICIENT` PASS requires source/analytic authority that no additional curvature-specific nonlocal counterterm is allowed/needed.

G. If sufficiency is not established, identify the minimal allowed counterterm/operator sectors that must be included before computing the highest-pole residue.

H. No EDT target may be used to choose finite counterterms or infer a basis.

## Frozen classifications

- `PASS_SCOPED_STANDARD_BULK_PLUS_ZCHI_COUNTERTERMS_SUFFICIENT` if A-H establish sufficiency.
- `PASS_SCOPED_ZCHI_SEPARATED_INACTIVE_CURVATURE_PRODUCT_COUNTERTERM_BASIS_OPEN` if A-D show the scalar-style counterterm is contact-only for RR but E-F remain open.
- `PASS_SCOPED_ADDITIONAL_CURVATURE_GEODESIC_COUNTERTERMS_REQUIRED` if a source/analytic divergence explicitly requires them.
- `BLOCKED_SOURCE_AUTHORITY` if the renormalization structure cannot be typed.

## Controls

- `MATTER_TREE_CURVATURE_TREE_SWAP_CONTROL`
- `CONTACT_NONLOCAL_COUNTERTERM_CONTROL`
- `INDEPENDENT_OPERATOR_PRODUCT_RENORMALIZATION_CONTROL`
- `LOCAL_BULK_GEODESIC_LINE_COUNTERTERM_CONTROL`
- `EDT_COUNTERTERM_FIT_CONTROL`

## Claim ceiling

This gate determines renormalization completeness only. It does not compute `B_1`, prove cancellation/noncancellation, authorize an EDT fit, establish a direct EDT/EFT conflict, `BRIDGE_DERIVED`, new physics or a candidate theory.