# ITER138 terminal result — first exact M/G numerator kernels and ceiling audit

Date: 2026-09-15
Preregistration: `bbb6b19bf063353510e7fb292498ceb571e30898`
Implementation: `11e493a541ec91bd9510af3a2f2c230da10964c2`
Workflow head: `9c16d18bbd58728e49170ab9b0b96e0affac8f03`
Authoritative run: `34957193433`
Job: `104341966119` (`numerator-ceiling-audit`)
Artifact: `10392280306` (`iter138-first-mg-exact-numerator-kernels`)
Artifact SHA256: `4ed1ec825b8442b5b2e7f525f18f989e582672436a578ca1635560d64c14e4ba`

## Scientific classification

`PASS_SCOPED_FIRST_MG_EXACT_NUMERATOR_KERNELS_CLOSED_ITER129_SINGLE_LINE_CEILING_REOPENED`

All frozen tensor, symmetry, direct-basis, rational-unit-vector covariance, affine-source and target-blind checks passed. Both admitted connected Gaussian numerator kernels are explicitly nonzero and remain within the ITER129 total derivative ceiling `D_total<=6`.

## Exact independent-line degrees

For independent internal momenta `q,k` before routing `k=p-q`:

- `M_R2_chi1_dR1`: total degree 6, q-degree 3, **k-degree 5**, 131 monomials;
- `G_R1_chi2_Gamma2_dR1`: total degree 6, q-degree 3, k-degree 4, 119 monomials.

Thus the global ITER129 statement `N1_max<=5` remains valid. However the row-specific machine-table entry `M_R2_chi1_dR1: N1_max=4` is too low and is reopened for prospective correction. The G row remains compatible with `N1_max=4`.

The exact highest degree-5 M component in the line-adapted frame `n=(1,0,0,0)` is

`1/2 (k1^2+k2^2+k3^2) (k0^2+k1^2+k2^2+k3^2) (k0 q0+k1 q1+k2 q2+k3 q3)`.

Equivalently, the rational-unit-vector panels confirm the covariant form

`1/2 [k^2-(k.n)^2] k^2 (k.q)`

for unit `n`. This establishes that the degree-5 term is not an artifact of choosing `n=e0`.

## Validation strength

The production calculation compared two independent contraction paths on three deterministic exact panels:

1. propagated symmetric tensor sources through the de Donder map `P[S]`;
2. a separately assembled ten-component symmetric-basis Wick contraction.

They agree exactly for both M and G kernels. R2/Gamma2 graviton-leg exchange identities and de Donder projector symmetry also pass exactly.

## Consequence for local endpoint jets

ITER126 uses `m_raw=2+N` for one-propagator local singular channels and `jet=m_raw-s-1` after source suppression `s`. Therefore, for the reopened M row, the conservative row-specific local ceiling changes from `N=4` to `N=5`:

- lower endpoint (`s=0`): `m_raw<=7`, Taylor/jet ceiling `<=6` rather than 5;
- upper endpoint with the exact `(1-tau)` suppression (`s=1`): effective Taylor/jet ceiling `<=5` rather than 4.

This is a ceiling correction only. No curvature pole residue has been extracted, and tensor/subtraction structure may still lower or eliminate the actual residue.

## Wick-channel scope

ITER138 closes the connected cross-pairing numerator kernels only. The third Gaussian Wick channel — quadratic-vertex self-pairing times the two linear operators paired together — is explicitly recorded and deferred to the renormalized local/tadpole subtraction gate rather than silently discarded.

## Claim ceiling

No `1/epsilon` coefficient, `B1`, noncancellation result, finite `B0`, EDT comparison, bridge, new physics or candidate theory follows. Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.

## Exact successor

Prospectively repair the row-specific ITER129 single-line ceiling for `M_R2_chi1_dR1`, verify the induced ITER126 lower/upper endpoint Taylor orders, and preserve the unchanged G row. Endpoint-pole evaluation remains blocked until that corrected ceiling is frozen and validated.
