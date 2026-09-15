# ITER139 terminal result — affine single-line derivative ceiling repair

Date: 2026-09-15
Preregistration: `dccb8a3bc53aa0f186126e0f70f9e9ff79062a84`
Implementation: `cabddb23c6606efab4bfe4b91e40720e2b3ebbf7`
Workflow head: `6111ecfbe6a4952988cb96ca8d5791e9066a32be`
Authoritative run: `34957549365`
Job: `104343137406` (`affine-ceiling-repair`)
Artifact: `10391284660` (`iter139-affine-single-line-ceiling-repair`)
Artifact SHA256: `3fc8cf990382fdbd93fb7569619d39a127dbf4b20909e00ffc169d7a0aa115d3`

## Scientific classification

`PASS_SCOPED_AFFINE_SINGLE_LINE_CEILING_REPAIR_CLOSED_ENDPOINT_POLES_OPEN`

The global ITER129 affine one-propagator ceiling `N1_max<=5` survives exact tensor allocation. The old row-specific rule `N1_max=D_line_max+D_partner_max` is not generally a valid conservative rule for nonlinear multi-leg vertices because the nonlinear vertex derivatives can concentrate on one internal propagator.

## Exact rows

Independent-line exact degrees before routing `k=p-q`:

- `M_R2_chi1_dR1`: `N1_exact=5` (reproduced from ITER138);
- `M_R1_chi1_dR2`: `N1_exact=5` (new ITER139 result);
- `G_R1_chi2_Gamma2_dR1`: `N1_exact=4` (reproduced control).

For the new `M_R1_chi1_dR2` numerator:

- total degree = 6;
- q-degree = 5;
- k-degree = 4;
- monomial count = 213 in the adapted frame.

Three deterministic exact held-outs agree between the propagated-source contraction and an independent ten-component symmetric-basis Wick contraction:

- `-48893/8`;
- `-8441`;
- `6463/4`.

The same maximum degree 5 persists on the exact rational unit-vector panels `n=(3/5,4/5,0,0)` and `n=(1/2,1/2,1/2,1/2)`, so it is not a frame artifact.

## Prospective V2 ceiling policy

A corrected table is stored separately as `analysis/iter139_affine_single_line_ceiling_table_v2.json`; historical ITER129 files remain unchanged evidence.

- exact M1: 5;
- exact M2: 5;
- interaction-dressed M3: raised conservatively 4 -> 5 pending exact allocation;
- exact direct-Gamma2 G1: remains 4;
- `Gamma1-dchi1` G2: raised conservatively 4 -> 5 pending exact allocation;
- rows already at 5 remain 5.

Thus no prospective affine row exceeds the already-authorized global ITER129 ceiling 5, and no row is allowed to retain an unverified 4 if the old nonlinear-allocation rule is the only authority.

## Corrected endpoint jet ceilings for bulk chi1 M rows

Using the ITER126/129 local one-propagator map

`m_raw=2+N1`, `jet=m_raw-s-1`,

and exact bulk weight `(1-tau)`:

- lower endpoint `s=0`: `N1=5`, `m_raw<=7`, `jet<=6`;
- upper endpoint `s=1`: `N1=5`, effective `jet<=5`.

This applies exactly to M1/M2 as derivative ceilings and conservatively to M3 until its tensor allocation is closed. It is not a pole residue.

## Scope boundary

The ITER124 physical pole contract is in general `d=4-2 epsilon`. ITER138/139 exact tensor polynomials are D=4 authorities. They are sufficient to repair D=4 allocation/jet ceilings, but not by themselves sufficient to determine renormalized `1/epsilon` coefficients when higher-pole/subdivergence mixing can multiply O(epsilon) tensor terms. A general-d lift is therefore required before claiming B1 or physical noncancellation.

## Claim ceiling

No curvature `1/epsilon` coefficient, B1, noncancellation theorem, finite B0, EDT comparison, bridge, new physics or candidate theory is established. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
