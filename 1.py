# Euler's Method to approximate y' = -y + t*sqrt(y) on [0,1] with 4 steps

import numpy as np
import matplotlib.pyplot as plt

# our function f in the ODE y' = f(t,y)
def f(t,y):
    return (1 + t)/(1 + y)

# exact solution
def g(t):
    return np.sqrt(t**2 + 2*t + 6) - 1

# the interval of approximation
a = 1
b = 2

# initial data
y = 2
t = a

# steps and step size
n = 10
h = (b-a)/n

# max error function
MY = 5/27
L = 2/9
def ME(t):
    return (h*MY/(2*L))*(np.exp(L*(t - a)) - 1)

# Euler's Method
W = [y]
k = 0
K = [k]
Y = [y]
E = [0]
M = [0]
T = [a]

for i in range(n):
    m = f(t,y)
    t = t + h
    y = y + m*h
    k = k + 1
    T.append(t)
    W.append(y)
    K.append(k)
    Y.append(g(t))
    E.append(abs(y-g(t)))
    M.append(ME(t))

print("\n\t n\tw_n \t\ty(t_n)\t\terror\t\terror bound")
print("\t--------------------------------------------------------------------\n")
for i in range(len(W)):
    print("\t %d"%K[i],"\t%0.6f"%W[i],"\t%0.6f"%Y[i],"\t%0.6f"%E[i],"\t%0.6f"%M[i])

# create the PL interpolation function
def PL(s):
    for i in range(n):
        aa = T[i]
        bb = T[i+1]
        if (aa <= s) and (s < bb):
            return (-1/h)*W[i]*(s-bb)+W[i+1]*(s-aa)/h
        elif s==T[n]:
            return W[n]
        
# Plot x(t) against PL(t)

# Create the list Z of y-values of PL(t)
t = np.linspace(2,3)
Z = []
for i in range(len(t)):
   Z.append(PL(t[i]))

# Plot them   
WW = np.linspace(2,3,n+1)
B, BX = plt.subplots()
B1 = BX.plot(t,g(t),color="k",linewidth=1)
B2 = BX.plot(t,Z,color="r",linewidth=1)
BX.legend(("y(t) = (t-2+sqrt(2)e^(1 - t/2))^2\nthe exact solution","PL(t) = the PL Euler\napproximation function"))
BX.set_title("Plot of y(t) against PL(t).")
BX.set_xlim(1.9,3.1)
BX.set_ylim(1.5,3.5)
plt.axvline(color="k",linewidth=1)
plt.axhline(color="k",linewidth=1)
B3 = BX.plot(WW,W,'o',color="b")
plt.show()
