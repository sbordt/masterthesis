import networkx as nx

def random_starting_distribution(P):
	dist = numpy.zeros(P.shape[1])
	dist[random.randint(0, P.shape[1]-1)] = 1
	return dist

def fixed_starting_distribution(P, n):
	dist = numpy.zeros(P.shape[1])
	dist[n] = 1
	return dist

def stationary_distribution(P):
	return linalg.matrix_power(P, 10 ** 15)[1,:]

def adjacency_to_transition_matrix(adjacency_matrix):
	P = adjacency_matrix.copy()
	N = P.shape[1]

	for irow in range(0,N):
		P[irow,:] = P[irow,:] / P[irow,:].sum()

	return P

def adjacency_to_lazy_transition_matrix(adjacency_matrix):
	return (adjacency_to_transition_matrix(adjacency_matrix) + np.identity(N)) / 2.

def erdos_renyi_giant_component(n,p):
	g = nx.fast_gnp_random_graph(n,p)

	number_of_nodes = 0
	C_1 = 0
	for c in nx.connected_component_subgraphs(g):
		if nx.number_of_nodes(c) > number_of_nodes:
			number_of_nodes = nx.number_of_nodes(c)
			C_1 = c

	return C_1


def ergc_transition_matrix(n,p):
	C_1 = erdos_renyi_giant_component(n,p)

	adjacency_matrix = nx.to_numpy_matrix(C_1)

	P = adjacency_to_transition_matrix(adjacency_matrix)
	return P

def ergc_lazy_transition_matrix(n,p):
	C_1 = erdos_renyi_giant_component(n,p)

	adjacency_matrix = nx.to_numpy_matrix(C_1)

	P = adjacency_to_lazy_transition_matrix(adjacency_matrix)
	return P


# lazy random walk on the line
def line_lazy_transition_matrix(n, p = 0.5):
	P = numpy.zeros((n,n))
	P[0,0] = 0.5
	P[0,1] = 0.5
	P[n-1,n-1] = 0.5
	P[n-1, n-2] = 0.5

	for i in range(1,n-1):
		P[i,i-1] = (1-p)/2
		P[i,i] = 0.5
		P[i,i+1] = p/2

	return P
