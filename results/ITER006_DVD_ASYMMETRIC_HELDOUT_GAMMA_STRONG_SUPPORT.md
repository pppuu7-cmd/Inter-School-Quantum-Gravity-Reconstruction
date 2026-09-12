# ITER006 — asymmetric-boundary held-out gamma strong support

Date: 2026-09-12

## Scope
Prospectively frozen held-out gamma transport test for the already frozen asymmetric Lorentzian EPRL DVD2/DVD3 finite-shell object. This tests finite-cutoff robustness across gamma and boundary data only.

Frozen boundary: `j=(1,2,2,2)`, `j'=(1,2,2,1)`, `i=t=i'=t'=1`; finite auxiliary cutoffs `D={0,1,2}`; held-out gamma set `{0.3,0.8,1.6,2.5,3.0}` inherited before observing these asymmetric responses.

Frozen pattern: for both DVD2 and DVD3, the relative D1->D2 shell increment is smaller than the D0->D1 increment. Strong support requires 5/5 lanes; natural support requires >=4/5. No retuning after response.

## Provenance
- preregistration: `protocol/ITER006_DVD_ASYMMETRIC_HELDOUT_GAMMA_PREREG.json`
- authoritative run: `34709003568`
- head: `e4c63f51acc538c734284110331ae4c4991641af`
- aggregate job: `103594420826`
- aggregate artifact: `10302597203`
- artifact digest: `sha256:755d1da35be78fa50f4a24e64a88d49590576ccf67d54956d20d76fe3568da52`
- classification: `DVD_ASYMMETRIC_HELDOUT_STRONG_SUPPORT`

## Result
All 5/5 held-out gamma lanes passed the frozen stabilization pattern and all numerical gates. Repeat maximum relative difference was exactly `0.0` in every lane.

Observed D1->D2 vs D0->D1 relative increments:
- gamma 0.3: DVD2 `0.345627 < 0.509608`; DVD3 `0.230639 < 0.484065`
- gamma 0.8: DVD2 `0.302460 < 0.506162`; DVD3 `0.232219 < 0.505918`
- gamma 1.6: DVD2 `0.258898 < 0.502313`; DVD3 `0.236601 < 0.533261`
- gamma 2.5: DVD2 `0.244095 < 0.500426`; DVD3 `0.239517 < 0.546229`
- gamma 3.0: DVD2 `0.241459 < 0.499833`; DVD3 `0.240431 < 0.549749`

## Scientific classification
`SCIENTIFIC_PASS_SCOPED / DVD_ASYMMETRIC_HELDOUT_STRONG_SUPPORT`.

This materially strengthens the statement that the finite-shell stabilization pattern is not confined to the original symmetric boundary or calibration gamma set. It does not establish convergence, a continuum limit, cylindrical consistency, or a coarse/refined amplitude map.

## Claim lock
A shell cutoff is not a refinement map. This result does not authorize `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, candidate equations, or RQIR/KMQGB promotion.
