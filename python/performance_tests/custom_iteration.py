import numpy 
import random
import scipy.io as sio

random.seed(1) 

execfile('transition_matrix.py')
execfile('cutoff.py')

n = 100000
_lambda = 1.1

C_1 = erdos_renyi_giant_component(n, _lambda/n)



sparse_matrix = nx.to_scipy_sparse_matrix(C_1)


print ssp.isspmatrix_csr(sparse_matrix)
print sparse_matrix.data
print sparse_matrix.indices
print sparse_matrix.indptr

def crs_sparse_adjacency_to_transition_matrix(A):
	N = A.shape[1]
	P = ssp.lil_matrix((N,N))

	row_sums = A.sum(1)

	irow = 0
	while irow < N-1:
		for j in range(A.indptr[irow], A.indptr[irow+1]):
			P[irow, A.indices[j]] = 1.0 / row_sums[irow, 0]

		irow = irow+1	

	for j in range(A.indptr[N-1], A.data.shape[0]):
			P[irow, A.indices[j]] = 1.0 / row_sums[irow, 0]

	return P.tocsc()

def crs_sparse_adjacency_to_transition_matrix(A):
	N = A.shape[1]
	P = ssp.lil_matrix((N,N))

	row_sums = A.sum(1)

	irow = 0
	while irow < N-1:
		for j in range(A.indptr[irow], A.indptr[irow+1]):
			P[irow, A.indices[j]] = 1.0 / row_sums[irow, 0]

		irow = irow+1	

	for j in range(A.indptr[N-1], A.data.shape[0]):
			P[irow, A.indices[j]] = 1.0 / row_sums[irow, 0]

	return P.tocsc()


P = crs_sparse_adjacency_to_transition_matrix(sparse_matrix)

print P

#sio.savemat("/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/sparse.mat", {'matrix': sparse_matrix})



