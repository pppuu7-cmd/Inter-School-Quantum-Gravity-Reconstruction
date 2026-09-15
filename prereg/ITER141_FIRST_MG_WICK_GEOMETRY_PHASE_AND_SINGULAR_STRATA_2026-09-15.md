# ITER141 preregistration — first M/G Wick geometry, phase routing and actual affine singular strata

Date: 2026-09-15
Gate: `ITER141_FIXED_GEODESIC_CURVATURE_FIRST_MG_WICK_GEOMETRY_PHASE_AND_SINGULAR_STRATA`
Status: **FROZEN BEFORE AUTHORITATIVE PRODUCTION RUN**

## Motivation

ITER139 repaired conservative derivative/jet ceilings but intentionally applied the generic bulk weight `(1-tau)` to both affine endpoints. A concrete Wick graph can be singular at only one endpoint if its line-dependent propagator has separation `tau*l` or `(1-tau)*l`; a full endpoint-to-endpoint propagator at fixed nonzero `l` is not an affine endpoint singularity. Before extracting any pole, the exact graph geometry must therefore be frozen separately from the derivative ceiling.

This gate is independent of ITER140's dimensional continuation and may be executed in parallel.

## Frozen anchored geometry

Use the anchored fixed-geodesic configuration

- first curvature endpoint `x=0`;
- second curvature endpoint `y=L n`, with `L>0`, `n^2=1`;
- bulk geodesic insertion `z(tau)=tau y`, `0<=tau<=1`.

The direct source weight for the admitted first-order chi1 and direct-Gamma2 chi2 terms is exactly `(1-tau)` from ITER127.

## Frozen connected cross-Wick channels

Only the connected cross-pairings already admitted in ITER138/139 are classified here. The quadratic-vertex self-pairing/local channel remains a separate renormalization sector.

### M1 — `R2(x) * chi1(y) . dR1(y)`

Let R2 legs carry momenta `q,k`. Pair the chi1 field at `z(tau)` with the q leg and dR1 at y with the k leg (the Bose-exchanged pairing is equivalent by q<->k).

Expected edge separations to be tested:

- `x <-> z(tau)`: `tau L`;
- `x <-> y`: `L`.

Expected Fourier phase:

`exp[-i (tau q + k).(L n)]`
`= exp[-i (q+k).(L n)] exp[+i (1-tau) q.(L n)]`.

### M2 — `R1(x) * chi1(y) . dR2(y)`

Let the dR2 leg paired with R1 carry q and the leg paired with chi1 carry k, matching the ITER139 tensor convention.

Expected edges:

- `x <-> y`: `L`;
- `z(tau) <-> y`: `(1-tau)L`.

Expected phase:

`exp[+i (q+k).(L n)] exp[-i tau k.(L n)]`
`= exp[+i q.(L n)] exp[+i (1-tau) k.(L n)]`.

### G1 — `R1(x) * chi2_Gamma2(y) . dR1(y)`

Let Gamma2 legs at z(tau) carry q,k, with R1 paired to q and dR1 paired to k.

Expected edges:

- `x <-> z(tau)`: `tau L`;
- `z(tau) <-> y`: `(1-tau)L`.

Expected phase:

`exp[+i tau (q+k).(L n)] exp[-i k.(L n)]`
`= exp[+i tau q.(L n) - i (1-tau) k.(L n)]`.

## Frozen singular-stratum rule

For fixed nonzero L, an affine endpoint can contribute a local line UV singularity in a connected cross channel only if at least one Wick edge separation tends to zero there. Momentum derivatives may increase the singular power but cannot create a zero separation on an edge whose distance remains L.

Therefore the frozen expected actual affine strata are:

- M1: lower `tau->0` only;
- M2: upper `tau->1` only;
- G1: both lower and upper.

The gate must derive these from the frozen edge incidence and not hard-code a residue.

## Frozen jet consequence

Consume ITER139 exact independent-line ceilings only as upper bounds on the singular edge:

- M1 N1=5 at lower endpoint, source suppression s=0 -> conservative local jet <=6;
- M2 N1=5 at upper endpoint, source suppression s=1 -> conservative local jet <=5;
- G1 N1=4: lower s=0 -> jet <=5; upper s=1 -> jet <=4.

The nonsingular opposite M endpoint is marked `NO_AFFINE_PROPAGATOR_SINGULARITY_IN_CONNECTED_CROSS_CHANNEL`, not assigned a fake Taylor-jet pole order.

## Frozen validation

A machine implementation must:

1. encode insertion coordinates symbolically as affine multiples of y;
2. derive each Wick-edge affine distance coefficient;
3. derive the Fourier exponent from field momenta and insertion coordinates;
4. verify the stated algebraic phase factorizations exactly;
5. infer endpoint-zero edge sets algorithmically;
6. verify the inferred singular strata and the ITER139 jet map;
7. keep the local/self-pairing channel explicitly outside scope rather than silently dropping it.

## Frozen classifications

- All geometry/phase/strata/jet predicates pass:
  `PASS_SCOPED_FIRST_MG_WICK_GEOMETRY_PHASE_AND_SINGULAR_STRATA_CLOSED_LOCAL_POLES_OPEN`.
- Any edge incidence, phase identity or endpoint-zero inference fails:
  `SCIENTIFIC_FAIL_FIRST_MG_WICK_GEOMETRY_ROUTING`.
- Infrastructure failure before evaluation:
  `NUMERICAL_OR_INFRASTRUCTURE_FAIL`.

## Claim ceiling

A PASS fixes graph geometry, phase routing and which affine endpoints can carry local UV poles for the three connected cross channels. It does not compute a `1/epsilon` coefficient, B1, noncancellation, B0, EDT comparison, bridge, new physics or candidate theory. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
