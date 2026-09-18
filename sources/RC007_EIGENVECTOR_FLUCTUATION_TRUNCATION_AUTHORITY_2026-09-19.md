# RC007 source authority — eigenvector fluctuation persistence as an entropy-blind truncation channel

Date: 2026-09-19

Status: **SOURCE-QUALIFIED REOPENING AUTHORITY / NOT YET A SCIENTIFIC RESULT**

## Primary source

Théo Keseman, Hans J. Muneesamy, Yasaman K. Yazdi,
*Insights on Entanglement Entropy in 1+1 Dimensional Causal Sets*,
Class. Quantum Grav. 39 (2022) 245004,
arXiv:2111.05879.

Secondary review confirmation:

Abhishek Mathur, Sumati Surya, Nomaan X,
*Spacetime Entanglement Entropy: Covariance and Discreteness*,
Gen. Rel. Grav. 54 (2022),
arXiv:2207.01080.

## Source-qualified statement

The 2021/2022 primary paper studies the causal-set Pauli-Jordan eigenvectors on ensembles of causal sets that share a fixed coarse-grained subset while differing in the additional sprinkled elements.

The procedure is explicitly independent of the target entanglement entropy:

1. choose a fixed coarse-grained causal set of `N_c` elements;
2. construct an ensemble of denser `N`-element causal sets that all contain those same `N_c` elements and differ only in the additional `N-N_c` elements;
3. diagonalize `i Delta` on every ensemble member and order eigenvectors by eigenvalue magnitude;
4. for each mode index `j`, phase-align the corresponding eigenvectors using a shared coarse element;
5. average the aligned `j`-th eigenvectors over the common `N_c` elements;
6. compare the magnitude scale of this averaged vector against the corresponding per-sprinkling magnitude scale.

The source reports that the resulting persistence ratio initially decreases with mode index and later approaches a roughly constant fluctuation regime. Large-eigenvalue modes retain smooth, common large-scale structure; sufficiently small-eigenvalue modes are jagged and realization-specific.

The source then explicitly discusses the transition between the decreasing and plateau regimes as an **independent truncation signature**, and states that this eigenvector-based prescription can generalize to causal sets where analytic wavelength/eigenvalue information is unavailable.

This is distinct from:

- the source density formula `sqrt(N)/(4 pi)`;
- entropy fitting;
- the previously tested two-line knee in the eigenvalue spectrum;
- closure/compression selection;
- Bernoulli-thinning projector optimization;
- ITER178 mass-deformation spectral instability.

## Exact source mechanism relevant to ISQGR

The paper's fluctuation test uses the following scalar compression of a mode:

- in each ensemble member, take the mean of the largest ten absolute entries of the `j`-th eigenvector;
- phase-align the same `j`-th eigenvector across the ensemble on a shared causal-set element;
- average the aligned eigenvector over the ensemble on the common coarse elements;
- again take the mean of the largest ten absolute entries;
- divide the averaged-vector statistic by the ensemble mean of the individual-vector statistic.

A ratio near one indicates a persistent mode shared across sprinklings. A lower ratio indicates cancellation under ensemble averaging and therefore realization-specific fluctuation behavior.

The paper describes the curve as a decreasing regime followed by stagnation and compares those regimes by approximately linear/constant behavior.

## Why this reopens the current Phase-1 frontier

The post-ITER178 repository audit set

`CURRENT_REPOSITORY_PHASE1_EXECUTABLE_UNSATURATED_FRONT_COUNT = 0`

unless genuinely new source/mathematical authority appeared.

This primary source supplies exactly such authority for RC007/BH003:

- same realization;
- executable from the existing causal-set `i Delta` object;
- no entropy target required;
- no source cutoff required during selector construction;
- physically motivated independently of ITER178 output;
- explicitly proposed by the source as a general truncation channel.

Therefore an eigenvector-fluctuation persistence gate is admissible prospectively.

## Claim lock

This authority does **not** establish that the fluctuation transition equals the source SSEE cutoff, nor that it yields an area law.

It authorizes only a prospective test.

No threshold, transition rank or source-cutoff comparison may be chosen after seeing the new campaign.
