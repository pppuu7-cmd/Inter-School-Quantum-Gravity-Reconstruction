# ITER129 source authority — projected graph numerator derivative census

Date: 2026-09-15
Gate: `ITER129_FIXED_GEODESIC_CURVATURE_PROJECTED_GRAPH_NUMERATOR_DERIVATIVE_CENSUS`
Preregistration: `prereg/ITER129_FIXED_GEODESIC_CURVATURE_PROJECTED_GRAPH_NUMERATOR_DERIVATIVE_CENSUS_2026-09-15.md`
Machine table: `analysis/iter129_graph_derivative_ceiling_table.json`
Validator: `analysis/iter129_validate_graph_derivative_ceiling_table.py`
Artifact: `iter129-graph-derivative-ceiling-table`

## 1. Finite graph-family census

The `O(kappa^4)` anchored fixed-geodesic curvature calculation is represented by 12 derivative-budget families:

- five F-sector ordinary curvature/interaction families;
- three M-sector first-order localization families;
- four G-sector second-order localization families.

They are the operator-level realizations of the finite ITER112 F/M/G census after the ITER125 topology reduction.

## 2. Frozen derivative budgets

The table uses source/operator derivative counts:

`R1,R2,R3: 2`,
`dR1,dR2: 3`,
`d2R1: 4`,
`Gamma1: 1`,
`Gamma2: 1 total`,
`dGamma1: 2`,
`S3,S4: 2`.

This yields total graph ceilings:

- F: `D_total=4,4,6,6,8`;
- M: `D_total=6,6,8`;
- G: `D_total=6,7,8,8`.

The maximum total derivative budget is therefore eight before tensor reduction.

## 3. Affine one-propagator ceilings

For line-connected local singularities, the largest partner allocations are:

- M families: `N1_max=4`;
- direct Gamma2 G family: `N1_max=4`;
- `Gamma1-dchi1` G family: `N1_max=4`;
- `dGamma1-chi1` G family: `N1_max=5`;
- `chi1 chi1 d2R1` G family: `N1_max=5`.

These are conservative maxima: exact contractions can route derivatives onto fixed external momenta or the other propagator and lower the local degree.

## 4. Line-line diagonal ceilings

The two nested G classes reproduce the expected distinction from ITER127:

- `Gamma1` against `Gamma1`: `N_line-line<=2`;
- `dGamma1` against `Gamma1`: `N_line-line<=3`.

The latter source term retains the inner `(tau-sigma)` suppression in the position-chi1 branch, so its superficial diagonal degree is reduced by one power when that specific contraction is used.

The `chi1 chi1` bulk-bulk family has `N_line-line<=2` and no source polynomial suppression on the diagonal.

## 5. Two-propagator raw ceilings

If two propagators approach the same affine singular stratum simultaneously, the deliberately conservative raw bound is

`m_raw <= 4 + D_total`.

Thus the family ceilings range from 8 to 12. The maximum `m_raw=12` occurs only in `D_total=8` families before source suppression, tensor identities, gauge cancellations and required subdivergence subtraction.

No `m_raw=12` row is asserted to possess an actual logarithmic residue.

## 6. Pure F sector has no affine jet budget

F-sector graphs contribute to the direct bulk/nonlocal coefficient and to renormalization, but they do not contain the geodesic affine singular integrations classified by ITER126. Their derivative ceilings are therefore recorded for loop numerator reduction but are not assigned endpoint/diagonal Taylor jets.

## 7. Tadpole control

Some routings of `R1-R3` or quartic interaction families contain massless local tadpoles that vanish in dimensional regularization when genuinely scaleless. This does not erase the entire operator family: other contractions/routings or counterterm roles must be treated separately.

## 8. What remains open

The table does not fix the exact per-propagator numerator after:

- tensor index contraction;
- integration by parts;
- de-Donder/BRST algebra;
- projection at `u=0,1/2`;
- subtraction of bulk/local subdivergences.

Therefore the result is a finite **ceiling census**, not an exact numerator reduction.

## Source classification

**`PASS_SCOPED_GRAPH_DERIVATIVE_CEILINGS_CLOSED_EXACT_TENSOR_ALLOCATION_OPEN`**

The interaction-specific local subtraction problem is finite. The largest raw two-propagator superficial power is bounded, and every affine one-propagator channel has a finite derivative ceiling. Exact numerator allocation remains a loop-algebra task.

## Highest-information successor

Do not immediately evaluate every graph. Use the ITER124 stopping objective and compute the projected UV numerator **only to the Taylor orders capable of feeding `1/epsilon` poles**. A successor should generate graph-local numerator jets symbolically at `u=0,1/2`, apply ITER127 source weights and discard terms whose affine order cannot reach the pole-controlling Taylor coefficient.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No derivative ceiling is a pole residue; no `B1`, noncancellation theorem, EDT fit, discrepancy, bridge or new physics follows.