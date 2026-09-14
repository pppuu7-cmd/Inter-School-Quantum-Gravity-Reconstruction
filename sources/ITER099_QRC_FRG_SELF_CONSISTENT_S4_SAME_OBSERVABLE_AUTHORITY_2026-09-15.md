# ITER099 source authority — QRC on the FRG self-consistent S4 background

Date: 2026-09-15
Gate: `ITER099_RETROSPECTIVE_QRC_FRG_SELF_CONSISTENT_S4_SAME_OBSERVABLE_AUTHORITY`
Protocol: `8b10d7f04ab295b33f43dd108c54c25e6c813861`
Retrospective validation credit: **0**

## 1. QRC is an ordinary metric-space functional before it is a quantum expectation value

The 4D CDT QRC source defines, on a smooth Riemannian metric `g`, two equal-radius geodesic spheres `S_p^delta` and `S_p'^delta` whose centres are separated by `delta`. It then defines the normalized double sphere-distance integral

`dbar_g(delta;p,p') = [vol(S_p^delta) vol(S_p'^delta)]^(-1) int_{S_p^delta} int_{S_p'^delta} d_g(x,x') dmu_h(x) dmu_h'(x')`.

The dimensionless QRC quantity is encoded through

`dbar_g/delta = c_q [1-K_q(p,p')]`,

with `c_q` metric-space dependent. Directional averaging at fixed `delta` produces `K_q(delta)`.

The source states explicitly that, despite its name and quantum-gravity motivation, QRC can be implemented on classical metric spaces. It also gives the smooth Riemannian formula before the CDT discrete implementation.

Therefore the same finite-radius functional `Q_delta[g] := dbar_g/delta` is mathematically available on any smooth Riemannian metric supplied by the FRG reduced sector.

Predicate A: **PASS**.

## 2. ITER078 supplies an FRG self-consistent Euclidean de-Sitter metric in scope

ITER078 source-qualified the direct 2024 CDT↔FRG reduced comparison. On the FRG side the Einstein-Hilbert EAA is reduced to a self-consistent Euclidean de-Sitter solution, i.e. a round four-sphere in the frozen convention, with scale-dependent geometric radius determined by the running cosmological coupling and `k`.

The same direct source retains the distinction between this self-consistent background solution and the full quantum theory. Nothing in ITER099 promotes the reduced background to the full metric path integral.

Predicate B: **PASS_SCOPED**.

## 3. The finite-radius semantic mismatch of ITER083B disappears at the background-functional level

ITER083B compared QRC to a **local relational Ricci-scalar composite operator**. That comparison necessarily left a finite-radius mismatch because QRC is a sphere-smeared distance functional.

No such replacement is needed here. One may apply exactly the same map

`g -> Q_delta[g] = dbar_g(delta)/delta`

to the FRG self-consistent round-S4 metric. The geodesic spheres, their induced measures, centre separation and pairwise geodesic distances retain their original QRC meanings.

Thus the two descriptions admit a genuinely identical observable functional at the smooth-background level.

Predicate C: **PASS_SCOPED_SAME_FUNCTIONAL**.

## 4. Same functional is not the same quantum expectation value

The CDT quantity actually measured is an expectation over the triangulation ensemble together with point/direction averaging. Schematically,

`<Q_delta[T]>_CDT`.

Applying QRC to an FRG self-consistent EAA metric gives instead

`Q_delta[g_k^sc]`.

Since `Q_delta[g]` depends nonlinearly and nonlocally on the metric through geodesic spheres, their volumes, geodesic-distance constraints and a double distance integral, there is no identity

`<Q_delta[g]> = Q_delta[<g>]`

or

`<Q_delta[g]> = Q_delta[g_k^sc]`

without additional quantum/composite-observable authority.

The 4D CDT source itself stresses this distinction: a de-Sitter-like expectation value of the global volume profile does not imply the local quantum geometry is de Sitter, which is exactly why QRC was measured independently.

Predicate D: **BLOCKER / NO EXPECTATION MAP**.

`BACKGROUND_EXPECTATION_SWAP_CONTROL`: **TRIGGERS**.
`NONLINEAR_EXPECTATION_CONTROL`: **TRIGGERS**.

## 5. Averaging objects remain different

CDT QRC uses discrete distance and volume analogues on each triangulation, averages over suitable centre pairs/directions, then over Monte-Carlo geometries. The FRG background evaluation is a deterministic functional evaluation on the self-consistent smooth metric at scale `k`.

No frozen source identifies those averaging operations.

Predicate E: **OPEN / NOT SOURCE-DERIVED**.

## 6. QRC normalization and distance conventions remain physical nuisance structure

The QRC definition contains the positive metric-space-dependent constant `c_q`. In the 4D CDT measurement the useful signal depends on the discrete distance convention; dual-lattice and link-distance implementations are not numerically interchangeable.

Therefore a matching of curvature-profile shape does not by itself provide an absolute value or physical-radius calibration.

Predicate F: **PASS_CONTROL / NORMALIZATION OPEN**.

## 7. Absolute radius crosswalk remains open

The direct reduced map relates continuum four-volume/Newton coupling to CDT effective-action parameters and the spacelike lattice scale under its stated conventions. The 4D QRC implementation, however, uses geodesic distances on the four-dimensional triangulation, in particular a dual-link prescription whose physical centre-to-centre distances depend on simplex geometry/type and anisotropy.

The frozen stack does not provide the complete matched conversion needed to turn the measured QRC fit radius or `delta` into the self-consistent FRG radius with an exact absolute coefficient.

Predicate G: **OPEN**.

`DUAL_LINK_PHYSICAL_LENGTH_CONTROL`: **TRIGGERS**.

## 8. Retrospective observed outcome

The 4D CDT QRC paper reports that at sufficiently large scales the measured curvature behaviour is compatible with a four-sphere. This is relevant representational evidence that the independent quasi-local observable is consistent with the de-Sitter interpretation.

However, this outcome was inspected before the ITER099 protocol. Under the frozen retrospective lock it receives **zero prospective validation credit** and cannot be used to retune definitions, scales or fit windows.

Predicate H: **PASS_CONTROL; CREDIT = 0**.

## Source classification

**`PASS_SCOPED_SAME_QRC_FUNCTIONAL_BACKGROUND_LEVEL_ENSEMBLE_MAP_OPEN`**

The main advance over ITER083B is exact and narrow: the finite-radius observable-definition mismatch can be removed by applying the identical QRC functional to the source-defined FRG self-consistent metric. The surviving obstruction is not observable naming but quantum expectation semantics and absolute distance normalization.

## Highest-information successor

Test whether FRG/asymptotic-safety composite-operator or relational-observable machinery source-defines the quantum expectation/RG flow of the **same nonlocal QRC ingredients** — geodesic distance, geodesic-sphere hypersurface measure, fixed-distance constraints and their normalized double integral — rather than only local curvature or isolated geometric operators.

The existence of generic composite-operator machinery is not sufficient. PASS must require an explicit or derivable closed QRC-type nonlocal operator construction without fitting CDT QRC data.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. No full theory equivalence, shared trajectory, shared fixed point, `BRIDGE_DERIVED`, or new physics is authorized.