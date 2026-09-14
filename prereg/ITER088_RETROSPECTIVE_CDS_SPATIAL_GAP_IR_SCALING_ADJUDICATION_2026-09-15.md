# ITER088 retrospective protocol — CdS spatial-gap infrared scaling adjudication

Date: 2026-09-15
Gate: `ITER088_RETROSPECTIVE_CDS_SPATIAL_GAP_IR_SCALING_ADJUDICATION`

## Non-blind status

This gate is **not** a prospectively blind validation test.

While preparing a successor to ITER087, the published 2019 source arXiv `1903.00430` was inspected and its reported finite-size exponent became known before this protocol was committed. Therefore ITER088 may adjudicate source compatibility and sharpen the frontier, but it receives **zero prospective validation credit** regardless of outcome.

This explicit status prevents accidental retroactive preregistration.

## Question

Does the published low-lying spatial Laplacian spectrum in the four-dimensional CDT `C_dS` phase support the round-three-sphere infrared finite-size law

`lambda_n propto V_S^(-2/3)`

for fixed low mode number `n`, or does it exhibit a different source-measured effective scaling dimension?

## Frozen comparison target

The round-`S^3` hypothesis implied by the relative-scaling residue of ITER087 is

`lambda_n propto V_S^(-2/d_IR)` with `d_IR=3`.

For the lowest nonzero mode this gives

`lambda_1 propto V_S^(-2/3)`.

Because the published target result is already known, ITER088 does not test a newly generated prediction. It only asks whether the source evidence supports or rejects this specific round-`S^3` infrared spectral law in the accessible finite-regulator `C_dS` ensemble.

## Frozen sources

- arXiv `1903.00430` / Phys. Rev. D 99, 114506 (2019), *Running scales in causal dynamical triangulations*.
- arXiv `1804.02294`, earlier spatial Laplace-spectrum study, only as contextual/corroborating authority.
- ITER087 terminal record, only for the scaling hypothesis and its claim ceiling.

## Required predicates

A. The published simulation is in the `C_dS` phase at fixed bare couplings.

B. Slice volume `V_S` is explicitly defined and low eigenvalues are binned/averaged as functions of `V_S`.

C. The fit form `lambda_n = A_n V_S^(-2/d_eff)` is explicit.

D. The fitted `d_eff` is reported with enough source authority to compare against `d_IR=3`.

E. The fit quality and mode range are recorded; one mode cannot be selected post hoc.

F. Closing of the spectral gap as `V_S -> infinity` is kept distinct from the value of the effective infrared dimension.

G. The global four-dimensional de-Sitter volume profile is not used to override the independently measured spatial spectral exponent.

H. No FRG quantity is used to reinterpret a failed round-`S^3` scaling law.

## Interpretive controls

- `RETROSPECTIVE_VALIDATION_CREDIT_CONTROL`: no validation credit can be awarded.
- `GLOBAL_PROFILE_SPECTRUM_SWAP_CONTROL`: de-Sitter-like `N_3(t)` does not imply round-`S^3` Laplace spectrum.
- `GAP_CLOSURE_DIMENSION_CONTROL`: `lambda_1 -> 0` does not imply `d_eff=3`.
- `MODE_PICKING_CONTROL`: published low modes are considered as a family, not only the most favorable one.
- `FINITE_REGULATOR_CONTINUUM_CONTROL`: the measured finite-size exponent is not automatically the continuum-limit dimension.
- `FRG_RESCUE_CONTROL`: no FRG trajectory or regulator may be used to repair the CDT-only comparison.

## Retrospective classifications

- `SOURCE_SUPPORTS_ROUND_S3_IR_SCALING` if the source reports `d_eff` compatible with 3 across the low-mode finite-size fits.
- `SOURCE_REJECTS_ROUND_S3_IR_SCALING_ACCESSIBLE_CDS` if the source reports a stable low-mode exponent materially incompatible with 3 while the gap still closes.
- `SOURCE_INCONCLUSIVE_FOR_ROUND_S3_IR_SCALING` if fit/systematic information is insufficient to adjudicate.

## Claim ceiling

Even a rejection applies only to the accessible finite-regulator spatial spectral geometry of the published `C_dS` ensembles. It cannot reject the global de-Sitter minisuperspace description, prove the final CDT continuum infrared geometry, determine an FRG trajectory, create bridge credit or authorize a candidate theory.
