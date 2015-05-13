import numpy

execfile('transition_matrix.py')
execfile('cutoff.py')

n = 1000
P = line_lazy_transition_matrix(n, 0.51)

print linalg.cond(P)

#plot_mixing(P, random_starting_distribution(P), stationary_distribution(P))

plot_mixing(P, fixed_starting_distribution(P, 0), stationary_distribution(P))