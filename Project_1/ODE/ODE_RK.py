import numpy as np
import scipy
import black
import math
import matplotlib.pyplot as plt 
import ODE_euler


m = ODE_euler.m   #values of these parameters are imported from ODE_euler python module
k = ODE_euler.k
b = ODE_euler.b

a_new = ODE_euler.a
w_new = ODE_euler.w

x_i = ODE_euler.a
v_i = ODE_euler.w 

    
h_1 = ODE_euler.h
t_1 = ODE_euler.t 


s = x_i
vs = v_i 


position = [] 
velocity = []

P_E_r = []
K_E_r = []
Total_energy_r = [] 

#Two first order equations for this ODE are:
#x' = v
#v' = f(x, v) = -2 beta v - omega^2 x


def func(x, v, t): 
    return(ODE_euler.f(x, v)) 
    


#This function takes initial values 
#of x and v, step size and then calculate position and
#velocity at the next time by calculating the weights 


def RK_4(h_1, vs, s, t_1, position, velocity):
    for t in t_1:
        position.append(s)
        velocity.append(vs) 

        m1 = h_1*vs
        k1 = h_1*func(s, vs, t)  #(x, v, t)

        m2 = h_1*(vs + 0.5*k1)
        k2 = h_1*func(s+0.5*m1, vs+0.5*k1, t+0.5*h_1)

        m3 = h_1*(vs + 0.5*k2)
        k3 = h_1*func(s+0.5*m2, vs+0.5*k2, t+0.5*h_1)

        m4 = h_1*(vs + k3)
        k4 = h_1*func(s+m3, vs+k3, t+h_1)

        s += ((m1 + 2*m2 + 2*m3 + m4)/6)
        vs += (k1 + 2*k2 + 2*k3 + k4)/6 
        
    #plt.plot(t_1, position)
    #plt.grid()
    #plt.show()   
    return(position, velocity) 
    
 

#This function calculates total 
#energy using Runge Kutta method at each instant of time
#and returns the modified total_energy
#array

    
def energy_RK(x, v, h_1):
    for i in range(0, len(t_1)):
        P_E_r.append((k * x[i]**2)/2) 
        K_E_r.append((m*v[i]**2)/2)
        Total_energy_r.append(P_E_r[i] + K_E_r[i])
    #plt.plot(t_1, Total_energy_r)
    #plt.show()
    return(P_E_r, K_E_r,Total_energy_r)
    
 

 
 
 
 
        

 

 
