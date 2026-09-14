# ITER071 terminal result — FRG / CDT spectral-dimension observable identity authority

Date: 2026-09-14
Gate: `ITER071_FRG_CDT_SPECTRAL_DIMENSION_OBSERVABLE_IDENTITY_AUTHORITY`
Preregistration commit: `bd42843d2dbb6203b3d1513b079107499ce631d2`
Source-authority audit commit: `3582bcca11dcfa4eca279cc2b266213712de48b3`
Adversarial critic commit: `0e26ac63d1ea947c219394ee7cbcdeac6f32cafc`

## Terminal scientific classification

**`PASS_SCOPED / COMMON_DEFINITION_DIFFERENT_REALIZATION`**

Mandatory retained lock:

**`SAME_OBSERVABLE_POINTWISE_4D_COMPARATOR = NOT_YET_AUTHORIZED`**

Bridge credit: **0**.

## Question adjudicated

Do the frozen CDT and FRG/QEG sources define spectral dimension through sufficiently compatible operational objects that the two programmes can be said to measure the same observable, and can their running spectral dimensions already be compared pointwise at matched physical scale?

## Result

The first part passes; the stronger second part does not.

The common definition is source-qualified on both sides:

`diffusion/heat operator -> return probability -> D_s = -2 d log P / d log(diffusion duration)`.

This is a substantive cross-school commonality. Unlike the generic `composition` or `ordered evolution` kernels rejected as bridge evidence in ITER068-070, it is an explicitly defined observable functional with the same operational mathematical construction.

However, its realization remains typed and different:

### CDT realization

- diffusion is implemented as a discrete random walk on Euclideanized causal triangulations;
- the observable is averaged over sampled triangulations/configurations and starting points;
- the diffusion parameter is an integer random-walk duration in lattice units;
- short walks suffer odd/even lattice artifacts and long walks suffer finite-volume effects;
- the frozen 4D source does not calibrate diffusion duration to an absolute continuum physical length.

### QEG / FRG realization

- the return probability is a quantum expectation over metrics;
- the effective-average-action calculation represents the quantum spacetime using a scale-dependent family of effective metrics/Laplacians;
- diffusion time is fictitious and distinct from RG time;
- the RG resolution scale is attached to Laplacian eigenmodes (`k^2 = E_n`), while the heat kernel relates diffusion duration to the momentum modes that dominate the return probability;
- the detailed finite-scale curve retains effective-metric/truncation approximations away from the strongest fixed-point asymptotics.

## Frozen predicate results

- A — explicit diffusion object: **PASS_BOTH**.
- B — return probability and logarithmic spectral dimension: **PASS_BOTH**.
- C — diffusion target identified: **PASS_BOTH, TYPED DIFFERENCE RETAINED**.
- D — averaging procedure identified: **PASS_BOTH, TYPED DIFFERENCE RETAINED**.
- E — diffusion parameter operationally defined and separated from proper/RG time: **PASS_BOTH**.
- F — physical/RG/lattice scale map sufficient for pointwise frozen-4D comparison: **PARTIAL / NOT SUFFICIENT**.
- G — lattice/continuum, finite-size and approximation assumptions recorded: **PASS_SCOPED**.
- H — numerical coincidence withheld until authority audit: **PASS_CONTROL**.

The preregistered classification corresponding to this pattern is therefore exactly:

**`PASS_SCOPED_COMMON_DEFINITION_DIFFERENT_REALIZATION`**.

## Important positive result

ITER071 identifies the first cross-school commonality in this sequence that survives beyond a purely forgetful algebraic host:

**spectral dimension is source-qualified as a shared observable definition across CDT and QEG/FRG.**

This permits future comparison work to begin from an actually common measurement functional rather than from analogies between evolution or composition mechanisms.

The commonality is still not a bridge between microscopic theories. A common observable can be shared by inequivalent physical systems.

## Why the stronger comparator does not yet pass

The QEG sources provide an explicit relation between Laplacian mode resolution and RG scale. The frozen 4D CDT source provides diffusion duration in lattice steps and documents how it probes short versus long lattice distances, but it does not supply the absolute/continuum scale calibration required to match a CDT diffusion step range to a QEG physical/RG length range.

The 2011 QEG paper explicitly demonstrates a detailed comparison against a **3D** CDT data set from another source and says that an analogous 4D comparison would require detailed four-dimensional Monte Carlo data. That is evidence that the shared definition is operationally useful, but it does not close the frozen 4D scale-map requirement.

## Adversarial critic

The critic tried both directions:

1. demote the result to FAIL because ensemble averaging and effective-metric evaluation differ;
2. promote it to full comparator PASS because QEG literature already compares spectral-dimension curves to CDT.

Neither succeeds.

The averaging difference changes the realization but not the common return-probability/log-slope observable definition. Conversely, the published 3D comparison does not provide the missing frozen-4D physical scale calibration.

Critic verdict: **CONFIRMS researcher classification**.

## Structural consequence for ISQGR

The research programme now has a sharper hierarchy:

- `C_seq`, `C_tensor`, and `C_scale_flow` are different physical operation types;
- a common operation-level parent has not been established;
- nevertheless, distinct theories can possess a genuinely common **observable functional**.

This suggests that the most defensible cross-school route is currently observable-first rather than operation-first: establish same-observable authority, then test universality and scale matching without inferring microscopic equivalence from agreement alone.

## Downstream authorization

No numerical FRG/CDT value matching is authorized yet as bridge evidence.

The next gate should target the exact blocker exposed by predicate F:

**`PREREGISTER_ITER072_CDT_SPECTRAL_DIFFUSION_SCALE_CONTINUUM_AUTHORITY`**.

That gate should determine whether 4D CDT sources provide a source-defined lattice-spacing/physical-scale calibration for spectral diffusion, whether rescaling of `D_s(sigma)` across bare couplings can determine relative lattice spacing, and whether finite-size/discretization effects are controlled strongly enough to promote spectral dimension from a common definition to a physically scale-matched comparator.

## Claim ceiling

ITER071 does **not** establish:

- FRG/CDT microscopic equivalence;
- equality of their RG/evolution maps;
- shared continuum dynamics;
- universality of the numerical value `d_s ~ 2` across theories;
- `BRIDGE_DERIVED`;
- `UNIVERSAL_COMMON_PARENT_FOUND`;
- a candidate theory;
- new physics.

`CANDIDATE_THEORY = UNFORMED`

`THEORY_ESTABLISHED = 0%`

`BRIDGE_CREDIT = 0`