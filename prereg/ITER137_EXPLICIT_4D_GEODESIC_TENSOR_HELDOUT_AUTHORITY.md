# ITER137 — explicit 4D geodesic tensor held-out authority
Status: **PREREGISTERED BEFORE PRODUCTION COMPUTE**
Date: 2026-09-15

Frozen geometry and source census are unchanged from ITER135/136.

Required independent lanes:
1. Explicitly instantiate the 4D plane-wave Christoffel tensor `Gamma1^a_bc=(i/2)(p_b e^a_c+p_c e^a_b-p^a e_bc)` and compare `-Gamma1(v,v)` component-by-component against direct differentiation of `h_ab=e_ab exp(i p.z)` for >=3 frozen rational momentum/polarization/vector panels.
2. For the same held-outs, test 4D endpoint reversal and componentwise first-order source covariance; no scalar proxy may stand in for the tensor test.
3. Independently verify the O(kappa^2) geodesic source coefficient by explicit indexed contractions using Gamma1 and the already-authorized Gamma2 tensor representation, rather than abstract G1/G2 symbols. At least three held-out panels, exact equality or relative error <=1e-10.
4. No B1/EDT/bridge target.

Only all required tensor tests passing may close the tensor-authority prerequisite. A genuine mismatch is scientific FAIL; missing executable Gamma2 authority is BLOCKED_MISSING_PREREQUISITE, not a surrogate PASS. Candidate theory remains 0/UNFORMED; bridge credit 0.