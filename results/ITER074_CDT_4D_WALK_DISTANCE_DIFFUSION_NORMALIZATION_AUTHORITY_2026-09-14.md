# ITER074 terminal result — CDT 4D walk-distance / diffusion-normalization authority

Date: 2026-09-14
Gate: `ITER074_CDT_4D_WALK_DISTANCE_DIFFUSION_NORMALIZATION_AUTHORITY`
Preregistration commit: `6ed0ba6a07d28c2fa44c66bc03caff1db4da1a2e`
Source-authority commit: `3a0eb0714cf17c2294a601c734c98fba627b1847`
Adversarial critic commit: `9b4cca52601bc29c18df59be1cba605570e7ef73`

## Terminal scientific classification

**`PASS_SCOPED / REGULAR_STEP_GEOMETRY_ONLY`**

Mandatory retained lock:

**`INDEPENDENT_4D_WALK_DISTANCE_OBSERVABLE = NOT_ESTABLISHED`**

Additional lock:

**`ITER073_REOPENED = false`**

Bridge credit: **0**.

## Question adjudicated

Does full four-dimensional CDT already provide an independent random-walk displacement observable — for example `<r^2(sigma)>`, diffusion radius or scale-dependent walk dimension — that fixes how physical distance grows with the same diffusion duration used in the spacetime spectral-dimension measurement?

## Result

Not at comparator-grade source authority in the frozen stack.

The stack does provide a narrower positive object: a full-4D nearest-neighbour diffusion process on the triangulation/dual adjacency graph, standard regular-diffusion `sqrt(sigma)` distance semantics, and independent full-4D geodesic-distance measurements. What it does not provide is a measured scale-dependent displacement law for the spectral random walker in the Planckian quantum regime.

## Positive authority retained

### Full-4D spectral random walk

The spacetime spectral measurement explicitly implements a discrete diffusion process on four-dimensional CDT configurations and measures the ensemble-averaged return probability. Short odd/even lattice artifacts and long finite-size effects are controlled by a restricted diffusion window.

### Regular-step distance interpretation

For ordinary smooth diffusion, the heat kernel gives Gaussian spread with linear scale `sqrt(sigma)`. Detailed CDT accounts use this relation as an order-of-magnitude step-distance interpretation of the reliable spectral window.

This is legitimate as a regular nearest-neighbour interpretation. It is not an independent measurement of a quantum walk exponent.

### Independent geometric distance observables

CDT does measure discrete geodesic distances and Hausdorff-type volume-distance relations. Full-4D toroidal work also measures shortest noncontractible loops and dual-lattice geodesics, exposing strong fractal outgrowths and shortcuts.

These results show that distance itself is source-defined and highly nontrivial in the quantum geometry. They do not measure the stochastic displacement of the spectral random walk as a function of `sigma`.

## Frozen predicate results

- A — independent full-4D diffusion-displacement observable: **NOT ESTABLISHED**.
- B — such an observable actually evaluated on 4D CDT ensembles: **NOT ESTABLISHED**.
- C — scale-dependent `R(sigma)` or `D_w(sigma)` extracted in a controlled window: **NOT ESTABLISHED**.
- D — discrete geometric distance tied to CDT lattice units: **PARTIAL POSITIVE AUTHORITY**, but dual/direct/anisotropy conversion remains non-universal at finite cutoff.
- E — independent evidence rather than inference from `D_s`: **NO INDEPENDENT WALK MEASUREMENT; CONTROL PASSES**.
- F — scale-by-scale applicability of `D_s = 2D_H/D_w` to the same full-4D crossover geometry: **NOT ESTABLISHED**.
- G — full-4D scope: **spectral and several geodesic observables qualify, but not the required walk-displacement object**.
- H — no FRG import: **PASS_CONTROL**.

The frozen pattern matches:

**`PASS_SCOPED_REGULAR_STEP_GEOMETRY_ONLY`**.

## Why `sqrt(sigma)` does not close ITER073

The physical-scale blocker requires an independently normalized Planckian walk distance, not merely the classical/regular relation between random-walk step count and root-mean-square spread.

The full-4D quantum geometry has scale-dependent spectral behavior, nontrivial geodesic structure, outgrowths and shortcuts. Without a direct displacement measurement one cannot assume that the microscopic quantum walk obeys a universal `D_w=2` law simply because the discretized algorithm uses nearest-neighbour steps.

The distinction is especially important because ITER073 showed that QEG itself has anomalous walk regimes. A physical-resolution crosswalk cannot be constructed by imposing normal diffusion on one side merely to match the other.

## Why Hausdorff data do not rescue the walk law

Full-4D and thick-slice CDT studies find Hausdorff-type scaling compatible with four dimensions in relevant regimes, but the spacetime spectral dimension is explicitly scale dependent.

Inferring

`D_w = 2 D_H / D_s`

would require source authority that the fractal identity applies scale by scale to the same non-self-similar quantum geometry. That authority is absent in the frozen stack. It would also make the proposed walk dimension depend algebraically on the target spectral observable instead of providing independent calibration.

## Why geodesic-loop measurements do not rescue it

The 4D toroidal studies use diffusion-wave / breadth-first algorithms to find shortest paths and noncontractible loops on the dual graph. These are independent and important geometric observables, but they are shortest-path searches, not the stochastic diffusion process whose return probability defines `D_s`.

They therefore strengthen geometric distance authority without supplying `<r^2(sigma)>`.

## Adversarial critic

The critic attempted to promote the result by:

- treating the review statement `distance ~ sqrt(sigma)` as a measured `D_w=2`;
- combining `D_H≈4` and `D_s(sigma)` through a generic fractal identity;
- using thick-slice Hausdorff radius as random-walk displacement;
- treating toroidal shortest-path diffusion waves as stochastic diffusion;
- multiplying dual step count by ITER072's `a_abs`;
- importing lower-dimensional or multigraph CDT walk results.

Each route violates at least one frozen control.

The critic also considered a full source-block classification, but retained the narrower preregistered scoped PASS because the full-4D random-walk definition, regular step-distance semantics and independent geodesic distance structure are genuinely established.

Critic verdict: **CONFIRMS terminal classification**.

## Structural consequence

The spectral branch is now sharply factorized:

1. same spectral observable definition across CDT and QEG: **established**;
2. CDT internal diffusion/lattice scale calibration: **established in scope**;
3. independent full-4D CDT quantum walk-distance law: **not established**;
4. independent 4D cross-school physical-resolution normalization: **blocked**;
5. repeated `D_s` curve matching without a new distance observable is therefore low-information and receives no bridge credit.

## Downstream decision

Do **not** reopen ITER073 on the basis of ITER074.

The next highest-information route should use an independent observable family:

**`PREREGISTER_ITER075_FRG_CDT_VOLUME_PROFILE_EFFECTIVE_ACTION_OBSERVABLE_AUTHORITY`**.

The gate should compare the source-qualified CDT de-Sitter volume profile / effective minisuperspace action with the closest QEG/FRG background-geometry or scale-factor effective object, first asking whether they are actually the same observable/reduced effective action before comparing functional shapes or fitted parameters.

## Claim ceiling

ITER074 does **not** establish:

- a full-4D CDT quantum walk dimension;
- a Planckian absolute diffusion radius;
- a reopened FRG/CDT physical-scale spectral comparator;
- a no-go theorem for future walk observables;
- FRG/CDT equivalence;
- `BRIDGE_DERIVED`;
- `UNIVERSAL_COMMON_PARENT_FOUND`;
- new physics;
- a candidate theory.

`CANDIDATE_THEORY = UNFORMED`

`THEORY_ESTABLISHED = 0%`

`BRIDGE_CREDIT = 0`