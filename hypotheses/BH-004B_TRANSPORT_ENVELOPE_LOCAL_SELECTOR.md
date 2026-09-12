# BH-004B — Transport Envelope + Local Physical Selector

Status: `BRIDGE REFINEMENT / ADMITTED FOR FALSIFICATION`  
Date: 2026-09-12  
Parent: `BH-004_PROJECTOR_MEASURE_COVARIANT_SCALE_TRANSPORT`  
Motivation: `ITER004_BH004_STABLE_CORE_NEGATIVE_ENVELOPE_SIGNAL`

## 1. Problem exposed by the stable-core holdout

The first BH-004 three-level test forced the transported parent subspace to a predicted child rank and obtained useful closure but a weak minimum principal cosine.

A subsequent disjoint-seed fourth-level test attempted to identify and prune a universal unstable tail using restriction singular values. That preregistered stable-core gate failed: the training-only threshold `tau=0.525` did not improve projector distance relative to the unpruned restriction.

However, the unpruned transported restriction itself showed very strong held-out containment of the child source sector:

- median mean principal cosine about `0.988`;
- median minimum principal cosine about `0.868`;
- median transported rank about `1.15` times the child source rank;
- closure advantage over rank-matched random controls remained large.

This suggests that **orientation transport and physical-rank selection are distinct operations**.

## 2. Hypothesis

At a child scale `s'`, the canonical image of a parent physical sector need not equal the final child physical sector. Instead it may define an overcomplete transport envelope

`E_{s'} = span(T_{s->s'} P_s)`

such that

`P_{s'} approximately lies inside E_{s'}`.

The final physical projector is then selected by a source-native child-scale constraint/measure operator `J_{s'}` and scale datum `mu_{s'}` **inside the transported envelope**:

`P_hat_{s'} = E_{s'} 1[ |E_{s'}^† J_{s'} E_{s'}| >= mu_{s'} ] E_{s'}^†`.

For the present causal-set realization:

- `J = i Delta = (i/2)(C-C^T)`;
- `mu(N) = sqrt(N)/(4*pi)` is the frozen source BH-003 spectral rule;
- the envelope is the full numerical-rank restriction of the parent source sector to the nested child subset.

No closure target enters the selector.

## 3. What makes the test nontrivial

Applying the source spectral rule to the **full** child `J` reproduces the source child projector by definition and therefore is not a test.

BH-004B instead first restricts the allowed orientation space to the parent-derived envelope, then diagonalizes only the **projected child operator**

`J_E = E^† J_child E`.

If the parent envelope misses physically necessary directions, or if local spectral selection and transport do not commute even approximately, the reconstructed projector will disagree with the full child source sector.

Thus the test probes a factorization:

`parent physical orientation -> transported envelope -> local source-native selection`,

rather than merely re-running the child source prescription.

## 4. Falsifiable held-out gate

Use new parent sizes and seeds not used in previous BH-004 campaigns where practical. For each nested transition, construct:

1. parent source projector from the frozen source rule;
2. full transported envelope by canonical restriction;
3. projected child `J_E`;
4. predicted child projector from the same frozen scalar cutoff `mu(N_child)` applied **inside the envelope**;
5. only afterward construct the full child source projector for evaluation.

Compare against:

- the envelope without local selection;
- the previous rank-matched SVD transport idea;
- rank-matched Haar controls;
- the full child source sector as evaluation oracle only.

### Natural support

Require in aggregate:

- median predicted/source rank relative error `<= 0.15`;
- median mean principal cosine `> 0.95`;
- median minimum principal cosine `> 0.50`;
- median normalized-projector-distance ratio `predicted/envelope < 0.80`;
- median random/predicted leakage and sequential-return improvements both `>1`;
- at least `2/3` jobs improve both closure metrics over random.

### Strong support

Require:

- rank error `<=0.08`;
- mean cosine `>0.98`;
- minimum cosine `>0.80`;
- distance ratio `predicted/envelope <0.60`;
- both median closure improvements `>1.5`;
- at least `0.80` jobs improve both metrics.

These thresholds are fixed before the new held-out campaign.

## 5. Kill conditions

Reject BH-004B in this causal-set realization if:

- projected local selection cannot recover child source rank/subspace substantially better than the raw envelope;
- the envelope systematically excludes source directions;
- the result requires closure-target-dependent tuning;
- the scalar cutoff must be changed ad hoc after viewing child results;
- extra directions are necessary for the observed closure benefit but cannot be removed by source-native local information.

## 6. Novelty lock

The architecture is close to standard projected effective-space and tensor-network ideas: first transport an effective subspace, then impose a local/truncated operator inside it. Therefore success would **not** by itself establish new physics.

Scientific value would be to show that the causal-set source structure naturally realizes the same factorization that the cross-school RM-001 closure theorem demands, and to provide a precise object that can later be sought in an independent QG refinement realization.

`NEW_PHYSICS = NOT AUTHORIZED`  
`CANDIDATE_THEORY = UNFORMED`
