import numpy 
import time, os, inspect
import scipy.io as sio
from scipy.sparse import *

execfile('../config.py')
execfile('../transition_matrix.py')
execfile('../mc_iterate.py')

mat = sio.loadmat("../../data/tests/graph.mat")
N = mat['N'][0][0]
A = mat['A']
P = mat['P']
P = P.tocsr()

print N
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

# single distribution
x = numpy.zeros(N)
x[0] = 1
start = time.time()
for i in xrange(k):
	x = P.dot(x)
end = time.time()
print "Python:"
print end - start 
print x

x = numpy.zeros(N)
x[0] = 1
start = time.time()
x = mc_iterate_py(P,x,k)
end = time.time()
print "Python iteration:"
print end - start 
print x

x = numpy.zeros(N)
x[0] = 1
start = time.time()
x = mc_iterate_py_process(P,x,k)
end = time.time()
print "Python process iteration:"
print end - start 
print x

# 10 distributions
k = 10000

x = uniform_starting_point_distributions(N,10)
start = time.time()
x = mc_iterate_py(P,x,k)
end = time.time()
print "Python iteration:"
print end - start 
print x

x = uniform_starting_point_distributions(N,10)
start = time.time()
x = mc_iterate_py_process(P,x,k)
end = time.time()
print "Python process iteration:"
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






