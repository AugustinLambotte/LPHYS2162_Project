import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from matplotlib.animation import FuncAnimation, writers
import matplotlib.animation as animation
from scipy.signal import argrelextrema
"""
    This code Plots potential function for different forcing values and a 5th power dependance in delta_t
"""
################### - Simulation parameters - ######################
T_ref = 287
C = 8.36 * 10 ** 8 

alpha = 0.058
lamb = -0.88
beta = -4*10**(-6)

T_min = 280
T_max = 310
Temperature_incrementation = 0.1
Temperature_discretization = np.arange(T_min, T_max, Temperature_incrementation)

F_discretization = np.arange(0,10,0.005) #The range of F value for wich the potential will be plot

################### - Function definitions - #######################


def potential(F, lamb, alpha, beta, T_integration):
    #Return the potential of the system for a given temperature T_integration, the return is in K^2/year so we mult by the number of second in a year.
    def integrant(T):
        delta_T = T - T_ref
        return  (-1/C)*(F + lamb * delta_T + alpha * delta_T**2 + beta * delta_T**5)
    return 31536000 * integrate.quad(integrant, 0, T_integration)[0]

###################### - Simulation - #######################
Potential_tot = []
for F in F_discretization:
    Potential = []
    for T in Temperature_discretization:
        Potential.append(potential(F, lamb, alpha, beta, T))
    Potential_tot.append(Potential)

d2v = [] #The second derivative of the potential at the steady state
for i in range(len(Potential_tot)): #argrelextrema return the position of an extrema.
    d2v.append(np.gradient(np.gradient(Potential_tot[i]))[argrelextrema(np.array(Potential_tot[i]),np.less)[0][0]])

###################### - Plotting results - ###################""
#Plot d2v
plt.plot(F_discretization,d2v)
plt.grid()
plt.xlabel('F(W/m^2)')
plt.ylabel('second derivative of the potential at the equilibrium point')
plt.show()

#Plotting potential

fig = plt.figure()
a_1, = plt.plot([],[])


plt.xlabel('F (W/m^2')
plt.ylabel('V (K^2/y)')
plt.xlim(T_min,T_max)
def init():
    a_1.set_data([],[])
    return a_1

def animate(i):
    a_1.set_data(Temperature_discretization, Potential_tot[i])
    plt.ylim(np.amin(Potential_tot[i]),np.amax(Potential_tot[i]))

    
    plt.title('F ={} W/m^2'.format(round(F_discretization[i],2)))

    return a_1

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(F_discretization),blit = False ,interval=50, repeat=True)
plt.show()
"""
#uncomment to save.
Writer = writers['ffmpeg']
writer = Writer(fps=5, metadata={'artist': 'Me'}, bitrate=-1)
name_file = 'test'
ani.save('test.mp4', writer)
"""