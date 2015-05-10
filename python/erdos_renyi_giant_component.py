import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv
import numpy as np
from numpy import linalg
import scipy.io as sio

_lambda = 1.5
n = 1000

def erdos_renyi_giant_component(n,p):
	g = nx.erdos_renyi_graph(n,p)

	number_of_nodes = 0
	C_1 = 0
	for c in nx.connected_component_subgraphs(g):
		if nx.number_of_nodes(c) > number_of_nodes:
			number_of_nodes = nx.number_of_nodes(c)
			C_1 = c

	return C_1

C_1 = erdos_renyi_giant_component(n,_lambda/n)

print nx.number_of_nodes(C_1)


nx.draw_spectral(C_1)

P = nx.to_numpy_matrix(C_1)

linalg.matrix_power(P, 10)

sio.savemat("/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/matrix.mat", {'matrix': P})
# nx.write_gml(C_1, "/home/sbordt/Desktop/giant_component.gml")