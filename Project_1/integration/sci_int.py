import numpy as np
import scipy.integrate
import black
import math
import matplotlib.pyplot as plt 
import int_all

ul = int_all.b  #upper limit, lower limit and constant C are imported from the trape.py
ll = int_all.a   
L = int_all.L

def func(x):
    return (L*int_all.f(x)) 
    
    
    
result = scipy.integrate.quad(func, ul, ll) 

 
