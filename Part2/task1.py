import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.signal import argrelextrema
"""
    Plotting of potential function for different forcing values and a 5th power dependance in delta_t
"""
################### - Simulation parameters - ######################
T_ref = 287
C = 8.36 * 10 ** 8 

alpha = 0.058
lamb = -0.88
beta = -4*10**(-6)

T_min = 282
T_max = 307
Temperature_incrementation = 0.01
Temperature_discretization = np.arange(T_min, T_max, Temperature_incrementation)

F_1 = 0
F_2 = 2
F_3 = 3.1
F_4 = 3.3
F_5 = 3.5
F_6 = 3.6

################### - Function definitions - #######################


def potential(F, lamb, alpha, beta, T_integration):
    #Return the potential of the system for a given temperature T_integration, the return is in K^2/year so we mult by the number of second in a year.
    def integrant(T):
        delta_T = T - T_ref
        return  (-1/C)*(F + lamb * delta_T + alpha * delta_T**2 + beta * delta_T**5)
    return 31536000 * integrate.quad(integrant, 0, T_integration)[0]

###################### - Simulation - #######################
Potential_quad_1 = []
Potential_quad_2 = []
Potential_quad_3 = []
Potential_quad_4 = []
Potential_quad_5 = []
Potential_quad_6 = []

Potential_1 = []
Potential_2 = []
Potential_3 = []
Potential_4 = []
Potential_5 = []
Potential_6 = []
for T in Temperature_discretization:
    Potential_1.append(potential(F_1, lamb, alpha, beta, T))
    Potential_2.append(potential(F_2, lamb, alpha, beta, T))
    Potential_3.append(potential(F_3, lamb, alpha, beta, T))
    Potential_4.append(potential(F_4, lamb, alpha, beta, T))
    Potential_5.append(potential(F_5, lamb, alpha, beta, T))
    Potential_6.append(potential(F_6, lamb, alpha, beta, T))

    Potential_quad_1.append(potential(F_1, lamb, alpha, 0, T))
    Potential_quad_2.append(potential(F_2, lamb, alpha, 0, T))
    Potential_quad_3.append(potential(F_3, lamb, alpha, 0, T))
    Potential_quad_4.append(potential(F_4, lamb, alpha, 0, T))
    Potential_quad_5.append(potential(F_5, lamb, alpha, 0, T))
    Potential_quad_6.append(potential(F_6, lamb, alpha, 0, T))

Delta_T_1 = round(Temperature_discretization[argrelextrema(np.array(Potential_1),np.less)[0][0]] - T_ref,1)
Delta_T_2 = round(Temperature_discretization[argrelextrema(np.array(Potential_2),np.less)[0][0]] - T_ref,1)
Delta_T_3 = round(Temperature_discretization[argrelextrema(np.array(Potential_3),np.less)[0][0]] - T_ref,1)
Delta_T_4 = round(Temperature_discretization[argrelextrema(np.array(Potential_4),np.less)[0][0]] - T_ref,1)
Delta_T_5 = round(Temperature_discretization[argrelextrema(np.array(Potential_5),np.less)[0][0]] - T_ref,1)
Delta_T_6 = round(Temperature_discretization[argrelextrema(np.array(Potential_6),np.less)[0][0]] - T_ref,1)

Delta_T_quad_1 = round(Temperature_discretization[argrelextrema(np.array(Potential_quad_1),np.less)[0][0]] - T_ref,1)
Delta_T_quad_2 = round(Temperature_discretization[argrelextrema(np.array(Potential_quad_2),np.less)[0][0]] - T_ref,1)
Delta_T_quad_3 = round(Temperature_discretization[argrelextrema(np.array(Potential_quad_3),np.less)[0][0]] - T_ref,1)
Delta_T_quad_4 = round(Temperature_discretization[argrelextrema(np.array(Potential_quad_4),np.less)[0][0]] - T_ref,1)

#Plotting potential


plt.subplot(2,3,1)
plt.plot(Temperature_discretization, Potential_1)
plt.title('F = {} W/m^2, Delta_t = {}K'.format(F_1,Delta_T_1))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.subplot(2,3,2)
plt.plot(Temperature_discretization,Potential_2)
plt.title('F = {} W/m^2, Delta_t = {}K'.format(F_2,Delta_T_2))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.subplot(2,3,3)
plt.plot(Temperature_discretization,Potential_3)
plt.title('F = {} W/m^2, Delta_t = {}K'.format(F_3,Delta_T_3))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.subplot(2,3,4)
plt.plot(Temperature_discretization,Potential_4)
plt.title('F = {} W/m^2, Delta_t = {}K'.format(F_4,Delta_T_4))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.subplot(2,3,5)
plt.plot(Temperature_discretization,Potential_5)
plt.title('F = {} W/m^2, Delta_t = {}K'.format(F_5,Delta_T_5))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.subplot(2,3,6)
plt.plot(Temperature_discretization,Potential_6)
plt.title('F = {} W/m^2, Delta_t = {}K'.format(F_6,Delta_T_6))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.show()

#Plotting potential for quadratic dependance

plt.subplot(2,3,1)
plt.plot(Temperature_discretization,Potential_quad_1)
plt.title('F = {} W/m^2, Delta_t = {}K'.format(F_1,Delta_T_quad_1))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.subplot(2,3,2)
plt.plot(Temperature_discretization,Potential_quad_2)
plt.title('F = {} W/m^2, Delta_t = {}K'.format(F_2,Delta_T_quad_2))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.subplot(2,3,3)
plt.plot(Temperature_discretization,Potential_quad_3)
plt.title('F = {} W/m^2, Delta_t = {}K'.format(F_3,Delta_T_quad_3))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.subplot(2,3,4)
plt.plot(Temperature_discretization,Potential_quad_4)
plt.title('F = {} W/m^2, Delta_t = {}K'.format(F_4,Delta_T_quad_4))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.subplot(2,3,5)
plt.plot(Temperature_discretization,Potential_quad_5)
plt.title('F = {} W/m^2, runaway warming'.format(F_5))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.subplot(2,3,6)
plt.plot(Temperature_discretization,Potential_quad_6)
plt.title('F = {} W/m^2, runaway warming'.format(F_6))
plt.ylabel('V (K^2/y)')
plt.xlabel('T(K)')
plt.grid()

plt.show()
