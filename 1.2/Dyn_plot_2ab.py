import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import matplotlib.animation as animation

"""
    This code provides an animation of the transient behaviour of the system under one and two doubling 
    and with a varying alpha value.
"""
############### - Simulation parameters - ###########

C = 8.36 * 10 ** 8 

lamb_2ab_1 = -0.79
lamb_2ab_2 = -1.17
lamb_2ab_3 = -1.78

CO2_2a = 2
CO2_2b = 4

########## - Temporal discretization  - ###########

delta_t_in_year = 0.1
integration_time_in_year = 200
delta_t = delta_t_in_year * 365 * 24 * 60 * 60 # Using SI units
integration_time = integration_time_in_year * 365 * 24 * 60 * 60 # Using SI units

temporal_discretization = np.arange(0, integration_time, delta_t)

############ - alpha discretization - ##############

alpha_min = -0.1
alpha_max = 0.1
detla_alpha = 0.0005
alpha_distribution = np.arange(alpha_min, alpha_max, detla_alpha)

############ - Function definition - ##############
def alpha_critique(lamb, CO_2_multiplication):
	"""
		Give the value of alpha wher sqrt(lamb**2 - 4 * alpha * F) doesn't exist -> runaway warming.
	"""
	F = np.log2(CO_2_multiplication)*3.71
	return (lamb**2)/(4*F)

def delta_T_next_time_step(CO2_multiplication, lamb, alpha, delta_T):
    # return the next time step with Euler Forward method.
    F = np.log2(CO2_multiplication)*3.71
    return (delta_t/C) * (F + lamb * delta_T + alpha * delta_T**2) + delta_T
    



################# - Simulation - #####################

T_2a_1_tot = []
T_2a_2_tot = []
T_2a_3_tot = []

T_2b_1_tot = []
T_2b_2_tot = []
T_2b_3_tot = []

for alpha in alpha_distribution:
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
    T_2a_1_tot.append(T_2a_1)
    T_2a_2_tot.append(T_2a_2)
    T_2a_3_tot.append(T_2a_3)

    T_2b_1_tot.append(T_2b_1)
    T_2b_2_tot.append(T_2b_2)
    T_2b_3_tot.append(T_2b_3)



################## - Animation 1 - #####################
fig = plt.figure()
a_1, = plt.plot([],[], label = 'lambda = {}'.format(lamb_2ab_1))
a_2, = plt.plot([],[], label = 'lambda = {}'.format(lamb_2ab_2))
a_3, = plt.plot([],[], label = 'lambda = {}'.format(lamb_2ab_3))


plt.xlim(0, integration_time_in_year)
plt.ylim(0,12)
plt.xlabel('time in year')
plt.ylabel('delta_T in °K')
plt.legend()
plt.grid()
def init():
    a_1.set_data([],[])
    a_2.set_data([],[])
    a_3.set_data([],[])
    return a_1, a_2, a_3

def animate(i):
    a_1.set_data(temporal_discretization/31536000, T_2a_1_tot[i])
    a_2.set_data(temporal_discretization/31536000, T_2a_2_tot[i])
    a_3.set_data(temporal_discretization/31536000, T_2a_3_tot[i])
    plt.title('CO_2 x 2, alpha = {}'.format(round(alpha_distribution[i],2)))
    return a_1, a_2, a_3


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(alpha_distribution),blit = False ,interval=20, repeat=True)
plt.show()
"""
#uncomment to save
Writer = writers['ffmpeg']
writer = Writer(fps=5, metadata={'artist': 'Me'}, bitrate=-1)
name_file = 'alpha_dyn_co2x2'
ani.save('alpha_dyn_co2x2.mp4', writer)"""

##################### - Animation 2 - ####################

fig = plt.figure()
b_1, = plt.plot([],[], label = 'lambda = {}'.format(lamb_2ab_1))
b_2, = plt.plot([],[], label = 'lambda = {}'.format(lamb_2ab_2))
b_3, = plt.plot([],[], label = 'lambda = {}'.format(lamb_2ab_3))


plt.xlim(0,integration_time_in_year)
plt.ylim(0,12)
plt.xlabel('time in year')
plt.ylabel('delta_T in °K')
plt.legend()
plt.grid()
def init():
    b_1.set_data([],[])
    b_2.set_data([],[])
    b_3.set_data([],[])
    return b_1, b_2, b_3

def animate(i):
    b_1.set_data(temporal_discretization/31536000, T_2b_1_tot[i])
    b_2.set_data(temporal_discretization/31536000, T_2b_2_tot[i])
    b_3.set_data(temporal_discretization/31536000, T_2b_3_tot[i])
    plt.title('CO_2 x 4, alpha = {}'.format(round(alpha_distribution[i],2)))
    return b_1, b_2, b_3

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(alpha_distribution),blit = False ,interval=20, repeat=True)

plt.show()
"""
#uncomment to save
Writer = writers['ffmpeg']
writer = Writer(fps=5, metadata={'artist': 'Me'}, bitrate=-1)
name_file = 'alpha_dyn_co2x4'
ani.save('alpha_dyn_co2x4.mp4', writer)
"""

