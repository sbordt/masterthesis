import networkx as nx
import scipy.io as sio

import scipy.stats as sst
import pydot

import cutoff, time, numpy, scipy, random
import matplotlib.pyplot as plt

execfile('graph_generation.py')

#n = 1e5
#lam = 1.05

#my = scipy.optimize.brentq(lambda x: x*numpy.exp(-x)-lam*numpy.exp(-lam), 0, 1)

#print my*numpy.exp(-my)
#print lam*numpy.exp(-lam)

#Lam = numpy.random.normal(lam-my,1/n)

#D_u = numpy.random.poisson(Lam, n)

#print D_u

#print random.choice([0,0,2])



#G = nx.path_graph(10)

#G = nx.cycle_graph(200)
#grow_gw_trees_at_all_nodes(G, lambda: numpy.random.poisson(0.95, 1))

#G = grow_gw_tree(lambda: random.choice([1,2]), num_generations = 10)

#nx.draw_graphviz(G)
#plt.show()

#show_graph(G)

n = 1000000
lam = 1.05

G = erdos_renyi_giant_component(n, lam/n)
G_2core = nx.k_core(G,k=2)
G_kernel = graph_kernel(G)

print G.number_of_nodes()
print G_2core.number_of_nodes()
print G_kernel.number_of_nodes()

#for n in G_kernel:
#	edges = nx.edges(G_kernel,nbunch=n)
#	print edges

nx.write_dot(G_kernel,cutoff.tmp_path+'multi_kernel.dot')
#!neato -T png cutoff.tmp_path+'multi.dot' > multi.png

show_graph(G_kernel)

#cutoff.analyze_graph_srw(G_2core)
