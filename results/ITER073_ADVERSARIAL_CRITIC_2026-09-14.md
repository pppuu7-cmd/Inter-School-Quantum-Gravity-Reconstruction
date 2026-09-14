# ITER073 adversarial critic — FRG/QEG ↔ CDT spectral physical-scale crosswalk

Date: 2026-09-14
Preregistration commit: `8082e08b2b5349b53b5ffbf20a4676a2e57bf859`
Source-authority audit: `dc604f6881f81fb12d4e1f6aab5ae62b0f75251c`

## Target

Attempt to falsify or promote:

`BLOCKED_INDEPENDENT_PHYSICAL_SCALE_NORMALIZATION`.

## Attack 1 — Combine `a_abs` with `sigma` and declare `T_CDT = a_abs^2 sigma`

This is the strongest promotion attempt. ITER072 establishes the relative squared scaling and a conditional absolute lattice-spacing estimate. But the frozen CDT source itself warns that translating the lattice spectral result into dimensionful continuum quantities requires a nontrivial dimensional transmutation; its continuum ansatz retains an unspecified order-one constant.

Moreover the random walk is on the dual four-simplex adjacency graph, while `a_abs` is extracted from the effective spacetime/simplex geometry. The exact center-to-center diffusion normalization and anisotropy dependence are not frozen as an absolute identity.

Thus one may write a dimensional ansatz `T_CDT proportional_to a_abs^2 sigma`, but ITER073 requires the proportionality to be source-qualified before absolute pointwise matching.

**Verdict: block survives.**

## Attack 2 — The unknown constant cancels because spectral dimension is a logarithmic derivative

A constant rescaling of diffusion time does cancel from a plateau value and preserves the shape under a horizontal translation in `log T`. But ITER073 asks for a **physical-scale** comparator: the position of crossovers relative to `l_Pl`, not only plateau values, is exactly what must be fixed.

An unknown multiplicative constant therefore matters materially for pointwise scale matching even though it does not change an asymptotic spectral dimension.

**Verdict: block survives.**

## Attack 3 — In QEG just set `k = 1/sqrt(T)`

This is not source-faithful in the quantum regimes. QEG's return probability contains `exp[-p^2 F(p^2) T]`. In power-law regimes the typical walk displacement scales as `T^(1/(2+delta))`, with `D_w=2+delta`. The fixed-point regime has `D_w=4`, not 2.

The QEG source does identify `k^2=E_n` for a Laplacian eigenmode, but the heat-kernel parameter samples a spectrum of modes. A universal `k=1/sqrt(T)` substitution erases the running operator and anomalous walk behavior.

**Verdict: control rejects the promotion.**

## Attack 4 — QEG and CDT can both use Planck units, so normalization is independent

Using the same unit name does not imply the same operational resolution. CDT's `a_abs/l_Pl` estimate is conditional on a semiclassical de Sitter/minisuperspace matching. QEG's Planck normalization belongs to an RG trajectory and effective metric family. The frozen sources do not supply an independent mapping from the sampled CDT ensemble to a specific 4D QEG trajectory before using `D_s` itself.

**Verdict: common units are necessary but not sufficient.**

## Attack 5 — The 2011 QEG/CDT direct fit proves the bridge empirically

It proves something important but weaker: a QEG spectral curve can reproduce the reliable **3D** CDT spectral data at approximately percent-level accuracy after the QEG trajectory's initial conditions are fitted to that data.

ITER073 prospectively forbids treating this as an independent physical-scale calibration because the target observable selects the comparator trajectory. The paper itself says the analogous 4D comparison would require detailed 4D Monte Carlo data.

**Verdict: strong representational compatibility retained; independent 4D bridge not established.**

## Attack 6 — Fit circularity is acceptable because all parameter estimation uses data

Parameter estimation is not inherently circular. The issue is the logical role assigned to it. If a QEG trajectory is inferred from `D_s^CDT(T)` and then the agreement of that same `D_s` is cited as independent evidence that the theories share the physical scale map, the evidence is reused.

The fit can be used predictively only on held-out observables, held-out scale regions, or independently calibrated quantities.

**Verdict: circularity control is scientifically material.**

## Attack 7 — Spectral dimension itself already defines the physical scale

No. Spectral dimension is a return-probability logarithmic slope. Two systems can share `D_s` while having different Hausdorff and walk dimensions. The QEG source explicitly notes that if nonclassical `D_s` agrees between CDT and QEG, their `D_w` need not agree because the microscopic Hausdorff structures differ.

Thus `D_s` cannot self-calibrate the physical diffusion distance without additional structure.

**Verdict: block strengthened.**

## Attack 8 — Classify as `FAIL_SCOPED_SCALE_CROSSWALK_REJECTED`

Too strong. There is no contradiction preventing a future physical crosswalk. The frozen stack already supplies several required pieces, and the missing normalization/4D independent trajectory objects could in principle be added by new measurements or source-defined calibration. This is missing authority, not a no-go theorem.

**Verdict: BLOCKED rather than FAIL.**

## Critic verdict

**CONFIRMS `BLOCKED_INDEPENDENT_PHYSICAL_SCALE_NORMALIZATION`.**

Durable factorization of the blocker:

1. `CDT_ABSOLUTE_DIFFUSION_NORMALIZATION`: incomplete beyond relative `a^2` scaling / dimensional ansatz;
2. `CDT_4D_WALK_DISTANCE_AUTHORITY`: not comparator-grade in the frozen stack;
3. `QEG_4D_TRAJECTORY_NORMALIZATION_FOR_CDT_ENSEMBLE`: not independently fixed;
4. `PUBLISHED_DIRECT_MATCH`: high-quality but 3D and target-fitted;
5. `MUTUAL_RELIABILITY_WINDOW_AT_SAME_PHYSICAL_SCALE`: cannot be established before 1-3.

## Highest-information successor

The cheapest next question is not another `D_s` curve fit. It is whether 4D CDT supplies an independent walk-distance / Hausdorff / diffusion-radius observable that fixes how physical displacement grows with diffusion duration in the same ensembles used for spectral dimension.

Recommended next gate:

`PREREGISTER_ITER074_CDT_4D_WALK_DISTANCE_DIFFUSION_NORMALIZATION_AUTHORITY`.

If that object exists, it can close or sharply constrain the unknown CDT diffusion normalization without using FRG. If it does not exist, the pointwise physical-resolution route is source-blocked and attention should shift to other common observables.