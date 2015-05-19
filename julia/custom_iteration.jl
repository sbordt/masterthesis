using MAT

include("cutoff.jl")

file = matopen("/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/line_lazy_transition_matrix.mat")
P = read(file, "matrix")
stationary = read(file, "stationary")'
close(file)

n = length(stationary)

function get_transition_matrix_col(i)
	return P[:,i]
end

function get_transition_matrix(x,y)
	return P[x,y]
end

function iterate_dist(dist)
	iteration = zeros(n)

	for icol in 1:n
		iteration[icol] = (dist'*get_transition_matrix_col(icol))[1]
	end

	return iteration
end

function iterate_dist_2(dist)
	iteration = zeros(n)
	intermediate_term = zeros(n)

	for icol in 1:n
		for irow in 1:n
			intermediate_term[irow] = dist[irow]*get_transition_matrix(irow, icol)
		end

		iteration[icol] = sum(intermediate_term)
	end

	return iteration
end

# native matrix multiplication
dist = zeros(n)
dist[1] = 1
dist = dist'

i = 0
@time while i < 1e5
	dist = dist*P

	if i % 1000 == 0
#		println(i)
	end
	i += 1
end
dist = dist'

print(total_variation(dist, stationary))

# custom method 
dist = zeros(n)
dist[1] = 1

i = 0
@time while i < 1e5
	dist = iterate_dist_2(dist)

	if i % 1000 == 0
#		println(i)
	end
	i += 1
end

print(total_variation(dist, stationary))

