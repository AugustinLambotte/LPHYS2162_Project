import numpy as np
import matplotlib.pyplot as plt

"""
    This code plots the transient behaviour of 6 scenarios under 6 differents forcing
"""
############## - Function definition - ##################
def delta_T_next_time_step(F, lamb, alpha, beta, delta_T):
    # return the next time step with Euler Forward method.
    return (time_step/C) * (F + lamb * delta_T + alpha * delta_T**2 + beta * delta_T**5) + delta_T

############## - Simulation parameter - #################
alpha = 0.058
lamb = -0.88
beta = -4*10**(-6)
C = 8.36 * 10 ** 8 

F_1 = 0
F_2 = 2
F_3 = 3.1
F_4 = 3.3
F_5 = 3.5
F_6 = 3.6

############# - Temporal discretization - ################

integration_time_in_year = 3000
time_step_in_year = 0.1

integration_time = integration_time_in_year * 365 * 24 * 60 * 60 #SI
time_step = time_step_in_year * 365 * 24 * 60 * 60 #SI

time_discretization = np.arange(0,integration_time,time_step)

################# - Simulation - #######################
Delta_T_1 = []
Delta_T_2 = []
Delta_T_3 = []
Delta_T_4 = []
Delta_T_5 = []
Delta_T_6 = []
for t in time_discretization:
    if t == 0:
        Delta_T_1.append(0)
        Delta_T_2.append(0)
        Delta_T_3.append(0)
        Delta_T_4.append(0)
        Delta_T_5.append(0)
        Delta_T_6.append(0)
    else:
        Delta_T_1.append(delta_T_next_time_step(F_1,lamb,alpha,beta, Delta_T_1[-1]))
        Delta_T_2.append(delta_T_next_time_step(F_2,lamb,alpha,beta, Delta_T_2[-1]))
        Delta_T_3.append(delta_T_next_time_step(F_3,lamb,alpha,beta, Delta_T_3[-1]))
        Delta_T_4.append(delta_T_next_time_step(F_4,lamb,alpha,beta, Delta_T_4[-1]))
        Delta_T_5.append(delta_T_next_time_step(F_5,lamb,alpha,beta, Delta_T_5[-1]))
        Delta_T_6.append(delta_T_next_time_step(F_6,lamb,alpha,beta, Delta_T_6[-1]))
################ - Plotting results - ##################



plt.subplot(2,3,1)
plt.plot(time_discretization/31536000, Delta_T_1, label = 'F = {}, Delta T = {}'.format(F_1, round(Delta_T_1[-1],1)))
plt.ylabel('Delta T (K)')
plt.xlabel('Time (y)')
plt.grid()
plt.legend()

plt.subplot(2,3,2)
plt.plot(time_discretization/31536000, Delta_T_2, label = 'F = {}, Delta T = {}'.format(F_2, round(Delta_T_2[-1],1)))
plt.ylabel('Delta T (K)')
plt.xlabel('Time (y)')
plt.grid()
plt.legend()

plt.subplot(2,3,3)
plt.plot(time_discretization/31536000, Delta_T_3, label = 'F = {}, Delta T = {}'.format(F_3, round(Delta_T_3[-1],1)))
plt.ylabel('Delta T (K)')
plt.xlabel('Time (y)')
plt.grid()
plt.legend()

plt.subplot(2,3,4)
plt.plot(time_discretization/31536000, Delta_T_4, label = 'F = {}, Delta T = {}'.format(F_4, round(Delta_T_4[-1],1)))
plt.ylabel('Delta T (K)')
plt.xlabel('Time (y)')
plt.grid()
plt.legend()

plt.subplot(2,3,5)
plt.plot(time_discretization/31536000, Delta_T_5, label = 'F = {}, Delta T = {}'.format(F_5, round(Delta_T_5[-1],1)))
plt.ylabel('Delta T (K)')
plt.xlabel('Time (y)')
plt.grid()
plt.legend()

plt.subplot(2,3,6)
plt.plot(time_discretization/31536000, Delta_T_6, label = 'F = {}, Delta T = {}'.format(F_6, round(Delta_T_6[-1],1)))
plt.ylabel('Delta T (K)')
plt.xlabel('Time (y)')
plt.grid()
plt.legend()

plt.show()
