# ITER092 adversarial review — kappa4 pseudocritical scaling as a cosmological eigendirection

Date: 2026-09-15
Retrospective protocol: `b1fa8614840fd5b5cc0762a989b42a5d7110a04b`
Source authority: `886d8d3e30e4dc00481da11717a19545957e7921`

## Attack 1 — because `K_4` is the bare cosmological coupling, its finite-size exponent is automatically the cosmological critical exponent

Rejected. A coordinate in bare coupling space need not align with an RG scaling eigenvector. The source itself observes that the pseudocritical displacement in `K_4` is approximately linearly correlated with the displacement in `Delta` and that both scale with the same finite-size exponent.

This is evidence for a mixed direction in the measured bare coordinates, not for eigenvector purity of the `K_4` axis.

## Attack 2 — equal exponents prove two independent relevant directions with equal critical exponents

The data do not require that interpretation. One finite-size transition displacement represented in two correlated coordinates naturally yields the same exponent in both. Distinguishing one mixed scaling field from two degenerate eigenfields would require additional independent response/eigenvector information, which the frozen source does not provide.

The approximately linear `K_4^crit` versus `Delta^crit` relation favors the lower-rank interpretation until contrary authority exists.

## Attack 3 — use `gamma_K4=1.62` directly as an FRG critical exponent

Rejected. The measured `gamma` is the finite-size shift exponent of a pseudocritical transition location under the volume variable used by the lattice simulation. An FRG critical exponent is an eigenvalue of the linearized RG stability matrix in a specified theory-space truncation. Matching numbers requires a source-derived scaling-field and finite-size/RG conversion, not numerical resemblance.

## Attack 4 — the standard CDT relation `kappa_4-kappa_4^c ~ (Lambda/G) a^4` makes the `K_4` shift a pure cosmological scaling field

That standard relation motivates the critical subtraction needed to obtain the physical cosmological term when the lattice spacing is taken to zero. It does not identify the finite-volume drift of the **B-C transition location** in the `(Delta,K_4)` plane with the cutoff scaling of a pure cosmological source.

The 2019 measurement varies a phase-transition point and observes coupled displacement of both coordinates. These are different statements.

## Attack 5 — use the slope of `K_4^crit` versus `Delta^crit` as the RG eigenvector

The observed approximately linear relation does provide a **candidate tangent direction** to the finite-size pseudocritical trajectory. But a single tangent to a transition locus is not yet an RG stability eigenvector: one needs a local response/stability map, including the normal direction and coupling mixing with any other relevant bare coordinate such as `kappa_0`.

This attack therefore motivates the next gate rather than upgrading ITER092.

## Attack 6 — hysteresis invalidates the scaling result entirely

Too strong. The source explicitly fits multiple branches/endpoints of the shrinking hysteresis and obtains consistent finite-size scaling. The result is legitimate source authority for the pseudocritical trajectory, with its stated uncertainties. Hysteresis does reinforce the need for caution when translating the shift exponent into continuum RG language.

## Verdict

The strongest defensible source classification remains

**`SOURCE_SUPPORTS_MIXED_PSEUDOCRITICAL_SHIFT_NOT_INDEPENDENT_COSMOLOGICAL_DIRECTION`**.

Prospective validation credit: **0** by protocol.
Bridge credit: **0**.
Candidate theory: **UNFORMED / 0%**.

The next missing object is a scaling-field/eigenvector construction, not another scalar critical exponent.
