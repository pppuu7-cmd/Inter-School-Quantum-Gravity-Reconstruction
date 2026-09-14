# ITER034 authority-validation repair

Date: 2026-09-14

Run `34804823837` produced a green aggregate labelled `RC006_EQ27_SOURCE_LABEL_DOMAIN_AUTHORITY_PASS`, but **is not accepted as a scientific PASS** after raw-evidence review.

The frozen preregistration requires source-qualified numerical/domain meaning for every Eq.(27) label and explicitly forbids Eq.(29)/Lambda-only authority and mere lexical occurrence. Raw artifacts show the first implementation scanned all `sources/`, `results/`, and `docs/` files and accepted generic cue words. It therefore counted unrelated evidence (including BH003 material) and Eq.(29)-related contexts as positive authority. The code also contained an intended forbidden-document branch whose body was only `pass`, so it did not actually exclude such documents.

Classification of run `34804823837`: **IMPLEMENTATION/VALIDATION FAIL PRE-SCIENCE — AUTHORITY EVIDENCE SCOPE TOO PERMISSIVE**. Green CI is explicitly not scientific PASS.

Run jobs: external `103854517728`, factor1 `103854517736`, factor2 `103854517848`, null `103854517905`, aggregate `103854549888`.
Artifacts: external `10332927566` digest `sha256:7651f19c63d8ff4fb6ae9ee1bc513949d615286338220189d69893d5babfbac4`; factor1 `10332408272` digest `sha256:2bdf64d23e93c1a2e4cd93552bfb4a2a3f9a78692829e446d99974f90c0b8262`; factor2 `10333047133` digest `sha256:5058c7754f01bfd47e84408991828bcfcc1526b0b904b60b4157f07b10ff248b`; null `10332817669` digest `sha256:27c475c0c904251766e8205c4dade774918f0c25b5e1e0e75a60bb763af21829`; aggregate `10332716774` digest `sha256:de542506b2bdb66b58771c423428d37c2af6750aa5238700c2f1691077bdcb69`.

Minimal validation repair commit `a2443d483fa8e981b0482203fead6c18600f26c8` restricts admissible evidence to a fixed allowlist of already validated RC006 source-authority notes and rejects ambiguity/nonidentifiability contexts. It does not change the frozen scientific criterion, source labels, or authorization threshold. Workflow-trigger commit `7ea3e3f8fd894197dee7023742426e347e859954` starts recovery run `34804915740`.

No numerical scalar/summation lift is authorized until that recovery run terminalizes and its raw artifacts are consumed. Eq.(29)/Lambda, one-step TNR, bridge credit and candidate theory remain unauthorized.