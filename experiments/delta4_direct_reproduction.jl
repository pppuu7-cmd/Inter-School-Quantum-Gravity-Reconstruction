using JLD2
using DelimitedFiles
using LinearAlgebra
using Printf

# Direct reproduction of the contraction published in
# PietropaoloFrisoni/HowToSpinFoamAmplitude, VertexContraction.ipynb.
# We deliberately use only stored vertex tensors; sl2cfoam-next is not needed.

root = ARGS[1]
gamma = 1.2
j = 1.0
Dls = [0, 5, 15]

function delta4_contract(root, gamma, j, Dl, i_boundary)
    i_b = i_boundary + 1
    vertex_path = joinpath(root, "vertex_ampls", "Immirzi_$(gamma)", "j_$(j)", "Dl_$(Dl)")
    amp = 0.0
    j_bulk_min = iszero(j % 1) ? 0.0 : 0.5
    j_bulk_max = 3j
    for j_bulk in j_bulk_min:1.0:j_bulk_max
        f = joinpath(vertex_path, "j_bulk_$(j_bulk)_fulltensor.jld2")
        isfile(f) || error("missing vertex tensor $f")
        vertex = JLD2.load(f, "vertex")
        D = size(vertex[i_b, :, :, i_b, i_b], 1)
        partial = 0.0
        @inbounds for i1 in 1:D, i2 in 1:D, i3 in 1:D, i4 in 1:D
            partial += vertex[i_b,i1,i2,i_b,i_b] * vertex[i_b,i2,i3,i_b,i_b] *
                       vertex[i_b,i3,i4,i_b,i_b] * vertex[i_b,i4,i1,i_b,i_b]
        end
        amp += (2j_bulk + 1) * partial
    end
    return amp
end

csv = joinpath(root, "Delta_4_ampls", "Immirzi_$(gamma)", "j_$(j)", "CSV_format", "Delta_4_ampls_Dl_max_25.csv")
ref = readdlm(csv)
results = []
for Dl in Dls
    for i_boundary in 0:2
        got = delta4_contract(root, gamma, j, Dl, i_boundary)
        expected = Float64(ref[Dl+1, i_boundary+1])
        relerr = abs(got-expected) / max(abs(expected), 1e-300)
        push!(results, (Dl=Dl, i_boundary=i_boundary, got=got, expected=expected, relerr=relerr))
        @printf("Dl=%d i=%d got=%.17e expected=%.17e relerr=%.3e\n", Dl, i_boundary, got, expected, relerr)
    end
end

maxerr = maximum(r.relerr for r in results)
println("MAX_RELERR=", maxerr)
maxerr <= 1e-12 || error("direct Delta4 reproduction failed tolerance: $maxerr")

# Machine-readable TSV artifact without adding a JSON package dependency.
out = ARGS[2]
open(out, "w") do io
    println(io, "Dl\ti_boundary\tcomputed\treference\trelative_error")
    for r in results
        println(io, "$(r.Dl)\t$(r.i_boundary)\t$(r.got)\t$(r.expected)\t$(r.relerr)")
    end
    println(io, "MAX_RELERR\t\t\t\t$(maxerr)")
end
