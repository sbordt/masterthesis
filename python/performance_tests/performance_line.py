import numpy 
import time
import scipy.io as sio
from scipy.sparse import *

execfile('../transition_matrix.py')
execfile('../cutoff.py')

n = 10000
k = 100000

P = line_lazy_transition_matrix(n)
P_csr = csr_matrix(P)

# matlab takes 5.5 seconds
sio.savemat("../../data/sparse.mat", {'matrix': P_csr})

# dense matrix multiplication
# start = time.time()
# x = fixed_starting_distribution(P, 0)
# for i in range(1,k):
# 	x = numpy.dot(x, P)

# end = time.time()
# print end - start

# print x

# sparse matrix multiplication
P_csr = P_csr.transpose()

start = time.time()
x = fixed_starting_distribution(P, 0)
for i in range(1,k):
	x = P_csr.dot(x)

end = time.time()
print end - start

print x





