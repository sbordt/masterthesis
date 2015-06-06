import numpy as np
import scipy.sparse as ssp
import os, inspect, subprocess
import scipy.io as sio
from multiprocessing import Pool

tmp_path = '/home/sbordt/Desktop/masterthesis_tmp/'

def load_P():
	mat = sio.loadmat(tmp_path + "P.mat")
	return mat['P'].tocsr()

def save_P(P):
	sio.savemat(tmp_path + "P.mat", {'P': P})
	return

def remove_P():
	os.remove(tmp_path + "P.mat")
	return

def load_x(i):
	mat = sio.loadmat(tmp_path + "x_" + `i` + ".mat")
	return mat['x'][0]

def save_x(x,i):
	# handle both vector and matrix inputs
	if x.ndim == 1:
		sio.savemat(tmp_path + "x_" + `i` + ".mat", {'x': x})	
	else:
		sio.savemat(tmp_path + "x_" + `i` + ".mat", {'x': x[:,i]})
	return 

def remove_x(i):
	os.remove(tmp_path + "x_" + `i` + ".mat")

# P is the transpose of a transition matrix
# x is an ndarray where every column is taken as a distribution
# k is the number of iterations
def mc_iterate(P,x,k): 
	N = P.shape[0]
	ndistr = x.shape[1] 
	y = x.copy()

	if ndistr == 1 or N*k < 1e5:
		for i in xrange(ndistr):
			for j in xrange(k):
				y[:,i] = P.dot(y[:,i])

	# spawn worker processes and iterate distributions seperately
	else:
		save_P(P)
		for i in xrange(ndistr):
			save_x(x,i)

		# start processes
		pool = Pool(processes=min(ndistr,6))
		processes = []

		for i in xrange(ndistr):
			processes.append( pool.apply_async(mc_iterate_process, (i,k)) ) 

		# fetch results
		for i in xrange(ndistr):
			processes[i].get()
			y[:,i] = load_x(i)

		pool.close()

		for i in xrange(ndistr):
			remove_x(i)
		remove_P()
		

	return y

def mc_iterate_process(i,k):
	P = load_P()
	x = load_x(i)

 	for j in xrange(k):
 		x = P.dot(x)

 	save_x(x,i)
 	return 

def mc_iterate_c(fsparse, nsparse, fdense, ndense, num_iter, fout):
	base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

	args = (os.path.abspath(base_path+"/../bin/iterate_mc"), fsparse, nsparse, fdense, ndense, num_iter, fout)
	print args
	popen = subprocess.Popen(args, stdout=subprocess.PIPE)
	popen.wait()
	output = popen.stdout.read()
	print output


