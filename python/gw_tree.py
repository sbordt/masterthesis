import networkx as nx

import cutoff, numpy
import matplotlib.pyplot as plt

execfile('graph_generation.py')

nn = []
N = 100000

for i in range(0,N):
	G = grow_gw_tree(lambda: numpy.random.poisson(0.95, 1))
	nn.append(nx.number_of_nodes(G)-1)

plt.hist(nn, bins=101, range=(0,100))
plt.show()