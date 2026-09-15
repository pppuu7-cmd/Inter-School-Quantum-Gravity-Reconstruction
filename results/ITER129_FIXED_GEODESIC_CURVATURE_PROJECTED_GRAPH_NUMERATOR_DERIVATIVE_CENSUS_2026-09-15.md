# ITER129 terminal result — projected graph numerator derivative census

Date: 2026-09-15
Gate: `ITER129_FIXED_GEODESIC_CURVATURE_PROJECTED_GRAPH_NUMERATOR_DERIVATIVE_CENSUS`
Preregistration: `prereg/ITER129_FIXED_GEODESIC_CURVATURE_PROJECTED_GRAPH_NUMERATOR_DERIVATIVE_CENSUS_2026-09-15.md`
Source authority: `sources/ITER129_FIXED_GEODESIC_CURVATURE_PROJECTED_GRAPH_NUMERATOR_DERIVATIVE_CENSUS_2026-09-15.md`
Adversarial review: `results/ITER129_ADVERSARIAL_CRITIC_2026-09-15.md`
Machine table: `analysis/iter129_graph_derivative_ceiling_table.json`
Validator: `analysis/iter129_validate_graph_derivative_ceiling_table.py`
Artifact: `iter129-graph-derivative-ceiling-table`

## Terminal classification

**`PASS_SCOPED_GRAPH_DERIVATIVE_CEILINGS_CLOSED_EXACT_TENSOR_ALLOCATION_OPEN`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

The finite `O(kappa^4)` graph/operator census has 12 derivative-budget families:

- F: 5;
- M: 3;
- G: 4.

Total derivative ceilings are finite:

- F: `4,4,6,6,8`;
- M: `6,6,8`;
- G: `6,7,8,8`.

Thus `D_total<=8` before tensor reduction.

For affine one-propagator singular channels, `N1_max<=5` in the interaction/localization families. For a simultaneous raw two-propagator local product, the conservative superficial bound is

`m_raw <= 4+D_total <= 12`.

Exact ITER127 source suppression then lowers specific endpoint/diagonal powers before ITER126 residue extraction.

## Hard scope boundary

These are raw/conservative derivative ceilings. They do not supersede the corrected physical one-loop radial basis `G^2 l^-8[B0+B1 log]` and do not imply physical `l^-12` behavior.

Tensor contractions, integration by parts, external-momentum routing, Bianchi identities, gauge cancellation and subdivergence subtraction can all lower the actual local singular degree or eliminate a residue.

## Computational consequence

A brute-force finite integration of every graph is unnecessary for the binary `B1` question. The next implementation should:

1. generate projected graph numerators at `u=0` and `u=1/2`;
2. expand only around ITER127 singular strata;
3. retain only Taylor orders capable of feeding the ITER126 `1/epsilon` coefficient;
4. perform sector/forest subtraction for overlaps;
5. combine direct and defect-running pole data under the ITER124 RG contract.

## Exact successor

`ITER130_FIXED_GEODESIC_CURVATURE_POLE_RELEVANT_NUMERATOR_JET_GENERATOR`

Freeze a symbolic representation for the 12 graph families that outputs only pole-relevant local numerator jets rather than complete finite amplitudes. Start with the Gaussian/no-action M/G families, where field contractions are simplest, and use them as a validation subset before adding cubic-interaction graphs.

## Claim ceiling

No pole residue or `B1` value has been computed. No noncancellation theorem, EDT fit, direct discrepancy, bridge, new physics or candidate theory follows.