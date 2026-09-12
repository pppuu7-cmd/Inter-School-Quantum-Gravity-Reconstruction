# ITER006 — DVD refinement-map source authority: NOT FOUND IN PINNED SOURCE

Date: 2026-09-12

Pinned source: arXiv:1801.03771, source SHA256 `27e781f9ae9b36056a57b7747dc3c58b5b9c944dd0214041149843d8434e16c1`.

Preregistered protocol: `protocol/ITER006_DVD_REFINEMENT_MAP_SOURCE_AUTHORITY_PREREG.json`.

Authoritative inventory run: `34709790323` (commit `5cab51746b6d8cc25a31c1f8b56638ae047f29b5`).

## Frozen rule

`EXPLICIT_REFINEMENT_MAP_CANDIDATE_FOUND` required a source passage containing an explicit mathematical map/operator/relation connecting two discretization levels or boundary/amplitude spaces. Comparisons of diagrams, auxiliary shell cutoffs, sums over labels, or representation-theoretic embeddings at a fixed discretization do not qualify.

## Inventory

The six frozen query classes returned 62 contexts:

- boundary: 32
- coarse/fine: 18
- DVD/two-vertex: 9
- maps (`cylindrical|embedding|injection|projection`): 2
- refinement: 0
- resummation: 1

## Semantic classification of the only two `maps` hits

1. The source calls `⟨W_C|` a **dynamical projection** on a boundary state for a fixed foam `C`. This is an amplitude functional at one chosen two-complex, not a map between coarse and refined boundary discretizations.
2. The source calls the EPRL `Y`-map an **embedding of SU(2) irreps into unitary SL(2,C) irreps**. This is a representation/simplicity map, not a coarse→fine boundary-discretization embedding.

The `coarse/fine` contexts discuss the continuum/coarse-graining problem and explicitly point outward to other references. In particular the source says that viewing spin foams as finite-degree-of-freedom amplitudes to be studied in a continuum limit is an alternative programme and cites external works for results in that direction. The conclusion likewise says higher-valence vertices *could be interesting from a coarse-graining perspective* and cites other work; it does not define the required map itself.

The source separately studies convergence of ordinary finite sums/cutoffs in a minisuperspace calculation. Those cutoffs are not discretization refinement maps under the frozen rule.

## Terminal classification

`SOURCE_REFINEMENT_AUTHORITY_NOT_FOUND`

This result is scoped **only** to the pinned source arXiv:1801.03771. It does not imply that Lorentzian EPRL/spin-foam refinement maps are absent from the literature. It means only that the already validated DVD2/DVD3 shell calculation cannot obtain genuine refinement/bridge credit by reinterpreting its auxiliary shell cutoff.

## Consequence

The next admissible step is a source ladder over explicit cylindrical-consistency/coarse↔fine constructions, with semantic levels kept separate. A positive external source candidate may authorize a later compatibility test; it does not automatically splice that map into the Lorentzian DVD amplitude.

`BRIDGE_DERIVED = false`; candidate theory remains `UNFORMED / 0%`.
