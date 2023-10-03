import numpy as np
import scipy
import black
import math
import matplotlib.pyplot as plt 


a = float(input("Enter lower limit = ")) 
b = float(input("Enter upper limit = ")) 
L = float(input("Enter the value of inductance = ")) 
n = int(input("Enter step size = ")) 
 


 

# Define function to integrate
def f(x):
    return x
    
    



# Implementing trapezoidal method
def trapezoidal(x0, xn, n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    sum_t = f(x0) + f(xn) 
    
    for i in range(1, n):
        k = x0 + i*h
        sum_t = sum_t + 2 * f(k)
    
    # Finding final integration value
    sum_t = L * sum_t * h/2
    
    return sum_t 
    
    
    
    
 
# Implementing Simpson's 1/3 
def simp_13(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    sum_s = f(x0) + f(xn)
    
    for i in range(1, n):
        k = x0 + i*h
        
        if i%2 == 0:
            sum_s = sum_s + 2 * f(k)
        else:
            sum_s = sum_s + 4 * f(k)
    
    # Finding final integration value
    sum_s = L * sum_s * h/3
    
    return sum_s
    
    

# Implementing Simpson's 3/8
def simp_38(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    sum_si = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%3 == 0:
            sum_si = sum_si + 2 * f(k)
        else:
            sum_si = sum_si + 3 * f(k)
    
    # Finding final integration value
    sum_si = 3 * L * sum_si * h / 8
    
    return sum_si
    
 

 
 

#this program approximates the area under the curve using Riemann Sum
def rie_sum(x0, xn, n):
#calculating step size
    h = (xn - x0) / n
    Area = 0
    i = 0
    #Finding sum 
    while (i<=(n+1)):
        Area = f(xn + h*i)*h + Area
        i = i+1 
    return (L * Area)
    
 
 
 

 
 

