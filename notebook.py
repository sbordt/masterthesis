#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import markovmixing as mkm
import numpy as np
import random

execfile('graph_util.py')

################ Generate and save some graphs ################

random.seed(0)

# G = erdos_renyi_giant_component(5000000,1.05/5000000)
# print nx.number_of_nodes(G)

# G_2core = nx.k_core(G,k=2)
# print nx.number_of_nodes(G_2core)

# nx.write_sparse6(G_2core, '/home/sbordt/Desktop/masterthesis_data/ergc_2core_1.s6')

random.seed(1)

# G = erdos_renyi_giant_component(5000000,1.1/5000000)
# print nx.number_of_nodes(G)

# G_2core = nx.k_core(G,k=2)
# print nx.number_of_nodes(G_2core)

# nx.write_sparse6(G_2core, '/home/sbordt/Desktop/masterthesis_data/ergc_2core_2.s6')

################ Mixing on the 100-cycle ################

G = nx.cycle_graph(100)

mc = mkm.nx_graph_lazy_srw(G)
mc.add_random_delta_distributions(1)
mc.compute_tv_mixing()

#plot the mixing
# mc.plot_tv_mixing(0)

# convergence video
mc.convergence_video('/home/sbordt/Desktop/cycle_lazy_100.avi', 0, 60)	

################ Mixing of the random walk on the 101-cycle ################

n = 101
mc = mkm.MarkovChain(mkm.circle_transition_matrix(n,0.9,lazy=False))
mc.set_stationary(mkm.uniform_distribution(n))
mc.add_random_delta_distributions(1)
mc.compute_tv_mixing()

mc.convergence_video('/home/sbordt/Desktop/cycle_biased_101.avi', 0, 60)


################ Mixing on the 100-cycle with appended binary trees ################

# G = append_graph_to_all_nodes(nx.cycle_graph(100), nx.balanced_tree(3,2), 0)
# #show_graph(G)

# mc = mkm.nx_graph_lazy_srw(G)
# mc.add_random_delta_distributions(1)
# mc.compute_tv_mixing()

# # plot the mixing
# mc.plot_tv_mixing(0)

################ Mixing on the 100-cycle with appended Poi-GW-Trees ################

# np.random.seed(0)

# G = nx.cycle_graph(100)
# grow_gw_trees_at_all_nodes(G, lambda: np.random.poisson(0.95, 1))

# mc = mkm.nx_graph_lazy_srw(G)
# mc.add_random_delta_distributions(1)
# mc.compute_tv_mixing()

# # plot the mixing
# mc.plot_tv_mixing(0)

################ Mixing on the 2-core of the giant component of an Erdős–Rényi random graph ################

# G = nx.read_sparse6('/home/sbordt/Desktop/masterthesis_data/ergc_2core_2.s6')

# mc = mkm.nx_graph_srw(G)
# mc.add_random_delta_distributions(1)
# mc.compute_tv_mixing()

# # plot the mixing
# mc.plot_tv_mixing(0)

################ Mixing on a GW-Tree ################

# np.random.seed(0)

# G = grow_gw_tree(lambda: np.random.poisson(1.05, 1), num_generations = 100)
# while nx.number_of_nodes(G) < 100:
# 	G = grow_gw_tree(lambda: np.random.poisson(1.05, 1), num_generations = 100)

# #show_tree(G)

# mc = mkm.nx_graph_lazy_srw(G)
# mc.add_distributions(mkm.delta_distribution(mc.get_n(),0))
# mc.compute_tv_mixing()

# # plot the mixing
# mc.plot_tv_mixing(0)

################ lazy biased random walk on the line ################

mc = mkm.MarkovChain(mkm.line_lazy_transition_matrix(100, p=0.51))
mc.add_random_delta_distributions(1)
mc.compute_tv_mixing()

mc.convergence_video('/home/sbordt/Desktop/line_biased.avi', 0, 60)