import numpy, random, math, time, os, os.path

import matplotlib.pyplot

import networkx as nx
import scipy.sparse as ssp

from numpy import linalg

# configuration file
execfile('config.py')

# these require only the configuration file
execfile('mc_iterate.py')
execfile('transition_matrix.py')
execfile('mat_file_format.py')

def total_variation(my,nu):
	return abs(my-nu).sum()/2.

def relative_error(my,nu):
	divisor = numpy.maximum(numpy.minimum(my,nu), 1e-20)
	
	return numpy.divide(abs(my-nu), divisor).max()

# these require previously included files
execfile('analyze_markov_chain.py')
execfile('graph.py')

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
