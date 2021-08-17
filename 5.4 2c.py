import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return -y + t*(y**(1/2))

def g(t):
    return (t - 2 + np.sqrt(2)*np.e*np.exp(-t/2))**2

#def ME(t):
    #return

a = 2
b = 3

h = 0.25
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

for i in range(int((b-a)/h)):
    m = f(t,w)
    t = t + h
    w = w + (h/2)*(m + f(t, w + h*m))
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

