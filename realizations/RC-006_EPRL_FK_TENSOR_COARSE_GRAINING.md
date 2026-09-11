# RC-006 — EPRL/FK-type simplicity constraints under tensor-network coarse graining

Status: `MECHANISM_MAPPED / REDUCED_MODEL`  
Family: `F04 spinfoam/LQG`  
Date: 2026-09-12

## Primary source

B. Dittrich, E. Schnetter, C. J. Seth, S. Steinhaus, *Coarse graining flow of spin foam intertwiners* (2016), arXiv:1609.02429.  
https://arxiv.org/abs/1609.02429

Related method source:

B. Dittrich, F. C. Eckert, M. Martin-Benito, *Coarse graining methods for spin net and spin foam models* (2011), arXiv:1109.4927.  
https://arxiv.org/abs/1109.4927

Evidence class: `SOURCE_GROUNDED / REDUCED_EUCLIDEAN_ANALOGUE`.

## Scope firewall

The audited system uses intertwiner/spin-net models with `SU(2)_k x SU(2)_k` data implementing simplicity constraints analogous to 4D Euclidean BC and EPRL/FK spin-foam constructions. It is **not** the full Lorentzian EPRL theory and cannot establish a family-level continuum verdict.

Its value for ISQGR is narrower: it supplies a concrete example where physically defining constraint data can change nontrivially under an explicit coarse-graining map.

## Source-grounded mechanism

The cited work applies adapted tensor-network renormalization to follow simplicity constraints across scales.

Within the studied truncation/model class:

- BC-type and EPRL/FK-type models show different coarse-graining behavior;
- EPRL/FK-type data flow away from the original simplicity constraints immediately;
- with the employed truncation they do not generically settle to a fixed point;
- the authors explicitly identify further coarse-graining development as necessary for large-scale spin-foam analysis.

These statements are scoped to the studied reduced models and numerical method.

## ISQGR interface map

- IF-03 dynamics/amplitude: `MAPPED_PARTIAL`
- IF-04 composition/gluing: `MAPPED_PARTIAL`
- IF-06 gauge/constraint structure: `MAPPED_PARTIAL`
- IF-08 continuum/coarse graining: `MAPPED_PARTIAL`
- IF-10 GR recovery: `NOT_ESTABLISHED_IN_THIS_CARD`
- IF-12 UV/IR identity: `OPEN_BLOCKED`
- IF-15 cross-school splice: `NOT_APPLICABLE`

## BH-001A relevance

The result is a concrete warning against assuming

`coarse-grain(constraint-defined physical data)`

`=`

`same constraint-defined data at a larger scale`.

In the language of the scale/composition leakage identity, the original simplicity-defined sector need not be invariant under the coarse map/effective dynamics.

This does **not** prove that the exact BH-001A leakage operator is the correct mathematical description of the spin-foam calculation. Establishing that requires an explicit native mapping of retained/discarded tensor sectors to physical constraint data.

## Motif-candidate contribution

This card supports a candidate motif:

`MC-001 — PHYSICAL/CONSTRAINT SECTOR NOT AUTOMATICALLY CLOSED UNDER SCALE FLOW`.

`MC-001` is not promoted to `RM-001` yet. Promotion requires at least one further independent QG realization with a source-defined analogous obstruction at the same semantic level, plus a dependence audit.

## Next cheapest tests

1. Translate one explicit tensor-network truncation step into retained/discarded sectors and compute a native analogue of `Delta_seq`.
2. Check whether enlarging the retained tensor/constraint data closes the flow with finite additional operators.
3. Compare the required closure variables with FRG-generated operator closure in a continuum realization without equating them by analogy.
4. Keep Lorentzian EPRL continuum claims locked until a same-realization Lorentzian refinement chain is audited.

## Claim lock

Flow away from simplicity constraints in this reduced numerical model is not a refutation of EPRL/FK or loop quantum gravity.