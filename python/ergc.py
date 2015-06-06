import numpy 
import scipy.io as sio
import scipy.sparse as ssp
import random, os, time

path = '/media/sbordt/LINUXSHARE/masterthesis_data/'

execfile('transition_matrix.py')
execfile('cutoff.py')

def load_gc(igc):
	return sio.loadmat("../data/giant_components/gc_" + `igc` + ".mat")

def save_x(x, i):
	sio.savemat("../data/x_" + `i` + ".mat", {'x': x})
	return

def load_x(i):
	mat = sio.loadmat("../data/x_" + `i` + ".mat")
	x = mat['x'][0]
	return x 

def remove_x(i):
	os.remove("../data/x_" + `i` + ".mat")

def iterate(i,igc):
	mat = load_gc(igc)
	P = mat['P']

	x = load_x(i)

 	for j in range(0,10000):
 		x = P.dot(x)

 	save_x(x,i)
 	return 

def main():
	igc = 1

	mat = load_gc(igc)
	N = mat['N'][0][0]
	print N
	
	num_simulations = 3
	max_steps = 500

	x = uniform_starting_point_distributions(N,num_simulations)

	 # start num_simulations worker processes
	pool = Pool(processes=num_simulations)             
	results = [0,0,0]

	# iteration loop
	for istep in range(1,max_steps):
		start = time.time()

		# iterate one step
		for i in range(0,num_simulations):
			results[i] = pool.apply_async(iterate, (i,igc)) 

		# fetch results
		x.append([])

		for i in range(0,num_simulations):
			results[i].get()
			x[istep].append( load_x(i) )

		end = time.time()

		# compute the error and exit loop 
		rel_err = max(relative_error(x[istep][0], x[istep][1]), relative_error(x[istep][1], x[istep][2]))		
		print "Step "  + `istep` +  " completed (%(a)f seconds)." % {'a': (end - start)}
		print "Relative error: %(a).8f" % {'a': rel_err}

		if rel_err < 1e-2:
			print "Relative error smaller than treshold."
			break 

	# delete temporary files
	for i in range(0,num_simulations):
		remove_x(i)

	# process iteration data
	M = []
	d_tv = []

	for i in range(0,num_simulations):
		L = []
		d_tv.append([])

		for j in range(0,istep+1):
			L.append(x[j][i])
			d_tv[i].append( total_variation(x[j][i], x[istep][i]) )
		
		M.append(numpy.matrix(L))
 
 	# save to file
	for i in range(0,num_simulations):
		sio.savemat("/media/sbordt/LINUXSHARE/masterthesis_data/gc_" + `igc` + "_iter_" + `i` + ".mat", {'x': M[i], 'd_tv': d_tv[i]})

	return

main()

# 22 seconds one computation
# ~70 seconds 4 computations one matrix
#  68 seconds 4 computations 4 matrices
# 50 seconds 3 computations 3 matrices
