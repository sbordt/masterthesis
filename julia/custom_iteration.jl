using MAT
using Base.LinAlg.BLAS

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
@time for i=1:1e4
	dist = dist*P
end
dist = dist'

print(total_variation(dist, stationary))

# custom method 
#=dist = zeros(n)
dist[1] = 1

i = 0
@time while i < 1e5
	dist = iterate_dist_2(dist)

	if i % 1000 == 0
#		println(i)
	end
	i += 1
end

print(total_variation(dist, stationary)) =#

# build specific c function
code = "#include <cblas.h>\n\n"

code = string("$(code)#define GEN_MAT_MUL_N $(n)\n\n")

code = string("$(code)void gen_mat_mul(double* x, double* y)\n")
code = string("$(code){\n")
code = string("$(code)	double tmp[__MAX_NUM_SUMMANDS__];\n")
max_num_summands = 0

for i in 1:n
	# determine the effective number of summands in this column
	num_summands = countnz(P[:,i])	
	max_num_summands = max(num_summands, max_num_summands)

	i_summand = 0	

	for j in 1:n
		if P[j,i] > 0.0005
			code = string("$(code)	tmp[$i_summand] = x[$(j-1)] * $(P[j,i]);\n")

			i_summand = i_summand+1
		end
	end

	code = string("$(code)	y[$(i-1)] = cblas_dasum($num_summands, tmp, 1);\n")
end 

code = string("$(code)}\n")

code = replace(code, "__MAX_NUM_SUMMANDS__", max_num_summands)

f = open("../bin/gen_mat_mul.c", "w")
write(f, code)
close(f)

# compile
run(`make --directory=/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/`)

# performance test
Libdl.dlopen("/opt/OpenBLAS/lib/libopenblas.so", Libdl.RTLD_GLOBAL | Libdl.RTLD_NOW)

dist = zeros(n)
dist[1] = 1

y = zeros(n)

mylib = "/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/gen_mat_mul"

@time for i=1:1e4
	ccall((:gen_mat_mul, :"/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/gen_mat_mul.so"), Void, (Ptr{Float64},Ptr{Float64}), dist, y )
	ccall((:gen_mat_mul, :"/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/gen_mat_mul.so"), Void, (Ptr{Float64},Ptr{Float64}), y, dist )
end

print(total_variation(dist, stationary)) 

#build specific julia function
code = "function gen_mat_mul!(x,y)\n"

code = string("$(code)@inbounds begin\n")
code = string("$(code)	tmp = zeros(__MAX_NUM_SUMMANDS__)\n")
max_num_summands = 0

for i in 1:n
	# determine the effective number of summands in this column
	num_summands = countnz(P[:,i])	
	max_num_summands = max(num_summands, max_num_summands)

	i_summand = 1

	for j in 1:n
		if P[j,i] != 0.0
			code = string("$(code)	tmp[$i_summand] = x[$j] * $(P[j,i])\n")

			i_summand = i_summand+1
		end
	end

	code = string("$(code)	y[$i] = asum($(num_summands), tmp, 1)\n")
end 

code = string("$(code)end\n")
code = string("$(code)end")

code = replace(code, "__MAX_NUM_SUMMANDS__", max_num_summands)

f = open("/home/sbordt/Desktop/gen.jl", "w")
write(f, code)
close(f)

# metaprogramming :)
eval(parse(code))

# performance test
function julia_performance_test()
	dist = zeros(n)
	dist[1] = 1

	y = zeros(n)

	@time for i=1:1e4
		gen_mat_mul!(dist,y)
		gen_mat_mul!(y, dist)
	end

	print(total_variation(dist, stationary)) 
end

julia_performance_test()

