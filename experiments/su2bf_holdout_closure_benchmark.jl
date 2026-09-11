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

function metrics(a, v)
    av = a * v
    pav = v * (v' * av)
    qav = av - pav
    leak_den = norm(av)
    leakage = leak_den > 0 ? norm(qav) / leak_den : 0.0

    num = v' * (a * qav)
    den = v' * (a * (a * v))
    den_norm = norm(den)
    seq = den_norm > 0 ? norm(num) / den_norm : 0.0
    return Dict(
        "leakage" => leakage,
        "sequential_return_defect" => seq,
    )
end

function one_case(j::Float64, holdout::String, nrandom::Int, seed::Int)
    train = vertex(j, [NN, NN, NN])
    d = size(train, 1)
    r = max(1, cld(d, 2))
    vtrain = top_right_singular_basis(train, r)

    p_swap = permute_normals(NN, [2, 1, 3, 4])
    p_cycle = permute_normals(NN, [2, 3, 4, 1])
    p_reverse = permute_normals(NN, [4, 3, 2, 1])

    nvs = if holdout == "swap_one"
        [p_swap, NN, NN]
    elseif holdout == "cycle_two"
        [p_cycle, p_cycle, NN]
    elseif holdout == "mixed_three"
        [p_swap, p_cycle, p_reverse]
    else
        error("unknown holdout $holdout")
    end
    test = vertex(j, nvs)

    spectral = metrics(test, vtrain)
    rng = MersenneTwister(seed)
    randrows = [metrics(test, random_basis(d, r, rng)) for _ in 1:nrandom]
    rleak = [x["leakage"] for x in randrows]
    rseq = [x["sequential_return_defect"] for x in randrows]

    return Dict(
        "spin" => j,
        "holdout" => holdout,
        "dimension" => d,
        "retained_rank" => r,
        "retained_fraction" => r / d,
        "train_frobenius_norm" => norm(train),
        "test_frobenius_norm" => norm(test),
        "train_to_test_relative_difference" => norm(test-train) / max(norm(train), eps()),
        "train_svd_sector" => spectral,
        "random_controls" => Dict(
            "n" => nrandom,
            "mean_leakage" => sum(rleak)/length(rleak),
            "mean_seq_defect" => sum(rseq)/length(rseq),
            "fraction_random_worse_leakage" => sum(x -> x > spectral["leakage"], rleak) / length(rleak),
            "fraction_random_worse_seq" => sum(x -> x > spectral["sequential_return_defect"], rseq) / length(rseq),
        ),
        "improvement" => Dict(
            "random_mean_over_train_sector_leakage" => (sum(rleak)/length(rleak)) / max(spectral["leakage"], eps()),
            "random_mean_over_train_sector_seq" => (sum(rseq)/length(rseq)) / max(spectral["sequential_return_defect"], eps()),
        ),
    )
end

function main()
    j = parse(Float64, ARGS[1])
    holdout = ARGS[2]
    seed = parse(Int, ARGS[3])
    nrandom = parse(Int, ARGS[4])
    outfile = ARGS[5]
    row = one_case(j, holdout, nrandom, seed)
    out = Dict(
        "test" => "SU2BF_SOURCE_NATIVE_HOLDOUT_CLOSURE",
        "source_repository" => "sethkasante/su2bf-TNAlgo",
        "source_commit" => "2460cda77b8fe27a4106e98bf39a94fa9059bc92",
        "result" => row,
        "claim_lock" => (
            "SU(2) BF partial-coherent-vertex holdout test. The retained sector is learned only from the equilateral train vertex; " *
            "closure is evaluated on different boundary coherent data. This is independent spin-foam evidence, not EPRL gravity."
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
