import numpy as np
import matplotlib.pyplot as plt

"""
This code plot how the standard deviation of a range of stochastic evolution is varying with F
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

nb_stochastic_simulation = 200

#Choose over wicch range of forcing we want to see std
F_min = 4
F_max = 15

F_discretization = np.arange(F_min,F_max,0.1)

################ - Temporal discretization - ################
integration_time_in_year = 2000
time_step_in_year = 0.5

integration_time = integration_time_in_year * 365 * 24 * 60 * 60 #SI

time_step = time_step_in_year * 365 * 24 * 60 * 60 #SI

time_discretization = np.arange(0,integration_time,time_step)




################# - Simulation - #######################


standard_deviation = []

for F in F_discretization:
    print(round(F,3),'/',round(F_discretization[-1],3))
    Delta_T_stoch = []
    for i in range(nb_stochastic_simulation):
        current_stocastic_shot = []
        for t in time_discretization:
            if t == 0:
                current_stocastic_shot.append(0)
            else:
                current_stocastic_shot.append(delta_T_next_time_step(F,lamb,alpha,beta, current_stocastic_shot[-1],D))
        Delta_T_stoch.append(current_stocastic_shot)

    Delta_T_stoch = np.array(Delta_T_stoch)

    standard_deviation.append(np.std(Delta_T_stoch[:,-1]))


################ - Plotting results - ##################
plt.plot(F_discretization, standard_deviation, label = 'std for {} simulations'.format(nb_stochastic_simulation))
plt.xlabel('F (W/m^2)')
plt.ylabel('standard deviation (K)')
plt.legend()
plt.grid()
plt.xlim(F_min,F_max)
plt.show()
