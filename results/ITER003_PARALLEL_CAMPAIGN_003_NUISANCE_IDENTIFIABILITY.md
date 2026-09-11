# Iter003 Result — Campaign 003 / CEMR Nuisance Identifiability

Status: `NUMERICALLY_VERIFIED_SYNTHETIC`  
Date: 2026-09-12  
Workflow run: `34652964675` — **SUCCESS**

## 1. Scientific question

Campaign 001 showed that a structured QES-like correction can bias the reconstructed conformal field while leaving goodness-of-fit apparently acceptable.

Campaign 003 asks whether adding an explicit nuisance sector fixes the problem, or whether geometry and nuisance can become intrinsically non-identifiable.

Synthetic linearized model:

`y = H_phi phi + H_n eta + noise`,

where `phi` denotes conformal-geometry modes and `eta` denotes generalized-entropy/QES-like nuisance modes. The parameter `overlap` controls how parallel the two response subspaces are.

## 2. Weak overlap — nuisance is identifiable

For `overlap=0.2`:

- geometry variance inflation from adding nuisance: only `1.0417x`;
- joint condition number: `1.5`;
- at nuisance SNR `2.0`, geometry-only reduced chi2 rises to about `5.20`, while the joint model returns about `0.72`;
- mean geometry RMSE improves from about `0.0303` to `0.0191` (`1.96x` bias reduction).

Interpretation: when quantum-information corrections point in a sufficiently independent data direction, they can be fitted without destroying geometric identifiability.

## 3. Intermediate overlap — correction helps but costs information

For `overlap=0.8`:

- joint condition number: about `9`;
- geometry variance inflation: about `2.78x`;
- at nuisance SNR `2.0`, geometry-only RMSE about `0.0827`, joint RMSE about `0.0283` (`3.13x` improvement).

This is still useful, but the price of separating geometry from nuisance is already visible as larger posterior variance.

## 4. Near-collinearity — good fit does NOT mean identifiable geometry

For `overlap=0.99`:

- joint condition number: about `199`;
- geometry variance inflation: about `50.25x`;
- joint reduced chi2 remains about `0.72` in both SNR groups;
- at nuisance SNR `0.5`, geometry-only RMSE about `0.0336`, joint RMSE about `0.1346`;
- at nuisance SNR `2.0`, geometry-only RMSE about `0.1009`, joint RMSE about `0.1346`.

Therefore the joint model can fit the data very well while the inferred geometry becomes much less precise.

This is the central result:

> **explicitly modelling the nuisance is not sufficient when its response is nearly collinear with the geometric response.**

The correct output in that regime is an identifiability limitation, not a preferred `Omega(x)` estimate.

## 5. New CEMR gate — geometry/nuisance angle

Before using entanglement/generalized-entropy information to infer a conformal scale, CEMR must quantify the principal angles or singular-value structure between:

- the geometric response space;
- the quantum-information correction/nuisance response space;
- the independent causal response space.

A good chi-square is insufficient.

A practical gate is now required:

`CEMR-I1 — IDENTIFIABILITY_GATE`

A physical reconstruction cannot be promoted if the joint Fisher/Jacobian system has an uncontrolled near-null direction mixing geometry with nuisance.

## 6. Interaction with Campaign 002

Campaign 002 found that a sufficiently precise independent causal channel can dramatically improve conditioning in a near-degenerate area inversion.

Campaign 003 shows exactly why such an independent channel may be necessary: QES-like nuisance can occupy almost the same response directions as the conformal geometry.

The next physical question is therefore sharper:

> can a source-defined causal observable constrain the near-null geometry/nuisance combination without importing the target geometry itself?

This is more informative than asking whether causality and entanglement are philosophically compatible.

## 7. Implication for BH-002

`BH-002 = RETAIN / IDENTIFIABILITY-CONDITIONED`.

CEMR is allowed to infer geometry only after:

1. same-regime domain overlap;
2. non-circular surface/region mapping;
3. explicit generalized-entropy/nuisance model;
4. geometry–nuisance identifiability audit;
5. independent causal information-gain audit;
6. stable reconstruction under holdout data.

## 8. Next test

Build a three-channel synthetic and then source-grounded system:

`area/entanglement + QES nuisance + causal observable`.

Vary the causal precision and its angle relative to the geometry/nuisance near-null direction. Determine the minimum independent causal information needed to restore stable geometric inference.

## Claim lock

The nuisance basis in Campaign 003 is synthetic. This result establishes an inverse-problem failure mode, not the actual spectrum of quantum extremal surface corrections in a physical spacetime.