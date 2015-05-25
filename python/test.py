import numpy 
import random
import scipy.io as sio

execfile('transition_matrix.py')

# Test for SRW on the line
A = line_adjacency_matrix(5)
#print A

P = adjacency_to_transition_matrix(A)
P_sparse = adjacency_to_sparse_transition_matrix(A)

assert (P == P_sparse.toarray()).all()

# Test for SRW on a giant component
C_1 = erdos_renyi_giant_component(50, 1.1/100)

A = nx.to_numpy_matrix(C_1)
P = adjacency_to_transition_matrix(A) 

A_sparse = nx.to_scipy_sparse_matrix(C_1)
P_sparse = adjacency_to_sparse_transition_matrix(A_sparse)

assert (P == P_sparse.toarray()).all()

# lazy version
P = adjacency_to_lazy_transition_matrix(A)
P_sparse = adjacency_to_lazy_sparse_transition_matrix(A_sparse)

assert (P == P_sparse.toarray()).all()

# Test C code generation
execfile('ccode.py')

P = line_lazy_transition_matrix(25)
P = P.transpose()
code = ccode_matrix_vector_product(P)
print code

prog = cprog_matrix_vector_product(P) 