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

G = nx.cycle_graph(200)
grow_gw_trees_at_all_nodes(G, lambda: numpy.random.poisson(0.95, 1))

#G = grow_gw_tree(lambda: random.choice([1,2]), num_generations = 10)

#nx.draw_graphviz(G)
#plt.show()

#show_graph(G)

cutoff.analyze_graph_srw(G)
