# ITER071 source authority — FRG / CDT spectral dimension observable identity

Date: 2026-09-14
Gate: `ITER071_FRG_CDT_SPECTRAL_DIMENSION_OBSERVABLE_IDENTITY_AUTHORITY`
Preregistration commit: `bd42843d2dbb6203b3d1513b079107499ce631d2`

## Frozen sources audited

### CDT
- arXiv:hep-th/0505113 — Ambjorn, Jurkiewicz, Loll, *Spectral Dimension of the Universe*.

### FRG / QEG
- arXiv:hep-th/0508202 — Lauscher, Reuter, *Fractal Spacetime Structure in Asymptotically Safe Gravity*.
- arXiv:1110.5224 — Reuter, Saueressig, *Fractal space-times under the microscope: A Renormalization Group view on Monte Carlo data*.

## Equation-level crosswalk

### CDT object

The CDT source first states the continuum heat-kernel definition on a Euclidean geometry,

`partial_sigma K_g = Delta_g K_g`,

with fictitious diffusion time `sigma`, and defines the normalized return probability

`P_g(sigma) = V^{-1} int sqrt(g) K_g(x,x;sigma)`.

It then defines the quantum/ensemble average over Euclideanized geometries at fixed volume and carries the construction to the piecewise-linear CDT ensemble. The scale-dependent spectral dimension is

`D_S(sigma) = -2 d log P_N(sigma) / d log sigma`.

In the simulation, `sigma` becomes an integer number of random-walk diffusion steps. The source explicitly distinguishes this fictitious diffusion parameter from CDT proper time. The measurement is averaged over statistically independent triangulations and independent starting points. The source also records the short-`sigma` odd/even lattice artifact, finite-volume limitations, the finite discrete four-volume, and the restricted fit window used in the quoted 4D result.

### QEG / FRG object

The QEG sources use the same heat-kernel construction on a smooth Euclidean metric,

`partial_T K_g = Delta_g K_g`

(up to sign convention for the positive Laplacian), the same normalized heat-trace / return probability, and the same logarithmic-slope definition

`D_s(T) = -2 d log P(T) / d log T`.

For QEG, the classical-metric return probability is promoted to an expectation value over microscopic metrics. The effective-average-action method represents the result through a scale-dependent family of effective metrics `<g_{mu nu}>_k` and their Laplacians. The RG scale is not identified with diffusion time. Instead, source-defined mode resolution provides `k^2 = E_n` for a Laplacian eigenmode; in a flat reference approximation this becomes `k ~= |p|`, while diffusion time selects momentum scales through the heat kernel, with relevant ranges satisfying parametrically `T ~ 1/p^2`.

The 2011 source explicitly formulates a generalized `D_s(T)` intended for comparison to discrete approaches and performs such a comparison against 3D CDT Monte Carlo data in an intermediate window chosen to suppress short-walk discretization and long-walk compactness effects. It also states that the analogous 4D comparison would require access to detailed four-dimensional Monte Carlo data.

## Frozen predicate adjudication

| Predicate | Verdict | Authority result |
| --- | --- | --- |
| A. Explicit diffusion/heat-kernel or random-walk evolution | `PASS_BOTH` | CDT defines continuum diffusion and a discrete random walk on triangulations; QEG defines the heat kernel and its effective-metric implementation. |
| B. Return probability and spectral dimension/log slope | `PASS_BOTH` | Both use the normalized return probability and `-2 d log P / d log(diffusion parameter)`. Sign conventions for the Laplacian do not change the observable. |
| C. Diffusion target object identified | `PASS_BOTH_TYPED_DIFFERENCE` | CDT: Euclideanized causal triangulations / their ensemble. QEG: microscopic metric expectation represented using a family of scale-dependent effective metrics/operators. |
| D. Averaging procedure explicit | `PASS_BOTH_TYPED_DIFFERENCE` | CDT performs ensemble/configuration and starting-point averaging; QEG defines a quantum expectation over metrics and evaluates it via the effective average action. The difference is retained rather than erased. |
| E. Diffusion parameter operational meaning | `PASS_BOTH` | `sigma`/`T` is fictitious diffusion duration / random-walk length. It is neither CDT proper time nor FRG RG time. |
| F. Diffusion scale -> physical/RG/lattice scale map sufficient for pointwise 4D comparison | `PARTIAL_NOT_SUFFICIENT` | QEG gives the mode-resolution map `k^2=E_n` and heat-kernel relation between `T` and resolved momenta. The frozen 4D CDT source gives diffusion steps and lattice-scale behavior, but no absolute continuum physical-length calibration for `sigma`. The 2011 QEG paper performs a 3D comparison but explicitly notes that a 4D comparison requires detailed 4D Monte Carlo data not supplied by the frozen 4D source. |
| G. Continuum/lattice/finite-size assumptions recorded | `PASS_SCOPED` | CDT records finite volume, lattice odd/even effects and fit windows. QEG records the effective-metric/flat-space and, away from the fixed-point limit, truncation assumptions. |
| H. Numerical coincidence withheld until authority audit | `PASS_CONTROL` | The near-2 short-distance values are not used to infer equivalence or bridge identity. |

## Observable-identity result

The two programmes do share a nontrivial observable definition. At the abstract level the common object is:

`geometry/quantum-geometry object -> heat kernel/random walk -> normalized return probability -> logarithmic slope D_s`.

This is stronger than the forgetful operation-level commonality rejected in ITER070 because the measured functional is explicitly the same spectral observable, not merely an ordered evolution parameter.

However, the realized objects and scale maps remain different:

- CDT diffusion is sampled on discrete, Euclideanized triangulations and then ensemble averaged;
- QEG diffusion is formulated as a metric expectation and represented through scale-dependent effective metrics/operators;
- the frozen 4D CDT source lacks the physical scale calibration needed to identify a given integer diffusion duration with a QEG physical/RG resolution scale.

Therefore a source-qualified definition-level comparison is authorized, but a pointwise 4D physical-scale/value comparator is not.

## Classification supported by authority

**`PASS_SCOPED_COMMON_DEFINITION_DIFFERENT_REALIZATION`**

Explicit non-promotion:

`SAME_OBSERVABLE_POINTWISE_4D_COMPARATOR = NOT_YET_AUTHORIZED`.

## Controls

- `DIFFUSION_TIME_RG_TIME_SWAP_CONTROL`: passed; no such identification is made.
- `DIFFUSION_TIME_CDT_PROPER_TIME_SWAP_CONTROL`: passed; CDT itself calls diffusion time fictitious and separately discusses proper time.
- `LATTICE_CONTINUUM_SCALE_SWAP_CONTROL`: blocks stronger PASS because the frozen 4D source lacks an absolute diffusion-step to physical-length calibration.
- `ENSEMBLE_EFFECTIVE_METRIC_SWAP_CONTROL`: passed by retaining the distinct averaging constructions.
- `NUMERICAL_COINCIDENCE_CONTROL`: passed; `d_s ~ 2` is not used as bridge evidence.
- `FINITE_SIZE_ERASURE_CONTROL`: passed; finite-size and discreteness windows remain explicit.
- `TRUNCATION_SCHEME_ERASURE_CONTROL`: passed; finite-scale QEG results retain approximation/truncation qualifiers.

## Claim ceiling

This authority result establishes a common observable definition only. It does not establish FRG/CDT equivalence, common microscopic dynamics, common RG flow, a shared continuum limit, `BRIDGE_DERIVED`, `UNIVERSAL_COMMON_PARENT_FOUND`, new physics, or a candidate theory.