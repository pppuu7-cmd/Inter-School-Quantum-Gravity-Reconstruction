# ITER160 preregistration — independent confirmation of raw G `b^2*S^2` endpoint support split

Date: 2026-09-17

Gate: `ITER160_FIRST_MG_G_B2S2_RAW_ENDPOINT_SUPPORT_CONFIRMATION`

Frozen parent: `8211cd1143ff549d2788cab8000662db17570659`.

## Epistemic status

This is a **confirmatory, prediction-known** gate, not a blind discovery gate.

The parent contains `analysis/ITER160_EXPLORATORY_G_B2S2_ENDPOINT_SPLIT_2026-09-17.md`, which openly records an exploratory Taylor-jet derivation. Therefore the numerical predictions below are frozen as already-known hypotheses. No discovery credit may be assigned to agreement.

## Frozen upstream scope

Consume only the ITER150 raw separated connected-cross TWO_PROPAGATOR master

`G_R1_chi2_Gamma2_dR1 : b^2*S^2`.

Frozen total simple-pole residue:

`R_total = -1050/(pi^4 L^10)` multiplying `1/epsilon` in `d=4-2 epsilon`.

Frozen affine factor:

`I(epsilon)=Integral_0^1 tau^(-4+2 epsilon) (1-tau)^(-5+2 epsilon) d tau`

under the ITER150 meromorphic-continuation prescription, equivalently

`B(-3+2 epsilon,-4+2 epsilon)`.

Frozen total Beta residue: `35`.

Frozen graph prefactor: `-30/(pi^4 L^10)`.

No other M/G family or invariant is consumed by this gate.

## Frozen predictions from the exploratory producer

Under minimal local endpoint extension/subtraction:

- lower endpoint `tau=0`: Beta residue `35/2`;
- upper endpoint `tau=1`: Beta residue `35/2`;
- lower raw graph pole: `-525/(pi^4 L^10)`;
- upper raw graph pole: `-525/(pi^4 L^10)`;
- endpoint sum equals the frozen total raw two-propagator pole.

These are predictions to be tested, not values to be refit.

## Independent confirmation method frozen before execution

Do **not** reproduce the exploratory binomial/Taylor-coefficient argument as the primary confirmation.

Use the meromorphic distribution identity on the half-line:

`Res_{epsilon=0} x^(-m-1+2 epsilon) = (-1)^m/(2 m!) delta^(m)(x)`

in the sense of distributions acting on smooth endpoint test factors.

For the lower endpoint use `m=3` and smooth factor `f_0(x)=(1-x)^(-5)`.

For the upper endpoint set `u=1-tau`, use `m=4` and smooth factor `f_1(u)=(1-u)^(-4)`.

The implementation must obtain each endpoint residue by distribution action,

`<delta^(m),f> = (-1)^m f^(m)(0)`,

rather than by reading the exploratory coefficients.

As held-out checks, independently verify:

1. the sum of the two local distributional residues equals the Laurent residue of `Gamma(-3+2 epsilon) Gamma(-4+2 epsilon) / Gamma(-7+4 epsilon)`;
2. after subtracting the required endpoint jets, the local remainder has no logarithmic endpoint singularity at `epsilon=0`;
3. multiplication by the frozen ITER150 prefactor reproduces the frozen total graph pole exactly.

## Support and subtraction firewall

This gate confirms only support decomposition of the already-separated raw TWO_PROPAGATOR master.

It must not:

- interpret the endpoint pieces as ITER118 counterterm coefficients;
- map them onto `[R,S,DR,DS,BoxR,D2R,BoxS,D2S]`;
- import or alter any ITER153 contact distribution;
- use ITER123 genuine-line projectors;
- reorder the ITER124 full renormalization prescription;
- claim survival through endpoint counterterms, line mixing, or full renormalization;
- infer `B1_total`.

The distinction `raw support residue != endpoint counterterm coefficient` is immutable.

## Frozen terminal classes

### PASS

`PASS_SCOPED_ITER160_RAW_G_B2S2_ENDPOINT_SUPPORT_SPLIT_INDEPENDENTLY_CONFIRMED`

iff the independent distributional method gives exactly the two frozen endpoint predictions, the local sum equals the frozen total Beta residue and graph pole, all held-out checks pass, and no forbidden sector is imported.

PASS confirms a raw-support decomposition only. It does not close slot 7.

### SCIENTIFIC_FAIL

`SCIENTIFIC_FAIL_ITER160_RAW_ENDPOINT_SPLIT_PREDICTION_NOT_CONFIRMED`

iff the independently implemented distribution identity under the frozen prescription gives a different endpoint residue or violates the frozen sum identity.

The exploratory values must then remain recorded and rejected; they may not be retuned.

### BLOCKED

`BLOCKED_SCOPED_ITER160_DISTRIBUTIONAL_ENDPOINT_SPLIT_REQUIRES_ADDITIONAL_EXTENSION_INPUT`

iff the frozen distribution identity is insufficient to define the split without an additional local extension/normalization choice. The exact missing primitive must be named; absence is not zero.

### INVALID

`INVALID_ITER160`

for implementation error, use of the exploratory values as hard-coded outputs instead of deriving them, post-outcome prescription mutation, contact import, basis/coefficient reinterpretation, or provenance failure.

## Critic requirements

An adversarial Critic must check at minimum:

- `d=4-2 epsilon` is retained through pole extraction;
- the lower singular power corresponds to `m=3` and upper to `m=4`;
- the factor `1/2` from `2 epsilon` is present;
- the source weight `(1-tau)` is already included in the upper exponent and is not counted twice;
- distribution derivative signs cancel correctly against test-function derivative signs;
- endpoint pieces sum to the frozen total but are not promoted to counterterm coefficients;
- no contact/line-projector information enters.

## Claim locks

`B1_total = UNAUTHORIZED`.

`BRIDGE_DERIVED = false`.

`NEW_PHYSICS_FOUND = false`.

Candidate theory remains `UNFORMED / 0%`.
