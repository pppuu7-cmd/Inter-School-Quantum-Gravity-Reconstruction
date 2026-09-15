# ITER133 — fixed-geodesic localization-kernel prerequisite gate

Date: 2026-09-15

## Frozen gate
Preregistered at commit `6a60c8fc0519d7641e31004cd1078ce7408f3512`. Production head `385257511705240128482a5680b05746058a4e1c`. Frozen classification on all A–F checks for covered objects: `PASS_SCOPED_DERIVATIVE_AND_CHI1_KERNELS_CLOSED_CHI2_OPEN`.

## Authoritative run
Run `34926966782` completed success. Green CI alone was not used as scientific evidence; raw job logs and artifacts were consumed against the preregistered predicates.

### Lane: chi1-line-kernel
- job `104246950120`
- artifact `10380014169`, `iter133-chi1-line-kernel`
- digest `sha256:8df334fc847f47165ce41135f3493a7d9045e7158f584c69e6a93c8b032f169d`
- explicit kernel: `K_ab(tau,p;n)=n_a n_b exp(i tau p.n)`
- D=4: PASS
- target blind: PASS
- affine kernel retained: PASS
- endpoint reversal covariance: PASS
- held-out direct check: PASS
- scope explicitly defers overall segment/world-function normalization and makes no chi2 claim.

### Lane: curvature-derivatives
- job `104246950236`
- artifact `10379428829`, `iter133-curvature-derivatives`
- digest `sha256:8aa399e3d12bcc2090553f765c6662f8065f50566dbadc8f14234502e249ef5d`
- objects: `dR1_mu=i p_mu R1`, `d2R1_munu=-p_mu p_nu R1`
- D=4: PASS
- target blind: PASS
- exact homogeneity `dR1:3`, `d2R1:4`: PASS
- held-out direct check: PASS

## Scientific classification
`PASS_SCOPED_DERIVATIVE_AND_CHI1_KERNELS_CLOSED_CHI2_OPEN`.

This closes only the covered differentiated linear-curvature and first-order affine localization kernels. It does not close `chi2`, does not reopen frozen ITER132 by itself, does not compute a pole residue or B1, and gives no bridge/new-physics/candidate-theory credit.

## Next admissible gate
Prospectively preregister an explicit second-order fixed-geodesic/world-function localization kernel `chi2` and the differentiated localization variants actually required by the seven frozen ITER132 M/G families. The gate must preserve affine ordering, endpoint-reversal covariance, D=4 tensor structure, target blindness, held-out direct checks, and must not replace the nonlocal kernels by scalar proxies. Only after those prerequisites close may unchanged ITER132 be rerun.
