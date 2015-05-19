using MAT

include("cutoff.jl")

file = matopen("/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/line_lazy_transition_matrix.mat")
P = read(file, "matrix")
stationary = read(file, "stationary")
close(file)

println(stationary)

