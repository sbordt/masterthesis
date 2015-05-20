#using MAT

include("cutoff.jl")
include("transition_matrix.jl")

file = matopen("/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/line_lazy_transition_matrix.mat")
P = read(file, "matrix")
stationary = read(file, "stationary")'
close(file)

n = 10

