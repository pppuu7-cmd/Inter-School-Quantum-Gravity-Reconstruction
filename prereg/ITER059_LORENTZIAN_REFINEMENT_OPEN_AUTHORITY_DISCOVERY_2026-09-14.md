# Preregistration — ITER059 open Lorentzian refinement authority discovery

Date frozen: 2026-09-14

## Inherited state

ITER056–058 establish a scoped authority blocker: the Lorentzian EPRL 5→1 fine amplitude is source-qualified and nearby spin-foam models contain explicit coarse-graining maps, but no exact model-matched Lorentzian simplicial EPRL refinement/transfer map has yet been qualified.

The search must not respond by importing Euclidean, hypercuboidal, BF or Riemannian-holomorphic maps.

## Scientific purpose

Perform a prospective, reproducible literature discovery for **previously untested exact Lorentzian-EPRL-compatible refinement/coarse-graining authority**. This is discovery only: candidates are not scientific PASS until a later source-qualification gate freezes and consumes their exact source.

## Frozen discovery queries

Exactly four independent arXiv discovery lanes are frozen before results:

1. `lorentzian-eprl-refinement`: `all:"Lorentzian EPRL" AND (all:refinement OR all:"coarse graining")`
2. `lorentzian-spin-foam-map`: `all:"Lorentzian spin foam" AND (all:"embedding map" OR all:"coarse graining")`
3. `eprl-rg-simplicial`: `all:EPRL AND all:renormalization AND (all:simplicial OR all:Pachner)`
4. `eprl-refinement-map`: `all:EPRL AND (all:"refinement map" OR all:"embedding map")`

Each lane requests up to 50 entries, sorted by relevance. No query may be changed after seeing results in ITER059.

## Candidate inclusion rule

A candidate may be promoted to a later source-qualification gate only if title/abstract/metadata prospectively indicate at least two of:

- Lorentzian EPRL/EPRL-FK object;
- explicit refinement/coarse-graining/embedding/renormalization transformation;
- simplicial/Pachner/multi-vertex object;
- boundary-state or amplitude map between discretizations.

Already-consumed sources `2302.00072`, `1803.00835`, `0810.1714`, `1903.12624`, `1412.8247`, `1409.2407`, `1701.02311` are retained as saturation controls, not new candidates.

## Lanes

Run the four queries independently with `fail-fast:false`, plus a null/provenance lane. Save exact query, retrieval timestamp, entry arXiv IDs, titles, authors, abstracts and API-response SHA256.

## Classification

- `DISCOVERY_POSITIVE_SCOPED`: at least one genuinely new candidate passes the metadata inclusion rule. This authorizes only a new preregistered exact-source qualification gate.
- `DISCOVERY_SATURATED_SCOPED`: retrieval succeeds but no new candidate passes inclusion after deduplication against consumed sources.
- `INFRASTRUCTURE FAIL`: query transport/parsing fails before discovery can be evaluated.

Neither positive nor saturated discovery gives bridge credit.

## Locks

`refinement_map_derived=false`; `bridge_credit=false`; candidate theory `UNFORMED / 0%`. No amplitude execution, no numerical threshold, no map fitting, no claim-lock release.