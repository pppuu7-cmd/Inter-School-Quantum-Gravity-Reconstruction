# ITER124 preregistration — fixed-geodesic curvature projected RG/pole calculation specification

Date: 2026-09-15
Gate: `ITER124_FIXED_GEODESIC_CURVATURE_PROJECTED_RG_POLE_CALCULATION_SPEC`

## Motivation

ITER112–123 reduce the missing `O(G^2)` fixed-geodesic scalar-curvature problem to a finite renormalized calculation with:

- closed F/M/G localization classes;
- corrected noncontact radial basis `G^2 l^-8[B_0+B_1 L]`;
- finite curvature-specific line/endpoint counterterm basis;
- two genuine line-defect directions after field-redefinition quotient;
- exact two-point general-`d` projector for their pole residues.

ITER124 freezes the calculation contract required to determine `B_1` without yet evaluating the loop integrals.

## Frozen regularization / kinematics

- dimensional regularization `d=4-2 epsilon`;
- flat Euclidean background;
- fixed geodesic segment of physical length `l`;
- external nonzero momentum `Q=q^2`;
- projector kinematics `u=(q.n)^2/Q` evaluated at `u=0` and `u=1/2`, away from line-form-factor zeros;
- de-Donder gauge for the primary symbolic reduction, with a required independent gauge/BRST consistency check before a physical coefficient is accepted.

## Frozen renormalization sectors

### F — ordinary field/curvature sector

Include all `O(kappa^4)` curvature/composite diagrams, ghosts, cubic/quartic action insertions and standard bulk gravitational EFT counterterms required by ITER112.

### M — mixed first-order geodesic sector

Include every `chi_1` / line-localization contribution at the frozen order, including interaction-dressed pieces and endpoint mixing.

### G — pure second-order geodesic sector

Include `chi_2`, `chi_1 chi_1` and associated second-order localization terms.

### Endpoint/local composite sector

Retain the finite ITER118 endpoint basis through dimension four for subdivergence and contact renormalization. Endpoint-local pieces may be removed from the separated coefficient only after their contact nature is established in the renormalized sum.

### Line-defect sector

Retain the ITER118 line basis during renormalization. After consistent field redefinition of action+observable, quotient the redundant `int R`, `int R_nn` physical matching directions as in ITER120, while keeping them as invariance checks. The genuine representatives are

`J_R=int ds Box_perp R`,
`J_S=int ds Box_perp R_nn`

(or the equivalent trace/traceless basis).

## Required subtraction order

A. Generate the unrenormalized F/M/G pole amplitudes in general `d`.

B. Subtract standard bulk/ghost/composite subdivergences before interpreting defect poles.

C. Add endpoint and geodesic-embedding counterterms required by lower-order subgraphs.

D. Renormalize the line-defect mixing matrix, retaining both simple and higher poles required by consistency.

E. Only after A-D, separate polynomial/contact terms from the noncontact line-dependent pole structures.

F. Project the remaining genuine-defect divergence using the general-`d` two-point projector of ITER123; do not set `d=4` or isotropically average `u` before pole extraction.

## Required RG outputs

The calculation must report separately:

1. `B1_direct`: explicit noncontact logarithmic contribution from the renormalized F/M/G loop structures;
2. `beta_defect`: projected beta/pole data of the genuine line-defect couplings;
3. `B1_defect`: contribution induced by defect running acting on the lower-order/finite defect insertion kernels;
4. `B1_total = B1_direct + B1_defect` after all redundant-sector and gauge checks;
5. coefficients of `1/epsilon^2` and `1/epsilon` before and after subdivergence subtraction as consistency data.

The calculation must not identify `B1_total` with a raw highest pole of any single diagram.

## Consistency checks

- cancellation of nonphysical gauge-parameter dependence in the complete observable or an equivalent BRST identity;
- invariance of `B1_total` under the ITER120 local metric field-redefinition redistribution;
- exact trace/traceless decomposition of ITER122;
- equality of residue extraction performed from the full angular expression and the ITER123 two-point projector on a validation subset;
- cancellation/consistency of higher poles according to the renormalization hierarchy;
- no dependence on EDT target values.

## Stopping rules

### If `B1_total` is proven nonzero

Stop the noncancellation branch. By ITER116, the `O(G^2)` separated fixed-geodesic curvature correlator is then not identically zero and has engineering form `l^-8` with a logarithmic correction. A finite `B_0` calculation is not needed merely to answer the binary noncancellation question.

### If `B1_total = 0` exactly

Proceed to a dedicated finite-constant calculation for `B_0`; a zero log coefficient does not imply a zero `O(G^2)` correlator.

### If residual gauge/field-redefinition dependence remains

Do not interpret the coefficient physically; reopen the missing counterterm/mixing sector.

## Frozen classifications

- `PASS_SCOPED_PROJECTED_RG_POLE_CALCULATION_SPEC_CLOSED` if the finite sectors, subtraction order, projector and stopping rules above are internally complete.
- `BLOCKED_RENORMALIZATION_SPEC_INCOMPLETE` if a source-required sector cannot be placed in the subtraction/projector workflow.

## Claim ceiling

This gate is a calculation specification, not a pole evaluation. It does not determine `B_1`, prove noncancellation, authorize an EDT fit, establish a direct EDT/EFT discrepancy, bridge, new physics or candidate theory.