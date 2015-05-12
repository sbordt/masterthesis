import numpy

execfile('cutoff.py')

# lazy random walk on the line
def line_lazy_transition_matrix(n, p = 0.5):
	P = numpy.zeros((n,n))
	P[0,0] = 0.5
	P[0,1] = 0.5
	P[n-1,n-1] = 0.5
	P[n-1, n-2] = 0.5

	for i in range(1,n-1):
		P[i,i-1] = (1-p)/2
		P[i,i] = 0.5
		P[i,i+1] = p/2

	return P

n = 1000
P = line_lazy_transition_matrix(n, 0.51)

print linalg.cond(P)

#plot_mixing(P, random_starting_distribution(P), stationary_distribution(P))

plot_mixing(P, fixed_starting_distribution(P, 0), stationary_distribution(P))