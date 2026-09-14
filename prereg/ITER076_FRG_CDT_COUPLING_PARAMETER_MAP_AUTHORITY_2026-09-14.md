# ITER076 preregistration — FRG/CDT coupling-parameter map authority

Date: 2026-09-14

## Frozen question

Does the frozen literature derive an explicit, non-forgetful map between CDT lattice/bare/effective gravitational parameters and FRG/QEG running dimensionless couplings, while preserving regulator, scale/time, measure and observable semantics?

## Frozen sources

- arXiv:1203.3591 — *Nonperturbative Quantum Gravity*.
- arXiv:1110.5224 — *Fractal space-times under the microscope: A Renormalization Group view on Monte Carlo data*.
- arXiv:0807.4481 — CDT semiclassical effective action / Newton-scale extraction.
- arXiv:1403.5940 — CDT reduced transfer-matrix effective action.
- arXiv:1202.2274 — QEG/FRG review and running couplings.

## PASS requirements

A scoped PASS requires a source-defined map with explicit domain/codomain and equations connecting at least one CDT parameter set such as `(kappa_0, Delta, a, G_eff/a^2, Lambda_eff a^2, transfer-action coefficients)` to FRG/QEG running couplings such as `(g_k=k^2 G_k, lambda_k=Lambda_k/k^2)` or an equivalent dimensionless set.

The map must state or derive:

1. scale identification and its validity range;
2. regulator/lattice dependence;
3. normalization/measure conventions;
4. which observables or effective-action coefficients fix the map;
5. whether it is bare, effective, renormalized, or continuum-limit matching;
6. uncertainty or scheme dependence where relevant.

## Mandatory failure controls

- `FIXED_POINT_LANGUAGE_CONTROL`: both frameworks discussing fixed points is not a parameter map.
- `SPECTRAL_FIT_CONTROL`: fitting spectral dimension curves is not a coupling map.
- `NEWTON_SYMBOL_CONTROL`: both using a symbol `G` does not establish equality of renormalized objects.
- `LATTICE_RG_SCALE_SWAP_CONTROL`: `a^{-1}=k` may not be imposed without source derivation.
- `DE_SITTER_COEFFICIENT_FIT_CONTROL`: shared de-Sitter/minisuperspace coefficients may not be retuned to force matching.
- `BARE_EFFECTIVE_SWAP_CONTROL`: CDT bare couplings may not be identified with effective/renormalized FRG couplings by name.
- `REGULATOR_ERASURE_CONTROL`: scheme/lattice dependence must remain explicit.

## Terminal classes

- `PASS_SCOPED_EXPLICIT_COUPLING_MAP_ESTABLISHED`
- `PASS_SCOPED_PARTIAL_PARAMETER_CORRESPONDENCE_ONLY`
- `SCOPED_BLOCKED_NO_EXPLICIT_COUPLING_MAP_AUTHORITY`
- `FAIL_SCOPED_PROPOSED_COUPLING_EQUIVALENCE_REJECTED`
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION`

Green CI is not scientific PASS. No post-result retuning or new bridge assumption is allowed.

Candidate theory remains `UNFORMED / 0%`; bridge credit remains zero unless a later constitution gate explicitly changes it.
