# ITER078 preregistration — direct CDT/FRG reduced-action and parameter crosswalk authority

Date: 2026-09-14
Gate: `ITER078_DIRECT_CDT_FRG_REDUCED_ACTION_PARAMETER_CROSSWALK_AUTHORITY`

## Motivation

ITER075 rejected physical effective-action equivalence in an older frozen source stack, retaining only a common de-Sitter/minisuperspace functional structure. ITER076 found no explicit CDT-to-FRG coupling map in its older frozen stack. A later direct comparison paper, identified only after those gates were frozen, explicitly compares the CDT scale-factor effective action to the simplest FRG minisuperspace effective action and proposes parameter identifications. It must therefore be tested prospectively in its own gate rather than imported retroactively.

## Frozen question

Does the direct 2024 CDT↔FRG literature establish a source-defined, non-forgetful **reduced minisuperspace effective-action / parameter crosswalk** between the CDT de-Sitter phase and the simplest FRG Einstein-Hilbert minisuperspace sector, while preserving:

- reduced variable and time normalization;
- fixed four-volume constraint;
- kinetic/potential terms and their signs;
- conformal-factor prescription;
- CDT deformation/anisotropy parameters;
- Newton/cosmological coupling normalization;
- finite-size/continuum scaling;
- distinction between CDT correlation length and FRG RG scale `k`;
- distinction between reduced-action matching and full microscopic equivalence?

A separate predicate asks whether the same source stack closes the **RG-scale/correlation-length map**. Reduced-action matching cannot automatically satisfy that predicate.

## Frozen sources

Direct comparison:
- arXiv:2408.07808 — J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, D. Németh, *Is Lattice Quantum Gravity Asymptotically Safe? Making contact between Causal Dynamical Triangulations and the Functional Renormalization Group*.
- arXiv:2411.02330 — J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, D. Németh, *IR and UV limits of CDT and their relations to FRG*.

Native supporting authority, frozen prospectively:
- arXiv:1403.5940 — CDT reduced transfer-matrix/effective-action authority.
- arXiv:1202.2274 — QEG/FRG EAA and dimensionless-running-coupling authority.

No source outside this frozen stack may upgrade ITER078 after result inspection.

## Required predicates

A. Both reduced actions are written explicitly in variables that can be compared after a source-defined rescaling, rather than by visual de-Sitter-profile similarity alone.

B. The direct source gives explicit equations mapping the CDT reduced parameters/observables (such as `N4`, volume-profile deformation `omega`, fluctuation/effective-action coefficient `Gamma` or equivalent) to FRG minisuperspace quantities (such as `V4(k)`, Newton coupling `G_k`, cosmological/radius parameter, or dimensionless combinations).

C. The time/volume rescaling used in the mapping is explicit, including how discrete CDT proper time and the continuum minisuperspace coordinate are related. This does **not** authorize identifying either with FRG RG time.

D. The opposite-sign/conformal-mode issue between Euclidean Einstein-Hilbert minisuperspace and the CDT reconstructed action is explicitly source-adjudicated (for example by a conformal-factor rotation/prescription). The sign cannot be silently flipped.

E. CDT deformation/anisotropy relative to a round four-sphere is retained in the map; `omega` or equivalent cannot be set to its round-sphere value without source authority.

F. Coupling normalization is explicit enough to identify which combination of CDT effective parameters corresponds to `G_k`, `Lambda_k`, `g_k lambda_k`, or another FRG quantity. Unknown proportionality constants/geometry factors must remain visible.

G. The map is typed as a **reduced minisuperspace/effective-action** crosswalk. It cannot be promoted to equality of full CDT transfer dynamics, microscopic path integrals, full EAA functionals, gauge/background sectors, or state spaces.

H. The infinite-volume / IR identification is source-qualified with its assumptions and limiting procedure.

I. The putative CDT UV fixed-point construction is separated from proof: finite-size scaling, phase-boundary location/order and Monte-Carlo precision/caveats remain explicit.

J. The source-defined CDT correlation length / finite-size scaling variable is identified and its physical meaning stated.

K. A source-defined map between the CDT correlation length (or cutoff trajectory) and the FRG coarse-graining scale `k` is required for an RG-scale crosswalk. Dimensional analogy `k ~ 1/a` or `k ~ 1/xi` is insufficient without the source's derivation and validity range.

L. Regulator/scheme dependence on both sides remains explicit. Reduced-action agreement cannot erase lattice regularization, FRG cutoff/truncation, or projection dependence.

## Frozen classifications

- `PASS_SCOPED_DIRECT_REDUCED_ACTION_PARAMETER_CROSSWALK_RG_SCALE_QUALIFIED` only if A-L pass, including an explicit CDT correlation-length ↔ FRG `k` relation.
- `PASS_SCOPED_DIRECT_REDUCED_ACTION_PARAMETER_CROSSWALK_RG_SCALE_OPEN` if A-J and L pass sufficiently to establish the reduced-action/parameter map while K remains open or explicitly unresolved.
- `PASS_SCOPED_PARTIAL_PARAMETER_MAP_ONLY` if a subset of reduced parameters is explicitly related but action/sign/normalization/limit structure is incomplete.
- `SCOPED_BLOCKED_DIRECT_MAP_AUTHORITY` if the direct sources remain too qualitative to establish even a reduced map.
- `FAIL_SCOPED_DIRECT_REDUCED_MAP_REJECTED` if the direct proposed map fails its own source-defined consistency conditions.
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION` only for source-access failure.

## Mandatory controls

- `DE_SITTER_SHAPE_ONLY_CONTROL`: a common `cos^3`/four-sphere profile alone cannot pass.
- `CONFORMAL_SIGN_ERASURE_CONTROL`: opposite kinetic/conformal signs cannot be ignored.
- `OMEGA_ROUND_SPHERE_ERASURE_CONTROL`: CDT deformation/anisotropy cannot be erased.
- `PROPER_TIME_RG_TIME_SWAP_CONTROL`: minisuperspace/proper time cannot be identified with RG time.
- `CORRELATION_LENGTH_K_SWAP_CONTROL`: CDT `xi` cannot be set to `1/k` without source derivation.
- `BARE_EFFECTIVE_RUNNING_SWAP_CONTROL`: bare lattice parameters, CDT effective coefficients and FRG running couplings remain distinct categories unless mapped.
- `FULL_REDUCED_ACTION_SWAP_CONTROL`: reduced action matching cannot become full-theory equality.
- `REGULATOR_ERASURE_CONTROL`: CDT lattice and FRG cutoff/truncation structures remain explicit.
- `UV_FIXED_POINT_PROMOTION_CONTROL`: source-supported compatibility/putative UV fixed point cannot be promoted to proof.
- `FIT_CIRCULARITY_CONTROL`: parameters fitted from the same CDT reduced data cannot count as independent validation of the microscopic theory.
- `IR_UV_LIMIT_CONFLATION_CONTROL`: Gaussian/IR and putative UV limits must remain distinct.

## Claim ceiling

Even the strongest PASS can establish only a source-qualified **reduced minisuperspace effective-action/parameter crosswalk** and, if K passes, a scoped scale relation. It cannot establish microscopic CDT/FRG equivalence, equality of full dynamics, universal common parent, proven shared UV fixed point, `BRIDGE_DERIVED`, new physics, or a candidate theory.

Candidate theory remains `UNFORMED / 0%`; bridge credit remains zero absent a later constitutional gate.

Predicates, classifications and controls are frozen prospectively before detailed equation-level adjudication.