import numpy as np
import matplotlib.pyplot as plt


"""
	This code generate a plot comparing Delta T_{x4} and 2 x Delta T_{x2} for varying value of alpha.
"""
###################### - Simulation Parameter - ###################
T_0 = 287
C_0 = 270

lamb = -0.79

CO2_1 = 2
CO2_2 = 4

alpha_min = -0.025
alpha_max = 0.025
detla_alpha = 0.00001
alpha_distribution = np.arange(alpha_min, alpha_max, detla_alpha)

###################### - Function definitions - ###########################


def temperature_increase(CO_2_multiplication, alpha, lamb):
	"""
		Give the increase of temperature for a given perturbation in CO_2 concetration and given values of the feedback
	"""
	F = np.log2(CO_2_multiplication)*3.71
	if alpha == 0:
		return -F/lamb
	else:
		return (-lamb - np.sqrt(lamb**2 - 4 * alpha * F))/(2*alpha)


############################ - Simulation - ########################## 

T_1 = [] #For one doubling
T_2 = [] #For two doubling

for alpha in alpha_distribution:
	T_1.append(2*temperature_increase(CO2_1, alpha, lamb))
	T_2.append(temperature_increase(CO2_2, alpha, lamb))


##################### - Ploting the results - ####################

plt.plot(alpha_distribution, T_1, label = '2 x Delta T_2x')
plt.plot(alpha_distribution, T_2, label = 'Delta T_4x')
plt.ylabel('delta_T (K)')
plt.xlabel('alpha (W/m^2 / K^2)')
plt.title('lambda = {}W/m^2/K'.format(lamb))
plt.xlim(-0.025,0.025)
plt.grid()
plt.legend()



plt.show()

