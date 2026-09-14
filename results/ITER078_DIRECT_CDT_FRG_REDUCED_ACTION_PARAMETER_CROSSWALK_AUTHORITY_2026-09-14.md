# ITER078 terminal result — direct CDT/FRG reduced-action and parameter crosswalk authority

Date: 2026-09-14
Gate: `ITER078_DIRECT_CDT_FRG_REDUCED_ACTION_PARAMETER_CROSSWALK_AUTHORITY`
Preregistration commit: `83b414e729cc18033086230fc6833285cf21bace`
Source-authority commit: `0474d9756d23f225e7815aaa58311183dd34b853`
Adversarial-critic commit: `af57c29b4ff879afc389520af7765ce57596d06e`

## Terminal classification

**`PASS_SCOPED / DIRECT_REDUCED_ACTION_PARAMETER_CROSSWALK_RG_SCALE_OPEN`**

Bridge credit: **0**.

## Question adjudicated

Does the direct 2024 CDT↔FRG literature establish a source-defined reduced minisuperspace effective-action / parameter crosswalk, and does it also establish the physical CDT-correlation-length ↔ FRG-RG-scale map required to turn that crosswalk into a common RG flow?

## Result

The reduced-action/parameter crosswalk passes in scope. The RG-scale/correlation-length map remains open.

This is the strongest positive CDT↔FRG structural correspondence established in the programme so far, but it is explicitly a **reduced minisuperspace/effective** result and must not be promoted to microscopic theory equivalence.

## Explicit source-defined crosswalk

The direct source writes the simplest Euclidean Einstein-Hilbert EAA, reduces it to a fixed-four-volume minisuperspace action for the three-volume, and compares it term-by-term with the Monte-Carlo reconstructed CDT scale-factor/three-volume action.

The source derives the mapping

`(N_4, omega, Gamma) -> (V_4(k), omega_0, G_k)`

with

`V_4(k) = (omega_0/omega)^(4/3) N_4 a^4`,

`24 pi G_k = (omega/omega_0)^(4/3) Gamma a^2`,

and the dimensionless relation

`omega^2 Gamma(kappa_0, Delta, N_4) / (omega_0^2 sqrt(N_4)) ~= 1.63 lambda_k g_k`.

Thus the accepted literature supplies the equation-level parameter authority absent from ITER076.

## Time/volume and anisotropy map

The source keeps the measured deformation of the CDT de-Sitter geometry explicit. Instead of setting `omega = omega_0`, it introduces the effective temporal scaling

`a_t = (omega_0/omega)^(4/3) a`

under the stated geometric assumptions, and carries the same ratio into the four-volume and Newton-coupling relations.

This is a mapping between the reduced CDT proper-time coordinate and the continuum minisuperspace proper-time coordinate. It is **not** a map between proper time and FRG RG time.

## Conformal-sign prescription

The opposite signs of the FRG Euclidean minisuperspace action and the measured CDT effective action are explicit in the source. The direct comparison attributes the CDT sign to the entropy/conformal-factor structure and identifies the reduced CDT action with the Hartle-Hawking minisuperspace action after conformal-factor rotation.

ITER078 records this as an explicit scoped prescription, not as proof that the full conformal sectors or measures are identical.

## Coupling authority

At the reduced level the source identifies a measured CDT dimensionless combination built from `omega`, `Gamma` and `N_4` with the FRG product

`lambda_k g_k = G_k Lambda_k`.

This is a genuine parameter crosswalk. It does **not** establish a global isomorphism between CDT bare-coupling space `(kappa_0, Delta, ...)` and FRG theory space `(g_k, lambda_k, ...)`, nor does it determine the two FRG couplings separately without the remaining background/scale information.

## IR / infinite-volume result

The direct/follow-up stack gives a scoped interpretation of the generic `N_4 -> infinity` limit inside the CDT de-Sitter phase in terms of the Gaussian/IR side of the simplest FRG reduced flow. This comparison is source-defined at the reduced-action/coupling-combination level.

No claim is made that all CDT observables or the full CDT transfer dynamics become the full FRG EAA in this limit.

## Putative UV path

The sources use finite-size scaling and the measured behavior of `Gamma` and `omega` to construct a candidate path toward a CDT critical region on which the reduced FRG combination can remain fixed.

The authors explicitly do **not** claim that the available Monte-Carlo precision proves a CDT UV fixed point. ITER078 therefore records:

`PUTATIVE_UV_SCALING_PATH = SOURCE_CONSTRUCTED`

but

`SHARED_UV_FIXED_POINT_ESTABLISHED = false`.

## Exact retained blocker — correlation length versus FRG k

The remaining failure is unusually sharp.

The direct source explicitly states that the precise relation between the geometric CDT correlation length used in finite-size scaling and the FRG coarse-graining scale `k` is not known sufficiently to identify the critical exponents directly.

The follow-up derives formulas in which the lattice spacings contain factors proportional to `1/k`, but then explicitly warns that

`a proportional_to 1/k`

is only a dimensional relation.

The physically nontrivial source statement is weaker: at fixed FRG reduced coupling/scale parameter, the lattice cutoff can tend to zero while the CDT correlation length diverges.

Therefore ITER078 does not establish an operational one-to-one map

`xi_CDT <-> 1/k`

or a source-defined common RG parameter along the full trajectory.

## Frozen predicate results

- A — explicit comparable reduced actions: **PASS**.
- B — explicit parameter map: **PASS**.
- C — time/volume rescaling: **PASS_SCOPED**.
- D — conformal-sign prescription: **PASS_SCOPED**.
- E — deformation/anisotropy retained: **PASS_SCOPED**.
- F — coupling normalization: **PASS_SCOPED**.
- G — reduced/full typing: **PASS_CONTROL**.
- H — IR/infinite-volume identification: **PASS_SCOPED**.
- I — UV caveats retained: **PASS_CONTROL**.
- J — CDT correlation length/finite-size scaling: **PASS_SCOPED**.
- K — operational CDT correlation length ↔ FRG `k`: **OPEN / NOT ESTABLISHED**.
- L — regulator/scheme dependence retained: **PASS_AS_SCOPE_LOCK**.

This predicate pattern maps exactly to the preregistered class:

**`PASS_SCOPED_DIRECT_REDUCED_ACTION_PARAMETER_CROSSWALK_RG_SCALE_OPEN`**.

## Adversarial critic

The critic attempted to demote the result by arguing that the mapping is only a change of variables, that the conformal-sign difference invalidates it, that the round-sphere temporal rescaling is circular, and that only the product `lambda_k g_k` is fixed.

Those objections correctly bound the scope but do not erase the explicit source-defined reduced-action equations.

The critic also attempted the stronger promotion `RG_SCALE_QUALIFIED`; this fails because the source itself calls `a ~ 1/k` dimensional and leaves the correlation-length/`k` relation unresolved.

Critic verdict: **CONFIRMS terminal classification**.

## Structural consequence

ISQGR can now distinguish four levels on the CDT↔FRG route:

1. generic shared language / de-Sitter shape — too weak;
2. common reduced functional motif — established earlier but not a map;
3. **direct equation-level reduced-action/parameter crosswalk — now established in scope**;
4. common operational RG scale / full microscopic theory identity — still not established.

This is a material advance without creating bridge credit.

## Next admissible gate

**`PREREGISTER_ITER079_CDT_FRG_CORRELATION_LENGTH_RG_SCALE_AUTHORITY`**

The next gate should target only the remaining scale-setting question: whether a source-defined physical observable or matching condition relates the geometric CDT correlation length / finite-size-scaling trajectory to the FRG coarse-graining scale `k` beyond dimensional analysis.

No new action matching or target-fit comparison should receive credit unless it closes that exact scale object.

## Claim locks

- `DIRECT_REDUCED_ACTION_PARAMETER_CROSSWALK = true_scoped`
- `CDT_CORRELATION_LENGTH_TO_FRG_K_MAP = false`
- `FULL_THEORY_EQUIVALENCE = false`
- `SHARED_UV_FIXED_POINT_ESTABLISHED = false`
- `BRIDGE_DERIVED = false`
- `UNIVERSAL_COMMON_PARENT_FOUND = false`
- `NEW_PHYSICS_FOUND = false`
- candidate theory = `UNFORMED / 0%`
- bridge credit = `0`