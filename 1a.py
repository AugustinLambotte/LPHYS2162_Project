import numpy as np 
import random as rand
import math
import matplotlib.pyplot as plt

########################## - Graph 1a - ###########################
"""
   		In this simulation we want to study the net top-of-atm energy flux N, caused by a forcing F. F will have tree dependance;
    the preindustrial linear feedback on temperature difference lambda, the quadratic feedback on temperature modification alpha, and
    a forcing caused by a multiplication of a CO_2 concentration. 

   		All simulation have the same pre-industrial feedback lambda (linear) but we test and the same multiplication of CO_2
   	concentration but we test 3 differents quadratic alpha feedback relative to a doubling of CO_2.
"""
test = 1

T_ref = 287
lamb = -0.88

def F(lamb, alpha, delta_T, CO_2_multiplication):
	"""
		return F, the forcing on the net top-of-atm energy flux. Lambda represent the linear dependance on temperature and alpha the quadratic one.
	The last term is the sensitivity to a multiplication by CO_2_multiplication of the concentration of CO_2 in the atm.
	"""
	return lamb * delta_T + alpha * delta_T**2 + np.log2(CO_2_multiplication)*3.71

T_min = 285
T_max = 297

# N  is the net difference top-of-atm energy flux from pre-industrial period.

N_1 = [F(lamb, -0.035, T_min - T_ref, 2)]
N_2 = [F(lamb, 0.058, T_min - T_ref, 2)]
N_3 = [F(lamb, 0.03, T_min - T_ref, 2)]
N_4 = [F(lamb, 0, T_min - T_ref, 2)]

line_0 = [0] # serve to plot a line on the zero value on the fig.
iteration = 100
T = [T_min]
delta_T_iteration = (T_max - T_min)/iteration

for i in range(iteration):
	T.append(T[-1] + delta_T_iteration)
	line_0.append(0)

	N_1.append(F(-0.88, - 0.035, T[-1] - T_ref, 2))
	N_2.append(F(-0.88, 0.058, T[-1] - T_ref, 2))
	N_3.append(F(-0.88, 0.03, T[-1] - T_ref, 2))
	N_4.append(F(-0.88, 0, T[-1] - T_ref, 2))


plt.plot(T, N_1, label = "alpha = -0.035")
plt.plot(T, N_2, label = "alpha = 0.058")
plt.plot(T, N_3, label = "alpha = 0.03")
plt.plot(T, N_4, label = "linéaire")
plt.plot(T,line_0)
plt.legend()
plt.grid()
plt.xlim(T_min,T_max)
plt.ylim(-2,8)
plt.show()

