import networkx as nx

import cutoff

for ig in xrange(4):
	for igc in xrange(3):
		mat = cutoff.load_gc(ig, igc)

		if cutoff.get_num_iteration_steps(mat) == 0:
			mat = cutoff.analyze_markov_chain(mat)

			cutoff.save_gc(ig, igc, mat)

#for ig in xrange(4):
#	for igc in xrange(3):
#		mat = cutoff.load_gc(ig, igc)

#		cutoff.plot_mixing(mat)






#G = nx.complete_graph(100)

#mat = cutoff.analyze_graph_srw(G)

#print cutoff.get_iteration_steps(mat)
#print cutoff.get_stationary_distribution(mat)

#cutoff.plot_mixing(mat)

