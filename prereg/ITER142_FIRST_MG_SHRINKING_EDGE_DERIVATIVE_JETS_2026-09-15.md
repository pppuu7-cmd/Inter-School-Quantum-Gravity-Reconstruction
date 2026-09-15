# ITER142 preregistration — first M/G shrinking-edge derivative allocation and sharp local jets

Date: 2026-09-15
Gate: `ITER142_FIXED_GEODESIC_CURVATURE_FIRST_MG_SHRINKING_EDGE_DERIVATIVE_JETS`
Status: **FROZEN BEFORE AUTHORITATIVE PRODUCTION RUN**

## Motivation

ITER139 repaired the global/row maximum one-propagator derivative ceiling, and ITER141 then identified which Wick edge actually shrinks at each affine endpoint. For a local endpoint singularity, the relevant derivative count is the polynomial degree in the momentum carried by that shrinking edge, not the maximum degree carried by any nonsingular companion propagator.

This gate sharpens the connected-cross local Taylor-jet ceilings without changing the global ITER139 safety bound.

## Frozen prerequisites

- ITER138 exact M1/G1 numerator polynomials;
- ITER139 exact M2 numerator polynomial;
- ITER141 connected-cross Wick edge incidence and singular strata;
- ITER128/126 local rule `m_raw=2+N`, `jet=m_raw-s-1`.

If the ITER141 edge map is not reproduced exactly, this gate fails rather than choosing a different momentum assignment.

## Frozen edge-to-momentum map

Consume the tensor conventions of ITER138/139 exactly:

- `M_R2_chi1_dR1`: q is the R2 leg paired to the chi1 field at `z(tau)`; k is paired to dR1 at y. ITER141 says only edge `x-z` shrinks at lower endpoint, hence **q-degree** controls the lower singularity.
- `M_R1_chi1_dR2`: q is the dR2 leg paired to R1 at x; k is the dR2 leg paired to chi1 at `z(tau)`. ITER141 says only edge `z-y` shrinks at upper endpoint, hence **k-degree** controls the upper singularity.
- `G_R1_chi2_Gamma2_dR1`: q Gamma2 leg is paired to R1 at x and k Gamma2 leg to dR1 at y. Lower `x-z` uses **q-degree**; upper `z-y` uses **k-degree**.

## Frozen expected directional degrees to be recomputed

The already committed polynomial metadata suggest, but do not substitute for production recomputation:

- M1: q-degree 3, k-degree 5;
- M2: q-degree 5, k-degree 4;
- G1: q-degree 3, k-degree 4.

The gate must rebuild the exact polynomials and measure these directional degrees. It must also emit the highest homogeneous component in each actually singular momentum.

## Frozen sharp jet map

Using exact source suppression from ITER127/141:

- M1 lower: `N_sing = degree_q`, `s=0`;
- M2 upper: `N_sing = degree_k`, `s=1`;
- G1 lower: `N_sing = degree_q`, `s=0`;
- G1 upper: `N_sing = degree_k`, `s=1`.

Nonsingular opposite M endpoints remain `NO_AFFINE_PROPAGATOR_SINGULARITY_IN_CONNECTED_CROSS_CHANNEL` and receive no local-pole Taylor order.

## Frozen checks

1. Recompute all three exact D=4 connected-cross polynomials from the committed tensor implementations.
2. Verify the frozen edge-to-momentum incidence against ITER141.
3. Measure q/k directional degrees exactly.
4. Verify each shrinking-edge degree is <= the corresponding ITER139 max-line bound.
5. Emit nonzero highest homogeneous shrinking-edge component when the directional degree is nonzero.
6. Apply the ITER128/126 jet rule with exact endpoint suppression.
7. Keep denominator cancellation/contact reduction and actual residue evaluation outside this gate; those can only lower/remove a local noncontact contribution, not raise this derivative ceiling.

## Frozen classifications

- All exact degree/incidence/homogeneous/jet checks pass:
  `PASS_SCOPED_FIRST_MG_SHRINKING_EDGE_DERIVATIVE_JETS_CLOSED_LOCAL_RESIDUES_OPEN`.
- A shrinking-edge degree exceeds ITER139 global bound 5:
  `SCIENTIFIC_FAIL_ITER139_GLOBAL_BOUND_ON_ACTUAL_SINGULAR_EDGE`.
- Edge map or exact polynomial consistency fails:
  `SCIENTIFIC_FAIL_FIRST_MG_SHRINKING_EDGE_ALLOCATION`.
- Infrastructure failure before predicates are evaluated:
  `NUMERICAL_OR_INFRASTRUCTURE_FAIL`.

## Claim ceiling

A PASS supplies sharp D=4 derivative/Taylor-jet ceilings on the actually shrinking connected-cross propagators. It is not a pole residue, B1, noncancellation, B0, EDT comparison, bridge, new physics or candidate theory. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
