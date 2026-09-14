# ITER111 source-discovery audit — post-2018 fixed-geodesic curvature correlator

Date: 2026-09-15
Gate: `ITER111_RETROSPECTIVE_FIXED_GEODESIC_CURVATURE_CORRELATOR_POST2018_SOURCE_DISCOVERY`
Protocol: `142580287fe3aa6c6def0a145f79d21b32887c06`
Retrospective validation credit: **0**

## Frozen target

A qualifying result requires a four-dimensional perturbative/low-energy quantum-gravity calculation of a curvature two-point function whose endpoint separation is fixed by the fluctuating metric geodesic distance/world function, with an explicit separated-point quantum result and renormalization/gauge treatment.

## Search result by source class

### 1. Fixed fluctuating geodesic distance + explicit one-loop calculation

**Located, but insertion is a matter scalar, not curvature.**

Markus Fröb, arXiv:1706.01891 / CQG 35, 035005 (2018), computes the one-loop graviton correction to a massless scalar-field two-point function at fixed geodesic distance. It includes geodesic-embedding renormalization and obtains a finite gauge-independent separated result with double logarithms.

This is the strongest methodology precedent but fails the curvature-insertion requirement.

`MATTER_CURVATURE_SWAP_CONTROL`: **TRIGGERS**.

### 2. Four-dimensional curvature correlator + explicit one-loop result

**Located, but separation is harmonic/master-coordinate relational distance, not fluctuating geodesic distance.**

Laiho & Ratliff, arXiv:2510.11888 / PRD 113, 106032 (2026), compute the diffeomorphism-invariant scalar-curvature correlator through one loop and find the universal noncontact `768 G^2/(pi^2 r^8)` tail. The relational localization is defined by harmonic metric-dependent master coordinates.

This fails the fixed-geodesic target by construction.

`MASTER_COORDINATE_GEODESIC_SWAP_CONTROL`: **TRIGGERS**.

### 3. Formal fixed-geodesic curvature correlator definitions

**Located, but no qualifying perturbative calculation.**

Modern talks/reviews on invariant observables and lattice quantum gravity explicitly write formal objects of the type

`< R(x) R(y) delta(d_g(x,y)^2-D^2) sqrt(g_x)sqrt(g_y) >`

or the corresponding integrated/shell-averaged curvature correlator at fixed geodesic distance. These sources establish that the target observable is standard and meaningful.

They do not provide the required four-dimensional one-loop curvature evaluation/renormalization.

`FORMAL_DEFINITION_CALCULATION_SWAP_CONTROL`: **PASS_CONTROL / NO PROMOTION**.

### 4. Explicit curvature correlators at fixed dynamical geodesic distance in lower-dimensional nonperturbative gravity

**Located, but wrong dimension/framework.**

Recent 2D Lorentzian/CDT work constructs nonperturbative curvature correlators at fixed geodesic distance, carefully distinguishing normalized and connected versions. This strengthens the observable semantics and shows that the geodesic-shell curvature construction remains an active modern research object.

It is not a four-dimensional perturbative low-energy curvature calculation.

`2D_4D_SWAP_CONTROL`: **TRIGGERS**.

### 5. World-function/geodesic-biscalar quantum-geometry literature

**Located, but no matching RR loop correlator.**

Post-2018 work on Synge's world function, van Vleck determinant, zero-point length and geodesic structure analyzes nonlocal geometric data and quantum-spacetime modifications. None of the located sources supplies the required four-dimensional perturbative `RR` correlator at fixed fluctuating geodesic distance.

## Discovery classification

**`DISCOVERY_SATURATED_NO_EXPLICIT_4D_PERTURBATIVE_FIXED_GEODESIC_CURVATURE_CORRELATOR_IN_FROZEN_SEARCH`**

The frozen surface contains all major neighboring ingredients separately:

- explicit fixed-geodesic one-loop method — matter scalar;
- explicit four-dimensional one-loop curvature correlator — master-coordinate relational separation;
- formal fixed-geodesic curvature observable — no loop evaluation;
- explicit geodesic curvature correlators — lower-dimensional nonperturbative gravity.

No located source joins all target predicates in one calculation.

## Consequence

The `-10` modern EDT geodesic-shell target versus the `-8` master-coordinate low-energy EFT tail cannot be adjudicated further by source discovery alone. A genuinely new calculation is required unless a source outside the frozen search surface is later identified.

The minimal original theory task is now sharply specified:

1. construct invariant scalar-curvature insertions at endpoints of a fluctuating geodesic;
2. include geodesic-coordinate fluctuations through the first noncontact order;
3. renormalize both curvature composites and the geodesic embedding;
4. compute the full separated `O(G^2)` coefficient and logarithms;
5. only then map to the normalized shell estimator used in modern EDT.

## Claim ceiling

This is scoped discovery saturation, not a global no-source theorem and not a physics no-go. Bridge credit remains **0**; candidate theory remains **UNFORMED / 0%**.