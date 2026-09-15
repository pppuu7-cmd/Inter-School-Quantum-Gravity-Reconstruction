# ITER115 terminal disposition — invalidated before adjudication

Date: 2026-09-15
Original gate: `ITER115_FIXED_GEODESIC_CURVATURE_G2_RG_LOG_HIERARCHY_AUTHORITY`
Original preregistration: `40ef27f6d0be59c5d47b40a9ebc9d6c46c748d2e`
Triggering correction: `7e8d7e9c0ade3d0483de2448a8011bd09d6a699a`
Corrected ITER114 terminal: `8fb4ca397617ed9f0a84e10422acee9088429a8c`

## Classification

**`INVALIDATED_PRE_ADJUDICATION_BY_ITER114_SEPARATED_LOG_DEGREE_CORRECTION`**

Scientific credit: **0**.
Bridge credit: **0**.

## Reason

ITER115 was preregistered on the superseded ansatz

`A_0 + A_1 L + A_2 L^2`.

The corrected separated distributional analysis shows that the one-loop noncontact basis is instead

`B_0 + B_1 L`,

because the outer Laplacian in `H^(2)` lowers the separated logarithmic degree:

`partial^2[L^2/r^2]=8(1-L)/r^4` for `r>0`.

Thus ITER115's central `A_2` question does not correspond to an independent separated coefficient and must not be adjudicated.

## Audit status

No coefficient calculation, target comparison or EDT fit was performed under the invalid premise. The invalidation therefore removes no scientific result and does not create retrospective tuning.

## Correct successor

A new preregistration must use

`C_RR^geo(l;mu)=G^2 l^-8[B_0(mu)+B_1(mu)L]+O(G^3)`

and test the RG hierarchy between `B_0` and `B_1`, with particular attention to whether the highest UV-pole/geodesic residue fixes `B_1`.

Candidate theory remains **UNFORMED / 0%**.