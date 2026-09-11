using LinearAlgebra
using Random
using JSON3

root = abspath(get(ENV, "SL2CFOAM_ROOT", "external/sl2cfoam-next"))
include(joinpath(root, "julia", "SL2Cfoam.jl"))
using .SL2Cfoam

const NN = [
    [0.0, 0.0, 1.0],
    [0.0, 2sqrt(2)/3, -1/3],
    [sqrt(2/3), -sqrt(2)/3, -1/3],
    [-sqrt(2/3), -sqrt(2)/3, -1/3],
]

# Exact equal-area closure family, deliberately distinct from permutations.
function closed_shape(theta)
    s, c = sin(theta), cos(theta)
    n = [
        [ s, 0.0,  c],
        [-s, 0.0,  c],
        [0.0,  s, -c],
        [0.0, -s, -c],
    ]
    norm(reduce(+, n)) < 1e-12 || error("shape closure failure")
    all(abs(norm(v)-1) < 1e-12 for v in n) || error("shape normalization failure")
    n
end

const SHAPES = Dict(
    "regular" => NN,
    "shape_a" => closed_shape(0.92),
    "shape_b" => closed_shape(1.02),
    "shape_c" => closed_shape(1.12),
    "shape_d" => closed_shape(0.82),
)

function angles(normals)
    out = zeros(Float64, 4, 2)
    for a in 1:4
        x,y,z = normals[a]
        out[a,1] = acos(clamp(z,-1.0,1.0))
        out[a,2] = atan(y,x)
    end
    out
end

function coherent(j, label)
    js4 = [j,j,j,j]
    SL2Cfoam.coherentstate_compute(js4, angles(SHAPES[label]))
end

# The official SL2Cfoam Julia wrapper stores vertex dimensions as
# (i5,i4,i3,i2,i1) and contracts coherent states from the leftmost index.
# Therefore contracting cs5,cs4,cs3 returns a matrix with dimensions (i2,i1).
function partial_operator(vertex, j, labels::NTuple{3,String})
    cs5 = coherent(j, labels[1])
    cs4 = coherent(j, labels[2])
    cs3 = coherent(j, labels[3])
    A = Matrix{ComplexF64}(SL2Cfoam.contract(vertex, cs5, cs4, cs3))
    A
end

function top_right_basis(A, r)
    F = svd(A)
    F.V[:,1:r], F.S
end

function random_basis(n,r,rng)
    z = randn(rng, ComplexF64, n, r)
    Matrix(qr(z).Q)[:,1:r]
end

function metrics(A1,A2,V)
    A1V = A1*V
    PA1V = V*(V'*A1V)
    QA1V = A1V-PA1V
    leak = norm(QA1V)/max(norm(A1V),eps())
    num = V'*(A2*QA1V)
    den = V'*(A2*(A1*V))
    ret = norm(num)/max(norm(den),eps())
    (leak,ret)
end

function main()
    gamma = parse(Float64, ARGS[1])
    Dl = parse(Int, ARGS[2])
    seed = parse(Int, ARGS[3])
    nrandom = parse(Int, ARGS[4])
    outfile = ARGS[5]

    # Integer j=1 gives a 3-dimensional intertwiner space on every tetrahedron.
    # This avoids a 2x2 near-trivial test while keeping the first EPRL campaign cheap.
    j = 1
    js = fill(j,10)
    data_root = joinpath(root,"data_sl2cfoam")
    conf = SL2Cfoam.Config(SL2Cfoam.VerbosityOff, SL2Cfoam.NormalAccuracy, 6, 0)
    SL2Cfoam.cinit(data_root, gamma, conf)

    vr = SL2Cfoam.VertexResult((true,false,false))
    vertex = SL2Cfoam.vertex_compute(js, Dl; result=vr)
    size(vertex.a) == (3,3,3,3,3) || error("unexpected vertex dimensions $(size(vertex.a))")

    configs = Dict(
        "train" => ("regular","regular","regular"),
        "a" => ("shape_a","regular","regular"),
        "b" => ("regular","shape_b","regular"),
        "c" => ("shape_c","shape_b","regular"),
        "d" => ("shape_d","regular","shape_a"),
    )
    ops = Dict(k => partial_operator(vertex,j,v) for (k,v) in configs)

    train = ops["train"]
    V,S = top_right_basis(train,2)
    rank_train = count(x -> x > maximum(S)*1e-12, S)
    norm(train) > 0 || error("zero EPRL partial operator")
    rank_train >= 2 || error("EPRL partial operator rank too small: $rank_train")
    all(isfinite, real.(train)) || error("non-finite real matrix entries")
    all(isfinite, imag.(train)) || error("non-finite imaginary matrix entries")

    rng = MersenneTwister(seed)
    rows=[]
    names=["a","b","c","d"]
    for first in names, second in names
        first == second && continue
        A1=ops[first]; A2=ops[second]
        pl,pr = metrics(A1,A2,V)
        rleak=Float64[]; rret=Float64[]
        for _ in 1:nrandom
            Vr=random_basis(3,2,rng)
            l,r=metrics(A1,A2,Vr)
            push!(rleak,l); push!(rret,r)
        end
        push!(rows,Dict(
            "first"=>first,"second"=>second,
            "a1_a2_relative_difference"=>norm(A2-A1)/max(norm(A1),eps()),
            "train_sector"=>Dict("leakage"=>pl,"return_defect"=>pr),
            "random_controls"=>Dict(
                "n"=>nrandom,
                "mean_leakage"=>sum(rleak)/length(rleak),
                "mean_return"=>sum(rret)/length(rret),
                "fraction_random_worse_leakage"=>sum(x->x>pl,rleak)/length(rleak),
                "fraction_random_worse_return"=>sum(x->x>pr,rret)/length(rret),
            )
        ))
    end

    opdiag=Dict{String,Any}()
    for (k,A) in ops
        ss=svdvals(A)
        opdiag[k]=Dict(
            "frobenius_norm"=>norm(A),
            "singular_values"=>collect(ss),
            "numerical_rank"=>count(x->x>maximum(ss)*1e-12,ss),
            "relative_to_train"=>norm(A-train)/max(norm(train),eps()),
        )
    end

    out=Dict(
        "test"=>"LORENTZIAN_EPRL_PARTIAL_OPERATOR_HETEROGENEOUS_RETURN",
        "source_repository"=>"qg-cpt-marseille/sl2cfoam-next",
        "source_commit"=>"052e4346028870bd76f69a3034e6cae8defb8f7f",
        "spin_j"=>j,"gamma"=>gamma,"Dl"=>Dl,
        "vertex_dimensions"=>collect(size(vertex.a)),
        "partial_operator_dimensions"=>collect(size(train)),
        "train_singular_values"=>collect(S),
        "train_numerical_rank"=>rank_train,
        "operator_diagnostics"=>opdiag,
        "rows"=>rows,
        "summary"=>Dict(
            "n_ordered_pairs"=>length(rows),
            "mean_fraction_random_worse_return"=>sum(r["random_controls"]["fraction_random_worse_return"] for r in rows)/length(rows),
            "mean_fraction_random_worse_leakage"=>sum(r["random_controls"]["fraction_random_worse_leakage"] for r in rows)/length(rows),
            "mean_relative_operator_difference"=>sum(r["a1_a2_relative_difference"] for r in rows)/length(rows),
        ),
        "claim_lock"=>(
            "Source-native Lorentzian EPRL vertex and Livine-Speziale coherent-state contraction. " *
            "The retained sector is SVD-defined from a regular-boundary train operator, not an independently physical coarse-graining sector. " *
            "Ordinary composition identifies equal-spin i2 and i1 intertwiner Hilbert spaces; a separate gluing-convention audit is required before a strong multi-vertex physical claim."
        )
    )

    mkpath(dirname(outfile))
    open(outfile,"w") do io
        JSON3.pretty(io,out); write(io,"\n")
    end
    JSON3.pretty(stdout,out); println()
    SL2Cfoam.cclear()
end

main()
