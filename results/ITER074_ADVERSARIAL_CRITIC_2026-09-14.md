# ITER074 adversarial critic — CDT 4D walk-distance / diffusion-normalization authority

Date: 2026-09-14
Preregistration commit: `6ed0ba6a07d28c2fa44c66bc03caff1db4da1a2e`
Source-authority audit: `3a0eb0714cf17c2294a601c734c98fba627b1847`

## Target

Attempt to falsify or promote:

`PASS_SCOPED_REGULAR_STEP_GEOMETRY_ONLY`

with mandatory lock

`INDEPENDENT_4D_WALK_DISTANCE_OBSERVABLE = NOT_ESTABLISHED`.

## Attack 1 — the CDT review says diffusion distance grows as `sqrt(sigma)`, therefore `D_w=2`

This is the strongest apparent rescue.

A detailed CDT account of the full-4D spectral measurement indeed uses `sqrt(sigma)` as the diffusion-distance estimate when explaining why the reliable window beginning near `sigma=40` is still only a few simplex steps from the origin. But the same construction is a nearest-neighbour discretization chosen to extract the spectral return probability. No independent displacement distribution or mean-square-distance measurement is reported there.

The smooth-flat derivation of `sqrt(sigma)` is exact for Gaussian diffusion on a regular manifold. Promoting the review's step-count interpretation to a measured quantum walk exponent across the Planckian scale-dependent regime would violate the preregistered flat-Gaussian control.

**Verdict: supports `REGULAR_STEP_GEOMETRY_ONLY`, not `4D_WALK_DISTANCE_NORMALIZATION_QUALIFIED`.**

## Attack 2 — combine full-spacetime `D_H≈4` with `D_s(sigma)` using `D_s = 2D_H/D_w`

Rejected as evidentially circular and source-unsafe.

The full-4D spacetime has Hausdorff measurements consistent with dimension four in suitable regimes, while the spectral dimension is scale-dependent. A generic relation among spectral, Hausdorff and walk dimensions applies to specified fractal scaling settings. The frozen full-4D CDT stack does not establish a scale-by-scale `D_H(sigma)` and does not validate this identity over the same non-self-similar quantum crossover.

Even if inserted formally, the resulting `D_w(sigma)` would be algebraically inferred from the target spectral observable rather than independently measured from displacement data.

**Verdict: no promotion.**

## Attack 3 — thick-slice Hausdorff distance is already the required walk distance

No. Thick-slice measurements start from a simplex and count geodesic shells to obtain volume-versus-distance scaling. They are independent and useful geometric observables, but they do not follow the stochastic spectral random walker as a function of diffusion duration.

A geodesic shell radius and a random-walk displacement can have different scaling on fractal/random geometry.

**Verdict: typed distinction survives.**

## Attack 4 — the 4D toroidal diffusion-wave algorithm measures walk propagation

The toroidal study uses a diffusion-wave / breadth-first propagation algorithm to find shortest noncontractible geodesic loops. This produces full-4D dual-lattice geodesic distances and exposes highly nontrivial fractal outgrowths and shortcuts.

But the algorithm is a shortest-path search, not the stochastic random walk used for spectral return probability. It does not yield `<r^2(sigma)>` for that walker.

**Verdict: independent distance authority strengthened; walk authority still absent.**

## Attack 5 — dual geodesic distance plus `a_abs` closes the normalization

Not yet.

ITER072's `a_abs` is obtained from semiclassical volume fluctuations and microscopic simplex geometry assumptions. The spectral process advances between neighbouring four-simplices on the dual adjacency graph. Full-4D distance studies often set dual-link length to one for combinatorial measurement, while direct spacelike/timelike edge lengths carry the CDT regulator and anisotropy.

The frozen stack does not supply the universal physical factor converting one stochastic dual step into the same continuum distance unit over the Planckian quantum regime.

**Verdict: ITER073 remains blocked.**

## Attack 6 — use lower-dimensional or multigraph CDT walk dimension

Rejected prospectively. Reduced/radial multigraph models can calculate walk dimensions and are valuable mechanism laboratories, but they integrate out or replace most of the full 4D geometry. Lower-dimensional CDT likewise has different dynamical content.

**Verdict: toy/full promotion control succeeds.**

## Attack 7 — absence from reviews is not proof of nonexistence

Correct. ITER074 does not claim a global literature no-go theorem. The classification is source-scoped: within the frozen primary stack, no comparator-grade full-4D displacement/walk observable is qualified.

This is why the result is a scoped positive residual rather than `FAIL_SCOPED_WALK_NORMALIZATION_REJECTED` or a universal absence claim.

**Verdict: scope ceiling preserved.**

## Attack 8 — classify as `BLOCKED_NO_4D_WALK_DISTANCE_AUTHORITY` instead of a scoped PASS

This is defensible if the gate is interpreted only as a search for independent `D_w`. However the preregistration included `PASS_SCOPED_REGULAR_STEP_GEOMETRY_ONLY` precisely to record the case in which a source-defined discrete diffusion geometry exists, but the stronger independently measured anomalous walk law does not.

The frozen stack meets that narrower positive condition:

- nearest-neighbour full-4D diffusion is explicitly defined;
- smooth/regular `sqrt(sigma)` spread is the source's scale heuristic;
- dual-lattice distance and full-4D geodesic observables are explicitly defined;
- the missing object is sharply isolated as an independent quantum walk-distance measurement.

**Verdict: retain the preregistered scoped PASS with mandatory negative lock.**

## Critic verdict

**CONFIRMS `PASS_SCOPED_REGULAR_STEP_GEOMETRY_ONLY`.**

Durable factorization:

- `FULL_4D_RANDOM_WALK_DEFINITION = qualified`
- `REGULAR_STEP_DISTANCE_HEURISTIC = qualified_scoped`
- `FULL_4D_INDEPENDENT_GEODESIC_DISTANCE = qualified`
- `INDEPENDENT_R2_OF_SIGMA = not_established`
- `SCALE_DEPENDENT_DW = not_established`
- `DUAL_STEP_TO_ABSOLUTE_PHYSICAL_DISTANCE = not_established_in_quantum_regime`
- `ITER073_REOPENED = false`

## Successor decision

Repeated attempts to obtain the missing cross-school scale calibration from the same spectral observable family are now low-information without a new 4D CDT displacement measurement.

The next research gate should move to an **independent common observable family** rather than fit `D_s` again.

The 4D CDT programme has a source-qualified semiclassical volume profile and effective minisuperspace action. FRG/QEG literature also studies effective background geometries / scale-factor dynamics. The next high-information question is whether those objects are genuinely the same observable/effective action or merely share a de-Sitter/minisuperspace functional form after reduction.

Recommended successor:

`PREREGISTER_ITER075_FRG_CDT_VOLUME_PROFILE_EFFECTIVE_ACTION_OBSERVABLE_AUTHORITY`.