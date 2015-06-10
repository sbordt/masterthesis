import numpy
import scipy.sparse as ssp
import os, inspect, subprocess
import scipy.io as sio
from multiprocessing import Pool

def load_P():
	mat = sio.loadmat(tmp_path+"P.mat")
	return mat['P'].tocsr()

def save_P(P):
	sio.savemat(tmp_path+"P.mat", {'P': P})
	return

def remove_P():
	os.remove(tmp_path+"P.mat")
	return

def load_x(i):
	mat = sio.loadmat(tmp_path+"x_"+`i`+".mat")
	return mat['x'][0]

def save_x(x,i):
	# handle both vector and matrix inputs
	if x.ndim == 1:
		sio.savemat(tmp_path+"x_"+`i`+".mat", {'x': x})	
	else:
		sio.savemat(tmp_path+"x_"+`i`+".mat", {'x': x[:,i]})
	return 

def remove_x(i):
	os.remove(tmp_path+"x_"+`i`+".mat") 

# util to handle vector and matrix inputs
def get_ndistr(x):
	if x.ndim == 2:
		return x.shape[1]
	return 1

# P is the transpose of a transition matrix
# x is an ndarray where every column is taken as a distribution
# k is the number of iterations
def mc_iterate(P,x,k): 
	ndistr = get_ndistr(x)
	N = P.shape[0]
	y = x.copy()

	if ndistr == 1 or N*k < 1e5:
		return mc_iterate_py(P,x,k)

	# spawn worker processes and iterate distributions seperately		
	return mc_iterate_py_process(P,x,k)

def mc_iterate_py(P,x,k):
	ndistr = get_ndistr(x)
	y = x.copy()

	# vector shape
	if x.ndim == 1:
		for j in xrange(k):
			y = P.dot(y)
	# matrix shape	
	else:	
		for i in xrange(get_ndistr(x)):
			for j in xrange(k):
				y[:,i] = P.dot(y[:,i])

	return y

def mc_iterate_py_process(P,x,k):
	ndistr = get_ndistr(x)
	y = x.copy()

	save_P(P)
	for i in xrange(ndistr):
		save_x(x,i)

	# start processes
	pool = Pool(processes=min(ndistr,6))
	processes = []

	for i in xrange(ndistr):
		processes.append( pool.apply_async(py_iteration_process, (i,k)) ) 

	# fetch results (vector/matrix shape version)
	if x.ndim  == 1:
		processes[0].get()
		y = load_x(0)
	else:
		for i in xrange(ndistr):
			processes[i].get()
			y[:,i] = load_x(i)

	pool.close()

	for i in xrange(ndistr):
		remove_x(i)
	remove_P()

	return y
	
def py_iteration_process(i,k):
	P = load_P()
	x = load_x(i)

 	for j in xrange(k):
 		x = P.dot(x)

 	save_x(x,i)
 	return

#def mc_iterate_c(fsparse, nsparse, fdense, ndense, num_iter, fout):
#	base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#
#	args = (os.path.abspath(base_path+"/../bin/iterate_mc"), fsparse, nsparse, fdense, ndense, num_iter, fout)
#	print args
#	popen = subprocess.Popen(args, stdout=subprocess.PIPE)
#	popen.wait()
#	output = popen.stdout.read()
#	print output