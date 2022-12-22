import numpy as np
import matplotlib.pyplot as plt

########################## - Graph 1a and 1d- ###########################


################## - Simulation parameters - ####################

T_ref = 287
T_min = 285
T_max = 300
delta_T = 0.1
T_distribution = np.arange(T_min,T_max,0.1)

lamb_a = -0.88
alpha_a1 = -0.035
alpha_a2 = 0.058
alpha_a3 = 0.03
alpha_a4 = 0
CO2_a = 2

lamb_d = -1.28
alpha_d1 = 0
alpha_d2 = 0.058
alpha_d3 = 0
alpha_d4 = 0.058
CO2_d1 = 2
CO2_d2 = 2
CO2_d3 = 4
CO2_d4 = 4


################### - Function definitions - #######################

def F(lamb, alpha, delta_T, CO_2_multiplication):
	"""
		return F, the forcing on the net top-of-atm energy flux. Lambda represent the linear dependance on temperature and alpha the quadratic one.
	The last term is the sensitivity to a multiplication by CO_2_multiplication of the concentration of CO_2 in the atm.
	"""
	return lamb * delta_T + alpha * delta_T**2 + np.log2(CO_2_multiplication)*3.71

def temperature_increase(lamb, alpha, CO_2_multiplication):
	"""
		Give the increase of temperature for a given perturbation in CO_2 concetration and given values of the feedback
	"""
	F = np.log2(CO_2_multiplication)*3.71
	if alpha == 0:
		return round(-F/lamb,2)
	else:
		return round((-lamb - np.sqrt(lamb**2 - 4 * alpha * F))/(2*alpha),2)

################## - Simulation - ############################
N_a1 = []
N_a2 = []
N_a3 = []
N_a4 = []

N_d1 = []
N_d2 = []
N_d3 = []
N_d4 = []


for T in T_distribution:

	N_a1.append(F(lamb_a, alpha_a1, T - T_ref, CO2_a))
	N_a2.append(F(lamb_a, alpha_a2, T - T_ref, CO2_a))
	N_a3.append(F(lamb_a, alpha_a3, T - T_ref, CO2_a))
	N_a4.append(F(lamb_a, alpha_a4, T - T_ref, CO2_a))

	N_d1.append(F(lamb_d, alpha_d1, T - T_ref, CO2_d1))
	N_d2.append(F(lamb_d, alpha_d2, T - T_ref, CO2_d2))
	N_d3.append(F(lamb_d, alpha_d3, T - T_ref, CO2_d3))
	N_d4.append(F(lamb_d, alpha_d4, T - T_ref, CO2_d4))

##################### - Ploting the results - #######################

zeros_line = np.zeros((len(T_distribution),1))

plt.subplot(1,2,1)
plt.plot(T_distribution, N_a1, label = "alpha = {}, delta_T = {}K".format(alpha_a1, temperature_increase(lamb_a, alpha_a1, CO2_a)))
plt.plot(T_distribution, N_a2, label = "alpha = {}, delta_T = ?".format(alpha_a2))
plt.plot(T_distribution, N_a3, label = "alpha = {}, delta_T = {}K".format(alpha_a3, temperature_increase(lamb_a, alpha_a3, CO2_a)))
plt.plot(T_distribution, N_a4, label = "linear, delta_T = {}K".format(temperature_increase(lamb_a, alpha_a4, CO2_a)))
plt.plot(T_distribution, zeros_line)
plt.legend()
plt.grid()
plt.xlim(T_min,297)
plt.ylim(-2,8)
plt.xlabel('T(°K)')
plt.ylabel('N(W/m^2)')

plt.subplot(1,2,2)
plt.plot(T_distribution, N_d1, label = "linear, CO_2 x {}, delta_T = {}K".format(CO2_d1, temperature_increase(lamb_d, alpha_d1, CO2_d1)))
plt.plot(T_distribution, N_d2, label = "alpha = {}, CO_2 x {}, delta_T = {}K".format(alpha_d2, CO2_d2, temperature_increase(lamb_d, alpha_d2, CO2_d2)))
plt.plot(T_distribution, N_d3, label = "linear, CO_2 x {}, delta_T = {}K".format(CO2_d3, temperature_increase(lamb_d, alpha_d3, CO2_d3)))
plt.plot(T_distribution, N_d4, label = "alpha = {}, CO_2 x {}, delta_T = ?".format(alpha_d4, CO2_d4, ))
plt.plot(T_distribution, zeros_line)
plt.legend()
plt.grid()
plt.xlim(T_min,T_max)
plt.ylim(-7,21)
plt.xlabel('T(°K)')
plt.ylabel('N(W/m^2)')
plt.show()

