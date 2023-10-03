import numpy as np
import scipy
import black
import math
import matplotlib.pyplot as plt 


m = float(input("Please enter the mass of the oscillator = "))
k = float(input("Please enter the spring constant of the oscillator = ")) 
b = float(input("Please enter coefficient of damping = ")) 

x_0 = float(input("Please enter the position at initial time (t = 0) = "))
v_0 = float(input("Please enter the velocity at initial time (t = 0) = ")) 

#ODE: D^2 x + 2\beta Dx + \omega^2 x = 0, \beta = a and \omega = w
a = round(b/(2*m), 2)
w = round(math.sqrt(k/m), 2)

h = 0.001 # Step size
t = np.arange(0, 10 + h, h)

print(a)
print(w)  

#creating two one dimensional arrays, x and v
x = [x_0]
 
v = [v_0]

#Declaring other three arrays, potential energy, kinetic energy and total energy
P_E_e = []
K_E_e = []
Total_energy_e = [] 


#Two first order equations for this ODE are:
#x' = v
#v' = f(x, v) = -2 beta v - omega^2 x



def f(x, v):
    return (-2*a*v -w**2 * x) 
    
    
#This function takes initial values 
#of x and v, step size and then calculate position and
#velocity at the next time by calculating the weights     
    
    
    
def euler(x, v, h):
    for i in range(0, len(t) - 1):
        x.append(x[i] + v[i]*h)
        v.append(v[i] + f(x[i],v[i])*h) 
    

    #plt.plot(t,x,label="Euler's method")
    #plt.grid() 
    #plt.show() 
    return(x, v)
    
   
#This function takes the position 
#and velocity array as inputs and 
#return potential and kinetic energy
#arrays
  

def energy_euler(x, v):
    for i in range(0, len(t)):
        P_E_e.append((k * x[i]**2)/2) 
        K_E_e.append((m*v[i]**2)/2)
    return(P_E_e, K_E_e)
    
 

#This function calculates total 
#energy using euler's method at each instant of time
#and returns the modified total_energy
#array


def tot_euler(pe, ke):
    for i in range(0, len(t)):
        Total_energy_e.append(pe[i] + ke[i])
    #plt.plot(t,Total_energy_e)
    #plt.show()
    return(Total_energy_e)
        
 
 

