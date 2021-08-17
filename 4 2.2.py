# define the function
def g1(x):
    return x - (x**5-7)/5*x**4

p0 = 1
e = 10**(-2) # tolerance
N0 = 41 
i = 1

while i <= N0:

    # p = Decimal(0)
    
    p = g1(p0)
    
    if abs(p-p0) < e:
        print("p = ",p," after ", i, " iterations.") #successful
        break
    
    i=i+1
    p0 = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")
