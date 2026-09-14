# ITER070 terminal result — FRG / CDT scale-time type discrimination

Date: 2026-09-14
Gate: `ITER070_FRG_CDT_SCALE_TIME_TYPE_DISCRIMINATION`
Preregistration commit: `13dc381f81cb7f2f14e3dac7a099448d4d576ae2`
Researcher audit commit: `c600d83bb7231b0d53d6719aafe3335c043007f9`
Adversarial critic commit: `4bf2dc7c44af35f16f9305038bb9726b53b9d8ca`

## Terminal scientific classification

**`FAIL_SCOPED / FRG_CDT_TYPE_EQUIVALENCE_REJECTED`**

Retained positive sub-result:

**`COMMON_ORDERED_EVOLUTION_KERNEL_ONLY`**

Bridge credit: **0**.

## Adjudicated question

Can source-qualified FRG `C_scale_flow` and CDT `C_seq` be related by a non-forgetful typed invariant or explicit embedding that preserves domain/codomain, parameter meaning, dynamics, measure/regulator structure, gauge/quotient structure and observables?

## Answer

No, within the frozen ITER070 authority stack.

Both objects form parameter-ordered families and therefore share a weak abstract evolution schema. That commonality ceases to be non-forgetful once the physical type information is restored.

## Decisive mismatches

1. **Parameter semantics** — FRG `k`/RG time is a cutoff/coarse-graining parameter in theory space; CDT proper time labels the source-defined temporal slicing of triangulated histories.
2. **Domain/codomain** — FRG evolves scale-indexed effective actions/couplings; CDT composes amplitudes between full spatial-triangulation states.
3. **Finite composition** — CDT has an exact regulated finite semigroup/gluing law; the frozen FRG stack does not establish the corresponding exact finite source-defined physical composition law.
4. **Generator** — Wetterich/beta-function flow and the CDT transfer/Hamiltonian package have different domains and meanings; no typed intertwiner is source-defined.
5. **Measure/regulator** — FRG regulator/background/gauge structure is not the CDT action/automorphism state-sum measure.
6. **Observables** — theory-space effective-action flow is not source-defined state/amplitude transport of the CDT type.

## Controls

All preregistered failure controls triggered in the intended direction:

- RG time was not swapped with proper time;
- regulator structure was not erased;
- full CDT states were not replaced by reduced volume states;
- fixed points were not promoted to refinement objects;
- observable meaning was retained;
- regulator kernels were not identified with state-sum weights;
- differential FRG flow was not promoted to CDT's exact finite semigroup law.

## Adversarial result

The critic tested stronger commonizations through semigroup language, emergent-time reinterpretation, generic marginalization/path-integration, common generator categories and fixed-point universality. All operation-level rescues either forgot mandatory physical structure or introduced a new bridge assumption.

Critic verdict: **CONFIRMS researcher FAIL_SCOPED**.

## Structural consequence

The current operation atlas is now empirically constrained to retain distinct types:

- `C_seq` — CDT temporal/state-sum composition;
- `C_tensor` — HaPPY tensor-contraction/isometric encoding;
- `C_scale_flow` — FRG regulator-dependent theory-space scale flow.

The typed multi-operation form of H0 remains viable only as a search for explicit morphisms or shared observables between these distinct operation classes. It no longer supports identification by common words such as `evolution`, `composition`, `integration`, or `coarse graining`.

## Highest-information successor

ITER070 exposes a more promising orthogonal route: compare **same-observable structures** rather than evolution parameters.

The cheapest candidate is the scale-dependent / spectral-dimension sector because both CDT and asymptotic-safety/FRG programmes have literature using diffusion/spectral-dimension constructions. However no bridge credit may be taken from numerical similarity alone; the operational definitions, diffusion operators, scale identification, ensembles/effective metrics, limits and uncertainties must first be source-qualified as the same observable or explicitly shown to differ.

Recommended next gate:

**`PREREGISTER_ITER071_FRG_CDT_SPECTRAL_DIMENSION_OBSERVABLE_IDENTITY_AUTHORITY`**

The gate should first test observable identity/typing, before comparing reported numerical values or UV limits.

## Claim ceiling

This result does not establish failure of FRG or CDT, a no-go theorem for all cross-school bridges, a universal parent, new physics or a candidate QG theory.

`CANDIDATE_THEORY = UNFORMED`

`THEORY_ESTABLISHED = 0%`

`BRIDGE_CREDIT = 0`
