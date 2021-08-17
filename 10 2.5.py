import math

# define the functions
def g(x):
   return 5/math.sqrt(x)

p0 = 3
e = 10**(-4) # tolerance
N0 = 41 
i = 1

print('\n Steffensen"s Method')
print('\n\n  i           p\n')

while i <= N0:

    p1 = g(p0)
    p2 = g(p1)
    p = p0 - ((p1 - p0)**2)/(p2-2*p1+p0)

    print(' ',i,'  ',   p)

    
    if abs(p-p0) < e:
       #  print("p = ",p," after ", i, " iterations.") #successful
        break
    
    i=i+1
    
    p0 = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")
