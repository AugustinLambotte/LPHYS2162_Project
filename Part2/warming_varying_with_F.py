import numpy as np
import matplotlib.pyplot as plt

"""
    This code plot the steady state warming dependance on the forcing and the time the system take to reach this steady state.
"""

############## - Parameters - ##############
alpha = 0.058
lamb = -0.88
beta = -4*10**(-6)
C = 8.36 * 10 ** 8 

############## - Function definition - ##################
def delta_T_next_time_step(F, lamb, alpha, beta, delta_T):
    # return the next time step with Euler Forward method.
    return (time_increment/C) * (F + lamb * delta_T + alpha * delta_T**2 + beta * delta_T**5) + delta_T

############ - Discretization of Forcing and time - ############

F_min = 0
F_max = 15
F_discretization = np.arange(F_min,F_max,0.01)

integration_time_in_year = 25000
time_increment_in_year = 0.1

integration_time = integration_time_in_year * 365 * 24 * 60 * 60 #SI
time_increment = time_increment_in_year * 365 * 24 * 60 * 60 #SI

time_discretization = np.arange(0,integration_time,time_increment)

################# - Simulation - ###################

time_to_steady_state = []
delta_T_steady_state = []

for F in F_discretization:
    Delta_T = []
    for t in time_discretization:
        if t == 0:
            Delta_T.append(0)
        else:
            Delta_T.append(delta_T_next_time_step(F,lamb,alpha,beta, Delta_T[-1]))
            if (Delta_T[-1] - Delta_T[-2]) <= 0.0001:
                time_to_steady_state.append(t/31536000)
                delta_T_steady_state.append(Delta_T[-1])
                break
            if t == time_discretization[-1]: #Only usefull if steady state unreached
                time_to_steady_state.append(0)
fig,ax = plt.subplots()
ax.plot(F_discretization,time_to_steady_state)
ax.set_xlabel('F (W/m^2)')
ax.set_ylabel('Convergence time (y)', color = 'blue', fontsize = 12)
ax2 = ax.twinx()
ax2.plot(F_discretization,delta_T_steady_state, color = "red")
ax2.set_ylabel('Delta T steady state (K)', color = 'red', fontsize = 12)
plt.grid()
plt.show()
