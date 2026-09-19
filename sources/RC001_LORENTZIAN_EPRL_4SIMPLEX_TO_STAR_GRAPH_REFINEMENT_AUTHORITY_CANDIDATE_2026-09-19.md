# RC001 Lorentzian EPRL 4-simplex -> star graph-refinement authority candidate

Date: 2026-09-19

Status: **AUTHORITY_CANDIDATE_ONLY / NOT ACTIVE ITERATION / NO SCIENTIFIC CLASSIFICATION**

This note does not modify the active ITER179 gate and does not authorize an ITER180/other successor while ITER179 is nonterminal.

## Primary source

Pietropaolo Frisoni, Francesco Gozzini, Francesca Vidotto,
*Markov Chain Monte Carlo methods for graph refinement in Spinfoam Cosmology*,
Class. Quantum Grav. 40 (2023) 105001,
arXiv:2207.02881.

Public source-code repository:

`PietropaoloFrisoni/Markov_Chain_Monte_Carlo_spinfoams`

Inspected repository head:

`8a722eb81b7e4c6f4eba75fe76ec7c89d334b53b`

## What the source explicitly supplies

The paper studies the **Lorentzian EPRL amplitude** with homogeneous boundary spin data under a graph refinement

`5 boundary tetrahedra -> 20 boundary tetrahedra`.

The coarse object is the single 4-simplex / single-vertex graph. The refined object is the source's “star” spinfoam, obtained by splitting each of the five boundary tetrahedra into four tetrahedra.

The paper states that the refined bulk is built from multiple EPRL vertices and that this refinement does not add internal dynamical faces. It computes boundary geometrical observables, their correlations, and entanglement entropy.

The paper uses one common normalized boundary-state framework:

`|psi_0> = sum_{i_n} A(j,{i_n}) |j,{i_n}>`

and

`<O_k> = <psi_0|O_k|psi_0> / Z`,
`Z=<psi_0|psi_0>`.

Thus the two graphs are not merely visually compared: the same class of normalized boundary observable is evaluated on the coarse and refined amplitudes.

The source reports that the average boundary geometry is stable under this refinement while quantum fluctuations/correlations acquire nontrivial finer-scale structure.

## Refined star amplitude

The source gives an explicit star-amplitude contraction in terms of EPRL vertex amplitudes. The public repository implements this contraction in

`src/star_amplitude.jl`.

At inspected head, the code contracts one central vertex tensor with five additional vertex factors over five internal intertwiner sums and twenty boundary intertwiner indices.

The public execution path contains:

- `configs_to_compute.jl`, including `model = "EPRL"`;
- `execute_me.jl`;
- `src/random_walk.jl`;
- `src/star_amplitude.jl`;
- boundary angle, volume, correlation and entropy routines;
- precomputed EPRL vertex-amplitude data.

README execution is explicitly Julia MCMC / Metropolis-Hastings and supports parallel Markov chains.

Therefore the refined Lorentzian EPRL object is **executable source code**, not a lexical or conceptual placeholder.

## Coarse 4-simplex side

The paper separately tests the same Monte Carlo framework on the single Lorentzian EPRL 4-simplex, where the five boundary intertwiner sums are small enough to admit deterministic calculation.

The paper explicitly compares Monte-Carlo output against deterministic single-vertex results before applying the method to the 20-node star.

However, the inspected public repository is organized operationally around the star model:

- executable output paths are named `data_star_model`;
- angle arrays are length 20;
- the central runtime calls `star_amplitude`;
- no separate 5-node coarse executable driver was found by direct code search for
  `4-simplex`, `simplex`, `coarse` or `refinement`.

Thus the source-level coarse formula is present in the paper, but the exact **repository execution binding** for a 5-node deterministic/MCMC coarse comparator is not yet captured inside ISQRG.

## Why this matters relative to the old frontier

Earlier ISQRG recovery described Lorentzian EPRL refinement as blocked for lack of a source-qualified model-matched coarse/fine object.

The 2023 source materially changes that assessment:

1. it is Lorentzian EPRL, not a nearest-framework BF/SU(2) replacement;
2. it supplies an explicit graph refinement from the 4-simplex boundary to a 20-node star boundary;
3. it defines normalized boundary observables on the same amplitude/state framework;
4. it supplies executable public code for the refined star amplitude;
5. it reports the coarse/refined observable comparison.

Therefore the old statement “no source-qualified Lorentzian refinement object exists” is too strong after this source is admitted.

The remaining blocker is narrower: **construct and independently verify an exact source-faithful coarse 4-simplex execution binding and a frozen observable-comparison manifest compatible with the public star code**.

## Required prospective acquisition gate before any scientific comparison

A future gate may become admissible only after freezing and independently checking:

1. exact single-4-simplex EPRL amplitude convention matching the source paper;
2. exact Immirzi / shell truncation / boundary spin conventions used in the chosen star data;
3. 5-node coarse observable evaluator for at least one paper-defined local boundary observable;
4. 20-node refined evaluator using the inspected public star implementation or a source-faithful port;
5. explicit map from one coarse boundary tetrahedron/node observable to the corresponding symmetry-equivalent refined observable average;
6. common normalization convention `Z`;
7. numerical convergence / Monte-Carlo uncertainty criteria;
8. an independent Critic reconstruction of the coarse/refined observable definitions;
9. no use of the source-reported agreement as a fitted target.

Only after that acquisition layer passes should a held-out Lorentzian EPRL refinement test be preregistered.

## Claim ceiling

This source does not establish continuum refinement invariance, full cylindrical consistency, GR recovery or a QG bridge.

It provides a concrete **same-model Lorentzian EPRL graph-refinement laboratory** that was previously missing from the ISQRG source ledger.

Current active science remains ITER179.

Persistent locks remain:

`B1_total = UNAUTHORIZED`

`ITER118_MATCHING_AUTHORIZED=false`

`BRIDGE_DERIVED=false`

`NEW_PHYSICS_FOUND=false`

`NEW_QG_THEORY_REQUIRED=false`

`ALL_KNOWN_SCHOOLS_FAIL=false`

candidate theory `UNFORMED / 0%`.


## Follow-up source-code provenance narrowing

A direct inspection of the public repository's `vertex_ampls/EPRL` tree at
`8a722eb81b7e4c6f4eba75fe76ec7c89d334b53b` found precomputed EPRL vertex tensors for every half-integer spin

`j = 0.5, 1.0, ..., 6.0`.

These are five-index vertex tensors. The star implementation loads one such tensor and uses it both for the central vertex and for the five surrounding vertex factors in the explicit `star_amplitude` contraction.

The public cluster-generation script additionally fixes the numerical EPRL provenance:

- `IMMIRZI=1.2`;
- `SHELLS=20`;
- `vertex-fulltensor` from the authors' sl2cfoam-next installation.

This matches the paper's discussion of an EPRL shell truncation and removes two previously unresolved convention variables from the prospective execution binding.

### Exact coarse observable binding now available in principle

The same repository publishes the diagonal dihedral-angle eigenvalue rule:

`cos(theta_i) = [i(i+1)-2j(j+1)]/[2j(j+1)]`,
for intertwiner `i=0,...,2j`.

Therefore for the stored five-index vertex tensor
`A[i1,i2,i3,i4,i5]`, the exact coarse single-4-simplex expectation at node 1 is source-defined by

`Z = sum_{i1...i5} A^2`

and

`<cos(theta_1)> = (1/Z) sum_{i1...i5} A^2 cos(theta_{i1})`.

The corresponding second moment and quantum spread follow analogously.

No Monte-Carlo fit is needed on the five-node side. The other four nodes provide immediate permutation/symmetry controls.

Thus the remaining acquisition task is now very narrow:

1. load the immutable published JLD2 tensor at an exact external repository SHA;
2. verify its dimensions and real-valued convention;
3. reproduce the paper's coarse regular-tetrahedron angle behavior and node symmetry;
4. bind the same exact tensor to the public star contraction;
5. freeze one or more coarse/refined observable comparisons with uncertainty treatment.

The absence of a dedicated coarse driver in the public repository is therefore no longer evidence that the coarse amplitude object itself is missing.
