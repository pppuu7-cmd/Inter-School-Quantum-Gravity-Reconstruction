# ITER078 adversarial critic — direct CDT/FRG reduced-action and parameter crosswalk

Date: 2026-09-14
Preregistration: `83b414e729cc18033086230fc6833285cf21bace`
Source-authority audit: `0474d9756d23f225e7815aaa58311183dd34b853`

## Target

Attempt to falsify or strengthen:

`PASS_SCOPED_DIRECT_REDUCED_ACTION_PARAMETER_CROSSWALK_RG_SCALE_OPEN`.

## Attack 1 — Eq. (40) is only a convenient change of variables, not a physical crosswalk

The direct source indeed makes a deliberate reduced-model choice: it adjusts the effective temporal lattice scale so that the deformed CDT four-sphere is associated with a round continuum four-sphere. This is not a unique microscopic map.

However, the gate is explicitly scoped to the **reduced minisuperspace effective-action/parameter** level. Within that scope the source carries the transformation through the kinetic term, potential term, fixed-volume constraint and Newton-coupling coefficient and writes the map explicitly. The transformation is therefore more than a visual reparameterization, though its assumptions must remain attached.

**Verdict: scoped crosswalk survives; microscopic promotion remains forbidden.**

## Attack 2 — the opposite action sign invalidates the map

The sign mismatch is real and would invalidate an unqualified equality. But the direct source does not hide it: it explicitly connects the CDT sign to the entropy/conformal-factor problem and identifies the measured reduced action with the Hartle-Hawking minisuperspace action after conformal-factor rotation.

This is a source-defined prescription sufficient for a scoped reduced-action correspondence. It is not evidence that the full conformal sector or full EAA measure is the same.

**Verdict: no demotion below the scoped PASS; retain conformal-sign ceiling.**

## Attack 3 — choosing `a_t` to enforce a round sphere makes the result circular

The rescaling is partly a convention chosen to compare the anisotropically deformed CDT geometry with the round GR/FRG four-sphere. That means the roundness match itself is not independent evidence.

But the resulting source equations also constrain the kinetic coefficient and yield the nontrivial combination relating `omega^2 Gamma / sqrt(N_4)` to `lambda_k g_k`. The gate does not count roundness as independent validation; it counts the source-defined parameter translation.

**Verdict: `FIT_CIRCULARITY_CONTROL` limits evidential weight but does not erase the explicit map.**

## Attack 4 — `omega` is erased by the mapping

Rejected. `omega/omega_0` appears explicitly in `a_t`, `V_4(k)` and `G_k`. The direct source discusses the fact that measured `omega` generally differs from the round-sphere value and uses that difference to rescale temporal versus spatial directions.

**Verdict: deformation/anisotropy is retained at the reduced level.**

## Attack 5 — the map only fixes `lambda_k g_k`, not `g_k` and `lambda_k` separately

This is an important ceiling. The clean dimensionless lattice relation is to the product `lambda_k g_k = G_k Lambda_k`. Individual running couplings are reconstructed only together with the de-Sitter volume/radius relation and the chosen scale/background conventions.

The gate does not claim a global coordinate isomorphism of theory spaces. It claims a reduced-action/parameter crosswalk with explicit combinations.

**Verdict: scoped PASS survives; no full coupling-space map.**

## Attack 6 — `a proportional_to 1/k` in the follow-up closes the RG-scale predicate K

The follow-up itself prevents this promotion. After deriving formulas containing `1/k`, it explicitly says that `a proportional_to 1/k` is **just a dimensional relation**. The substantive statement is that at fixed `k` / fixed reduced FRG coupling combination, the lattice cutoff goes to zero when the CDT correlation length diverges.

This does not provide a one-to-one operational map between the geometric CDT correlation length and FRG coarse-graining resolution along arbitrary trajectories.

**Verdict: K remains OPEN; strongest classification with RG-scale-qualified is rejected.**

## Attack 7 — finite-size scaling proves the shared UV fixed point

Rejected. The source derives necessary scaling conditions and reports exponents close to the limiting inequalities needed for a candidate UV path. It then says explicitly that the data precision is not sufficient to decide/prove the CDT UV fixed point.

**Verdict: `UV_FIXED_POINT_PROMOTION_CONTROL` succeeds.**

## Attack 8 — identify the CDT critical exponent directly with an FRG critical exponent

The direct paper explicitly notes that such a comparison is obstructed by the unknown precise connection between its CDT correlation length and FRG scale `k`. Thus even the authors do not promote the measured lattice exponent to an FRG critical exponent by simple equality.

**Verdict: no critical-exponent bridge.**

## Attack 9 — the map should be classified only `PARTIAL_PARAMETER_MAP_ONLY`

Too weak. The frozen direct stack supplies all of the following together:

- explicit reduced actions;
- fixed-volume mapping;
- time/anisotropy rescaling;
- explicit conformal-sign prescription;
- equations mapping `(N_4, omega, Gamma)` to `(V_4(k), omega_0, G_k)`;
- a dimensionless relation to `lambda_k g_k`;
- an IR/infinite-volume interpretation;
- a finite-size-scaling construction for a putative UV path.

The missing object is specifically the operational CDT-correlation-length ↔ FRG-`k` map, not the reduced-action/parameter crosswalk itself.

**Verdict: retain `PASS_SCOPED_DIRECT_REDUCED_ACTION_PARAMETER_CROSSWALK_RG_SCALE_OPEN`.**

## Attack 10 — reduced-action matching implies full CDT/FRG equivalence

Rejected by construction. The source comparison integrates/sums out almost all CDT degrees of freedom and uses the simplest FRG Einstein-Hilbert minisuperspace sector. Many inequivalent microscopic theories can share the same reduced effective dynamics.

**Verdict: `FULL_REDUCED_ACTION_SWAP_CONTROL` remains a hard claim ceiling.**

## Critic verdict

**CONFIRMS `PASS_SCOPED_DIRECT_REDUCED_ACTION_PARAMETER_CROSSWALK_RG_SCALE_OPEN`.**

Durable factorization:

- `DIRECT_REDUCED_ACTION_CROSSWALK = established_scoped`
- `CDT_N4_OMEGA_GAMMA_TO_FRG_V4_GK_MAP = established_scoped`
- `CDT_DIMENSIONLESS_COMBINATION_TO_LAMBDAK_GK = established_scoped`
- `CONFORMAL_SIGN_PRESCRIPTION = explicit_scoped`
- `ANISOTROPY_DEFORMATION_TRANSLATION = explicit_scoped`
- `IR_INFINITE_VOLUME_IDENTIFICATION = established_scoped`
- `PUTATIVE_UV_SCALING_PATH = source_constructed_but_not_proven`
- `CDT_CORRELATION_LENGTH_TO_FRG_K_OPERATIONAL_MAP = not_established`
- `FULL_THEORY_EQUIVALENCE = false`
- `BRIDGE_CREDIT = 0`

## Highest-information successor

The remaining blocker is now unusually sharp: the reduced action and parameter combinations are mapped, but the physical meaning of the cross-framework RG parameter remains open.

The next gate should not repeat the action comparison. It should target the **scale-setting object** itself:

`PREREGISTER_ITER079_CDT_FRG_CORRELATION_LENGTH_RG_SCALE_AUTHORITY`.

The gate should prospectively freeze the geometric CDT two-point/correlation-length construction together with FRG coarse-graining-scale authority and ask whether a physical observable or matching condition determines `k` as a function of the CDT correlation length/cutoff trajectory beyond dimensional analysis.