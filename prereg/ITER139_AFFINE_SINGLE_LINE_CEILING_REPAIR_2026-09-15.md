# ITER139 preregistration — affine single-line derivative ceiling repair

Date: 2026-09-15
Gate: `ITER139_FIXED_GEODESIC_CURVATURE_AFFINE_SINGLE_LINE_CEILING_REPAIR`
Status: **FROZEN BEFORE AUTHORITATIVE PRODUCTION RUN**

## Motivation

ITER138 closed exact connected Gaussian numerator kernels for `M_R2_chi1_dR1` and `G_R1_chi2_Gamma2_dR1`. It preserved the ITER129 total ceiling `D_total<=6` but exactly found independent-line degree 5 for the M family, whereas the ITER129 machine row recorded `N1_max=4`. The global ITER129 statement `N1_max<=5` remains intact.

This gate repairs the row-specific single-line ceiling logic before any endpoint pole extraction. It must not use a desired residue, B1 sign/value, EDT target or cancellation criterion.

## Frozen tasks

1. Reproduce the ITER138 exact independent-line degrees for the two already closed families from the committed tensor implementation:
   - `M_R2_chi1_dR1`: expected by prior authority to be 5, but this gate must recompute rather than hard-code the polynomial result;
   - `G_R1_chi2_Gamma2_dR1`: exact control row.
2. Construct the second Gaussian M family `M_R1_chi1_dR2` explicitly, using
   `dR2_mu(A(q),B(k)) = i(q+k)_mu R2(A(q),B(k))`,
   with the same de Donder, chi1 and D=4 tensor conventions as ITER138.
3. Measure total and independent-line polynomial degrees before imposing `k=p-q`.
4. Independently validate the new M numerator on at least three deterministic exact panels using the ten-component symmetric-basis Wick contraction, not merely the propagated-source shortcut.
5. Audit the old ITER129 rule `N1_max=D_line_max+D_partner_max` against exact nonlinear-vertex allocation. A nonlinear vertex's derivative budget may be allocated onto either internal leg; a row-specific ceiling is valid only if it upper-bounds the exact independent-line degree.
6. Emit a prospective corrected affine ceiling table V2. Historical ITER129 files remain immutable evidence; V2 is an addendum/correction, not a rewrite of the old terminal result.

## Frozen conservative policy for rows without exact tensor allocation

ITER129 already established the global affine one-propagator bound `N1_max<=5`. Therefore, for any affine row not exactly recomputed here:

- if its old row ceiling is 5, retain 5;
- if its old row ceiling is 4 and no exact tensor result closes it here, raise the prospective V2 ceiling to 5 and mark `authority=GLOBAL_SAFE_BOUND_PENDING_EXACT_ALLOCATION`.

This policy may lose row-specific sharpness but cannot lower the previously authorized global safety margin.

## Frozen local-jet map

For a one-propagator local endpoint channel after bulk subtraction, use the ITER126/129 rule

`m_raw = 2 + N1`,
`jet = m_raw - s - 1`,

where `s` is the exact source polynomial suppression. For bulk chi1 weight `(1-tau)`, `s_lower=0`, `s_upper=1`.

The gate records resulting ceiling orders only. It does **not** evaluate a curvature pole residue.

## Frozen classifications

- If all exact recomputations/direct checks pass and V2 upper-bounds every exact row while never exceeding the ITER129 global bound 5:
  `PASS_SCOPED_AFFINE_SINGLE_LINE_CEILING_REPAIR_CLOSED_ENDPOINT_POLES_OPEN`.
- If an exact family exceeds global `N1=5`:
  `SCIENTIFIC_FAIL_ITER129_GLOBAL_SINGLE_LINE_BOUND` and pole work stops pending a broader census repair.
- If an exact direct/tensor identity fails:
  `SCIENTIFIC_FAIL_ITER139_TENSOR_ALLOCATION` unless a purely technical implementation defect is demonstrated without changing these predicates.
- Infrastructure failure before evaluation: `NUMERICAL_OR_INFRASTRUCTURE_FAIL`.

## Claim ceiling

A PASS is a corrected derivative/jet ceiling authority only. It is not a `1/epsilon` residue, B1 result, noncancellation theorem, B0 result, EDT comparison, bridge, new physics or candidate theory. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
