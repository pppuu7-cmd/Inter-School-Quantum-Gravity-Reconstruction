# ITER127 preregistration — fixed-geodesic chi1/chi2 projected singular-strata authority

Date: 2026-09-15
Gate: `ITER127_FIXED_GEODESIC_CHI1_CHI2_PROJECTED_SINGULAR_STRATA_AUTHORITY`

## Motivation frozen before source extraction

ITER126 authorizes local endpoint/coincidence pole extraction once the exact affine-parameter weights of the fixed-geodesic perturbation are known. The remaining source-sensitive input is the first- and second-order geodesic embedding expansion used by the frozen fixed-geodesic one-loop formalism.

ITER127 forbids reconstructing these weights from memory or from a generic geodesic equation alone. It extracts them from the exact arXiv source package and only then builds the singular-strata table.

## Frozen source

- arXiv:1706.01891 / published 2018 fixed-geodesic perturbative calculation.

The exact arXiv source archive SHA256 and TeX file hashes must be preserved.

## Frozen extraction procedure

1. Download the exact current arXiv source package for `1706.01891`.
2. Preserve archive SHA256.
3. Recursively inventory TeX files and SHA256 hashes.
4. Locate the equation environments defining the perturbative geodesic embedding, especially first- and second-order corrections conventionally denoted by `chi_1`, `chi_2` or equivalent notation.
5. Preserve only short equation-centered snippets needed to identify integration limits/weights and initial-data terms; do not copy large prose sections.
6. Record equation/file locations and the exact source conventions for affine parameter, tangent/initial conditions and metric expansion.

## Required scientific predicates

A. Source-explicit first-order geodesic correction is recovered, including its affine integration kernel and initial-data term.

B. Source-explicit second-order correction is recovered, including all nested/ordered line integrations required at that order.

C. Confirm or reject the ITER125 structural claim that `chi_1` contains at most one independent line parameter and `chi_2` at most two.

D. Record polynomial/endpoint weights that can soften or enhance `tau -> 0,1` and `tau -> sigma` singularities.

E. Combine only the **weight/power information** with ITER122 curvature projectors; do not import matter-scalar numerical residues.

F. Produce a singular-strata table for M/G sectors with columns:

- source term/class;
- number of line parameters;
- local singular stratum;
- polynomial suppression order from the geodesic kernel;
- curvature/projector derivative order still to be applied;
- whether ITER126 local subtraction can determine the pole.

G. Initial-tangent/vierbein normalization terms must be kept separate from bulk line-integral terms.

H. No `B_1` or EDT target may be inferred from the source extraction itself.

## Frozen classifications

- `PASS_SCOPED_EXACT_CHI1_CHI2_WEIGHTS_SOURCE_QUALIFIED_SINGULAR_TABLE_CLOSED` if A-H pass.
- `PASS_SCOPED_EXACT_CHI1_CHI2_SOURCE_QUALIFIED_CURVATURE_WEIGHT_TABLE_OPEN` if A-C/G pass but D-F require additional algebra.
- `BLOCKED_SOURCE_AUTHORITY` if the exact geodesic equations cannot be recovered from the frozen source.
- `INFRASTRUCTURE_FAIL` only for source transport/extraction failure.

## Controls

- `MEMORY_RECONSTRUCTION_CONTROL`
- `GENERIC_GEODESIC_SOURCE_EQUATION_SWAP_CONTROL`
- `INITIAL_TANGENT_LINE_KERNEL_SWAP_CONTROL`
- `MATTER_RESIDUE_CURVATURE_RESIDUE_CONTROL`
- `TARGET_WEIGHT_SELECTION_CONTROL`

## Claim ceiling

A PASS only source-qualifies the actual geodesic weights and singular-strata inputs. It does not compute a curvature pole residue, `B_1`, noncancellation, EDT fit, bridge, new physics or candidate theory.