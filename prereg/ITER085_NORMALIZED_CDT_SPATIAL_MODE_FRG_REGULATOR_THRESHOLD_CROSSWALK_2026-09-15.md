# ITER085 preregistration — normalized CDT spatial mode ↔ foliated-FRG regulator-threshold crosswalk

Date: 2026-09-15
Gate: `ITER085_NORMALIZED_CDT_SPATIAL_MODE_FRG_REGULATOR_THRESHOLD_CROSSWALK`

## Motivation frozen before extraction

ITER084 fixed the finite-regulator local normalization of the CDT spatial dual-graph eigenvalue under a target-independent cell-centred TPFA interpretation:

`z_CDT = 9 lambda_graph / a^2`.

ITER082 had established that foliated FRG admits a genuinely spatial coarse-graining operator, but the same 2023 fluctuation paper distinguishes that background-computation route from the covariant regulator actually adopted in its production fluctuation calculation.

ITER085 therefore tests the regulator/operator typing itself before any numerical mode matching. No FRG trajectory, CDT spectral target or identification `k=1/a` may be used to rescue a type mismatch.

## Frozen sources

- arXiv `2306.10408` — F. Saueressig, J. Wang, *Foliated asymptotically safe gravity in the fluctuation approach*; production fluctuation regulator, Type-I replacement, Litim profile, spatial-vs-covariant regulator discussion and momentum projections.
- arXiv `1212.5114` — S. Rechenberger, F. Saueressig, *A functional renormalization group equation for foliated spacetimes*; background foliated-FRG construction.
- arXiv `1609.04813` — J. Biemans, A. Platania, F. Saueressig, *Quantum gravity on foliated spacetimes: Asymptotically safe and sound*; background foliated computation using spatial coarse graining.
- ITER084 terminal/source records may be used only for the already-qualified CDT normalization `z_CDT=9 lambda_graph/a^2`; they may not supply missing FRG operator authority.

## Frozen question

Does the frozen foliated-FRG stack provide a source-defined, target-independent regulator-mode threshold relation that can accept the normalized CDT **spatial** eigenvalue `z_CDT` as the eigenvalue of the same coarse-graining operator?

The gate must separately adjudicate:

1. **background-spatial route**: `Box_sp = -bar_sigma^{ij} bar_D_i bar_D_j`, where a spatial eigenvalue may be compared to the regulator threshold if the profile is explicit;
2. **2023 production fluctuation route**: the actual regulator argument used in the calculation, including its temporal momentum dependence.

A static `p0=0` restriction is admissible only if the frozen source defines or justifies that restriction as an operator sector relevant to the production flow. It cannot be introduced solely to make the CDT mode fit.

## Required predicates

A. The FRG source explicitly defines what `k` means operationally in the regulator: low/high modes are discriminated by eigenvalues/momenta of a specified coarse-graining operator relative to `k^2`.

B. The regulator profile is explicit enough to identify its support/threshold rule; for a Litim profile, the statement `z<k^2` or `z/k^2<1` must come directly from the source-defined regulator argument.

C. The background foliated route explicitly uses a spatial-hypersurface Laplacian with the same operator dimension and sign convention as normalized `z_CDT`.

D. The 2023 production fluctuation calculation's actual regulator argument is identified exactly; candidate operators listed before the production choice do not count as the implemented operator.

E. If the production regulator is covariant, any `p0=0` reduction must be source-authorized as a physical/operator sector of that flow, not imposed post hoc.

F. A regulator-support threshold is kept distinct from an equality of physical observables or a statement that `k` is the inverse CDT lattice spacing.

G. The relation `z_CDT=9 lambda_graph/a^2` is inserted only as an independently normalized spatial eigenvalue. No constant may be fitted to FRG data.

H. The gate records background-vs-fluctuation and spatial-vs-covariant scheme dependence rather than erasing it.

I. No claim about the separate running couplings `(g_k,lambda_k,...)` or an RG trajectory may follow merely from a mode-threshold crosswalk.

## Frozen controls

- `SPATIAL_COVARIANT_REGULATOR_SWAP_CONTROL`: a spatial Laplacian used in background flows cannot be substituted for a covariant production regulator.
- `CANDIDATE_IMPLEMENTED_OPERATOR_SWAP_CONTROL`: an operator mentioned as an available choice is not the implemented choice.
- `P0_ZERO_SECTOR_CONTROL`: `p0=0` cannot be imposed solely to force `p^2 -> vec p^2`.
- `REGULATOR_SUPPORT_PHYSICAL_SCALE_CONTROL`: `R_k(z)` support at `z/k^2~1` is a coarse-graining/probe statement, not a proof that two theories share a physical resolution observable.
- `K_EQUALS_ONE_OVER_A_CONTROL`: `k=1/a` is forbidden unless independently source-derived.
- `LITIM_THRESHOLD_CONTROL`: the numerical threshold `1` belongs to the regulator profile and scheme; it is not a universal physical constant.
- `BACKGROUND_FLUCTUATION_SWAP_CONTROL`: background-flow and fluctuation-flow results remain distinct.
- `TARGET_TRAJECTORY_FIT_CONTROL`: no CDT spectrum/value may select an FRG trajectory, coupling or regulator normalization.

## Frozen classifications

- `PASS_SCOPED_PRODUCTION_SPATIAL_REGULATOR_MODE_THRESHOLD_CROSSWALK` only if the implemented production regulator acts on the same spatial operator and gives an explicit target-independent threshold rule.
- `PASS_SCOPED_BACKGROUND_SPATIAL_THRESHOLD_ROUTE_PRODUCTION_COVARIANT_OPEN` if the background stack supplies an exact spatial threshold crosswalk but the production fluctuation calculation uses a covariant operator and no source-authorized static reduction closes the type gap.
- `PASS_SCOPED_STATIC_SECTOR_THRESHOLD_ONLY` if the production source explicitly authorizes a `p0=0` sector and the normalized CDT eigenvalue can be inserted there, while the full production flow remains covariant.
- `SCOPED_BLOCKED_COVARIANT_REGULATOR_REQUIRES_TEMPORAL_MODE` if the production operator necessarily requires temporal-mode data unavailable from the CDT spatial eigenvalue and no source-authorized sector removes it.
- `BLOCKED_SOURCE_AUTHORITY` if the frozen stack does not specify the relevant regulator/operator choices sufficiently.
- `INFRASTRUCTURE_FAIL_SOURCE_EXTRACTION` only for transport/extraction failure.

## Claim ceiling

A PASS can authorize at most a typed regulator-mode **probe crosswalk**. It cannot establish `k=1/a`, determine an FRG trajectory, infer running couplings from CDT, prove a shared fixed point, establish full theory equivalence, create bridge credit, support `BRIDGE_DERIVED`, or authorize candidate-theory construction.

Predicates, controls and classifications are frozen before terminal adjudication.
