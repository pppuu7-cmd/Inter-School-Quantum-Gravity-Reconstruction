# ITER037 result — diagonal external-label source support

Date: 2026-09-14

Scientific classification: **PASS — `RC006_DIAGONAL_EXTERNAL_LABEL_SOURCE_SUPPORT_PASS`**.

This PASS is scoped to source-authorized diagonal external labels and their bounded internal-j support. It does not alter the frozen ITER036 result, does not yet evaluate the complete Eq.(27) sums, and does not authorize Eq.(29)/Lambda, one-step TNR, bridge credit, or candidate-theory construction.

## Frozen provenance

- preregistration commit: `8b9a3b7d97afcf5fafb1cd6ece8d300b43652619`
- implementation commit: `0a9c787c1d95937f9052c0a0b36b8b3f4ddaca3e`
- production/workflow head: `bbad8c8acfcee52b856c5a977f2caf64a31770d4`
- authoritative run: `34805544176`

Jobs/artifacts:
- B diagonal admissibility job `103856600497` -> artifact `10332369404`, digest `sha256:7f50b529718c9ba176dfe047449cacee5451abe4663a0ce9aab68caf65abbd2c`
- D null controls job `103856600592` -> artifact `10333063169`, digest `sha256:5d5bab5736d9c913c0c5dd8b1e2da0cd9af4592eb040f09b857d9e52d481da84`
- C diagonal internal-j support job `103856600613` -> artifact `10332983484`, digest `sha256:7d37c41d9dc7da8df861d6943eecd67500738da457132d323c3e4385d7cf43f3`
- A external-label scope authority job `103856600629` -> artifact `10332868664`, digest `sha256:d7f5adb14f7c6d7aa25fe8d66a384641464a12054ab3dbaef360d8412bdde75e`
- aggregate job `103856639970` -> artifact `10332862398`, digest `sha256:21e67d0ca092e5ddf63f9bb770fb80aafa5378b3c239d786f439a490a91cb9af`

## Scientific readout

Raw lane evidence was consumed in addition to the green aggregate.

### A — external-label scope authority: PASS
The exact byte-pinned source positively states that the normalization depends on the `SU(2)_k` representations `l_i`, discusses a generic non-trivial map `l_i -> (j^+,j^-)`, and explicitly states that the simplicity constraints are implemented in the indexed maps `l_i -> (j_i^+,j_i^-)`. Eq.(27) and the surrounding EPRL diagrams separately carry `l_1,l_2`. This is positive indexed-domain authority; the diagonal interpretation is not based merely on absence of an `l_1 != l_2` restriction.

### B — diagonal admissibility: PASS
Exactly the source-listed nonzero mapped labels were tested diagonally, with no new gamma or l introduced. The prospectively frozen diagonal split is:
- primary: `(k=6,gamma=1/3,l_1=l_2=3)`;
- held-out: `(k=10,gamma=3/5,l_1=l_2=5)`;
- primary: `(k=12,gamma=1/3,l_1=l_2=3)`;
- held-out: `(k=12,gamma=1/3,l_1=l_2=6)`.
All four satisfy the source EPRL map, integer-representation restriction and finite-level cutoff exactly.

### C — diagonal internal-j support: PASS
All four diagonal cases have finite non-empty common internal-j support under the source coupling rules, with exactly 2 primary and 2 held-out tested cases:
- `k=6, gamma=1/3, l=3`: internal `j={1,2,3}`, both source exponents `{-3,-1,2}`;
- `k=10, gamma=3/5, l=5`: internal `j={3,4,5}`, both source exponents `{-5,-1,4}`;
- `k=12, gamma=1/3, l=3`: internal `j={1,2,3}`, both source exponents `{-3,-1,2}`;
- `k=12, gamma=1/3, l=6`: internal `j={2,3,4,5,6}`, both source exponents `{-10,-7,-3,2,8}`.
No result-dependent panel repair or held-out retuning occurred.

### D — frozen null controls: PASS
All 3/3 preregistered wrong constructions are detected: an unmapped non-integral external label, a label above the finite-level cutoff, and a swapped plus/minus EPRL pair at positive gamma.

Aggregate classification is `RC006_DIAGONAL_EXTERNAL_LABEL_SOURCE_SUPPORT_PASS`, with no blocked, failed or infrastructure lanes and all claim locks preserved.

## Exact authorization

ITER037 authorizes only a new separately preregistered **central-coupling/domain authority gate** before a full label-complete panel or numerical Eq.(27) sum is attempted. The remaining source object is the central coupling: the exact source states that `j_1^+,j_2^+` and `j_1^-,j_2^-` couple to `J^+,J^-`, which are then coupled to central `l`; it also notes that simplicity constraints are not explicitly imposed on that latter coupling. The admissible finite-k domains of `J^+`, `J^-` and central `l` must therefore be frozen source-faithfully rather than filled by an EPRL-map assumption.

ITER036 remains historically BLOCKED under its own frozen split and is not retrofitted by this PASS.

Candidate theory remains `UNFORMED / 0%`. Overall roadmap readiness remains 49%; bridge credit remains zero.