# ITER158 auto-research adversarial audit

Date: 2026-09-17

## Scope

This audit checks whether the automated ITER158 execution actually implements the prospectively frozen scientific gate. It does not alter either preregistration and does not reinterpret missing information as zero.

Principal preregistration commit: `e12634d544b345a4e309021cebbb251c9a549abd` (`prereg/ITER158_ENDPOINT_TENSOR_POLE_FIRST_PRINCIPLES_AND_PRIMARY_SOURCE_DERIVATION_2026-09-17.md`).

Operational preregistration addendum commit: `aa9f306845080325f343f3ebf8598dba445b4c39` (`analysis/ITER158_PREREGISTRATION_2026-09-17.md`). The addendum is a direct child of the principal preregistration and precedes implementation/outcome, so it is not post-outcome retuning. Where labels differ, the fuller principal preregistration remains controlling.

Automated implementation commit: `b93890fff1cf9e5ec03c12e479ba283c464bf9ed`.

Workflow commit/head: `f9d8c46021e6a60128148d18650c377f440db6cf`.

Workflow run: `35183584814`.

Artifact: `10481575859`, `iter158-endpoint-tensor-acquisition`.

Artifact ZIP SHA256: `894882977d2cdd22c6cfc5ae736054366039010653401b5cb1755fd2cb19515a`.

Exact JSON SHA256: `8d927ba0016a71a7579481eb7e5cf6d833f00b693018b87f6e47dab0bb408fc2`.

## Frozen requirement actually tested

The principal preregistration requires ITER158 to create or acquire genuinely new mathematical information. The required first-principles chain is

`fields/propagators/vertices -> uncontracted tensor numerator -> regulated endpoint kernel -> raw local pole tensor -> support classification -> endpoint tensor equation`,

or, on the literature lane, an actual primary-source formula plus exact source-to-repository convention/operator map. It explicitly forbids replacing this by another repository grep/audit.

The raw tensor residue must be persisted before endpoint-basis projection, including free indices, contractions, tangent data, general-d dependence, pole order, normalization and support class.

## What the automated implementation actually does

`scripts/iter158_endpoint_tensor_acquisition.py` performs a lexical repository presence scan for six categories (`graviton_propagator`, `geodesic_perturbation`, `first_mg_vertex`, `general_d_regulator`, `endpoint_support_rule`, `r_operation`) and checks whether `inputs/iter158_primary_source_convention_manifest.json` exists.

It does not:

- construct or persist an uncontracted first-M/G tensor numerator;
- perform a regulated endpoint integral;
- extract a `1/epsilon^2` or `1/epsilon` tensor residue;
- classify a newly derived divergent term as endpoint/line/contact/bulk support;
- inspect the frozen primary paper or extract a primary-source formula;
- construct the exact source-to-repository convention/operator map;
- identify the earliest lossy/undefined map by executing the frozen derivation chain.

Its emitted `BLOCKED_SCOPED_ITER158_PRIMARY_SOURCE_CONVENTION_MAP_INCOMPLETE` therefore follows from absence of a checked-in manifest, not from execution of the frozen scientific test.

## Adjudication

**`INVALID_ITER158` — implementation error.**

The run remains useful diagnostic evidence about repository text coverage, but its automated BLOCKED label is not accepted as the scientific terminal outcome of the principal ITER158 gate.

This is not a physical/scientific FAIL and does not imply any endpoint coefficient is zero or nonzero.

## Consequence for ITER159

ITER159 is still usable as a separately preregistered source-extraction/repair gate, because it performs a real acquisition of the frozen arXiv source package. However, its preregistration sentence naming the automated ITER158 BLOCKED label as a terminal parent must not be used to retroactively validate the invalid ITER158 implementation.

Latest successful ITER159 extraction run checked in this audit: `35230270651` at head `9d098d19b57e81d9c0a5bcbec5efa076ea22714c`, artifact `10500703567`, artifact ZIP SHA256 `0a6daac0e655b02c8898395ebb832e249b28938cbc863b486ab72547f6cc47dc`. Its machine classification is `PENDING_MANUAL_SOURCE_CONVENTION_ADJUDICATION`, not a scientific PASS.

## Recovery warning

At head `9d098d19b57e81d9c0a5bcbec5efa076ea22714c`, `recovery/state.json` and `recovery/CURRENT_FRONT.md` remain on the post-ITER157 front and still contain the superseded auto-PASS interpretation of ITER155. They are therefore stale as a scientific authority until explicitly reconciled.

## Claim locks

`B1_total = UNAUTHORIZED`.

`BRIDGE_DERIVED = false`.

`NEW_PHYSICS_FOUND = false`.

Candidate theory remains `UNFORMED / 0%`.
