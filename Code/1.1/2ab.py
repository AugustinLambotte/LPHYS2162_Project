import numpy as np
import matplotlib.pyplot as plt


"""
	This code reproduce graph 2a and 2b of the Bloch_johnson paper.

"""
###################### - Simulation Parameter - ###################
T_0 = 287
C_0 = 270

lambda_1 = -0.79
lambda_2 = -1.17
lambda_3 = -1.78

CO2_1 = 2
CO2_2 = 4

alpha_min = -0.1
alpha_max = 0.1
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

def alpha_critique(lamb, CO_2_multiplication):
	"""
		Give the value of alpha where sqrt(lamb**2 - 4 * alpha * F) doesn't exist -> runaway warming.
	"""
	F = np.log2(CO_2_multiplication)*3.71
	return round((lamb**2)/(4*F),3)


############################ - Simulation - ########################## 
#These are for a doubling of CO_2
T_11 = []
T_12 = []
T_13 = []
#these are for two doubling.
T_21 = []
T_22 = []
T_23 = []

for alpha in alpha_distribution:
	T_11.append(temperature_increase(CO2_1, alpha, lambda_1))
	T_12.append(temperature_increase(CO2_1, alpha, lambda_2))
	T_13.append(temperature_increase(CO2_1, alpha, lambda_3))

	T_21.append(temperature_increase(CO2_2, alpha, lambda_1))
	T_22.append(temperature_increase(CO2_2, alpha, lambda_2))
	T_23.append(temperature_increase(CO2_2, alpha, lambda_3)) 


##################### - Ploting the results - ####################

plt.subplot(2,1,1)
plt.plot(alpha_distribution, T_11, label = 'lambda = {}, critical alpha = {}'.format(lambda_1, alpha_critique(lambda_1,CO2_1)))
plt.plot(alpha_distribution, T_12, label = 'lambda = {}, critical alpha = {}'.format(lambda_2, alpha_critique(lambda_2,CO2_1)))
plt.plot(alpha_distribution, T_13, label = 'lambda = {}, critical alpha = {}'.format(lambda_3, alpha_critique(lambda_3,CO2_1)))
plt.ylabel('delta_T (??K)')
plt.xlabel('alpha (W/m^2 / K^2)')
plt.title('2x CO_2 concentration')
plt.xlim(-0.1,0.1)
plt.grid()
plt.legend()

plt.subplot(2,1,2)
plt.plot(alpha_distribution, T_21, label = 'lambda = {}, critical alpha = {}'.format(lambda_1, alpha_critique(lambda_1,CO2_2)))
plt.plot(alpha_distribution, T_22, label = 'lambda = {}, critical alpha = {}'.format(lambda_2, alpha_critique(lambda_2,CO2_2)))
plt.plot(alpha_distribution, T_23, label = 'lambda = {}, critical alpha = {}'.format(lambda_3, alpha_critique(lambda_3,CO2_2)))
plt.ylabel('delta_T (??K)')
plt.xlabel('alpha (W/m^2 /K^2)')
plt.title('4x CO_2 concentration')
plt.xlim(-0.1,0.1)
plt.grid()
plt.legend()


plt.show()

