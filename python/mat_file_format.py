def step_distr_name(i):
	return "x_%(i)d" % {'i': i}

def get_N(mat):
	return mat['N'][0][0]

def get_P(mat):
	return mat['P']

def get_num_distributions(mat):
	return mat['x_1'].shape[1]

def get_iteration_steps(mat):
	steps = []

	for key in mat.keys():
		if key.find("x_") == 0:
			steps.append(int(key.replace("x_", "")))

	steps.sort()
	return steps

def get_num_iteration_steps(mat):
	return len(get_iteration_steps(mat))

def get_distributions(mat):
	x = []

	for step in get_iteration_steps(mat):
		x.append(mat[ step_distr_name(step) ])

	return x

def get_stationary_distribution(mat):
	# vector shape
	if mat['stationary'].ndim == 1:
		return mat['stationary']

	# matrix shape
	return mat['stationary'][0]

def get_tv_mixing(mat,i):
	x = mat["d_tv_%(i)d" % {'i': i}]

	if x.ndim == 2:
		return x[0]

	return x
	

