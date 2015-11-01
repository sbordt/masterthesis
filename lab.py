import scipy.sparse as ssp
import networkx as nx
import markovmixing as mkm
import numpy as np
import time, random

execfile('graph_util.py')

G = nx.path_graph(10)
A = nx.to_scipy_sparse_matrix(G)

#show_graph(glue_graphs(nx.cycle_graph(5), nx.cycle_graph(10), 1,1))
show_graph(append_graph_to_all_nodes(nx.cycle_graph(5), nx.path_graph(4),0))


#grow_gw_trees_at_all_nodes(G,lambda: np.random.poisson(0.90, 1))
#mkm.nx_graph_analyze_lazy_srw(G)

#G_di = nx.DiGraph(G)
#print G_di
#print nx.number_of_nodes(G_di)
#print nx.number_of_edges(G_di)




#P = mkm.lazy(mkm.graph_srw_transition_matrix(A))
#mc = mkm.MarkovChain(P)
#mc.set_stationary_distribution(mkm.graph_srw_stationary_distribution(A))




#print mc.get_stationary_distribution()

# random.seed(1)
# n = 5000000
# C1 = erdos_renyi_giant_component(n,1.1/n)
# print nx.number_of_nodes(C1)
# C1_2core = nx.k_core(C1,k=2)
# print nx.number_of_nodes(C1_2core)
# nx.write_sparse6(C1_2core, '/home/sbordt/Desktop/masterthesis_data/ergc_2core_3.s6')

# C1_2core = nx.read_sparse6('/home/sbordt/Desktop/masterthesis_data/ergc_2core_3.s6')

# mkm.nx_graph_analyze_lazy_srw(C1_2core)













#G = nx.cycle_graph(200)
#grow_gw_trees_at_all_nodes(G, lambda: numpy.random.poisson(0.95, 1))

#G = grow_gw_tree(lambda: random.choice([1,2]), num_generations = 10)

#nx.draw_graphviz(G)
#plt.show()

#show_graph(G)

#n = 1000000
#lam = 1.05

#G = erdos_renyi_giant_component(n, lam/n)
#G_2core = nx.k_core(G,k=2)
#G_kernel = graph_kernel(G)

#print G.number_of_nodes()
#print G_2core.number_of_nodes()
#print G_kernel.number_of_nodes()

#for n in G_kernel:
#	edges = nx.edges(G_kernel,nbunch=n)
#	print edges

#nx.write_dot(G_kernel,cutoff.tmp_path+'multi_kernel.dot')
#!neato -T png cutoff.tmp_path+'multi.dot' > multi.png

#show_graph(G_kernel)

#cutoff.analyze_graph_srw(G_2core)


#G = nx.read_sparse6("/home/sbordt/Dropbox/Masterarbeit/masterthesis/data/3_regular_2.s6")
#print G.number_of_nodes()

#cutoff.analyze_graph_srw(G)