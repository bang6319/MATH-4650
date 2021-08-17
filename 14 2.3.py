import math

# define the functions
def f(x):
    return -2/(x**3) + 2/(x**2) + 2*x - 4  
def f_prime(x):
    return -4/(x**3) + 6/(x**4) + 2

p0 = 2
e = 10**(-4) # tolerance
N0 = 41 
i = 1

while i <= N0:

    p = p0 - f(p0)/f_prime(p0)
    
    if abs(p-p0) < e:
        print("p = ",p," after ", i, " iterations.") #successful
        break
    
    i=i+1
    
    p0 = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")
