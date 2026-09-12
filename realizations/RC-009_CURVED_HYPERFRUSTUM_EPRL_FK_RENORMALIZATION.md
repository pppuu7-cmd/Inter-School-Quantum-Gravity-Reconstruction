# RC-009 — Curved Hyperfrustum EPRL-FK Renormalization

Status: `SOURCE_GROUNDED / CURVED_AMPLITUDE_REFINEMENT_TARGET`  
Family: `F04 spinfoam/LQG`  
Date: 2026-09-12

## Primary source

B. Bahr, G. Rabuffo, S. Steinhaus, *Renormalization of symmetry restricted spin foam models with curvature in the asymptotic regime*, Phys. Rev. D 98, 106026 (2018), arXiv:1804.00023v3.

Evidence class: `SOURCE_GROUNDED / SYMMETRY_RESTRICTED_RIEMANNIAN_EPRL_FK / LARGE_J`.

## Why this realization matters

RC-009 is a stronger refinement target than the quantum-cuboid RC-008 in one specific respect: the hyperfrustum sector admits non-zero extrinsic curvature and expanding/contracting spatial slices. The Regge action of a hyperfrustum no longer vanishes, so the retained model samples configurations with different curvature rather than only a flat cuboid orbit.

It is still a severe symmetry reduction of the full 4D theory and uses the asymptotic Riemannian EPRL-FK amplitude. It is not the full Lorentzian EPRL model.

## Source-native coarse/fine setup

The paper defines background-independent RG by matching geometric observables between two different discretizations.

In the isotemporal three-parameter setup:

- coarse lattice: `Phi_(3,2)`, 54 hyperfrusta;
- fine lattice: `Phi_(4,3)`, 192 hyperfrusta;
- fixed boundary areas correspond to the same total initial/final spatial volume;
- total height is fixed and divided equally among time steps;
- the remaining path integrals are over one intermediate spatial spin on the coarse lattice and two on the fine lattice;
- couplings are `g=(alpha,G,Lambda)`;
- three observables are matched: intermediate 3-volume, its variance, and total 4-volume.

Thus the flow is not inferred from a scalar amplitude alone: it is a projection defined by a vector of geometric observables and an explicit cylindrical-consistency residual.

## Published source results

The paper reports:

- curved one-parameter isochoric fixed point `alpha* ~ 0.69`;
- a three-parameter fixed-point candidate near `alpha* ~ 0.677`, `G* ~ 0.037`, `Lambda* ~ 0.008`;
- one repulsive and two attractive directions in that projected flow;
- the free point `G=Lambda=0` is not a fixed point of the asymptotic Riemannian EPRL model in the tested setup;
- replacing the EPRL amplitude by the exponential of the Regge action with the measure factors restores the free fixed point in their analysis.

The last item is an especially useful falsification/control channel: the extra EPRL asymptotic branches can materially change coarse/fine consistency rather than merely renormalizing a scalar prefactor.

## ISQGR mapping

RC-009 naturally separates:

1. a coarse/fine boundary identification;
2. a transported amplitude on a different discretization;
3. a vector of source-native geometric observables used to project back to a truncated coupling family;
4. a residual measuring failure of exact cylindrical consistency.

This is structurally relevant to `BH-004/BH-004B`, but the observable-matching projection is not automatically the same object as a local physical constraint selector. The correspondence must be tested rather than asserted.

## Immediate tests

1. Audit survival of the alpha fixed-point location under the cuboid -> curved one-parameter -> curved three-parameter extensions.
2. Treat the EPRL-vs-Regge free-point behavior as an amplitude-structure control, not as evidence that the full EPRL theory fails.
3. Reconstruct at least one source-defined coarse/fine observable integral from Eqs. (50)-(53) before promoting RC-009 to an executable amplitude-refinement realization.
4. If numerical reconstruction is possible, freeze couplings on two observables and test the third as a held-out cylindrical-consistency observable.

## Claim lock

- This is a symmetry-restricted Riemannian large-j model, not full Lorentzian EPRL gravity.
- The reported fixed point is associated to a fixed physical transition/discretization comparison, not directly to an energy-scale RG flow.
- `G` and `Lambda` being attractive in this projected flow must not be equated with irrelevance in asymptotic safety.
- The source's free-point result does not constitute a refutation of EPRL-FK.
- No candidate-theory promotion is authorized from RC-009 alone.
