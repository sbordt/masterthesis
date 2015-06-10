import random
import networkx as nx

import cutoff

def generate_ginat_components(ig,n,_lambda,k):
	for igc in range(0,k):
		random.seed( igc*pow(n,2)*int(_lambda) )
		C_1 = cutoff.erdos_renyi_giant_component(n, _lambda/n)
		
		A = nx.to_scipy_sparse_matrix(C_1)
		P = cutoff.adjacency_to_lazy_sparse_transition_matrix(A)
		P = P.transpose()
		N = A.shape[0]

		print "N: "+`N`
		cutoff.save_gc(ig, igc, {'N': N, 'A': A, 'P': P})

	return
		
#generate_ginat_components(0, 100000, 1.1, 3)
#generate_ginat_components(1, 1000000, 1.01, 3)
#generate_ginat_components(2, 100000, 1.05, 3)
#generate_ginat_components(3, 100000, 1.01, 3)

#generate_ginat_components(4,    10000, 1.05, 3)
#generate_ginat_components(5,    20000, 1.05, 3)
#generate_ginat_components(6,    50000, 1.05, 3)
#generate_ginat_components(7,   100000, 1.05, 3)
#generate_ginat_components(8,   200000, 1.05, 3)
#generate_ginat_components(9,   500000, 1.05, 3)
#generate_ginat_components(10, 1000000, 1.05, 3)