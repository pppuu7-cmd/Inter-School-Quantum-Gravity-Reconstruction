# ITER011 — RC006 Eq.(27)/Appendix-F numerical authority

Date: 2026-09-13

## Frozen gate
Preregistration commit `1d967344dafcbfbf23e802d3042c7c8b7669b8d0` preceded implementation commit `350a90124b04c8a83e5f0e978e2e8ca33c4c0fb9` and production head `a261237e1a549264917d37cec4adb556462eea6c`.

The gate asked whether arXiv:1609.02429v2 supplies a complete authority chain for the numerical 3-valent EPRL tensor used by the triangular TNR algorithm, while excluding Eq.(29)/Lambda/formLambda6j and fitted conventions.

## Authoritative production
- run `34769981357`
- lane A job `103757677191`, artifact `10321452567`, digest `sha256:cd88e065eac39c4c91dc1b56b5507958b795d5f68e144d6d91f5f041f3f48458`
- lane B job `103757677291`, artifact `10321692002`, digest `sha256:4f69906bc647fe60ad14efd29e669cfb1594ad53d9317cdd8d33ac9c1d860b41`
- lane C job `103757677262`, artifact `10322105524`, digest `sha256:7c1286d54f5daa9a24e16db32b5b39324d98173fb4301797aaa06836deba0b05`
- lane D job `103757677321`, artifact `10321333042`, digest `sha256:e0e4a58f2af4c401fa2769b436216732f6e2dd16738dc50f484f20686c00bfde`
- aggregate job `103757712301`, summary artifact `10322335128`, digest `sha256:440ec9bcec015cd1cb23d0b4cf7a761c80caf2588196e7e46b372d9f49e6dff0`

All four raw lane logs/artifacts and the frozen aggregate were consumed; green CI was not used as the scientific classifier.

## Scientific result
Terminal scientific PASS:
`RC006_EQ27_APPENDIXF_NUMERICAL_AUTHORITY_CHAIN_COMPLETE_SCOPED`.

Lane A confirmed that Eq.(27)'s scalar ingredients are source-defined: admissibility, q-dimensions, EPRL map, explicit phase and intermediate-j sum.

Lane B confirmed source authority for q-CG decomposition/modified normalization, cap/cup and q/qbar duality, orthogonality, Haar structure, 6j recoupling and B15 splitting.

Lane C confirmed that Appendix F derives the 3-valent diagrams from the 4-valent object through source-stated identities without introducing a new free amplitude convention.

Lane D confirmed the independence controls: Eq.(29), Lambda and fitted normalization are absent, while deleting the modified q-CG normalization or swapping q/qbar is detected as non-authoritative.

## Scope guard
This result authorizes only the smallest source-faithful one-step numerical reconstruction with alpha declared prospectively. It gives zero bridge credit by itself. It does not authorize Eq.(29)/Lambda, does not establish a preferred alpha, does not establish a genuine Lorentzian multi-vertex refinement bridge, and does not authorize candidate-theory construction.

Candidate theory remains `0% / UNFORMED`; all constitutional claim locks remain in force.
