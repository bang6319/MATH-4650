import math

print("a)")

# define the functions
def f_a(x):
    return math.exp(x) + 2**(-x) + 2*(math.cos(x)) - 6

p0 = 1
p1 = 2
q0 = f_a(p0)
q1 = f_a(p1)
e = 10**(-5) # tolerance
N0 = 41 
i = 1

while i <= N0:

    p = p1 - q1*(p1-p0)/(q1-q0) # compute p_i
    
    if abs(p-p0) < e:
        print("p = ",p," after ", i, " iterations.") #successful
        break
    
    i=i+1

    # update p0, q0, p1, q1
    p0 = p1
    q0 = q1
    p1 = p
    q1 = f_a(p)
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")

print("b)")

# define the functions
def f_e(x):
    return math.exp(x) - 3*(x**2)

p0 = 0
p1 = 1
q0 = f_e(p0)
q1 = f_e(p1)
e = 10**(-5) # tolerance
N0 = 41 
i = 1

while i <= N0:

    p = p1 - q1*(p1-p0)/(q1-q0) # compute p_i
    
    if abs(p-p0) < e:
        print("In [0, 1], p = ",p," after ", i, " iterations.") #successful
        break
    
    i=i+1

    # update p0, q0, p1, q1
    p0 = p1
    q0 = q1
    p1 = p
    q1 = f_e(p)
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")

p0 = 3
p1 = 5
q0 = f_e(p0)
q1 = f_e(p1)
e = 10**(-5) # tolerance
N0 = 41 
i = 1

while i <= N0:

    p = p1 - q1*(p1-p0)/(q1-q0) # compute p_i
    
    if abs(p-p0) < e:
        print("In [0, 1], p = ",p," after ", i, " iterations.") #successful
        break
    
    i=i+1

    # update p0, q0, p1, q1
    p0 = p1
    q0 = q1
    p1 = p
    q1 = f_e(p)
    
if (i > N0):
    print("The method failed after ", i, " iterations.:")
