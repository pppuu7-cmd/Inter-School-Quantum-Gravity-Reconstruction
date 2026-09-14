# ITER040 — RC006 central-component validity-boundary diagnostic

Date: 2026-09-14

## Terminal classification

**DIAGNOSTIC COMPLETE — `RC006_CENTRAL_COMPONENT_VALIDITY_BOUNDARY_DIAGNOSTIC_COMPLETE`**.

ITER039 remains terminal **SCIENTIFIC FAIL** under its frozen gate. ITER040 does not change a threshold, remove a tuple, fit a convention, or reinterpret ITER039 as PASS.

## Provenance

- preregistration: `7fe47cd180c9e2869d8aaaf445ad676a1bb53396`
- implementation: `4a69b1ae7e8c7685bac88e2145e04ef5ce6a4d54`
- first workflow head: `334d02e7621af4fd896a64d3d9a49a242af6ace5`
- first run `34806258751`: **INFRASTRUCTURE FAIL PRE-SCIENCE**, no jobs instantiated because of workflow YAML wiring
- YAML-only repair: `cf9bf1c442c6059ab2244e892ef563800b2499b5`
- authoritative recovery run: `34806282247`
- jobs: C `103858683855`; D `103858683992`; B `103858683995`; A `103858684049`; aggregate `103858835458`
- artifacts:
  - A `10332198958`, `sha256:816ced337c3b4d225dfebc727f68014b112fef24806fad78ae4df8fb0ccac4f3`
  - B `10333315781`, `sha256:43690ac5f11a5fe1656bfaacb943493b88989c6d3826c3b7ca62fda8f36d62aa`
  - C `10333246069`, `sha256:2570c91b6df15c5bae144782e68f733b0ea13b05f49c51a0cb662fefc2265079`
  - D `10333153468`, `sha256:7edb8e4a11412c479e4c4124a0507580f8c4fac0f16acc286150903acb297a4c`
  - aggregate `10333440520`, `sha256:1e81dc44316e0f7d735eaa95ef4a2ece4cf06f920b24c88260f95423965f0bb1`

## Frozen diagnostic results

### Scope census

150 central tuples total: 54 primary and 96 held-out. Exactly 24 tuples lie in the exact ordered ITER027 pair scope `(1,1),(2,1),(2,2),(4,2)`. Eighteen tuples lie at the preregistered root-tensor boundary `a+b>k`.

### Prior validated pair scope

The strongest clean result is negative/diagnostic rather than bridge-positive: **all 24/24 exact prior-scope tuples pass**. There are 12 primary and 12 held-out prior-scope tuples, and both groups have zero failures. Their maximum residuals remain tiny: primary `max R^-1 residual = 7.224267142543843e-15`, `max dual = 4.965068306494546e-16`; held-out `max R^-1 residual = 3.3601445959922215e-15`, `max dual = 4.965068306494546e-16`.

Thus ITER039 did not invalidate the earlier bounded-component validation inside its exact preregistered pair scope. It demonstrated a failure of extrapolating those primitives unchanged across the larger central-coupling domain authorized later by ITER038.

### Root-tensor boundary

Primary out-of-prior-scope/root-boundary group: `3/3` fail, with `max R/R^-1 residual = 16.485281374238554` while `max dual = 3.0545887418016495e-15`.

Held-out out-of-prior-scope/root-boundary group: `15/15` fail, with `max R/R^-1 residual = 2349.9680224303156` and `max dual = 0.4939592074349445`.

The prospectively selected orientation reproduction tuple `(k=6,J+=2,J-=2,l=0)` has `R/R^-1 residual = 16.48528137423864` and essentially zero dual/qbar residual. Swapping the ordered pair does not remove this residual. Therefore the R failure at this boundary is not explained by a simple `(a,b)` orientation swap.

### Non-root failures outside prior scope

Root-boundary structure is **not sufficient** to explain all failures. Outside the exact prior pair scope but with `a+b<=k`:

- primary: 39 tuples, 4 fail; `max R/R^-1 = 3.3932659338529537e-13` but `max dual = 0.7137917357844189`;
- held-out: 69 tuples, 8 fail; `max R/R^-1 = 5.335659810334467e-13` but `max dual = 0.7137917357844189`.

So the expanded-domain failure separates into at least two diagnostic mechanisms: a strong R/R^-1 breakdown concentrated at `a+b>k`, and a distinct dual-contraction breakdown for some out-of-prior-scope channels that are not at that root boundary.

## Consequence

The next admissible step is **not** to rerun ITER039 with a narrower fitted domain. It is a prospectively preregistered source-authority audit asking:

1. what is the correct categorical/quotient-domain meaning of R and R^-1 at root of unity when the naive tensor-product highest channel exceeds the finite physical cutoff; and
2. over what exact representation/channel domain the source-qualified dual/cap/cup contraction identity used earlier is stated, including any quantum-trace, negligible-morphism, quotient, or normalization qualifications.

Only a source-backed authority result can authorize a new numerical formulation. ITER039 remains FAIL permanently.

## Claims/readiness

Overall programme readiness remains **49%**. Candidate theory remains **0% / UNFORMED**. Bridge credit remains zero. No full Eq.(27), Eq.(29), Lambda or one-step TNR claim is authorized.
