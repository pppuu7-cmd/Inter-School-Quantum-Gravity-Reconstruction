# Preregistration — ITER048 Lorentzian Eq.(11) routing/reference authority

Date frozen: 2026-09-14

## Inherited state

ITER047 is terminal SCIENTIFIC PASS — `LORENTZIAN_5TO1_ASSEMBLY_AUTHORITY_PASS` (run `34808646324`, result commit `d477c5514e4c6156ce96187cbe75f27c40cb2b6d`). It authorizes a separately preregistered bounded fixed-cutoff multi-vertex contraction, but only after source-faithful routing is executable without OCR/convention inference.

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `0 / UNFORMED`.

## Motivation frozen before results

The preserved PDF extraction around Eq.(11) is sufficient for assembly classes but is not a safe executable transcription authority: OCR may confuse intertwiner indices such as `i8/i9`. The paper also states that its calculation scripts/notebooks are public at cited repository [30]. We therefore qualify the exact TeX equation and cited implementation before any five-vertex numerical contraction.

No numerical amplitude agreement may be used to choose between ambiguous source indices.

## Frozen source panel

1. arXiv `2302.00072` e-print source, preferably TeX source from `https://export.arxiv.org/e-print/2302.00072` or the equivalent arXiv source endpoint.
2. The bibliography entry explicitly cited as repository `[30]` in that frozen arXiv source. Only the URL/identifier actually present in the source may be followed; no substitute repository discovered after seeing results.
3. Exact backend `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.
4. Independent exact SU(2) Wigner-6j evaluation for the preregistered bounded test sectors below.

## Frozen bounded sectors for later contraction

These are frozen now solely for source-independent algebra/admissibility checks; ITER048 does **not** yet multiply the five Lorentzian vertex amplitudes.

- boundary: `jb=1/2`; `gamma=1.2`; backend shell `Dl=0` for the later first contraction;
- primary: `j1..j10=1/2`, `ib=0`, `i1..i15=0`;
- held-out: `j1..j10=1/2`, `ib=1`, `i1..i15=(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0)` in index order `i1...i15`.

No sector may be changed after outputs are observed. A zero exact 6j/product is not itself failure; finiteness/admissibility and source-faithful evaluation are the predicates.

## Independent lanes (`fail-fast:false`)

1. `tex-eq11`: fetch the frozen arXiv source; preserve file hashes; mechanically extract Eq.(11), Eq.(12), and enough adjacent TeX to identify every `j1...j10`, `i1...i15`, the five vertex argument lists, all five 6j factors, phase, face/intertwiner weights and summation bounds/classes.
2. `cited-reference`: from the same frozen source, resolve bibliography item `[30]`; preserve its literal URL/identifier; if it is a public repository, inventory files relevant to vertex renormalization/Monte Carlo and record commit/default-branch provenance. Do not substitute another repository.
3. `backend-api`: pin backend SHA and mechanically verify its vertex interface has ten face-spin and five intertwiner slots; compare only the arity/order class with the TeX vertex argument lists. No amplitude-based routing inference.
4. `algebra-null`: evaluate exact SU(2) triangle/admissibility and the five source-defined 6j factors for the frozen primary and held-out sectors after TeX routing is available; reject the OCR-derived alternative in which an index is silently duplicated and another omitted. This lane may classify BLOCKED if exact TeX cannot be obtained.

## Frozen PASS predicates

`EQ11_TEX_ROUTING_PASS` requires exact TeX/source evidence giving a one-to-one, unambiguous transcription of all 10 spin labels and all 15 intertwiner labels into the five vertices, five 6j factors, weights and phase. Every internal label required by the source sum must have a defined role; accidental OCR duplication/omission is a BLOCKER.

`CITED_REFERENCE_AUTHORITY_PASS` requires repository `[30]` to resolve directly from the frozen source and to contain source-relevant executable/script material sufficient to independently check at least the Eq.(11) routing or summation object. If `[30]` is unavailable or lacks that material, classify this lane BLOCKED, not scientific FAIL.

`BACKEND_API_PASS` requires exact SHA provenance and the expected 10-spin/5-intertwiner local vertex interface without using output agreement to choose ordering.

`ALGEBRA_ADMISSIBILITY_PASS` requires exact finite SU(2) 6j evaluations for the frozen sectors under the exact TeX routing and successful rejection of a deliberately malformed duplicated-index transcription. Numerical magnitude is not a PASS criterion.

## Terminal outcomes

- `LORENTZIAN_EQ11_ROUTING_REFERENCE_AUTHORITY_PASS` iff all four predicates PASS.
- `LORENTZIAN_EQ11_ROUTING_REFERENCE_AUTHORITY_BLOCKED` if transport succeeds but exact TeX routing, cited implementation, or a required convention remains unavailable/ambiguous.
- `SCIENTIFIC_FAIL` only for an executed frozen algebra/backend predicate failure.
- `INFRASTRUCTURE_FAIL` only for transport/tool failure before predicates are evaluable.

Only PASS authorizes ITER049 bounded five-vertex summand contraction on the already-frozen primary and held-out sectors. No unbounded sum, convergence/refinement claim, bridge credit, zero-face deletion, or candidate-theory construction is authorized.

## Claim locks

Do not assert `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, or `BRIDGE_DERIVED`. `refinement_map_derived=false`; `bridge_credit=false`; candidate theory `0 / UNFORMED`.
