import numpy as np 
import random as rand
import math
import matplotlib.pyplot as plt


######################## - Graph 1d - ########################

"""
	In this simulation we want to study the net top-of-atm energy flux N, caused by a forcing F. F will have tree dependance;
    the preindustrial linear feedback on temperature difference lambda, the quadratic feedback on temperature modification alpha, and
    a forcing caused by a multiplication of a CO_2 concentration. 

		This time the quadratic dependence, alpha, and the linear one, lambda, are fixed but 
	we test the model for one and two doubling of CO_2 concentration.
"""
alpha = 0.058
lamb = -1.28
T_ref = 287
def F(lamb, alpha, delta_T, CO_2_multiplication):
	"""
		return F, the forcing on the net top-of-atm energy flux. Lambda represent the linear dependance on temperature and alpha the quadratic one.
	The last term is the sensitivity to a multiplication by CO_2_multiplication of the concentration of CO_2 in the atm.
	"""
	return lamb * delta_T + alpha * delta_T**2 + np.log2(CO_2_multiplication)*3.71

T_min = 286
T_max = 300
T = [T_min]

N_1 = [F(lamb, 0, T_min - T_ref, 2)]
N_2 = [F(lamb, alpha, T_min - T_ref, 2)]
N_3 = [F(lamb, 0, T_min - T_ref, 4)]
N_4 = [F(lamb, alpha, T_min - T_ref, 4)]

line_0 = [0] # serve to plot a line on the zero value on the fig.
iteration = 100
delta_T_iteration = (T_max - T_min)/iteration

for i in range(iteration):
	T.append(T[-1] + delta_T_iteration)
	line_0.append(0)

	N_1.append(F(lamb, 0, T[-1] - T_ref,2))
	N_2.append(F(lamb, alpha, T[-1] - T_ref,2))
	N_3.append(F(lamb, 0, T[-1] - T_ref,4))
	N_4.append(F(lamb, alpha, T[-1] - T_ref,4))


plt.plot(T, N_1, label = "linear, doubling of CO_2")
plt.plot(T, N_2, label = "alpha = 0.058, doubling of CO_2")
plt.plot(T, N_3, label = "linear, CO_2 doubled twice")
plt.plot(T, N_4, label = "alpha = 0.058, CO_2 doubled twice")
plt.plot(T,line_0)
plt.legend()
plt.grid()
plt.xlim(T_min,T_max)
plt.ylim(-7,21)
plt.show()
