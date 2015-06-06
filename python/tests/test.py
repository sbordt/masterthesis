################################################################
# transition_matrix.py
################################################################
execfile('../transition_matrix.py')

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

# uniform_starting_points
x = uniform_starting_point_distributions(10,4)
y = uniform_starting_point_distributions(10,4)

assert (x == y).all()

################################################################
# mc_iterate.py
################################################################
execfile('../mc_iterate.py')

P = line_lazy_transition_matrix(50)
P = P.transpose()
P = P.tocsr()

assert ssp.isspmatrix_csr(P)

x = uniform_starting_point_distributions(50,5)

# load/save/remove P
save_P(P)
P = load_P()
assert ssp.isspmatrix_csr(P)
remove_P()

# load/save/remove x 
save_x(x,0)
x_0 = load_x(0)
save_x(x_0,0)
x_0 = load_x(0)
assert (x_0 == x[:,0]).all()
remove_x(0)


print mc_iterate(P,x,1000)
print mc_iterate(P,x,10000)





















