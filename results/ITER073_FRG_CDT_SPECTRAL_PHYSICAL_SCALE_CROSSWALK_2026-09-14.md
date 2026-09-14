# ITER073 terminal result — FRG/QEG ↔ CDT spectral physical-scale crosswalk

Date: 2026-09-14
Gate: `ITER073_FRG_CDT_SPECTRAL_PHYSICAL_SCALE_CROSSWALK`
Preregistration commit: `8082e08b2b5349b53b5ffbf20a4676a2e57bf859`
Source-authority commit: `dc604f6881f81fb12d4e1f6aab5ae62b0f75251c`
Adversarial critic commit: `384f01d4b6656aece95b9819582999315885029c`

## Terminal scientific classification

**`BLOCKED_INDEPENDENT_PHYSICAL_SCALE_NORMALIZATION`**

Bridge credit: **0**.

## Question adjudicated

Can the source-qualified CDT spectral-diffusion scale calibration and QEG heat-kernel/RG scale semantics be assembled into an independently normalized four-dimensional physical-resolution crosswalk before comparing the target spectral-dimension values?

## Result

No, not from the frozen source stack.

This is a source-authority block, not evidence that no such crosswalk can exist.

## What is already established

The accumulated authority is nontrivial:

1. **Same observable definition** — both programmes define scale-dependent spectral dimension from a normalized diffusion return probability.
2. **CDT relative scale authority** — changes between regulated CDT ensembles are source-calibrated through the explicit `sigma/a_rel^2` rescaling.
3. **CDT scoped absolute lattice ruler** — the phase-C fluctuation analysis supplies `a_abs` in Planck units under explicit semiclassical/de-Sitter and simplex-geometry assumptions.
4. **QEG scale semantics** — the heat kernel is tied to scale-dependent effective metrics/Laplacians, Laplacian eigenmodes satisfy `k^2 = E_n`, and the return kernel carries the RG-dependent factor `F(E_n)`.
5. **Published representational fit** — a QEG RG trajectory can reproduce reliable 3D CDT spectral-dimension data at approximately percent-level accuracy after fitting the QEG trajectory to that data.

None of these facts is discarded.

## Exact missing object

A comparator-grade crosswalk would require a source-defined chain of the form

`integer CDT diffusion step sigma`

`-> absolute CDT heat parameter / diffusion resolution`

`-> common physical units independent of D_s`

`<- QEG heat parameter / mode spectrum / RG resolution`

for the same four-dimensional physical scale window.

The frozen stack does not close this chain.

### CDT side

The 2005 source assigns continuum diffusion time length-dimension two but explicitly says that translating the lattice measurement into dimensionful continuum quantities requires a subtle dimensional transmutation. Its continuum ansatz retains an unspecified order-one constant.

ITER072 improves this substantially by adding a measured relative `a^2` rescaling and an independent `a_abs/l_Pl` estimate. But the exact absolute normalization of the dual-lattice random-walk step — including centre-to-centre step geometry and anisotropy/simplex dependence — is not established as a source-defined identity valid over the quantum spectral regime.

Thus

`T_CDT proportional_to a_abs^2 sigma`

is supported dimensionally and relatively, while the absolute proportionality needed for pointwise scale matching remains underdetermined.

### QEG side

The QEG heat-kernel parameter is not universally convertible to a typical physical distance through `sqrt(T)`. In a scaling regime with running exponent `delta`, the kernel depends on

`r/T^(1/(2+delta))`

and the walk dimension is

`D_w = 2 + delta`.

At the QEG fixed point, `D_w = 4`. Therefore the ordinary Brownian relation is not a source-faithful universal scale map.

QEG does provide the separate mode/RG relation `k^2 = E_n`; the point is precisely that heat time, walk distance and RG resolution must not be collapsed into a single variable by notation.

## Fit circularity

The strongest published direct QEG/CDT spectral comparison in the frozen stack is in `d=3`. It selects the QEG RG trajectory by fitting its initial conditions to the target CDT spectral-dimension curve.

This is valid and strong evidence of representational compatibility. It is not an independent physical-scale calibration under ITER073, because the same observable being compared is used to select the comparator trajectory.

The source explicitly states that the analogous 4D comparison requires detailed four-dimensional Monte Carlo data.

## Further typed obstruction — spectral and walk dimensions

The QEG source derives, in the relevant scaling regimes,

`D_s/2 = d_H/D_w`

and notes a structural difference: QEG has `d_H=d` for its smooth-manifold effective geometry, while CDT can possess nonclassical microscopic Hausdorff structure. The paper therefore warns that even if `D_s^CDT = D_s^QEG` in a nonclassical regime, one should not generally expect their walk dimensions to agree.

This does not reject the shared spectral observable. It shows why `D_s` cannot serve as its own physical-distance calibration.

## Frozen predicate results

- A — absolute CDT integer-step -> physical diffusion normalization: **PARTIAL / INSUFFICIENT**.
- B — QEG heat parameter / mode / RG relation with anomalous walk retained: **PASS_SCOPED**.
- C — common independently fixed physical normalization: **BLOCKED**.
- D — diffusion parameter vs walk distance vs RG scale distinguished: **PASS_QEG / PARTIAL_CDT / CROSSWALK_BLOCKED**.
- E — mutually reliable comparison window: **PARTIAL; windows exist separately but cannot yet be aligned physically**.
- F — QEG trajectory selected independently of target CDT `D_s`: **NOT ESTABLISHED; published direct fit is target-fitted**.
- G — genuinely 4D direct crosswalk: **NOT ESTABLISHED**.
- H — bridge claim ceiling: **PASS_CONTROL**.

The preregistered classification is therefore:

**`BLOCKED_INDEPENDENT_PHYSICAL_SCALE_NORMALIZATION`**.

## Adversarial critic

The critic attempted the strongest rescue routes:

- set `T_CDT = a_abs^2 sigma` directly;
- argue that the remaining constant is irrelevant to a logarithmic derivative;
- set QEG `k=1/sqrt(T)`;
- use common Planck units as sufficient normalization;
- promote the 3D percent-level direct fit to bridge evidence;
- let spectral dimension define its own scale.

Each route either erases a preregistered physical distinction or reuses the target observable to calibrate itself.

The critic also rejected the stronger `FAIL_SCOPED_SCALE_CROSSWALK_REJECTED`: the missing objects could still be supplied by new source authority.

Critic verdict: **CONFIRMS BLOCKED**.

## Structural consequence

The research programme now distinguishes three levels that must not be conflated:

1. **observable identity** — established for spectral dimension;
2. **within-theory scale calibration** — established in scope for CDT and separately structured in QEG;
3. **cross-theory physical-resolution calibration** — still blocked.

This factorization is useful because it explains why impressive curve agreement can coexist with zero bridge credit.

## Downstream authorization

The highest-information successor is:

**`PREREGISTER_ITER074_CDT_4D_WALK_DISTANCE_DIFFUSION_NORMALIZATION_AUTHORITY`**.

The next gate should ask whether 4D CDT has a source-defined observable for mean diffusion displacement / walk dimension / diffusion radius on the same or source-comparable ensembles, and whether it fixes the absolute dual-walk normalization independently of spectral dimension.

If positive, it can reopen ITER073 with a new independent scale object. If negative/source-blocked, the spectral pointwise physical-resolution route should be deprioritized rather than repeatedly curve-fit.

## Claim ceiling

ITER073 does **not** establish:

- failure of CDT or QEG;
- incompatibility of their spectral observables;
- failure of all FRG/CDT correspondences;
- a no-go theorem;
- `BRIDGE_DERIVED`;
- `UNIVERSAL_COMMON_PARENT_FOUND`;
- a candidate theory;
- new physics.

`CANDIDATE_THEORY = UNFORMED`

`THEORY_ESTABLISHED = 0%`

`BRIDGE_CREDIT = 0`