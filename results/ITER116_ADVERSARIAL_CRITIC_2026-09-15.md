# ITER116 adversarial critic — corrected single-log RG hierarchy

Date: 2026-09-15
Gate: `ITER116_FIXED_GEODESIC_CURVATURE_G2_SINGLE_LOG_RG_HIERARCHY_AUTHORITY`
Preregistration: `ec44eb92a104aaa4a2e41039bf031377404daece`
Source authority: `48cc9022327003e293c8b523386e534b5ec97032`

## Attack 1 — `beta_1=0` assumes too much about Newton-constant running

The statement is order-scoped. ITER116 factors the correlator as `G^2` times a dimensionless bracket and asks for explicit `mu` independence at the first noncontact order. Any running that changes the overall `G^2` factor at the same accuracy can be absorbed into the coefficient RG equation; in low-energy EFT, the universal separated one-loop structure is not described by a logarithmic running of a new dimensionless Newton coupling. Corrections induced by higher perturbative order belong to `O(G^3)` and do not invalidate the frozen `O(G^2)` hierarchy.

## Attack 2 — B1 may itself contain hidden finite-log dependence

By definition the corrected radial basis places all explicit `L=log(mu^2 l^2)` dependence into `B_1 L`; `B_0,B_1` are separation-independent running coefficients. Allowing them to depend on `L` would double-count the basis. They may depend on dimensionless gauge/scheme parameters, but physical gauge dependence must cancel in the complete observable.

## Attack 3 — a nonzero B1 could still be canceled by B0

Not for all separations. `B_0+B_1L` with `B_1!=0` can vanish at most at isolated `l` values, not identically as a function of separation. Thus `B_1!=0` is sufficient for noncancellation of the whole `O(G^2)` separated observable.

## Attack 4 — the highest pole always fixes the physical log coefficient without subtleties

Needs the scope qualifier retained in the source audit. The net residue must be assembled **after** including all F/M/G subdivergence/counterterm and geodesic-renormalization contributions consistently. A raw pole from a single diagram is not `B_1`. But once the renormalized highest-pole/H^(2)-type coefficient of the complete observable is known, its separated part fixes `B_1` without the finite `B_0` integrals.

## Attack 5 — nonzero matter-scalar H2 proves nonzero curvature B1

Rejected. The matter scalar has a nonzero separated tree-level propagator and a different operator algebra. Curvature's lower-order separated two-point function is contact-only in the relevant low-energy calculation. Only the structural RG mechanism transfers.

## Attack 6 — if B1 vanishes the entire O(G^2) tail vanishes

Rejected. `B_1=0` leaves the finite constant `B_0` unconstrained. A zero highest-pole/log coefficient would merely force the calculation to continue into the finite nonlog sector.

## Attack 7 — finite observable-specific renormalization can shift B1 arbitrarily

Within the corrected one-loop basis, finite local/geodesic renormalization can shift the constant convention and running bookkeeping but cannot remove or create the separated log coefficient without changing the UV residue/nonlocal observable definition. `B_1` is the RG-invariant coefficient of the physical explicit log in the fixed observable.

## Critic verdict

**CONFIRMS `PASS_SCOPED_SINGLE_LOG_RG_HIERARCHY_HIGHEST_POLE_DIAGNOSTIC_B1_VALUE_OPEN`.**

The lowest-cost unresolved calculation is the complete curvature-specific highest-pole/H^(2) residue across F/M/G. It is strictly smaller than the full finite one-loop coefficient problem and is sufficient to prove noncancellation if nonzero.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.