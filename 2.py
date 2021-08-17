import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return (1 + t)/(1 + y)

def g(t):
    return np.sqrt(t**2 + 2*t + 6) - 1

#def ME(t):
    #return

a = 1
b = 2

n = 10
h = (b-a)/n
t = a

w = 2
i = 0

W = [w]
k = 0
K = [k]
X = [w]
E = [0]
M = [0]
T = [0]

for i in range(n):
    m = f(t + h/2,w + (h/2)*f(t,w))
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

