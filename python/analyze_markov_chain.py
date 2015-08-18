import time
import matplotlib.pyplot as plt

def iterate_distributions(mat, TOL=1e-1):

	N = get_N(mat)
	P = get_P(mat)
	ndistr = 5

	print "Iterating "+`ndistr`+" distribution(s) for a markov chain with n="+`N`+"."

	x = []
	x.append(uniform_starting_point_distributions(N,ndistr))

	mat = dict(mat, **{"x_0": x[0]})

	# iterate in steps that are powers of 2
	power_of_2 = 0
	total_steps = 0
	total_seconds = 0.0

	while True:
		# iterate!
		steps = pow(2,power_of_2)-total_steps
		total_steps = total_steps+steps

		start = time.time()
		x.append(mc_iterate(P,x[power_of_2],steps))
		end = time.time()

		seconds = end-start
		total_seconds = total_seconds + seconds

		print time.strftime("%d %b %H:%M", time.localtime())+": "+`steps`+" step(s) completed for a total of "+`total_steps`+" step(s) (that took %(sec).2f seconds for a total of %(total_min).0f minutes)." % {'sec': seconds, 'total_min': (total_seconds / 60.0)}

		# save iteration data
		mat = dict(mat, **{"x_%(i)d" % {'i': total_steps}: x[-1]})

		# compute the error and exit loop if the error is < TOL
		rel_err = 0
		tv_err = 0

		for i in xrange(ndistr):
			rel_err = max(rel_err, relative_error(x[power_of_2][:,0], x[power_of_2][:,i]))
			tv_err = max(tv_err, total_variation(x[power_of_2][:,0], x[power_of_2][:,i]))
		
		print "Relative error: %(a).4f. Total variation error: %(b).4f." % {'a': rel_err, 'b': tv_err}

		if rel_err < TOL or tv_err < 0.05:
			print "Error smaller than treshold!"
			break 

		power_of_2 = power_of_2+1

	return mat

def compute_stationary_distribution(mat):
	x = get_distributions(mat)
	mat['stationary'] = x[-1][:,0]

	return mat

def compute_d_tv(mat):

	x = get_distributions(mat)
	stationary = get_stationary_distribution(mat)
	num_steps = get_num_iteration_steps(mat)

	d_tv = numpy.zeros(num_steps)

	for i in xrange(get_num_distributions(mat)):
		for j in xrange(num_steps):
			d_tv[j] = total_variation(stationary, x[j][:,i])

		mat = dict(mat, **{"d_tv_%(i)d" % {'i': i}: d_tv})

	return mat

def plot_mixing(mat):
	x = get_iteration_steps(mat)
	fig = plt.figure()

	for i in xrange(get_num_distributions(mat)):
		y = get_tv_mixing(mat,i)

		plt.plot(x, y)

	plt.xlabel("t")
	plt.ylabel("Distance to stationary distribution in total variation")
	plt.show()	
	return

def analyze_markov_chain(mat):
	mat = iterate_distributions(mat)
	mat = compute_stationary_distribution(mat)
	mat = compute_d_tv(mat)

	return mat
