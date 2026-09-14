# ITER110 protocol — retrospective relational-completion protection of the nonanalytic G^2 curvature tail

Date: 2026-09-15
Gate: `ITER110_RETROSPECTIVE_RELATIONAL_COMPLETION_NONANALYTIC_G2_COEFFICIENT_PROTECTION_AUTHORITY`
Protocol status: **RETROSPECTIVE SOURCE/STRUCTURAL AUDIT / validation credit 0**

## Motivation

ITER109 established a conditional theorem: any nonzero fixed-geodesic curvature correlator at `O(G^2)` must scale as `G^2/l^8` up to logarithms, but the literature does not yet establish that the `O(G^2)` coefficient is nonzero after changing the relational separation observable.

Before this protocol was registered, sources were inspected showing that the 2026 master-coordinate result is universal within its chosen relational construction, while fixed-geodesic observables form a distinct nonlocal renormalized class. ITER110 therefore receives no prospective validation credit.

## Frozen sources

1. arXiv:2510.11888 / Phys. Rev. D 113, 106032 (2026) — harmonic/master-coordinate relational curvature correlator.
2. arXiv:1706.01891 / Class. Quantum Grav. 35, 035005 (2018) — fixed-geodesic-distance perturbative observable and its extra renormalization.
3. Relational-observable literature used only for the general statement that different physical clock/reference constructions define distinct gauge-invariant observables.
4. ITER109 only as prior power-counting authority.

## Frozen question

Is the nonzero nonanalytic `O(G^2)` coefficient of the 2026 master-coordinate scalar-curvature correlator protected by unitarity, massless-cut structure, BRST/gauge invariance or another source-defined theorem against cancellation under a change to fixed-geodesic relational localization? Or is universality only guaranteed after the relational observable itself has been fixed?

## Required predicates

A. Distinguish gauge independence of one defined relational observable from invariance under changing the relational observable.

B. Nonanalytic massless-loop terms must be separated from local/contact counterterms within a fixed observable.

C. A full protection PASS requires a source theorem or derivation that admissible relational completion terms cannot alter/cancel the separated `O(G^2)` curvature coefficient.

D. The fixed-geodesic precedent must be checked for additional nonlocal terms/counterterms that survive away from coincidence.

E. Positivity/spectral arguments may count only if they apply to the relational scalar-curvature connected correlator itself; scalar curvature is not to be treated as a positive operator by assumption.

F. Distinct clock/master-coordinate/geodesic choices must not be declared physically identical merely because each is diffeomorphism invariant.

G. No EDT exponent may be used to infer cancellation.

## Frozen classifications

- `PASS_SCOPED_NONANALYTIC_G2_COEFFICIENT_PROTECTED_ACROSS_RELATIONAL_COMPLETIONS` if A-C/E-F pass with an explicit protection theorem.
- `PASS_SCOPED_NONANALYTIC_TAIL_UNIVERSAL_WITHIN_FIXED_RELATIONAL_OBSERVABLE_CROSS_COMPLETION_PROTECTION_OPEN` if B-D/F pass but C is not established.
- `SOURCE_SUPPORTS_RELATIONAL_COMPLETION_DEPENDENCE_OF_LONG_RANGE_COEFFICIENT` if a source explicitly computes two admissible completions and finds different noncontact coefficients.
- `BLOCKED_SOURCE_AUTHORITY` if the issue cannot be adjudicated at all.

## Controls

- `GAUGE_INVARIANCE_RELATIONAL_UNIQUENESS_SWAP_CONTROL`
- `LOCAL_COUNTERTERM_NONANALYTIC_CONTROL`
- `POSITIVITY_ASSUMPTION_CONTROL`
- `CLOCK_CHOICE_ERASURE_CONTROL`
- `EDT_TARGET_CANCELLATION_CONTROL`

## Claim ceiling

No outcome may establish a direct EDT/EFT conflict without a matched observable calculation. No continuum EDT, shared fixed point, `BRIDGE_DERIVED`, new physics or candidate theory follows.