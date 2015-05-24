#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import scipy.sparse as ssp

def random_starting_distribution(P):
	dist = numpy.zeros(P.shape[0])
	dist[random.randint(0, P.shape[0]-1)] = 1
	return dist

def fixed_starting_distribution(P, n):
	dist = numpy.zeros(P.shape[0])
	dist[n] = 1
	return dist

def stationary_distribution(P):
	return linalg.matrix_power(P, 10 ** 15)[1,:]

################################################################
# Adjancency and transition matrices
################################################################

def adjacency_to_transition_matrix(A):
	P = A.copy()
	N = A.shape[0]

	for irow in range(0,N):
		P[irow,:] = P[irow,:] / P[irow,:].sum()

	return P

def adjacency_to_lazy_transition_matrix(A):
	N = A.shape[0]

	return (adjacency_to_transition_matrix(A) + numpy.identity(N)) / 2.

def adjacency_to_sparse_transition_matrix(A):
	(I,J,V) = ssp.find(A)
	N = A.shape[0]

	P = ssp.lil_matrix((N,N))
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
	N = A.shape[0]

	P = ssp.lil_matrix((N,N))
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

################################################################
# For the giant component of the Erdős–Rényi random graph
################################################################

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

	A = nx.to_numpy_matrix(C_1)

	return adjacency_to_transition_matrix(A)

def ergc_lazy_transition_matrix(n,p):
	C_1 = erdos_renyi_giant_component(n,p)

	A = nx.to_numpy_matrix(C_1)

	return adjacency_to_lazy_transition_matrix(A)

def ergc_sparse_transition_matrix(n,p):
	C_1 = erdos_renyi_giant_component(n,p)

	A = nx.to_scipy_sparse_matrix(C_1)

	return adjacency_to_sparse_transition_matrix(A)

################################################################
# Random walk on the line
################################################################

def line_adjacency_matrix(n):
	A = numpy.zeros((n,n))
	A[0,1] = 1
	A[n-1,n-2] = 1

	for i in range(1,n-1):
		A[i,i-1] = 1
		A[i,i+1] = 1

	return A

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
