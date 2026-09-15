# ITER138 preregistration — first exact M/G numerator kernels and derivative-allocation ceiling audit

Date: 2026-09-15
Gate: `ITER138_FIXED_GEODESIC_CURVATURE_FIRST_MG_EXACT_NUMERATOR_KERNELS_AND_CEILING_AUDIT`
Status: **FROZEN BEFORE AUTHORITATIVE PRODUCTION RUN**

## Provenance and bookkeeping

Canonical ITER132 (`27a8c8d...`) asked for exact Gaussian M/G numerator jets but stopped at `BLOCKED_MISSING_PREREQUISITE`. ITER133-137 then accumulated the missing localization, derivative and tensor diagnostics. Canonical ITER131 is already an explicit repaired D=4 R2/Gamma2 authority (`da613bc...`, terminal `429f3a96...`). The later independently coded D=4 direct-metric replication is retained as corroborating `RPL-D4-01` under `recovery/ITERATION_ID_RECONCILIATION_2026-09-15.md`.

A non-authoritative scratch calculation performed while reconciling the history suggested that the M-family per-line degree may be larger than the ITER129 `N1_max=4` table entry. That scratch result is **not** accepted as evidence. Because it has been seen, this gate is explicitly confirmatory/adversarial: either reproduction or refutation is an allowed frozen outcome, and no threshold may be changed after the production run.

## Frozen families

This gate covers only the connected Gaussian cross-Wick numerator kernels for:

1. `M_R2_chi1_dR1`;
2. `G_R1_chi2_Gamma2_dR1`, specifically the source-qualified Gamma2 term in chi2.

The local/self-pairing Wick channel is recorded separately and is not silently discarded; its renormalized treatment belongs to the later pole/subtraction gate. No claim is made here for the other ITER129 M/G rows.

## Frozen conventions

- Flat Euclidean D=4 tensor algebra, de Donder numerator
  `P_ab,cd = 1/2(delta_ac delta_bd + delta_ad delta_bc - delta_ab delta_cd)`.
- Symmetric graviton field.
- Independent internal line momenta `q` and `k` are retained first. Only after derivative-allocation degrees are measured may the routing substitution `k=p-q` be made.
- For sparse polynomial emission use a line-adapted orthonormal frame `n=(1,0,0,0)`. This is a frame choice, not an angular average. Two additional exact rational unit-vector panels must confirm that any claimed highest per-line degree is not an artifact of this frame.
- Linear scalar-curvature tensor:
  `A_ab(l)=l^2 delta_ab-l_a l_b`.
- `dR1_mu(l)=i l_mu A_ab(l) h_ab(l)`.
- First-order path source is the exact indexed `-Gamma1^mu_nn` coefficient from canonical ITER127/133 conventions, with affine weight `(1-tau)`.
- The admitted second-order G source is the exact indexed `-Gamma2^mu_nn` term, with the same source-qualified outer weight `(1-tau)`.
- R2/Gamma2 definitions are byte-equivalent in algebra to canonical repaired ITER131; no on-shell, integration-by-parts, equation-of-motion or target-based simplification is allowed.
- No EDT target, desired B1 sign/value or desired cancellation enters generation or classification.

## Frozen contraction definition

Let `P[S]` denote contraction of a symmetric linear source tensor with one de Donder propagator numerator. The connected cross-pairing numerators are constructed as exact tensor contractions:

- M: R2 receives one propagated `chi1/Gamma1` source and one propagated `dR1` source; sum the geodesic displacement index exactly.
- G: Gamma2 receives one propagated `R1` source and one propagated `dR1` source; contract its upper geodesic-displacement index and both lower indices with `n` exactly.

The nonlinear vertices' Bose symmetrization supplies the two cross pairings. The third Gaussian Wick pairing (quadratic vertex self-pairing times the two linear operators paired together) is emitted in the channel manifest as local/self-pairing and is not used to manufacture a nonlocal numerator PASS.

## Frozen outputs

For each M/G cross numerator:

1. exact expanded sparse polynomial in independent `q,k` in the adapted frame;
2. monomial count, total degree, maximum `q` degree and maximum `k` degree;
3. exact highest-`k` homogeneous component;
4. routed polynomial after `k=p-q`, with total degree and loop-`q` degree;
5. exact Bose/leg-exchange consistency;
6. at least three deterministic held-out exact evaluations comparing the fast propagated-source contraction with an independently assembled ten-component symmetric-basis Wick contraction;
7. rational-unit-vector covariance panels for the maximum per-line degree;
8. affine metadata `(1-tau)`, lower endpoint suppression 0, upper endpoint suppression +1;
9. comparison with ITER129 `D_total=6` and `N1_max=4` for these two rows.

## Frozen decisions

- If both exact numerator kernels exist, total degree is <=6, all tensor/direct/covariance checks pass, and each independent-line degree is <=4:
  `PASS_SCOPED_FIRST_MG_EXACT_NUMERATOR_KERNELS_CLOSED_ITER129_CEILINGS_CONFIRMED`.
- If both kernels and all checks pass, total degree remains <=6, but an exact nonzero independent-line degree 5 term is reproduced for either family:
  `PASS_SCOPED_FIRST_MG_EXACT_NUMERATOR_KERNELS_CLOSED_ITER129_SINGLE_LINE_CEILING_REOPENED`.
  In this branch no endpoint residue may be extracted until the affected ITER129/ITER126 jet ceiling is corrected prospectively.
- If an exact tensor/Bose/direct/covariance identity fails:
  `SCIENTIFIC_FAIL_FIRST_MG_NUMERATOR_CONSTRUCTION` unless a purely technical implementation defect is demonstrated without changing these predicates.
- Resource failure before predicates are evaluated:
  `NUMERICAL_OR_INFRASTRUCTURE_FAIL`.

## Claim ceiling

Even a PASS is only an exact unintegrated Gaussian numerator result for two connected M/G families. It is not a pole residue, B1 determination, noncancellation result, finite B0 result, EDT comparison, bridge, new physics or candidate theory. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
