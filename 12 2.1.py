# consider f(x) = x^2 - 3 to approximate sqrt(3)
def f(x):
    return x**2 - 3

# we choose a = 1 and b = 2 since 1^2 - 3 = -2 < 0 and 2^2 - 3 = 1 > 0
a = 1
b = 2
e = 10**(-4) # tolerance
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
