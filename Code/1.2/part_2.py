import numpy as np
import matplotlib.pyplot as plt
"""
    Here, the goal is to investigate the role of the thermal inertia C and the transient behaviour of the model.
    A numerical scheme is implemented to solve (eq 3.). We will perform several times series, all of theme during 200y,
    for all the value of alpha lambda and F used in the previous exercises.
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
    return (delta_t/C) * (F + lamb * delta_T + alpha * delta_T**2) + delta_T

############ - Simulation Parameters - ############
C = 8.36 * 10 ** 8 

#Graph 1a. Same lambda, varying alpha
lamb_1a = -0.88

alpha_1a_1 = -0.035
alpha_1a_2 = 0.03
alpha_1a_3 = 0.058
alpha_1a_4 = 0

CO2_1a = 2

#Graphs 1d. Same lambda, varying from linear to alpha = 0.058 and from one to two doubling of CO2
lamb_1d = -1.28
alpha_1d_1 = 0
CO2_1d_1 = 2

alpha_1d_2 = 0.058
CO2_1d_2 = 2

alpha_1d_3 = 0
CO2_1d_3 = 4

alpha_1d_4 = 0.058
CO2_1d_4 = 4





########## - Temporal discretization  - ###########

delta_t_in_year = 0.2
integration_time_in_year = 200 
delta_t = delta_t_in_year * 365 * 24 * 60 * 60 # Using SI units
integration_time = integration_time_in_year * 365 * 24 * 60 * 60 # Using SI units

temporal_discretization = np.arange(0, integration_time, delta_t)



################# - Simulation - ###################
T_1a_1 = []
T_1a_2 = []
T_1a_3 = []
T_1a_4 = []

T_1d_1 = []
T_1d_2 = []
T_1d_3 = []
T_1d_4 = []

for t in temporal_discretization:
    if t == 0:
        T_1a_1.append(0)
        T_1a_2.append(0)
        T_1a_3.append(0)
        T_1a_4.append(0)

        T_1d_1.append(0)
        T_1d_2.append(0)
        T_1d_3.append(0)
        T_1d_4.append(0)
    else:
        T_1a_1.append(delta_T_next_time_step(CO2_1a, lamb_1a, alpha_1a_1, T_1a_1[-1]))
        T_1a_2.append(delta_T_next_time_step(CO2_1a, lamb_1a, alpha_1a_2, T_1a_2[-1]))
        T_1a_3.append(delta_T_next_time_step(CO2_1a, lamb_1a, alpha_1a_3, T_1a_3[-1]))
        T_1a_4.append(delta_T_next_time_step(CO2_1a, lamb_1a, alpha_1a_4, T_1a_4[-1]))

        T_1d_1.append(delta_T_next_time_step(CO2_1d_1, lamb_1d, alpha_1d_1, T_1d_1[-1]))
        T_1d_2.append(delta_T_next_time_step(CO2_1d_2, lamb_1d, alpha_1d_2, T_1d_2[-1]))
        T_1d_3.append(delta_T_next_time_step(CO2_1d_3, lamb_1d, alpha_1d_3, T_1d_3[-1]))
        T_1d_4.append(delta_T_next_time_step(CO2_1d_4, lamb_1d, alpha_1d_4, T_1d_4[-1]))

################## - Ploting the results - ##################



plt.subplot(2,1,1)
plt.plot(temporal_discretization/31536000,T_1a_1, label = 'lambda = {}, alpha = {}, CO2_mult = {}, delta_T steady state= {}°K'.format(lamb_1a,alpha_1a_1,CO2_1a,round(T_1a_1[-1],1)))
plt.plot(temporal_discretization/31536000,T_1a_2, label = 'lambda = {}, alpha = {}, CO2_mult = {}, delta_T steady state= {}°K'.format(lamb_1a,alpha_1a_2,CO2_1a,round(T_1a_2[-1],1)))
plt.plot(temporal_discretization/31536000,T_1a_3, label = 'lambda = {}, alpha = {}, CO2_mult = {}, steady state unreached'.format(lamb_1a,alpha_1a_3,CO2_1a))
plt.plot(temporal_discretization/31536000,T_1a_4, label = 'lambda = {}, linear, CO2_mult = {}, delta_T steady state = {}°K'.format(lamb_1a,CO2_1a,round(T_1a_4[-1],1)))

plt.xlabel('time (y)')
plt.ylabel('delta_T (K)')
plt.legend()
plt.grid()
plt.title('Transient behaviour')
   
plt.subplot(2,1,2)
plt.plot(temporal_discretization/31536000,T_1d_1, label = 'lambda = {}, linear, CO2_mult = {}, delta_T steady state= {}°K'.format(lamb_1d, CO2_1d_1, round(T_1d_1[-1],1)))
plt.plot(temporal_discretization/31536000,T_1d_2, label = 'lambda = {}, alpha = {}, CO2_mult = {}, delta_T steady state= {}°K'.format(lamb_1d, alpha_1d_2, CO2_1d_2, round(T_1d_2[-1],1)))
plt.plot(temporal_discretization/31536000,T_1d_3, label = 'lambda = {}, linear, CO2_mult = {}, delta_T steady state= {}°K'.format(lamb_1d,CO2_1d_3,round(T_1d_3[-1],1)))
plt.plot(temporal_discretization/31536000,T_1d_4, label = 'lambda = {}, alpha = {}, CO2_mult = {}, steady state unreached'.format(lamb_1d,alpha_1d_4,CO2_1d_4))
plt.legend()
plt.xlabel('time (y)')
plt.ylabel('delta_T (K)')
plt.grid()

plt.show()