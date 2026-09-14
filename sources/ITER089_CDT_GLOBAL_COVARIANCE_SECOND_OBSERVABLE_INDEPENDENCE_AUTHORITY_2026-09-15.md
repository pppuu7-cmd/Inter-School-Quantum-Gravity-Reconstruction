# ITER089 source authority — CDT global covariance as an independent second observable

Date: 2026-09-15
Gate: `ITER089_CDT_GLOBAL_COVARIANCE_SECOND_OBSERVABLE_INDEPENDENCE_AUTHORITY`
Preregistration: `ba4b6733cec302925f537ed0e9dde2e0d7fe315e`

## 1. Covariance is explicitly the inverse Hessian of the same effective action

arXiv `1510.08719`, Sec. 3, expands the CDT effective action around the semiclassical average volume profile and defines

`P_tt' = partial^2 S_eff / (partial n_t partial n_t') |_(n=bar n)`.

For Gaussian fluctuations it then gives

`C_tt' = <delta n_t delta n_t'> = (P^{-1})_tt'`.

The source states directly that numerical measurement of `C` and inversion to `P` reconstructs the second derivatives of the effective action.

Therefore the eigenvalues/eigenvectors of the leading covariance matrix are not a separate dynamical sector: they are the fluctuation spectrum of the same reduced action.

## 2. Leading large-volume action contains the already-used fluctuation and shape parameters

The CDT effective action in the de-Sitter phase is source-parametrized as

`S_eff = (1/Gamma) sum_t [ (n_t-n_(t+1))^2/(2 n_t) - lambda n_t + mu n_t^(1/3) ]`

(up to equivalent symmetrized discretizations and the fixed-volume treatment).

The source explains:

- `Gamma` controls the amplitude of quantum fluctuations and is proportional to `a_s^2/G`;
- `mu` is related to the temporal width/shape of the semiclassical solution;
- lattice `lambda` is a Lagrange multiplier fixing total volume in this effective description.

The direct 2024 source arXiv `2408.07808` rewrites the same large-volume reduced information as

`<n_3(s)> = (3/(4 omega)) cos^3(s/omega)`

and

`S_eff = sqrt(N_4)/Gamma * integral ds [ dot(n_3)^2/n_3 + delta n_3^(1/3) ]`,

with

`delta/delta_0 = (omega_0/omega)^(8/3)`.

Thus the shape part of the leading Hessian is fixed by the same mean-profile parameter `omega` (equivalently `delta`/`mu` after convention conversion), while the overall fluctuation normalization is `Gamma`.

## 3. Direct FRG comparison confirms that global two-point fluctuations depend on the coupling product

The direct source studies the fixed-four-volume minisuperspace action and states that fluctuations around the classical `S^4` are governed by

`g_eff^2(k) = 24 pi G_k / sqrt(V_4(k)) = (4/sqrt(6)) Lambda_k G_k approximately 1.63 lambda_k g_k`.

The relative fluctuation amplitude is `O(g_eff)`. The paper also notes that for compact space only constant spatial modes contribute to fluctuations of global quantities such as the three-volume; these are precisely the minisuperspace modes used in the comparison.

Therefore the leading global covariance sector supplies the same coupling combination already used in ITER078. Diagonalizing `C` does not create a second independent dependence on `g_k` versus `lambda_k`.

## 4. The lattice parameter named `lambda` is not the FRG dimensionless cosmological coupling

The older CDT effective-action/transfer-matrix notation includes a parameter `lambda` multiplying a term linear in volume. In the covariance/minisuperspace reconstruction this parameter enforces/fits the total-volume condition and is convention-dependent under the volume-fixing setup.

The 2024 direct comparison deliberately performs the continuum comparison at fixed `V_4`, where the physically relevant fluctuation strength is expressed through `G_k/sqrt(V_4)` or equivalently `g_k lambda_k` after inserting the self-consistent FRG de-Sitter volume.

No frozen source derives an identity between the transfer-matrix/lattice `lambda` and the FRG dimensionless `lambda_k`. Name equality therefore gives no independent equation.

## 5. Transfer-matrix agreement is a method cross-check, not an extra observable

The transfer-matrix method independently measures the same effective Lagrangian and finds parameters consistent with the covariance reconstruction. For a representative large-volume de-Sitter point it fits `Gamma`, `mu`, and a volume potential parameter `lambda`, and the source explicitly states that the transfer-matrix and covariance methods are fully consistent.

This is strong methodological validation of the reduced action. It does not increase the number of independent continuum couplings when both methods parameterize the same `S_eff`.

## 6. Subleading corrections do not supply a stable continuum second observable in the frozen stack

The covariance analysis can resolve subleading kinetic/curvature-like corrections such as `xi_2`. The source reports a nonzero finite-regulator fit for some such coefficients, but its later scale/volume analysis concludes that the observed subleading corrections are best interpreted as discretization/finite-size effects rather than established higher-derivative continuum terms.

In the large-volume transfer-matrix regime the subleading coefficients become very small and are difficult to distinguish from numerical noise. The source explicitly says the large-volume effective action is very well described by the simple minisuperspace form and that subleading corrections, if present, are at the noise level.

Therefore no frozen subleading coefficient satisfies the preregistered requirement of a stable, source-qualified large-volume continuum coupling independent of `Gamma` and `omega`.

## Predicate adjudication

- A covariance-Hessian relation: **PASS**.
- B leading action/parameter content explicit: **PASS**.
- C leading Hessian fixed by known reduced-action parameters: **PASS_SCOPED**.
- D extra large-volume continuum parameter: **NO** in frozen stack.
- E lattice `lambda` kept distinct from FRG `lambda_k`: **PASS_CONTROL**.
- F stable continuum subleading coefficient: **NO / finite-size-discretization status retained**.
- G covariance eigenmodes treated as consistency checks rather than double-counted constraints: **PASS_CONTROL**.
- H no post-hoc FRG use: **PASS_CONTROL**.

## Source classification

**`FAIL_SCOPED_COVARIANCE_REDUNDANT_WITH_REDUCED_ACTION_PARAMETERS`**

The failure is useful: it prevents double-counting the same global fluctuation data as a second coupling constraint. The covariance/Hessian sector strongly validates the minisuperspace effective action, but at leading large volume it carries the same `Gamma` + shape information already used by ITER078.

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**.

## Highest-information successor

A viable second global observable must be **outside the Gaussian two-point covariance of `N_3(t)`**. The frozen source stack suggests two possibilities:

1. a genuinely held-out non-Gaussian/higher cumulant of the global volume fluctuations with a source-derived FRG minisuperspace counterpart; or
2. a source-qualified response derivative across bare couplings/volume (for example a susceptibility or renormalized deformation response) whose dependence is not algebraically fixed by `Gamma` and `omega`.

Before either route, source authority must establish that the observable is not merely a reparameterization of the same leading effective action.
