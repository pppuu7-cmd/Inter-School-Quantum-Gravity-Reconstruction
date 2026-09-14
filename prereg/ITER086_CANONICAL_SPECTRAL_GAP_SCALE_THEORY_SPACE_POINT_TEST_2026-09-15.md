# ITER086 preregistration — canonical spectral-gap scale ↔ reduced-map FRG theory-space point

Date: 2026-09-15
Gate: `ITER086_CANONICAL_SPECTRAL_GAP_SCALE_THEORY_SPACE_POINT_TEST`

## Status of this gate

This is a **prospectively frozen ISQGR bridge hypothesis test**, not a source claim that the literature already identifies the scales.

The hypothesis is deliberately narrow and falsifiable:

`H_gap`: for a CDT ensemble in the de-Sitter phase, the FRG coarse-graining scale entering the already-qualified reduced minisuperspace map is identified with the Litim threshold of the **lowest nonzero normalized spatial Laplacian eigenmode** of that same ensemble.

No other eigenmode may be substituted after seeing the result.

## Prior authority imported

From ITER078:

`24 pi G_k = (omega/omega_0)^(4/3) Gamma a^2`,

and

`P_CDT = omega^2 Gamma/(omega_0^2 sqrt(N_4)) ~= 1.63 lambda_k g_k`.

From ITER084:

`z_n = 9 ell_n/a^2`,

where `ell_n` is the dimensionless eigenvalue of `L_graph=4I-A`.

From ITER085 background-spatial Litim route:

`k_thr,n^2 = z_n`.

These are imported only at their existing scoped claim ceilings. ITER085 does not say that this threshold is the minisuperspace scale; that equality is exactly the new `H_gap` hypothesis.

## Canonical mode frozen before matched-data search

The only admissible mode for ITER086 is

`ell_1 = lowest strictly positive eigenvalue`

of the CDT spatial dual-graph Laplacian on the qualified spatial slice/ensemble.

Rationale for freezing `ell_1`:

- it is canonically defined without target values;
- it probes the largest nonconstant spatial length scale and is therefore the least arbitrary candidate for a global reduced/minisuperspace scale;
- it avoids post-hoc choice among higher modes.

No mobility edge, hand-selected mode number, plateau edge, spectral-dimension crossover or best-fit eigenvalue may replace `ell_1` in this gate.

## Algebraic prediction frozen before data

Under `H_gap`,

`k_1^2 = z_1 = 9 ell_1/a^2`.

Combining with the ITER078 Newton-coupling map gives

`g_1 = k_1^2 G_k`

`    = [9 ell_1/a^2] [(omega/omega_0)^(4/3) Gamma a^2/(24 pi)]`

so

**`g_1 = (3/(8 pi)) ell_1 Gamma (omega/omega_0)^(4/3)`**.

The lattice spacing cancels.

The reduced coupling product is

`lambda_1^FRG g_1 = [omega^2 Gamma/(omega_0^2 sqrt(N_4))]/1.63`.

Therefore

**`lambda_1^FRG = [8 pi/(3*1.63)] (omega/omega_0)^(2/3) / [ell_1 sqrt(N_4)]`**.

Thus `H_gap` predicts a complete dimensionless FRG theory-space point `(g_1,lambda_1^FRG)` from the four dimensionless CDT quantities `(ell_1,Gamma,omega/omega_0,N_4)` without an absolute value of `a`.

No spectral-dimension target enters these equations.

## Frozen source/data stack for the test

- arXiv `2408.07808` and `2411.02330` — direct reduced CDT↔FRG parameter map and scaling interpretation.
- arXiv `1403.5940` and source-linked CDT transfer-matrix/effective-action data — `Gamma`, `omega`, `N_4` authority.
- arXiv `1804.02294`, `1903.00430`, `1912.11311` and source-linked spectral datasets — spatial dual-graph eigenvalues and finite-volume scaling.
- arXiv `2306.10408` — FRG regulator and Einstein-Hilbert theory-space domain/beta-function authority where applicable.

## Required predicates

A. At least one CDT ensemble in the de-Sitter phase has source-recoverable `ell_1`, `Gamma`, `omega` and `N_4` at the **same bare couplings and compatible volume/slice prescription**.

B. `ell_1` is obtained independently of the reduced-action fit and was not selected because it improves FRG agreement.

C. The algebra above is applied exactly; no additional multiplicative scale parameter may be introduced.

D. The resulting `(g_1,lambda_1^FRG)` lies in a source-defined domain where the frozen FRG truncation/regulator is meaningful. If it crosses a pole/singularity/excluded region, this counts against `H_gap` rather than being repaired by changing the mode.

E. If multiple matched ensembles exist, their predicted points must be compared against the frozen FRG vector field/trajectory structure without refitting each point independently.

F. A common or sequential FRG trajectory may receive credit only if the predicted point ordering with `k_1` is compatible with the beta-function direction and no CDT spectral target fixes initial conditions.

G. The original ITER080 held-out spectral-dimension values remain held out until the point/trajectory test is complete.

H. The distinction between local finite-regulator spectral normalization and global continuum spectral convergence remains explicit.

I. Failure of matched-data availability is not scientific confirmation or rejection of `H_gap`; it is a data-authority blocker.

## Frozen controls

- `MODE_SELECTION_CONTROL`: only `ell_1` is admissible.
- `SAME_ENSEMBLE_CONTROL`: no mixing `ell_1` from one bare-coupling/volume point with `Gamma,omega` from another unless a source-derived interpolation with propagated uncertainty was preregistered (none is).
- `VOLUME_SLICE_CONTROL`: spatial-slice volume/time prescription must be compatible with the reduced ensemble definition.
- `ABSOLUTE_A_REINTRODUCTION_CONTROL`: cancellation of `a` must not be undone by an arbitrary absolute scale fit.
- `FRG_DOMAIN_RESCUE_CONTROL`: a predicted point outside the valid FRG domain cannot be rescued by mode switching or regulator switching.
- `DE_SITTER_GEOMETRY_CONTROL`: round-sphere eigenvalue identities may be used only as held-out consistency checks, not to fit `ell_1` or the point.
- `SPECTRAL_DIMENSION_HOLDOUT_CONTROL`: no `D_s` value may determine `(g_1,lambda_1^FRG)`.
- `TRAJECTORY_INITIAL_CONDITION_FIT_CONTROL`: no target spectral curve may select FRG initial conditions.
- `BACKGROUND_PRODUCTION_CONTROL`: ITER085's background-spatial threshold cannot be presented as the 2023 production regulator identity.

## Frozen classifications

- `PASS_SCOPED_CANONICAL_GAP_SCALE_POINT_PREDICTION_TESTABLE` if matched source data determine at least one complete point with no extra fit and it lies in the admissible FRG domain; this does not yet validate a trajectory.
- `PASS_SCOPED_CANONICAL_GAP_SCALE_TRAJECTORY_TESTABLE` if multiple matched points additionally define a no-refit ordered test against the FRG vector field.
- `FAIL_SCOPED_CANONICAL_GAP_SCALE_INCOMPATIBLE` if the frozen hypothesis yields points inconsistent with the source-defined FRG domain/ordering and cannot be repaired without violating controls.
- `BLOCKED_MATCHED_ENSEMBLE_DATA_AUTHORITY` if the required same-ensemble observable tuple cannot be source-qualified.
- `PASS_ALGEBRAIC_CLOSURE_MATCHED_DATA_OPEN` if the algebra is sound but the frozen stack exposes insufficient matched numerical data for A.
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION` only for transport/extraction failure.

## Claim ceiling

Even a PASS only authorizes a new, explicit, falsifiable theory-space-point hypothesis. It does not establish a common RG trajectory, validate the held-out spectral dimension, prove a shared fixed point, create bridge credit, support `BRIDGE_DERIVED`, or authorize candidate-theory construction.

The mode, formulas, controls and classifications are frozen before matched-data extraction.
