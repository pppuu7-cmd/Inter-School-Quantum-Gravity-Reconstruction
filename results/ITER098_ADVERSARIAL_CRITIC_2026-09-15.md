# ITER098 adversarial critic — multivariate response-object mapping

Date: 2026-09-15
Gate: `ITER098_PUBLISHED_MULTIVARIATE_RESPONSE_OBJECT_AUTHORITY`

## Target under attack

Provisional classification: genuine multivariate CDT covariance/Hessian objects exist, but in a reduced spatial-volume variable space rather than the ITER093 bare-coupling response basis.

## Rescue attempt 1 — identify spatial volume with total four-volume

Rejected. A time-slice spatial-volume profile does not uniquely determine `N_0`, `N_41`, and `N_32`, and the exact action-conjugate basis cannot be reconstructed from profile covariance alone.

## Rescue attempt 2 — use `C^{-1}` as the desired Fisher matrix

Rejected by index/domain mismatch. `C^{-1}_{tt'}` is a Hessian of an effective action with respect to reduced profile variables `n_t`; ITER093 requires covariance/Hessian with respect to bare couplings/action-conjugate observables. The matrices do not even have the same index set.

## Rescue attempt 3 — invoke chain rule

A chain-rule transformation would require an explicit Jacobian between reduced variables and the bare action-conjugate observables, plus control of the integration-out map. No frozen source supplies such an invertible map.

## Rescue attempt 4 — use transfer-matrix parameters as bare coupling responses

Rejected. Effective transfer-matrix fit parameters are reduced dynamical parameters. Their dependence on bare couplings can be scientifically interesting, but without a source-defined Jacobian it does not reconstruct `Cov(A_i,A_j)`.

## Rescue attempt 5 — assume universality of principal directions

Rejected. Similar principal directions in two projected descriptions would be an empirical observation requiring a common map, not a license to identify their vector spaces.

## Critic verdict

`PASS_SCOPED_MULTIVARIATE_OBJECT_EXISTS_DIFFERENT_DOMAIN` survives.

The useful positive fact is that CDT has source-qualified cross-information in effective spatial-volume space. The useful negative fact is that this does not reopen ITER093. Any future bridge must derive, not assume, a map between the reduced effective variables and the microscopic action-conjugate response basis.
