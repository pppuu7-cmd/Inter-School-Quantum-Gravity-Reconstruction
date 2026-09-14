# ITER075 preregistration — FRG/CDT volume-profile and effective-action observable authority

Date: 2026-09-14

## Frozen question

Do 4D CDT semiclassical volume-profile / reduced effective-action observables and FRG/QEG effective-background / effective-action objects admit a source-defined, non-forgetful typed correspondence that preserves domain, time/scale semantics, measure/normalization, dynamics and observable meaning?

This gate is authority-first. It does **not** assume that a shared de-Sitter or minisuperspace functional form is a physical bridge.

## Frozen source stack

CDT:

1. arXiv:0807.4481 — *The Nonperturbative Quantum de Sitter Universe*.
2. arXiv:1403.5940 — *The effective action in 4-dim CDT. The transfer matrix approach*.

FRG/QEG:

3. arXiv:1412.0468 — *Towards a C-function in 4D quantum gravity* (de-Sitter background / EAA trajectory object).
4. arXiv:2203.08003 — *The Spectral Geometry of de Sitter Space in Asymptotic Safety* (scale-dependent effective de-Sitter geometry).

The exact PDFs above are frozen before extraction. Additional literature may only be used later as an explicitly preregistered follow-up authority gate; it may not silently modify this verdict.

## Predicates

### A — CDT observable/action definition

PASS only if the frozen CDT sources explicitly define the measured/reconstructed spatial-volume profile and/or reduced effective transfer-matrix/action object, including its state variable and discrete proper-time role.

### B — FRG effective object definition

PASS only if the frozen FRG sources explicitly define the relevant EAA/effective-background geometry object and its dependence on RG scale `k`, background/dynamical metric structure, and running couplings.

### C — domain/codomain compatibility

PASS only if there is a source-defined map between the CDT reduced state/history object and the FRG effective field/background object. Mere similarity after minisuperspace reduction is insufficient.

### D — time/scale semantics

PASS only if a source explicitly identifies or derives CDT discrete proper time and FRG RG scale in the compared construction. A post-hoc `t <-> k^{-1}` or similar substitution is forbidden.

### E — measure/normalization preservation

PASS only if the mapping preserves or derives the CDT state-sum/transfer normalization and the FRG functional-integral/EAA regulator structure rather than erasing them.

### F — dynamical/effective-action equivalence

PASS only if the source stack establishes more than shared Einstein-Hilbert/de-Sitter/minisuperspace functional form: coefficients, variables, boundary conditions and operational meaning must be mapped or derived.

### G — observable correspondence

PASS only if observables on both sides are source-defined counterparts under the same mapping, not merely quantities with similar names or dimensions.

### H — regulator/reduction robustness

Any positive common structure must survive explicit bookkeeping of CDT lattice regulator/reduced-volume projection and FRG cutoff/background dependence. Erasing either structure triggers failure.

## Mandatory failure controls

- `DE_SITTER_SHAPE_IDENTITY_CONTROL`: same cosine/cos^3/de-Sitter shape alone is not bridge evidence.
- `MINISUPERSPACE_FORM_CONTROL`: same reduced Einstein-Hilbert/minisuperspace action form alone is not bridge evidence.
- `RG_TIME_PROPER_TIME_SWAP_CONTROL`: no `k`/RG time substitution for CDT proper time without source derivation.
- `EAA_MONTE_CARLO_ACTION_SWAP_CONTROL`: no identification of EAA with reconstructed CDT effective action by name alone.
- `REGULATOR_ERASURE_CONTROL`: FRG regulator/background structure and CDT lattice/state-sum measure must remain explicit.
- `FULL_REDUCED_STATE_SWAP_CONTROL`: reduced volume transfer matrix may not be promoted to the full triangulation-state object.
- `COEFFICIENT_RETUNING_CONTROL`: no post-result fitting/retuning to manufacture agreement.
- `OBSERVABLE_ERASURE_CONTROL`: comparison cannot discard the observables that operationally define each object.

## Frozen classifications

Possible terminal outcomes:

- `PASS_SCOPED_TYPED_EFFECTIVE_OBSERVABLE_MAP_ESTABLISHED`
- `PASS_SCOPED_COMMON_FUNCTIONAL_FORM_ONLY`
- `FAIL_SCOPED_PHYSICAL_EFFECTIVE_ACTION_EQUIVALENCE_REJECTED`
- `SCOPED_BLOCKED_INSUFFICIENT_SOURCE_AUTHORITY`
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION`

A green CI run is never scientific PASS.

## Claim ceiling

Even the strongest PASS can only establish a scoped typed common-structure candidate. It cannot establish `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, `ALL_KNOWN_SCHOOLS_FAIL`, a candidate action, or a universal parent theory.

Candidate theory remains `UNFORMED / 0%`.
