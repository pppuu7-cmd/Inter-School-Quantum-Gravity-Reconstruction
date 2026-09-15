# ITER148 preregistration — full D=4 M3 invariant numerator and canonical bubble reduction

Date: 2026-09-15
Gate: `ITER148_FIXED_GEODESIC_CURVATURE_M3_FULL_INVARIANT_BUBBLE_REDUCED_NUMERATOR`
Execution dependency: ITER147 must classify `PASS_SCOPED_RATIONAL_S3_EVALUATOR_AND_M3_SLICE_REPAIR_CLOSED_FULL_INVARIANT_OPEN`.

## Frozen motivation

ITER147 closes exact rational-momentum tensor allocation for the interaction-dressed family `M_R1_chi1_dR1_S3` and shows realized affine loop degree exactly 8 on all four held-out slices. ITER145 independently proves the apparent three-denominator routing reduces algebraically to three bubble terms. The next admissible step is to reconstruct the complete D=4 scalar numerator in a covariant invariant basis and attach the exact ITER145 bubble/canonical-loop maps before any dimensional pole extraction.

## Frozen tensor object and routing

Use exactly the ITER147 repaired rational S3 authority and ITER145 routing

`p=-q-(1-tau)k`,
`r=q-tau k`,

for the frozen contraction

`R1(p) x [(1-tau) chi1(k).partial R1(r)] x S3(p,k,r)`

with three D=4 de Donder propagator numerators. No integration by parts, on-shell identity, denominator cancellation, target coefficient or fitted physics input is admitted.

The pinned S3 source tensor structure may be contracted through the ITER144 independently reconstructed Einstein-Hilbert Gamma-Gamma cubic form using the already authorized exact constant relation

`S3_source_contraction = -2 * EH_GammaGamma_cubic_contraction`,

but only if this fast contraction is revalidated exactly against the repaired direct rational ITER147 source evaluator on deterministic rational full-polarization/M3 panels before production reconstruction.

## Frozen D=4 invariant basis

Let

`Q=q^2`, `K=k^2`, `S=q.k`, `a=q.n`, `b=k.n`, `n^2=1`.

The numerator is homogeneous of total momentum degree 8 and contains at most two powers of the unit line vector. The frozen basis has exactly 45 monomials:

1. 15 scalar monomials `Q^i K^j S^l` with `i+j+l=4`;
2. 30 line-dependent monomials `X Q^i K^j S^l` with `i+j+l=3` and `X in {a^2, a b, b^2}`.

No basis enlargement is allowed after production data are seen.

## Frozen tau polynomial bound

All tau dependence enters through the linear routed momenta p/r and the explicit source weight `(1-tau)`. The exact tensor construction therefore has formal tau degree <=8.

Use nine frozen training values

`tau in {0,1/8,2/8,3/8,4/8,5/8,6/8,7/8,1}`

to reconstruct every invariant coefficient as a polynomial of degree <=8. Validate without refitting at `tau=1/3` and `tau=2/5` on held-out q/k panels not used in the 45-panel solve.

## Frozen reconstruction predicates

A. Build a deterministic exact 45-panel design matrix in D=4 with `n=e0` only as a coordinate frame; require exact rank 45.
B. Revalidate the fast `-2 * EH_GammaGamma` contraction against the repaired direct rational pinned-source contraction on at least three nontrivial rational M3 panels before using it for the 45x9 production table.
C. At each of the nine training tau values, solve exactly for all 45 invariant coefficients and verify direct held-out q/k panels at that same tau.
D. Interpolate each of the 45 coefficient functions in tau; require realized degree <=8.
E. Without refitting, validate the full invariant numerator at tau=1/3 and 2/5 on additional held-out q/k panels.
F. Preserve exact S3 leg permutation, ITER145 routing conservation, source weight `(1-tau)`, and global `(q,k)->(-q,-k)` parity controls.
G. Keep construction target-independent and denominator-integration-free.

## Frozen ITER145 bubble reduction

With

`D1=[q+(1-tau)k]^2`, `D2=k^2`, `D3=[q-tau k]^2`,

verify exactly

`tau D1 + (1-tau) D3 - tau(1-tau) D2 = Q`

and therefore

`N/(D1 D2 D3)`
`= (tau/Q) N/(D2 D3)`
`+ ((1-tau)/Q) N/(D1 D2)`
`- (tau(1-tau)/Q) N/(D1 D3)`.

Also emit and verify the three canonical massless-bubble loop maps, with canonical loop `l` and invariants `L=l^2`, `T=q.l`, `c=l.n`:

### Bubble A: D2 D3

`l=-tau k`, hence

`K=L/tau^2`, `S=-T/tau`, `b=-c/tau`,

and measure plus partial-fraction prefactor gives

`tau^(3-d)/Q * N(Q,L/tau^2,-T/tau,a,-c/tau,tau) / [l^2 (q+l)^2]`.

### Bubble B: D1 D2

`l=(1-tau)k`, hence

`K=L/(1-tau)^2`, `S=T/(1-tau)`, `b=c/(1-tau)`,

and

`(1-tau)^(3-d)/Q * N(Q,L/(1-tau)^2,T/(1-tau),a,c/(1-tau),tau) / [l^2 (q+l)^2]`.

### Bubble C: D1 D3

`l=(1-tau)(tau k-q)`, hence

`K=Q/tau^2 + 2T/[tau^2(1-tau)] + L/[tau^2(1-tau)^2]`,
`S=Q/tau + T/[tau(1-tau)]`,
`b=a/tau + c/[tau(1-tau)]`,

and

`-[tau(1-tau)]^(3-d)/Q * N(transformed invariants,tau) / [l^2 (q+l)^2]`.

The endpoint-degenerate tau=0/1 cases remain governed by the already verified ITER145 endpoint limits and are not obtained by naively substituting into singular canonical variable maps.

## Frozen classifications

- `PASS_SCOPED_M3_FULL_D4_INVARIANT_AND_CANONICAL_BUBBLE_REDUCTION_CLOSED_GENERAL_D_POLES_OPEN` iff A-G and all three bubble-map identities pass exactly.
- `SCIENTIFIC_FAIL_M3_INVARIANT_BASIS_OR_TAU_DEGREE` if the 45-basis, tau-degree or exact held-outs fail.
- `FAIL_M3_FAST_CONTRACTION_AUTHORITY_MISMATCH` if the accelerated EH contraction disagrees with repaired direct pinned-source evaluation.
- `FAIL_ITER145_BUBBLE_CANONICAL_MAP` if any denominator/Jacobian/invariant substitution identity fails.

## Claim ceiling

A PASS supplies the full D=4 interaction-dressed M3 invariant numerator and an exact canonical-bubble representation. It does not yet supply general-d/O(epsilon) continuation, master poles, renormalized endpoint subtraction, B1, noncancellation, B0, EDT comparison, bridge, new physics or candidate theory. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
