import math
#import numpy as np

# define the functions
def f_a(x):
    return math.exp(x) + 2**(-x) + 2*(math.cos(x)) - 6 
def f_a_prime(x):
    return math.exp(x) - (math.log(2))*(2**(-x)) - 2*(math.sin(x))

p0 = 1.5
e = 10**(-5) # tolerance
N0 = 41 
i = 1

print("a)")

while i <= N0:

    p = p0 - f_a(p0)/f_a_prime(p0)
    
    if abs(p-p0) < e:
        print("p = ",p," after ", i, " iterations.") #successful
        break
    
    i=i+1
    
    p0 = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")

# define the functions
def f_e(x):
    return math.exp(x) - 3*(x**2)
def f_e_prime(x):
    return math.exp(x) - 6*x

p1 = 0.5
e = 10**(-5) # tolerance
N0 = 41 
i = 1

print("b)")

while i <= N0:

    p = p1 - f_e(p1)/f_e_prime(p1)
    
    if abs(p-p1) < e:
        print("In [0, 1], p = ",p," after ", i, " iterations.") #successful
        break
    
    i=i+1
    
    p1 = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")

p2 = 4
e = 10**(-5) # tolerance
N0 = 41 
i = 1

while i <= N0:

    p = p2 - f_e(p2)/f_e_prime(p2)
    
    if abs(p-p2) < e:
        print("In [3, 5], p = ",p," after ", i, " iterations.") #successful
        break
    
    i=i+1
    
    p2 = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")

