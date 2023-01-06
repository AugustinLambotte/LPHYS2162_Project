import numpy as np
import matplotlib.pyplot as plt


######################## - Graph 2a - ########################

"""
	This code plot a comparison between some linear models and quadratic and how there predicted \Delta T are changing when
    the forcing increase.
"""
###################### - Simulation Parameter - ###################
T_0 = 287
C_0 = 270

lamb_1 = -0.88
lamb_2 = -1.28

alpha_1 = 0.03
alpha_2 = 0.058
F_disctretization = np.arange(0,3,0.01)

###################### - Function definitions - ###########################


def temperature_increase(F, alpha, lamb):
	"""
		Give the increase of temperature for a given perturbation in CO_2 concetration and given values of the feedback
	"""
	
	if alpha == 0:
		return -F/lamb
	else:
		return (-lamb - np.sqrt(lamb**2 - 4 * alpha * F))/(2*alpha)

############################ - Simulation - ########################## 
#These are for a doubling of CO_2
T_11 = []
T_12 = []

T_21 = []
T_22 = []

T_1_lin = []
T_2_lin = []

for F in F_disctretization:
    T_11.append(temperature_increase(F,alpha_1,lamb_1))
    T_12.append(temperature_increase(F,alpha_2,lamb_1))
    T_21.append(temperature_increase(F,alpha_1,lamb_2))
    T_22.append(temperature_increase(F,alpha_2,lamb_2))
    T_1_lin.append(temperature_increase(F,0,lamb_1))
    T_2_lin.append(temperature_increase(F,0,lamb_2))


##################### - Ploting the results - ####################


plt.plot(F_disctretization, T_11, label = 'alpha = {} W/m^2/K^2, lambda = {} W/m^2/K'.format(alpha_1,lamb_1))
plt.plot(F_disctretization, T_12, label = 'alpha = {} W/m^2/K^2, lambda = {} W/m^2/K'.format(alpha_2,lamb_1))
plt.plot(F_disctretization, T_21, label = 'alpha = {} W/m^2/K^2, lambda = {} W/m^2/K'.format(alpha_1,lamb_2))
plt.plot(F_disctretization, T_22, label = 'alpha = {} W/m^2/K^2, lambda = {} W/m^2/K'.format(alpha_2,lamb_2))
plt.plot(F_disctretization, T_1_lin, label = 'linear, lambda = {} W/m^2/K'.format(lamb_1))
plt.plot(F_disctretization, T_2_lin, label = 'linear, lambda = {} W/m^2/K'.format(lamb_2))
plt.ylabel('delta T (K)')
plt.xlabel('F (W/m^2)')
plt.grid()
plt.xlim(0,3)
plt.legend()

plt.show()

