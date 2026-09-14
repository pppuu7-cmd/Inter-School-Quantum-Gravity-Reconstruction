# ITER041 — RC006 root-unity primitive-domain source audit

Date: 2026-09-14

## Terminal classification

**SCOPED BLOCKED — `RC006_ROOT_UNITY_PRIMITIVE_DOMAIN_SOURCE_AUTHORITY_BLOCKED`**.

This is a source-authority result. ITER039 remains terminal SCIENTIFIC FAIL. No numerical threshold, tuple domain, phase, normalization, orientation, or model was changed after observing ITER039/040.

## Provenance

- preregistration: `4884e9b784506db0c428decc808eaac2ffdb9831`
- implementation: `a02700b58dafcc92e6b5d3fea3039dc3ae312020`
- production/workflow head: `5464d07efb957dbc5476fd99baa2c4baae1b465b`
- authoritative source-evidence run: `34806469113`
- jobs: C `103859206862`; D-original `103859206973`; A `103859206982`; B `103859207036`; aggregate `103859245378`
- artifacts:
  - A `10333475564`, `sha256:1e73b88457abaab5c1df692bf0cc95c5bf5e0233fc41beac386d256dac95e882`
  - B `10333480570`, `sha256:1d5cc53cbdc24fce1f52788af065b9765ff320780c8df1c21fb83207503f5139`
  - C `10333400754`, `sha256:5b40763bafc11eb13be49f5d18dd1d328c365554424acaff91e55b75dd0b5d81`
  - D-original `10332708547`, `sha256:0f6e55e072e5d2be4181e27d791bec648f4a238ebfd1e9388bbbacfc710378b0`
  - aggregate `10333330998`, `sha256:29b3757059c4e1770b6671e2b47f99e42b4c263e42bfb9c201050db910ca4468`

The original D positive qbar control missed only because its regex required a non-source TeX spelling. Minimal control-parser repair commit `262c0e0d52b81e747447c409ff72bdf7e2547152` changed no source panel or scientific predicate. D-only recovery workflow head `61616aff25f3a0d5a25e01058bfc789d7d633300`, run/job `34806601065 / 103859578836`, artifact `10332758669`, digest `sha256:35d4f50756466af20c3e43672b5b9e3faa93de1fada5b313df02d30c240f49bd`, recovered 4 R positive hits, 7 qbar positive hits, synthetic negative absent, and is PASS.

## A — exact provenance PASS

All three preregistered archives reproduce their frozen hashes exactly:

- `1609.02429v2`: `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`;
- `1312.0905v2`: `69334656117892b255ebb9b0c3855b6387bafc630bb9345b084e5434e22294c0`;
- `1311.1798v1`: `d6804794d3f4589f77a2e11d2a143c1125a900160e0c632ed3b3e471598af3f7`.

## B — root-of-unity R domain: SOURCE AUTHORITY PASS (scoped)

The frozen q-spinnet/target source set explicitly distinguishes the naive tensor product from the physical root-of-unity object. It states that representations above `k/2` have quantum trace zero; `V_j1 tensor V_j2` decomposes into irreducibles plus a trace-zero part **which is modded out**; the root-of-unity coupling condition includes `j1+j2+j3 <= k`; and the completeness relation is not the full tensor-space identity but a projector `Pi^{j1 j2}` that **projects out the trace-zero part**.

This is sufficient for the narrow ITER041-B question: the prior executable full-space `R^-1 R = I` check used in ITER039 is not source-authorized as a universal full-naive-tensor-product identity across the `a+b>k` boundary. The source category includes a quotient/projection by trace-zero sectors. This conclusion is source-driven and was not selected from the numerical residuals.

It does **not** yet provide an executable projected R matrix for the failed tuples; therefore it authorizes source-level correction work only, not a numerical retry.

## C — dual/cap/cup expanded-domain authority: BLOCKED

The same source set gives explicit cap/cup formulas for admissible representations and requires cup-cap concatenation to give the identity. It also defines qbar CG coefficients by bending legs with cups/caps and gives a dual intertwiner construction.

However, the exact stronger identity used in ITER039's expanded central closure — the executable `F @ D = sign / d_j * I` normalization across every newly introduced `(J+,J-,l)` channel — is not source-qualified in the frozen panel with enough channel/quotient/quantum-trace scope to decide the non-root failures found by ITER040. The source explicitly warns that at root of unity some equations hold only modulo trace-zero parts and supplies projected completeness, while the broad ITER039 dual predicate was applied as an ordinary matrix identity.

Because ITER040 also found dual failures for channels with `a+b <= k`, the root-tensor-boundary projector alone cannot be used post hoc to explain or remove them. The frozen source panel does not contain enough explicit authority to derive an executable corrected expanded-domain dual identity without importing additional source material or making an inference not frozen in advance.

Therefore lane C is **BLOCKED_SOURCE_AUTHORITY**.

## Aggregate

A PASS, B PASS scoped, C BLOCKED, D PASS after parser-only control recovery -> terminal **`RC006_ROOT_UNITY_PRIMITIVE_DOMAIN_SOURCE_AUTHORITY_BLOCKED`**.

No numerical retry of ITER039 is authorized. The exact next admissible gate is prospective source expansion targeted at the cited delegated authorities for root-of-unity quotient/projector and q-CG duality/normalization (the source itself delegates some of these facts to the Biedenharn-Lohe / `yellowbook` references). Any source expansion must be preregistered before using it to define an executable correction.

## Claims/readiness

Overall programme readiness remains **49%**. Candidate theory remains **0% / UNFORMED**. Bridge credit remains zero. Eq.(29), Lambda, full Eq.(27), one-step TNR and candidate-theory construction remain unauthorized.
