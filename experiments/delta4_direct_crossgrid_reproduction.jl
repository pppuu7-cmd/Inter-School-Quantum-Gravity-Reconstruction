using JLD2
using DelimitedFiles
using Printf

# Cross-grid direct reproduction of the four-vertex Lorentzian EPRL Delta_4
# contraction from stored vertex tensors in PietropaoloFrisoni/HowToSpinFoamAmplitude.
# No source Delta_4 table value participates in the contraction itself; the table
# is read only after contraction for a frozen equality check.

root=ARGS[1]
gamma=parse(Float64,ARGS[2])
j=parse(Float64,ARGS[3])
outfile=ARGS[4]
Dls=[0,5,15]

function csv_reference(root,gamma,j)
    d=joinpath(root,"Delta_4_ampls","Immirzi_$(gamma)","j_$(j)","CSV_format")
    fs=filter(f->endswith(f,".csv") && occursin("Dl_max_",f), readdir(d; join=true))
    isempty(fs) && error("no reference CSV in $d")
    score(f)=parse(Int,match(r"Dl_max_(\d+)\.csv$",f).captures[1])
    return argmax(f->score(f),fs)
end

function contract(root,gamma,j,Dl,ib)
    i_b=ib+1
    vp=joinpath(root,"vertex_ampls","Immirzi_$(gamma)","j_$(j)","Dl_$(Dl)")
    jbmin=iszero(j % 1) ? 0.0 : 0.5
    jbmax=3j
    total=0.0
    for jb in jbmin:1.0:jbmax
        f=joinpath(vp,"j_bulk_$(jb)_fulltensor.jld2")
        isfile(f) || error("missing $f")
        vertex=JLD2.load(f,"vertex")
        D=size(vertex[i_b,:,:,i_b,i_b],1)
        partial=0.0
        @inbounds for i1 in 1:D, i2 in 1:D, i3 in 1:D, i4 in 1:D
            partial += vertex[i_b,i1,i2,i_b,i_b]*vertex[i_b,i2,i3,i_b,i_b]*
                       vertex[i_b,i3,i4,i_b,i_b]*vertex[i_b,i4,i1,i_b,i_b]
        end
        total += (2jb+1)*partial
    end
    return total
end

csv=csv_reference(root,gamma,j)
ref=readdlm(csv)
nchan=size(ref,2)
rows=[]
for Dl in Dls
    Dl+1 <= size(ref,1) || error("reference table too short for Dl=$Dl")
    for ib in 0:nchan-1
        got=contract(root,gamma,j,Dl,ib)
        expected=Float64(ref[Dl+1,ib+1])
        rel=abs(got-expected)/max(abs(expected),1e-300)
        push!(rows,(Dl=Dl,ib=ib,got=got,expected=expected,rel=rel))
        @printf("gamma=%.3g j=%.3g Dl=%d ib=%d got=%.17e expected=%.17e rel=%.3e\n",gamma,j,Dl,ib,got,expected,rel)
    end
end
maxerr=maximum(r.rel for r in rows)
println("N_CHECKS=",length(rows))
println("MAX_RELERR=",maxerr)
maxerr <= 1e-12 || error("cross-grid Delta4 reproduction failed: $maxerr")
open(outfile,"w") do io
    println(io,"gamma\tj\tDl\ti_boundary\tcomputed\treference\trelative_error")
    for r in rows
        println(io,"$(gamma)\t$(j)\t$(r.Dl)\t$(r.ib)\t$(r.got)\t$(r.expected)\t$(r.rel)")
    end
    println(io,"MAX_RELERR\t\t\t\t\t\t$(maxerr)")
end
