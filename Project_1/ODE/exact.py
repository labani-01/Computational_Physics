import numpy as np
import scipy
import black
import math
import matplotlib.pyplot as plt 
import ODE_euler 

"""
In this module we will 
write the functional form of x(t) for 
different choice of parameters
"""
m = ODE_euler.m
k = ODE_euler.k
b = ODE_euler.b

x_0 = ODE_euler.x_0
v_0 = ODE_euler.v_0

a = ODE_euler.a
w = ODE_euler.w

h = ODE_euler.h
t = ODE_euler.t

x_t = 0

C_1 = 0 
C_2 = 0 
A = 0 
angle = 0

def exact_ODE(a, w, t):
    if a>w:
        C_1 = (v_0 + x_0*(a + math.sqrt(a**2 - w**2)))/(2*math.sqrt(a**2 - w**2)) 
        C_2 = (- v_0 + x_0*(-a + math.sqrt(a**2 - w**2)))/(2*math.sqrt(a**2 - w**2)) 
        x_t = C_1*np.exp(-a*t + np.sqrt(a**2 - w**2)*t) + C_2*np.exp(-a*t - np.sqrt(a**2 - w**2)*t)
        print("Overdamped Situation") 
        return(x_t) 
    elif a==w:
        x_t = np.exp(-a*t)*(x_0 + v_0*t + a*t*x_0) 
        print("Critically Damped")
        return(x_t)
    else:
        A = math.sqrt((w**2 * x_0**2 + v_0**2 + 2*v_0*x_0*a)/(w**2 - a**2))
        angle = np.arctan((v_0 + a*x_0)/(x_0*np.sqrt(w**2 - a**2))) 
        x_t = A*np.exp(-a*t)*np.cos(math.sqrt(w**2 - a**2)*t - angle)
        print("Underdamped Situation") 
        return(x_t)
    
     
#x_t = exact_ODE(a, w, t) 
#plt.plot(t, x_t)
#plt.show()
        
    
