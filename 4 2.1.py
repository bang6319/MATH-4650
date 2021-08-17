# define the function
def f(x):
    return x**4 - 2*(x**3) - 4*(x**2) + 4*x + 4

a1 = -2
a2 = -1
e = 10**(-2) # tolerance
N0 = 41
i = 1
FA = f(a1)

while i <= N0:
    
    p = a1 + (a2-a1)/2
    FP = f(p)
    
    if (FP == 0 or (a2-a1)/2 < e): #then we're done
        print("a) p = ",p," after ", i, " iterations.")
        break 
    
    i=i+1
    
    if (f(p)*f(a1) > 0): # if f(p) and f(a) have the same sign
        a1 = p
        FA = FP
    else: #if f(p) and f(a) have opposite signs
        a2 = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")

b1 = 0
b2 = 2
e = 10**(-2) # tolerance
N0 = 41
i = 1
FA = f(b1)

while i <= N0:
    
    p = b1 + (b2-b1)/2
    FP = f(p)
    
    if (FP == 0 or (b2-b1)/2 < e): #then we're done
        print("b) p = ",p," after ", i, " iterations.")
        break 
    
    i=i+1
    
    if (f(p)*f(b1) > 0): # if f(p) and f(a) have the same sign
        b1 = p
        FA = FP
    else: #if f(p) and f(a) have opposite signs
        b2 = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")

c1 = 2
c2 = 3
e = 10**(-2) # tolerance
N0 = 41
i = 1
FA = f(c1)

while i <= N0:
    
    p = c1 + (c2-c1)/2
    FP = f(p)
    
    if (FP == 0 or (c2-c1)/2 < e): #then we're done
        print("c) p = ",p," after ", i, " iterations.")
        break 
    
    i=i+1
    
    if (f(p)*f(c1) > 0): # if f(p) and f(a) have the same sign
        c1 = p
        FA = FP
    else: #if f(p) and f(a) have opposite signs
        c2 = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")

d1 = -1
d2 = 0
e = 10**(-2) # tolerance
N0 = 41
i = 1
FA = f(d1)

while i <= N0:
    
    p = d1 + (d2-d1)/2
    FP = f(p)
    
    if (FP == 0 or (d2-d1)/2 < e): #then we're done
        print("d) p = ",p," after ", i, " iterations.")
        break 
    
    i=i+1
    
    if (f(p)*f(d1) > 0): # if f(p) and f(a) have the same sign
        d1 = p
        FA = FP
    else: #if f(p) and f(a) have opposite signs
        d2 = p
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")
