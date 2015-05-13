import matplotlib.pyplot as plt
import pygraphviz as pgv
import numpy as np
from numpy import linalg
import scipy.io as sio

execfile('transition_matrix.py')
execfile('cutoff.py')

_lambda = 1.05
n = 20000

# setup for the RW and stationary distribution
P = ergc_transition_matrix(n,_lambda/n)

N = P.shape[1]

# plot distance in total variation from an arbitrary starting point
print N

plot_mixing(P, random_starting_distribution(P), stationary_distribution(P))

#print linalg.cond(P)
#print linalg.cond(linalg.matrix_power(P, 10000))

#x = np.arange(1, 1e8, 10000)
#y = np.zeros(x.size)
#P_step = linalg.matrix_power(P, 10000)
#
#for idx, val in enumerate(x):
#	y[idx] = total_variation(distr, limit)
#	distr =  distr*P
	
 
#plt.plot(x, y)
#plt.ylabel("Distance in total variation")
#plt.show()



# sio.savemat("/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/matrix.mat", {'matrix': P})
# nx.write_gml(C_1, "/home/sbordt/Desktop/giant_component.gml")
