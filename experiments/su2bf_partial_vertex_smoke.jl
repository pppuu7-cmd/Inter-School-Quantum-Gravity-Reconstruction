using LinearAlgebra
using JSON3

root = get(ENV, "SU2BF_ROOT", "external/su2bf-TNAlgo")
include(joinpath(root, "src", "partial_coherent_vertex.jl"))
using .partial_coherent_vertex

# Boundary normals copied from the source repository's equilateral example.
nn = [
    [0.0, 0.0, 1.0],
    [0.0, 2sqrt(2)/3, -1/3],
    [sqrt(2/3), -sqrt(2)/3, -1/3],
    [-sqrt(2/3), -sqrt(2)/3, -1/3],
]

function one_case(j)
    jays = j .* ones(10)
    amp = partial_cohn_vertex2(jays, [nn, nn, nn])
    s = svdvals(amp)
    return Dict(
        "spin" => j,
        "shape" => collect(size(amp)),
        "frobenius_norm" => norm(amp),
        "max_abs" => maximum(abs.(amp)),
        "singular_values" => collect(s),
        "numerical_rank_1e12" => count(x -> x > maximum(s)*1e-12, s),
    )
end

rows = [one_case(j) for j in (0.5, 1.0, 1.5)]
out = Dict(
    "test" => "SU2BF_PARTIAL_COHERENT_VERTEX_SOURCE_NATIVE_SMOKE",
    "source_repository" => "sethkasante/su2bf-TNAlgo",
    "source_commit" => "2460cda77b8fe27a4106e98bf39a94fa9059bc92",
    "cases" => rows,
    "claim_lock" => "Execution smoke test only; SU(2) BF is an independent spin-foam realization, not EPRL gravity.",
)
mkpath("compute_out")
open("compute_out/su2bf_partial_vertex_smoke.json", "w") do io
    JSON3.pretty(io, out)
    write(io, "\n")
end
JSON3.pretty(stdout, out)
println()
