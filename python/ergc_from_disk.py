import numpy 
import random
import scipy.io as sio

execfile('transition_matrix.py')
execfile('cutoff.py')

_lambda = 1.3
n = 20000

path = '/media/sbordt/LINUXSHARE/masterthesis_data/' 

def ergc_generate_P ():
	P = ergc_transition_matrix(n,_lambda/n)
	print P.shape[1]

	for i in range(0,24):
		numpy.save(path + 'P_' + `i` + '.npy', P)
		P = numpy.dot(P,P)

	return

def load_P_n (n):
	return numpy.load(path + 'P_' + `n` + '.npy')

#random.seed(1)  # 10236 vertices
#random.seed(2)  # 2742 vertices
random.seed(4)   
ergc_generate_P()



P_23 = load_P_n(23)	
print P_23.shape[1]

initial = fixed_starting_distribution(P_23, 100)
stationary = P_23[1,:]

print total_variation(numpy.dot(initial, P_23), stationary)

_plot_mixing(load_P_n, initial, stationary)