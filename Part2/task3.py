import numpy as np
import matplotlib.pyplot as plt

"""
    This code plots the evolution with time of a set of stocastic simulation and give the pdf of the final temperature rise.
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
F = 4

nb_stochastic_simulation = 500

############# - Temporal discretization - ################

integration_time_in_year = 1000
time_step_in_year = 0.5

integration_time = integration_time_in_year * 365 * 24 * 60 * 60 #SI
time_step = time_step_in_year * 365 * 24 * 60 * 60 #SI

time_discretization = np.arange(0,integration_time,time_step)

################# - Simulation - #######################
Delta_T_stoch = []
Delta_T_mean = []
Delta_T = []

for t in time_discretization:
        if t == 0:
            Delta_T.append(0)
        else:
            Delta_T.append(delta_T_next_time_step(F,lamb,alpha,beta, Delta_T[-1],0))
for i in range(nb_stochastic_simulation):
    current_stocastic_shot = []
    for t in time_discretization:
        if t == 0:
            current_stocastic_shot.append(0)
        else:
            current_stocastic_shot.append(delta_T_next_time_step(F,lamb,alpha,beta, current_stocastic_shot[-1],D))
    Delta_T_stoch.append(current_stocastic_shot)

Delta_T_stoch = np.array(Delta_T_stoch)

for t in range(len(time_discretization)):
    Delta_T_mean.append(np.mean(Delta_T_stoch[:,t]))

standard_deviation = np.std(Delta_T_stoch[:,-1])


################ - Plotting results - ##################
plt.subplot(2,1,1)
plt.title('Number of stochastic simulation = {}'.format(nb_stochastic_simulation))
for i in range(nb_stochastic_simulation):
    plt.plot(time_discretization/31536000, Delta_T_stoch[i], color = 'blue')
plt.plot(time_discretization/31536000, Delta_T, color = 'black', label = 'Deterministic, delta T = {}K'.format(round(Delta_T[-1],1)))
plt.plot(time_discretization/31536000, Delta_T_mean, color = 'red', label = 'Mean, delta T = {}K'.format(round(Delta_T_mean[-1],1)))
plt.ylabel('Delta T (K)')
plt.xlabel('Time (y)')
plt.legend()
plt.grid()

plt.subplot(2,1,2)
hist = []
for i in range(nb_stochastic_simulation):
    hist.append(Delta_T_stoch[i][-1])
plt.hist(hist, bins = 50,label = 'standard deviation ={}'.format(round(standard_deviation,2)))
plt.xlabel('Delta T (K)')
plt.legend()
plt.show()