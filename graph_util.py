#!/usr/bin/env python
# -*- coding: utf-8 -*-

# functions to facilitate the generation of graphs with the networkx package
import matplotlib.pyplot as plt

################################################################
# For the giant component of the Erdős–Rényi random graph
################################################################

def erdos_renyi_giant_component(n,p):
	g = nx.fast_gnp_random_graph(n,p)

	number_of_nodes = 0
	C_1 = 0
	for c in nx.connected_component_subgraphs(g):
		if nx.number_of_nodes(c) > number_of_nodes:
			number_of_nodes = nx.number_of_nodes(c)
			C_1 = c

	return C_1

#def ergc_contiguous_model(n,p):
	#so.brentq(lambda x: x*)



def ergc_transition_matrix(n,p):
	C_1 = erdos_renyi_giant_component(n,p)

	A = nx.to_numpy_matrix(C_1)

	return cutoff.adjacency_to_transition_matrix(A)

def ergc_lazy_transition_matrix(n,p):
	C_1 = erdos_renyi_giant_component(n,p)

	A = nx.to_numpy_matrix(C_1)

	return cutoff.adjacency_to_lazy_transition_matrix(A)

def ergc_sparse_transition_matrix(n,p):
	C_1 = erdos_renyi_giant_component(n,p)

	A = nx.to_scipy_sparse_matrix(C_1)

	return cutoff.adjacency_to_sparse_transition_matrix(A)


################################################################
# Galton-Watson-Trees
################################################################

# grow a galton-watson-tree given an offspring distribution an a maximal number of generations (where the root belongs to generation 0)
def grow_gw_tree(offspring, num_generations = 1e10):
	G = nx.Graph()
	G.add_node(1)

	grow_gw_tree_at_node(G, G.nodes()[0], offspring, num_generations = num_generations)
	return G

def grow_gw_tree_at_node(G, node, offspring, num_generations = 1e10):
	if num_generations == 0:
		return

	for i in range(0, offspring()):
		if G.has_node(G.number_of_nodes()+1):
			raise Exception('Node already exists.')
		G.add_edge(node, G.number_of_nodes()+1)	# automatically adds the node

		grow_gw_tree_at_node(G, G.nodes()[G.number_of_nodes()-1], offspring, num_generations = num_generations -1)

def grow_gw_trees_at_all_nodes(G, offspring, num_generations = 1e10):
	nodes = G.nodes()

	for n in nodes:
		grow_gw_tree_at_node(G,n,offspring, num_generations = num_generations)

################################################################
# Utilities
################################################################

def graph_kernel(G):
	# remove leaves first
	kernel = nx.MultiGraph(nx.k_core(G,k=2))

	# remove all nodes who have exactly tho neighbors and edges
	for n in nx.nodes(kernel):
		neighbors = list(nx.all_neighbors(kernel,n))
		edges = nx.edges(kernel,nbunch=n)

		if len(neighbors) == 2 and len(edges) == 2:
			kernel.add_edge(neighbors[0],neighbors[1])
			kernel.remove_node(n)

	return kernel

def show_graph(G):
	pos = nx.graphviz_layout(G, prog='neato')
	nx.draw(G, pos, with_labels=False, arrows=False)
	plt.show()

def show_tree(G):
	pos = nx.graphviz_layout(G, prog='dot')
	nx.draw(G, pos, with_labels=False, arrows=False)
	plt.show()
