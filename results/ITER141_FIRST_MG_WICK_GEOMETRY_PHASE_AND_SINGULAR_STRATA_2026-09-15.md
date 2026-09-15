# ITER141 terminal result — first M/G Wick geometry, phase routing and actual affine singular strata

Date: 2026-09-15
Preregistration: `c324ca5091ca3bad4a1025914a95a4e786b64841`
Implementation: `20a191522a7f84a10e7b49870400aabc496db220`
Workflow head: `8e9a006067a251b15d0ea3ec910a3fad6a216bc6`
Authoritative run: `34958390269`
Job: `104345848468` (`wick-geometry-audit`)
Artifact: `10391767876` (`iter141-first-mg-wick-geometry-phase-strata`)
Artifact SHA256: `51d4fe655f1cc5393ec3ff23fb8eca1dd94d42a88e8dddb05593974e107dd1d5`

## Scientific classification

`PASS_SCOPED_FIRST_MG_WICK_GEOMETRY_PHASE_AND_SINGULAR_STRATA_CLOSED_LOCAL_POLES_OPEN`

All frozen affine-coordinate, Wick-momentum, exact phase-factorization, endpoint-zero inference, conservative ITER139 jet-map, channel-scope and target-blind checks passed.

## Actual connected-cross singular strata

With anchored geometry `x=0`, `y=L n`, `z(tau)=tau L n`, `L>0`:

- `M_R2_chi1_dR1`: Wick edges have lengths `tau L` and `L`; therefore only **lower `tau->0`** is an affine propagator singularity. The upper endpoint has no shrinking propagator in this connected cross channel.
- `M_R1_chi1_dR2`: edges have lengths `L` and `(1-tau)L`; therefore only **upper `tau->1`** is singular. The lower endpoint is nonsingular in this channel.
- `G_R1_chi2_Gamma2_dR1`: edges have lengths `tau L` and `(1-tau)L`; therefore **both lower and upper endpoints** are singular.

Momentum derivatives can strengthen a singular edge but cannot create an affine singularity on an edge whose separation remains the fixed nonzero length L.

## Exact phase routing

For one representative Bose pairing:

- M1: `exp[-i(tau q+k).L n] = exp[-i(q+k).L n] exp[+i(1-tau)q.L n]`;
- M2: `exp[+i(q+k).L n] exp[-i tau k.L n] = exp[+i q.L n] exp[+i(1-tau)k.L n]`;
- G1: `exp[+i tau(q+k).L n] exp[-i k.L n] = exp[+i tau q.L n-i(1-tau)k.L n]`.

These identities were generated from field momenta and insertion coordinates rather than imposed as a chosen master routing.

## Conservative jet map frozen by this gate

ITER141 intentionally consumed ITER139's max-line ceilings as conservative bounds:

- M1 lower: N<=5 -> jet<=6;
- M2 upper with `(1-tau)` suppression: N<=5 -> jet<=5;
- G1 lower: N<=4 -> jet<=5;
- G1 upper with suppression: N<=4 -> jet<=4.

However ITER138/139 also record directional q/k degrees. Now that ITER141 has identified which propagator actually shrinks at each endpoint, a sharper successor may replace the max-line bound by the degree on that specific shrinking edge. This sharpening must be preregistered separately; it is not retroactively inserted into ITER141.

## Scope boundary

The quadratic-vertex self-pairing/local Wick channel is explicitly outside this connected-cross gate and remains part of the renormalized local/tadpole sector. No pole residue is silently discarded.

## Claim ceiling

No curvature `1/epsilon` coefficient, B1, noncancellation result, B0, EDT comparison, bridge, new physics or candidate theory is established. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
