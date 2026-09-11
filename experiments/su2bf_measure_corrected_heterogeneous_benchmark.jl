using LinearAlgebra
using Random
using JSON3

root = abspath(get(ENV, "SU2BF_ROOT", "external/su2bf-TNAlgo"))
include(joinpath(root, "src", "partial_coherent_vertex.jl"))
using .partial_coherent_vertex

const NN = [
    [0.0, 0.0, 1.0],
    [0.0, 2sqrt(2)/3, -1/3],
    [sqrt(2/3), -sqrt(2)/3, -1/3],
    [-sqrt(2/3), -sqrt(2)/3, -1/3],
]

function permute_normals(nn, perm)
    return [copy(nn[i]) for i in perm]
end

const PSWAP = permute_normals(NN, [2, 1, 3, 4])
const PCYCLE = permute_normals(NN, [2, 3, 4, 1])
const PREVERSE = permute_normals(NN, [4, 3, 2, 1])

function boundary_state(label::String)
    if label == "swap_one"
        return [PSWAP, NN, NN]
    elseif label == "cycle_two"
        return [PCYCLE, PCYCLE, NN]
    elseif label == "mixed_three"
        return [PSWAP, PCYCLE, PREVERSE]
    else
        error("unknown boundary state $label")
    end
end

function vertex(j, nvs)
    return partial_cohn_vertex2(j .* ones(10), nvs)
end

function top_right_singular_basis(a, r)
    h = Hermitian(a' * a)
    e = eigen(h)
    idx = sortperm(e.values, rev=true)[1:r]
    return e.vectors[:, idx]
end

function random_basis(n, r, rng)
    z = randn(rng, ComplexF64, n, r)
    q = qr(z).Q
    return Matrix(q[:, 1:r])
end

function canonicalize_with_edge_measure(a, j)
    # For equal spins j, the bulk intertwiner range is i = 0,1,...,2j.
    # SU(2) BF edge amplitude/measure is d_i = 2i+1.
    n = size(a, 1)
    ilabels = collect(0.0:1.0:(2j))
    length(ilabels) == n || error("intertwiner dimension mismatch: n=$n labels=$(length(ilabels))")
    weights = 2 .* ilabels .+ 1
    s = Diagonal(sqrt.(weights))
    return s * a * s, weights
end

function heterogeneous_metrics(a1, a2, v)
    a1v = a1 * v
    pa1v = v * (v' * a1v)
    qa1v = a1v - pa1v

    leak_den = norm(a1v)
    leakage1 = leak_den > 0 ? norm(qa1v) / leak_den : 0.0

    num = v' * (a2 * qa1v)
    den = v' * (a2 * (a1 * v))
    den_norm = norm(den)
    return_defect = den_norm > 0 ? norm(num) / den_norm : 0.0

    return Dict(
        "first_step_leakage" => leakage1,
        "heterogeneous_return_defect" => return_defect,
    )
end

function subspace_overlap(v1, v2)
    r = min(size(v1,2), size(v2,2))
    return real(norm(v1' * v2)^2) / r
end

function one_case(j::Float64, first::String, second::String, nrandom::Int, seed::Int)
    train_raw = vertex(j, [NN, NN, NN])
    a1_raw = vertex(j, boundary_state(first))
    a2_raw = vertex(j, boundary_state(second))

    train, weights = canonicalize_with_edge_measure(train_raw, j)
    a1, _ = canonicalize_with_edge_measure(a1_raw, j)
    a2, _ = canonicalize_with_edge_measure(a2_raw, j)

    d = size(train, 1)
    r = max(1, cld(d, 2))
    vtrain = top_right_singular_basis(train, r)
    vtrain_raw = top_right_singular_basis(train_raw, r)

    physical = heterogeneous_metrics(a1, a2, vtrain)
    raw_reference = heterogeneous_metrics(a1_raw, a2_raw, vtrain_raw)

    rng = MersenneTwister(seed)
    randrows = [heterogeneous_metrics(a1, a2, random_basis(d, r, rng)) for _ in 1:nrandom]
    rleak = [x["first_step_leakage"] for x in randrows]
    rret = [x["heterogeneous_return_defect"] for x in randrows]

    return Dict(
        "spin" => j,
        "first" => first,
        "second" => second,
        "dimension" => d,
        "retained_rank" => r,
        "retained_fraction" => r/d,
        "edge_weights" => weights,
        "canonicalization" => "A_tilde = sqrt(D) A sqrt(D), D_ii = 2 i + 1",
        "a1_a2_relative_difference_weighted" => norm(a2-a1) / max(norm(a1), eps()),
        "train_a1_relative_difference_weighted" => norm(a1-train) / max(norm(train), eps()),
        "train_a2_relative_difference_weighted" => norm(a2-train) / max(norm(train), eps()),
        "weighted_vs_unweighted_train_sector_overlap" => subspace_overlap(vtrain, vtrain_raw),
        "weighted_train_sector" => physical,
        "unweighted_reference_train_sector" => raw_reference,
        "random_controls" => Dict(
            "n" => nrandom,
            "mean_first_step_leakage" => sum(rleak)/length(rleak),
            "mean_heterogeneous_return_defect" => sum(rret)/length(rret),
            "fraction_random_worse_leakage" => sum(x -> x > physical["first_step_leakage"], rleak) / length(rleak),
            "fraction_random_worse_return" => sum(x -> x > physical["heterogeneous_return_defect"], rret) / length(rret),
        ),
        "improvement" => Dict(
            "random_mean_over_weighted_train_leakage" => (sum(rleak)/length(rleak)) / max(physical["first_step_leakage"], eps()),
            "random_mean_over_weighted_train_return" => (sum(rret)/length(rret)) / max(physical["heterogeneous_return_defect"], eps()),
        ),
    )
end

function main()
    j = parse(Float64, ARGS[1])
    first = ARGS[2]
    second = ARGS[3]
    seed = parse(Int, ARGS[4])
    nrandom = parse(Int, ARGS[5])
    outfile = ARGS[6]

    row = one_case(j, first, second, nrandom, seed)
    out = Dict(
        "test" => "SU2BF_MEASURE_CORRECTED_HETEROGENEOUS_BH001_COMPOSITION",
        "source_repository" => "sethkasante/su2bf-TNAlgo",
        "source_commit" => "2460cda77b8fe27a4106e98bf39a94fa9059bc92",
        "result" => row,
        "claim_lock" => (
            "Source-native SU(2) BF edge-measure-corrected heterogeneous test. " *
            "Canonicalization uses sqrt(D) A sqrt(D), with D_ii = 2i+1, so products contain the physical internal edge weight. " *
            "This remains SU(2) BF, not EPRL quantum gravity."
        ),
    )

    mkpath(dirname(outfile))
    open(outfile, "w") do io
        JSON3.pretty(io, out)
        write(io, "\n")
    end
    JSON3.pretty(stdout, out)
    println()
end

main()
