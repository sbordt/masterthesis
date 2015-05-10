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

@time line_lazy_transition_matrix(100)^1e12
@time line_lazy_transition_matrix(300)^1e12
@time line_lazy_transition_matrix(500)^1e12
@time line_lazy_transition_matrix(800)^1e12
@time line_lazy_transition_matrix(1000)^1e12
@time line_lazy_transition_matrix(2000)^1e12