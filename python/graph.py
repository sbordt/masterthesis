import os

def graph_create_srw_mat(G,mat_path):
	A = nx.to_scipy_sparse_matrix(G)
	P = adjacency_to_lazy_sparse_transition_matrix(A)
	P = P.transpose()
	N = A.shape[0]

	sio.savemat(mat_path, {'N': N, 'A': A, 'P': P})

def analyze_graph_srw(G):
	# create a temporaray mat file that holds the markov chain for the srw on the graph
	mat_path = tmp_mat_file_path()
	graph_create_srw_mat(G,mat_path)

	# analyze this markv chain
	mat = sio.loadmat(mat_path)
	mat = analyze_markov_chain(mat)

	# remove the temporary file
	os.remove(mat_path)

	return mat

