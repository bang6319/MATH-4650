# define the function
def g(x):
    return 2**(-x)

p0 = 1
e = 10**(-4) # tolerance
N0 = 41 
n = 1

while n <= N0:
    
    p = g(p0)
    
    if abs(p-p0) < e:
        print("p = ",p," after ", n, " iterations.") #successful
        break
    
    n=n+1
    
    p0=p
    
if (n > N0):
    print("The method failed after ", n, " iterations.:")
