import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return (y/t)**2 + y/t

a = 1
b = 1.2
al = 1 # initial condition
TOL = 10**(-4) # tolerance
hmax = 0.05
hmin = 0.02

t = a
w = al
h = hmax
FLAG = 1

T = [t]
W = [w]
H = [h]

n = 0
N = [n]

while (FLAG == 1):
    
    k1 = h*f(t,w)
    k2 = h*f(t + (1/4)*h,w + (1/4)*k1)
    k3 = h*f(t + (3/8)*h,w + (3/32)*k1 + (9/32)*k2)
    k4 = h*f(t + (12/13)*h,w + (1932/2197)*k1 - (7200/2197)*k2 + (7296/2197)*k3)
    k5 = h*f(t + h,w + (439/216)*k1 - 8*k2 + (3680/513)*k3 - (845/4104)*k4)
    k6 = h*f(t + (1/2)*h,w - (8/27)*k1 + 2*k2 - (3544/2565)*k3 + (1859/4104)*k4 - (11/40)*k5)

    R = (1/h)*abs((1/360)*k1 - (128/4275)*k3 - (2197/75240)*k4 + (1/50)*k5 + (2/55)*k6)

    if R <= TOL:
        t = t + h
        w = w + (25/216)*k1 + (1408/2565)*k3 + (2197/4104)*k4 - (1/5)*k5
        n = n + 1
        T.append(t)
        W.append(w)
        H.append(h)
        N.append(n)
             
    ep = float(0.84*(TOL/R)**(1/4))

    if ep <= 0.1:
        h = 0.1*h
    elif ep >= 4:
        h = 4*h
    else:
        h = ep*h

    if h > hmax:
        h = hmax

    if t >= b:
        FLAG = 0
    elif (t + h) > b:
        h = b - t
    elif h < hmin:
        FLAG = 0

print("\n\t i\tt_i \t\tw_i\t\th_i")
print("\t--------------------------------------------------------------------\n")
for i in range(len(W)):
    print("\t %d"%N[i],"\t%0.6f"%T[i],"\t%0.6f"%W[i],"\t%0.6f"%H[i])

    


