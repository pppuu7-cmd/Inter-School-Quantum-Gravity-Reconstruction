# ITER079 terminal result — CDT correlation length ↔ FRG RG-scale authority

Date: 2026-09-14
Gate: `ITER079_CDT_FRG_CORRELATION_LENGTH_RG_SCALE_AUTHORITY`
Preregistration commit: `87c23a0ff5dcc134b7b98e588951c58f0c158b07`
Source-authority commit: `46657aa21bbd191e6133171d4a2d9dd8fb402fff`
Adversarial-critic commit: `4442eb47da3f52c72a4ede254b219fea8408e0e9`

## Terminal classification

**`PASS_SCOPED / REDUCED_SCALE_RELATION_ONLY`**

Mandatory retained lock:

**`OPERATIONAL_CDT_XI_TO_FRG_K_MAP = NOT_ESTABLISHED`**

Bridge credit: **0**.

## Question adjudicated

Does the frozen direct CDT↔FRG source stack establish a physical, operational map from the geometric CDT correlation length / finite-size-scaling trajectory to the FRG coarse-graining scale `k`, beyond dimensional inverse-length reasoning?

## Result

No full operational map is established.

A weaker but nontrivial source-defined reduced scaling relation **is** established, so the correct classification is the preregistered intermediate PASS rather than a complete source block.

## CDT correlation-length authority

The direct literature defines a gravitational/geometric correlation-length analogue from two-point/finite-size scaling of fluctuating geometries. In the four-dimensional CDT de-Sitter phase,

`xi_CDT proportional_to N_4^(1/4)`

plays the role of the dimensionless correlation length.

The source is explicit that this is not simply the propagation length of a matter field. It is tied to correlations between spacetime points/geodesic separation and to finite-size scaling of the ensemble.

Within the reduced de-Sitter scaling description the physical global length satisfies schematically

`xi_CDT * a proportional_to V_4^(1/4)`.

Thus lattice correlation length, lattice cutoff and physical length are distinct source-defined objects.

## FRG k authority

The FRG review defines `k` as the coarse-graining scale of the Effective Average Action. The regulator makes the functional trace peak at fluctuation momenta of order

`p^2 approximately k^2`.

Running couplings and the EAA therefore depend on a regulator/mode-resolution scale, not merely on an arbitrary inverse length label.

## Reduced a-xi-k relation

Combining the direct minisuperspace correspondence with finite-size scaling gives source-derived near-UV relations involving

- `a`, `a_t`;
- `N_4` and hence `xi_CDT`;
- `k`;
- the fixed reduced FRG coupling combination `lambda_k g_k`.

The physical continuum-scaling content is source-qualified:

at fixed `k` / fixed `lambda_k g_k`, the lattice cutoff tends to zero while the CDT correlation length diverges.

This is more than two unrelated scale definitions and earns the scoped partial PASS.

## Why the operational map does not pass

The direct source explicitly says that the precise relation between the CDT correlation length used to derive the lattice critical exponent and the FRG scale `k` is not known sufficiently for direct critical-exponent comparison.

The follow-up derives expressions containing

`a proportional_to 1/k`

but then explicitly states that this is **just a dimensional relation**. The source does not supply a separate held-out physical observable or unique mode-matching condition that assigns a specific FRG `k` to a measured CDT `xi`.

Therefore ITER079 does not establish

`k = c / (a xi_CDT)`

or any other one-to-one operational `xi_CDT <-> k` identity.

## Frozen predicate results

- A — CDT geometric correlation-length object: **PASS_SCOPED**.
- B — finite-size/critical scaling: **PASS_SCOPED**.
- C — relation of `xi`, `a` and physical global length: **PASS_SCOPED / MODEL-DEPENDENT**.
- D — FRG `k` coarse-graining semantics: **PASS**.
- E — independent operational `xi <-> k` matching condition: **NOT ESTABLISHED**.
- F — validity range of reduced relation: **PASS_SCOPED**.
- G — cutoff/correlation-length/RG-scale distinction retained: **PASS_CONTROL**.
- H — independent held-out scale-setting observable: **NOT ESTABLISHED**.
- I — direct critical-exponent equality: **NOT AUTHORIZED**.
- J — regulator/truncation/anisotropy retained: **PASS_AS_SCOPE_LOCK**.
- K — 2026 current-status evidence: **POSITIVE UPDATE, NO NEW SCALE MAP**.

This pattern maps to:

**`PASS_SCOPED_REDUCED_SCALE_RELATION_ONLY`**.

## Adversarial critic

The critic attempted to promote the result by:

- using the ordinary field-theory identity `m_R ~ 1/(a xi)`;
- setting `k` equal to inverse de-Sitter radius through the ITER078 volume map;
- appealing to Fourier duality between geodesic two-point functions and FRG momentum modes;
- treating the derived `a ~ 1/k` behavior as operational scale matching;
- using critical-exponent similarity to calibrate the map.

Each route adds a non-source-defined identification or becomes circular.

The critic also tested demotion to a full source block. That would erase genuine source-derived relations among `a`, `xi`, `k` and the reduced coupling at fixed-physics continuum scaling.

Critic verdict: **CONFIRMS terminal classification**.

## Structural consequence

The CDT↔FRG route now has a sharp hierarchy:

1. direct reduced action/parameter crosswalk: **established in scope** (ITER078);
2. reduced continuum scale relation among `a`, `xi`, `k` and fixed reduced coupling: **established in scope** (ITER079);
3. independently operational common RG resolution `xi <-> k`: **not established**;
4. direct cross-framework critical-exponent equality: **not authorized**;
5. full microscopic theory/RG equivalence: **not established**.

## Next admissible gate

Further manipulation of the same reduced volume/action variables is unlikely to add independent evidence. A successor must use a held-out observable.

Recommended gate:

**`PREREGISTER_ITER080_CDT_FRG_OUT_OF_SAMPLE_SPECTRAL_PREDICTION_FROM_REDUCED_MAP`**

The aim is not to refit the spectral curve. It is to test whether the already established ITER078 reduced map plus independently fixed source information predicts any spectral-dimension feature/range **without selecting the FRG trajectory or scale from the target CDT `D_s` data**.

If no such independent prediction is possible, the gate should terminate blocked rather than repeat the target-fitted 3D comparison.

## Claim locks

- `DIRECT_REDUCED_ACTION_PARAMETER_CROSSWALK = true_scoped`
- `REDUCED_A_XI_K_SCALE_RELATION = true_scoped`
- `OPERATIONAL_CDT_XI_TO_FRG_K_MAP = false`
- `DIRECT_CRITICAL_EXPONENT_IDENTITY = false`
- `FULL_THEORY_EQUIVALENCE = false`
- `SHARED_UV_FIXED_POINT_ESTABLISHED = false`
- `BRIDGE_DERIVED = false`
- candidate theory = `UNFORMED / 0%`
- bridge credit = `0`