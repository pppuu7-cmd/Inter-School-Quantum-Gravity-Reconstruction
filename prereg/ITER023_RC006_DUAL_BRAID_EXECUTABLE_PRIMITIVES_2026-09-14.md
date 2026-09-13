# ITER023 preregistration — RC006 executable cup/qbar-dual and R-braiding primitives

Date: 2026-09-14

## Authority
Authoritative ITER021 terminal class is `RC006_EQ27_COMPONENT_TRANSLATION_BLOCKED_MISSING_PRIMITIVE`; its two missing primitives are exactly `cup_qbar_dual` and `R_braiding`. ITER022 was not executed and is superseded.

Frozen primary source: arXiv:1609.02429v2, e-print SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

Use the unchanged ITER019/020 q-CG highest-weight backend. No external closed-form q-CG formula, phase fitting, or Hermitian-adjoint substitution is allowed.

## Source-grounded executable definitions

### qbar dual
Appendix B geometrically reverses the tensor order when bending the two outgoing legs. For an admissible ordered channel `(j1,j2)->j3`, construct the inverse-parameter embedding by solving the same representation problem at `qbar=q^-1` on the **reversed tensor order** `(j2,j1)`. Convert the resulting Appendix-A coefficient to Appendix-B `mathcal C` with `1/sqrt(d_j3)` and permute the row index back to the source component order `(m1,m2)` only for component comparison.

Frozen identities:
- q/qbar composition must equal `(-1)^(j1+j2-j3) d_j3^-1 I`;
- for `(j,j)->0`, the qbar dual must equal the source cup divided by `sqrt(d_j)` up to no post-production fitted sign;
- the geometric qbar embedding must intertwine the qbar coproduct on reversed tensor order.

### R/braiding
The source crossing identity is implemented channel-by-channel. With Appendix-A normalized q-CG embeddings `C_ab^j` and `C_ba^j`, the source `d_j mathcalC mathcalC` factor becomes `C_ba^j (C_ab^j)^T`. The graphical dual-orientation sign inherited from the Appendix-B composition is prospectively fixed as `(-1)^(j1+j2-j)`.

Thus the crossing map `V_j1 tensor V_j2 -> V_j2 tensor V_j1` is
`R = sum_j (-1)^(j1+j2-j) q^[-(C_j1+C_j2-C_j)/2] C_ba^j (C_ab^j)^T`,
with the source R-inverse using the opposite exponent.

No row/column sign is adjusted after output.

## Frozen panels
Levels `k=6,10,12`.

Dual channels include every admissible output for ordered input pairs `(1/2,1/2)`, `(1,1/2)`, `(2,1)` when allowed, plus at k=12 `(4,2)` and `(3,3)`.

R panels: `(1/2,1/2)`, `(1,1/2)`, `(2,1)` at every level where all listed labels are admissible, plus `(3,3)` at k=12.

Yang–Baxter panels, kept away from trace-zero pair sectors: `(1/2,1/2,1/2)`, `(1,1/2,1/2)`, `(1,1,1/2)` for k=6,10,12 and `(2,1,1/2)`, `(2,1,1)` for k=10,12.

## Parallel lanes

### A — cup/qbar dual
PASS if across the frozen dual panel:
- max q/qbar composition residual `<2e-9`;
- max qbar-coproduct intertwiner residual `<2e-9`;
- singlet cup comparison for j=1/2,1,2,3 (where admissible) `<2e-9`.

### B — R source identity / inverse / intertwining
PASS if every frozen R panel satisfies:
- `R Delta_ab(Jz,J+,J-) = Delta_ba(Jz,J+,J-) R` max residual `<5e-9`;
- source R-inverse on reversed pair composes to identity max residual `<5e-9`;
- every channel coefficient is exactly the preregistered source phase/sign expression; no fitted correction table exists.

### C — braid coherence
PASS if every frozen Yang–Baxter panel satisfies the braid relation to max residual `<2e-8`.

Also at undeformed q=1, the same construction must approach the ordinary tensor-factor swap on `(1/2,1/2)`, `(1,1/2)`, `(2,1)` to max residual `<2e-10`. This is an implementation sentinel only.

### D — adversarial calibration
On fixed small panels test separately:
1. omit the graphical orientation sign `(-1)^(j1+j2-j)` from R;
2. use a qbar embedding without reversed tensor order;
3. replace qbar dual by ordinary elementwise complex conjugation of the q embedding;
4. flip the source R exponent sign while comparing against the forward-source channel coefficient.

Correct primitives must pass A–C. Calibration PASS requires at least 3/4 wrong variants to violate a relevant frozen identity by `>1e-6`.

## Aggregate
Run A–D as independent GitHub Actions matrix jobs with `fail-fast:false`.

Terminal classes:
- `RC006_DUAL_BRAID_EXECUTABLE_PRIMITIVES_PASS`
- `RC006_QBAR_DUAL_EXECUTABLE_FAIL`
- `RC006_R_BRAIDING_EXECUTABLE_FAIL`
- `RC006_BRAID_COHERENCE_FAIL`
- `RC006_DUAL_BRAID_CALIBRATION_FAIL`
- `RC006_DUAL_BRAID_INFRASTRUCTURE_PARTIAL`

Only full PASS re-authorizes preregistration of executable Eq.(27) component contraction. It does not authorize one-step TNR, Eq.(29)/Lambda, alpha selection, bridge credit, candidate theory or new physics.

## Locks
`iter012_retry_authorized=false`; `one_step_tnr_authorized=false`; `eq29_amplitude_authorized=false`; `bridge_credit=false`; `candidate_theory_authorized=false`; `preferred_alpha_found=false`; `new_physics_found=false`.