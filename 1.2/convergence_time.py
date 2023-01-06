import numpy as np
import matplotlib.pyplot as plt

"""
    This code plots the time the system take to reach a steady state for a varying alpha value.
"""


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
    if alpha < alpha_critique(lamb, CO2_multiplication):
        return (delta_t/C) * (F + lamb * delta_T + alpha * delta_T**2) + delta_T
    else:
        return 0

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
detla_alpha = 0.0001
alpha_distribution = np.arange(alpha_min, alpha_max, detla_alpha)



########## - Temporal discretization  - ###########

delta_t_in_year = 0.2
integration_time_in_year = 500 
delta_t = delta_t_in_year * 365 * 24 * 60 * 60 # Using SI units
integration_time = integration_time_in_year * 365 * 24 * 60 * 60 # Using SI units

temporal_discretization = np.arange(0, integration_time, delta_t)

################# - Simulation - ################



record_2a_1 = []
record_2a_2 = []
record_2a_3 = []

record_2b_1 = []
record_2b_2 = []
record_2b_3 = []
for alpha in alpha_distribution:
    print(round(alpha,2),'/',alpha_max)
    T_2a_1 = []
    T_2a_2 = []
    T_2a_3 = []

    T_2b_1 = []
    T_2b_2 = []
    T_2b_3 = []
    
    #The following six variables are set to 1 when the steady state is reached to not overcount.
    a_1_steady_state = 0
    a_2_steady_state = 0
    a_3_steady_state = 0

    b_1_steady_state = 0
    b_2_steady_state = 0
    b_3_steady_state = 0
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
            if abs(T_2a_1[-1] - T_2a_1[-2]) < 0.001 and a_1_steady_state == 0:
                record_2a_1.append(t)
                a_1_steady_state = 1
            if abs(T_2a_2[-1] - T_2a_2[-2]) < 0.001 and a_2_steady_state == 0:
                record_2a_2.append(t)
                a_2_steady_state = 1
            if abs(T_2a_3[-1] - T_2a_3[-2]) < 0.001 and a_3_steady_state == 0:
                record_2a_3.append(t)
                a_3_steady_state = 1

            if abs(T_2b_1[-1] - T_2b_1[-2]) < 0.001 and b_1_steady_state == 0:
                record_2b_1.append(t)
                b_1_steady_state = 1
            if abs(T_2b_2[-1] - T_2b_2[-2]) < 0.001 and b_2_steady_state == 0:
                record_2b_2.append(t)
                b_2_steady_state = 1
            if abs(T_2b_3[-1] - T_2b_3[-2]) < 0.001 and b_3_steady_state == 0:
                record_2b_3.append(t)
                b_3_steady_state = 1

for i in range(len(alpha_distribution)):#Passing times units from s to y
    record_2a_1[i] /= 31536000
    record_2a_2[i] /= 31536000
    record_2a_3[i] /= 31536000

    record_2b_1[i] /= 31536000
    record_2b_2[i] /= 31536000
    record_2b_3[i] /= 31536000
plt.subplot(2,1,1)
plt.title('2 x CO_2 concentration.')
plt.plot(alpha_distribution,record_2a_1, label = 'lambda = {} W/m^2/K'.format(lamb_2ab_1))
plt.plot(alpha_distribution,record_2a_2, label = 'lambda = {} W/m^2/K'.format(lamb_2ab_2))
plt.plot(alpha_distribution,record_2a_3, label = 'lambda = {} W/m^2/K'.format(lamb_2ab_3))
plt.legend()
plt.ylabel('Convergence time (y)')
plt.xlabel('alpha (W/m^2/K^2)')
plt.xlim(-0.1,0.1)
plt.grid()
plt.subplot(2,1,2)
plt.title('4 x CO_2 concentration.')
plt.plot(alpha_distribution,record_2b_1, label = 'lambda = {} W/m^2/K'.format(lamb_2ab_1))
plt.plot(alpha_distribution,record_2b_2, label = 'lambda = {} W/m^2/K'.format(lamb_2ab_2))
plt.plot(alpha_distribution,record_2b_3, label = 'lambda = {} W/m^2/K'.format(lamb_2ab_3))
plt.legend()
plt.ylabel('Convergence time (y)')
plt.xlim(-0.1,0.1)
plt.xlabel('alpha (W/m^2/K^2)')
plt.grid()
plt.show()
        