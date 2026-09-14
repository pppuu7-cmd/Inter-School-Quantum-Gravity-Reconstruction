# ITER076 source authority — FRG/CDT coupling-parameter map

Date: 2026-09-14
Preregistration: `75a2c52a4a03180cd562261d2dfd3aa30f6c19a7`
Workflow head: `b5fedb498b1663948097f8ac2b2a64b6e12245ad`
Authoritative run: `34895920464`

## Validated Actions provenance

All five frozen source lanes and aggregate completed technically successfully. Green CI is extraction success only.

- `1202.2274`: job `104149730963`, artifact `10368572248`, digest `sha256:15b9952fa1de6e2ea813a824e4dffd6c80bc196afe8b0b25d67821eaae0805c9`.
- `1403.5940`: job `104149731141`, artifact `10368672029`, digest `sha256:fdf790cdaa4411b2541f5f6f43b8fc4641122d1c7eff788f74b60c6d712ab5e3`.
- `0807.4481`: job `104149731172`, artifact `10368711087`, digest `sha256:022911562734f7b958437ebf7b46ff3e8cb23bf85405e1ba005421ec61c09c77`.
- `1203.3591`: job `104149731345`, artifact `10369460357`, digest `sha256:0472029e3000db6bcbae21ad1ca977efd8a7aaf1d975ef7bb92055be9d90f2c2`.
- `1110.5224`: job `104149731408`, artifact `10369395695`, digest `sha256:3bd9fbb992b5e128eb2052fd8e0d75330ed7a09e2889367af4433b121d9e1ad1`.
- aggregate: job `104149859894`, artifact `10369231191`, digest `sha256:0dd67edde30f399dea0c8a93dcad23578c15a1c16848bb55681c6cc793464327`.

Raw extracted exact-PDF artifacts were consumed against the frozen predicates.

## Source audit

### CDT side

The CDT stack source-qualifies bare lattice parameters `(kappa_0, Delta)` and reduced effective parameters. In particular, the CDT review/source gives a relation of the reconstructed coefficient `k_1` and lattice geometry factors to Newton's constant in cutoff units, schematically `G/a^2`, and explicitly treats `k_1` as a function of the CDT bare couplings. It also makes clear that continuum scaling requires varying bare couplings and volume toward a critical surface; this is not itself an FRG coupling map.

### FRG/QEG side

The FRG stack source-qualifies dimensionless running couplings such as `g_k = G_k k^(d-2)` and `lambda_k = Lambda_k k^(-2)`, RG trajectories, beta functions and fixed-point structure.

### Direct cross-framework evidence

arXiv:1110.5224 performs a direct comparison to CDT spectral-dimension Monte-Carlo data, but the FRG/QEG trajectory parameters are **selected by fitting the target CDT spectral curve**. The source constructs RG trajectories from initial `(g_0, lambda_0)` and determines best-fit values by minimizing squared residuals against `D_s^CDT(T)`.

This is a real cross-framework phenomenological fit. Under the prospective ITER076 rules it does **not** constitute a coupling-parameter map, because the FRG couplings are not derived from CDT `(kappa_0, Delta, a, k_1, G/a^2, ...)`; they are chosen from the target observable.

The broader review literature discusses possible common fixed-point/continuum-limit interpretations and similarities, but the frozen stack does not supply equations transporting CDT bare/effective couplings to FRG dimensionless running couplings with regulator/lattice, scale and observable semantics preserved.

## Frozen-control audit

- `FIXED_POINT_LANGUAGE_CONTROL`: passes; qualitative fixed-point analogy not promoted.
- `SPECTRAL_FIT_CONTROL`: **triggered**; the strongest direct trajectory selection is target-fitted spectral data.
- `NEWTON_SYMBOL_CONTROL`: passes; CDT effective `G/a^2` is not silently equated to `g_k`.
- `LATTICE_RG_SCALE_SWAP_CONTROL`: passes; no unsupported `a^{-1}=k` identification.
- `DE_SITTER_COEFFICIENT_FIT_CONTROL`: passes; no retuning performed.
- `BARE_EFFECTIVE_SWAP_CONTROL`: passes.
- `REGULATOR_ERASURE_CONTROL`: passes.

## Classification

**`SCOPED_BLOCKED_NO_EXPLICIT_COUPLING_MAP_AUTHORITY`**

Positive residuals retained:

- `CDT_INTERNAL_G_OVER_A2_EFFECTIVE_CALIBRATION = QUALIFIED_SCOPED`
- `FRG_DIMENSIONLESS_RUNNING_COUPLINGS = QUALIFIED`
- `CROSS_FRAMEWORK_SPECTRAL_TRAJECTORY_FIT = QUALIFIED_TARGET_FITTED`

Missing object:

**`SOURCE_DERIVED_CDT_TO_FRG_COUPLING_MAP = NOT_ESTABLISHED`**.

This is source-scoped BLOCKED, not a scientific failure of either framework and not evidence for a new QG theory.
