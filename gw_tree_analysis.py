import networkx as nx
import markovmixing as mkm

import numpy
import matplotlib.pyplot as plt

execfile('graph_util.py')

################################################################
# This code plots a histogram of GW-Tree sizes
################################################################
# nn = []
# N = 100000

# for i in range(0,N):
# 	G = grow_gw_tree(lambda: numpy.random.poisson(0.95, 1))
# 	nn.append(nx.number_of_nodes(G)-1)

# plt.hist(nn, bins=101, range=(0,100))
# plt.show()

################################################################
# This code determines the average waiting time introduced
# for the SRW by appending GW-Tress
################################################################

tao_by_num_offsprings = {}

for i in xrange(100000):
	G = grow_gw_tree(lambda: numpy.random.poisson(0.95, 1))

	while nx.number_of_nodes(G) == 1:
		G = grow_gw_tree(lambda: numpy.random.poisson(0.95, 1))

	# waiting time via Markov chain stationary distribution
	mc = mkm.nx_graph_srw(G)

	if tao_by_num_offsprings.has_key(nx.number_of_nodes(G)) == False:
		tao_by_num_offsprings[nx.number_of_nodes(G)] = []

	tao_by_num_offsprings[nx.number_of_nodes(G)].append(1/mc.get_stationary_distribution()[0,0])
	
for key in tao_by_num_offsprings.keys():
	tao_by_num_offsprings[key] = numpy.mean(tao_by_num_offsprings[key])

print tao_by_num_offsprings
G = nx.cycle_graph(10)


#grow_gw_trees_at_all_nodes(G,lambda: np.random.poisson(0.90, 1))
#mkm.nx_graph_analyze_lazy_srw(G)



# G = grow_gw_tree(lambda: numpy.random.poisson(0.95, 1))

# while nx.number_of_nodes(G) != 10:
# 	G = grow_gw_tree(lambda: numpy.random.poisson(0.95, 1))

# mc = mkm.nx_graph_srw(G)
# print nx.number_of_nodes(G)

# s = mc.get_stationary_distribution()
# print s
# t = 1/(s[0,0])

# # Monte-Carlo estimate of the return time
# taos = []

# for i in xrange(10000):
# 	path = mc.sample_path(0,10)
# 	del path[0]

# 	while not(0 in path):
# 		path_continuation = mc.sample_path(path[-1],10)
# 		del path_continuation[0]
# 		path.extend(path_continuation)

# 	taos.append(path.index(0)+1)

# print taos
# print numpy.mean(taos)
# print t

# show_tree(G)

