import math
#import numpy as np

# define the functions
def f_a(x):
    return (x-2)**2 - math.log(x)
def f_a_prime(x):
    return 2*(x-2) - 1/x

p0 = 1.5
e = 10**(-4) # tolerance
N0 = 41 
i = 1

while i <= N0:

    p = p0 - f_a(p0)/f_a_prime(p0)
    
    if abs(p-p0) < e:
        print("p = ",p," after ", i, " iterations.") #successful
        break
    
    i=i+1
    
    p0 = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")
