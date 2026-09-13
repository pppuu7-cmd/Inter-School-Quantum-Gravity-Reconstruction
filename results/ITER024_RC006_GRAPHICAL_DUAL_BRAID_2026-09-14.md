# ITER024 — graphical-to-component qbar dual / braiding

Date: 2026-09-14
Production run: `34786045133`
Production head: `675098880739810a0e394d59497cc0471bbacdc8`

## Terminal classification

**`RC006_GRAPHICAL_QBAR_COMPONENT_FAIL`**

This is a scoped FAIL of the preregistered **independently normalized qbar dual sign convention**, not a failure of the tensor ordering, qbar coproduct, R crossing, braid coherence, or the q-CG backend.

Lane outcomes:
- qbar dual: **FAIL**;
- R crossing/intertwining/inverse: **PASS**;
- Yang–Baxter + q=1 swap sentinel: **PASS**;
- adversarial calibration: **PASS**.

No Eq.(27) contraction, TNR, Eq.(29), alpha scan, bridge credit, candidate theory or new-physics claim is authorized.

## 1. qbar dual: failure localizes to a global channel sign

Artifact `iter024-dual`: ID `10326955592`, ZIP SHA256 `d48a08abee952601a0311428bf8c0a13f981659f291d4e478995e126e958c5f2`.

The reversed-tensor-order qbar solver intertwines the qbar coproduct extremely well:

`max_qbar_intertwiner = 9.228190877461913e-14`.

Nearly every frozen q/qbar composition agrees with the Appendix-B scalar identity at ~1e-14 or better. The exceptions are:

- k=12, twice-spins `(8,4,4)` = physical `(4,2)->2`: residual `0.49395920743493416`;
- k=12, twice-spins `(8,4,6)` = physical `(4,2)->3`: residual `0.44504186791262956`;
- cup comparison at k=6, physical `j=3`: residual `2.000000000000002`.

These are not generic component distortions. Numerically,

- `0.49395920743493416 = 2/d_2` at k=12 within numerical precision;
- `0.44504186791262956 = 2/d_3` at k=12 within numerical precision;
- the cup residual 2 is exactly the distance between unit-normalized vectors differing by an overall sign.

Thus the independently normalized qbar highest-weight solver has the correct tensor/intertwiner structure but chooses the opposite allowed normalized sign on those channels. ITER024 preregistration forbade a post-production sign correction table, so the lane correctly remains FAIL.

Scientific localization: the missing primitive is now **coherent source-defined qbar channel-sign gauge**, not qbar index order or qbar representation action.

## 2. R crossing: PASS

Artifact `iter024-R`: ID `10326289008`, ZIP SHA256 `1acdde7ed320740cf904f49913678d717441f623679906d4c91cc0de9fb4b50b`.

Using the prospectively frozen graphical component dictionary

`R_ab = sum_j (-1)^(j1+j2-j) q^[-(C_j1+C_j2-C_j)/2] C_ba^j (C_ab^j)^T`,

the frozen k=6,10,12 panel gave:

- maximum coproduct intertwining residual: `1.950376767871912e-13`;
- maximum forward/inverse composition residual: `5.67368937610391e-13`.

Both are far below the `5e-9` threshold. No channel sign correction table was fitted.

## 3. Braid coherence: PASS

Artifact `iter024-braid`: ID `10325969207`, ZIP SHA256 `483d0717a9ed5eadfb5785fc730741261af4baced99cc8388a8caf6586b13c9e`.

Across the frozen Yang–Baxter panels:

- maximum YB residual: `2.88711357575485e-15`;
- q=1 ordinary-swap sentinel: `1.3322676295501878e-15`.

The orientation sign `(-1)^(j1+j2-j)` is essential: omitting it is independently detected by the calibration lane.

## 4. Adversarial calibration: PASS

Artifact `iter024-null`: ID `10326576795`, ZIP SHA256 `e20efddc6f5566d87f4ae2a65028e814d654f5e3ad67cf08aa50b856eab1861f`.

Correct YB control residual: `2.8177377798042847e-16`.

All 4/4 deliberately wrong variants were detected, with residuals:

`0.21635311151025566`, `0.4797102491250117`, `1.052791354593153`, `0.8677674782351162`.

## 5. Aggregate

Aggregate artifact: ID `10326124606`, ZIP SHA256 `ef5b574771ff6e05812a4553cdff9e994e38b383e411c0ff5ffb103eb0e4a410`.

Frozen aggregate:

`RC006_GRAPHICAL_QBAR_COMPONENT_FAIL`.

`R=true`, `braid=true`, `null=true`, `dual=false`.

## 6. Next admissible gate

Do **not** rerun R or braid. The next prospective test should define the qbar channel sign from the source Appendix-B normalization identity itself rather than from an arbitrary SVD/highest-weight sign.

For a raw reversed-order qbar embedding `D0`, first verify that `F_q D0` is scalar times identity and that the scalar magnitude is `1/d_j`. Then use the exact Appendix-B sign `(-1)^(j1+j2-j)` to choose the unique normalized sign of `D`. This is a source-defined normalization convention, not a fit to a physics amplitude. Independent validation must then use cup agreement, held-out transport and 4-valent source identities; the defining B7 scalar identity itself is construction evidence and must not be double-counted as an independent test.

Locks remain false: `eq27_component_reconstruction_prereg_allowed`, `one_step_tnr_authorized`, `iter012_retry_authorized`, `eq29_amplitude_authorized`, `bridge_credit`, `candidate_theory_authorized`, `new_physics_found`.