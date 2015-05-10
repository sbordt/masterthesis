using MAT
#using PyPlot

#include("cutoff.jl")

file = matopen("/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/matrix.mat")
P = read(file, "matrix")
close(file)

