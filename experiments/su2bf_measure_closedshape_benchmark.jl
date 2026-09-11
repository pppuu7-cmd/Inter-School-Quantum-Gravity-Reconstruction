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

# A one-parameter family of four unit normals with exact equal-area closure.
# This deliberately changes the coherent shape rather than merely permuting
# the regular-tetrahedron normals.
function closed_shape(theta)
    s, c = sin(theta), cos(theta)
    n = [
        [ s, 0.0,  c],
        [-s, 0.0,  c],
        [0.0,  s, -c],
        [0.0, -s, -c],
    ]
    closure = reduce(+, n)
    maximum(abs.(closure)) < 1e-12 || error("closure failure")
    all(abs(norm(x)-1) < 1e-12 for x in n) || error("unit-normal failure")
    return n
end

const SHAPE_A = closed_shape(0.92)
const SHAPE_B = closed_shape(1.02)
const SHAPE_C = closed_shape(1.12)
const SHAPE_D = closed_shape(0.82)

function boundary_state(label::String)
    if label == "shape_a"
        return [SHAPE_A, NN, NN]
    elseif label == "shape_b"
        return [NN, SHAPE_B, NN]
    elseif label == "shape_c"
        return [SHAPE_C, SHAPE_B, NN]
    elseif label == "shape_d"
        return [SHAPE_D, NN, SHAPE_A]
    else
        error("unknown boundary state $label")
    end
end

vertex(j, nvs) = partial_cohn_vertex2(j .* ones(10), nvs)

function top_right_singular_basis(a, r)
    e = eigen(Hermitian(a' * a))
    idx = sortperm(e.values, rev=true)[1:r]
    return e.vectors[:, idx]
end

function random_basis(n, r, rng)
    z = randn(rng, ComplexF64, n, r)
    q = qr(z).Q
    return Matrix(q[:,1:r])
end

function canonicalize(a, j)
    n = size(a,1)
    ilabels = collect(0.0:1.0:(2j))
    length(ilabels) == n || error("intertwiner dimension mismatch")
    Dhalf = Diagonal(sqrt.(2 .* ilabels .+ 1))
    return Dhalf * a * Dhalf
end

function metrics(a1, a2, v)
    a1v = a1*v
    pa1v = v*(v'*a1v)
    qa1v = a1v-pa1v
    leak = norm(qa1v)/max(norm(a1v),eps())
    num = v'*(a2*qa1v)
    den = v'*(a2*(a1*v))
    ret = norm(num)/max(norm(den),eps())
    return leak, ret
end

function main()
    j=parse(Float64,ARGS[1]); first=ARGS[2]; second=ARGS[3]
    seed=parse(Int,ARGS[4]); nrandom=parse(Int,ARGS[5]); outfile=ARGS[6]

    train=canonicalize(vertex(j,[NN,NN,NN]),j)
    a1=canonicalize(vertex(j,boundary_state(first)),j)
    a2=canonicalize(vertex(j,boundary_state(second)),j)
    d=size(train,1); r=max(1,cld(d,2))
    v=top_right_singular_basis(train,r)
    pleak,pret=metrics(a1,a2,v)

    rng=MersenneTwister(seed)
    leaks=Float64[]; rets=Float64[]
    for _ in 1:nrandom
        vr=random_basis(d,r,rng)
        l,x=metrics(a1,a2,vr)
        push!(leaks,l); push!(rets,x)
    end

    out=Dict(
        "test"=>"SU2BF_MEASURE_CORRECTED_CLOSED_SHAPE_HETEROGENEOUS",
        "source_repository"=>"sethkasante/su2bf-TNAlgo",
        "source_commit"=>"2460cda77b8fe27a4106e98bf39a94fa9059bc92",
        "spin"=>j,"first"=>first,"second"=>second,
        "dimension"=>d,"retained_rank"=>r,
        "a1_a2_relative_difference"=>norm(a2-a1)/max(norm(a1),eps()),
        "train_a1_relative_difference"=>norm(a1-train)/max(norm(train),eps()),
        "train_a2_relative_difference"=>norm(a2-train)/max(norm(train),eps()),
        "train_sector"=>Dict("leakage"=>pleak,"return_defect"=>pret),
        "random_controls"=>Dict(
            "n"=>nrandom,
            "mean_leakage"=>sum(leaks)/length(leaks),
            "mean_return"=>sum(rets)/length(rets),
            "median_leakage"=>sort(leaks)[cld(length(leaks),2)],
            "median_return"=>sort(rets)[cld(length(rets),2)],
            "fraction_random_worse_leakage"=>sum(x->x>pleak,leaks)/length(leaks),
            "fraction_random_worse_return"=>sum(x->x>pret,rets)/length(rets),
        ),
        "claim_lock"=>(
            "Closure-preserving equal-area coherent-shape deformation test in source-native SU(2) BF with edge measure. " *
            "The deformed normal sets are not asserted to be a complete Regge-geometric family."
        )
    )
    mkpath(dirname(outfile))
    open(outfile,"w") do io JSON3.pretty(io,out); write(io,"\n") end
    JSON3.pretty(stdout,out); println()
end

main()
