# ITER036 result — bounded EPRL-map label instantiation/consistency

Date: 2026-09-14

Scientific classification: **BLOCKED — `RC006_EPRL_MAP_LABEL_INSTANTIATION_CONSISTENCY_BLOCKED`**.

This is not a scientific failure of the EPRL map. The frozen source case extraction, exact map identities, finite-k cutoffs, and null controls all pass. The blocker is prospective panel support under the preregistered primary/held-out split: the source-derived nonzero mapped labels provide only one tested two-label pair, and that pair lands in held-out, leaving `primary_tested=0`. The split is not changed after seeing this result.

## Frozen provenance

- preregistration commit: `be603f7b288a60b0feb76d3bfc723523f6723754`
- implementation commit: `d9350854500b2d31c53f08fdbc325908909d9ef0`
- production head: `862736b45047cadef8f696e79e15815f67dd559b`
- authoritative run: `34805398376`

Jobs/artifacts:
- B map-integrality/cutoff job `103856182955` -> artifact `10333200104`, digest `sha256:1ca4b58653f480e9776ad114b1e60babb2f8729b44e2afbb595c4f3107b1f121`
- C indexed-exponent instantiation job `103856183065` -> artifact `10332158139`, digest `sha256:535cc85c7cc1b967a14c2e0cd0add1537837da6462c34d1730833d6d4ec44633`
- D null-controls job `103856183071` -> artifact `10332703718`, digest `sha256:e948045e6a2f88c1a45c19196cb1d402def7376c1d09be43a4c82847286e52f4`
- A source-list extraction job `103856183212` -> artifact `10332953277`, digest `sha256:0cd59fd2bcd89e63b447660e3c926c6c2e0e1935eb8427a7b4600a434a55a81c`
- aggregate job `103856219007` -> artifact `10332364237`, digest `sha256:e1c567700838c12ab742cb32f68c68b770f7453d023eb54ee800b4277e47c1d7`

## Scientific readout

Lane A PASS: the exact source mechanically yields exactly three non-trivial finite-q EPRL cases:
- `k=6, gamma=1/3: l=3 -> (j^+,j^-)=(2,1)`;
- `k=10, gamma=3/5: l=5 -> (4,1)`;
- `k=12, gamma=1/3: l=3 -> (2,1)` and `l=6 -> (4,2)`.

Lane B PASS: all seven generated entries including the trivial `l=0` entries satisfy exact rational map identities, integrality, and cutoff. The frozen alternating split contains 4 primary and 3 held-out entries.

Lane C is **BLOCKED_PANEL_SUPPORT**, not FAIL. After requiring two nonzero mapped labels within the same source-listed `(k,gamma)` case, only `k=12, gamma=1/3, (l_1,l_2)=(3,6)` remains. It has common admissible internal `j={3,4}` and exact source exponents `(factor1,factor2)=(-5,0)` at `j=3` and `(-1,4)` at `j=4`, so the substantive exponent construction works. But under the prospectively frozen entry split this tested pair is held-out, giving `heldout_tested=1`, `primary_tested=0`. The preregistration explicitly required at least one tested pair in each, so the lane remains blocked.

Lane D PASS: all 3/3 frozen wrong maps are detected — swapped plus/minus, missing factor 1/2, and above-cutoff extension.

Aggregate: `blocked_lanes=[C]`, `failed_lanes=[]`, no infrastructure failure, `scientific_pass=false`, classification `RC006_EPRL_MAP_LABEL_INSTANTIATION_CONSISTENCY_BLOCKED`.

## Exact authorization

ITER036 does **not** authorize the bounded numerical Eq.(27) scalar/summation lift. The next admissible independent question is a prospectively preregistered source-authority gate asking whether Eq.(27)'s two external labels `l_1,l_2` may independently take the same source-admissible mapped representation (`l_1=l_2`) and whether such diagonal external-label pairs are explicitly within source scope. This is not a retrofit of the ITER036 split.

Only positive source authority for diagonal/independent external-label support could justify a new panel-construction gate. Absence of such authority remains BLOCKED.

Candidate theory remains `UNFORMED / 0%`; overall roadmap readiness remains 49%; bridge credit remains zero.