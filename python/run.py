execfile('ergc.py')

mat = load_gc(0,0)

print get_stationary_distribution(mat)


print get_num_distributions(mat)

print get_num_iteration_steps(mat)

for igc in xrange(10):
	compute_d_tv(0,igc)