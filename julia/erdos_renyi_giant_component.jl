using Graphs
using PyPlot

include("cutoff.jl")

n = 300
lambda = 2

# get the giant component from an erdos renyi graph
function erdos_renyi_giant_component(n::Int64, p::FloatingPoint)
	g = simple_graph(n, is_directed=false)
	g = erdos_renyi_graph(g, n, p)

	# get the largest connected component
	components = connected_components(g)

	ilargest = 1
	size_largest = length(components[1])
	for i in 2:length(components)
		if length(components[i]) > size_largest
			ilargest = i
		end
	end

	# create a new graph
	largest_component = components[ilargest]

	C_1	= simple_graph(length(largest_component))
	

	C_1
end

C_1 = erdos_renyi_giant_component(n, lambda/n)