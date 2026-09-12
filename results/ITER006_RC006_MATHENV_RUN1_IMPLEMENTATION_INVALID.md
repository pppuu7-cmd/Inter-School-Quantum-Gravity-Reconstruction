# ITERATION 006 — RC006 named-anchor MathEnv run 1 invalid measurement

Date: 2026-09-12

## Provenance

Prospective script commit: `d7ae3b16855aa91f28766ba778c22e51f7414bd5`  
Workflow/head: `e4f833606c1a1911dd497f4173a8d689693efb59`  
Run: `34699899382`  
Aggregate job: `103569713709`  
Aggregate artifact: `10299916895`, digest `sha256:bf367358ed0ed38131d058b8fe5c0a042e347e231359356e93469d40452ba6e3`

The aggregate reported `9/9 PASS`, but raw lane logs invalidate that scientific classification.

## First causal failure

For source labels not inside a narrower explicit environment, the extractor selected the enclosing `document` environment. Example: `app:EPRL-diagram`, job `103569689677`, artifact `10300046597`, reported:

- `environment = document`;
- `context_char_count = 211945`;
- `ordered_symbol_token_count = 124373`;
- the context began at `\\begin{document}` rather than at the named source anchor.

In addition, the token regex accepted ordinary alphabetic prose characters, so the `symbol_incidence` lane's nominal shared-token count was contaminated by non-mathematical text.

## Classification

`INFRASTRUCTURE/IMPLEMENTATION_MEASUREMENT_INVALID — GREEN_CI_NOT_SCIENTIFIC_PASS`.

The frozen scientific criteria and interpretation rule are unchanged. The minimal repair excludes the `document` environment, uses a bounded local source block when no narrower environment encloses the label, and tokenizes only explicit TeX math/diagram fragments. No threshold is weakened and no physics model is changed.

Fix commit: `508764118d551fb1e85a1eee6730d52e7e732db6`. Corrected rerun: `34699987643`.

## Claim locks

Run `34699899382` provides no scientific bridge credit and cannot authorize a unique Eq.(29) contraction or numerical amplitude.
