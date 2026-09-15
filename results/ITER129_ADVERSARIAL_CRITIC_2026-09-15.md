# ITER129 adversarial critic — graph numerator derivative ceilings

Date: 2026-09-15
Gate: `ITER129_FIXED_GEODESIC_CURVATURE_PROJECTED_GRAPH_NUMERATOR_DERIVATIVE_CENSUS`
Source authority: `sources/ITER129_FIXED_GEODESIC_CURVATURE_PROJECTED_GRAPH_NUMERATOR_DERIVATIVE_CENSUS_2026-09-15.md`

## Attack 1 — total derivative count fixes the exact local singular degree

Rejected. Derivatives can land on fixed external momenta, different propagators, or cancel after tensor identities. `D_total` is only a ceiling. ITER129 explicitly separates it from exact per-propagator allocation.

## Attack 2 — the raw two-propagator bound m=4+D_total should be used as the subtraction order directly

Too conservative for implementation. It is safe as an upper bound, but the actual graph should first be projected/tensor-reduced so derivatives that cannot act on the singular pair are removed. The successor should generate only pole-relevant local jets.

## Attack 3 — quartic/tadpole families can be deleted completely

Rejected. A particular scaleless routing can vanish in DR, but the operator family can still participate through other contractions or counterterm/subdivergence bookkeeping.

## Attack 4 — the M/G family list misses arbitrary higher localization orders

At fixed `O(kappa^4)`, endpoint expansion needs at most `chi2` and `chi1 chi1`; higher `chi_n` enter at higher perturbative order. ITER112/127 close this localization order.

## Attack 5 — the D_total=8 ceiling proves a very high physical short-distance power

Rejected. It is raw numerator power before propagator denominators, source suppression, renormalization and cancellations. The physical separated one-loop radial basis remains the corrected ITER114 `l^-8[B0+B1 log]` form.

## Critic verdict

**CONFIRMS `PASS_SCOPED_GRAPH_DERIVATIVE_CEILINGS_CLOSED_EXACT_TENSOR_ALLOCATION_OPEN`.**

The next calculation should be pole-targeted symbolic jet generation, not brute-force full finite integration.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.