# ITER179 preregistration — RC007/BH003 shared-core eigenvector fluctuation-persistence truncation

Date frozen: 2026-09-19

## Authority

Primary source authority:
`sources/RC007_EIGENVECTOR_FLUCTUATION_TRUNCATION_AUTHORITY_2026-09-19.md`

Primary literature:
Keseman, Muneesamy, Yazdi, *Insights on Entanglement Entropy in 1+1 Dimensional Causal Sets*, CQG 39 (2022) 245004, arXiv:2111.05879.

This source explicitly proposes an entropy-independent truncation signature based on whether Pauli-Jordan eigenvectors persist across an ensemble of denser sprinklings sharing one fixed coarse-grained causal set.

## Scientific question

Can the source-proposed transition from persistent shared eigenvectors to realization-specific fluctuation eigenvectors be recovered prospectively and reproducibly, and does its selected scale agree post hoc with the independently known source SSEE cutoff?

No entropy value, entropy coefficient, `sqrt(N)/(4*pi)` cutoff, or source retained rank may enter transition selection.

## Frozen causal-set ensemble

Massless 1+1D causal diamond, using the existing source-native object

`G_R = C/2`,
`i Delta = i(G_R-G_R^T)`.

Parent sizes:

`N = [384, 512, 768, 1024]`.

Independent shared-core seeds:

`core_seed = [311, 337]`.

Eight jobs total.

For each job:

- `N_c = round(0.9 N)`;
- generate the `N_c` shared points once from `core_seed`;
- build `M=12` denser causal sets by adjoining `N-N_c` independent points;
- completion seeds are deterministic functions of `(N, core_seed, completion_index)` and are part of the frozen implementation;
- the shared core points occupy identical array indices in all 12 ensemble members.

The source used a 90% coarse shared set and 20 denser sprinklings. ITER179 retains the source 90% geometry and uses 12 completions for a bounded prospective campaign.

## Frozen eigenvector persistence statistic

For each ensemble member:

1. diagonalize `i Delta`;
2. keep positive eigenvalues and order them from largest to smallest;
3. order the corresponding eigenvectors by the same index `j`.

Analyze mode indices

`j = 5 ... floor(0.80 m_positive)`.

For each `j`:

### Individual magnitude statistic

For every ensemble member, restrict the `j`-th eigenvector to the shared `N_c` elements and compute the mean of its 10 largest absolute entries.

Average this statistic over the 12 ensemble members:

`A_j`.

### Phase alignment

Choose one phase-anchor element deterministically from the shared core: the point with minimum squared Euclidean distance in the stored `(u,v)` coordinates to `(0.5,0.5)`; ties resolve by smallest core index.

For each ensemble member multiply the `j`-th eigenvector by a unit phase so that its value at this same anchor element is real and nonnegative.

If the anchor magnitude is below `1e-12` for any member at a mode, that mode is marked unusable and may not define the transition.

### Averaged-vector magnitude statistic

Average the aligned restricted `j`-th eigenvectors over all 12 ensemble members on the shared `N_c` points.

Compute the mean of the 10 largest absolute entries of that averaged vector:

`B_j`.

Define source-derived persistence ratio

`R_j = B_j / A_j`.

A persistent mode has `R_j` closer to one. Realization-specific fluctuation modes are expected to have smaller persistence and eventually approach a plateau.

No entropy or source cutoff enters `R_j`.

## Frozen transition selector

The primary source describes an approximately decreasing regime followed by a roughly constant fluctuation regime.

For every candidate break `k` satisfying at least 20 usable modes on each side:

- fit `R_j = a + b j` on the prefix;
- fit a constant `R_j = c` on the suffix;
- compute total residual sum of squares `RSS_LC(k)`.

Compare with a single-line null model `R_j = a_0+b_0 j` over the same usable range.

Choose the `k` minimizing `RSS_LC`.

Use

`BIC = n log(RSS/n) + p log n`

with `p=4` for line+constant and `p=2` for one line.

A job-level transition is `RESOLVED` iff all are true:

1. `DeltaBIC = BIC_single - BIC_line_constant >= 10`;
2. fitted prefix slope `b < 0`;
3. if the suffix is separately fit to a line, `|b_suffix| <= 0.25 |b_prefix|`;
4. the selected break lies inside the analyzed range with >=20 usable modes on each side;
5. leave-one-completion-out recomputation over the 12 ensemble members gives a median break within 10% of the full break and at least 9/12 leave-one-out breaks within 20% of the full break.

The selected positive-mode rank is `j_star = k`.

The selected eigenvalue scale is the geometric mean across the 12 members of the magnitude of the positive eigenvalue at `j_star`.

## Independent Critic

Researcher and Critic independently regenerate all causal sets from frozen seeds.

Researcher uses SciPy Hermitian eigendecomposition and direct top-10 magnitude calculation.

Critic uses NumPy Hermitian eigendecomposition and a separately implemented phase-alignment / line+constant fit.

For every usable `j`, the two persistence-ratio curves must agree within absolute `1e-7`.

They must agree exactly on:

- usable mode index set;
- RESOLVED / UNRESOLVED;
- selected break index when resolved.

Failure is `INVALID_IMPLEMENTATION_ITER179`.

## Frozen campaign-level transition gate

The source mechanism is considered reproducibly identified only if:

- at least 6/8 jobs are RESOLVED;
- for each N, at least one of its two independent core-seed jobs is RESOLVED;
- among resolved jobs the coefficient of variation of `j_star/sqrt(N)` is <= 0.35.

If these fail after implementation validity passes:

`BLOCKED_SCOPED_ITER179_FLUCTUATION_TRANSITION_NOT_STABLY_IDENTIFIED`.

## Post-selection source comparison

Only after `j_star` has been selected, compute:

`lambda_source = sqrt(N)/(4*pi)`.

For each ensemble member compute the positive source rank

`j_source = count(lambda_positive >= lambda_source)`.

Compare:

- `j_star / median(j_source)`;
- `lambda_star / lambda_source`.

A source-compatible fluctuation selector requires campaign medians satisfying:

1. median `j_star / j_source in [0.5, 2.0]`;
2. median `lambda_star / lambda_source in [0.5, 2.0]`.

No entropy calculation is needed for ITER179. Entropy/double-truncation transfer belongs to a successor only after this gate passes.

## Frozen terminal taxonomy

### PASS

`PASS_SCOPED_ITER179_EIGENVECTOR_FLUCTUATION_TRANSITION_SOURCE_COMPATIBLE`

iff implementation validity passes, campaign transition gate passes, and both post-selection source-compatibility predicates pass.

Claim ceiling: the source-proposed eigenvector-fluctuation transition supplies an entropy-blind same-realization truncation scale compatible with the known 1+1D SSEE cutoff in this bounded campaign.

### SCIENTIFIC FAIL, scoped

`SCIENTIFIC_FAIL_SCOPED_ITER179_STABLE_FLUCTUATION_TRANSITION_SOURCE_INCOMPATIBLE`

iff implementation validity passes and the campaign transition gate passes, but one or both source-compatibility predicates fail.

This falsifies scale-identification by this frozen source-derived persistence selector, not causal-set SSEE or causal-set theory.

### BLOCKED, scoped

`BLOCKED_SCOPED_ITER179_FLUCTUATION_TRANSITION_NOT_STABLY_IDENTIFIED`

iff implementations agree but the campaign transition gate fails.

### INVALID

`INVALID_IMPLEMENTATION_ITER179`

for provenance mismatch, missing frozen jobs, non-finite required quantities, or Researcher/Critic disagreement beyond frozen tolerances.

## No post-hoc repair

After output:

- do not change the phase anchor;
- do not change top-10 to another number;
- do not smooth `R_j`;
- do not change the line+constant family;
- do not flip or redefine the transition;
- do not tune BIC or stability thresholds;
- do not use entropy to select a breakpoint.

A different selector requires a new independent source/mathematical rationale.

## Persistent locks

Always unchanged:

`B1_total = UNAUTHORIZED`

`ITER118_MATCHING_AUTHORIZED=false`

`BRIDGE_DERIVED=false`

`NEW_PHYSICS_FOUND=false`

`NEW_QG_THEORY_REQUIRED=false`

`ALL_KNOWN_SCHOOLS_FAIL=false`

Candidate theory remains `0 / UNFORMED`; bridge credit remains 0.
