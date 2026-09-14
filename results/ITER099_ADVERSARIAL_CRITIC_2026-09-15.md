# ITER099 adversarial critic — same-QRC functional versus quantum expectation

Date: 2026-09-15
Gate: `ITER099_RETROSPECTIVE_QRC_FRG_SELF_CONSISTENT_S4_SAME_OBSERVABLE_AUTHORITY`
Protocol: `8b10d7f04ab295b33f43dd108c54c25e6c813861`
Source authority: `3c7707b51ec0c68982f3505344f4dfb8262b80f5`

## Attack 1 — same functional implies same observable

Rejected as too strong. The same map `Q_delta[g]` exists on both a CDT geometry and a smooth FRG metric, but the theory-level objects differ:

- CDT: ensemble expectation of the functional over fluctuating geometries plus point/direction averaging;
- FRG reduced background: deterministic evaluation on a self-consistent metric.

Observable-functional identity is therefore weaker than expectation-value identity.

## Attack 2 — EAA mean field makes `Q[g_sc]` the expectation automatically

Rejected. QRC is nonlinear and nonlocal in the metric. Geodesic spheres, their measures and distance constraints all fluctuate with `g`. A stationary/self-consistent EAA metric does not source-qualify the identity `Q[g_sc]=<Q[g]>`.

## Attack 3 — use local Ricci scalar because a round S4 has constant curvature

Rejected. This reintroduces the exact finite-radius type substitution ruled out in ITER083B. Local constant curvature can help calculate the classical QRC profile of a round sphere, but it does not turn the QRC operator into a local Ricci-scalar operator in the quantum theory.

## Attack 4 — absorb all mismatch into `c_q`

Rejected. `c_q` handles a metric-space-dependent vertical normalization/offset convention. It does not encode ensemble fluctuations, distance renormalization, dual-link physical normalization or the difference between `Q[g_sc]` and `<Q[g]>`.

## Attack 5 — four-sphere-compatible CDT data validate the FRG map

Rejected for two independent reasons:

1. the target result was inspected before ITER099 and receives retrospective validation credit 0;
2. compatibility with a round four-sphere tests a background geometry class, not the unique FRG trajectory/couplings or the full theory.

## Attack 6 — the direct reduced map supplies the missing absolute radius

Not established. The QRC dual-link distance convention lives on the four-dimensional simplex complex and requires exact centre-to-centre physical geometry/anisotropy and ensemble matching. The simplified reduced volume map does not by itself provide this complete distance conversion.

## Surviving positive result

The critic cannot overturn the narrow positive statement:

> the exact same finite-radius metric-space QRC functional is well-defined on the source-qualified FRG self-consistent smooth S4 metric.

That statement is stronger and cleaner than ITER083B's common local-curvature target.

## Critic verdict

**CONFIRMS `PASS_SCOPED_SAME_QRC_FUNCTIONAL_BACKGROUND_LEVEL_ENSEMBLE_MAP_OPEN`.**

The next nonredundant question is whether FRG composite-operator/relational machinery actually supports the corresponding nonlocal quantum observable, not whether a classical background can be fitted to CDT QRC data.

Bridge credit: **0**. Candidate theory: **UNFORMED / 0%**.