# ITERATION 006 — RC-006 Eq.(29) pre-amplitude prerequisites

Date: 2026-09-12  
Status: **SOURCE/STRUCTURE PREREQUISITES PASS; FULL Eq.(29) AMPLITUDE STILL BLOCKED ON ORIENTED/BRAIDED GRAPH MAPPING**  
Candidate theory: `UNFORMED`

## 1. Appendix-B13 source-to-kernel bridge

Authoritative run: `34694997395`  
Aggregate job: `103556894034`  
Aggregate artifact: `10298094519`  
Artifact SHA256: `ecb16a4dac552d6427aacda7f66048da4bb674e47628e5dd0cf42005e03629b1`

Frozen per-case gate: `absolute_error <= 1e-11 OR relative_error <= 1e-11`.

Result: PASS at k=6,10,12, with `8009/8009` admissible integer-sector cases satisfying the frozen gate. This authorizes the pinned normalized `sixjr()` object only where the source graph has explicitly been reduced through Appendix-B B13/B16 identities.

## 2. Eq.(29) source-explicit channel topology

Implementation/workflow commit: `82dcf7ae62929e004ee2af348c1e97632746f337`  
Run: `34695720379`  
Job: `103558741023`  
Artifact: `10299100320`  
Artifact SHA256: `af7a1424bbe4aa3bf41f5914696e7873a5ecda6a88ce3eee3780d316b33a7a28`

At k=12, gamma=1/3, the source-listed integer simplicity image is

`l = 0,3,6 -> (j+,j-) = (0,0),(2,1),(4,2)`.

The source-explicit coupling rules generate:

- 11 admissible source boundary triples `(l1,l2,l)`;
- 46 admissible coarse `(J+,J-)` pairs;
- 35 of the 46 pairs are outside the original simplicity image (`0.7608695652`);
- every source simplicity target remains represented;
- every required crossing has at least one admissible internal R-channel.

Frozen structural gate: PASS.

This is direct finite-support evidence that the source coupling architecture has a substantially larger coarse envelope than the original simplicity image, while preserving the source target. It remains a topology/support result, not an amplitude result.

## 3. Appendix-C first-step feasibility

Run: `34695720384`  
Job: `103558741014`  
Artifact: `10298825789`  
Artifact SHA256: `dca0e3d52d386b920c7fa3f19518ad5a08008dba8785190c9ff6fbb3589bed51`

For the minimal k=12, gamma=1/3 EPRL-intertwiner sector:

- 31 coarse blocks;
- 26 non-simple blocks;
- maximum initial fine-pair dimension per block = 6;
- sum of naive square matrix-element upper bounds = 235;
- naive dense complex128 memory upper bound = 3760 bytes.

Frozen feasibility gate `<512 MiB`: PASS by a wide margin.

Therefore the first Appendix-C block/SVD step is computationally feasible once a source-faithful Eq.(29) amplitude exists. This is not permission to manufacture missing amplitudes.

## 4. Explicit Eq.(26) R-matrix factor

Implementation commit: `d55d6636ac3df3e16a3509504b98f24f701346dd`  
Workflow commit: `d63da2a44ec9f955a0517e506f5b5fba87769d14`  
Run: `34695809537`  
Aggregate job: `103558996929`  
Aggregate artifact: `10298790946`  
Artifact SHA256: `2c34bf5f9f4d2e03fa1d0af0224f227d11f39899c5d413c4e8baad3a46861d80`

Across all 11 source boundary triples:

- 27 explicit internal R-channels were evaluated;
- all 27 coefficients are nonzero;
- minimum coefficient modulus = `0.9999999999999987`.

Classification: **PARTIAL AMPLITUDE-FACTOR PASS**. The explicit braiding factor does not itself delete an admissible channel. The remaining q-spin-network graph can still vanish or cancel, so this is not a full Eq.(29) amplitude.

## Current blocker

The remaining prerequisite is an exact source mapping of the oriented/braided Eq.(29) graphical factor. The paper's Appendix F derives the relevant EPRL diagrams using the recoupling identities together with the R-matrix. We will not guess a product of `sixjr()` factors from the rendered diagram.

An official-arXiv-source metadata discovery workflow was launched as run `34695891870` to identify the TeX/graphic representation and exact source asset provenance before writing the contraction.

## Claim lock

These results do **not** establish:

- a numerical Eq.(29) EPRL tensor;
- Appendix-C singular spectra or RG flow;
- a genuine spin-foam refinement map;
- BH-004B amplitude/refinement universality;
- `BRIDGE_DERIVED`, a continuum limit, or new physics.

The exact next scientific gate is:

`RC006_EQ29_ORIENTED_BRAIDED_GRAPH_MAPPING_GATE -> RC006_EQ29_MINIMAL_K12_AMPLITUDE_GATE -> APPENDIX_C_C1_C2_SVD_GATE -> HELDOUT_NONRETUNED_SELECTOR_TRANSPORT_GATE`.
