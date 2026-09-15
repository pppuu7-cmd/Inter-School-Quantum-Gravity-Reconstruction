# ITER136 — terminal result

Classification: **PASS_DIAGNOSTIC_SCALARIZED_COMPLETION_FULL_TENSOR_AUTHORITY_OPEN**.

Prereg `eabd349cda5a0d323b537d8e3380de9aa43051d3`; production head `6640caf740a0c6d5f738b161056032c811b11b96`; run `34944054243`.

Consumed raw logs:
- job `104299166214`: scalarized first-order line response produced `xi1=A L^2(-t exp(iw)+t+exp(i t w)-1)/w^2`, with exact endpoints, differential equation and Green reversal PASS; artifact `10386158943`, sha256 `0225c2284b4f7de87d0baf6e517eef5fa16810f192e081ecb60979e19d6c4433`.
- job `104299166371`: abstract direct expansion gives exactly `G2+x dG1+2 G1 xp`; three frozen integer bookkeeping panels PASS; artifact `10386338161`, sha256 `463be948c750943ff1fe680707146ad76cacd84ff09bacce107b6b5001c9fb37`.

These are useful exact diagnostics but do **not** satisfy frozen task D as written: the held-outs are not explicit 4D momenta plus symmetric polarization tensors, and task A did not explicitly construct the full Gamma1 tensor. Therefore no full ITER135/136 scientific PASS is awarded. No chi2 credit. Next gate must supply explicit 4D tensor/polarization authority without changing the frozen geometry or source census.