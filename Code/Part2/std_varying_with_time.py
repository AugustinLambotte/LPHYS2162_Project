import numpy as np
import matplotlib.pyplot as plt

"""
     This code plots the evolution with time of the std of a given set of stochastics simulations
"""
############## - Function definition - ##################
def delta_T_next_time_step(F, lamb, alpha, beta, delta_T, D):
    # return the next time step with Euler Forward method.
    noise = np.random.normal()
    return ((time_step/C) * (F + lamb * delta_T + alpha * delta_T**2 + beta * delta_T**5) + 
    (D/C) * np.sqrt(time_step) * noise +  delta_T)

############## - Simulation parameter - #################
alpha = 0.058
lamb = -0.88
beta = -4*10**(-6)
C = 8.36 * 10 ** 8 
D = 5753
F = 3.43
nb_stochastic_simulation = 20

############# - Temporal discretization - ################


time_step_in_year = 0.5

time_step = time_step_in_year * 365 * 24 * 60 * 60 #SI
time_discretization = np.arange(0, 50000 * 365 * 24 * 60 * 60, time_step)


################# - Simulation - #######################

standard_deviation = []
mean = []
Delta_T_stoch = []
Delta_T_deterministic = []

for t in time_discretization:
    if t == 0:
        Delta_T_deterministic.append(0)
    else:
        Delta_T_deterministic.append(delta_T_next_time_step(F,lamb,alpha,beta, Delta_T_deterministic[-1],0))

for i in range(nb_stochastic_simulation):
    print(i,'/',nb_stochastic_simulation)
    current_stocastic_current = []
    for t in time_discretization:
        if t == 0:
            current_stocastic_current.append(0)
        else:
            current_stocastic_current.append(delta_T_next_time_step(F,lamb,alpha,beta, current_stocastic_current[-1],D))
    Delta_T_stoch.append(current_stocastic_current)

Delta_T_stoch = np.array(Delta_T_stoch)
for t in range(len(time_discretization)):
    standard_deviation.append(np.std(Delta_T_stoch[:,t]))
    mean.append(np.mean(Delta_T_stoch[:,t]))


################ - Plotting results - ##################

fig,ax = plt.subplots()
ax.plot(time_discretization/31536000,standard_deviation,)
ax.set_xlabel('integration time (y)')
ax.set_ylabel('standard deviation (K)', color = 'blue', fontsize = 12)
ax2 = ax.twinx()
ax2.plot(time_discretization/31536000, mean, color = "red", label = 'Mean value')
ax2.plot(time_discretization/31536000, Delta_T_deterministic, color = "black", label = 'Deterministic')
plt.legend()
ax2.set_ylabel('Delta T (K)', color = 'red', fontsize = 12)
plt.grid()
plt.title('Mean and std over {} simulations'.format(nb_stochastic_simulation))
plt.show()