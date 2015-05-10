using PyPlot

include("cutoff.jl")

n = 1000

# lazy random walk on the line
function line_lazy_transition_matrix(n::Int64, p::FloatingPoint = 0.5)
	P = zeros(n,n)
	P[1,1] = 0.5
	P[1,2] = 0.5
	P[n,n] = 0.5
	P[n, n-1] = 0.5

	for i in 2:n-1
		P[i,i-1] = (1-p)/2
		P[i,i] = 0.5
		P[i,i+1] = p/2
	end
	P
end

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
