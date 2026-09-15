# ITER136 — second-order geodesic response completion gate

Status: **PREREGISTERED BEFORE PRODUCTION COMPUTE**
Date: 2026-09-15

## Scope
Complete only the frozen ITER135 tasks left open after run 34940389488. Geometry remains 4D Euclidean, `g_ab=delta_ab+kappa h_ab`, `z0=x+t L n`, fixed coordinate endpoints, affine parameter, Dirichlet xi_r(0)=xi_r(1)=0. No B1/EDT/bridge target is available to the calculation.

## Frozen tasks
A. Construct Gamma1 for a generic plane wave `h_ab=e_ab exp(i p.z0)` and explicitly derive `S1^a=-Gamma1^a_bc v^b v^c`.
B. Construct `xi1^a(t)=integral_0^1 G(t,u) S1^a(u) du` and verify its differential equation and both endpoints.
C. Verify endpoint reversal covariance `t->1-t, n->-n` for S1, xi1, and each of the three O(kappa^2) source sectors.
D. For at least three frozen held-out pairs of 4D momenta and symmetric polarizations, compare the symbolic O(kappa) and O(kappa^2) source coefficients against an independently assembled direct perturbative expansion. Require exact symbolic equality where feasible, otherwise relative error <=1e-10.
E. Preserve the ITER135 source census exactly: `-Gamma2(v,v) -(xi1.d)Gamma1(v,v) -2 Gamma1(v,xi1_dot)`.
F. Target-blindness: no desired sign, B1, EDT exponent, bridge target, or fitted coefficient.

## Classification
A–F all pass: `PASS_SCOPED_SECOND_ORDER_PATH_RESPONSE_EQUATIONS_CLOSED_CHI2_ASSEMBLY_OPEN`.
Any genuine algebraic disagreement: `SCIENTIFIC_FAIL_SECOND_ORDER_PATH_RESPONSE_EQUATIONS`.
If algebra is internally consistent but the affine fixed-endpoint convention still lacks authority to define the physical ITER134 chi2 localization observable: `PASS_SCOPED_EQUATIONS_CONVENTION_TO_PHYSICAL_CHI2_AUTHORITY_OPEN`; no chi2 credit.
Infrastructure defects are repairable minimally without changing this prereg.

Candidate theory remains 0/UNFORMED; bridge credit remains 0.