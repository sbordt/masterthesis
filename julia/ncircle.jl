using PyPlot

n = 301

function total_varation(mu, nu)
	sum(abs(nu-mu))/2
end

function n_circle_transition_matrix(n::Int64)
	P = zeros(n,n)
	P[1,2] = 0.5
	P[1,n] = 0.5
	P[n,1] = 0.5
	P[n, n-1] = 0.5

	for i in 2:n-1
		P[i,i-1] = 0.5
		P[i,i+1] = 0.5
	end
	P
end

A = n_circle_transition_matrix(n)

distribution = zeros(1,n)
distribution[1] = 1

limit_distribution = ones(1,n)/n

# plot 
tic()
step = 5
A_step = A^step

x = 1:step:100000
x = x'
y = zeros(1,length(x))

for i in 1:length(y)
	y[i] = total_varation(distribution, limit_distribution)
	distribution = distribution*A_step
end

plot(x', y')
title("Distance in total variation")
toc()
