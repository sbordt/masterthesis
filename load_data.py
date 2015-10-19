import os
import scipy.io as sio

storage_path = "/home/sbordt/Desktop/masterthesis_data/"

def gc_file_path(ig,igc):
	return storage_path+"giant_components/generation_"+`ig`+"/gc_" + `igc` + ".mat"

def load_gc(ig,igc):
	return sio.loadmat(gc_file_path(ig,igc))

def save_gc(ig,igc,mat):
	path = gc_file_path(ig,igc)
	directory = os.path.dirname(path)

	if not os.path.exists(directory):
		os.makedirs(directory)

	sio.savemat(path, mat)
	return

def has_gc(ig,igc):
	return os.path.isfile(gc_file_path(ig,igc)) 
