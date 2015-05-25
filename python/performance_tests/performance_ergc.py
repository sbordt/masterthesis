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

# 22 seconds. matlab takes the same time for this
k = 2000

x = numpy.zeros(N)
x[0] = 1

start = time.time()
for i in range(0,k):
	x = P.dot(x)

end = time.time()
print "%(a)f seconds taken." % {'a': (end - start)}

#for i in range(0,N):
#	print x[i]

print x[0]
print x[N-1]


execfile('../ccode.py')

prog = cprog_matrix_vector_product(P) 





