# ITER125 source authority — projected UV topology / master-integral census

Date: 2026-09-15
Gate: `ITER125_FIXED_GEODESIC_CURVATURE_PROJECTED_UV_TOPOLOGY_AND_MASTER_INTEGRAL_CENSUS`
Preregistration: `prereg/ITER125_FIXED_GEODESIC_CURVATURE_PROJECTED_UV_TOPOLOGY_AND_MASTER_INTEGRAL_CENSUS_2026-09-15.md`

## 1. Ordinary F-sector denominator topology

Treat the curvature insertions as composite external vertices and count only denominators that carry an independent loop momentum.

At `O(kappa^4)` the ordinary field sector contains the familiar one-loop two-point structures:

- graviton/ghost self-energy insertion between leading curvature vertices;
- `R_2-R_2` Gaussian contractions;
- `R_1-R_2` with one cubic gravitational interaction;
- `R_1-R_1` with two cubic interactions;
- quartic/tadpole variants and counterterm insertions.

After external/fixed-momentum propagators are factored, the nonvanishing loop denominators are of massless bubble type

`1/[p^2 (p+q)^2]`

with tensor numerator powers. Quartic massless tadpoles and analogous scaleless subgraphs vanish in dimensional regularization when no line separation flows through them.

A graph that visually contains three propagators can still have only two **loop-dependent** denominators: the third line may carry the fixed external momentum `q` and factor outside the loop integration.

Predicates A-C: **PASS — NO GENUINE BULK TRIANGLE/BOX MASTER REQUIRED**.

## 2. Curvature nonlinearities change numerators, not one-loop denominator topology

`R_1,R_2,R_3` add derivatives and multiple graviton legs at the composite endpoint. At the frozen two-point one-loop order they generate additional powers/contractions of `p`, `q` and `n`, but graph counting leaves at most one independent loop momentum.

Tensor numerators over the two loop-dependent massless denominators can be reduced to scalar bubble integrals plus polynomial/contact pieces. Possible evanescent tensor structures remain numerator/projector bookkeeping and do not create a new denominator topology.

Predicate I: **PASS_CONTROL**.

## 3. M-sector: one line parameter dresses the bubble topology

A first-order geodesic displacement `chi_1` contains one integration point on the line. In momentum representation it inserts a finite-segment phase/form factor into one of the contractions.

After momentum conservation is used, the loop-dependent core is still a two-propagator bubble, now dressed by a one-parameter phase such as

`exp(i tau p.l)`

or an equivalent finite-segment difference quotient.

A convenient scalar family is therefore

`B^(1)[N](q,l) = int_0^1 d tau w(tau) int d^d p exp(i tau p.l) N(p,q,n) / [p^2 (p+q)^2]`,

with polynomial numerator `N` reducible by tensor differentiation/projectors.

Predicate D: **PASS**.

## 4. G-sector: two-parameter bubble masters and line self-contractions

Second-order geodesic localization has two sources:

- `chi_1 chi_1`;
- `chi_2`, whose source construction contains ordered/nested line integrations.

Accordingly, at most two independent dimensionless line parameters are required at the operator level.

Two distinct scalar master types appear.

### G-bubble family

Products in which the two geodesic insertions participate in the same connected two-point loop reduce to a bubble denominator with two line parameters. Momentum conservation makes the loop-dependent phase depend on a linear combination/difference of those parameters, while external `q` phases are known factors.

Schematic family:

`B^(2)[N] = int d tau d sigma w(tau,sigma) int d^d p exp(i alpha(tau,sigma) p.l) N / [p^2 (p+q)^2]`.

### Line-line self-contraction family

Some pure geodesic terms contract two metric fields located on the line with each other while the curvature endpoints are connected by a fixed/external propagator. The loop/defect integral is then a **single massless propagator with nonzero line separation**,

`P^(2)[N] = int d tau d sigma w(tau,sigma) int d^d p exp(i (tau-sigma) p.l) N(p,n)/p^2`.

This is not a scaleless tadpole for `tau != sigma`; its UV singularity occurs in the coincidence region `tau -> sigma` and is precisely part of defect renormalization. Calling it a tadpole and discarding it would be wrong.

Predicate E: **PASS**.
`TADPOLE_NONZERO_CONTROL`: **TRIGGERS FOR LINE-SEPARATED SELF-CONTRACTIONS**.

## 5. No genuine triangle/box loop denominator is introduced by line integration

A line parameter is an integration over the position of a composite/nonlocal operator insertion. It is not an additional loop momentum.

At the frozen order, once fixed external propagators and line parameters are distinguished from independent loop momentum, no F/M/G graph requires three or four independent loop-momentum denominators of triangle/box type.

Thus geodesic complexity is carried by finite-segment parameter moments and defect coincidence limits, not by higher-point bulk loop topology.

Predicate F: **PASS_CONTROL**.
`LINE_PARAMETER_LOOP_TOPOLOGY_SWAP_CONTROL`: **PASS_CONTROL**.
`EXTERNAL_PROPAGATOR_TRIANGLE_SWAP_CONTROL`: **PASS_CONTROL**.

## 6. Counterterm insertions are a separate master category

Bulk, endpoint and line-defect counterterms can appear as tree-level insertions multiplied by pole/renormalized coefficients, or as subdivergence insertions inside the one-loop subtraction hierarchy.

A tree counterterm insertion is not a new loop master. Its exact finite-segment Fourier factor is already controlled by ITER123.

Predicate G: **PASS_CONTROL**.

## 7. Minimal scalar master-family census

For the projected `B_1` pole calculation, the finite master categories are:

### M0 — ordinary massless bubble

`B(q) = int d^d p /[p^2 (p+q)^2]`

plus tensor/numerator derivatives and raised/cancelled propagator powers reducible to the same family and contact/scaleless pieces.

### M1 — one-parameter phase-dressed bubble

`B^(1)` as above, generated by M-sector localization.

### M2 — two-parameter phase-dressed bubble

`B^(2)` as above, generated by `chi_2` / `chi_1 chi_1` connected contractions.

### M3 — one-propagator two-line self-contraction

`P^(2)` as above, with coincidence/endpoint singularities supplying defect UV poles.

### M4 — counterterm/projector insertions

No new loop denominator; known line form factors multiplying running/pole coefficients.

These are **families**, not five individual scalar numbers: different tensor derivatives and line weights must still be reduced within each family.

Predicate H: **PASS_FINITE_CENSUS**.

## 8. Relation to the fixed-geodesic matter precedent

The source scalar calculation is consistent with this census: after its tensor and line-parameter manipulations, the nonlocal one-loop content reduces to products of massless propagators (`G_0^2`) and renormalized one-scale distributions, while the severe geodesic divergences arise from line/endpoint coincidence structure rather than a new bulk triangle topology.

Curvature adds derivative numerators and composite mixing but no new loop-momentum count.

## 9. Target independence

No EDT exponent, amplitude or desired cancellation is used to prune a master family.

Predicate J: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_ONE_LOOP_BUBBLE_TOPOLOGY_PLUS_ONE_TWO_LINE_PARAMETER_MASTER_FAMILIES`**

This label includes the mandatory one-propagator line-line self-contraction family as a defect/line-parameter master; it does **not** mean every scalar master has two propagators.

No genuine triangle/box loop denominator is required at the frozen one-loop two-point order.

## Highest-information successor

Exploit the fact that UV poles of the phase-dressed families come from short-distance/coincidence regions in the line parameters. Preregister an **endpoint/coincidence asymptotic subtraction gate**: derive the pole part of M1–M3 from local small-parameter expansions, separating it from finite oscillatory/Bessel dependence. If successful, `B_1` may be computable from endpoint asymptotics without evaluating complete finite geodesic integrals.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No master integral is evaluated, no pole residue or `B_1` is obtained, no EDT fit, direct discrepancy, bridge or new physics follows.