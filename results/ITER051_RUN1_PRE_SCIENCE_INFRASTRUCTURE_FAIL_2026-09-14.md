# ITER051 run 1 — pre-science infrastructure failure

Date: 2026-09-14

Workflow run: `34817480937` at head `2ef1af5e6906dbd94d9adc052a86eb1309dce3a1`.

Classification: **INFRASTRUCTURE_FAIL_PRE_SCIENCE — OUTPUT_PATH_ORCHESTRATION_ONLY**.

The `build-runtime` job reached the exact pinned backend checkout and successfully transported `wigxjpf-1.13.tar.gz`. It then stopped at the first archive-hash evidence write because, after `cd work/backend/ext`, the workflow addressed the repository-root evidence directory as `../../out`; the correct relative path is `../../../out`.

The log shows the downloaded archive SHA256 before termination:

`90ab9bfd495978ad1fdcbb436e274d6f4586184ae290b99920e5c978d64b3e6a  wigxjpf-1.13.tar.gz`

No wigxjpf compilation, fastwigxj compilation, table generation, backend build, vertex evaluation, scientific output or substantive predicate was reached. Stage-B checks were skipped.

Allowed repair: change only relative paths that address the evidence/output directory. Do not change backend SHA, dependency versions, build flags, table parameters, smoke configuration, reproducibility tolerance, PASS/FAIL/BLOCKED/INVALID criteria, or interpretation ceiling. The original ITER051 preregistration remains authoritative and unchanged.