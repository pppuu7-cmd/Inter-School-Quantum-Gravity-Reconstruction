# ITER089 terminal result — CDT global covariance as an independent second observable

Date: 2026-09-15
Gate: `ITER089_CDT_GLOBAL_COVARIANCE_SECOND_OBSERVABLE_INDEPENDENCE_AUTHORITY`
Preregistration: `ba4b6733cec302925f537ed0e9dde2e0d7fe315e`
Source authority: `bd74562cc07a0a62b9658524014c5c173b6a3ae2`
Adversarial review: `ba62d9e3aef1a3ea46ccceae4dd772d73e527d9a`

## Terminal classification

**`FAIL_SCOPED_COVARIANCE_REDUNDANT_WITH_REDUCED_ACTION_PARAMETERS`**

Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

## Main result

The measured CDT covariance matrix of global spatial-volume fluctuations is explicitly

`C = P^{-1}`,

where `P` is the Hessian of the same reduced effective action used to obtain the large-volume minisuperspace parameters.

At leading order that action is controlled by:

- the fluctuation normalization `Gamma`;
- the background/profile shape, equivalently `mu/delta/omega` after convention conversion;
- fixed-volume/Lagrange-multiplier conventions.

The direct 2024 CDT↔FRG comparison then shows that fixed-volume minisuperspace fluctuation strength is governed by

`g_eff^2(k) approximately 1.63 g_k lambda_k`.

Therefore the leading covariance eigenmodes/eigenvalues can validate or falsify the reduced action, but they do not provide a second independent functional dependence that separates `g_k` from `lambda_k`.

## Transfer-matrix cross-check

The transfer-matrix method independently reconstructs the same effective Lagrangian and yields parameters consistent with the covariance method. This is strong method validation, not a second physical coupling equation.

The lattice potential parameter conventionally named `lambda` is not source-mapped to the FRG dimensionless cosmological coupling `lambda_k`; it is tied to the fixed-volume effective-action convention and cannot be promoted by name matching.

## Subleading terms

The frozen sources can resolve finite-regulator subleading corrections, but they report that in the large-volume regime these corrections become very small/noise-level and are best interpreted as discretization/finite-size effects rather than established continuum higher-curvature couplings.

No subleading coefficient therefore passes the preregistered independent-continuum-observable criterion.

## Consequence for ITER080

The ITER080 underdetermination is not removed by diagonalizing the CDT covariance matrix. Reusing that matrix after `Gamma` and profile-shape extraction would double-count the same reduced sector.

## Highest-information successor

Before searching higher cumulants, test the stronger algebraic statement suggested by the direct source:

> in the fixed-four-volume Einstein-Hilbert minisuperspace truncation, after dimensionless rescaling the entire global volume-fluctuation distribution depends on the FRG couplings only through the product `g_k lambda_k`.

If this identifiability no-go is exact at the frozen truncation, **no fixed-volume global cumulant of the same scale-factor variable can separate the two couplings**. The route would then have to leave fixed `V_4`, leave the Einstein-Hilbert minisuperspace truncation, or introduce an independently normalized observable from another sector.
