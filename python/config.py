import os.path, random

tmp_path = '/home/sbordt/Desktop/masterthesis_tmp/'

storage_path = '/media/sbordt/LINUXSHARE/masterthesis_data/'

# this function loops forever if there are more than 100000 temporary files but that will work for now
def tmp_mat_file_path():
	ftemplate = tmp_path + "file_RANDOM_INT.mat"
	fname = ftemplate.replace("RANDOM_INT", `random.randint(0,100000)`) 

	while os.path.isfile(fname): 
		fname = ftemplate.replace("RANDOM_INT", `random.randint(0,100000)`) 

	return fname