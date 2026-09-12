# ITERATION 004 — RM-001 Spectral-Insufficiency Theorem for Projected Composition

Date: 2026-09-12  
Status: `PROVED / STRUCTURAL BRIDGE SUPPORT`  
Interface: `IF-04 COMPOSITION/GLUING`

## Statement

For projected two-step composition, the discarded-sector return operator

`Delta = P C2 Q C1 P`, with `Q = I-P`,

is **not determined in general** by:

- the spectrum (or singular values) of `C1`;
- the spectrum (or singular values) of `C2`;
- the rank of `P`;
- a shared similarity relation between `C1` and `C2`.

Relative orientation of the retained projector `P` to the composition operators is independent closure data.

Therefore a reduced description based only on scalar spectral data and retained dimension cannot, in general, determine composition closure.

## Explicit 2x2 proof

Let

`P = diag(1,0)`, `Q = diag(0,1)`

and take two nondegenerate diagonal operators

`D1 = diag(a1,b1)`,

`D2 = diag(a2,b2)`.

For a real rotation

`R(theta) = [[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]`,

define a **shared similarity orbit**

`Ck(theta) = R(theta) Dk R(theta)^T`,  `k=1,2`.

For every `theta`, each `Ck(theta)` has exactly the same eigenvalues and singular values as `Dk`. The pair is transformed by the same similarity, so any pair relation invariant under shared similarity is also unchanged.

The off-diagonal matrix element is

`[Ck(theta)]_01 = (ak-bk) sin(theta) cos(theta)`

up to the irrelevant sign convention for the rotation.

Because `P` and `Q` are rank-one complementary projectors,

`P C2 Q C1 P`

has only one potentially nonzero retained-sector matrix element, equal to

`(a2-b2)(a1-b1) sin^2(theta) cos^2(theta)`.

Hence

`||Delta(theta)|| = |(a2-b2)(a1-b1)| sin^2(theta) cos^2(theta)`.

Equivalently,

`||Delta(theta)|| = |(a2-b2)(a1-b1)| sin^2(2 theta) / 4`.

Therefore:

- at `theta = 0`, `||Delta|| = 0`;
- at `theta = pi/4`, `||Delta|| = |(a2-b2)(a1-b1)|/4`;
- all operator spectra are identical at the two angles.

So two descriptions with identical spectral data and identical retained rank can have different composition-closure defects. This proves the claim by explicit counterexample.

## General mixed-block identity

The exact BH-001 return defect can be written as the product of mixed retained/discarded blocks:

`Delta = (P C2 Q)(Q C1 P)`.

Consequently, for any submultiplicative operator norm,

`||Delta|| <= ||P C2 Q|| ||Q C1 P||`.

This shows what a closure-safe effective description must control: not merely eigenvalues of `C1,C2`, but their action **between retained and discarded sectors**.

The mixed blocks transform when the operators are rotated relative to a frozen `P`, even if their spectra do not.

## Relation to RM-001 numerics

The theorem explains the common structure seen in the two independent numerical chains used for RM-001:

1. causal-set SSEE: principal-angle/source-sector orientation adds held-out predictive information for closure while a coarser projector-distance statistic does not;
2. SU(2) BF: shared unitary similarity preserves holdout spectra and pair structure but scrambling orientation relative to the frozen train projector increases discarded-sector return.

The theorem does **not** use either numerical result in its proof.

## Minimal bridge requirement forced by the theorem

A closure-aware scale description must retain one of the following equivalent classes of information:

- the retained projector/subspace `P_s` itself;
- principal-angle/orientation data sufficient to reconstruct the mixed blocks;
- the mixed blocks `Q C P` and `P C Q` directly;
- a stronger parent object from which those data are uniquely recoverable.

A scalar cutoff, running coupling, retained rank, or operator spectrum is insufficient in general.

This motivates the bridge-level effective object

`E_s = (P_s, mu_s, ...)`,

where `P_s` carries sector orientation and `mu_s` stands for scale/measure/normalization information. The ellipsis is deliberate: the theorem does not determine the complete parent structure.

## Degenerate exceptions

The orientation dependence disappears in special cases, for example if:

- `C1` or `C2` is proportional to the identity on the relevant two-dimensional sector;
- `P` is transported covariantly together with the shared similarity;
- the relevant mixed block vanishes by an exact symmetry/constraint.

These are closure conditions or special symmetries, not counterexamples to the generic insufficiency statement.

## Claim lock

`PROVED` here means only the linear-algebra statement above. It does not establish:

- a fundamental quantum-gravity degree of freedom;
- a unique coarse-graining prescription;
- a new theory;
- new physics;
- GR/Lorentzian recovery;
- RQIR/KMQGB promotion readiness.
