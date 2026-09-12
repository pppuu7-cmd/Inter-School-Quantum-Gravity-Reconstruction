# ITERATION 004 — Lorentzian EPRL Shared-Unitary Orientation Null

Date: 2026-09-12  
GitHub Actions run: `34664484242`  
Status: `SUCCESS / STRONG SUPPORT FOR RM-001 / CLAIM LOCKED`

## Question

Does relative orientation to a frozen source/train-derived retained projector carry independent composition-closure information in a pinned Lorentzian EPRL 4-simplex vertex, after operator spectra are held fixed?

## Construction

For each `Dl=1 -> Dl=0` partial-slice pair `(A1,A2)` and frozen rank-1 projector `P`, draw a Haar unitary `U` and transform both holdout operators by the same similarity:

`A1 -> U^† A1 U`,

`A2 -> U^† A2 U`.

`P` is not transformed.

This preserves the spectrum/singular values of each holdout and preserves their shared-similarity pair relation, while scrambling only their orientation relative to `P`.

The exhaustive map contains `640` cases per Immirzi parameter and `256` orientation-null draws per case.

## Preregistered decision rule

Natural support requires, for a gamma lane:

- median case median-null/source return improvement `> 1`;
- fraction of cases with majority of null draws worse than source orientation `> 0.5`.

Strong support uses the same median condition and requires the majority-null-worse fraction `> 0.6`.

Gravity-side refutation would require median improvement `<= 1` together with majority-null-worse fraction `<= 0.5`.

## Result

All three gamma lanes satisfy the preregistered **strong-support** rule.

| gamma | median case mean improvement | median case median improvement | cases majority-null-worse | mean null-worse fraction | strong support |
|---:|---:|---:|---:|---:|:---:|
| 0.5 | 2.9927x | 1.7498x | 0.6141 | 0.6094 | YES |
| 1.2 | 3.8244x | 4.0274x | 0.7016 | 0.6946 | YES |
| 2.0 | 3.8195x | 4.0264x | 0.7016 | 0.6947 | YES |

For the previously specified `open_axes=[0,1]`, `Dl1=001 -> Dl0=111` slice:

| gamma | fraction null worse | mean improvement | median improvement |
|---:|---:|---:|---:|
| 0.5 | 0.9375 | 8.4197x | 3.6821x |
| 1.2 | 0.9609 | 7.0638x | 7.0665x |
| 2.0 | 0.9609 | 7.1893x | 7.1407x |

## Interpretation

This is direct gravity-side support for RM-001 in a Lorentzian EPRL realization:

- keeping spectra fixed is not sufficient to preserve the source-aligned return behaviour;
- changing only relative orientation to the frozen retained sector produces a systematic degradation in closure performance;
- the effect survives a large change of Immirzi parameter from `0.5` to `2.0`;
- the effect is not universal over every partial slice, which is consistent with a structural orientation dependence rather than a trivial matrix-size artifact.

Together with the explicit 2x2 spectral-insufficiency theorem, the numerical result supports the statement that projected composition requires mixed retained/discarded-sector information beyond scalar spectrum/rank data.

## Scope

This strengthens RM-001 from two independent chains (causal-set SSEE and SU(2) BF) to include a direct Lorentzian EPRL gravity-side realization.

It does **not** establish:

- full spinfoam gluing or refinement;
- continuum or GR recovery;
- that the chosen train projector is a unique physical projector;
- a complete coarse-graining law;
- a new quantum-gravity theory;
- new physics.

## Next bridge step

The now-supported structural requirement is to formulate and falsify a projector-aware scale-transport bridge in which effective data contain both:

`P_s` — retained-sector orientation,

and

`mu_s` — scale/measure/normalization data.

The bridge must recover ordinary scalar running only in special cases where the mixed blocks are fixed or vanish, and it must be tested in at least one scale/refinement setting rather than only one-vertex shell change.
