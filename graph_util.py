#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" functions to facilitate the generation of graphs with the networkx package
"""
import matplotlib.pyplot as plt

################################################################
# For the giant component of the Erdős–Rényi random graph
################################################################

def erdos_renyi_giant_component(n,p):
	""" Returns the giant component of an Erdős–Rényi random graph.
	"""
	g = nx.fast_gnp_random_graph(n,p)

	number_of_nodes = 0
	C_1 = 0
	for c in nx.connected_component_subgraphs(g):
		if nx.number_of_nodes(c) > number_of_nodes:
			number_of_nodes = nx.number_of_nodes(c)
			C_1 = c

	return C_1

################################################################
# Methods to compose graphs
################################################################

def glue_graphs(G, H, G_node, H_node):
	""" Glue the graphs G and H identifying the nodes G_node and H_node. Keeps the node G_node and
	removes the node H_node.
	"""
	G.add_node(G_node, G_node=0)
	H.add_node(H_node, H_node=0)

	I = nx.disjoint_union(G,H)

	# find the two nodes to identify in I
	node0 = nx.get_node_attributes(I,'G_node').keys()[0]
	node1 = nx.get_node_attributes(I,'H_node').keys()[0]

	# add edges to node0 and remove node1
	for neighbor in nx.all_neighbors(I,node1):
		I.add_edge(node0,neighbor)

	I.remove_node(node1)

	del I.node[node0]['G_node'] 
	del G.node[G_node]['G_node'] 
	del H.node[H_node]['H_node']

	# debug
	#print G.nodes(data=True)
	#print H.nodes(data=True)
	#print I.nodes(data=True)
	return I

def append_graph_to_all_nodes(G, H, H_node):
	""" Append copies of the graph H to all nodes of G. Appends the node H_node of H.
	"""
	nx.set_node_attributes(G, 'original_graph', 0) 
	I = G

	original_nodes = nx.get_node_attributes(I,'original_graph').keys()

	while len(original_nodes) != 0:
		node = original_nodes[0]
		I.add_node(node, appending=0) # add an attribute to identify the node after joining
		I = glue_graphs(I, H, node, H_node)

		node_in_I = nx.get_node_attributes(I,'appending').keys()[0]
		del I.node[node_in_I]['appending']
		del I.node[node_in_I]['original_graph'] 

		# append H to the next node
		original_nodes = nx.get_node_attributes(I,'original_graph').keys()
		
	# debug
	#print I.nodes(data=True)
	return I

################################################################
# Galton-Watson-Trees
################################################################
 
def grow_gw_tree(offspring, n_gen = 1e10, directed = False):
	""" Grow a Galton-Watson tree given an offspring distribution 
	'offspring' up to a maximal number of generations 'n_gen'
	(where the root belongs to generation 0).

	Root of the tree will be the node '0'.

	Every node has the attribute 'generation'. The root has 
	'generation' = 0. 
	
	n_gen: Defaults to 1e10.
	"""
	G = nx.Graph()

	if directed:
		G = nx.DiGraph()

	G.add_node(0, generation=0)

	grow_gw_tree_at_node(G, G.nodes()[0], offspring, n_gen = n_gen)
	return G

def grow_gw_tree_at_node(G, node, offspring, n_gen = 1e10):
	if n_gen == 0:
		return

	for i in range(0, offspring()):
		if G.has_node(G.number_of_nodes()):
			raise Exception('To grow Gw-Trees, nodes should be numbered 0...n')
		G.add_edge(node, G.number_of_nodes())	# automatically adds the node

		# add attribute 'generation' if the parent has this attribute
		generation = nx.get_node_attributes(G, 'generation')

		if generation.has_key(node):
			G.node[G.number_of_nodes()-1]['generation'] = generation[node]+1

		grow_gw_tree_at_node(G, G.nodes()[G.number_of_nodes()-1], offspring, n_gen = n_gen -1)

def grow_gw_trees_at_all_nodes(G, offspring, n_gen = 1e10):
	nodes = G.nodes()

	for n in nodes:
		grow_gw_tree_at_node(G,n,offspring, n_gen = n_gen)

################################################################
# Utilities
################################################################

def graph_kernel(G):
	# remove leaves first
	kernel = nx.MultiGraph(nx.k_core(G,k=2))

	# remove all nodes who have exactly two neighbors and edges
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
	nx.draw(G, pos, with_labels=True, arrows=False)
	plt.show()
