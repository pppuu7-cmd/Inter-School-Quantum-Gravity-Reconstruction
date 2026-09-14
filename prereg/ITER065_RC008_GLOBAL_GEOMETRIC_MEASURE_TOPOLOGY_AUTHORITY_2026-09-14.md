# ITER065 — RC008 global geometric measure / topology authority gate

Date frozen: 2026-09-14

## Motivation
ITER064 terminal manual audit invalidated crossing credit because (i) the positive crossing endpoint was outside the converged regime and (ii) ITER062B multiplied the one-hypercuboid `Delta_FP` locally without a source-qualified derivation of the global glued-complex reduced measure. No amplitude crossing is authorized here.

## Frozen scope
Restricted Euclidean/Riemannian EPRL-FK quantum-cuboid / hypercuboid sector only. Candidate theory remains UNFORMED. Bridge credit is forbidden.

Primary-source authority set is frozen prospectively to:
- arXiv:1508.07961 — quantum-cuboid restricted state sum / asymptotic vertex baseline;
- arXiv:1605.07649 — first hypercuboidal RG/coarse-fine calculation;
- arXiv:1701.02311 — detailed hypercuboidal renormalization / embedding-map treatment;
- arXiv:1804.00023 — symmetry-restricted coarse/fine observable extension.

No source may be added after observing ITER065 results without a new preregistration.

## Independent lanes
1. `coarse2`: two temporal hypercuboids; construct the reduced geometric embedding from one interior time split to the concatenated local six-area tuples. Compute the pullback Gram determinant and an independent finite-difference Jacobian.
2. `fine32`: frozen 2x2x2x4 refinement coordinates (three spatial cuts + three temporal cuts); construct the concatenated local-area embedding for all 32 cells. Compute analytic and finite-difference Jacobians and pullback Gram determinant.
3. `sentinel`: compare the old product-of-local one-cell `Delta_FP` prescription to `sqrt(det(J^T J))` only as an adversarial geometric-pullback sentinel. This comparison cannot define the physical spin-foam measure by itself.
4. `source_authority`: exact-PDF text extraction for the four frozen arXiv sources, preserving snippets around `Faddeev`, `Jacobian`, `measure`, `embedding`, `coarse`, `fine`, `gluing`, `constraint`, and `geometricity`. Automated keyword hits are never a scientific PASS; they only nominate exact passages for terminal manual equation audit.

## Frozen numerical/topological predicates
For `coarse2` and `fine32`, across frozen deterministic sample points:
- analytic vs central-finite-difference Jacobian max relative discrepancy <= 2e-5;
- pullback Jacobian rank equals reduced coordinate dimension at every sample;
- Gram log-determinant is finite at every sample.
Failure is `NUMERICAL_OR_IMPLEMENTATION_FAIL`, not a physical scientific FAIL.

For `sentinel`, report the coefficient of variation of `product(local Delta_FP)/sqrt(det(J^T J))` over frozen points. A nonconstant ratio (`CV > 1e-2`) is only evidence that the old local-product prescription is not identical up to normalization to this geometric embedding-pullback sentinel. It does not by itself determine the correct global quantum measure.

## Source-authority classification
- `SOURCE_AUTHORITY_CANDIDATE_PRESENT`: at least one frozen primary source yields exact extracted passages containing a measure/Jacobian/Faddeev-Popov term in the same local window as coarse/fine/gluing/embedding/constraint language. Requires manual equation-level audit before any gate credit.
- `SCOPED_BLOCKED_NO_EXPLICIT_GLOBAL_MEASURE_AUTHORITY`: all four PDFs are successfully extracted and no such passage is present.
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION`: one or more frozen PDFs cannot be retrieved/extracted. No scientific conclusion.

A green workflow is not a scientific PASS. The aggregate must preserve per-lane raw JSON/text artifacts.

## Claim locks
No `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`, fixed-point claim, corrected crossing claim, or candidate action/Hamiltonian/equations may be made from ITER065.

## Next-gate rule
Only after terminal source-authority classification plus manual equation audit may a corrected global measure implementation be preregistered. If authority remains blocked, RC008 numerical crossing work remains blocked and the programme must move to another independent PHASE_1 front.