import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return (2 - 2*t*y)/(t**2 + 1)

def g(t):
    return (2*t + 1)/(t**2 + 1)

#def ME(t):
    #return

a = 0
b = 1

h = 0.1
t = a

w = 1
i = 0

W = [w]
k = 0
K = [k]
X = [w]
E = [0]
M = [0]
T = [0]

for i in range(int((b-a)/h)):
    m = f(t,w)
    t = t + h
    w = w + m*h
    k = k + 1
    T.append(t)
    W.append(w)
    K.append(k)
    X.append(g(t))
    E.append(abs(w-g(t)))
    #M.append(ME(t))

print("\n\t n\tw_n \t\tx(t_n)\t\terror")
print("\t--------------------------------------------------------------------\n")
for i in range(len(W)):
    print("\t %d"%K[i],"\t%0.6f"%W[i],"\t%0.6f"%X[i],"\t%0.6f"%E[i])
