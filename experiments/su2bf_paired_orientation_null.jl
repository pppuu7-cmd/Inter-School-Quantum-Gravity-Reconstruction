using LinearAlgebra
using Random
using JSON3

root = abspath(get(ENV, "SU2BF_ROOT", "external/su2bf-TNAlgo"))
include(joinpath(root, "src", "partial_coherent_vertex.jl"))
using .partial_coherent_vertex

const NN = [[0.0,0.0,1.0],[0.0,2sqrt(2)/3,-1/3],[sqrt(2/3),-sqrt(2)/3,-1/3],[-sqrt(2/3),-sqrt(2)/3,-1/3]]
permute_normals(nn,p)=[copy(nn[i]) for i in p]
const PSWAP=permute_normals(NN,[2,1,3,4]); const PCYCLE=permute_normals(NN,[2,3,4,1]); const PREVERSE=permute_normals(NN,[4,3,2,1])
function boundary_state(label)
    label=="swap_one" && return [PSWAP,NN,NN]
    label=="cycle_two" && return [PCYCLE,PCYCLE,NN]
    label=="mixed_three" && return [PSWAP,PCYCLE,PREVERSE]
    error("unknown boundary state")
end
vertex(j,nvs)=partial_cohn_vertex2(j .* ones(10),nvs)
function top_basis(a,r)
    e=eigen(Hermitian(a'*a)); idx=sortperm(e.values,rev=true)[1:r]; e.vectors[:,idx]
end
function haar_unitary(n,rng)
    z=randn(rng,ComplexF64,n,n); f=qr(z); q=Matrix(f.Q)
    # QR phases do not matter for Haar subspaces, but normalize diagonal phases for a stable full-unitary draw.
    rr=Matrix(f.R)
    ph=diag(rr); ph=map(x->abs(x)>0 ? x/abs(x) : one(x),ph)
    q*Diagonal(conj.(ph))
end
function metrics(a1,a2,v)
    a1v=a1*v; qa1v=a1v-v*(v'*a1v)
    leak=norm(qa1v)/max(norm(a1v),eps())
    ret=norm(v'*(a2*qa1v))/max(norm(v'*(a2*(a1*v))),eps())
    leak,ret
end
function one_case(j,first,second,nnull,seed)
    train=vertex(j,[NN,NN,NN]); a1=vertex(j,boundary_state(first)); a2=vertex(j,boundary_state(second)); d=size(train,1)
    rng=MersenneTwister(seed); rows=[]
    for r in 1:d-1
        v=top_basis(train,r); pleak,pret=metrics(a1,a2,v)
        nl=Float64[]; nr=Float64[]
        for _ in 1:nnull
            w=haar_unitary(d,rng)
            # Same unitary similarity is applied to both holdout operators. This preserves
            # each singular spectrum and their mutual algebraic relation while destroying
            # their orientation relative to the frozen train-defined physical projector.
            b1=w'*a1*w; b2=w'*a2*w
            x,y=metrics(b1,b2,v); push!(nl,x); push!(nr,y)
        end
        push!(rows,Dict(
            "rank"=>r,"dimension"=>d,"retained_fraction"=>r/d,
            "source_leakage"=>pleak,"source_return"=>pret,
            "null_mean_leakage"=>sum(nl)/length(nl),"null_mean_return"=>sum(nr)/length(nr),
            "leakage_improvement"=>(sum(nl)/length(nl))/max(pleak,eps()),
            "return_improvement"=>(sum(nr)/length(nr))/max(pret,eps()),
            "fraction_null_worse_leakage"=>sum(x->x>pleak,nl)/length(nl),
            "fraction_null_worse_return"=>sum(x->x>pret,nr)/length(nr)))
    end
    Dict("spin"=>j,"first"=>first,"second"=>second,"dimension"=>d,
         "a1_a2_relative_difference"=>norm(a2-a1)/max(norm(a1),eps()),"ranks"=>rows)
end
function main()
    j=parse(Float64,ARGS[1]); first=ARGS[2]; second=ARGS[3]; seed=parse(Int,ARGS[4]); nn=parse(Int,ARGS[5]); outfile=ARGS[6]
    row=one_case(j,first,second,nn,seed)
    out=Dict("test"=>"SU2BF_PAIRED_UNITARY_ORIENTATION_NULL","source_repository"=>"sethkasante/su2bf-TNAlgo","source_commit"=>"2460cda77b8fe27a4106e98bf39a94fa9059bc92","result"=>row,
      "claim_lock"=>"The null applies a shared unitary similarity to both holdout operators, preserving their singular spectra and mutual pair structure while randomizing orientation relative to the frozen train projector. This is a structural-alignment diagnostic; SU(2) BF is not EPRL gravity.")
    mkpath(dirname(outfile)); open(outfile,"w") do io JSON3.pretty(io,out); write(io,"\n") end; JSON3.pretty(stdout,out); println()
end
main()
