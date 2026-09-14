# ITER035 result — indexed simplicity-map source authority

Date: 2026-09-14

Scientific classification: **PASS — `RC006_INDEXED_SIMPLICITY_MAP_SOURCE_AUTHORITY_PASS`**.

This is a source-authority PASS only. It resolves the specific ITER034 blocker by locating explicit source-internal authority for the EPRL simplicity map, indexed-label inheritance, and finite-level representation domain. It does not itself evaluate the Eq.(27) sums, derive the full Eq.(27) amplitude, authorize Eq.(29)/Lambda or one-step TNR, or earn bridge/candidate-theory credit.

## Frozen provenance

- preregistration commit: `865aa1901a54620b0cd296efd338268492caf787`
- implementation commit: `87b4e23b8e9bb915bd8e328464102bb6ccfa7240`
- authoritative production head: `ab1d30ef5446825d87ca07df00ba21129a401fd8`
- authoritative run: `34805066706`

Jobs/artifacts:
- A simplicity-map definition job `103855234468` -> artifact `10333007703`, digest `sha256:6cf5c8e03813de82a10fa930c7d61bcf91d6349d82ae0363bb2fbb6183585763`
- B indexed-label inheritance job `103855234205` -> artifact `10333112005`, digest `sha256:352681adc04b19535b3094cc0ef09779da93a5a83ccf47bda4ff30f88fa7df2e`
- C representation-domain job `103855234413` -> artifact `10332372427`, digest `sha256:8c8803223db6f167960ac5e1cdab01cec671863733d55bbc958044b2aa19bf8c`
- D provenance/null job `103855234346` -> artifact `10332583403`, digest `sha256:99514e1e1fa57beb488399a288a6a38ac3613e52721f2a29f60c180388fb9d2b`
- aggregate job `103855261464` -> artifact `10332861829`, digest `sha256:da69480c7864f0b99185a03622e26d107bfa2af18d2257ed28df869426b842e6`

Exact archive authority remained SHA256 `3e04a41195e0313fd97c68fcb8cc2ec30fa4bdfb5529ba867923c4120fc3e0ee`.

## Scientific readout

Raw artifacts were inspected, not merely the green aggregate.

### A — explicit simplicity map: PASS
The exact source explicitly gives the EPRL map
`(j^+,j^-) := ((1+gamma)/2 l, (1-gamma)/2 l)`
and describes it as a map `V_l -> V_{j^+} tensor V_{j^-}`. The same source discusses the finite-q restriction and requires mapped representations to remain below the quantum-group cutoff. This is direct source authority outside Eq.(29)/Lambda, not a convention fitted to Eq.(27) output.

### B — indexed-label inheritance: PASS
The exact source explicitly states that the simplicity constraints are implemented in the maps `l_i -> (j_i^+,j_i^-)` and then uses `j_1^±`, `j_2^±` as the coupled representation labels. Thus the indexed labels appearing in Eq.(27) are source-declared instances of the same simplicity map rather than merely notation-similar symbols.

### C — finite representation/admissibility domain: PASS
The exact source explicitly states that `SU(2)_k` irreps are labelled by spins up to `j_max=k/2` (for the paper's integer-representation restriction, odd k uses `(k-1)/2`), defines admissible representations, and gives the root-of-unity coupling conditions including `j_1+j_2+j_3 <= k`. It further imposes the mapped-pair condition
`(j^+(j_max),j^-(j_max)) in {(j,j') in (N,N): j,j' <= j_max}`
and lists non-trivial finite-k/gamma cases. This is sufficient source authority to enumerate bounded admissible mapped labels without post-hoc truncation.

### D — provenance/nulls: PASS
Archive hash matches exactly and all 3/3 frozen false authorities are rejected: lexical-only plus/minus occurrence, fabricated `j^+=j^-`, and Eq.(29)/Lambda-only relation.

The aggregate reports all A-D PASS and `RC006_INDEXED_SIMPLICITY_MAP_SOURCE_AUTHORITY_PASS`; raw review confirms those classifications are substantively supported. This differs from the rejected green ITER034 run, whose evidence scope was over-permissive.

## Exact authorization

ITER035 authorizes only a new separately preregistered **bounded EPRL-map label-instantiation/consistency gate**. That successor may mechanically apply source-listed admissible `(k,gamma,l)->(j^+,j^-)` mappings and test their consistency with the two Eq.(27) source exponents and finite-k domains, but it may not choose gamma after viewing numerical results or import Eq.(29)/Lambda.

A numerical Eq.(27) scalar/summation lift remains unauthorized until that label-instantiation gate passes.

Candidate theory remains `UNFORMED / 0%`. Overall roadmap readiness remains 49%. Bridge credit remains zero.