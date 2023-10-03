import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt 
import ODE_euler
from scipy.integrate import odeint

a_new = ODE_euler.a #values of the parameters are imported from ODE_euler python module
w_new = ODE_euler.w

x_i = ODE_euler.a
v_i = ODE_euler.w 
h = ODE_euler.h
t = ODE_euler.t 


def func(vx, t):

#This function takes a 2D array vx 
#whose 1st column is for position 
#and 2nd column is for velocity

#It returns slopes dv/dt and dx/dt

    v = vx[0] 
    x = vx[1]
    dvdt = ODE_euler.f(x, v)
    dxdt = v
    return np.array([dvdt, dxdt]) 
    
def sci_func(v_i, x_i, t, func):
    vx0 = np.array([v_i, x_i])
    vx = odeint(func, vx0, t)
    v = vx[:,0]
    x = vx[:,1] 
    return (v, x)
    
 
