# ITER164 navigator — submanifold extension / analytic-family authority map

Date: 2026-09-18

Status: **NAVIGATOR_ONLY — NOT ITER164 PASS, NOT A SOURCE OPERATION, NOT ITER165 PREREGISTRATION**.

This note is intentionally non-operative. It does not change the frozen ITER164 source-operation availability gate and does not authorize Laurent extraction. Its purpose is to record the smallest external mathematical authority chain that could support a later prospectively frozen derivation if ITER164 terminally finds the source-qualified open-G endpoint R-operation absent.

## Frozen ISQRG context

- ITER163 has a source-complete 21-term open-G tensor ledger.
- ITER164 requires an operation on the **unseparated** open tensor, preserving the free symmetric metric leg, endpoint orientation, and cancelled-propagator/contact sectors.
- ITER153 already established that ordinary canonical pullback of the ambient contact distributions to the geodesic is not authorized at the endpoint and that general extension theory alone does not supply the graph-level line map.
- No contact pole is zero by absence.

## Primary mathematical sources

### 1. Brunetti–Fredenhagen — scaling-degree extension in perturbative QFT

Romeo Brunetti and Klaus Fredenhagen,
*Microlocal Analysis and Interacting Quantum Field Theories: Renormalization on Physical Backgrounds*,
Commun. Math. Phys. 208 (2000), arXiv:math-ph/9903028.

Relevant role: local/microlocal renormalization by extension of distributions defined away from singular surfaces; scaling degree controls existence and finite local extension freedom.

This is mathematical extension authority, not an ISQRG endpoint prescription.

### 2. Nguyen Viet Dang — extension across a closed embedded submanifold

Nguyen Viet Dang,
*The extension of distributions on manifolds, a microlocal approach*,
arXiv:1412.2808.

The paper treats a smooth manifold `M`, a closed embedded submanifold `I`, and distributions on `U \ I`; geometric scaling and microlocal hypotheses give extensions in `D'(U)` with wave-front control. This is directly relevant to replacing informal point-only reasoning by a theorem whose singular set may be a submanifold.

Again, this theorem supplies conditions/classification of extensions. It does **not** by itself define the ISQRG map from the source-complete open-G graph to a one-dimensional endpoint distribution.

### 3. Dütsch–Fredenhagen–Keller–Rejzner — dimensional regularization in position space

Michael Dütsch, Klaus Fredenhagen, Kai Johannes Keller, Katarzyna Rejzner,
*Dimensional Regularization in Position Space, and a Forest Formula for Epstein–Glaser Renormalization*,
J. Math. Phys. 55, 122303 (2014), arXiv:1311.5424.

Relevant role: analytic/meromorphic regularization in position space; the Laurent principal part is local and represented by finitely many delta derivatives under the stated hypotheses. The existing repository note `ITER162_DISTRIBUTIONAL_EXTENSION_AUTHORITY_CANDIDATE_2026-09-17.md` already records why this result is only an authority candidate for open-G.

## Exact distinction that must be preserved

Three different objects must not be conflated:

1. **Extension theorem**: proves that a distribution on the complement of a singular set admits extensions and bounds/classifies local freedom.
2. **Renormalization scheme/representative**: chooses coefficients inside that local freedom (for example a minimal-subtraction representative).
3. **Source-qualified graph-level operation**: constructs the regulated/meromorphic **unseparated open-G endpoint distribution** from the frozen 21-term source ledger with the affine phase, free tensor leg, upper/lower orientation and contact sectors still present.

ITER164 needs object (3) before it may use (1) to classify ambiguity. Object (2) must not be promoted to physical law merely because it is convenient.

## Counterexample-first consequence

The punctured distribution alone cannot determine a contact contribution supported entirely on the singular set: two extensions agreeing off the endpoint can differ by local delta derivatives allowed by the scaling/singularity degree. Therefore a workflow of the form

`delete/cancel contact -> extend noncontact kernel -> declare contact zero`

cannot be source-authoritative.

The source-qualified route must instead be of the form

`21-term unseparated source tensor + affine phases + regulator`
`-> meromorphic distribution family`
`-> Laurent principal part`
`-> complete allowed local ambiguity span`
`-> quotient`.

## Minimal hypotheses a later prospective derivation must prove

Before any theorem above is applied to the 21-term open-G object, prove explicitly:

1. the distribution domain/test-function space of the unseparated upper and lower endpoint objects;
2. the analytic/meromorphic regulator and the convention `d = 4 - 2 epsilon`;
3. the exact singular/scaling degree transverse to the relevant singular set for every source support sector;
4. the ambient-to-affine construction used instead of the forbidden naive pullback;
5. preservation of the free symmetric metric leg and source orientation;
6. treatment of cancelled-propagator/contact structures inside the same operation;
7. the full local delta/normal-derivative tensor ambiguity allowed by the scaling degree, covariance, endpoint locality and ITER118 derivative ceiling;
8. an independent completeness attack that attempts to exhibit one omitted allowed local tensor;
9. the exact quotient of the source pole information by that full local ambiguity.

## What this note does not establish

It does not establish:

- `PASS_SOURCE_OPERATION_AVAILABLE`;
- any open-G Laurent coefficient;
- a unique pole tensor;
- `A_local` or its dimension;
- a nonzero quotient;
- a contact pole;
- lower/upper relative sign;
- ITER118 coefficients;
- `B1_total`;
- a bridge or candidate theory.

Persistent locks remain:

`ITER118_MATCHING_AUTHORIZED = false`.

`B1_total = UNAUTHORIZED`.

`BRIDGE_DERIVED = false`.

`NEW_PHYSICS_FOUND = false`.

Candidate theory remains `UNFORMED / 0%`.
