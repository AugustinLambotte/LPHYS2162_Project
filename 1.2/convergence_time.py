import numpy as np
import matplotlib.pyplot as plt


############ - Function definition - ##############
def alpha_critique(lamb, CO_2_multiplication):
	"""
		Give the value of alpha where sqrt(lamb**2 - 4 * alpha * F) doesn't exist -> runaway warming.
	"""
	F = np.log2(CO_2_multiplication)*3.71
	return (lamb**2)/(4*F)

def delta_T_next_time_step(CO2_multiplication, lamb, alpha, delta_T):
    # return the next time step with Euler Forward method.
    F = np.log2(CO2_multiplication)*3.71
    return (delta_t/C) * (F + lamb * delta_T + alpha * delta_T**2) + delta_T

def temperature_increase(CO_2_multiplication, alpha, lamb):
	"""
		Give the increase of temperature for a given perturbation in CO_2 concetration and given values of the feedback
	"""
	F = np.log2(CO_2_multiplication)*3.71
	if alpha == 0:
		return -F/lamb
	else:
		return (-lamb - np.sqrt(lamb**2 - 4 * alpha * F))/(2*alpha)

############ - Simulation Parameters - ############
C = 8.36 * 10 ** 8 



lamb_2ab_1 = -0.79
lamb_2ab_2 = -1.17
lamb_2ab_3 = -1.78

CO2_2a = 2
CO2_2b = 4

alpha_min = -0.1
alpha_max = 0.1
detla_alpha = 0.0005
alpha_distribution = np.arange(alpha_min, alpha_max, detla_alpha)

epsilon = 0.01

########## - Temporal discretization  - ###########

delta_t_in_year = 0.05
integration_time_in_year = 200 
delta_t = delta_t_in_year * 365 * 24 * 60 * 60 # Using SI units
integration_time = integration_time_in_year * 365 * 24 * 60 * 60 # Using SI units

temporal_discretization = np.arange(0, integration_time, delta_t)

################# - Simulation - ################



record = []
for alpha in alpha_distribution:
    print(round(alpha,2),'/',alpha_max)
    T_2a_1 = []
    T_2a_2 = []
    T_2a_3 = []

    T_2b_1 = []
    T_2b_2 = []
    T_2b_3 = []
    for t in temporal_discretization:
        if t == 0:
            T_2a_1.append(0)
            T_2a_2.append(0)
            T_2a_3.append(0)

            T_2b_1.append(0)
            T_2b_2.append(0)
            T_2b_3.append(0)
        else:
            T_2a_1.append(delta_T_next_time_step(CO2_2a, lamb_2ab_1, alpha, T_2a_1[-1]))
            T_2a_2.append(delta_T_next_time_step(CO2_2a, lamb_2ab_2, alpha, T_2a_2[-1]))
            T_2a_3.append(delta_T_next_time_step(CO2_2a, lamb_2ab_3, alpha, T_2a_3[-1]))

            T_2b_1.append(delta_T_next_time_step(CO2_2b, lamb_2ab_1, alpha, T_2b_1[-1]))
            T_2b_2.append(delta_T_next_time_step(CO2_2b, lamb_2ab_2, alpha, T_2b_2[-1]))
            T_2b_3.append(delta_T_next_time_step(CO2_2b, lamb_2ab_3, alpha, T_2b_3[-1]))
        if T_2a_1[-1] >= temperature_increase(CO2_2a,alpha,lamb_2ab_1) - (epsilon/2) and T_2a_1[-1] <= temperature_increase(CO2_2a,alpha,lamb_2ab_1) + (epsilon/2):
            record.append(t)
            break
plt.plot(alpha_distribution,record)
plt.show()
        