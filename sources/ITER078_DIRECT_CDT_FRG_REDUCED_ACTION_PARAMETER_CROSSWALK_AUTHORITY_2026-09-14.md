# ITER078 source authority — direct CDT/FRG reduced-action and parameter crosswalk

Date: 2026-09-14
Gate: `ITER078_DIRECT_CDT_FRG_REDUCED_ACTION_PARAMETER_CROSSWALK_AUTHORITY`
Preregistration commit: `83b414e729cc18033086230fc6833285cf21bace`

## Frozen source stack

Direct comparison:
- arXiv:2408.07808 — J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, D. Németh, *Is Lattice Quantum Gravity Asymptotically Safe? Making contact between Causal Dynamical Triangulations and the Functional Renormalization Group*.
- arXiv:2411.02330 — J. Ambjørn, J. Gizbert-Studnicki, A. Görlich, D. Németh, *IR and UV limits of CDT and their relations to FRG*.

Native support:
- arXiv:1403.5940 — CDT reduced transfer-matrix/effective-action authority.
- arXiv:1202.2274 — QEG/FRG EAA and running-coupling authority.

## Executive result

Unlike the older source stacks tested in ITER075 and ITER076, the frozen direct-comparison literature **does** give an explicit, equation-level mapping between the reduced CDT scale-factor/three-volume effective action and the simplest Einstein-Hilbert FRG minisuperspace action.

The map retains the CDT shape/deformation parameter, an anisotropic time rescaling, the conformal-sign prescription, four-volume normalization and the effective Newton coupling. It also identifies a specific dimensionless CDT combination with the FRG product `lambda_k g_k`.

However, the same source stack explicitly stops short of a genuine renormalization-scale identity: its derived `a proportional_to 1/k` relation is called only dimensional, while the physically nontrivial statement is that at **fixed** FRG coupling/scale parameter the lattice spacing tends to zero when the CDT correlation length diverges. A source-defined one-to-one `xi_CDT <-> 1/k` map is not established.

Therefore the source-authority classification is:

**`PASS_SCOPED_DIRECT_REDUCED_ACTION_PARAMETER_CROSSWALK_RG_SCALE_OPEN`**.

Bridge credit remains zero.

## A — explicit comparable reduced actions

**PASS.**

The direct source writes the simplest Euclidean Einstein-Hilbert EAA

`Gamma_k[g] = (16 pi G_k)^(-1) int sqrt(g) (-R + 2 Lambda_k)`

and reduces it to a fixed-four-volume minisuperspace action for the three-volume `V_3(t)`.

On the CDT side it uses the Monte-Carlo reconstructed scale-factor/three-volume effective action in terms of the discrete volume variable `N_3(t_i)`, with measured parameters `Gamma` and `omega` controlling fluctuations and the de-Sitter-volume profile.

This is a term-level action comparison, not a visual `cos^3` shape comparison.

## B — explicit parameter map

**PASS.**

The paper derives the source-defined map

`(N_4, omega, Gamma) -> (V_4(k), omega_0, G_k)`

with

`V_4(k) = (omega_0/omega)^(4/3) N_4 a^4`,

`24 pi G_k = (omega/omega_0)^(4/3) Gamma a^2`.

It then obtains the dimensionless combination

`omega^2 Gamma(kappa_0, Delta, N_4) / (omega_0^2 sqrt(N_4)) ~= 1.63 lambda_k g_k`.

Thus the direct stack closes exactly the type of equation-level parameter authority absent from ITER076.

## C — time/volume rescaling

**PASS_SCOPED.**

The source does not simply equate the deformed CDT four-sphere with a round FRG sphere. It introduces separate spatial and temporal lattice scales and chooses the effective temporal scale so that the continuum proper-time extension and spatial extension match the round-sphere geometry. In the source notation this gives

`a_t = (omega_0/omega)^(4/3) a`

within the stated simplifying geometric conventions.

The fixed-volume relation is carried through explicitly when translating sums over `N_3(t_i)` into the continuum `V_3(t)` action.

This maps CDT reduced proper-time coordinates to the minisuperspace proper-time coordinate. It does **not** identify proper time with FRG RG time.

## D — conformal-sign issue

**PASS_WITH_EXPLICIT_PRESCRIPTION.**

The direct source explicitly notes that the FRG minisuperspace action and the measured CDT effective action have opposite signs. It does not erase the discrepancy.

It argues that the lattice entropy/Boltzmann-weight structure changes the conformal-factor behavior and states that the CDT minisuperspace action is the Hartle-Hawking action after conformal-factor rotation. The sign difference is therefore treated as part of the correspondence prescription.

This is a scoped prescription at the reduced-action level, not a proof that the full conformal sectors are identical.

## E — deformation / anisotropy retained

**PASS_SCOPED.**

The measured CDT parameter `omega` is generally different from the round-sphere value `omega_0`. The source retains the ratio `omega/omega_0` explicitly in the temporal rescaling, four-volume map and Newton-coupling map.

Thus `OMEGA_ROUND_SPHERE_ERASURE_CONTROL` does not trigger: the deformation is translated rather than silently set to zero.

The authors also state the simplifying assumptions under which their spacelike/timelike simplex-volume treatment is used. The result remains an effective reduced mapping, not an exact microscopic anisotropy theorem.

## F — coupling normalization

**PASS_SCOPED.**

The mapping identifies the reduced CDT combination built from `Gamma`, `omega` and `N_4` with `lambda_k g_k = G_k Lambda_k` up to the explicit numerical/geometric normalization carried by the source.

The direct source also retains the distinction between dimensionful `G_k, Lambda_k` and dimensionless `g_k, lambda_k`, with

`G_k = g_k/k^2`, `Lambda_k = lambda_k k^2`.

This is materially stronger than symbol matching: the CDT effective observables enter an explicit dimensionless FRG coupling combination.

## G — reduced/full typing

**PASS_CONTROL.**

The correspondence is explicitly constructed after reducing both descriptions to a scale-factor/three-volume minisuperspace sector. The FRG side is the simplest Einstein-Hilbert truncation; the CDT side is the reduced effective scale-factor action obtained after integrating/summing over the other degrees of freedom.

Nothing in the frozen stack identifies:

- the full CDT triangulation-state transfer matrix with the full EAA;
- microscopic CDT histories with FRG field configurations;
- full gauge/background sectors;
- complete observables or state spaces.

`FULL_REDUCED_ACTION_SWAP_CONTROL` therefore remains a hard lock.

## H — infinite-volume / IR identification

**PASS_SCOPED.**

The direct paper identifies the generic `N_4 -> infinity` limit inside the de-Sitter phase with the Gaussian fixed-point limit or an FRG IR fixed-point limit at the reduced-coupling level.

The follow-up derives the same interpretation through the lattice correlation-length/finite-size-scaling picture: fixed bare CDT couplings with diverging correlation length correspond to an IR flow of the renormalized reduced coupling.

This is an identification within the simplest reduced comparison, not a theorem that all CDT observables reproduce the FRG IR theory.

## I — putative UV fixed point kept provisional

**PASS_CONTROL.**

The source constructs a candidate UV scaling path using the measured critical behavior of `Gamma` and `omega`. It derives necessary scaling conditions and a path that keeps `lambda_k g_k` fixed while approaching the candidate lattice critical point.

But the authors explicitly state that Monte-Carlo precision does **not** prove existence of the UV fixed point. The follow-up concludes that the data allow such a fixed point but are not strong evidence sufficient to decide the question.

No UV theorem is promoted in ITER078.

## J — CDT correlation length / finite-size scaling

**PASS_SCOPED.**

The direct/follow-up stack gives a diffeomorphism-invariant quantum-gravity correlation-length construction based on geometric two-point functions and finite-size scaling. In 4D CDT, `N_4^(1/4)` is used as the relevant correlation-length scale in the de-Sitter phase/scaling analysis, with the important qualifier that this correlation length is not the propagation length of an ordinary field degree of freedom.

The pseudocritical approach and critical exponents are expressed in terms of this scaling variable.

## K — correlation length versus FRG `k`

**OPEN / NOT FULLY SOURCE-QUALIFIED.**

This is the retained blocker.

The 2024 paper explicitly says that the precise connection between the CDT correlation length `xi ~ N_4^(1/4)` used to derive the lattice critical exponent and the FRG scale parameter `k` is not known well enough for a direct critical-exponent comparison.

The follow-up contains a section titled, in substance, the **enigmatic relation between `a` and `k`**. It derives relations in which `a` and `a_t` carry a factor `1/k` near the putative UV regime, but then explicitly states that `a proportional_to 1/k` is **only a dimensional relation**. The physical content is instead that for fixed `k` / fixed `lambda_k g_k`, the lattice cutoff tends to zero as the CDT correlation length diverges.

Therefore the frozen stack does not establish a one-to-one operational identification

`k = c / xi_physical`

or `xi_CDT = c/k` valid along the full cross-framework RG trajectory.

`CORRELATION_LENGTH_K_SWAP_CONTROL` remains active.

## L — regulator/scheme dependence

**PASS_AS_SCOPE_LOCK.**

The map does not erase the fact that:

- CDT is a lattice regularization with bare parameters, dynamical triangulations, finite-size scaling and a reduced Monte-Carlo effective action;
- FRG uses a regulator-dependent EAA and the simplest Einstein-Hilbert truncation.

The direct comparison targets a reduced invariant/effective sector; it is not promoted to a scheme-independent full-theory identity.

## Mandatory controls

- `DE_SITTER_SHAPE_ONLY_CONTROL`: **passes**; explicit action/parameter equations go beyond shape matching.
- `CONFORMAL_SIGN_ERASURE_CONTROL`: **passes**; sign difference and conformal rotation are explicit.
- `OMEGA_ROUND_SPHERE_ERASURE_CONTROL`: **passes**; `omega/omega_0` remains in the map.
- `PROPER_TIME_RG_TIME_SWAP_CONTROL`: **passes**; reduced proper time is not RG time.
- `CORRELATION_LENGTH_K_SWAP_CONTROL`: **triggers**; this is the retained RG-scale blocker.
- `BARE_EFFECTIVE_RUNNING_SWAP_CONTROL`: **passes as a type lock**; bare CDT parameters, measured reduced coefficients and FRG running couplings remain distinguished.
- `FULL_REDUCED_ACTION_SWAP_CONTROL`: **passes as a hard ceiling**.
- `REGULATOR_ERASURE_CONTROL`: **passes as a hard ceiling**.
- `UV_FIXED_POINT_PROMOTION_CONTROL`: **passes**; UV status remains putative/evidence-level.
- `FIT_CIRCULARITY_CONTROL`: **passes as a limitation**; the reduced map uses the measured CDT action parameters and therefore is not independent microscopic validation.
- `IR_UV_LIMIT_CONFLATION_CONTROL`: **passes**; IR/infinite-volume and putative UV paths are treated separately.

## Frozen predicate summary

- A explicit reduced actions: **PASS**
- B explicit parameter map: **PASS**
- C time/volume rescaling: **PASS_SCOPED**
- D conformal-sign prescription: **PASS_SCOPED**
- E deformation/anisotropy retained: **PASS_SCOPED**
- F coupling normalization: **PASS_SCOPED**
- G reduced/full typing: **PASS_CONTROL**
- H IR identification: **PASS_SCOPED**
- I UV caveats retained: **PASS_CONTROL**
- J CDT correlation length/scaling: **PASS_SCOPED**
- K CDT correlation length <-> FRG `k`: **OPEN / NOT ESTABLISHED AS AN OPERATIONAL MAP**
- L regulator/scheme retained: **PASS_AS_SCOPE_LOCK**

## Source-authority classification

**`PASS_SCOPED_DIRECT_REDUCED_ACTION_PARAMETER_CROSSWALK_RG_SCALE_OPEN`**

This is the strongest positive CDT↔FRG structural result reached in the programme so far, but its scope is narrow and explicit:

- reduced minisuperspace action/parameter crosswalk: **established in scope**;
- full microscopic/action/state-space equivalence: **not established**;
- operational CDT correlation-length ↔ FRG `k` map: **open**;
- shared/proven UV fixed point: **not established**;
- bridge credit: **0**.

## Claim ceiling

No `BRIDGE_DERIVED`, no universal common parent, no candidate theory, no proof of asymptotic safety for CDT, and no proof that the full CDT continuum theory equals the FRG/QEG theory.