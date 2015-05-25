import scipy.sparse as ssp
import os, inspect, subprocess

def ccode_matrix_vector_product(M):
	# utility
	def write_int_list(int_list):
		list_length = len(int_list)
		code = ""
		k = 100

		i = 0
		while i < list_length:
			line = "    "

			j = 0
			while j < k and i+j < list_length:
				line = line + "%(a)d," % {'a': int_list[i+j]}
				j = j+1

			code = code + line + "\n"
			i = i+k
		
		return code

	def write_double_list(int_list):
		list_length = len(int_list)
		code = ""
		k = 100

		i = 0
		while i < list_length:
			line = "    "

			j = 0
			while j < k and i+j < list_length:
				line = line + "%(a).30f," % {'a': int_list[i+j]}
				j = j+1

			code = code + line + "\n"
			i = i+k
		
		return code

	N = M.shape[0]

	(I,J,V) = ssp.find(M)
	nnz = I.shape[0]

	# dictionary for matrix values
	matrix_values_list = []
	matrix_dict = {}

	i = 0
	while i < nnz:
		if matrix_dict.has_key(V[i]) == False:
			matrix_values_list.append(V[i])
			matrix_dict[V[i]] = len(matrix_dict)
		i = i+1

	# the number of summands per row
	num_summands_list = []

	# two arrays for the vector and matrix index per multiplication
	matrix_indices_list = []
	vector_indices_list = []

	# fill data structures
	max_num_summands = 0	

	row_start = 0
	while row_start < nnz:
		row = I[row_start]

		# find the end of the row
		row_end = row_start
		while row_end < nnz and I[row_end] == row:
			row_end = row_end+1

		num_summands = row_end-row_start	
		num_summands_list.append(num_summands)

		max_num_summands = max(max_num_summands, num_summands)
	
		# add row * vector code
		i_summand = 0

		for row_entry in range(row_start, row_end):
			matrix_indices_list.append(matrix_dict[V[row_entry]])
			vector_indices_list.append(J[row_entry])

			i_summand = i_summand+1

		# continue with the next row
		row_start = row_end

	# write the code :)
	code = "#include <cblas.h>\n\n"
	code = code + "#define MATRIX_VECTOR_N %(a)d\n\n" % {'a': N}

	# write the matrix
	code = code + "const double const matrix[] = {\n"
	code = code + write_double_list(matrix_values_list)
	code = code + "};\n\n"

	# write number of summands per row
	code = code + "const int const num_summands[] = {\n"
	code = code + write_int_list(num_summands_list)
	code = code + "};\n\n"

	# write matrix indices
	code = code + "const unsigned long const matrix_indices[] = {\n"
	code = code + write_int_list(matrix_indices_list)
	code = code + "};\n\n"

	# write vector indices
	code = code + "const unsigned long const vector_indices[] = {\n"
	code = code + write_int_list(vector_indices_list)
	code = code + "};\n\n"

	# write the function to call
	code = code + "void matrix_vector(double *x, double *y)\n"
	code = code + "{\n"
	code = code + "    double tmp[%(a)d];\n" % {'a': max_num_summands}
		

	code = code + "    unsigned long i;\n"
	code = code + "    unsigned long j;\n"
	code = code + "    unsigned long k=0;\n"
	code = code + "    for (i=0; i<%(a)d; i=i+1)\n" % ({'a': N})	
	code = code + "    {\n"
	code = code + "        for (j=0; j<num_summands[i]; j=j+1)\n"
	code = code + "        {\n"
	code = code + "            tmp[j] = x[vector_indices[k]] * matrix[matrix_indices[k]];\n"
	code = code + "            k = k+1;\n"
	code = code + "        }\n"
	code = code + "        y[i] = cblas_dasum(num_summands[i], tmp, 1);\n"
	code = code + "    }\n"		

	code = code + "}\n"

	return code



def cprog_matrix_vector_product(M):
	code = ccode_matrix_vector_product(M)

	base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	file = open(base_path+"/../c/meta/generated/matrix_vector.c", "w")
	file.write(code)
	file.close()

	subprocess.call("make --directory="+os.path.abspath(base_path+"/../c/meta/"), shell=True) 







