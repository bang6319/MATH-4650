import math

# define the function
def f(x):
    return x - math.tan(x)

a = 4
b = 5
e = 10**(-5) # tolerance
N0 = 41
i = 1
FA = f(a)

while i <= N0:
    
    p = a + (b-a)/2
    FP = f(p)
    
    if (FP == 0 or (b-a)/2 < e): #then we're done
        print("p = ",p," after ", i, " iterations.")
        break 
    
    i=i+1
    
    if (f(p)*f(a) > 0): # if f(p) and f(a) have the same sign
        a = p
        FA = FP
    else: #if f(p) and f(a) have opposite signs
        b = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")
