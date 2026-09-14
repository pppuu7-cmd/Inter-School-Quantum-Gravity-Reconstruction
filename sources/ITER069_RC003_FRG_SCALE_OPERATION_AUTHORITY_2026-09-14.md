# ITER069 source authority — RC003 FRG scale operation

Date: 2026-09-14
Gate: `ITER069_RC003_FRG_SCALE_COMPOSITION_AUTHORITY`
Preregistration commit: `c938f74feed0e1aae729cdafea05a3d6e5d70227`
Production/extraction commit: `89aab44905ebc8406bf65711c384a39576c9ad5b`
Authoritative CI run: `34889707865`

## Scope

This record manually adjudicates the preregistered authority predicates against the frozen source stack. The successful CI run is transport/evidence preservation only and is not itself scientific PASS evidence.

Frozen sources:

1. F. Saueressig, *The Functional Renormalization Group in Quantum Gravity*, arXiv:2302.14152.
2. A. Eichhorn, *Asymptotically safe quantum gravity and its phenomenology — a review*, arXiv:2606.21522.
3. C. Laporte, A. D. Pereira, F. Saueressig, J. Wang, *Scalar-Tensor theories within Asymptotic Safety*, arXiv:2110.09566.

## Source-qualified object

The frozen stack defines the effective average action `Gamma_k` and its functional renormalization-group flow through the Wetterich equation. In schematic notation,

`k d_k Gamma_k = 1/2 Tr[(Gamma_k^(2) + R_k)^(-1) k d_k R_k]`

with the usual gravity-sector extensions for gauge/ghost contributions. The scale `k` is an infrared/coarse-graining cutoff scale; `R_k` suppresses modes relative to that scale. The flow is a trajectory in theory space / coupling space, not a source-defined evolution of physical spacetime states.

Saueressig (2302.14152) explicitly places `Gamma_k` in theory space, interprets beta functions as a vector field whose integral curves are RG trajectories, and presents the background-field, gauge-fixing and ghost structures used in gravity applications. The Einstein-Hilbert computation is explicitly a truncation/projection, not the exact full fixed-point action.

Eichhorn (2606.21522) explicitly describes local coarse graining through an IR regulator, the background-field construction and the Wetterich flow. It also sharply distinguishes cutoff/RG-scale dependence from physical scale dependence: `k` tracks how much of the path integral has been integrated out and the physical limit is obtained by removing the auxiliary cutoff. This forbids reading `k` as physical proper time or an automatically physical refinement coordinate.

Laporte et al. (2110.09566) give the modified Legendre-transform/EAA construction, exact Wetterich equation, background-field decomposition, gauge fixing, ghosts and an explicit Type-I regulator, while defining `t = ln(k/k0)` as RG time with `k0` an arbitrary reference momentum scale. Their scalar-tensor subspace is closed under the RG flow, but this is not a source-defined finite physical composition law on spacetime states.

## Frozen predicate adjudication

| Predicate | Verdict | Authority result |
| --- | --- | --- |
| A. Exact EAA/Wetterich object | `PASS` | `Gamma_k`, `Gamma_k^(2)`, `R_k` and the functional flow equation are explicit in the frozen stack. |
| B. Domain/codomain of scale evolution | `PASS` | The flow is between scale-indexed effective actions/functionals/couplings in theory space. The frozen stack does not identify this domain with physical spacetime-state Hilbert spaces. |
| C. Regulator insertion/dependence | `PASS` | `Delta S_k` / `R_k` and cutoff-profile dependence are explicit; truncations may retain regulator/scheme dependence. |
| D. Gauge/background structure | `PASS` | Metric background/fluctuation splits, gauge fixing and ghost sectors are explicit enough that their erasure would change the represented object. |
| E. Finite `k1 -> k2` composition law | `SCOPED_ABSENCE_FROM_FROZEN_STACK` | Differential FRG flow, beta-function integration, RG trajectories and shell-wise coarse graining are explicit. The frozen sources do not specify an exact finite transport `U(k2,k1)` together with a source-defined semigroup/composition law of the type required by the preregistration. This absence is recorded rather than completed by mathematical analogy. |
| F. Fixed point/trajectory vs physical refinement | `PASS` | Fixed points and trajectories are theory-space/RG objects. The frozen sources do not identify them with a physical refinement map on states or geometries; the cutoff/physical-scale distinction reinforces this separation. |
| G. No cross-school identification by analogy | `PASS_NEGATIVE_LOCK` | No source-defined typed equivalence to CDT proper-time gluing, HaPPY tensor contraction/isometric encoding, or EPRL refinement is present. |

## Composition-law search result

The exact-PDF audit found no source-defined `semigroup` or `composition law` for finite FRG scale transport in the frozen stack. Phrases such as `RG trajectory`, `integral curve`, `RG transformation`, `integrating beta functions`, and `coarse graining` do not by themselves satisfy predicate E's stronger finite-map requirement.

This is a source-authority statement, not a theorem that no finite flow map can be constructed mathematically from a sufficiently regular autonomous differential equation. ITER069 forbids promoting such a construction to source-qualified physical composition without an explicit typed derivation.

## Controls

- `RG_TIME_SWAP_CONTROL`: **PASS CONTROL**. `RG time` is a logarithmic momentum-scale parameter, not source-defined Lorentzian/proper time.
- `REGULATOR_ERASURE_CONTROL`: **PASS CONTROL**. Removing `R_k` / regulator dependence before the physical limit erases part of the qualified FRG object.
- `TRUNCATION_FULL_THEORY_CONTROL`: **PASS CONTROL**. Einstein-Hilbert/scalar-tensor truncations remain projections/approximations and are not promoted to the exact full theory.
- `FIXED_POINT_REFINEMENT_CONTROL`: **PASS CONTROL**. A fixed point or RG trajectory is not counted as a physical state/geometric refinement map.

## Authority classification

The frozen preregistration permits a scoped PASS when A-D and F are source-qualified and predicate E is exactly adjudicated, including an explicit scoped absence.

Therefore source authority supports:

**`PASS_SCOPED_FRG_SCALE_OPERATION_QUALIFIED`**

with the mandatory qualifier:

**`FINITE_SOURCE_DEFINED_COMPOSITION_LAW = NOT_ESTABLISHED_IN_FROZEN_STACK`**.

The qualified operation is best typed as `C_scale_flow`: regulator-dependent continuum coarse-graining / theory-space flow of effective actions. It is not yet a common physical composition object.

## Claim ceiling

No bridge credit. No universal common parent. No candidate theory. No identification of `C_scale_flow` with `C_seq` (CDT), `C_tensor` (HaPPY), causal-set refinement, or EPRL refinement. No promotion of truncation evidence to full quantum gravity.