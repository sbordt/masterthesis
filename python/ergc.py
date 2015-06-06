execfile('config.py')
execfile('transition_matrix.py')
execfile('cutoff.py')
execfile('mc_iterate.py')
execfile('mat_file_format.py')

def gc_file_path(ig,igc):
	return storage_path+"/giant_components/generation_"+`ig`+"/gc_" + `igc` + ".mat"

def load_gc(ig,igc):
	return sio.loadmat(gc_file_path(ig,igc))

def gc_add_dict(ig,igc,d):
	sio.savemat(gc_file_path(ig,igc), dict(load_gc(ig,igc), **d))
	return

def iterate_distributions(ig,igc):
	TOL = 1e-2

	mat = load_gc(ig,igc)
	N = get_N(mat)
	P = get_P(mat)
	print N
	
	num_simulations = 5

	x = []
	x.append(uniform_starting_point_distributions(N,num_simulations))

	# iterate in steps that are powers of 2
	power_of_2 = 0
	total_steps = 0

	while True:
		steps = pow(2,power_of_2)-total_steps
		total_steps = total_steps+steps

		start = time.time()
		x.append(mc_iterate(P,x[power_of_2],steps))
		end = time.time()

		print `steps`+" step(s) completed for a total of "+`total_steps`+" step(s) (that took %(sec)f seconds)." % {'sec': (end - start)}

		# compute the error and exit loop 
		rel_error = 0

		for i in xrange(num_simulations):
			rel_err = max(rel_error, relative_error(x[power_of_2][:,0], x[power_of_2][:,i]))
		
		print "Relative error: %(a).8f" % {'a': rel_err}

		if rel_err < TOL:
			print "Relative error smaller than treshold!"
			break 

		power_of_2 = power_of_2+1

	# save iteration data
	for i in xrange(power_of_2):
		gc_add_dict(ig, igc, {"x_%(i)d" % {'i': pow(2,i)}: x[i]})	 

	return

def compute_stationary_distribution(ig,igc):
	mat = load_gc(ig,igc)

	x = get_distributions(mat)

	return x[-1][:,0]

def compute_d_tv(ig,igc):
	mat = load_gc(ig,igc)

	x = get_distributions(mat)
	stationary = get_stationary_distribution(mat)
	num_steps = get_num_iteration_steps(mat)

	d_tv = numpy.zeros(num_steps)

	for i in xrange(get_num_distributions(mat)):
		for j in xrange(num_steps):
			d_tv[j] = total_variation(stationary, x[j][:,i])

		gc_add_dict(ig, igc, {"d_tv_%(i)d" % {'i': i}: d_tv}) 

	return






