def distr_key_name(i):
	return "x_%(i)d" % {'i': pow(2,i)}

def get_N(mat):
	return mat['N'][0][0]

def get_P(mat):
	return mat['P']

def get_num_distributions(mat):
	return mat['x_1'].shape[1]

def get_num_iteration_steps(mat):
	power_of_2 = 0

	while True:
		key = distr_key_name(power_of_2)
		if mat.has_key(key) == False:
			return power_of_2

		power_of_2 = power_of_2+1

def get_distributions(mat):
	power_of_2 = 0
	x = []

	while True:
		key = distr_key_name(power_of_2)
		if mat.has_key(key) == False:
			return x

		x.append(mat[key])

		power_of_2 = power_of_2+1

def get_stationary_distribution(mat):
	return mat['stationary'][0]
