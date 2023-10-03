This is a text file to briefly mention the instructions on how to run the code.

Problem - 1: Solve an Ordinary differential equation using Euler's, Runge Kutta 4th order method and external algorithm. 
1. First, we need to run the main_ODE.py file. Then it will call ODE_euler python module to import different values. It will ask for the values of the parameters from the user. In the code, I have mentioned the datatype of these variables. 
After that it will go to the next steps where different arrays are declared and initialised by calling functions from different python modules. 
Then various plots will be generated depending on the values of the parameters. 
Total four python modules (ODE_euler.py, ODE_RK.py, sci_py.py, exact.py) are created and each of them will be imported through main_ODE.py file. Sci_py.py module helps to provide the x(t) vs t plot using external algorithm. 

Problem - 2: Energy stored in an inductor
1. In this case we will first run main_int.py file. This file imports int_all python module. Then the code will ask for the values of the parameters from the user. After inserting the values of the parameters, the code will evaluate the results using different integration methods by importing int_all.py module. Another module sci_int.py helps to do the integration using scipy module of python. 
