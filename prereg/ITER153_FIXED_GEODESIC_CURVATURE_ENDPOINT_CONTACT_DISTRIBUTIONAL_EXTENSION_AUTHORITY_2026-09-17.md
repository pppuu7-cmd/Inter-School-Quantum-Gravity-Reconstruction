# ITER153 preregistration — fixed-geodesic curvature endpoint-contact distributional extension authority

Date: 2026-09-17
Frozen parent `main`: `d44245c8a1387df197489e95296096c3f004451e`
Gate: `ITER153_FIXED_GEODESIC_CURVATURE_ENDPOINT_CONTACT_DISTRIBUTIONAL_EXTENSION_AUTHORITY`

## Scientific objective

Close or sharply terminalize ITER152 slot 5 only: determine whether the seven already-frozen ITER151 one-propagator endpoint contacts admit a source-faithful distributional pullback/extension and dimensional pole authority from the existing general-d kernels plus dimensional regularization, without importing ITER126 prototype residues, choosing post-hoc counterterms, assuming cancellations, fitting coefficients, selecting a desired sign, or inventing an arbitrary local extension.

No `B1_total` may be formed in this gate. Slots 6-10 remain outside the PASS scope.

## Immutable upstream identities

Frozen source identities at the parent commit:

- `analysis/ITER151_RESULT_2026-09-16.md` — terminal seven-contact manifest and claim locks;
- `analysis/iter151_first_mg_contact_renormalization_authority_gate.py` — contact/support authority gate;
- `analysis/iter143_first_mg_denominator_contact_partition.py` — denominator-cancellation/support rules;
- `analysis/iter141_first_mg_wick_geometry_phase_strata.py` — affine endpoint geometry and Fourier phases;
- `analysis/iter142_first_mg_shrinking_edge_derivative_jets.py` — shrinking-edge degree/jet controls;
- `analysis/iter140_first_mg_general_d_invariant_continuation.py` and `analysis/iter140_first_mg_general_d_invariant_continuation_v3.py` — exact invariant definitions and `d=4-2 epsilon` continuation;
- `sources/ITER126_FIXED_GEODESIC_CURVATURE_LINE_ENDPOINT_COINCIDENCE_POLE_EXTRACTION_AUTHORITY_2026-09-15.md` — subtraction method only; its prototype residues are explicitly non-transferable;
- `sources/ITER107_RETROSPECTIVE_FIXED_GEODESIC_DISTANCE_EFT_CURVATURE_CORRELATOR_AUTHORITY_2026-09-15.md` — fixed-geodesic restriction/renormalization context.

Any mismatch with the frozen parent identities makes the implementation invalid rather than scientifically negative.

## Exact seven contact structures

The contact set is immutable and must be validated verbatim against terminal ITER151:

1. `M_R2_chi1_dR1 : b^2*Q*S`, lower endpoint, coefficient `-1/2`.
2. `M_R1_chi1_dR2 : a^2*K*S`, upper endpoint, coefficient `3/4`.
3. `M_R1_chi1_dR2 : a^2*K^2`, upper endpoint, coefficient `1/2`.
4. `M_R1_chi1_dR2 : a*b*K*S`, upper endpoint, coefficient `-1`.
5. `G_R1_chi2_Gamma2_dR1 : K*S^2`, upper endpoint, coefficient `-1/(2*d - 4)`.
6. `G_R1_chi2_Gamma2_dR1 : a^2*K*S`, upper endpoint, coefficient `(d - 1)/(2*d - 4)`.
7. `G_R1_chi2_Gamma2_dR1 : a*b*K*S`, upper endpoint, coefficient `1/(d - 2)`.

Invariant convention is frozen from ITER140:

`Q=q^2`, `K=k^2`, `S=q.k`, `a=n.q`, `b=n.k`, `n^2=1`.

The original two-propagator denominator before a single cancellation is `Q*K`. A Q-cancelled contact is polynomial in the shrinking q momentum and retains the K propagator. A K-cancelled contact is polynomial in the shrinking k momentum and retains the Q propagator.

## Dimensional convention

Freeze

`d = 4 - 2 epsilon`, `epsilon -> 0`,

with exact symbolic/rational arithmetic. No floating threshold may enter a scientific decision.

The physical microlocal pullback check is performed at integer physical dimension `d=4`; the general-d coefficients and their Laurent expansion remain exact symbolic input data.

## Endpoint coordinates, affine maps and phases

Freeze anchored geometry `x=0`, `y=L n`, `L>0`, `n^2=1`.

Use local endpoint coordinate `s>=0` increasing into the line:

- lower endpoint: `s=tau`, shrinking q-edge separation `L*s`; ITER141 phase is `exp[-i s L (n.q)]` in `M_R2_chi1_dR1`;
- upper endpoint: `s=1-tau`, shrinking k-edge separation `L*s`;
  - `M_R1_chi1_dR2` has shrinking-k phase `exp[+i s L (n.k)]`;
  - `G_R1_chi2_Gamma2_dR1` has shrinking-k phase `exp[-i s L (n.k)]`.

For the standard diagnostic Fourier convention

`delta^(d)(x) = integral d^d p/(2*pi)^d exp[-i p.x]`,

these signs define the line embeddings used for the formal contact transform:

- negative phase: `F_-(s)=+L*s*n`;
- positive phase: `F_+(s)=-L*s*n`.

The existence/nonexistence decision is invariant under the overall sign of `F`, but derivative signs must remain recorded. Overall amplitude normalization is not promoted unless already fixed by a frozen parent object.

## Distribution and test-function space

Work locally on an open interval `U=(-delta,delta)` around each endpoint coordinate `s=0`, then restrict to the physical half-interval after the distributional question is settled. Test functions are `C_c^infty(U)`.

The ambient contact distribution is a tempered distribution on `R^4` obtained by Fourier transforming the polynomial dependence on the cancelled shrinking momentum. A cancelled-momentum polynomial of total degree `m` gives a finite linear combination of order-`m` derivatives of `delta^(4)` contracted with the retained external/surviving momentum and `n` tensors.

The singular support is therefore the ambient coincidence point `x=0`; its line preimage is the endpoint `s=0`.

## Pullback map and microlocal admissibility

The canonical distributional restriction is the pullback `F^* T` under `F(s)=+/- L*s*n`.

Admissibility is prospectively judged by the standard wavefront pullback criterion: if `WF(T)` is disjoint from the normal set `N_F`, the canonical pullback is licensed. Failure of that sufficient criterion does not by itself authorize assigning a value; an alternative pullback/extension may be accepted only if it is supplied by an independently source-qualified analytic family tied to the frozen parent kernel and contains no newly chosen finite local datum.

For every contact the implementation must record:

- ambient wavefront class;
- the line normal set;
- whether their intersection is empty;
- whether a canonical pullback is thereby authorized.

## Scaling degree, homogeneity and singular order

For each formal ambient derivative contact of order `m`, record exact physical-dimension scaling data. For `partial^alpha delta^(4)` with `|alpha|=m`, the ambient scaling degree is `4+m`, homogeneity degree is `-(4+m)`, and ambient singular order relative to dimension four is `m`.

These quantities are metadata, not a license to invent a line pullback.

## Frozen extension prescription

The only admissible prescriptions in ITER153 are, in order:

1. canonical Hörmander pullback when its wavefront criterion is satisfied;
2. otherwise, a unique meromorphic/analytic continuation already determined by the exact frozen dimensional kernel, if such a family can be constructed without adding a second regulator, arbitrary finite local coefficient, desired-sign condition, or counterterm input.

If neither route uniquely determines the endpoint distribution/pole data, the contact is `BLOCKED_SCOPED_REQUIRES_NEW_LOCAL_EXTENSION_INPUT`.

No minimal subtraction or endpoint/line counterterm is to be chosen here; those belong to downstream slots 6-9. A finite or divergent local ambiguity must be exposed, not fixed.

## Allowed local ambiguity record

If a canonical pullback is unavailable, record the most specific endpoint-supported ambiguity class justified by the source/mathematics. Coefficients of endpoint-supported `delta(s)` and its derivatives are not to be set from desired cancellation. If the exact finite-dimensional ambiguity basis cannot itself be fixed without downstream counterterm/mixing authority, record that dependency explicitly and classify slot 5 as blocked rather than silently setting it to zero.

## Measure/Jacobian convention

The local line coordinate is dimensionless `s`; physical displacement is `L*s*n`. Any valid pullback/regularized line restriction must retain the `L` scaling induced by this map. A control with `L` omitted must be rejected. Endpoint orientation is frozen as above.

## Pole extraction convention

When an admissible exact analytic family exists, expand at `d=4-2 epsilon` and record separately the exact coefficients of `1/epsilon^2`, `1/epsilon`, and the finite local ambiguity. A coefficient may be declared zero only by exact symbolic proof within an authorized family. Absence of authority is `BLOCKED`, not zero.

## Independent methods

Where mathematically applicable, require two genuinely independent routes:

A. direct microlocal/distributional construction from the cancelled-momentum Fourier contact and the line pullback criterion;

B. an independent analytic regularization/mollifier/scaling test that probes whether a regulator-independent line distribution is obtained without an extra local renormalization datum.

Agreement on a nonzero/zero pole may promote a coefficient only if both methods refer to the same frozen object. If method B introduces an extra regulator, it is diagnostic of uniqueness/nonuniqueness only and may not become a new numerical prescription.

## Adversarial controls

The evaluator must reject or flag, for the correct reason:

- wrong endpoint orientation relative to ITER141;
- wrong shrinking momentum/contact support relative to ITER143/151;
- omitted `L` Jacobian/scaling in the line embedding;
- deliberately modified dimensional convention/exponent;
- illegal substitution of the ITER126 prototype residues `+2` or `-1` as curvature contact residues;
- hard-coded expected pole or desired cancellation;
- changed seven-contact set;
- post-outcome extension/counterterm choice.

## Decision rules

`PASS_SCOPED_SLOT5_SEVEN_CONTACT_DISTRIBUTIONAL_POLE_AUTHORITY_CLOSED` only if all seven frozen contacts have source-faithful distributional pullback/extension and exact pole authority sufficient to close ITER152 slot 5, with every remaining finite local ambiguity explicitly recorded and without requiring a new unauthorized local prescription.

`BLOCKED_SCOPED_SLOT5_REQUIRES_NEW_DISTRIBUTIONAL_EXTENSION_OR_RENORMALIZATION_INPUT` if at least one mandatory contact cannot be assigned source-faithful line distribution/pole data from the frozen dimensional object without a new local extension/renormalization input.

`SCIENTIFIC_FAIL_SCOPED_ITER153_FROZEN_MATHEMATICAL_HYPOTHESIS_FALSIFIED` only when a positively preregistered mathematical existence/identity check is exactly falsified rather than merely unsupported.

`INVALID_IMPLEMENTATION_ITER153` for wrong frozen contact set, changed parent kernel/support, post-outcome extension prescription, ITER126 prototype-residue copying, hard-coded desired pole/cancellation, floating threshold, or missing lineage/provenance.

Infrastructure failure is not a scientific failure.

## Reproducibility and critic

The implementation must emit deterministic machine-readable JSON, run twice in the same clean full-history GitHub Actions job with byte-identical output, preserve SHA256, and preserve the raw artifact. An independent adversarial critic must inspect endpoint sign, `L` scaling, contact derivative order, wavefront/pullback logic, implicit zeros, arbitrary extension choices, and prototype-residue leakage before recovery promotion.

## Claim ceiling

ITER153 concerns slot 5 only. It cannot by itself establish graph-specific subdivergence subtraction, endpoint counterterm coefficients, line-defect mixing, renormalized contact mapping, any of the six terminal ITER124 outputs, full first-M/G noncancellation, gauge/BRST closure, EDT matching, bridge derivation, new physics, or candidate theory. `BRIDGE_DERIVED=false`, `NEW_PHYSICS_FOUND=false`, candidate theory remains `UNFORMED / 0%`.