# ITER025 preregistration — coherent source-normalized qbar sign gauge

Date: 2026-09-14

## Authorization basis

ITER024 terminal classification is `RC006_GRAPHICAL_QBAR_COMPONENT_FAIL`. Its R, braid and adversarial lanes passed; the qbar lane failed only by an allowed normalized channel sign on three frozen cases while qbar coproduct intertwining passed. ITER025 therefore tests only the missing coherent qbar sign gauge. R and Yang–Baxter are not rerun for scientific credit.

Primary target remains arXiv:1609.02429v2, frozen e-print SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

No external q-CG formula, phase fit, physics amplitude, or hand-written per-channel correction table is allowed.

## Source-defined sign normalization algorithm

For every admissible ordered channel `(j1,j2)->j`:

1. construct the raw inverse-parameter embedding `D0` by the already validated qbar highest-weight solver on reversed tensor order `(j2,j1)`, with deterministic permutation back to source `(m1,m2)` component order and Appendix-B `1/sqrt(d_j)` scaling;
2. form `M0 = F_q D0`, where `F_q` is the source-normalized Appendix-B q fusion map;
3. **structural acceptance before normalization:** require `M0` to be scalar times identity to residual `<2e-9`, with nonzero scalar `g`, and require `||g|-1/d_j| <2e-9`;
4. let the target source scalar be `g_src = (-1)^(j1+j2-j)/d_j` from the frozen Appendix-B composition identity;
5. define the sign-normalized source dual `D = eta D0`, where `eta = g_src/g`;
6. require `|eta^2-1| <2e-9` and `|Im(eta)| <2e-9`. If eta is not numerically an allowed normalized sign, the channel FAILS. Eta is computed mechanically from the source identity and is never stored as a fitted lookup table.

The defining composition identity is used to fix the convention and therefore is **not** counted as an independent validation after normalization.

## Frozen panels

### Construction panel
Levels k=6,10,12. All admissible outputs for:
- `(1/2,1/2)`;
- `(1,1/2)`;
- `(2,1)`;
- at k=10,12 `(3,2)`;
- at k=12 `(4,2)`, `(3,3)`, `(4,4)` restricted to outputs with nonzero target quantum dimension.

### Independent singlet panel
For every level k=6,10,12 and every `j=1/2,1,...,k/2` for which the displayed source cap/cup is non-singular, compare the normalized `(j,j)->0` qbar dual directly to Appendix-B cup divided by `sqrt(d_j)`.

### 4-valent panel
At k=6,10,12 use external quadruples:
- `(1/2,1/2,1/2,1/2)`;
- `(1,1,1,1)`;
- `(2,1,2,1)` when admissible;
- at k=12 `(3,3,3,3)` and `(4,2,4,2)`.
Use every common admissible internal channel with nonzero quantum dimension.

## Parallel lanes

### Lane A — sign normalization construction audit

Across the construction panel record raw scalar `g`, source target scalar, eta, scalarity residual and magnitude residual.

PASS if every channel satisfies the structural acceptance and eta-sign conditions above. Also require the qbar-coproduct intertwiner residual of the raw/normalized embeddings `<2e-9`.

### Lane B — independent cup validation

Using the mechanically source-normalized duals from Lane-A algorithm, compare every frozen `(j,j)->0` channel to the exact Appendix-B cup component formula divided by `sqrt(d_j)`.

PASS if max residual `<2e-9`. No additional sign choice is allowed in this lane.

### Lane C — independent 4-valent dual identity

Construct the Appendix-B 4-valent basis from q fusion coefficients and the source-normalized qbar dual primitive. Construct its source-defined dual including the explicit `(-1)^(2j5) q^(m5)` weight. Contract all external magnetic indices.

PASS if the internal-channel matrix equals the frozen source identity
`(-1)^(j1+j2+j3+j4) d_j5^-1 delta_(j5,j5')`
with max absolute residual `<5e-8` across every frozen panel.

A panel with a trace-zero internal quantum dimension is excluded only by the prospectively frozen nonzero-dimension predicate; no exclusion may be added after output.

### Lane D — held-out/adversarial sign calibration

Use held-out levels k=7,9,11 and low/mid-spin admissible pairs not in the construction panel. Apply the same algorithm unchanged; require structural sign acceptance, qbar intertwining `<5e-9`, and singlet cup checks `<5e-9` where applicable.

Additionally compare against two wrong conventions:
1. raw D0 without source sign normalization;
2. forced eta=+1 for every channel.

Calibration PASS requires the correct normalized construction to pass all held-out predicates and at least one frozen channel to detect each wrong convention by residual `>1e-6` against cup or 4-valent/source composition structure. The wrong variants receive no physics interpretation.

## Aggregate

Run A-D independently/concurrently with `fail-fast:false`. Each emits machine-readable evidence. Green CI is not PASS.

Terminal classes:
- `RC006_SOURCE_NORMALIZED_QBAR_SIGN_PASS`
- `RC006_QBAR_SIGN_CONSTRUCTION_FAIL`
- `RC006_QBAR_CUP_INDEPENDENT_FAIL`
- `RC006_QBAR_4VALENT_INDEPENDENT_FAIL`
- `RC006_QBAR_SIGN_HELDOUT_FAIL`
- `RC006_QBAR_SIGN_INFRASTRUCTURE_PARTIAL`

Only full PASS, combined with preserved ITER024 R/braid PASS, authorizes preregistration of executable Eq.(27) component reconstruction. It does not authorize one-step TNR, Eq.(29)/Lambda, alpha selection, bridge credit, candidate theory or new physics.

## Claim locks

Always false during ITER025: `one_step_tnr_authorized`, `iter012_retry_authorized`, `eq29_amplitude_authorized`, `bridge_credit`, `candidate_theory_authorized`, `preferred_alpha_found`, `new_physics_found`.