import numpy 
import scipy.io as sio
import scipy.sparse as ssp
import time

execfile('transition_matrix.py')
execfile('cutoff.py')

mat = sio.loadmat("../data/giant_components/gc_0.mat")

N = mat['N'][0][0]
P = mat['P']
 
print N

x = numpy.zeros(N)
x[0] = 1

num_steps = 1000
step_length = 20000

for i_step in range(0,num_steps):
	# iterate 
	for i in range(0,step_length):
	 	x = P.dot(x)

	# print & save
	print "Step " + `i_step` + " completed."
	print x[0]
	print x[N-1]

	sio.savemat("../data/step_" + `i_step` + ".mat", {'x': x})

