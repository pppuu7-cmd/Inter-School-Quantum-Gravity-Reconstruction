# ITERATION 006 — nearest-framework absorption and selector boundary

Date: 2026-09-12
Status: **ORIENTATION ABSORBED / PREDICTIVE SELECTOR STILL OPEN**
Candidate theory: `UNFORMED`

## A. Standard amplitude-level q-deformed TNR absorbs orientation/spectrum insufficiency

Nearest-framework implementation: `ssteinhaus/Fusion-basis-coarse-graining`, pinned at `bb4d1adb1aa81e5090f3ef25a3b9fb8845f19ff4`.

ISQGR controlling commit: `3ea29f7245ea0657af43bac186b313bdc96f07ef`  
Run: `34666545108`  
Aggregate job: `103480108558`  
Aggregate artifact: `10289342687`.

Counterfactual protocol: after SVD, keep the current singular spectrum exactly fixed and apply a norm-preserving permutation to the retained embedding-vector orientation. Then continue the genuine amplitude-level q-deformed RG flow.

Frozen gate result: **STRONG nearest-framework absorption support, 3/3 couplings**.

- first-step SVD spectrum relative difference: exactly `0` for all three couplings;
- downstream output changes in all three couplings;
- `g=0.0`: final ribbon relative difference `1.0`;
- `g=0.5`: final ribbon relative difference `0.6244225510`, final second-SVD difference `0.4166283246`;
- `g=1.0`: final ribbon relative difference `11.6218041626`, final second-SVD difference `0.3912719667`.

**Decision:** “spectrum/rank alone is insufficient; embedding orientation matters” is already realized inside a standard amplitude-level TNR framework. This part of RM-001/BH-004 is **not** available as an ISQGR novelty claim.

## B. Standard TNR does not automatically provide the predictive selector tested here

ISQGR commit: `250147344b252c1d158bb8fd657046e4dc10e95b`  
Run: `34676760272`  
Aggregate job: `103508171070`  
Aggregate artifact: `10292547840`.

Twelve lanes tested continuous amplitude predictivity and cross-lag incremental predictivity across six couplings using permutation/persistence nulls.

Frozen aggregate result:

- `continuous_amplitude_support = false`;
- `crosslag_incremental_support = false`;
- median amplitude fraction of steps significant beyond permutation p95: `0.0`;
- fraction of amplitude couplings with majority significant steps: `0.0`;
- median cross-lag significant-step fraction: `0.0`;
- fraction of cross-lag couplings with majority significant steps: `0.0`;
- median cross-lag mean L1 improvement: `-0.85615686299`.

Cross-lag mean L1 improvement is negative in every tested coupling (approximately `-0.889, -0.888, -0.879, -0.833, -0.702, -0.537`).

**Decision:** the standard q-deformed TNR control demonstrates orientation dependence but does **not** pass our preregistered tests for a predictive dynamically transported selector.

## Consequence for BH-004/BH-004B

The defensible remaining research question is now narrow:

> Can a **source-native physical selector**, defined by QG constraints rather than by generic SVD relevance, be transported through a genuine QG refinement/coarse-graining map without target retuning and improve held-out closure?

Generic projector awareness, generic retained-subspace orientation, and generic overcomplete transport envelopes are nearest-framework structure and must not be advertised as new quantum gravity.

## Claim lock

These controls are nearest-framework audits, not quantum-gravity evidence. Their purpose is to remove generic TNR structure from the novelty budget. They do not authorize `BRIDGE_DERIVED`, a candidate action/Hamiltonian, or new-physics claims.
