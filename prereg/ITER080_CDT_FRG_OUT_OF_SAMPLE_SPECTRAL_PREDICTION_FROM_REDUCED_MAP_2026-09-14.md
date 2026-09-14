# ITER080 preregistration — CDT/FRG out-of-sample spectral prediction from the reduced map

Date: 2026-09-14
Gate: `ITER080_CDT_FRG_OUT_OF_SAMPLE_SPECTRAL_PREDICTION_FROM_REDUCED_MAP`

## Motivation

ITER071 established that CDT and QEG/FRG use the same abstract spectral-dimension observable definition. ITER073 showed that an independently normalized pointwise physical-scale crosswalk was missing. ITER078 subsequently established a direct equation-level reduced CDT↔FRG action/parameter map, and ITER079 established a reduced `a-xi-k` scaling relation while leaving the operational `xi_CDT <-> k` map unresolved.

The next scientifically useful question is therefore predictive rather than descriptive: does the new reduced map determine enough FRG information to predict any held-out CDT spectral-dimension feature **without fitting or selecting the FRG trajectory/scale using the target spectral data**?

## Frozen question

Given only source information already independent of the target CDT spectral curve, does the ITER078 reduced map

`(N_4, omega, Gamma) -> (V_4(k), G_k, lambda_k g_k)`

plus the frozen FRG spectral machinery determine a unique or sufficiently narrow prediction for one or more held-out four-dimensional CDT spectral observables?

Possible admissible predictions include, if source-defined independently:

- an asymptotic UV or IR spectral dimension;
- crossover ordering or plateau structure;
- a crossover scale in independently normalized units;
- a bounded spectral curve family narrower than generic FRG theory-space freedom.

The gate forbids using the target CDT `D_s(sigma)` data to choose the FRG RG trajectory, initial conditions, scale normalization, regulator choice, or the missing decomposition of `lambda_k g_k` into `lambda_k` and `g_k`.

## Frozen sources

Direct reduced CDT↔FRG map:
- arXiv:2408.07808 — J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, D. Németh, *Is Lattice Quantum Gravity Asymptotically Safe? Making contact between Causal Dynamical Triangulations and the Functional Renormalization Group*.
- arXiv:2411.02330 — same authors, *IR and UV limits of CDT and their relations to FRG*.

QEG/FRG spectral prediction machinery:
- arXiv:1110.5224 — M. Reuter, F. Saueressig, *Fractal space-times under the microscope: A Renormalization Group view on Monte Carlo data*.
- arXiv:hep-th/0508202 — O. Lauscher, M. Reuter, *Fractal Spacetime Structure in Asymptotically Safe Gravity*.

Held-out four-dimensional CDT spectral data/authority:
- arXiv:hep-th/0505113 — J. Ambjørn, J. Jurkiewicz, R. Loll, *Spectral Dimension of the Universe*.
- arXiv:1411.7712 — D. N. Coumbe, J. Jurkiewicz, *Evidence for Asymptotic Safety from Dimensional Reduction in Causal Dynamical Triangulations*.

No later source or target-data tuning may upgrade ITER080 after detailed adjudication.

## Required predicates

A. The FRG spectral observable must be written explicitly as a function of source-defined RG/effective-geometry data, identifying which running quantities are required beyond the product `lambda_k g_k`.

B. The ITER078 reduced map must determine those required FRG quantities uniquely or within a prospectively bounded family **without using the held-out CDT spectral data**.

C. If the spectral prediction requires separate `g_k` and `lambda_k`, beta functions, a trajectory label/initial condition, or a `k` normalization, the frozen non-spectral sources must determine them independently enough for prediction.

D. Any universal fixed-point spectral-dimension value may count as an out-of-sample prediction only if its applicability to the held-out CDT data window is source-qualified independently of fitting the target curve and independently of assuming the shared UV fixed point that the gate is meant to test.

E. A crossover scale prediction requires an independently normalized `k` ↔ CDT diffusion/physical-scale map. The unresolved ITER079 `xi <-> k` relation cannot be silently bypassed.

F. The target observable must be held out: no FRG trajectory, scale, horizontal normalization, or regulator is selected by minimizing disagreement with the target CDT `D_s` curve.

G. The published 3D QEG↔CDT spectral fit must be treated as prior evidence of representational flexibility, not as an out-of-sample 4D validation, because its FRG trajectory is target-fitted.

H. Four-dimensional CDT data must remain distinct from three-dimensional comparisons and from asymptotic extrapolations outside reliable lattice windows.

I. Regulator/truncation dependence and the distinction between asymptotic fixed-point predictions and finite-scale Einstein-Hilbert trajectory predictions remain explicit.

J. A successful prediction can validate only the reduced crosswalk on a held-out observable. It cannot establish full microscopic theory equivalence or bridge credit automatically.

## Frozen classifications

- `PASS_SCOPED_OUT_OF_SAMPLE_4D_SPECTRAL_PREDICTION` if A-J pass and at least one nontrivial four-dimensional CDT spectral feature is predicted without target-data tuning.
- `PASS_SCOPED_ASYMPTOTIC_SPECTRAL_PREDICTION_ONLY` if a genuinely parameter-independent asymptotic spectral value is predicted, but no finite-scale curve/crossover can be predicted independently.
- `SCOPED_BLOCKED_UNDERDETERMINED_FRG_TRAJECTORY_FROM_REDUCED_MAP` if the ITER078 map fixes only combinations insufficient to determine the FRG spectral trajectory and no independent source closes the missing degrees of freedom.
- `SCOPED_BLOCKED_NO_INDEPENDENT_SPECTRAL_SCALE_NORMALIZATION` if the spectral function can be predicted in FRG variables but cannot be mapped to a held-out CDT scale without target tuning.
- `FAIL_SCOPED_OUT_OF_SAMPLE_SPECTRAL_PREDICTION_REJECTED` if a source-fixed prediction exists and is contradicted by the held-out 4D CDT data in its qualified window.
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION` only for source-access failure.

## Mandatory controls

- `TARGET_TRAJECTORY_FIT_CONTROL`: any FRG trajectory chosen using target CDT `D_s` receives zero prediction credit.
- `PRODUCT_TO_INDIVIDUAL_COUPLINGS_CONTROL`: `lambda_k g_k` cannot be replaced by separately known `lambda_k` and `g_k` unless independently derived.
- `MISSING_K_NORMALIZATION_CONTROL`: an unresolved physical `k` normalization cannot be filled by horizontal curve shifting.
- `FIXED_POINT_ASSUMPTION_CIRCULARITY_CONTROL`: assuming that CDT reaches the same FRG UV fixed point cannot then count the FRG UV value as independent evidence of that assumption.
- `3D_TO_4D_PROMOTION_CONTROL`: the 3D target-fitted comparison cannot be promoted to 4D prediction authority.
- `ASYMPTOTIC_FINITE_WINDOW_CONTROL`: an asymptotic `k -> infinity` value cannot be compared directly to finite-cutoff CDT data unless the source qualifies the regime.
- `REGULATOR_ERASURE_CONTROL`: finite-scale regulator/truncation dependence remains explicit.
- `SPECTRAL_SCALE_CIRCULARITY_CONTROL`: target spectral crossover locations cannot set the scale used to predict themselves.
- `REDUCED_FULL_VALIDATION_CONTROL`: a held-out spectral success would validate only the reduced correspondence in scope.

## Claim ceiling

Even the strongest PASS would establish only a scoped out-of-sample validation of the reduced CDT↔FRG crosswalk on the spectral observable. It would not establish full theory identity, a universal common parent, a proven shared UV fixed point, `BRIDGE_DERIVED`, new physics or a candidate quantum-gravity theory.

Candidate theory remains `UNFORMED / 0%`; bridge credit remains zero absent a later constitutional promotion.

Predicates, source stack and classifications are frozen before detailed spectral adjudication.