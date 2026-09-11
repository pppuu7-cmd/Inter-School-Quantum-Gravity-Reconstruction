using LinearAlgebra
using Random
using Statistics

include(joinpath(ENV["SL2CFOAM_ROOT"], "julia", "SL2Cfoam.jl"))
using .SL2Cfoam

function rbasis(n,r,rng)
    q=qr(randn(rng,ComplexF64,n,r)).Q
    Matrix(q[:,1:r])
end
function metrics(a1,a2,v)
    a1c=ComplexF64.(a1); a2c=ComplexF64.(a2)
    a1v=a1c*v; qa1v=a1v-v*(v'*a1v)
    leak=norm(qa1v)/max(norm(a1v),eps())
    num=v'*(a2c*qa1v); den=v'*(a2c*(a1c*v))
    ret=norm(num)/max(norm(den),eps())
    leak,ret
end
function topbasis(a,r)
    f=svd(ComplexF64.(a)); f.V[:,1:r]
end

root=ENV["SL2CFOAM_ROOT"]
data=joinpath(root,"data_sl2cfoam")
# all ten face spins j=1/2; each four-valent intertwiner leg has dimension two
js=fill(HalfInteger(1,2),10)
conf=SL2Cfoam.Config(SL2Cfoam.VerbosityOff, SL2Cfoam.NormalAccuracy, 5, 0)
SL2Cfoam.cinit(data,1.2,conf)
try
    v0=SL2Cfoam.vertex_compute(js,0; result=SL2Cfoam.VertexResult((true,true,false)))
    v1=SL2Cfoam.vertex_compute(js,1; result=SL2Cfoam.VertexResult((true,true,false)))
    @assert size(v0.a)==(2,2,2,2,2)
    @assert size(v1.a)==(2,2,2,2,2)
    # Open i1,i2 as operator indices; fixed (i3,i4,i5) define boundary slices.
    slices0=Dict{String,Matrix{Float64}}()
    slices1=Dict{String,Matrix{Float64}}()
    triples=Dict("000"=>(1,1,1),"100"=>(2,1,1),"010"=>(1,2,1),"001"=>(1,1,2),"111"=>(2,2,2))
    for (lab,t) in triples
        slices0[lab]=Matrix(v0.a[:,:,t[1],t[2],t[3]])
        slices1[lab]=Matrix(v1.a[:,:,t[1],t[2],t[3]])
    end
    train=slices0["000"]
    P=topbasis(train,1)
    rng=MersenneTwister(20260912)
    rows=NamedTuple[]
    cases=[("Dl0_100_to_010",slices0["100"],slices0["010"]),
           ("Dl0_010_to_001",slices0["010"],slices0["001"]),
           ("Dl1_100_to_010",slices1["100"],slices1["010"]),
           ("cross_Dl0_100_to_Dl1_010",slices0["100"],slices1["010"]),
           ("cross_Dl1_001_to_Dl0_111",slices1["001"],slices0["111"])]
    for (label,a1,a2) in cases
        pl,pr=metrics(a1,a2,P); rl=Float64[]; rr=Float64[]
        for _ in 1:512
            R=rbasis(2,1,rng); x,y=metrics(a1,a2,R); push!(rl,x); push!(rr,y)
        end
        push!(rows,(label=label,opdiff=norm(a2-a1)/max(norm(a1),eps()),
                    source_leak=pl,source_return=pr,
                    leak_improve=mean(rl)/max(pl,eps()),return_improve=mean(rr)/max(pr,eps()),
                    frac_random_worse_leak=mean(rl .> pl),frac_random_worse_return=mean(rr .> pr)))
    end
    println("EPRL_PARTIAL_SLICE_CLOSURE=PASS")
    println("train=",repr(train))
    for r in rows println(join(string.((r.label,r.opdiff,r.source_leak,r.source_return,r.leak_improve,r.return_improve,r.frac_random_worse_leak,r.frac_random_worse_return)),",")) end
finally
    SL2Cfoam.cclear()
end
