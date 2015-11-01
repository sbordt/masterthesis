import random
import networkx as nx

import markovmixing as mkm

execfile('graph_util.py')

def generate_ginat_components(ig,n,_lambda,k):
	for igc in range(0,k):
		random.seed( igc*pow(n,2)*int(_lambda*1e5) )
		C_1 = erdos_renyi_giant_component(n, _lambda/n)
		
		A = nx.to_scipy_sparse_matrix(C_1)
		P = mkm.adjacency_to_lazy_srw_sparse_transition_matrix(A)
		P = P.transpose()
		N = A.shape[0]

		print "N: "+`N`
		#cutoff.save_gc(ig, igc, {'N': N, 'A': A, 'P': P})
	return

# current matherthesis_data content
#k = 3

# generate_ginat_components(101,  100000, 1.001, k) 
# generate_ginat_components(102,  500000, 1.001, k) 
# generate_ginat_components(103, 1000000, 1.001, k) 
# generate_ginat_components(104, 2000000, 1.001, k) # ca 7616 ...

# generate_ginat_components(201,  100000, 1.005, k) 
# generate_ginat_components(202,  500000, 1.005, k) 
# generate_ginat_components(203, 1000000, 1.005, k) 
# generate_ginat_components(204, 2000000, 1.005, k) # ca 32253 ...

# generate_ginat_components(301,  100000, 1.01, k) 
# generate_ginat_components(302,  500000, 1.01, k) 
# generate_ginat_components(303, 1000000, 1.01, k) 
# generate_ginat_components(304, 2000000, 1.01, k) # ca 27659 ...	

# generate_ginat_components(401,  100000, 1.05, k)
# generate_ginat_components(402,  500000, 1.05, k)
# generate_ginat_components(403, 1000000, 1.05, k)
# generate_ginat_components(404, 2000000, 1.05, k) # ca 187729 ...

# generate_ginat_components(501,  100000, 1.1, k)
# generate_ginat_components(502,  500000, 1.1, k)
# generate_ginat_components(503, 1000000, 1.1, k)
# generate_ginat_components(504, 2000000, 1.1, k) # ca 351704 ...

# generate_ginat_components(601,  100000, 1.15, k)
# generate_ginat_components(602,  500000, 1.15, k)
# generate_ginat_components(603, 1000000, 1.15, k) # ca 250512 ...

# generate_ginat_components(701,  100000, 1.2, k)
# generate_ginat_components(702,  500000, 1.2, k) # ca 155700 ...



