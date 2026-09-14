# ITER079 adversarial critic — CDT correlation length ↔ FRG RG scale

Date: 2026-09-14
Preregistration: `87c23a0ff5dcc134b7b98e588951c58f0c158b07`
Source-authority audit: `46657aa21bbd191e6133171d4a2d9dd8fb402fff`

## Target

Attempt to falsify or strengthen:

`PASS_SCOPED_REDUCED_SCALE_RELATION_ONLY`

with lock

`OPERATIONAL_CDT_XI_TO_FRG_K_MAP = NOT_ESTABLISHED`.

## Attack 1 — identify k with the inverse physical correlation length exactly as in ordinary lattice field theory

In an ordinary fixed-background field theory one may define a renormalized mass by the inverse physical correlation length, schematically `m_R ~ 1/(a xi)`. The 2024 follow-up says that, in the analogy to its scalar example, `k` plays the role of `m_R`.

This is not enough to upgrade the gravitational map. The same source emphasizes that the CDT `xi ~ N_4^(1/4)` is not the propagation length of an ordinary degree of freedom and that its use as a correlation length follows from geometric two-point/finite-size scaling. Most decisively, the direct paper states that the precise relation between this `xi` and FRG `k` is not known.

**Verdict: analogy does not establish `k = 1/(a xi)`.**

## Attack 2 — use `xi a ~ V_4^(1/4)` and the FRG de-Sitter volume to set `k ~ 1/(xi a)`

ITER078 already maps the reduced four-volume and couplings. One could therefore choose an RG-improvement prescription in which `k` is proportional to inverse de-Sitter radius or inverse physical size.

But this is not an independent scale-setting observable under ITER079. It reuses the same reduced volume/action sector that constructed the crosswalk and adds a scale-identification convention not derived as a unique FRG coarse-graining condition. The FRG scale resolves fluctuation modes through the regulator; the frozen stack does not prove that the global four-sphere radius is the unique physical cutoff resolution.

**Verdict: target-observable circularity control rejects the promotion.**

## Attack 3 — the FRG regulator peaks at p^2 ~ k^2, while CDT two-point functions depend on geodesic distance; Fourier duality gives the map

The FRG mode-resolution statement is source-defined. The CDT geometric two-point function is also source-defined. What is missing is a common spectral/mode transform establishing that the particular CDT finite-size correlation length corresponds to the same modes selected by the FRG regulator.

There is no source-defined Fourier/Laplacian map from the CDT geometric correlation-length observable to the FRG background-mode spectrum in the frozen stack.

**Verdict: no operational map.**

## Attack 4 — `a proportional_to 1/k` is explicitly derived, so predicate E must pass

The follow-up source itself blocks this reading. It calls `a proportional_to 1/k` **just a dimensional relation** and says the real physical content is that, at fixed `k` / fixed `lambda_k g_k`, the lattice cutoff tends to zero when `xi` diverges.

Thus the source-derived relation is a continuum-scaling relation among three scale objects, not a unique matching of their operational resolutions.

**Verdict: supports the partial PASS, not full operational PASS.**

## Attack 5 — because `a -> 0` at fixed k and xi -> infinity, k must equal a fixed physical inverse correlation length

Not necessarily. Holding a renormalized coupling/FRG parameter fixed while removing a regulator is the correct logic of a continuum limit, but it does not by itself identify the auxiliary RG coarse-graining parameter with a particular physical observable. Many values of `k` can label the same continuum trajectory at different coarse-graining stages.

The direct source treats `k` primarily as the parameter of the reduced coupling `lambda_k g_k` in this comparison.

**Verdict: fixed-k continuum scaling is not scale identity.**

## Attack 6 — the 2026 review upgrades the result to a physical scale map

The current CDT review strengthens the finite-size/critical interpretation: `N_4^(1/4)` is used as a correlation length, and the reduced combination corresponding to `Lambda G` is followed toward IR/putative UV limits.

It does not add the missing operational equation assigning a unique FRG coarse-graining `k` to the CDT geometric correlation length. Current evidence therefore strengthens the lattice side without closing the cross-framework map.

**Verdict: no promotion.**

## Attack 7 — similar CDT and FRG critical exponents can empirically calibrate the map

The direct authors explicitly say the opposite logical order is required: because the `xi` ↔ `k` connection is not known, they cannot directly compare the critical exponent derived from CDT `xi` with the FRG critical exponent.

Using exponent agreement to define the map and then citing the agreement as evidence for it would be circular.

**Verdict: critical-exponent premap control succeeds.**

## Attack 8 — demote the result to `SCOPED_BLOCKED_NO_OPERATIONAL_XI_TO_K_MAP_AUTHORITY`

This would understate the source-derived content. The direct stack establishes more than two unrelated scale definitions:

- `xi ~ N_4^(1/4)`;
- `xi a ~ V_4^(1/4)` in the reduced de-Sitter scaling description;
- explicit near-UV formulas relating `a`, `a_t`, `N_4`, `k` and the critical exponents;
- fixed-`k` / fixed-`lambda_k g_k` continuum scaling where `a -> 0` as `xi -> infinity`.

The source itself interprets these relations as the gravitational counterpart of the continuum-limit logic, while simultaneously refusing to identify `a ~ 1/k` as more than dimensional.

This is exactly the preregistered intermediate case `PASS_SCOPED_REDUCED_SCALE_RELATION_ONLY`.

**Verdict: partial PASS retained.**

## Attack 9 — partial scale relation plus ITER078 should already count as bridge credit

Rejected by the project constitution and by the gate's claim ceiling. The established relation is confined to the simplest reduced minisuperspace/EH comparison and leaves the operational RG-scale map, full state spaces, measures and microscopic dynamics unresolved.

**Verdict: bridge credit remains zero.**

## Critic verdict

**CONFIRMS `PASS_SCOPED_REDUCED_SCALE_RELATION_ONLY`.**

Mandatory lock confirmed:

**`OPERATIONAL_CDT_XI_TO_FRG_K_MAP = NOT_ESTABLISHED`**.

Durable factorization:

- `CDT_GEOMETRIC_CORRELATION_LENGTH = qualified_scoped`
- `XI_TIMES_A_TO_PHYSICAL_GLOBAL_LENGTH = qualified_scoped_reduced`
- `FRG_K_COARSE_GRAINING_MODE_SCALE = qualified`
- `SOURCE_DERIVED_A_XI_K_SCALING_RELATIONS = qualified_scoped`
- `A_PROPORTIONAL_1_OVER_K = dimensional_only_by_source`
- `INDEPENDENT_PHYSICAL_MATCHING_CONDITION = absent`
- `DIRECT_CRITICAL_EXPONENT_IDENTIFICATION = unauthorized`
- `FULL_THEORY_RG_SCALE_IDENTITY = false`
- `BRIDGE_CREDIT = 0`

## Successor decision

The missing scale cannot be closed by manipulating the same reduced volume/action variables again. A useful successor must introduce a **held-out physical observable** that can select the FRG resolution independently and then test the already-derived ITER078 map out of sample.

The spectral observable is the strongest candidate because ITER071 established a common spectral-dimension definition, while the earlier spectral branch lacked the direct parameter crosswalk now supplied by ITER078.

Recommended next gate:

`PREREGISTER_ITER080_CDT_FRG_OUT_OF_SAMPLE_SPECTRAL_PREDICTION_FROM_REDUCED_MAP`.

The gate should forbid fitting the FRG trajectory or scale to the target CDT spectral curve. It should ask whether the ITER078 reduced action/parameter map plus an independently fixed scale prescription predicts any held-out spectral observable/range. If no independent scale can be fixed without using `D_s` itself, the gate should terminate source-blocked rather than repeat the old target-fit comparison.