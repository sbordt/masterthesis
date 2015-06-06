import numpy 
import time, os, inspect
import scipy.io as sio
from scipy.sparse import *

execfile('../transition_matrix.py')
#execfile('../cutoff.py')

execfile('../mc_iterate.py')

mat = sio.loadmat("../../data/tests/graph.mat")
N = mat['N'][0][0]
A = mat['A']
P = mat['P']

print N

x = numpy.zeros(N)
x[0] = 1

#x = numpy.zeros((N,5))
#x[0,0] = 1
#x[0,1] = 1
#x[0,2] = 1
#x[0,3] = 1
#x[0,4] = 1

sio.savemat("../../data/tests/x.mat", {'x': x})

k = 10000

# matlab takes 5.5 seconds
#sio.savemat("../../data/sparse.mat", {'matrix': P_csr})

# dense matrix multiplication
# start = time.time()
# x = fixed_starting_distribution(P, 0)
# for i in range(1,k):
# 	x = numpy.dot(x, P)

# end = time.time()
# print end - start

# print x

# sparse matrix multiplication in python
P = P.tocsr()
start = time.time()

for i in xrange(k):
	x = P.dot(x)

end = time.time()
print "Python:"
print end - start 

print x

# using an external c application
#base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#
#start = time.time()
#
#fsparse = os.path.abspath(base_path+"/../../data/tests/graph.mat")
#fdense = os.path.abspath(base_path+"/../../data/tests/x.mat")
#fout = os.path.abspath(base_path+"/../../data/tests/output.mat")
#
#citeration(	fsparse, "P", fdense, "x", "%d" % k, fout )
#
#end = time.time()
#print "C:"
#print end - start 






