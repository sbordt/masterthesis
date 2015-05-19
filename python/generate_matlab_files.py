import numpy 
import random
import scipy.io as sio

execfile('transition_matrix.py')
execfile('cutoff.py')

n = 50
P = line_lazy_transition_matrix(n, 0.50)

sio.savemat("/home/sbordt/Dropbox/Masterarbeit/masterthesis/bin/line_lazy_transition_matrix.mat", {'matrix': P, 'stationary': stationary_distribution(P)})