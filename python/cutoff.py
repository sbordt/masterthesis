import numpy
from numpy import linalg
import random
import math
import matplotlib.pyplot

def total_variation(my,nu):
	return abs(my-nu).sum()/2.

def plot_mixing(P, initial, stationary, tol = 0.02):	
	# Simple algorithm that only computes P^n if n is a power of two.
	# It then utilizes the biwise representation of integers to determine the distribution
	# at any any time t.
	x = [0, 1]
	y = [total_variation(stationary, initial), total_variation(stationary, numpy.dot(initial, P))]

	# determine time till total_variation < tol
	P_2_powers = [P]

	while y[-1] > tol:
		x.append(x[-1]*2)
		P_2_powers.append(linalg.matrix_power(P_2_powers[-1], 2))
		y.append(total_variation(stationary, numpy.dot(initial, P_2_powers[-1])))

		if x[-1] > 1e15:
			print 'Does not convergence to the stationary distribution.'
			return

	print 'Converges to the stationary distribution.'

	# compute additional points to smooth the plot
	x_2 = map(int, numpy.linspace(3,x[-1],num=20))

	for idx, val in enumerate(x_2):
		dist = initial
		for  power, M in enumerate(P_2_powers):
			if val & int((2 ** power)):
				dist = numpy.dot(dist, M)

		x.append(val)
		y.append(total_variation(stationary, dist))

	# can do this sort-reverse trick since the distance in total variation is decreasing (is it? :) )
	x.sort()
	y.sort()
	y.reverse()

	matplotlib.pyplot.plot(x, y)
	matplotlib.pyplot.xlabel("t")
	matplotlib.pyplot.ylabel("Distance to stationary distribution in total variation")
	matplotlib.pyplot.show()
	return

def _plot_mixing(get_P_2_power, initial, stationary, tol = 0.02):	
	# Simple algorithm that only uses P^n if n is a power of two.
	# Use get_P_2_power to get that power.
	x = [0, 1]
	y = [total_variation(stationary, initial), total_variation(stationary, numpy.dot(initial, get_P_2_power(1)))]

	# determine time till total_variation < tol
	while y[-1] > tol:
		x.append(x[-1]*2)
		y.append(total_variation(stationary, numpy.dot(initial, get_P_2_power(len(x)-2))))

		if x[-1] > 1e15:
			print 'Does not convergence to the stationary distribution.'
			return

	print 'Converges to the stationary distribution.'

	matplotlib.pyplot.plot(x, y)
	matplotlib.pyplot.xlabel("t")
	matplotlib.pyplot.ylabel("Distance to stationary distribution in total variation")
	matplotlib.pyplot.show()
	return