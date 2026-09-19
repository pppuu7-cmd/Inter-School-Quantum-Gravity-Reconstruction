#!/usr/bin/env julia
# RC001 Lorentzian EPRL source-acquisition helper.
#
# NON-SCIENTIFIC / NON-ITERATION.
# Reads one immutable five-index EPRL vertex tensor from the public
# Frisoni-Gozzini-Vidotto graph-refinement repository and evaluates the exact
# coarse single-4-simplex diagonal dihedral-angle moments.
#
# Usage:
#   julia rc001_eprl_coarse_vertex_angle_binding.jl <vertex_j=X.jld2> <j>
#
# Expected published tensor provenance (to be checked outside this script):
# external repo head 8a722eb81b7e4c6f4eba75fe76ec7c89d334b53b
# IMMIRZI=1.2, SHELLS=20.

using JLD2
using Printf
using Statistics

length(ARGS) == 2 || error("usage: script <vertex_j=X.jld2> <j>")
path = ARGS[1]
j = parse(Float64, ARGS[2])

@load path vertex
ndims(vertex) == 5 || error("expected rank-5 vertex tensor, got ndims=$(ndims(vertex))")

D = size(vertex, 1)
all(size(vertex, k) == D for k in 1:5) || error("vertex tensor is not D^5")
expected_D = round(Int, 2j + 1)
D == expected_D || error("tensor dimension D=$D incompatible with j=$j (expected $expected_D)")

maximum(abs.(imag.(complex.(vertex)))) <= 1e-13 ||
    error("published coarse binding expects effectively real vertex tensor")

A = Float64.(real.(vertex))
angles = [
    (i * (i + 1) - 2j * (j + 1)) / (2j * (j + 1))
    for i in 0:(D - 1)
]

Z = sum(abs2, A)
isfinite(Z) && Z > 0 || error("nonpositive/nonfinite normalization Z=$Z")

means = zeros(Float64, 5)
seconds = zeros(Float64, 5)

for I in CartesianIndices(A)
    w = abs2(A[I])
    @inbounds for node in 1:5
        x = angles[I[node]]
        means[node] += w * x
        seconds[node] += w * x * x
    end
end

means ./= Z
seconds ./= Z
spreads = sqrt.(max.(seconds .- means .^ 2, 0.0))

symmetry_max_abs = maximum(abs.(means .- mean(means)))
regular_tetrahedron_cos = -1 / 3
mean_all_nodes = mean(means)
regular_abs_deviation = abs(mean_all_nodes - regular_tetrahedron_cos)

println("RC001_EPRL_COARSE_VERTEX_ANGLE_BINDING")
@printf("j=%.6g\n", j)
println("tensor_path=", path)
println("tensor_dims=", size(A))
@printf("Z=%.17g\n", Z)
println("node_means=", means)
println("node_spreads=", spreads)
@printf("mean_all_nodes=%.17g\n", mean_all_nodes)
@printf("symmetry_max_abs=%.17g\n", symmetry_max_abs)
@printf("regular_tetrahedron_cos=%.17g\n", regular_tetrahedron_cos)
@printf("regular_abs_deviation=%.17g\n", regular_abs_deviation)
println("claim_lock=SOURCE_ACQUISITION_ONLY_NOT_A_REFINEMENT_RESULT")
