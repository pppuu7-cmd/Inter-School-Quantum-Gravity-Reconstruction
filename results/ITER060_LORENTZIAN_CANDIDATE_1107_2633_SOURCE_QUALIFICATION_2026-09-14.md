# ITER060 result — arXiv:1107.2633 source qualification

Date: 2026-09-14

Classification: **SCOPED BLOCKED — SCOPED_BLOCKED_NO_EXPLICIT_REFINEMENT_MAP**

## Provenance
- preregistration commit: `97c7c2747c08717068dbecbf492347324a833881`
- implementation commit: `63912df8c7bc9635fd3737218ac5ea237dd7f3fb`
- production/workflow head: `de686bf46e9c78eb2c70fcb57d09a589ae218f6a`
- authoritative run: `34835559911`
- exact-source job: `103948451061`, artifact `10343789193`, digest `sha256:e2ecc34c84456e4319c34765d2ae5e792b2e63202044bd79264b84006a14c629`
- refinement-language job: `103948451105`, artifact `10343724359`, digest `sha256:4f27b5ce3a94d67aa2889da514030dcbbfe6068655d7ef238e953216f89809f2`
- object-match job: `103948451023`, artifact `10343802580`, digest `sha256:29a9e5d5199a0d24cd79ee4c2dc8e8a4d3112bec9c8ebe8dc3ba748df215c890`
- null-controls job: `103948450815`, artifact `10344220494`, digest `sha256:a216ec7bc622fcdb7870f8843906000295dcf4552c6f775fea36861553045592`
- aggregate job: `103948497310`, artifact `10344285407`, digest `sha256:e5b88e4fc9b0bdab73c0fa4a371acd800be5ac18f1b88b0a5887275193ff3244`
- exact source SHA256: `d46522e8f605202fb0bd1be7b13d4fe197133521597507a11d3bba2ecc64c564`

## Scientific result
The exact source is genuinely Lorentzian EPRL/FK/KKL and compares amplitudes on multiple boundary graphs, including a many-link dipole and the complete five-node / 4-simplex boundary graph. The source also states that the resulting amplitudes have the same support in the large-j limit.

However, the frozen qualification gate fails because the paper does **not** provide a distinct coarse and fine pair connected by an explicit refinement/embedding/coarse-graining map applicable to the active Lorentzian simplicial multi-vertex refinement problem. The source explicitly limits the discussion to boundary graphs and states that bulk two-complex refinement is not addressed. The object-match lane therefore returned `distinct_coarse_fine=false`, `explicit_refinement_map=false`, `homogeneous_isotropic_truncation=true`, and `qualifies=false`.

This is a scoped authority blocker, not a failure of Lorentzian EPRL itself. Common large-j support, common Friedmann behavior, graph-size comparison, and metadata-level map language remain forbidden substitutes for an explicit refinement map.

## Locks and readiness
- `refinement_map_derived=false`
- `bridge_credit=false`
- overall programme readiness remains 49%
- candidate theory remains `0 / UNFORMED`
- no `BRIDGE_DERIVED`, `NEW_PHYSICS_FOUND`, `NEW_QG_THEORY_REQUIRED`, or `ALL_KNOWN_SCHOOLS_FAIL` claim is authorized

## Next admissible action
Preserve this negative source-authority result. Continue only independent ITER059 discovery lanes and/or another independent PHASE_1 amplitude/refinement branch. Do not launch a coarse↔fine numerical comparison from arXiv:1107.2633.
