import numpy as np 
import random as rand
import math
import matplotlib.pyplot as plt


######################## - Graph 2a - ########################

"""
	In this simulation we want to study the increase of temperature, delta_T, regarding the quadratic parametre alpha
	in tree case diffentiating each other by tree different lambda values.
	- C is the concentration of CO_2 in ppm
"""

T_0 = 287
C_0 = 270

lambda_1 = -0.79
lambda_2 = -1.17
lambda_3 = -1.78

def F(CO_2_multiplication):
	return np.log2(CO_2_multiplication)*3.71

def temperature_increase(F, alpha, lamb):
	return (-lamb - np.sqrt(lamb**2 - 4 * alpha * F))/(2 * alpha)

alpha_min = -0.1
alpha_max = 0.1
iteration = 200
detla_alpha = (alpha_max - alpha_min)/iteration
alpha = np.arange(alpha_min, alpha_max, detla_alpha)
#These are for a doubling of CO_2
T_11 = []
T_12 = []
T_13 = []
#these are for two doubling.
T_21 = []
T_22 = []
T_23 = []
for i in range(iteration):
	T_11.append(temperature_increase(F(2),alpha[i],lambda_1))
	T_12.append(temperature_increase(F(2),alpha[i],lambda_2))
	T_13.append(temperature_increase(F(2),alpha[i],lambda_3))

	T_21.append(temperature_increase(F(4),alpha[i],lambda_1))
	T_22.append(temperature_increase(F(4),alpha[i],lambda_2))
	T_23.append(temperature_increase(F(4),alpha[i],lambda_3))

plt.subplot(1,2,1)
plt.plot(alpha,T_11, label = 'lambda = {}'.format(lambda_1))
plt.plot(alpha,T_12, label = 'lambda = {}'.format(lambda_2))
plt.plot(alpha,T_13, label = 'lambda = {}'.format(lambda_3))
plt.ylabel('delta_T')
plt.xlabel('alpha')
plt.title('2x CO_2 concentration')
plt.xlim(-0.1,0.1)
plt.legend()

plt.subplot(1,2,2)
plt.plot(alpha,T_21, label = 'lambda = {}'.format(lambda_1))
plt.plot(alpha,T_22, label = 'lambda = {}'.format(lambda_2))
plt.plot(alpha,T_23, label = 'lambda = {}'.format(lambda_3))
plt.ylabel('delta_T')
plt.xlabel('alpha')
plt.title('4x CO_2 concentration')
plt.xlim(-0.1,0.1)
plt.legend()


plt.show()

