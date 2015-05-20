using PyPlot

include("cutoff.jl")
include("transition_matrix.jl")

n = 1000

A = line_lazy_transition_matrix(n, 0.50)

distribution = zeros(1,n)
distribution[1] = 1

#determine the limit
limit_distribution = (A^1e15)[1,:]

# plot 
tic()
step = 1000
A_step = A^step

x = 1:step:200000
x = x'
y = zeros(1,length(x))

for i in 1:length(y)
	y[i] = total_varation(distribution, limit_distribution)
	distribution = distribution*A_step
end

plot(x', y')
title("Distance in total variation")
toc()
