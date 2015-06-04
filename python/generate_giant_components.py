import numpy 
import random
import scipy.io as sio
import scipy.sparse as ssp
import time

execfile('transition_matrix.py')

n = 10
_lambda = 1.1

for i_gc in range(0,1):
	random.seed(i_gc)
	C_1 = erdos_renyi_giant_component(n, _lambda/n)
	
	A = nx.to_scipy_sparse_matrix(C_1)
	P = adjacency_to_lazy_sparse_transition_matrix(A)
	P = P.transpose()
	N = A.shape[0]

	sio.savemat("../data/giant_components/gc_" + `i_gc` + ".mat", {'N': N, 'A': A, 'P': P})
	print P

	print N