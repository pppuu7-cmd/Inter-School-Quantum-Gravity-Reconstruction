# ITER054 — bounded Lorentzian five-vertex fixed summands

Date: 2026-09-14

## Terminal classification

**SCIENTIFIC PASS — `LORENTZIAN_BOUNDED_FIVE_VERTEX_FIXED_SUMMAND_VALIDATED_SCOPED`.**

This verdict was assigned from the frozen preregistered predicates and consumed raw evidence artifacts, not from green CI alone.

PASS scope is deliberately narrow: two pre-frozen low-spin 5→1 **fixed summands** at `gamma=1.2`, `Dl=0`, standard Lorentzian `mu=weight=1`, evaluated with the exact pinned `sl2cfoam-next` runtime and source-qualified local argument/recoupling/phase convention. No ten-face/fifteen-intertwiner sum was performed.

## Frozen provenance

Preregistration: `prereg/ITER054_LORENTZIAN_BOUNDED_FIVE_VERTEX_FIXED_SUMMAND_2026-09-14.md`.

Prereg commit: **`39b33c127342e6b12150228bfd91b3e37e967683`**.

Implementation commit: **`5b295ed5cf5c9416a77661bccb7fb9140a6b573d`**.

Production/workflow head: **`1fd40c077cc25dd12573f683fb457b7180f63e46`**.

Authoritative Actions run: **`34821111285`**.

Frozen call-map object: `sources/ITER053_FIXED_SECTOR_BACKEND_CALL_MAP.json`, git blob **`1af32d358747f333a04531d27af1e03b9a0bd038`**.

Runtime inherited exactly from ITER051 run `34818301950`, artifact `10336669907`, with backend `qg-cpt-marseille/sl2cfoam-next@052e4346028870bd76f69a3034e6cae8defb8f7f`.

## Raw jobs and artifacts

All eight preregistered lanes were terminal and their raw artifacts were consumed.

- authority-object — job **`103902664531`**, artifact **`10338575774`**, digest `sha256:f905d972d2e1c524ddff94fda4217b7ea75bca9cd471af3e680126a6c51da857` — PASS;
- null-controls — job **`103902664557`**, artifact **`10337764334`**, digest `sha256:ca3bede6a61b047b7480dc29ae976fa82f5653fe032e17cf7f9b5622a441ff71` — PASS;
- recoupling-controls — job **`103902664600`**, artifact **`10338192052`**, digest `sha256:c8391b7664388e5655dc813c3d5ba558b908a7ddfefba524985834a4f4d6f49b` — PASS;
- runtime-identity — job **`103902664191`**, artifact **`10338710281`**, digest `sha256:0695800a2d3eefb52d355191605ad93a11be2cb87e50f8b690f5fa24f8008cd7` — PASS;
- primary-A — job **`103902664421`**, artifact **`10337534649`**, digest `sha256:3a2437ec0b1c51673c09b5e194c5bb7ac51e4dfaea7f6c3bd46021f5021a99d9` — PASS;
- primary-B — job **`103902664403`**, artifact **`10337824138`**, digest `sha256:c27d122f8e25f5b37cadd15198294f964464a5d46082d16bc5f49008ed6d3384` — PASS;
- heldout-A — job **`103902664434`**, artifact **`10338228086`**, digest `sha256:608e0a77920ce5c53bd908d88369c5e9fee1c7b8fe1d7256caf77821f61511ed` — PASS;
- heldout-B — job **`103902664580`**, artifact **`10337943965`**, digest `sha256:411c6cbd414cc28cf83abe5e38abd1fc539e53baa51dca76a2ac7421c328711a` — PASS.

Dependent aggregate — job **`103902785578`**, artifact **`10337904083`**, digest `sha256:0dbc02a599838b22f0a8985cb73057beb18d4b3bc7f490e7bc6630472a9e0130` — records `LORENTZIAN_BOUNDED_FIVE_VERTEX_FIXED_SUMMAND_VALIDATED_SCOPED`.

## Source/runtime controls

Authority-object PASS independently re-established that the pinned backend's `sl2cfoam_vertex_amplitude(two_js,two_is,Dl)` fixes all five intertwiner ranges to the supplied labels and returns the unique `(0,0,0,0,0)` tensor component. The immutable call-map blob and ITER051/052/053 prerequisite records were present.

Runtime-identity PASS reproduced all frozen hashes:

- `bin/vertex-amplitude`: `b4f8f536645b3fe6bc55830040f624140eefca02a3b960b9940b2564a7876e26`;
- `lib/libsl2cfoam.so`: `a539c968afde2a7ec397b2fa7184f9dd036042b82ff2ec5d8026c2b6881b71fc`;
- `.3j` table: `73d9170de4f04b776923106c5c6ea1bbb70cf2e62a14d24b83cda31194567e6e`;
- `.6j` table: `de1a29d0252c3c1ebf51b96d7fdebe7f21587ee65dcbc3864070774c14704b72`.

Exact recoupling controls reproduced the prospectively frozen values:

- primary: five factors `+1/2`;
- held-out: five factors `-sqrt(3)/2`;
- both sectors: `df_phase=+1`, face factor `1024`, paper conversion `A_paper=-A_author`;
- primary final signs `[-1,-1,-1,-1,-1]`;
- held-out final signs `[+1,-1,-1,+1,-1]`.

Adversarial null controls rejected wrong doubled held-out labels, literal-Eq.(11) held-out routing, a second manual edge-dimension product, and insertion of the paper sign inside the author-convention production formula.

## Primary fixed summand

Both independent replicas executed five exact backend calls. Every local vertex returned

`V = 1.34499311005e-09`.

The source-frozen author-convention summand is

**`A_author(primary) = -1.4084786761527471e-43`**.

The prospectively declared paper conversion gives

**`A_paper(primary) = +1.4084786761527471e-43`**.

A/B absolute differences are exactly `0.0` for all five local vertices and both reported summands. The frozen reproducibility predicates PASS.

## Held-out fixed summand

Both independent replicas executed the prospectively frozen non-retuned call map. Local vertex values were, in source-defined order `(up,left,bottom-left,bottom-right,right)`:

1. `+2.32959640243e-09`;
2. `-7.76532134144e-10`;
3. `-1.34499311005e-09`;
4. `-4.48331036683e-10`;
5. `-1.34499311005e-09`.

The source-frozen author-convention summand is

**`A_author(heldout) = +7.318669885380604e-43`**.

The paper conversion gives

**`A_paper(heldout) = -7.318669885380604e-43`**.

Again A/B absolute differences are exactly `0.0`; all frozen local and summand tolerances PASS. No primary-vs-heldout ratio or sign relation was a PASS target.

## Scientific meaning

This closes the earlier implementation gap: the exact source-qualified Lorentzian 5→1 construction can now be evaluated as complete fixed five-vertex summands in two prospectively frozen sectors, including a held-out non-retuned sector, with exact runtime provenance and reproducibility.

This is stronger than a single-vertex smoke test, but it is **not** a refinement-map derivation. It does not establish the full internal-label sum, convergence in `Dl`, coarse↔fine amplitude equality, zero-face deletion, universality, continuum/GR recovery, or new physics.

## Claim locks / readiness

`refinement_map_derived=false`.

`bridge_credit=false`.

Candidate theory remains **`UNFORMED / 0%`**.

Overall scientific-programme readiness remains **49%**: this PASS closes an authorized bounded rubric item but does not yet close the genuine refinement-map/bridge rubric.

Still forbidden: `ALL_KNOWN_SCHOOLS_FAIL`, `NEW_QG_THEORY_REQUIRED`, `NEW_PHYSICS_FOUND`, `BRIDGE_DERIVED`; full Eq.(27), Eq.(29)/Lambda and one-step TNR remain unauthorized from this result.

## Exact next admissible gate

A successor may now be preregistered only as either:

1. a **bounded, prospectively frozen fixed-configuration minipanel / transport test** with additional source-valid sectors and no retuning; or
2. a **source-faithful refinement-map test** only if the genuine map object and coarse/fine objects are explicitly pinned before numerical output.

No unbounded ten-face/fifteen-intertwiner sum or shell/convergence escalation is authorized merely by this PASS.