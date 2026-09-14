# ITER082 preregistration — CDT spatial-Laplacian ↔ FRG mode-scale crosswalk authority

Date: 2026-09-15
Gate: `ITER082_CDT_SPATIAL_LAPLACIAN_FRG_MODE_SCALE_CROSSWALK_AUTHORITY`

## Motivation

ITER081 qualified the low-lying CDT spatial-slice Laplace-Beltrami spectrum as an independent scale-sensitive observable, while retaining the mandatory obstruction that the CDT operator acts on three-dimensional spatial slices whereas the established FRG spectral-geometry object acts on the running four-dimensional effective spacetime.

ITER082 asks one narrow source-authority question: is there a source-defined, non-retuned slicing/embedding/operator-normalization map that can connect the CDT spatial-slice eigenvalue scales to an FRG mode-resolution object without identifying `lambda_1 = k^2` by dimensional analogy alone?

This is an authority/type gate, not a numerical fit.

## Frozen source stack

### CDT slice spectral observable
- arXiv:1903.00430 — *Spectral Methods and Running Scales in Causal Dynamical Triangulations*.
- arXiv:1912.11311 — *Spectral Methods in Causal Dynamical Triangulations*.

### Covariant FRG spectral geometry
- arXiv:2203.08003 — *The Spectral Geometry of de Sitter Space in Asymptotic Safety*.

### Foliated/ADM FRG comparator
- arXiv:2306.10408 — *Foliated asymptotically safe gravity in the fluctuation approach*.
- arXiv:2402.01260 — *Global Flows of Foliated Gravity-Matter Systems*.

The foliated sources are frozen prospectively because they explicitly formulate FRG gravity with ADM variables and a spatial metric. Their inclusion does not authorize a CDT↔FRG map unless the required operator and normalization correspondence is actually present.

## Required predicates

A. `CDT_SLICE_OPERATOR_DEFINED`: the exact CDT spatial-slice Laplacian, spectral gap/eigenvalue normalization and continuum scaling semantics are explicit.

B. `FRG_SPATIAL_OPERATOR_DEFINED`: an FRG source explicitly defines the regulator/coarse-graining operator on spatial slices (or an equivalent ADM spatial operator), not merely a foliation of the field variables.

C. `SLICING_DOMAIN_MAP_DEFINED`: the source stack supplies an explicit mathematical map between the CDT spatial slice and the FRG spatial hypersurface/operator domain, including dimensionality and boundary/ensemble semantics.

D. `NORMALIZATION_MAP_DEFINED`: graph/discrete eigenvalues and continuum/operator eigenvalues have an explicit normalization/conversion rule sufficient for comparison.

E. `MODE_SCALE_RULE_DEFINED`: the FRG source defines how the relevant spatial eigenmode corresponds to RG resolution `k`; generic statements that regulator modes are of order `k` or that eigenvalues have mass dimension two are insufficient by themselves.

F. `NO_TARGET_FIT`: no parameter, eigenmode number, scale factor, lapse/anisotropy normalization or proportionality constant may be fitted after looking at the CDT target spectrum.

G. `REGULATOR_LATTICE_SEMANTICS_RETAINED`: regulator dependence, ADM gauge/background dependence, CDT lattice/ensemble dependence and finite-size effects remain explicit.

H. `HELD_OUT_INFORMATION_GAIN`: any authorized map must create information beyond ITER078/079 and ITER081 dimensional reasoning.

## Mandatory controls

- `SPATIAL_SLICE_FULL_SPACETIME_CONTROL`: a 3D CDT slice operator is not the 4D covariant EAA operator.
- `FOLIATION_IS_NOT_OPERATOR_MAP_CONTROL`: an ADM/foliated FRG formulation alone is not a Laplacian-eigenvalue crosswalk.
- `EIGENVALUE_K_CONTROL`: `lambda_CDT = k^2`, `sqrt(lambda_CDT)=k`, or an arbitrary proportionality is forbidden without source authority.
- `NORMALIZATION_FREE_PARAMETER_CONTROL`: an unfixed conversion constant between graph and continuum spectra blocks prediction-grade status.
- `MODE_NUMBER_RETUNING_CONTROL`: choosing a mode index after examining the target spectrum is forbidden.
- `ANISOTROPY_LAPSE_CONTROL`: temporal/spatial scaling and lapse/anisotropy conventions may not be erased.
- `PHASE_ORDER_PARAMETER_CONTROL`: critical closing of the CDT gap is not automatically an FRG cutoff-scale identity.

## Frozen classifications

- `PASS_SCOPED_TYPED_SPATIAL_MODE_SCALE_MAP` only if B-E are explicitly source-qualified and F-H pass. This remains a scoped structural result and gives no bridge credit by itself.
- `PASS_SCOPED_FOLIATED_OPERATOR_CANDIDATE_MAP_NORMALIZATION_OPEN` if a genuinely spatial FRG cutoff/operator exists but the CDT↔FRG normalization/domain map remains missing.
- `SCOPED_BLOCKED_NO_SPATIAL_OPERATOR_CROSSWALK_AUTHORITY` if foliated FRG does not supply the required spatial spectral operator/cross-framework map.
- `SCOPED_BLOCKED_NORMALIZATION_OR_MODE_SCALE_OPEN` if the operator types are close but normalization or the mode↔k rule remains unfixed.
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION` only for technical inability to obtain/evaluate the frozen sources; it is not scientific failure.

## Claim ceiling

No result from ITER082 can establish full CDT/FRG equivalence, a shared UV fixed point, a unique `(g_k,lambda_k)`, bridge derivation, new physics, or candidate theory construction. Candidate theory remains `UNFORMED / 0%`; bridge credit remains zero.

Sources, predicates, controls and classifications are frozen before exact-PDF extraction and manual equation-level adjudication.