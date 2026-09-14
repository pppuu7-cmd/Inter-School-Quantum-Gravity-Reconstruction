# ITER071 preregistration — FRG / CDT spectral-dimension observable identity authority

Date: 2026-09-14
Gate: `ITER071_FRG_CDT_SPECTRAL_DIMENSION_OBSERVABLE_IDENTITY_AUTHORITY`

## Motivation frozen before extraction

ITER070 rejected an operation-level identification between FRG `C_scale_flow` and CDT `C_seq`, retaining only a forgetful ordered-evolution kernel. The next higher-information route is therefore not to identify their evolution parameters, but to ask whether both programmes define the **same observable** closely enough for a cross-school comparison.

Spectral dimension is the cheapest candidate because both CDT and asymptotic-safety/QEG literature explicitly formulate diffusion/return-probability constructions and discuss dimensional flow. Numerical agreement or similar UV limits are not bridge evidence unless observable identity is established first.

## Frozen question

Do the frozen CDT and FRG/QEG sources define spectral dimension through sufficiently compatible operational objects that their reported scale dependence can be compared as the same observable, with an explicit map between diffusion parameter, Laplacian/diffusion operator, averaging procedure, geometry/effective metric and physical scale?

## Frozen sources

### CDT

- arXiv:hep-th/0505113 — J. Ambjorn, J. Jurkiewicz, R. Loll, *Spectral Dimension of the Universe*.

### FRG / asymptotic safety

- arXiv:hep-th/0508202 — O. Lauscher, M. Reuter, *Fractal Spacetime Structure in Asymptotically Safe Gravity*.
- arXiv:1110.5224 — M. Reuter, F. Saueressig, *Fractal space-times under the microscope: A Renormalization Group view on Monte Carlo data*.

The prior ITER067 and ITER069 authority records may be used only to enforce object typing and claim ceilings, not to fill missing spectral-dimension definitions.

## Required observable predicates

A. Each side explicitly defines a diffusion/heat kernel or discrete random-walk evolution.

B. Each side explicitly defines return probability and spectral dimension, including the derivative/log-slope convention.

C. The object on which diffusion occurs is identified: CDT triangulation/ensemble versus FRG/QEG effective geometry or scale-dependent metric/operator.

D. The averaging procedure is explicit enough to determine whether ensemble averaging, effective-metric evaluation or another expectation operation is being compared.

E. The diffusion parameter `sigma` (or equivalent) has an explicit operational meaning on both sides; no direct identification with CDT proper time or FRG RG time is permitted unless source-defined.

F. The map from diffusion scale to physical/RG/lattice scale is explicit enough to compare running `d_s` without silently equating diffusion time, lattice steps, momentum cutoff and proper time.

G. Continuum/lattice and finite-size/discretization assumptions are recorded and cannot be erased.

H. Reported numerical values or UV limits are not compared until A-G have been adjudicated.

## Classification

- `PASS_SCOPED_SAME_OBSERVABLE_COMPARATOR_AUTHORIZED` only if A-E are source-qualified on both sides and F-G admit an explicit scoped comparison map with recorded uncertainties/assumptions.
- `PASS_SCOPED_COMMON_DEFINITION_DIFFERENT_REALIZATION` if A-E establish the same abstract spectral-dimension definition but F-G prevent direct pointwise scale/value comparison. This authorizes definition-level commonality only, not numerical bridge credit.
- `FAIL_SCOPED_OBSERVABLE_IDENTITY_REJECTED` if the diffusion/return-probability objects are physically incompatible even at the definition level.
- `BLOCKED_SOURCE_AUTHORITY` if the frozen stack does not expose the required definitions well enough to adjudicate.
- `INFRASTRUCTURE_FAIL` only for source extraction/transport failure.

## Frozen controls

- `DIFFUSION_TIME_RG_TIME_SWAP_CONTROL`: diffusion parameter cannot be equated with FRG RG time.
- `DIFFUSION_TIME_CDT_PROPER_TIME_SWAP_CONTROL`: diffusion parameter cannot be equated with CDT proper time.
- `LATTICE_CONTINUUM_SCALE_SWAP_CONTROL`: diffusion steps/lattice units cannot be identified with continuum physical length without a source-defined map.
- `ENSEMBLE_EFFECTIVE_METRIC_SWAP_CONTROL`: CDT ensemble averaging cannot be replaced by evaluation on an FRG effective metric without accounting for the change of object.
- `NUMERICAL_COINCIDENCE_CONTROL`: similar values such as a short-distance dimension near 2 cannot establish observable identity.
- `FINITE_SIZE_ERASURE_CONTROL`: CDT finite-volume/discretization effects cannot be erased.
- `TRUNCATION_SCHEME_ERASURE_CONTROL`: FRG truncation/RG-improvement/scheme assumptions cannot be erased where relevant.

## Claim ceiling

A PASS may authorize a same-observable comparator or a common definition only. It cannot establish FRG/CDT equivalence, a shared microscopic theory, `BRIDGE_DERIVED`, `UNIVERSAL_COMMON_PARENT_FOUND`, new physics or a candidate QG theory.

Predicates, classifications and controls are frozen before exact-source extraction.