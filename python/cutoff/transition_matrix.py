import networkx as nx
import scipy.sparse as ssp
import scipy.optimize as so
import numpy, random

def random_starting_distribution(P):
	dist = numpy.zeros(P.shape[0])
	dist[random.randint(0, P.shape[0]-1)] = 1
	return dist

def fixed_starting_distribution(P, n):
	dist = numpy.zeros(P.shape[0])
	dist[n] = 1
	return dist

# uniform starting positions: random but the same for the same n
def uniform_starting_point_distributions(n,k):
	random.seed(n)
	x = numpy.zeros((n,k))

	indices = random.sample(xrange(n),k)

	for i in range(0,k):
		x[indices[i],i] = 1

	return x

################################################################
# Adjancency and transition matrices
################################################################
def adjacency_to_transition_matrix(A):
	P = A.copy()
	n = A.shape[0]

	for irow in range(0,n):
		P[irow,:] = P[irow,:] / P[irow,:].sum()

	return P

def adjacency_to_lazy_transition_matrix(A):
	n = A.shape[0]

	return (adjacency_to_transition_matrix(A) + numpy.identity(n)) / 2.

def adjacency_to_sparse_transition_matrix(A):
	(I,J,V) = ssp.find(A)
	n = A.shape[0]

	P = ssp.lil_matrix((n,n))
	nnz = I.shape[0]

	row_start = 0
	while row_start < nnz:
		row = I[row_start]

		# find the end of the row
		row_end = row_start
		while row_end < nnz and I[row_end] == row:
			row_end = row_end+1

		# srw probability
		p = 1. / (row_end-row_start)

		# fill P
		for row_entry in range(row_start, row_end):
			P[row, J[row_entry]] = p

		# continue with the next row
		row_start = row_end

	return P.tocsr()

def adjacency_to_lazy_sparse_transition_matrix(A):
	(I,J,V) = ssp.find(A)
	n = A.shape[0]

	P = ssp.lil_matrix((n,n))
	nnz = I.shape[0]

	row_start = 0
	while row_start < nnz:
		row = I[row_start]

		# find the end of the row
		row_end = row_start
		while row_end < nnz and I[row_end] == row:
			row_end = row_end+1

		# lazy srw probability
		p = 0.5 / (row_end-row_start)

		# fill P
		for row_entry in range(row_start, row_end):
			P[row, J[row_entry]] = p

		P[row,row] = 0.5

		# continue with the next row
		row_start = row_end

	return P.tocsr()