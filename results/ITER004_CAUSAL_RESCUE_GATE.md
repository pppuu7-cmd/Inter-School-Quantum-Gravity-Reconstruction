# Iter004 Result — Quantitative Causal Rescue Gate

Status: `DERIVED_ISQGR + NUMERICALLY_VERIFIED_SYNTHETIC`  
Date: 2026-09-12  
Workflow run: `34653258086` — **SUCCESS**

## 1. Problem

Campaign 003 established a near-null direction mixing conformal geometry with QES-like nuisance when their response spaces are nearly collinear.

Campaign 004 asks what an independent causal channel must measure in order to restore stable geometry.

The answer is directional: precision alone is not enough.

## 2. Fisher statement

Let the area+nuisance Fisher matrix be

`F0`.

Let `v_min` be its weakest identifiable eigen/singular direction with eigenvalue

`lambda_min`.

Let an independent causal channel contribute

`Fc = Hc^T Cc^-1 Hc`.

The causal information carried specifically along the dangerous direction is

`I_causal(v_min) = v_min^T Fc v_min`.

Define the dimensionless rescue ratio

`R_rescue = I_causal(v_min) / lambda_min`.

This quantity measures whether the causal data actually constrain the degeneracy that limits geometric inference.

A channel can be very precise and still have little rescue value when it is nearly orthogonal to `v_min`.

## 3. Campaign 004 controls

The synthetic area+nuisance system uses overlap `0.99`, producing a strongly ill-conditioned geometry/nuisance inverse problem.

The causal channel alignment with the dangerous direction is scanned over

`0.0, 0.5, 0.9, 1.0`,

and causal uncertainty over

`0.02, 0.05, 0.20`.

Four seeds are used for every cell.

## 4. Orthogonal causal information does not rescue geometry

At alignment `0.0`:

- smallest-Fisher-singular-value gain remains approximately `1.0` for all three causal precisions;
- conformal variance reduction remains approximately `1.0`;
- conformal RMSE improvement remains approximately `1.0`;
- with sigma_causal `0.02`, the overall condition number becomes worse (`~299`) because the already-strong direction is further constrained while the near-null direction remains untouched.

This is a decisive negative control.

> Additional data are not equivalent to additional identifiability.

## 5. Partial alignment produces graded rescue

At alignment `0.5`:

### sigma_causal = 0.02

- condition-number improvement: about `13.20x`;
- smallest singular value gain: about `18.66x`;
- conformal variance reduction: about `24.72x`;
- conformal RMSE improvement: about `5.85x`.

### sigma_causal = 0.20

- condition improvement: only about `1.24x`;
- singular-value gain: about `1.25x`;
- variance reduction: about `1.25x`;
- RMSE improvement: about `1.10x`.

Thus direction and precision enter jointly.

## 6. Strong alignment sharply restores conditioning

At alignment `0.9`, sigma_causal `0.02`:

- condition improvement: about `62.26x`;
- joint condition number: about `3.20`;
- weakest singular value gain: about `71.50x`;
- conformal variance reduction: about `74.11x`;
- conformal RMSE improvement: about `9.00x`.

At perfect synthetic alignment `1.0`, sigma_causal `0.02`:

- condition improvement: about `101x`;
- joint condition number: about `1.97`;
- weakest singular value gain: about `101x`;
- conformal variance reduction: about `67.33x`;
- RMSE improvement: about `8.32x`.

The non-monotonic difference between variance/RMSE metrics at `0.9` and `1.0` is expected in finite-noise multi-parameter estimation and should not be overinterpreted as an optimum at 0.9.

## 7. CEMR-I2 — CAUSAL_RESCUE_GATE

A causal channel may be credited with resolving a geometry/nuisance degeneracy only if all of the following are demonstrated in the same physical regime:

1. identify the dangerous near-null direction of the geometry+nuisance inverse problem;
2. show that the causal Fisher/information operator has non-negligible projection onto that direction;
3. propagate causal uncertainty rather than treating causal structure as exact;
4. demonstrate gain in the weakest singular value / posterior geometry covariance, not only total Fisher information;
5. show holdout stability so that the rescue is not a basis-specific fit artifact.

The primary continuous diagnostic is

`R_rescue = (v_min^T Fc v_min) / lambda_min`.

No universal numerical pass threshold is fixed yet; the acceptable threshold must be tied to the physical target accuracy and comparator uncertainty.

## 8. Physical meaning for ISQGR

This sharpens BH-002 substantially.

The useful question is no longer

> does causal information help metric reconstruction?

but

> does the source-defined causal observable constrain precisely the geometric ambiguity left unresolved after quantum-information corrections are included?

This criterion can reject a proposed causal/entanglement synthesis even when both channels individually contain large amounts of information.

## 9. Next source-grounded step

Replace the synthetic `Hc` with a concrete causal observable/operator in a regime where the entanglement/QES response is also source-defined.

Candidate routes:

- causal-set SSEE / Pauli–Jordan spectral data within RC-007;
- a controlled HRT setting where independently specified causal/light-cone data exist without being reconstructed from the same entropy dataset.

The first route has the stronger same-realization advantage.

## Claim lock

`R_rescue` is a generic inverse-problem information diagnostic. Its use in a physical quantum-gravity model requires source-defined observables, covariances and a same-regime map.