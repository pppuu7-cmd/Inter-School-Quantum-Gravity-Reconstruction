# ITER126 source authority — fixed-geodesic curvature line endpoint/coincidence pole extraction

Date: 2026-09-15
Gate: `ITER126_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COINCIDENCE_POLE_EXTRACTION_AUTHORITY`
Preregistration: `prereg/ITER126_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COINCIDENCE_POLE_EXTRACTION_AUTHORITY_2026-09-15.md`
Authoritative implementation: `analysis/iter126_defect_pole_prototypes_v2.py`
Workflow: `.github/workflows/iter126_defect_pole_prototypes.yml`
Artifact: `iter126-defect-pole-prototypes`

## 1. Residual defect poles are local in affine-parameter space

After ordinary bulk/subgraph UV divergences are subtracted, consider a compact subdomain of the line-parameter integration in which:

- no line point approaches an endpoint that coincides with another insertion;
- no two line points coincide;
- all relevant coordinate separations remain bounded below by a positive fraction of the physical geodesic length `l`.

On such a subdomain, massless coordinate-space propagators and their finite number of derivatives are ordinary smooth functions/distributions at nonzero separation. The remaining affine-parameter integral is finite at `epsilon -> 0`.

Therefore residual defect UV poles arise only from local boundary strata:

- endpoint regions `tau -> 0,1`;
- line-line coincidence `tau -> sigma`;
- intersections/overlaps of such regions in two-parameter integrals.

Predicate A: **PASS**.

## 2. General one-dimensional local subtraction formula

A useful local model is

`I(epsilon)=int_0^1 d x x^(-m+a epsilon) w(x,epsilon)`,

where `m` is a positive integer and `w` is smooth near `x=0`.

Taylor-expand at `epsilon=0`:

`w(x,0)=sum_k w_k x^k`.

Termwise analytic continuation gives denominators

`k-m+1+a epsilon`.

Hence the pole at `epsilon=0` is controlled by the **single local Taylor coefficient** with

`k=m-1`,

and

**`Res I = w_(m-1)/a`**

for that endpoint, with higher Taylor terms finite and lower terms corresponding to analytically continued power-divergent pieces away from the logarithmic pole.

This explains why a nominal `x^-2` singularity can have a `1/epsilon` residue controlled by the *linear* term of the smooth weight rather than by its constant term.

This local formula is the core of the ITER126 subtraction method.

## 3. Endpoint-product prototype

For `d=4-2 epsilon`, a product of two massless propagator scalings attached to opposite endpoints yields the prototype

`E(epsilon)=int_0^1 d tau [tau(1-tau)]^(-2+2 epsilon)`.

Analytic continuation gives

`E = B(-1+2 epsilon,-1+2 epsilon)`.

Using Gamma recurrence to move all Gamma functions near positive arguments, the symbolic workflow verifies

**`Res_{epsilon=0} E = +2`.**

The local formula reproduces this transparently:

near `tau=0`,

`w(tau)=(1-tau)^-2 = 1+2 tau+...`,

so `m=2`, `a=2`, `w_1=2` gives residue `+1`; the `tau=1` endpoint contributes another `+1`.

Predicate B: **PASS**.

## 4. Line-line coincidence prototype

For a single massless propagator between two line points,

`D(epsilon)=int_0^1 d tau int_0^1 d sigma |tau-sigma|^(-2+2 epsilon)`.

Changing to the separation `delta=|tau-sigma|` gives exactly

`D = 2 int_0^1 d delta (1-delta) delta^(-2+2 epsilon)`

and therefore

`D = 1/[epsilon(-1+2 epsilon)]`.

The workflow verifies

**`Res_{epsilon=0} D = -1`.**

Again the local rule explains the sign: the smooth weight is `2(1-delta)=2-2 delta`, so `w_1=-2`; with `m=2`, `a=2`, the residue is `-1`.

Predicate C: **PASS**.

## 5. Why these are prototypes, not curvature residues

Curvature insertions, geodesic vertices and gauge/projector numerators can apply derivatives, multiply by powers of affine parameters and alter the local singular exponent `m` and smooth Taylor weight `w`.

Therefore `+2` and `-1` are **not** transferable values for any F/M/G coefficient or for `B_1`.

Their role is to verify the extraction method and show exactly how local affine Taylor data determine poles.

Predicate D: **PASS_CONTROL**.
`PROTOTYPE_B1_SWAP_CONTROL`: **PASS_CONTROL**.

## 6. Smooth finite line form factors do not require full integration for pole extraction

Near any singular stratum, a smooth phase/form-factor/kinematic weight can be Taylor-expanded in the local small parameter. Power counting determines a finite number of Taylor coefficients that can multiply pole-producing monomials.

The subtracted remainder has improved local degree and is integrable at `epsilon=0`; it can be left for later finite symbolic/numerical integration if the full `B_0` function is eventually required.

Thus finite oscillatory dependence away from endpoint/coincidence regions cannot alter the pole residue except through its local Taylor coefficients at those regions.

Predicate F: **PASS**.

## 7. Overlapping M2 regions require sector/forest subtraction

Two-parameter bubble/localization families can contain overlapping regions such as:

- `tau -> 0` simultaneously with `sigma -> 0`;
- `tau -> sigma` near an endpoint;
- ordered `chi_2` corner regions.

A naive sum of one-dimensional endpoint subtractions would double-count intersections and can assign higher poles incorrectly.

The correct method is to sector-decompose or apply an equivalent forest subtraction:

1. identify all singular strata;
2. resolve overlaps into sectors with ordered small variables;
3. expand smooth weights locally in each sector;
4. subtract nested/overlap contributions in forest order;
5. integrate singular monomials analytically;
6. verify the `1/epsilon^2` and `1/epsilon` hierarchy required by ITER124.

No finite interior value is needed to determine those pole coefficients.

Predicate E: **PASS_METHOD / OVERLAP SUBTRACTION REQUIRED**.
`OVERLAP_DOUBLE_COUNT_CONTROL`: **PASS_CONTROL**.

## 8. Authorized asymptotic-subtraction algorithm

For each M1-M3 scalar master after tensor reduction:

A. map the line domain to dimensionless affine variables;

B. list endpoint, diagonal and overlap singular strata;

C. determine the local power `m` from the propagator/derivative numerator structure;

D. Taylor-expand only to the finite order `m-1` (and corresponding multivariable orders) needed to capture poles;

E. integrate those local singular monomials analytically in `epsilon`;

F. subtract them from the exact integrand;

G. set `epsilon=0` in the finite remainder;

H. combine pole coefficients with bulk/counterterm subtraction before ITER123 projection.

Predicate G: **PASS_ALGORITHM**.

## 9. Symbolic and finite-interior checks

The authoritative `v2` workflow verifies:

- endpoint prototype residue `+2`;
- line-coincidence prototype residue `-1`;
- a representative fixed-cut interior integral is finite at `epsilon=0`.

The named artifact is present.

Predicate H: **PASS_INFRASTRUCTURE**.

## 10. Target independence

No EDT exponent, amplitude or desired sign is used in the residue extraction.

Predicate I: **PASS_CONTROL**.

## Source classification

**`PASS_SCOPED_DEFECT_POLES_LOCAL_ENDPOINT_COINCIDENCE_ASYMPTOTIC_SUBTRACTION_AUTHORIZED`**

The pole part of the geodesic master families can be extracted from local endpoint/coincidence asymptotics after ordinary bulk subtraction; complete finite line integrals are not needed for the RG/pole question.

## Highest-information successor

Apply the local subtraction algorithm to the **actual two ITER122 genuine-defect projector kernels** and the explicit `chi_1/chi_2` line weights from the fixed-geodesic expansion. The next gate should produce a table of local exponents/Taylor coefficients for every projected M/G singular stratum and determine which strata can feed the simple-pole beta data entering `B_1`.

## Claim ceiling

Bridge credit remains **0**. Candidate theory remains **UNFORMED / 0%**. The prototype residues are not curvature coefficients; no `B_1`, noncancellation theorem, EDT fit, direct discrepancy, bridge or new physics follows.