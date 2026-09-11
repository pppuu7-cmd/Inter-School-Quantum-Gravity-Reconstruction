# BH-002 — Causal–Entanglement Metric Reconstruction (CEMR)

Status: `BRIDGE_HYPOTHESIS / DOMAIN_SCOPED`  
Date: 2026-09-12  
Origin: Corridor B, RC-004 causal set + RC-005 holographic/QEC mechanism.

## 1. Motivation

Two independently developed reconstruction facts suggest a sharper inter-school bridge:

1. In sufficiently well-behaved Lorentzian spacetimes, causal order determines the conformal geometry, i.e. the metric up to a positive local conformal factor.
2. In controlled holographic/entanglement-reconstruction settings, families of entanglement quantities determine geometric area or metric data.

BH-002 asks whether these can be used as complementary rather than competing reconstructions.

The slogan is deliberately narrower than a theory of quantum gravity:

`causal structure -> conformal geometry`

`quantum-information geometry data -> scale / area structure`

`compatibility -> reconstructed Lorentzian metric`

## 2. Classical reconstruction skeleton

Let the emergent semiclassical sector admit a distinguishing Lorentzian spacetime `(M,g)`.

A causal-order reconstruction determines a conformal class

`[g] = { Omega^2 g_bar | Omega(x) > 0 }`.

Choose a representative `g_bar` fixed only up to the remaining local scale `Omega`.

The unknown metric is

`g = Omega^2 g_bar`.

CEMR seeks independent quantum-information data sufficient to determine `Omega` without inserting the target metric by hand.

## 3. Entanglement/area input

In the leading semiclassical holographic regime, the Ryu–Takayanagi relation supplies geometric area data from boundary entanglement entropy schematically as

`S(A) = Area(gamma_A) / (4 G_N)`

for appropriate regions/surfaces and domain assumptions.

More general entanglement-based reconstruction programmes can infer spatial metric data from sufficiently rich entanglement data without assuming that HaPPY itself is realistic gravity.

Under `g = Omega^2 g_bar`, a local codimension-`p` induced volume element scales as a power of `Omega`. In 4D, codimension-2 area data are sensitive to `Omega^2` along the surface.

Thus a sufficiently rich family of independent area/entanglement constraints can in principle supply equations for the missing conformal scale.

## 4. Core inverse problem

Given:

- causal order `C`, determining `[g]`;
- entanglement data `E = {S(A)}` in a domain where a geometric reconstruction theorem/algorithm is valid;
- calibration data such as `G_N` or an independently determined scale relation;

solve

`Area_{Omega^2 g_bar}(gamma_A[Omega]) = 4 G_N S(A)`

for `Omega(x)` together with the extremal-surface dependence `gamma_A[Omega]`.

This is a nonlinear inverse problem because the relevant surfaces themselves depend on the metric.

A successful CEMR result requires uniqueness/stability conditions, not merely the formal equation.

## 5. Why this is more specific than BH-001

BH-001 concerns compatibility of composition and scale flow in many frameworks.

BH-002 makes a concrete geometric claim:

> causal information and quantum-information area/metric information may be complementary data channels for reconstructing one Lorentzian geometry.

It can therefore fail mathematically even if BH-001 survives.

## 6. Immediate nontrivial predictions / constraints

If CEMR is correct in a domain, then:

1. entanglement data inconsistent with a single conformal factor over the causally reconstructed class must be rejected as belonging to that semiclassical geometry;
2. causal reconstruction and entanglement reconstruction must produce the same dimension/topology/domain where both are applicable;
3. the inferred scale field `Omega(x)` must be independent of which sufficiently complete family of admissible entanglement regions is used;
4. coarse graining must map both the causal-order and entanglement reconstruction data to the same effective metric rather than two independently fitted metrics.

These are compatibility tests, not inserted target equations.

## 7. Major blockers

### B1 — Domain overlap

The causal-order reconstruction theorem and holographic entanglement reconstruction must apply to the **same physical regime**. AdS/CFT-specific results cannot be silently exported to generic spacetime.

### B2 — Circular region definition

Boundary/subregion labels used to define entanglement data may already presume geometric information. CEMR must formulate the input relationally enough to avoid inserting the scale it aims to derive.

### B3 — Quantum corrections

At finite quantum-gravity corrections the simple area law is replaced by generalized-entropy / quantum-extremal-surface structure. Entanglement is then not pure geometric area.

Initial CEMR tests are therefore restricted to a controlled leading semiclassical domain unless a corrected inversion is derived.

### B4 — Scale calibration

`G_N` or an equivalent physical scale must be identified through the same realization. It may not be chosen post hoc to force agreement.

### B5 — Dynamics

Metric reconstruction is kinematics. Even a successful CEMR does not yet derive Einstein dynamics or a quantum gravitational amplitude.

## 8. Relation to causal-set "order + number"

Causal set theory commonly summarizes its continuum reconstruction as

`order + number ~ Lorentzian geometry`,

where counting supplies volume information missing from causal order.

CEMR tests a different possibility in an overlap domain:

`causal order + quantum-information geometric data -> Lorentzian geometry`.

It does **not** claim that entanglement replaces causal-set cardinality inside causal set theory. The two are alternative scale channels to compare.

A later synthesis test may ask whether counting/volume and entanglement/area become related observables of one deeper state.

## 9. Falsification tests

Reject or narrow BH-002 if any of the following holds in the chosen overlap domain:

1. the same causal class admits multiple inequivalent conformal factors reproducing all entanglement data;
2. entanglement reconstruction yields metric information incompatible with the causally reconstructed conformal class;
3. the required region labels or cutoff scheme already contain the target conformal factor;
4. `G_N`/scale calibration cannot be fixed independently;
5. generalized-entropy corrections are of the same order as the inferred scale and destroy identifiability;
6. the construction reduces to an already complete single-school reconstruction with the causal input doing no work.

## 10. Novelty firewall

Pieces of BH-002 are known separately:

- causal structure -> conformal metric;
- order + volume reconstruction in causal-set theory;
- entanglement/RT-based geometry reconstruction in holography;
- entanglement-based spatial metric reconstruction beyond a boundary in specialized settings.

ISQGR does **not** currently claim that their exact combination is novel.

Novelty would require a new compatibility theorem, inversion algorithm, obstruction, or observable consequence arising specifically from using both channels together.

## 11. Current verdict

`BH-002 = ADMISSIBLE / HIGH-PRIORITY / UNPROVED`

It is currently the most concrete ISQGR bridge candidate because it converts a philosophical school tension into a well-posed inverse problem.
