# ITER058 — Lorentzian refinement-transfer second-hop authority

Date: 2026-09-14

## Terminal classification

**SCOPED BLOCKED — `LORENTZIAN_REFINEMENT_TRANSFER_SECOND_HOP_BLOCKED`**

This is not a scientific FAIL of Lorentzian EPRL. The second-hop sources contain real coarse-graining machinery, but no exact source theorem transfers it to the relevant Lorentzian simplicial EPRL 5→1 object.

## Frozen provenance

Prereg commit `4da059da6b8639158d4f298869e968c75c577b5f`.

Implementation commit `e6c41bad1c2a0e46d4d58c94b251bba1ec1af47c`.

Production head `731201da41118368f65b21891142d24bd3e192eb`.

Authoritative run **`34823516850`**.

Jobs/artifacts:

- citation-provenance-1903: job `103910245976`, artifact `10339028584`, digest `sha256:d70bf835ea8af5fbc534f7a081758cf8ee2abde3cc88bb9c40a799f573f95bbc`
- hypercuboidal-1701: job `103910246241`, artifact `10338973724`, digest `sha256:fddf9e13f29affce3e0103b515affda0e7192a4119760d2fcecde77f2f2a05b4`
- dtnr-1409: job `103910246332`, artifact `10338553866`, digest `sha256:380aaf347b2404d1cd87e72c47f3675d27b229be3ee96943779ef5585c58294e`
- null-controls: job `103910246400`, artifact `10338933813`, digest `sha256:99a9efa5748da9a5109e887111752c973353ddde15af97e5c6280889e330f649`
- aggregate: job `103910287288`, artifact `10338824044`, digest `sha256:9b9cd4534d9a6361ee331902cbd58abd7883836236c8d4a7b9dadeb8c4022025`

All source lanes were retrieved and raw contexts manually classified. Green CI was not used as authority PASS.

## Findings

### arXiv:1903.12624 citation provenance

The Lorentzian EPRL numerical source explicitly says that extended triangulations may require simplification schemes and cites:

- Bahr & Steinhaus, hypercuboidal renormalization, as a minisuperspace/Euclidean-EPRL example;
- Dittrich, Mizera & Steinhaus, decorated tensor-network renormalization, as a many-vertex/intertwiner-renormalization direction.

The source language is contextual/future-facing, not an exact transfer theorem for its Lorentzian EPRL vertex amplitude.

### arXiv:1701.02311 hypercuboidal renormalization

This source contains a genuine fine/coarse construction. In particular it explicitly defines an embedding map

`iota_{Gamma Gamma'} psi_J^(Gamma') = (1/N_J) sum_{j_e} prod_E delta(J_E - sum_{e subset E} j_e) psi_j^(Gamma)`

for quantum cuboids, with normalization specified elsewhere in the source. This is strong coarse-graining/refinement authority **for that model**.

However, the same source states that it studies a drastically restricted version of the full 4D theory: the EPRL-FK model on a **hypercubic two-complex / quantum-cuboid sector**. Its discussion also distinguishes features specific to the Euclidean signature model from Lorentzian signature. The embedding map is therefore not an authority-level map for the Lorentzian simplicial 5→1 EPRL object used in ITER054–055.

### arXiv:1409.2407 decorated tensor-network renormalization

This source provides a concrete decorated-TNR coarse-graining framework for lattice gauge theories and related spin-foam models. It explicitly notes that full 4D spin-foam models with Euclidean-signature structure are technically easier, whereas Lorentzian models based on noncompact Lorentz groups present additional challenges. The worked coarse-graining constructions are not an exact Lorentzian EPRL 5→1 transfer theorem.

## Frozen null controls

Passed: generic TNR applicability, Euclidean/hypercuboidal truncation, “can be adapted” language, shared boundary space alone, and fitted maps do not qualify.

## Scientific interpretation

ITER058 establishes an important distinction:

1. explicit refinement/coarse-graining maps do exist in nearby spin-foam realizations;
2. the source-qualified Lorentzian EPRL 5→1 amplitude also exists and has bounded fixed-summand transport evidence;
3. **the missing bridge object is the exact model-matched map/transfer theorem between those two facts**.

Therefore no coarse↔fine numerical comparison is authorized by substituting the hypercuboidal embedding map or decorated-TNR blocking into the simplicial Lorentzian EPRL amplitude.

Locks remain `refinement_map_derived=false`, `bridge_credit=false`, candidate theory `UNFORMED / 0%`.