import numpy as np
import scipy
import black
import math
import matplotlib.pyplot as plt 
import ODE_euler
import ODE_RK 
import exact
from scipy.integrate import odeint
import sci_py 


m = ODE_euler.m
k = ODE_euler.k
b = ODE_euler.b

x_0 = ODE_euler.x_0
v_0 = ODE_euler.v_0

a = ODE_euler.a
w = ODE_euler.w

h = ODE_euler.h
t = ODE_euler.t 

A_1 = exact.C_1
A_2 = exact.C_2 
B = exact.A
delta = exact.angle

x_e = [x_0]
v_e = [v_0] 

x_r = []
v_r = []  


#ODE: D^2 x + 2 beta Dx + omega x = 0, initial conditions: x(0) = 1, v(0) = 0
#1. For different values of the parameter showing x(t) vs t plot
#2. Analyzing the conservation of energy when damping is zero. 


#position and velocities are imported from different python modules for different functions
x_euler, v_euler = ODE_euler.euler(x_e, v_e, h) 
x_RK, v_RK = ODE_RK.RK_4(h, v_0, x_0, t, x_r, v_r)
x_exact = exact.exact_ODE(a, w, t)
v_ext_algo, x_ext_algo = sci_py.sci_func(v_0, x_0, t, sci_py.func)



#x(t) vs t plot for both euler and Runge Kutta 4th order method 
#in one plot


plt.plot(t, x_euler, color='k', label = "Euler method")
plt.plot(t,x_RK,color='g', label = "RK_4 method") 
plt.ylabel("x(t)")
plt.xlabel("t") 
plt.grid
plt.legend(loc='upper center')
plt.show() 


#x(t) vs t plot for both euler and Runge Kutta 4th order method 
#in one plot comparing with the exact solution


plt.plot(t, x_euler, color='k', label = "Euler method")
plt.plot(t, x_RK, color='g', label = "RK_4 method") 
plt.plot(t, x_exact, color='m', label = "Exact solution")
plt.ylabel("x(t)")
plt.xlabel("t") 
plt.grid
plt.legend(loc='upper center')
plt.show() 


#x(t) vs t plot for both euler and Runge Kutta 4th order method 
#in one plot comparing with the result from external algorithm

 
plt.plot(t, x_euler, color='k', label = "Euler method")
plt.plot(t, x_RK, color='g', label = "RK_4 method") 
plt.plot(t, x_ext_algo, color='m', label = "External algorithm solution")
plt.ylabel("x(t)")
plt.xlabel("t") 
plt.grid
plt.legend(loc='upper center')
plt.show() 


#Importing energies from different python modules
PE_e, KE_e = ODE_euler.energy_euler(x_euler, v_euler)
Total_energy_e = ODE_euler.tot_euler(PE_e, KE_e)

PE_r, KE_r, Total_energy_r = ODE_RK.energy_RK(x_RK, v_RK, h) 
 


#Potential energy vs t plot for both euler and Runge Kutta 4th order method 
#in one plot  


plt.plot(t, PE_e,  color='k', label = "Euler method") 
plt.plot(t, PE_r,  color='g', label = "RK_4 method") 
plt.ylabel("Potential energy")
plt.xlabel("t") 
plt.grid
plt.legend(loc='upper center')
plt.show()



#Kinetic energy vs t plot for both euler and Runge Kutta 4th order method 
#in one plot  


plt.plot(t, KE_e,  color='k', label = "Euler method") 
plt.plot(t, KE_r,  color='g', label = "RK_4 method") 
plt.ylabel("Kinetic energy")
plt.xlabel("t") 
plt.grid
plt.legend(loc='upper center')
plt.show() 


#Total energy vs t plot for both euler and Runge Kutta 4th order method 
#in one plot  
 

plt.plot(t, Total_energy_e,  color='k', label = "Euler method") 
plt.plot(t, Total_energy_r,  color='g', label = "RK_4 method") 
plt.ylabel("Total energy")
plt.xlabel("t") 
plt.grid
plt.legend(loc='upper center')
plt.show()



