# ITER135 — terminal result

Classification: **PASS_DIAGNOSTIC_PARTIAL_GATE_OPEN**.

Authoritative production head: `16275060f6110c151cfbba75050c7bf28295fcb9`.
Authoritative run: `34940389488`.

Consumed raw logs and artifacts:
- job `104287516182` (`second-order-source-census`), artifact `10385046903`, sha256 `a28f9c922aee88a608791f86ab72f496a831a81712c20fddf9264160b9c11fc5`;
- job `104287516471` (`dirichlet-green`), artifact `10385460103`, sha256 `698a60b18ac0a5b609cf721535eb4781e3befd92a84c3c88fe2a3ee5151f01fb`.

Scientific assessment against prereg commit `2d1137077c595eee272fa64fbb59e3f9db4d7026`:
- task 2 PASS: Dirichlet Green function endpoint, continuity and derivative-jump checks passed;
- tasks 4–5 PASS at structural source-census level: the three required O(kappa^2) sectors are present with frozen signs/multiplicity and bilinear h counting after xi1 substitution;
- task 8 PASS: target-blind diagnostics;
- tasks 1, 3, 6, 7 remain OPEN: the production run did not explicitly construct S1 from Gamma1, did not emit the xi1 nonlocal line integral, did not test endpoint-reversal covariance of the full source, and did not perform the preregistered >=3 held-out direct perturbative plane-wave/polarization comparisons.

Therefore green CI is **not** scientific closure of ITER135 and neither preregistered terminal PASS label is awarded. No threshold, model, endpoint convention, or metric split is changed. The next allowed gate is a frozen completion gate for the missing tasks 1/3/6/7 only.

Candidate theory remains 0/UNFORMED. Bridge credit remains 0. Claim locks unchanged.