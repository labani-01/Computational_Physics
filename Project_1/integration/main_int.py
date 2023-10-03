import numpy as np
import scipy
import black
import math
import matplotlib.pyplot as plt 
import int_all 
import sci_int

ul = int_all.b
ll = int_all.a 
L = int_all.L
n = int_all.n
 

def func(x):
    return (C*int_all.f(x)) 
    
# Calling trapezoidal() method by importing int_all module 

result_1 = int_all.trapezoidal(ll, ul, n) 

# Calling simp_13() method by importing trape int_all module 
result_2 = int_all.simp_13(ll, ul, n) 

# Calling simp_38() method by importing int_all module 
result_3 = int_all.simp_38(ll, ul, n)

# Calling rie_sum() method by importing int_all module
result_4 = int_all.rie_sum(ll, ul, n) 

# Importing sci_int module for doing the integration using external algorithm
result_5 = sci_int.result 

print("Energy (using trapezoidal rule) =  ", result_1)
print("Energy (using simpson's 1/3 rule) =  ", result_2)
print("Energy (using simpson's 3/8 rule) = ", result_3)
print("Energy (using riemann sum rule) =  ", result_4)
print("Energy (using external algorithm) =  ", result_5)
