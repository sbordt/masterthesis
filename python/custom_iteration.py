import numpy 
import random
import scipy.io as sio

execfile('transition_matrix.py')
execfile('cutoff.py')

n = 100

P = line_lazy_transition_matrix(n, 0.50)
stationary = stationary_distribution(P)

def get_transition_matrix_row(i):
	return P[:,i]

def iterate_dist(dist):
	iteration = numpy.empty(n)

	for irow in range(0,n):
		iteration[irow] = numpy.dot(dist, get_transition_matrix_row(irow))
	
	return iteration

dist = numpy.zeros(n)
dist[0] = 1

i = 0
while i < 1e5:
	dist = iterate_dist(dist)
	if i % 1000 == 0:
		print(i)
	i += 1

print(total_variation(dist, stationary))