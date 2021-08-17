import math

# define the functions
def f(x):
    return 1 - 4*x*math.cos(x) + 2*(x**2) + math.cos(2*x)  
def f_prime(x):
    return -2*math.sin(2*x) + 4*x*math.sin(x) - 4*math.cos(x) + 4*x

p0 = 0.5
e = 10**(-5) # tolerance
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
