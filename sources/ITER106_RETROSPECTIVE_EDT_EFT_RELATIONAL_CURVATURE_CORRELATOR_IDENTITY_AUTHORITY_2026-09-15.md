# ITER106 source authority — EDT ↔ low-energy EFT relational scalar-curvature correlator

Date: 2026-09-15
Gate: `ITER106_RETROSPECTIVE_EDT_EFT_RELATIONAL_CURVATURE_CORRELATOR_IDENTITY_AUTHORITY`
Protocol: `79006728921007dd339844487483995020c2c868`
Retrospective validation credit: **0**

## 1. The local scalar-curvature field is common up to affine Regge normalization

The 1995 four-dimensional EDT construction localizes Regge curvature on triangles. If `n_triangle` four-simplices meet at a triangle, the deficit angle is

`delta_triangle = 2 pi - n_triangle theta`,

and the local scalar curvature averaged over the dual volume associated with that hinge is therefore affine in `1/n_triangle`:

`R_Regge(triangle) = A/n_triangle + B`

for fixed equilateral simplex geometry. The paper consequently uses `1/n_triangle` as its convenient local curvature variable, dropping an overall factor and additive constant.

For a connected covariance defined with the same distance-conditioned one-point prescription, an affine change `R -> A R+B` changes only the overall connected normalization by `A^2`; the additive constant cancels. Thus the EDT field is source-typed to local Regge scalar curvature for exponent/shape questions.

The 2026 EFT correlator uses the diffeomorphism-invariant relational scalar curvature `R(X)`.

Predicate A: **PASS_SCOPED_COMMON_SCALAR_CURVATURE_FIELD**.
`REGGE_AFFINE_NORMALIZATION_CONTROL`: **PASS_CONTROL**.

## 2. EDT uses dynamical geodesic/graph-distance conditioning

For each triangulation the EDT paper defines a distance between curvature-carrying triangles through the minimal number of local neighbor steps. Correlators at integer distance `d` are conditional pair averages over all triangle pairs satisfying that configuration-dependent distance.

Schematically,

`<OO>(d) = < [sum_xy O_x O_y 1_{d(x,y)=d}] / [sum_xy 1_{d(x,y)=d}] >_ensemble`.

The denominator is part of the observable: the measured object is a normalized conditional expectation at fixed dynamical distance, not an unnormalized shell integral.

Predicates C-D: **PASS_SOURCE_TYPING**.
`CONDITIONAL_SHELL_UNNORMALIZED_SWAP_CONTROL`: **PASS_CONTROL**.

## 3. EFT separation is relational/master-coordinate separation, not source-defined geodesic distance

The 2026 EFT construction restores diffeomorphism invariance by promoting source and sink locations to field-dependent relational/master coordinates. The final Euclidean curvature correlator away from contact is expressed as a function of the source-sink separation `r=|X-Y|` in that relational frame.

At the calculated order,

`<R(X) R(Y)>_EFT = 768 G^2/(pi^2 r^8)`

for nonzero Euclidean separation, with analytic momentum-space pieces contributing only contact terms.

This `r` is a gauge-invariant relational-coordinate separation. The frozen EFT source does **not** identify it with the fluctuating metric geodesic distance used by EDT. The coordinate corrections needed for gauge invariance are not a proof that `|X-Y|=d_g(X,Y)` configuration by configuration.

Predicate B: **NO DIRECT GEODESIC MAP**.
`MASTER_COORDINATE_GEODESIC_DISTANCE_SWAP_CONTROL`: **TRIGGERS**.

## 4. Connectedness prescriptions differ nontrivially in fluctuating geometry

In the EDT ensemble the naive subtraction

`<RR>(d) - <R>^2`

does not approach zero as expected at large `d`, because the conditioning variable `d_g` itself fluctuates with the geometry and correlates with local observables. de Bakker and Smit therefore introduce a distance-dependent one-point, often described as the `curvature-to-nothing` correlator `<R>(d)`, and define the connected quantity by subtracting its square.

Later reviews emphasize that this prescription can differ significantly from more conventional connected correlators, especially at short distance.

The EFT result is instead the standard gauge-invariant relational two-point calculation around flat space. Its curvature one-point vanishes in the perturbative background, while local analytic pieces are contact terms; the noncontact result is the quoted `r^-8` term.

No frozen source derives equality between the EDT distance-conditioned connected subtraction and the EFT relational connected correlator.

Predicate E: **DIFFERENT CONNECTEDNESS REALIZATION / MAP OPEN**.
`DISTANCE_DEPENDENT_CONNECTED_SUBTRACTION_CONTROL`: **TRIGGERS**.

## 5. Contact terms are cleanly separated only on the EFT side

The EFT one-loop momentum-space curvature correlator contains local analytic terms. On Fourier transformation these become delta functions and derivatives thereof and therefore vanish for nonzero source-sink separation. The universal noncontact term is `768 G^2/(pi^2 r^8)`.

EDT measurements are at finite integer graph/geodesic separation with lattice-scale contact/discretization structure. Dropping EFT contact terms is legitimate only for the continuum nonzero-separation observable; it does not authorize using the first few EDT lattice shells as continuum noncontact data.

Predicate F: **PASS_CONTROL / NONZERO-SEPARATION ONLY**.
`CONTACT_TERM_CONTROL`: **PASS_CONTROL**.

## 6. Absolute amplitude comparison is not authorized

A direct amplitude comparison would require at least:

- `d -> r/a` or an equivalent physical-distance calibration for the old EDT ensembles;
- the exact curvature normalization converting `1/n_triangle` to dimensionful `R`;
- Newton's constant `G` in the same lattice units;
- finite-volume and shell-pair normalization corrections;
- an identified regime in which the EFT long-distance expansion applies.

The frozen historical EDT source does not provide this complete package.

Predicate G: **OPEN / AMPLITUDE COMPARATOR NOT AUTHORIZED**.

## 7. Historical EDT power law is not a controlled low-energy continuum test

The 1995/1996 EDT studies report power-law curvature correlations in the elongated phase and near the transition; the proceedings summary states that near the transition the fitted power is consistent with `4`.

However, subsequent larger-volume work on the same original equilateral 4D EDT model found clear first-order transition evidence. A first-order transition does not supply the standard diverging-correlation-length continuum-limit mechanism expected for a universal lattice definition of the long-distance EFT.

Therefore the historical exponent cannot be promoted to a continuum-GR prediction or used to reject the EFT `r^-8` law.

Predicate H: **PASS_CONTROL / CONTINUUM STATUS BLOCKS NUMERICAL THEORY TEST**.
`LATTICE_CONTINUUM_REGIME_CONTROL`: **TRIGGERS**.

## 8. Retrospective exponent lock

The qualitative old-EDT exponent was known before the ITER106 protocol. It receives **zero prospective validation credit**. It cannot be used to retune the EFT observable, distance definition, connected subtraction or fit window.

Predicate I: **PASS_CONTROL; CREDIT=0**.

## Source classification

**`PASS_SCOPED_COMMON_SCALAR_CURVATURE_TWO_POINT_TARGET_DIFFERENT_RELATIONAL_REALIZATION`**

The two frameworks genuinely share a local scalar-curvature field and a two-point-correlation target. That is stronger than a name analogy. But the actual observables are not yet the same connected correlator:

- EDT conditions on fluctuating geodesic/graph distance and normalizes by shell-pair counts;
- EFT uses relational/master-coordinate source-sink separation;
- EDT subtracts a distance-dependent one-point square;
- EFT gives a standard relational noncontact connected result around flat space.

Consequently the historical EDT `~d^-4` statement and EFT `~r^-8` prediction are **not directly exponent-comparable** under current authority.

## Highest-information successor

Two routes are admissible:

1. derive, in continuum perturbation theory, the curvature correlator **conditioned on physical geodesic distance** and with the same normalized shell-pair/connected prescription used by EDT; or
2. identify a modern 4D lattice-gravity measurement formulated directly in a relational coordinate/separation scheme compatible with the 2026 EFT observable.

The first route is analytically cleaner because it asks how much the exponent/connectedness changes when the separation observable itself fluctuates.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No direct conflict between exponents, no validation/falsification of low-energy EFT by the 1995 EDT data, no continuum EDT claim, no shared fixed point, no `BRIDGE_DERIVED`, no new physics follows.