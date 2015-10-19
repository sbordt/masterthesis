import networkx as nx
import scipy.io as sio

import cutoff, time

# add all markov chains to a list
mcl = []

for ig in xrange(1000):
	for igc in xrange(100):
		if cutoff.has_gc(ig,igc):
			mat = cutoff.load_gc(ig, igc)

			mcl.append( cutoff.gc_file_path(ig,igc) )

# sort by N
decorated = [(cutoff.get_N(sio.loadmat(path)), path) for path in mcl]
decorated.sort()
mcl = [path for N, path in decorated]

# analyze
for mc in mcl: 		
	print mc

	mat = sio.loadmat(mc)

	if cutoff.get_num_iteration_steps(mat) == 0:
		mat = cutoff.analyze_markov_chain(mat)
		sio.savemat(mc,mat)

# plot mixing
for mc in mcl:		
	print mc
	mat = sio.loadmat(mc)
	cutoff.plot_mixing(mat)

#G = nx.complete_graph(100)

#mat = cutoff.analyze_graph_srw(G)

#print cutoff.get_iteration_steps(mat)
#print cutoff.get_stationary_distribution(mat)

#cutoff.plot_mixing(mat)

