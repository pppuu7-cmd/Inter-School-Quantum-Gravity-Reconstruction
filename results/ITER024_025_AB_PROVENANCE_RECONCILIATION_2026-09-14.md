# ITER024/025 A/B provenance reconciliation — RC006

Date: 2026-09-14

Status: `AUTHORITATIVE_LINEAGE_RECONCILED / EQ27_RELOCKED`

## Why this reconciliation is required

Two independent work streams used the labels `ITER024` and `ITER025` for distinct prospectively frozen gates. Historical paths and commits are preserved unchanged; this note introduces logical aliases only. No earlier terminal result is rewritten.

The collision matters scientifically because the later source-authority PASS does not erase an earlier executable-primitive FAIL.

## Logical aliases

### ITER024A — graphical dual/braid executable checkpoint

- prereg commit: `0740c83d7951ba71a2c9797225ca7fcae7fbe739`
- production head: `675098880739810a0e394d59497cc0471bbacdc8`
- authoritative run: `34786045133`
- terminal result commit: `831d566555dc1e21ae84e5b0bd69ddb0e336f690`
- report: `results/ITER024_RC006_GRAPHICAL_DUAL_BRAID_2026-09-14.md`
- classification: `RC006_GRAPHICAL_QBAR_COMPONENT_FAIL`

Scoped facts retained from ITER024A: R crossing/intertwining/inverse PASS; Yang–Baxter and q=1 swap PASS; adversarial calibration PASS. The qbar-dual lane FAIL localized an allowed but unfixed channel-sign convention. Eq.(27) remained unauthorized.

### ITER024B — cited-authority-chain parser gate

- prereg commit: `6d007bf342997425d5eee88d0f354062e9f8bb95`
- implementation commit: `c223a73f0c66c950da98f478cfe4b7d2d3be8ca0`
- production head: `2511ad18bf53d7159b935df306419dad709a210c`
- authoritative run: `34788335930`
- report: `results/ITER024_RC006_CITED_AUTHORITY_CHAIN_INVALID_IMPLEMENTATION_2026-09-14.md`
- scientific classification: `INVALID_IMPLEMENTATION`

Its green CI/raw aggregate is not scientific PASS because the implementation did not actually follow the cited-source chain required by its preregistration.

### ITER025A — source-normalized qbar sign execution

- prereg: `prereg/ITER025_RC006_SOURCE_NORMALIZED_QBAR_SIGN_2026-09-14.md`
- prereg commit: `235438817d2731209e532524fb60a6d2150070db`
- implementation commit: `1dd6d2a316a63a487d49fec6f6a40f86b75223ae`
- production head: `72ef40054d450d6c97213ffa211ffb63a8b524f9`
- authoritative run: `34786242013`
- aggregate job: `103802168903`
- aggregate artifact: `10327015625`
- aggregate digest: `sha256:ff04cbffd2cf45db0c5f8b09f74f4075d54548ad412e048d517d3f9f42c6d40e`
- classification: `RC006_QBAR_CUP_INDEPENDENT_FAIL`

Frozen aggregate lane status:

- construction: PASS
- independent cup: FAIL
- 4-valent: PASS
- held-out: FAIL

The construction algorithm (inverse-parameter qbar highest-weight solver on reversed tensor order, then source B7 sign normalization) was internally strong: max scalarity `6.008377092244052e-13`, max magnitude error `2.494116024820414e-13`, max eta^2 error `2.0197584488487296e-12`, max qbar intertwiner `1.1403325463066974e-12`. The independent 4-valent panel also passed with max residual `1.4519000766079664e-13`.

However the preregistered independent cup panel failed decisively. Examples include:

- k=6, twice-j=6: residual `2.000000000000002`;
- k=10, twice-j=8: `1.2100006674121118`, twice-j=9: `1.438941402844524`;
- k=12, twice-j=9: `1.0669863302706881`, twice-j=10: `1.1948152457885843`.

Held-out cup counterexamples also failed:

- k=7, twice-j=7: `2.0000000000000027`;
- k=9, twice-j=9: `2.0000000000000004`;
- k=11, twice-j=9: `1.2014857516922792`.

Therefore `eq27_component_reconstruction_prereg_allowed=false` after ITER025A. Green workflow status is execution status only.

### ITER025B — exact qbar/R source authority

- prereg commit: `db2e00079e61258e69c1c8d68c587674e921be9e`
- implementation commit: `8294e02f2e0ab9e08f44b124d608efbc44a05072`
- production head: `cdf8142df05b61ea17b116571326e4e2721dbde0`
- authoritative run: `34788769863`
- report: `results/ITER025_RC006_EXACT_QBAR_R_SOURCE_AUTHORITY_2026-09-14.md`
- source record: `sources/ITER025_RC006_QBAR_R_AUTHORITY.md`
- classification: `PASS — RC006_EXACT_QBAR_R_SOURCE_AUTHORITY_COMPLETE`

ITER025B establishes source-level convention authority only. In particular `1312.0905v2` supplies the explicit ordered component identity

`{}_q C^{j1 j2 j3}_{m1 m2 m3} = (-1)^(j1+j2-j3) {}_{bar q} C^{j1 j2 j3}_{-m1,-m2,-m3}`

and the target/cited sources fix the R versus R^-1 crossing assignment.

## Combined scientific interpretation

The two ITER025 results are compatible, not contradictory:

1. exact source authority now fixes the qbar component relation and R crossing convention;
2. the specific ITER025A executable construction by inverse-parameter/reversed-order qbar highest-weight solving does **not** reproduce the independent cup formula over the full frozen root-of-unity panel;
3. therefore source authority does not authorize Eq.(27) until a source-direct executable qbar primitive is separately validated.

The ITER025A failures cluster near high/root-boundary spins but are not automatically dismissed as boundary artifacts: all were prospectively included and marked admissible by the frozen implementation. Whether any require a narrower source-domain interpretation must itself be tested prospectively.

## Authorization correction

Effective immediately:

- `eq27_component_reconstruction_prereg_allowed=false`
- `iter012_retry_authorized=false`
- `eq29_amplitude_authorized=false`
- `bridge_credit=false`
- `candidate_theory_authorized=false`
- `new_physics_found=false`

Candidate theory remains `UNFORMED`.

## Exact next admissible gate

`ITER026_RC006_DIRECT_SOURCE_QBAR_IDENTITY_EXECUTION`.

Prospectively construct qbar components directly from the now-source-qualified q↔qbar identity and the already validated q-CG tensor, preserving the source map order. The gate must include every known ITER025A cup counterexample, held-out levels, a source-domain/root-boundary audit, independent cup and 4-valent checks, qbar algebra/intertwining checks where semantically applicable, and wrong-index/wrong-sign controls. The failed inverse-parameter/reversed-order construction may be retained only as a frozen negative comparator, not as an authority.

Only a full terminal PASS of that new gate may re-authorize preregistration of bounded Eq.(27) component contraction.
