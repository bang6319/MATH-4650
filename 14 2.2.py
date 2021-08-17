import math

# define the function
def g(x):
    return x + 1/(math.tan(x)) - 1/x

p0 = 4
e = 10**(-4) # tolerance
N0 = 41 
i = 1

while i <= N0:
    
    p = g(p0)
    
    if abs(p-p0) < e:
        print("p = ",p," after ", i, " iterations.") #successful
        break
    
    i=i+1
    
    p0=p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")
