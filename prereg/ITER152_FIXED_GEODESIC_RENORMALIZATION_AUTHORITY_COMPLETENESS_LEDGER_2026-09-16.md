# ITER152 preregistration — fixed-geodesic renormalization authority completeness ledger

Date: 2026-09-16
Upstream authoritative main HEAD: `4d723952375750ff94c2c1f48e4ebaeeec92c440`

## Scientific objective

Resolve the ITER151 blocker at maximum information gain without inventing contact distributions, counterterm residues, line-defect mixing coefficients, or a physical `B1_total`.

The gate asks a narrower question than ITER151: **which exact renormalization-authority slots needed by ITER124 are already source-closed, and which remain genuinely missing after the completed ITER117–151 chain?**

This is a completeness/authority gate, not a numerical pole calculation.

## Frozen authority slots

The gate must classify the following slots using only repository objects that predate ITER152 plus their exact source-qualified classifications/claim locks:

1. finite curvature line/endpoint counterterm basis;
2. local endpoint/coincidence pole-subtraction algorithm;
3. exact source-qualified `chi1/chi2` affine weights and singular strata;
4. first-M/G general-d numerator/contact-support manifest and raw nonlocal two-propagator pole sector;
5. actual distributional pullback/renormalized value for the seven ITER151 one-propagator endpoint contacts in `d=4-2 epsilon`;
6. bulk/local-composite subdivergence subtraction map and values needed for the current first-M/G graphs;
7. divergent endpoint-counterterm coefficients for the relevant curvature/geodesic endpoint basis;
8. full four-operator line-defect pole/mixing matrix for `[int R, int R_nn, int Box_perp R, int Box_perp R_nn]`, including the pole information required by ITER124;
9. mapping of the seven ITER151 contacts into the renormalized endpoint/line basis after subtraction;
10. actual terminal ITER124 outputs: `B1_direct`, `beta_defect`, `B1_defect`, `B1_total`, `raw_and_subtracted_1_over_epsilon2_coefficients`, `raw_and_subtracted_1_over_epsilon_coefficients`.

## Frozen evidence rules

- A source-closed slot requires an exact authoritative repository object with a compatible PASS-scoped classification or a machine object whose semantics are explicit.
- A method/prototype is not an actual residue or mixing coefficient.
- A specification naming required outputs is not an authority containing their actual values.
- Absence of a required authority is `BLOCKED`, not a physical `FAIL` and not evidence that the contribution is zero.
- ITER152 files may not satisfy their own authority scan.
- No EDT datum, desired sign, desired cancellation, or target `B1` value may enter any decision.

## Decision rule

- `PASS_SCOPED_FULL_RENORMALIZATION_AUTHORITY_AVAILABLE` only if all ten slots are source-faithfully closed and the six ITER124 terminal outputs are present as actual non-null values in a terminal PASS authority object.
- `BLOCKED_SOURCE_AUTHORITY_INCOMPLETE_EXACT_MISSING_SLOTS_FROZEN` if the upstream chain is internally consistent but one or more required authority slots remain open.
- `SCIENTIFIC_FAIL_ITER152_AUTHORITY_LEDGER_INCONSISTENT` only if the frozen evidence rules, upstream classifications, or ledger exhaustiveness checks are violated.

The gate must exit successfully on a scientifically valid `BLOCKED` result. It must not reinterpret missing authority as zero.

## Reproducibility requirement

The implementation must write a deterministic JSON ledger, be rerun in the same clean GitHub Actions job, and produce byte-identical output. The workflow must use full git history so the frozen upstream HEAD ancestry can be verified.

## Claim ceiling

Authority-completeness localization only. No new contact pole, counterterm coefficient, mixing residue, `B1_total`, noncancellation theorem, gauge/BRST conclusion, EDT bridge, new physics, or candidate theory may be claimed by ITER152.