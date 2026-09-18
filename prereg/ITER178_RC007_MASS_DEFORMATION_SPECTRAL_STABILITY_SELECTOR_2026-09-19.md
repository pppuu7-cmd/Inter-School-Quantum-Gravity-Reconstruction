# ITER178 preregistration — RC007/BH003 mass-deformation spectral-stability selector

Date frozen: 2026-09-19

## Purpose

Recover a genuinely executable unsaturated PHASE_1 front after ITER177/RC008 reconciliation.

RC007/BH003 already established:
- source-native causal-set SSEE reproduction;
- geometry transfer of the externally source-defined `sqrt(N)/(4*pi)` spectral cutoff;
- negative entropy-blind two-line spectral-knee selection;
- negative closure-L-curve regulator selection;
- negative Bernoulli-thinning derivation of the source cutoff exponent;
- positive transfer of the source-defined subspace direction under thinning;
- a completed massive free-field robustness campaign that froze the source cutoff and therefore did not derive it.

ITER178 asks a new, narrower question:

> can a dynamical deformation of the same causal-set free-field object identify the useful spectral break without entropy and without using the source cutoff in selector construction?

This is a same-realization regulator-selection diagnostic, not a QG bridge claim.

## Frozen source-native object

Use the already implemented 1+1D causal-set massive retarded Green function

`K_m = K_0 [I + (m^2/rho) K_0]^{-1}`, with `K_0=C/2` and unit-parent-volume convention `rho=N`.

For each Poisson sprinkling construct `i Delta_m = i(K_m-K_m^T)`.

The selector may use only the spectra/eigenvectors of these operators for the same sprinkling at several prospectively frozen masses.

## Frozen holdout panel

Parent sizes:

`N = [384, 512, 768, 1024]`.

New sprinkling seeds, not used by the historical massive campaign:

`[211, 223, 227, 229]`.

Mass panel:

`m = [0.0, 2.0, 5.0]`.

The largest frozen deformation is `m^2/rho <= 25/384 < 0.066`.

No target entropy is computed or read by the selector.

## Frozen candidate retained-fraction grid

Use the largest-absolute-eigenvalue spectral sectors at even ranks nearest

`f = [0.04, 0.06, 0.09, 0.13, 0.18, 0.25, 0.35, 0.48, 0.65, 0.82]`.

For every `f`, use the same rank for `m=0,2,5` in a given realization.

For a rank-`r` orthonormal basis `U_m(f)`, define mass-deformation instability

`I(f) = mean_{m in {2,5}} [1 - ||U_0(f)^* U_m(f)||_F^2/r]`.

This equals the normalized rank-matched projector distance squared.

## Frozen entropy-blind break rule

For adjacent grid points define

`S_i = [I(f_{i+1})-I(f_i)] / [log(f_{i+1})-log(f_i)]`.

Choose the interval with maximum **positive** `S_i`.

A job-level break is `RESOLVED` only if:

1. the maximizing interval is not the first or last grid interval;
2. its slope is positive;
3. its slope is at least `1.25x` the second-largest positive slope.

The selected rank fraction is the geometric mean `sqrt(f_i f_{i+1})`.

The selected eigenvalue cutoff is the geometric mean of the absolute-eigenvalue thresholds of the two bounding ranks for the massless operator.

No source cutoff, entropy value, continuum coefficient, or source retained rank may enter this selection.

## Frozen selector-stability gate

Across 16 holdout realizations:

- at least 12/16 job-level breaks must be RESOLVED;
- at least 12/16 resolved break intervals must lie in one common interval or its immediately adjacent intervals.

Failure is `BLOCKED_SCOPED_ITER178_DYNAMIC_BREAK_NOT_STABLY_IDENTIFIED`, not a physics FAIL.

## Frozen post-selection source-compatibility test

Only after the selector is frozen and applied, compute the diagnostic source scale

`lambda_source(N) = sqrt(N)/(4*pi)`.

Fit the median selected cutoff at each N to

`lambda_selected = A N^alpha`

by ordinary least squares in log-log space.

A source-compatible selector requires all:

1. fitted `alpha in [0.35,0.65]`;
2. log-log `R^2 >= 0.85`;
3. median over all resolved jobs of `lambda_selected/lambda_source in [0.5,2.0]`.

These tolerances are frozen before ITER178 output.

## Independent implementation critic

Two independent implementations must run on identical `N,seed,mass,f` panels:

- Researcher computes instability from `1-||U_0^*U_m||_F^2/r`.
- Critic independently constructs orthoprojectors and computes `||P_0-P_m||_F^2/(2r)`.

They must agree per grid point within absolute `1e-9`, choose the same break interval, and agree on resolved/unresolved status. Any discrepancy is `INVALID_IMPLEMENTATION`.

A deterministic point-label permutation of the `m=5` projector is recorded as an adversarial null; it must not be used to choose the break or thresholds.

## Frozen terminal taxonomy

### PASS

`PASS_SCOPED_ITER178_MASS_DEFORMATION_DYNAMIC_BREAK_SOURCE_COMPATIBLE`

iff implementation agreement passes, the selector-stability gate passes, and all three post-selection source-compatibility predicates pass.

Interpretation ceiling: in this 1+1D free-field causal-set realization, an entropy-blind dynamical-deformation criterion identifies a stable spectral break compatible in scale with the externally known SSEE cutoff. This does not derive gravitational dynamics or universalize the rule.

### SCIENTIFIC FAIL, scoped

`SCIENTIFIC_FAIL_SCOPED_ITER178_MASS_DEFORMATION_DYNAMIC_BREAK_SOURCE_INCOMPATIBLE`

iff implementation agreement passes and a stable break is identified, but one or more frozen source-compatibility predicates fail.

This falsifies this specific dynamical-break mechanism, not BH003, causal-set theory, or SSEE.

### BLOCKED, scoped

`BLOCKED_SCOPED_ITER178_DYNAMIC_BREAK_NOT_STABLY_IDENTIFIED`

iff the independent implementations agree but the frozen selector-stability gate fails.

### INVALID

`INVALID_IMPLEMENTATION_ITER178`

for researcher/critic disagreement, non-finite required quantities, provenance mismatch, or failure of frozen panel execution.

## Claim locks

Always false / zero during ITER178:

- `BRIDGE_DERIVED`;
- `NEW_PHYSICS_FOUND`;
- `NEW_QG_THEORY_REQUIRED`;
- `ALL_KNOWN_SCHOOLS_FAIL`;
- `ITER118_MATCHING_AUTHORIZED`;
- `B1_total` authorization;
- candidate action/equations.

Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.

## Information-gain rationale

This gate uses genuinely new operator information absent from the already-falsified one-spectrum knee and closure rules: controlled dynamics deformation inside the same causal set and field realization. It is executable now, does not depend on the blocked RC008 global measure or ITER175 distributional branch, and has a clean negative outcome that would close another plausible endogenous-regulator mechanism.
