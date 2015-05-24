import numpy 
import scipy.io as sio
import scipy.sparse as ssp
import time

execfile('../transition_matrix.py')
execfile('../cutoff.py')

mat = sio.loadmat("../../data/giant_components/gc_0.mat")

N = mat['N'][0][0]
P = mat['P']
 
print N

# matlab takes the same time for this
k = 10000
P = P.transpose()

x = numpy.zeros(N)
x[0] = 1

start = time.time()
for i in range(0,k):
	x = P.dot(x)

end = time.time()
print end - start

print x[0]
print x[1]






