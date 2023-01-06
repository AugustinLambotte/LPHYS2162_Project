import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import matplotlib.animation as animation

"""
    This code give an animation of the five order system transient behaviour varying with the forcing
"""

############### - Simulation parameters - ###########

alpha = 0.058
lamb = -0.88
beta = -4*10**(-6)
C = 8.36 * 10 ** 8 

############ - Discretization of Forcing and time - ############

F_min = 3.4
F_max = 3.6

F_discretization = np.arange(F_min,F_max,0.001)

integration_time_in_year = 6000
time_increment_in_year = 0.5

integration_time = integration_time_in_year * 365 * 24 * 60 * 60 #SI
time_increment = time_increment_in_year * 365 * 24 * 60 * 60 #SI

time_discretization = np.arange(0,integration_time,time_increment)

############ - Function definition - ##############

def delta_T_next_time_step(F, lamb, alpha, beta, delta_T):
    # return the next time step with Euler Forward method.
    return (time_increment/C) * (F + lamb * delta_T + alpha * delta_T**2 + beta * delta_T**5) + delta_T


################# - Simulation - #####################

Time_evolution = []
time_to_steady_state = []
delta_T_steady_state = []

for F in F_discretization:
    print(round(F,2),'/',round(F_discretization[-1],1))
    Delta_T = []
    steady_state_reach = 0 #control variable to don't overcount the steady state temp and time
    for t in time_discretization:
        if t == 0:
            Delta_T.append(0)
        else:
            Delta_T.append(delta_T_next_time_step(F,lamb,alpha,beta, Delta_T[-1]))

            #The following two conditionnal are to record when and where the systeme reached a steady state
            if (Delta_T[-1] - Delta_T[-2]) <= 0.00001 and steady_state_reach == 0:
                time_to_steady_state.append(round(t/31536000,1))
                delta_T_steady_state.append(round(Delta_T[-1],1))
                steady_state_reach = 1
            if t == time_discretization[-1] and steady_state_reach == 0: #Only usefull if steady state unreached
                time_to_steady_state.append('not reached in given time')
                delta_T_steady_state.append('not reached in given time')
                steady_state_reach = 1

    Time_evolution.append(Delta_T)


time_discretization /= 31536000 #passing from second to year units

fig = plt.figure()
a_1, = plt.plot([],[])


plt.xlabel('time (year)')
plt.ylabel('delta T (k)')
plt.xlim(0, integration_time/31536000)
plt.ylim(-1,25 )
plt.grid()
def init():
    a_1.set_data([],[])
    return a_1

def animate(i):
    a_1.set_data(time_discretization, Time_evolution[i])

    plt.title('F ={} W/m^2, time to reach steady state = {}y, warming at steady state = {}K'.format(round(F_discretization[i],2),
    time_to_steady_state[i], delta_T_steady_state[i]))

    return a_1

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(F_discretization),blit = False ,interval=300, repeat=True)
plt.show()

"""
#uncomment to save
Writer = writers['ffmpeg']
writer = Writer(fps=5, metadata={'artist': 'Me'}, bitrate=-1)
name_file = 'test'
ani.save('test.mp4', writer)
"""