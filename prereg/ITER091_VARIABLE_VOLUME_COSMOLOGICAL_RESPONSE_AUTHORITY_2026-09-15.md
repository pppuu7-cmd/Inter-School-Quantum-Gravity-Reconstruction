# ITER091 preregistration — variable-volume CDT cosmological response ↔ renormalized FRG cosmological direction

Date: 2026-09-15
Gate: `ITER091_VARIABLE_VOLUME_COSMOLOGICAL_RESPONSE_AUTHORITY`

## Motivation frozen before terminal adjudication

ITER090 proved that, within the fixed-four-volume Einstein-Hilbert minisuperspace truncation, the complete coupling dependence represented by the reduced global action has rank one and depends only on `g_k lambda_k`. Therefore no additional cumulant of the same fixed-volume global volume distribution can separate the two FRG couplings.

The cleanest global escape is to change ensemble: in CDT the bare coupling `kappa_4` is conjugate to total four-volume, while the canonical/fixed-volume ensemble is related to the grand-canonical ensemble by a discrete Laplace transform. Variable-volume response is therefore a genuine candidate direction not covered by the ITER090 no-go.

However, `kappa_4` is a **bare lattice cosmological coupling**, is tuned to a critical/pseudocritical value in simulations, and Gaussian volume fixing introduces an external numerical stiffness. None of these may be silently identified with the renormalized FRG coupling `lambda_k`.

## Frozen sources

- arXiv `2408.07808` — direct CDT↔FRG comparison; bare-vs-renormalized coupling distinction, role of `kappa_4`, critical surface and fixed-volume replacement.
- four-dimensional CDT grand-canonical/canonical authority as used in the standard phase-structure literature: bare Regge action with `kappa_4 N_4`, exponential entropy `exp(kappa_4^c N_4)`, discrete Laplace transform between `Z(kappa_4)` and fixed-`N_4` partition functions.
- arXiv `1510.08719` / covariance-volume-fixing authority — exact-volume zero mode and Gaussian relaxation of the volume constraint.
- current four-dimensional CDT phase-transition/finite-size-scaling authority — pseudocritical `kappa_4^c(N_4,kappa_0,Delta)` and quadratic volume-fixing term.

## Frozen question

Does the four-dimensional CDT source stack provide a source-defined variable-volume response observable whose **renormalized continuum interpretation** is independent of the fixed-volume product `g_k lambda_k` and sufficiently typed to constrain the FRG cosmological direction `lambda_k` (or an equivalent renormalized volume source) without target fitting?

The gate must distinguish three levels:

1. **bare conjugacy**: `kappa_4` couples linearly to lattice four-volume and generates volume moments in the grand-canonical partition function;
2. **critical subtraction / continuum scaling**: the physically relevant source is a deviation such as `kappa_4-kappa_4^c`, with finite-size/pseudocritical corrections controlled;
3. **renormalized cross-framework map**: a source-derived relation from the critical/subtracted lattice volume source or susceptibility to the FRG renormalized cosmological direction.

Bare conjugacy alone is not enough for a bridge observable.

## Required predicates

A. The exact CDT Regge action contains a term in which `kappa_4` is conjugate to the appropriate total four-volume variable, with the `N_4` / `N_41` / `N_32` convention explicit.

B. The grand-canonical partition function and fixed-volume/canonical partition functions are related by a source-defined discrete Laplace transform.

C. The response identities are explicit at bare level, including sign/convention:

`-partial_{kappa_4} ln Z = <N_4>`

and

`partial_{kappa_4}^2 ln Z = Var(N_4)`

(or the source-equivalent convention).

D. The exponential entropy and critical value `kappa_4^c(kappa_0,Delta)` are retained, so the continuum/infinite-volume source is the distance from the critical surface rather than raw `kappa_4`.

E. Finite-volume simulations' pseudocritical `kappa_4^c(N_4,kappa_0,Delta)` are kept distinct from the infinite-volume critical value.

F. A quadratic/Gaussian volume-fixing term with stiffness `epsilon` is identified as an external simulation device. Its induced contribution to `Var(N_4)` must be removed or analytically accounted for before any physical susceptibility is claimed.

G. A source-defined scaling/renormalization prescription maps the critical/subtracted lattice cosmological source and its response to a continuum renormalized cosmological variable or susceptibility.

H. A source-derived equation connects that renormalized CDT direction to FRG `lambda_k` or another explicitly typed FRG cosmological response, independently of the fixed-volume `g_k lambda_k` relation.

I. Bare `kappa_4`, lattice effective-action Lagrange multipliers named `lambda`, critical `kappa_4^c`, and FRG `lambda_k=Lambda_k/k^2` remain distinct unless an equation explicitly maps them.

J. No FRG trajectory, spectral target or desired value may be used to choose the subtraction, normalization or susceptibility amplitude.

## Frozen controls

- `BARE_RENORMALIZED_COSMOLOGICAL_SWAP_CONTROL`: bare `kappa_4` is not FRG `lambda_k`.
- `RAW_KAPPA4_CRITICAL_DISTANCE_CONTROL`: raw `kappa_4` cannot be used where `kappa_4-kappa_4^c` is the scaling variable.
- `PSEUDOCRITICAL_TRUE_CRITICAL_CONTROL`: finite-volume `kappa_4^c(N)` is not the infinite-volume critical source.
- `GAUSSIAN_VOLUME_FIXING_SUSCEPTIBILITY_CONTROL`: the `epsilon(N-Nbar)^2` restraint cannot be interpreted as physical compressibility.
- `N4_N41_CONTROL`: response to total `N_4=N_41+N_32` cannot be replaced by response of `N_41` without the source-defined fixed-coupling conversion.
- `LATTICE_LAMBDA_FRG_LAMBDA_NAME_CONTROL`: same symbol/name gives no map.
- `CANONICAL_GRAND_CANONICAL_CONTROL`: fixed-volume cumulants conditioned on `N_4` cannot be called grand-canonical volume susceptibility.
- `TARGET_NORMALIZATION_CONTROL`: no target FRG value may set a missing multiplicative/additive renormalization.

## Frozen classifications

- `PASS_SCOPED_RENORMALIZED_COSMOLOGICAL_RESPONSE_MAP_IDENTIFIED` only if A-H pass and an independent renormalized CDT→FRG cosmological response equation is source-qualified.
- `PASS_SCOPED_BARE_VOLUME_RESPONSE_RENORMALIZED_MAP_OPEN` if A-F pass but G/H remain absent or incomplete.
- `PASS_SCOPED_CRITICAL_VOLUME_SCALING_RENORMALIZED_FRG_MAP_OPEN` if a nontrivial critical/subtracted scaling law passes G on the CDT side but no typed relation to FRG `lambda_k` passes H.
- `SCOPED_BLOCKED_VOLUME_FIXING_DOMINATES_RESPONSE` if available volume-fluctuation data cannot be separated from the external fixing potential.
- `FAIL_SCOPED_COSMOLOGICAL_RESPONSE_MAP_INCOMPATIBLE` if a frozen source-derived renormalized map exists but contradicts the FRG typing/domain.
- `BLOCKED_SOURCE_AUTHORITY` if even the bare/critical response cannot be adjudicated.

## Claim ceiling

A PASS can at most provide a second global coupling-sensitive candidate observable. It cannot by itself determine a unique FRG trajectory, establish a shared fixed point, validate another held-out observable, create bridge credit, support `BRIDGE_DERIVED`, or authorize candidate-theory construction.

Predicates, controls and classifications are frozen before terminal adjudication.
