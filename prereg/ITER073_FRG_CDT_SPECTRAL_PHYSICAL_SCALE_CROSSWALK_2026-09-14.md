# ITER073 preregistration — FRG/QEG ↔ CDT spectral physical-scale crosswalk

Date: 2026-09-14
Gate: `ITER073_FRG_CDT_SPECTRAL_PHYSICAL_SCALE_CROSSWALK`

## Motivation

ITER071 established the same abstract spectral-dimension observable definition. ITER072 established a CDT-internal relative spectral scale calibration and a scoped semiclassical absolute lattice-spacing estimate, while leaving the continuum limit open.

The remaining question is not whether both sides have a variable called diffusion time. It is whether a non-circular, source-defined map exists from their diffusion parameters to the same physical resolution scale strongly enough to authorize a pointwise 4D comparator.

## Frozen question

Can frozen 4D CDT and QEG/FRG sources define an independently normalized crosswalk

`CDT diffusion steps -> CDT physical diffusion parameter/resolution -> common physical units <- QEG heat-kernel parameter/mode resolution`

without fitting the QEG trajectory or scale normalization to the same CDT spectral-dimension values that will later be compared, and while retaining anomalous diffusion, regulator/truncation, anisotropy and finite-size structure?

## Frozen sources

### CDT
- arXiv:hep-th/0505113 — J. Ambjorn, J. Jurkiewicz, R. Loll, *Spectral Dimension of the Universe*.
- arXiv:1603.02076 — J. Ambjorn, D. Coumbe, J. Gizbert-Studnicki, J. Jurkiewicz, *Searching for a continuum limit in causal dynamical triangulation quantum gravity*.

### QEG / FRG
- arXiv:hep-th/0508202 — O. Lauscher, M. Reuter, *Fractal Spacetime Structure in Asymptotically Safe Gravity*.
- arXiv:1110.5224 — M. Reuter, F. Saueressig, *Fractal space-times under the microscope: A Renormalization Group view on Monte Carlo data*.

ITER071/072 records may be used only as prior authority for the shared observable definition and CDT-internal scale estimates.

## Required predicates

A. CDT must expose the dimensional relation between integer diffusion duration `sigma` and a physical heat-kernel parameter `T_CDT` (or equivalent) including any normalization factor, dual-step geometry and anisotropy needed for absolute rather than relative scale matching.

B. QEG must expose the relation between heat-kernel diffusion parameter `T_QEG`, Laplacian-mode resolution and RG scale `k`, including the fact that the dominant physical length need not scale as `sqrt(T)` in anomalous regimes.

C. Both sides must admit a common physical normalization, preferably dimensionless Planck units, whose normalization is fixed without using the spectral-dimension values being compared.

D. The crosswalk must distinguish three objects: diffusion parameter, typical diffusion distance/walk scale, and RG/cutoff resolution. Equality between any pair must be source-defined, not inferred from notation.

E. A valid comparison window must exclude CDT short-walk lattice artifacts and long-walk finite-volume/compactness effects and QEG regions where the frozen finite-scale truncation is explicitly unreliable.

F. If a QEG RG trajectory is selected, its physical normalization/initial conditions must be determined independently of the target CDT `D_s` curve. A trajectory obtained by fitting the same target curve can demonstrate representational fit quality but cannot establish an independent physical-scale bridge.

G. The comparison must be genuinely four-dimensional on both sides. A source-qualified 3D fit cannot be promoted to 4D authority.

H. Even if A-G pass, agreement of `D_s` at matched scale can authorize only a same-observable comparator. It cannot establish microscopic equivalence or a common theory.

## Frozen classifications

- `PASS_SCOPED_INDEPENDENT_4D_PHYSICAL_SCALE_COMPARATOR_AUTHORIZED` only if A-G pass with an independently normalized crosswalk.
- `PASS_SCOPED_DIFFUSION_PARAMETER_CROSSWALK_ONLY` if the common heat-kernel parameter can be related up to a residual normalization or realization-dependent scale factor, but absolute physical resolution cannot be independently matched.
- `BLOCKED_INDEPENDENT_PHYSICAL_SCALE_NORMALIZATION` if the only available absolute matching requires an unknown normalization, a missing 4D source object, or fitting the target CDT spectral curve itself.
- `FAIL_SCOPED_SCALE_CROSSWALK_REJECTED` if source-defined scale semantics are incompatible in the frozen scope.
- `BLOCKED_SOURCE_AUTHORITY` if exact definitions are unavailable.

## Frozen controls

- `SQRT_T_UNIVERSAL_DISTANCE_CONTROL`: `ell ~ sqrt(T)` is forbidden outside a source-qualified regular-diffusion regime.
- `DIFFUSION_RG_TIME_SWAP_CONTROL`: heat-kernel diffusion time cannot be identified with RG time.
- `RG_SCALE_DIFFUSION_SCALE_SWAP_CONTROL`: QEG `k` cannot be set to `1/sqrt(T)` without the source-defined mode-dominance law and its regime.
- `CDT_ABS_LATTICE_DIFFUSION_NORMALIZATION_CONTROL`: knowing `a_abs` does not by itself fix the center-to-center diffusion-step normalization or anisotropy factor.
- `FIT_CIRCULARITY_CONTROL`: QEG parameters/scale fitted to the target CDT `D_s` curve cannot then count as independent bridge evidence.
- `3D_TO_4D_PROMOTION_CONTROL`: published 3D fit quality cannot authorize 4D pointwise comparison.
- `ANOMALOUS_WALK_ERASURE_CONTROL`: QEG walk dimension / anomalous diffusion cannot be erased when interpreting physical distance.
- `FINITE_WINDOW_CONTROL`: only source-qualified artifact-free/truncation-reliable windows may be compared.
- `NUMERICAL_AGREEMENT_BRIDGE_CONTROL`: curve/value agreement is not microscopic bridge credit.

## Claim ceiling

A PASS can authorize only a scoped 4D physical-resolution comparator for spectral dimension. No classification in ITER073 can establish FRG/CDT equivalence, a shared UV fixed point, common microscopic dynamics, `BRIDGE_DERIVED`, `UNIVERSAL_COMMON_PARENT_FOUND`, new physics, or a candidate theory.

Predicates and controls are frozen before terminal adjudication.